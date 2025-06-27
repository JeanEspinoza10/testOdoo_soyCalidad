from odoo import models, fields, api

class AnswerNine(models.Model):
    _inherit = 'account.move'
    
    total_picking = fields.Many2many(
            comodel_name='stock.picking',
            string='Transferencias Relacionadas',
            compute='_compute_total_picking',
            store=True
            )
    
    @api.depends('create_date', 'write_date')
    def _compute_total_picking(self):
        for record in self:
            pos_order = self.env['pos.order'].search([("account_move", "=", record.id)], limit=1)
            if pos_order:
                pickings = self.env['stock.picking'].search([("pos_order_id", "=", pos_order.id)])
                record.total_picking = pickings
            else:
                record.total_picking = False
            
