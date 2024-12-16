# -*- coding: utf-8 -*-

{
'name': "Discount task",
'version': '1.2',
'sequence': -100,
'depends': ['base','account','product','sale'],
'data': [ 
'views/views.xml','views/third_inherit.xml','views/invoicing_inherit.xml','views/second_inherit.xml','views/account.move_inherit.xml'
],

    'application': True,


}
