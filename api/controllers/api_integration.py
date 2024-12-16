import json
import logging
import functools
import werkzeug.wrappers

from odoo import http
from odoo.exceptions import AccessDenied, AccessError
from odoo.http import request

_logger = logging.getLogger(__name__)


class Token(http.Controller):
    @http.route("/attentance", methods=["GET"], type="http", auth="none", csrf=False,)
    def attentance(self, **post):

        params = ["id"]
        params = {key: post.get(key) for key in params if post.get(key)}
        id = (
            post.get("id")
        )
        if not id:
            headers = request.httprequest.headers
            id = headers.get("id")

        hr_attendance = request.env["hr.attendance"].sudo().search(
            [('employee_id', '=', int(id))])

        attendance_data = []

        for record in hr_attendance:
            attendance_data.append({
                'id': record.id,
                'employee_id': record.employee_id.id,
                'check_in': str(record.check_in),
                'check_out': str(record.check_out),
            })
            print('aaaaaaasdasdasdasd', attendance_data)

        return werkzeug.wrappers.Response(
            status=200,
            content_type="application/json; charset=utf-8",
            headers=[("Cache-Control", "no-store"), ("Pragma", "no-cache")],
            response=json.dumps(
                [{"record_id":x['id'],
                  "user_context":x['employee_id'],
                  "check_in": x['check_in'],
                  "check_out": x['check_out']}
                 for x in attendance_data
                 ]
            ),
        )
