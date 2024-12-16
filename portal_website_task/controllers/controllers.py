import logging
import werkzeug
from odoo import http, _
from odoo.http import request
from odoo import fields, models
from datetime import datetime
from odoo.exceptions import ValidationError, UserError


class portal(http.Controller):
    @http.route('/employee/attendance', auth='public', website=True)
    def attendance(self, **kws):
        user = request.env.user
        employee_id = user.employee_id
        phone = user.phone
        hr_attendance = request.env["hr.attendance"].sudo().search([('employee_id', '=', employee_id.id)])
        return request.render("portal_website_zad_task.webpage_id", {
            'hr_attentance': hr_attendance

        })

    @http.route('/employee/attendance/details/<int:record_id>', auth='public', website=True)
    def attendance_details(self, record_id, **kws):
        user = request.env.user
        phone = user.phone
        mobile = user.mobile
        title = user.title
        job = user.function
        email = user.email
        hr_attendance_record = request.env["hr.attendance"].sudo().browse(record_id)
        dic = {
            'employee_work_hour': hr_attendance_record.worked_hours,
            'phone': phone,
            'mobile': mobile,
            'job': job,
            'email': email

        }
        for x in dic:
            if not dic[x]:
                dic[x] = " "

        return request.render("portal_website_zad_task.webpage_id_details", dic)

    @http.route('/employee/attendance/create', type="http", auth="public", website=True)
    def patient_webform(self, **kw):
        users = request.env["hr.employee"].sudo().search([])
        print("Execution Here.........................")
        return request.render("portal_website_zad_task.create_attendance", {
            'users': users
        })

    @http.route('/NEW/', auth='public', website=True)
    def attendance_new(self, **kws):
        print('asdasdasdas', kws)
        employee_idd = int(kws.get('employee_id'))
        check_in = kws.get('check_in')
        check_out = kws.get('check_out')
        employee_idd = int(kws.get('employee_id'))
        employee_obj = request.env['hr.employee'].browse(employee_idd)

        print('11111111111111111111', employee_obj.id)
        print('11111111111111111111', check_in)
        print('11111111111111111111', check_out)
        check_in_datetime = datetime.strptime(check_in, '%Y-%m-%dT%H:%M')
        check_out_datetime = datetime.strptime(check_out, '%Y-%m-%dT%H:%M')

        print('-------------------------------------')
        print('-------------------------------------')
        print('11111111111111111111', check_in_datetime.date())

        if check_in_datetime.date()==check_out_datetime.date():
            hr_attendance = request.env['hr.attendance'].create({
            'employee_id': employee_obj.id,
            'check_in': check_in_datetime,
            'check_out': check_out_datetime,
            'department_id': 'asfa'
            })

            return request.redirect('/success_page_url')
        else :
            raise UserError("check in and check out must be in the same day")

    @http.route('/success_page_url', auth='public', website=True)
    def success_page(self, **kws):
        return "Record successfully created!"
