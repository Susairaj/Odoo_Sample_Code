# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2016 OdooNinja.COM
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Inherit Models Example",
    'category': 'Custom',
    'version': '10.0.1.0.0',
    'author': "OdooNinja.COM",
    'depends': [
        'sale',
    ],
    'data': [
        'views/product.xml',
        'views/sale.xml',
    ],
    'website': 'http://odooninja.com',
    'license': 'AGPL-3',
    'installable': True,
}
