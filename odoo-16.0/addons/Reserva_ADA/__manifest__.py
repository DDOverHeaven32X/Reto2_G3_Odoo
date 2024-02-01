# -*- coding: utf-8 -*-
{
    'name': "Reserva ADA",

    'summary': """
       Esta aplicacion servira para administrar un parque natural""",

    'description': """
       Gestiona animales, zonas y las entradas del propio parque
   """,

    'author': "DAM Tartanga Grupo3",
    'website': "http://www.tartanga.eus",
    'icon': "/Reserva_ADA/static/description/odoo_icon.png",

    # Categories can be used to fi  lter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/reserva_security.xml',
        'security/ir.model.access.csv',
        'views/zonas.xml',
        'views/animales.xml',
        'views/entradas.xml',
        'report/Reserva_ADA_entradas_reporte.xml',
        'report/Reserva_ADA_animales_reporte.xml',
        'report/Reserva_ADA_zonas_reporte.xml'
        # 'views/templates.xml',
    ],

}
