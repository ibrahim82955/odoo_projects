import base64
from collections import OrderedDict
from datetime import datetime

from odoo import http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request, Response
from odoo.tools import image_process
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import CustomerPortal

from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        print('aaaaaaaaaaaaaaaaa')
        user = request.env.user
        employee_id = user.employee_id
        phone = user.phone
        hr_attendance = request.env["hr.attendance"].sudo().search_count([('employee_id', '=', employee_id.id)])
        values["attentance_count"]=hr_attendance
        return values
