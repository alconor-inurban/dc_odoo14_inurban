# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseSummaryReportWizard(models.TransientModel):
    _name = 'purchase.summary.report.wizard'

    date_start = fields.Date(string='Start Date', required=True, default=fields.Date.today)
    date_end = fields.Date(string='End Date', required=True, default=fields.Date.today)

    @api.multi
    def get_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'date_start': self.date_start, 'date_end': self.date_end,
            },
        }

        # ref `module_name.report_id` as reference.
        return self.env.ref('custom_report_odoo12.sale_summary_report').report_action(self, data=data)