# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of email_separator, an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     email_separator is free software: you can redistribute it and/or
#     modify it under the terms of the GNU Affero General Public License
#     as published by the Free Software Foundation, either version 3 of
#     the License, or (at your option) any later version.
#
#     email_separator is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with email_separator.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Email Separator',
    'version': '1.0',
    'author': 'ACSONE SA/NV',
    'maintainer': 'ACSONE SA/NV',
    'website': 'http://www.acsone.eu',
    'category': 'Tools',
    'depends': [
        'mass_mailing',
    ],
    'description': """
Email Separator
===============
This module uses '+' instead of '-' as technical email separator
to build bounce paths
""",
    'images': [
    ],
    'data': [
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
