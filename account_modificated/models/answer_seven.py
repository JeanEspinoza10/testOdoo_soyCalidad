from odoo import models, fields

class AnswerSeven(models.Model):
    _inherit = 'account.move'
    
    issue_date = fields.Datetime(string='Fecha de Emisión', default=fields.Datetime.now )

    