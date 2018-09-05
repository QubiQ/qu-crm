# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jimenez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, _
import logging
_logger = logging.getLogger(__name__)


class CrmTimelineAction(models.Model):
    _name = 'crm.timeline.action'

    date = fields.Datetime(
        string=_('Date'),
        required=True,
        default=lambda self: fields.Datetime.now(),
    )
    partner_id = fields.Many2one(
        'res.partner',
        string=_('Partner'),
        required=True,
    )
    user_id = fields.Many2one(
        'res.users',
        string=_('User'),
        required=True,
        default=lambda self: self.env.user,
    )
    description = fields.Text(string=_('Description'))
