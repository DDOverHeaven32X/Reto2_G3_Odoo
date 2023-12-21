# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class entradas(models.Model):
    _name = 'grupo3c.entradas'

    precio = fields.Monetary(required = true, string="Precio")
    fecha_entrada = fields.Date(required = true, string ="Fecha")

    client_id = fields.Many2one('res.users', string="Cliente")
    zona_id = fields.ManyMany("grupo3c.zona", "zonaId", string="codigo_zona")

    @api.constrains('fecha_entrada')
    def _validate_date(self):
        for entradas in self:
            if fields.Date.from_string(entradas.fecha_entrada) < fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("La fecha no puede ser inferior a la actual")

    @api.constrains('precio')
    def _validate_date(self):
        for entradas in self:
            if entradas.precio.isalpha():
                raise exceptions.ValidationError("No puedes introducir letras en el precio")









