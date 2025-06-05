{
    'name': 'Athena Customer Management',
    'version': '16.0.1.0.0',
    'summary': 'Manage Athena products and customers',
    'description': 'Module to manage Athena products and customers with multilingual support.',
    'author': 'Paul Lu',
    'website': 'https://www.example.com',
    'category': 'Sales/CRM',
    'depends': ['base'],
    'data': [
        'security/athena_groups.xml',
        'security/ir.model.access.csv',
        'views/athena_menus.xml',
        'views/athena_product_views.xml',
        'views/athena_customer_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
