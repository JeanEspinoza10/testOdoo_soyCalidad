from odoo import models, fields, api

class AnsweFive(models.Model):
    _inherit = 'account.move'
    
    serial_number = fields.Char(string="Número de serie",
                                compute = '_calculate_serial_number',
                                store=True)
    
    correlative_number = fields.Char(string="Número Correlativo", 
                                     compute = '_calculate_correlative_number',
                                     store=True)
    
    @api.depends('create_date', 'write_date','state','payment_reference')
    def _calculate_serial_number(self):
        for record in self:
            sq_prefix = record.sequence_prefix
            record.serial_number = sq_prefix.replace("/","")
    
    @api.depends('create_date', 'write_date','state','payment_reference')
    def _calculate_correlative_number(self):
        for record in self:
            record.correlative_number = str(record.sequence_number).zfill(8)            