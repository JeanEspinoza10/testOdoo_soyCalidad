from odoo import models, fields

class AnswerSix(models.Model):
    _inherit = 'account.move'
    
    sales_channel =  fields.Many2one(
        'sales.channel',
        string="Canal de Ventas"
    )

class SalesChannel(models.Model):
    _name = 'sales.channel'
    _description = 'Canal de Ventas'
    
    name = fields.Char(string="Name")