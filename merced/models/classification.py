# -*- coding: utf-8 -*-
from odoo import fields, models

class Classification(models.Model):
	_name = 'classification.product'

	name = fields.Char(string='Nombre de la clasificación', required=True)
	