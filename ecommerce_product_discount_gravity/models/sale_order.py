from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discounted_price = fields.Float(
        "Discounted Price")

    def write(self,vals):
        if self.product_id.discount_percentage > 0:
            vals['price_unit'] = self.product_id.list_price * (1 - self.product_id.discount_percentage / 100)
        else:
            vals['price_unit'] = self.product_id.list_price
        res = super().write(vals)
        



