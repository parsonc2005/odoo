from odoo import models, fields


class AthenaCustomer(models.Model):
    _name = 'athena.customer'
    _description = 'Athena Customer'

    name = fields.Char(string='Customer Name', required=True)
    address = fields.Char(string='Address')
    contact_person = fields.Char(string='Contact Person')
    phone = fields.Char(string='Phone')
    product_line_ids = fields.One2many(
        'athena.customer.product.line',
        'customer_id',
        string='Products'
    )


class AthenaCustomerProductLine(models.Model):
    _name = 'athena.customer.product.line'
    _description = 'Customer Product Line'

    customer_id = fields.Many2one('athena.customer', string='Customer', ondelete='cascade')
    product_id = fields.Many2one('athena.product', string='Product', required=True)
    purchase_date = fields.Date(string='Purchase Date')
    salesperson_id = fields.Many2one('res.users', string='Salesperson')
