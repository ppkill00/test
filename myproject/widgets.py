# -*- encoding: utf-8 -*-
from dashing.views import Dashboard
from dashing.widgets import NumberWidget
from random import randint
 

users = randint(50, 100)

class CustomDashboard(Dashboard):
    template_name = 'dashboard.html'


class MyCustomWidget(NumberWidget):
    title = 'New Users'
 
    def get_value(self):
        global users
        users += 1
        return users
 
    def get_detail(self):
        global users
        return '{} actives'.format(users * 2)
 
    def get_more_info(self):
        global users
        return '{} fakes'.format(users * 3)