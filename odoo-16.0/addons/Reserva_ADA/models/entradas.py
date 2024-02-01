from odoo import models, fields, api, exceptions


class entradas(models.Model):
    _name = 'grupo3c.entradas'
    # Precio de la entrada
    precio = fields.Float(required=True, string="Precio");
    fecha_entrada = fields.Date(string="Fecha")
    tipo_entrada = fields.Selection([('normal', 'Normal'), ('infantil', 'Infantil'), ('senior', 'Senior')],
                                    string="Tipo de entrada", required=True)

    client_id = fields.Many2one('res.users', string="Cliente")
    admin_id = fields.Many2one('res.users', string="Admin")
    zona_id = fields.Many2many('grupo3c.zonas', string="Código de Zona")

    @api.onchange('fecha_entrada')
    def _onchange_fecha_entrada(self):
        if self.fecha_entrada and self.fecha_entrada < fields.Date.today():
            return {
                'warning': {
                    'title': "Advertencia",
                    'message': "CAMPO FECHA: La fecha no puede ser inferior a la actual."
                }
            }

    @api.constrains('fecha_entrada')
    def _check_fecha_entrada(self):
        for entradas in self:
            if fields.Date.from_string(entradas.fecha_entrada) < fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("CAMPO FECHA: La fecha no puede ser inferior a la actual")

    @api.onchange('precio')
    def _onchange_precio(self):
        if not (0.0 <= self.precio <= 50.0):
            return {
                'warning': {
                    'title': "Advertencia",
                    'message': "CAMPO PRECIO: El precio debe estar entre 0 y 50."
                }
            }

    @api.constrains('precio')
    def _check_precio_range(self):
        for entradas in self:
            if not (0.0 <= self.precio <= 50.0):
                raise exceptions.ValidationError("CAMPO PRECIO: El precio debe estar entre 0 y 50.")

    @api.model
    def default_get(self, fields):
        defaults = super(entradas, self).default_get(fields)
        # Establecer valores predeterminados si no se especifican
        if 'precio' not in defaults or defaults['precio'] == 0:
            defaults['precio'] = 10.0

        return defaults

    @api.model
    def create(self, vals):
        # Establecer valores predeterminados si no se especifican
        if 'precio' not in vals or vals['precio'] == 0:
            vals['precio'] = 10.0
        if 'fecha_entrada' not in vals or not vals['fecha_entrada']:
            vals['fecha_entrada'] = fields.Date.today()

        # Llamar al método create de la superclase para crear el registro
        return super(entradas, self).create(vals)
