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

from openerp import api, models


def split_text(txt):
    return txt.split(';')


class SaleOrderReport(models.AbstractModel):
    _name = 'report.sale.report_saleorder'

    @api.multi
    def render_html(self, docids, data=None):
        report = self.env['report']._get_report_from_name('sale.report_saleorder')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env['sale.order'].browse(docids,),
            'split_text': split_text
            }
        return self.env['report'].render('sale.report_saleorder', docargs)
