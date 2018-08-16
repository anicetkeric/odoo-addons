# -*- coding: utf-8 -*-
##############################################################################
#
#     module for Odoo 10
#    Copyright (c) 2018 Copyright (c) 2018 aek
#      Anicet Eric Kouame <anicetkeric@gmail.com>
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
{
    "name": "HR Holidays Notification",
    "summary": "Notify employees by mail on Leave Requests",
    "version": "10.0",
    "category": "Human Resources",
    'author': 'Anicet Eric Kouame',
    'company': 'AEK',
    'website': "https://github.com/anicetkeric",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['hr',"hr_holidays"],
    "data": ['data/email_template.xml'],
    'images': ['static/description/banner.jpg'],
}
