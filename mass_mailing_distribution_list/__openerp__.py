# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: Nemry Jonathan
#    Copyright (c) 2014 Acsone SA/NV (http://www.acsone.eu)
#    All Rights Reserved
#
#    WARNING: This program as such is intended to be used by professional
#    programmers who take the whole responsibility of assessing all potential
#    consequences resulting from its eventual inadequacies and bugs.
#    End users who are looking for a ready-to-use solution with commercial
#    guarantees and support are strongly advised to contact a Free Software
#    Service Company.
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
    'name': 'Mass Mailing Distribution List',
    'version': '1.0',
    'author': 'ACSONE SA/NV',
    'maintainer': 'ACSONE SA/NV',
    'website': 'http://www.acsone.eu',
    'category': 'Marketing',
    'depends': [
        'distribution_list',
        'mass_mailing',
    ],
    'description': """
Mass Mailing Distribution List
==============================

This module make a link between distribution list and mass mailing.

It also provide the possibility to use a distribution as a newsletter.
If a distribution list is created as a newsletters then it will be available
to manage a Opt In/Out List of partners.
This Opt Out option may be directly set from a received email by clicking
unsubscribe URL
    """,
    'data': [
        'views/mass_mailing.xml',
        'views/distribution_list_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}