from odoo import models, fields

class AnswerOne(models.Model):
    _inherit = 'res.partner'
    _description = 'Add new field Language(Idioma)'
    
    language = fields.Char(string="Idioma")