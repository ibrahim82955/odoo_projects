
from odoo import models, fields, api
import ast
import datetime
import io
import json
import logging
import math
import re
import base64
from ast import literal_eval
from collections import defaultdict
from functools import cmp_to_key

import markupsafe
from babel.dates import get_quarter_names
from dateutil.relativedelta import relativedelta

from odoo.addons.web.controllers.utils import clean_action
from odoo import models, fields, api, _, osv, _lt
from odoo.exceptions import RedirectWarning, UserError, ValidationError
from odoo.tools import config, date_utils, get_lang, float_compare, float_is_zero
from odoo.tools.float_utils import float_round
from odoo.tools.misc import formatLang, format_date, xlsxwriter
from odoo.tools.safe_eval import expr_eval, safe_eval
from odoo.models import check_method_name


class AccountReport(models.Model):
    _inherit = 'account.report'

    filter_additional_field = fields.Boolean(
        string="Additional Filter",

        default=False,
        readonly=False, store=True,
    )
    # access_field=fields.Many2one()

    def _init_options_accountt_type(self, options, previous_options=None):
       
        options['balance_type'] = [
            {'id': 'show', 'name': _("show"), 'selected': True}]
        if previous_options and previous_options.get('balance_type'):
            previously_selected_ids = {
                x['id'] for x in previous_options['balance_type'] if x.get('selected')}
            for opt in options['balance_type']:
                opt['selected'] = opt['id'] in previously_selected_ids

        selected_options = {x['id']: x['name']
                            for x in options['balance_type'] if x['selected']}
        selected_ids = set(selected_options.keys())
        display_names = []

        def check_if_name_applicable(ids_to_matchh, string_if_matchh):

            if len(selected_ids) == 0:
                return
            if ids_to_matchh.issubset(selected_ids):
                display_names.append(string_if_matchh)
                for selected_id in ids_to_matchh:
                    selected_ids.remove(selected_id)

    @api.model
    def _get_options_initialbalance(self, options):

        if not options.get('balance_type') or len(options.get('balance_type')) == 0:
            return []
        for opt in options.get('balance_type', []):
            print(234, opt)
            if opt['id'] == 'show' and opt['selected'] == True:
                self.filter_additional_field = False

            else:
                self.filter_additional_field = True

    def _get_partner_and_general_ledger_initial_balance_line(self, options, parent_line_id, eval_dict, account_currency=None, level_shift=0):
        # Your additional logic here
        self._get_options_initialbalance(options)

        if self.filter_additional_field:
            return False

        else:
            result = super(AccountReport, self)._get_partner_and_general_ledger_initial_balance_line(
                options, parent_line_id, eval_dict, account_currency, level_shift)
            return result
