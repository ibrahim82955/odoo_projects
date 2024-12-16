{
    'name': "Custom Report Product Pricelist",
    'summary': """Custom Report Product Pricelist """,
    'description': """
        This module for Product Pricelist Report.
    """,
    'author': "Abanob Ashraf",
    'website': "http://zadsolutions.com",
    'license': 'OPL-1',
    'category': 'base',
    'version': '16.1',
        'sequence': -100,

    'depends': ['base', 'product'],
    'data': [
        'views/product_pricelist_report_template_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_report_product_pricelist/static/src/js/**/*',
            'custom_report_product_pricelist/static/src/xml/**/*',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
}
