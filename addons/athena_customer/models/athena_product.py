from odoo import models, fields


class AthenaProduct(models.Model):
    _name = 'athena.product'
    _description = 'Athena Product'

    name = fields.Char(string='Product Name', required=True)
    category = fields.Selection(
        [('A6', 'A6'), ('A7', 'A7')],
        string='Category',
        required=True,
        default='A6'
    )
