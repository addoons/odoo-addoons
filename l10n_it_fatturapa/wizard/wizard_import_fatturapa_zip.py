import base64
from io import BytesIO

from odoo import api, fields, models
from odoo.exceptions import UserError
import zipfile


class WizardImportFatturapaMassive(models.TransientModel):
    _name = "wizard.import.fatturapa.massive"
    _description = "Import E-bill massive"

    file_ids = fields.Many2many('ir.attachment')

    def importFatturaList(self):
        if self.file_ids:
            for zip in self.file_ids:
                zipdata = BytesIO(base64.b64decode(zip.datas))
                myzipfile = zipfile.ZipFile(zipdata)
                for name in myzipfile.namelist():
                    file = myzipfile.read(name)
                    if not name.endswith('.xml') and name.endswith('.p7m'):
                        raise UserError("Il file " + name + " non e' un file XML valido.")
                    # try:
                    self.env['fatturapa.attachment.in'].create({'datas': base64.b64encode(file), 'name': name, 'datas_fname': name})
                    # except Exception as e:
                    #     raise UserError("Il file " + name + " restituisce il seguente errore " + str(e))
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
