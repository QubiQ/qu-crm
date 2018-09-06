# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jimenez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)


class CrmTimelineAction(models.Model):
    _name = 'crm.timeline.action'

    date = fields.Datetime(
        string=_('Date'),
        required=True,
        default=lambda self: fields.Datetime.now(),
    )
    # Field to store the parent or self if there's no parent
    parent_id = fields.Many2one(
        'res.partner',
        string=_('Partner'),
        default=lambda self: self._get_default_parent(),
    )
    # Field to store the partner to whom the CRM action was made
    partner_id = fields.Many2one(
        'res.partner',
        string=_('Related Partner'),
        required=True,
    )
    user_id = fields.Many2one(
        'res.users',
        string=_('User'),
        required=True,
        default=lambda self: self.env.user,
    )
    description = fields.Text(string=_('Description'))

    @api.model
    def _get_default_parent(self):
        context = dict(self.env.context or {})
        _logger.info(context)
        if 'default_partner_id' in context:
            partner_obj = self.env['res.partner'].browse([
                context['default_partner_id']])

            if partner_obj.parent_id:
                return partner_obj.parent_id.id
            else:
                return partner_obj.id
