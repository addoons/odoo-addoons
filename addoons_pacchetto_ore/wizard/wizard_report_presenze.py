import datetime
from odoo import models, fields


class TracciatoXlsx(models.AbstractModel):
    _name = 'report.addoons_pacchetto_ore.presenze_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, vendors):

        header = workbook.add_format({'bold': True, 'text_wrap': True, 'border': True, 'border_color': 'black', 'font_name': 'Arial'})
        cell_text = workbook.add_format({'bold': False, 'text_wrap': True, 'font_name': 'Arial'})
        cell_number_empty = workbook.add_format({'bold': False, 'text_wrap': True, 'font_name': 'Arial', 'align': 'right'})
        cell_number_full = workbook.add_format({'bold': False, 'text_wrap': True, 'font_name': 'Arial', 'align': 'right', 'bg_color': '#DCDCDC'})
        cell_total_text = workbook.add_format({'bold': True, 'text_wrap': True, 'font_name': 'Arial'})
        cell_total_number = workbook.add_format({'bold': True, 'text_wrap': True, 'bg_color': 'yellow', 'font_name': 'Arial', 'align': 'right'})

        # Indici delle righe e colonne del foglio
        row = 0
        col = 0

        # Periodo preso come riferimento
        da_data = datetime.datetime.strptime(data['form']['da_data'], '%Y-%m-%d').date()
        a_data = datetime.datetime.strptime(data['form']['a_data'], '%Y-%m-%d').date()

        # Tipi permesso
        dict_tipi_permesso = {}
        arr_tot_ore_ferie_100 = []

        for permesso in self.env['hr.leave.type'].search([], order='id asc'):
            dict_tipi_permesso[permesso.id] = permesso.name

        # Recupero i dipendenti
        dipendenti = self.env['hr.employee'].search([('name', '=', 'Mitchell Admin')])

        for dipendente in dipendenti:

            # Prendo le ore medie giornaliere dall'ananagrafica
            # del dipendente
            ore_giornaliere_da_contratto = dipendente.resource_calendar_id.hours_per_day

            # Per ogni dipendente crea una sheet con l'intestazione
            sheet = workbook.add_worksheet(dipendente.name)
            sheet.write(0, 0, 'Dipendente', header)
            sheet.write(0, 1, 'Data', header)
            sheet.write(0, 2, 'Ore Lavoro', header)
            sheet.write(0, 3, 'Ore Straordinari', header)

            col = 4

            # Creo gli header per le colonne dei permessi e
            # resetto l'array che contiene i totali mensili
            # di ogni permesso
            for header_column_permesso in dict_tipi_permesso.keys():
                sheet.write(0, col, dict_tipi_permesso[header_column_permesso], header)
                arr_tot_ore_ferie_100.append(0)
                col = col + 1

            # Imposto la larghezza delle colonne
            sheet.set_column(0, 0, 16)
            sheet.set_column(1, 1, 10)
            sheet.set_column(2, 3, 14)

            # Larghezza delle colonne dei permessi
            if len(dict_tipi_permesso) > 0:
                sheet.set_column(4, 4 + len(dict_tipi_permesso), 23)

            # Calcolo i giorni di ferie e permessi
            giorni_ferie = self.calcolo_ferie(dipendente.id, da_data, a_data, ore_giornaliere_da_contratto, dict_tipi_permesso)

            # Calcolo le ore lavorate per il periodo selezionato
            # e il dipendente che sto ciclando
            giorni_lav = self.calcolo_ore_lavorate(dipendente.id, da_data, a_data)

            col = 0
            row = 1
            tot_ore_lavorate_100 = 0
            tot_ore_straordinari_100 = 0
            giorni = a_data - da_data

            # Inizio a scorrere giorno per giorno il
            # periodo selezionato

            for giorno in range(giorni.days + 1):

                col = 0
                data_corrente = da_data + datetime.timedelta(days=giorno)

                # Controllo se nella giornata che sto ciclando
                # ci sono delle ore lavorate
                if data_corrente in giorni_lav.keys():
                    ore_lavorate_100 = round(giorni_lav[data_corrente], 2)
                else:
                    ore_lavorate_100 = 0

                # Controllo se nella giornata che sto ciclando
                # ci sono delle ore di ferie o permessi
                arr_ore_ferie_100 = []
                tot_ferie_100_row = 0

                # Ogni volta che cambia giorno imposto a 0
                # il valore di ogni permesso
                for index_permesso in range(len(dict_tipi_permesso)):
                    arr_ore_ferie_100.append(0)

                index_permesso = 0

                if data_corrente in giorni_ferie.keys():

                    for permesso in giorni_ferie[data_corrente].keys():
                        arr_ore_ferie_100[index_permesso] += giorni_ferie[data_corrente][permesso]
                        arr_tot_ore_ferie_100[index_permesso] += giorni_ferie[data_corrente][permesso]
                        tot_ferie_100_row += giorni_ferie[data_corrente][permesso]
                        index_permesso += 1
                else:
                    tot_ferie_100_row = 0

                # Calcolo le ore di straordinario, se nella giornata
                # ci sono delle ore lavorate o di ferie

                ore_straordinari_100 = 0

                if ore_lavorate_100 > 0 or tot_ferie_100_row > 0:
                    ore_straordinari_100 = ore_lavorate_100 + tot_ferie_100_row - ore_giornaliere_da_contratto

                # Calcolo i totali
                tot_ore_lavorate_100 += ore_lavorate_100
                tot_ore_straordinari_100 += ore_straordinari_100

                # Scrivo la row del foglio excel
                sheet.write(row, col, dipendente.name, cell_text)
                sheet.write(row, col + 1, data_corrente.strftime("%d/%m/%Y"), cell_text)
                if ore_lavorate_100 > 0:
                    sheet.write(row, col + 2, self.convert_float_to_HH_MM_format(ore_lavorate_100), cell_number_full)
                else:
                    sheet.write(row, col + 2, self.convert_float_to_HH_MM_format(ore_lavorate_100), cell_number_empty)

                if ore_straordinari_100 > 0:
                    sheet.write(row, col + 3, self.convert_float_to_HH_MM_format(ore_straordinari_100), cell_number_full)
                else:
                    sheet.write(row, col + 3, self.convert_float_to_HH_MM_format(ore_straordinari_100), cell_number_empty)
                # Scrivo le ogni colonna di permesso per la
                # riga che sto ciclando
                for permesso in arr_ore_ferie_100:
                    if permesso > 0:
                        sheet.write(row, col + 4, self.convert_float_to_HH_MM_format(permesso), cell_number_full)
                    else:
                        sheet.write(row, col + 4, self.convert_float_to_HH_MM_format(permesso), cell_number_empty)

                    col += 1

                col = 0
                row += 1

            # Scrivo i totali delle ore e degli straordinari
            sheet.write(row, col, 'Totale', cell_total_text)
            sheet.write(row, col + 2, self.convert_float_to_HH_MM_format(tot_ore_lavorate_100), cell_total_number)
            sheet.write(row, col + 3, self.convert_float_to_HH_MM_format(tot_ore_straordinari_100), cell_total_number)

            # Scrivo i totali delle ferie
            col = 4

            for feria in arr_tot_ore_ferie_100:
                sheet.write(row, col, self.convert_float_to_HH_MM_format(feria), cell_total_number)
                col += 1

    def convert_float_to_HH_MM_format(self, ore_100):

        """
        Passate le ore in centesimi restituisce una stringa
        con formato HH:MM

        :param ore_100:
        :return:
        """

        return "%02d:%02d" % (int(ore_100), (ore_100 - int(ore_100)) * 60)

    def calcolo_ferie(self, employee_id, da_data, a_data, ore_giornaliere_da_contratto, dict_permessi):

        """
        La funzione crea un dizionario, dove le chiavi sono i giorni
        del periodo che si sta analizzanzo, e ogni chiave come valore
        ha il numero di ore di ferie per quella giornata

        :param dict_permessi:
        :param employee_id:
        :param da_data:
        :param a_data:
        :param ore_giornaliere_da_contratto:
        :return:
        """

        # Dizionario che avrà come chiave la data
        # e come valore le ore del permesso o delle ferie
        dict_giorni_ferie = {}

        # Prendo per un dipendente tutte le ferie e i permessi che ha fatto
        # nel periodo selezionato dal wizard
        giorni_ferie = self.env['hr.leave'].search(
            [('employee_id', '=', employee_id), ('request_date_from', '<=', a_data),
             ('request_date_to', '>=', da_data), ('state', '=', 'validate')], order='request_date_from asc, holiday_status_id asc')

        # ciclo ogni singola riga e calcolo per ogni giorno
        # le ore di ferie e permessi
        for giorno in giorni_ferie:
            if giorno.number_of_days_display >= 1:
                days = giorno.request_date_to - giorno.request_date_from
                for day in range(days.days + 1):
                    if giorno.request_date_from + datetime.timedelta(days=day) not in dict_giorni_ferie.keys():
                        dict_giorni_ferie[giorno.request_date_from + datetime.timedelta(days=day)] = {}

                        # Creo il modello del dizionario, come chiavi ha
                        # gli id dei tipi permesso e come valore 0
                        for permesso_model in dict_permessi.keys():
                            dict_giorni_ferie[giorno.request_date_from + datetime.timedelta(days=day)][permesso_model] = 0

                    dict_giorni_ferie[giorno.request_date_from + datetime.timedelta(days=day)][giorno.holiday_status_id.id] += ore_giornaliere_da_contratto
            else:
                if giorno.request_date_from not in dict_giorni_ferie.keys():
                    dict_giorni_ferie[giorno.request_date_from] = {}

                    # Creo il modello del dizionario, come chiavi ha
                    # gli id dei tipi permesso e come valore 0
                    for permesso_model in dict_permessi.keys():
                        dict_giorni_ferie[giorno.request_date_from][permesso_model] = 0

                if giorno.request_unit_half:
                    ore = ore_giornaliere_da_contratto / 2
                    dict_giorni_ferie[giorno.request_date_from][giorno.holiday_status_id.id] += ore

                elif giorno.request_unit_hours:

                    # Chiamata la funzione del modello hr.leave, perchè il campo
                    # number_of_hours_display è compute
                    giorni_ferie._compute_number_of_hours_display()
                    dict_giorni_ferie[giorno.request_date_from][giorno.holiday_status_id.id] += giorno.number_of_hours_display

        return dict_giorni_ferie

    def calcolo_ore_lavorate(self, employee_id, da_data, a_data):

        """
        Funzione che crea un dizionario, dove la chiavi sono i giorni
        del periodo che si sta analizzando, e ogni chiave come valore
        ha il numero di ore lavorate per quella giornata

        :param employee_id:
        :param da_data:
        :param a_data:
        :return:
        """

        # Dizionario che avrà come chiave la data
        # e come valore le ore lavorate
        dict_giorni_lavorati = {}

        # Prendo per un dipendente tutte le ferie e i permessi che ha fatto
        # nel periodo selezionato dal wizard
        giorni_lavorati = self.env['hr.attendance'].search(
            [('employee_id', '=', employee_id), ('check_in', '>=', da_data),
             ('check_out', '<=', a_data)], order='check_in asc')

        giorno_corrente = False

        # ciclo ogni singola riga e calcolo per ogni giorno
        # le ore lavorate
        for giorno in giorni_lavorati:

            if not giorno_corrente:
                giorno_corrente = giorno.check_in.date()

            if giorno.check_in.date() not in dict_giorni_lavorati.keys():
                dict_giorni_lavorati[giorno.check_in.date()] = 0

            # Quando viene cambiato il giorno eseguo l'arrotondamento
            # delle ore per quella giornata
            if giorno_corrente != giorno.check_in.date():
                dict_giorni_lavorati[giorno_corrente] = self.arrotondamento_ore_lavorate(
                    dict_giorni_lavorati[giorno_corrente])
                giorno_corrente = giorno.check_in.date()

            dict_giorni_lavorati[giorno.check_in.date()] += giorno.worked_hours

        if len(giorni_lavorati) > 0:
            dict_giorni_lavorati[giorno_corrente] = self.arrotondamento_ore_lavorate(
                dict_giorni_lavorati[giorno_corrente])

        return dict_giorni_lavorati

    def arrotondamento_ore_lavorate(self, ore_lavorate):

        """
        Funzione che in base alle ore che vengono passate come parametro le
        arrotonda al quarto d'ora per difetto

        :param ore_lavorate:
        :return:
        """

        minuti_ore_lavorate = (ore_lavorate - int(ore_lavorate)) * 100

        minuti_ore_lavorate = round(minuti_ore_lavorate, 2)

        if abs(minuti_ore_lavorate) < 25:
            minuti_ore_lavorate = 0
        elif 25 <= abs(minuti_ore_lavorate) < 50:
            minuti_ore_lavorate = 25
        elif 50 <= abs(minuti_ore_lavorate) < 75:
            minuti_ore_lavorate = 50
        elif abs(minuti_ore_lavorate) >= 75:
            minuti_ore_lavorate = 75

        return int(ore_lavorate) + (minuti_ore_lavorate / 100)


class WizardReportPresenze(models.TransientModel):
    _name = 'pacchetto.ore.presenze'

    da_data = fields.Date(required=True)
    a_data = fields.Date(required=True)

    def stampa_report_presenze(self):
        datas = {
            'model': 'pacchetto.ore.presenze',
            'form': {
                'da_data': self.da_data,
                'a_data': self.a_data,
            }
        }

        return self.env.ref('addoons_pacchetto_ore.report_presenze_xlsx').report_action(self, data=datas)
