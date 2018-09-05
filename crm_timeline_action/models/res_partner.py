# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jimenez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    crm_timeline_actions = fields.One2many(
        'crm.timeline.action',
        'partner_id',
        string=_('CRM Actions'),
    )
