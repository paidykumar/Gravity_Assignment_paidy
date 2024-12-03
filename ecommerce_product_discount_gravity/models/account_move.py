from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _prepare_account_move_line(self):
        move_line_vals = super()._prepare_account_move_line()
        if self.product_id.discount_percentage > 0:
            move_line_vals['price_unit'] = self.product_id.discounted_price
        return move_line_vals
