# -*- coding: utf-8 -*-
{
    'name': "Awesome Dashboard",
    'summary': """
        Starting module for "Discover the JS framework, chapter 2: Build a dashboard"
        """,
    'description': """
        Starting module for "Discover the JS framework, chapter 2: Build a dashboard"
        """,
    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials/AwesomeDashboard',
    'version': '18.0.1.0.0',
    'application': True,
    'installable': True,
    'depends': ['base', 'web', 'mail', 'crm'],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'gabriela-awesome_dashboard/static/src/dashboard_loader.js',
        ],
        'gabriela-awesome_dashboard.dashboard': [
            # Load JS files
            'gabriela-awesome_dashboard/static/src/dashboard/dashboard.js',
            'gabriela-awesome_dashboard/static/src/dashboard/dashboard_item/dashboard_item.js',
            'gabriela-awesome_dashboard/static/src/dashboard/pie_chart/pie_chart.js',
            'gabriela-awesome_dashboard/static/src/dashboard/statistics_service.js',
            'gabriela-awesome_dashboard/static/src/dashboard/dashboard_items.js',
            'gabriela-awesome_dashboard/static/src/dashboard/number_card/number_card.js',
            'gabriela-awesome_dashboard/static/src/dashboard/pie_chart_card/pie_chart_card.js',
            # Load XML templates
            'gabriela-awesome_dashboard/static/src/dashboard/dashboard.xml',
            'gabriela-awesome_dashboard/static/src/dashboard/number_card/number_card.xml',
            'gabriela-awesome_dashboard/static/src/dashboard/pie_chart_card/pie_chart_card.xml',
            'gabriela-awesome_dashboard/static/src/dashboard/dashboard_item/dashboard_item.xml',
            'gabriela-awesome_dashboard/static/src/dashboard/pie_chart/pie_chart.xml',
        ]
    },
    'license': 'AGPL-3'
}