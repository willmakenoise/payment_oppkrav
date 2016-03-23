# -*- encoding: utf-8 -*-
###############################################################################
# #                                                                           #
# Oppkrav for Odoo                                                            #
# Copyright (C) 2015 Marius Stedjan (<http://www.mariusstedjan.com>).         # 
#                                                                             #
###############################################################################
###############################################################################
# Oppkrav Payment Acquirer                                                    #
#                                                                             #
###############################################################################

{
    'name': 'Oppkrav Payment Acquirer',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: Oppkrav Implementation',
    'author': 'Marius Stedjan',
    'version': '1.0',
    'description': """Oppkrav Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/oppkrav.xml',
        'data/oppkrav.xml',
    ],
    'installable': True,
    'auto_install': True,
}
