# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jimenez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, _
import logging
_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Link for the main companies
    crm_timeline_actions_parent = fields.One2many(
        'crm.timeline.action',
        'parent_id',
        string=_('CRM Actions'),
    )
    # Link for contacts
    crm_timeline_actions_partner = fields.One2many(
        'crm.timeline.action',
        'partner_id',
        string=_('CRM Actions'),
    )
