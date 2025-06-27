# -*- coding: utf-8 -*-
# from odoo import http


# class PointOfSaleModificated(http.Controller):
#     @http.route('/point_of_sale_modificated/point_of_sale_modificated', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/point_of_sale_modificated/point_of_sale_modificated/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('point_of_sale_modificated.listing', {
#             'root': '/point_of_sale_modificated/point_of_sale_modificated',
#             'objects': http.request.env['point_of_sale_modificated.point_of_sale_modificated'].search([]),
#         })

#     @http.route('/point_of_sale_modificated/point_of_sale_modificated/objects/<model("point_of_sale_modificated.point_of_sale_modificated"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('point_of_sale_modificated.object', {
#             'object': obj
#         })

