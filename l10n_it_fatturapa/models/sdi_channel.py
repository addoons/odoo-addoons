# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)
import requests
from odoo import models, fields, api, _, exceptions
from odoo.addons.base.models.ir_mail_server import extract_rfc2822_addresses

SDI_CHANNELS = [
    ('pec', 'PEC'),
    ('web', 'Web service'),
    ('ftp', 'FTP')
]
SDI_PROVIDER = [
    ('aruba', 'ARUBA'),
    ('credemtel', 'CREDEMTEL')
]


class SdiChannel(models.Model):
    _name = "sdi.channel"
    _description = "Canale SDI"

    name = fields.Char(string='Name', required=True, default=_("PEC"))
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env['res.company']._company_default_get('sdi.channel'))
    pec_server_id = fields.Many2one('ir.mail_server', string='Outgoing PEC server', required=False, domain=[('is_fatturapa_pec', '=', True)])
    fetch_pec_server_id = fields.Many2one('fetchmail.server', string='Incoming PEC server', required=False, domain=[('is_fatturapa_pec', '=', True)])
    email_exchange_system = fields.Char("Exchange System Email Address",  default=lambda self: self.env['ir.config_parameter'].get_param('sdi.pec.first.address'))
    first_invoice_sent = fields.Boolean("First invoice sent", readonly=True)
    channel_type = fields.Selection(selection=SDI_CHANNELS)
    provider = fields.Selection(selection=SDI_PROVIDER)
    web_server_method_address = fields.Char(default='https://ws.fatturazioneelettronica.aruba.it')
    web_server_refresh_token = fields.Char()
    active_web_server = fields.Boolean()
    web_server_address = fields.Char(string='Web server address', default='https://auth.fatturazioneelettronica.aruba.it/auth/signin')
    web_server_login = fields.Char(string='Web server login')
    web_server_password = fields.Char(string='Web server password')
    web_server_token = fields.Char(string='Web server token')
    # campi credemtel
    url = fields.Char(string="URL")
    username = fields.Char(string="Username")
    password = fields.Char()

    def get_default_ws(self):
        """
        Ritorna i webservices (Attivi) da utilizzare
        :return:
        """
        return self.search([('active_web_server', '=', True)])

    def web_auth(self):
        """
        Utilizza le credenziali fornite per ottenere il token
        se e' disponibile il refresh token utilizza questo
        """
        if self.provider == 'aruba':
            header = {'Content-Type': 'application/x-www-form-urlencoded'}
            if not self.web_server_refresh_token:
                data = {
                    'grant_type': 'password',
                    'username': self.web_server_login,
                    'password': self.web_server_password,
                }
            elif self.web_server_refresh_token:
                data = {
                    'grant_type': 'refresh_token',
                    'refresh_token': self.web_server_refresh_token,
                }
            else:
                raise UserWarning(_('Error Aruba Auth'))

            r = requests.post(self.web_server_address, headers=header, data=data).json()
            if 'error' in r:
                if r['error'] == 'invalid_grant':
                    # Il token e' scaduto
                    self.web_server_refresh_token = ''
                    self.web_auth()
            else:
                self.web_server_token = r['access_token']
                self.web_server_refresh_token = r['refresh_token']
        else:
            raise exceptions.UserError(_('Only Aruba Provider is Supported'))

    @api.constrains('pec_server_id')
    def check_pec_server_id(self):
        """
        Validazione solamente se si tratta di un canale PEC
        """
        for channel in self:
            if channel.channel_type == 'pec':
                domain = [('pec_server_id', '=', channel.pec_server_id.id)]
                elements = self.search(domain)
                if len(elements) > 1:
                    raise exceptions.ValidationError(
                        _("The channel %s with pec server %s already exists")
                        % (channel.name, channel.pec_server_id.name))

    @api.constrains('email_exchange_system')
    def check_email_validity(self):
        """
        Validazione solamente se si tratta di un canale PEC
        """
        for channel in self:
            if channel.channel_type == 'pec':
                if not extract_rfc2822_addresses(channel.email_exchange_system):
                    raise exceptions.ValidationError(
                        _("Email %s is not valid")
                        % channel.email_exchange_system)

    @api.constrains('pec_server_id')
    def check_pec_server_id(self):
        for channel in self:
            domain = [('pec_server_id', '=', channel.pec_server_id.id)]
            elements = self.search(domain)
            if len(elements) > 1:
                raise exceptions.ValidationError(
                    _("The channel %s with pec server %s already exists")
                    % (channel.name, channel.pec_server_id.name))

    @api.constrains('email_exchange_system')
    def check_email_validity(self):
        if self.env.context.get('skip_check_email_validity'):
            return
        for channel in self:
            if not extract_rfc2822_addresses(channel.email_exchange_system):
                raise exceptions.ValidationError(
                    _("Email %s is not valid")
                    % channel.email_exchange_system)

    def check_first_pec_sending(self):
        sdi_address = self.env['ir.config_parameter'].get_param(
            'sdi.pec.first.address')
        if not self.first_invoice_sent:
            if self.email_exchange_system != sdi_address:
                raise exceptions.UserError(_(
                    "This is a first sending but SDI address is different "
                    "from %s"
                ) % sdi_address)
        else:
            if not self.email_exchange_system:
                raise exceptions.UserError(_(
                    "SDI PEC address not set. Please update it with the "
                    "address indicated by SDI after the first sending"))

    def update_after_first_pec_sending(self):
        if not self.first_invoice_sent:
            self.first_invoice_sent = True
            self.with_context(
                skip_check_email_validity=True).email_exchange_system = False

