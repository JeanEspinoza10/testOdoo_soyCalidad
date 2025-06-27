# -*- coding: utf-8 -*-
# from odoo import http


# class AccountModificated(http.Controller):
#     @http.route('/account_modificated/account_modificated', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_modificated/account_modificated/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_modificated.listing', {
#             'root': '/account_modificated/account_modificated',
#             'objects': http.request.env['account_modificated.account_modificated'].search([]),
#         })

#     @http.route('/account_modificated/account_modificated/objects/<model("account_modificated.account_modificated"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_modificated.object', {
#             'object': obj
#         })

