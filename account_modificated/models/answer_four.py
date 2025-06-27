# -*- coding: utf-8 -*-

from odoo import models, fields, api
import qrcode
import base64
import io

class ModificatedAccount(models.Model):
    _inherit = 'account.move'
    
    code_qr = fields.Binary(string="Code QR", compute="_generate_qr_new", store=True)
    calculate_quantity_lines = fields.Integer(string="quantity_lines", compute="_calculate_quantity", store=True)
    
    def generate_qr_code(self,qr_string):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(qr_string)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return {'x_qr_invoice': img_str}

    @api.depends('invoice_date_due','calculate_quantity_lines', 'payment_reference', 'partner_id', 'invoice_date', 'amount_total')
    def _generate_qr_new(self):
        for record in self:
            try:
                if not record.partner_id or not record.invoice_date or not record.amount_total:
                    record.code_qr = False
                    continue
                qr_string = (
                    f"{record.payment_reference or ''}|"
                    f"{record.partner_id.name or ''}|"
                    f"{record.invoice_date.strftime('%Y-%m-%d')}|"
                    f"{int(record.calculate_quantity_lines)}|"
                    f"{record.amount_total:.2f}"
                )

                qr_data = record.generate_qr_code(qr_string)
                record.code_qr = qr_data['x_qr_invoice']
            except Exception as err:
                record.code_qr = False
            
    @api.depends("line_ids")
    def _calculate_quantity(self):     
        for record in self:
            sum_quantity = 0
            for line in record.line_ids:
                if(line.display_type == 'product'):
                    sum_quantity += line.quantity
            record.calculate_quantity_lines = sum_quantity
