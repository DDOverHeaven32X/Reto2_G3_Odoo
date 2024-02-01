from odoo import models, api, fields, exceptions


class zonas(models.Model):
    _name = 'grupo3c.zonas'
    # Nombre de la zona
    name = fields.Char(required=True, string="Nombre")
    tipo_animal = fields.Selection([
        ('terrestre', 'Terrestre'),
        ('acuatico', 'Acuatico'),
        ('volador', 'Volador')
    ], string='Tipo Animal')
    descripcion = fields.Text(required=True, string="Descripcion")
    id_admin = fields.Many2one('res.users', string="Admin ID")
    id_entrada = fields.Many2many("grupo3c.entradas", string="Código Entrada")

    @api.onchange('name')
    def _onchange_nombre(self):
        if isinstance(self.name, str) and (not self.name.isalpha() or len(self.name) > 20):
            return {
                'warning': {
                    'title': "Ha ocurrido un error",
                    'message': "CAMPO NOMBRE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras."
                }
            }

    @api.constrains('name')
    def _check_nombre(self):
        if isinstance(self.name, str) and (not self.name.isalpha() or len(self.name) > 20):
            raise exceptions.ValidationError(
                " CAMPO NOMBRE: Los caracteres no pueden ser nulos y deben ser menores o iguales a 20. Además, deben contener solo letras.")

    @api.onchange('descripcion')
    def _onchange_description(self):
        if len(str(self.descripcion)) > 200:
            return {
                'warning': {
                    'title': "Ha sucedido un error",
                    'message': "CAMPO DESCRIPCION: Has superado el máximo de caracteres (Max: 100)"
                }
            }

    @api.constrains('descripcion')
    def _check_descripcion(self):
        if len(str(self.descripcion)) > 200:
            raise exceptions.ValidationError("El número de caracteres debe ser menor a 100.")

    @api.onchange('tipo_animal')
    def _onchange_tipo_animal(self):
        allowed_values = ['terrestre', 'acuatico', 'volador']
        if self.tipo_animal and self.tipo_animal not in allowed_values:
            self.tipo_animal = False
            return {
                'warning': {
                    'title': "Ha ocurrido un error",
                    'message': "El tipo de animal debe ser Terrestre, Acuático o Volador."
                }
            }

    @api.constrains('tipo_animal')
    def _check_tipo_animal(self):
        allowed_values = ['terrestre', 'acuatico', 'volador']
        if self.tipo_animal and self.tipo_animal not in allowed_values:
            raise exceptions.ValidationError("El tipo de animal debe ser Terrestre, Acuático o Volador.")

    @api.model
    def default_get(self, fields):
        defaults = super(zonas, self).default_get(fields)

        # Establecer valores predeterminados si no se especifican
        if 'tipo_animal' not in defaults:
            defaults['tipo_animal'] = "terrestre"
        if 'id_admin' not in defaults:
            defaults['id_admin'] = 2

        return defaults

    @api.model
    def create(self, vals):
        # Establecer valores predeterminados si no se especifican
        if 'tipo_animal' not in vals or not vals.get('tipo_animal'):
            vals['tipo_animal'] = "terrestre"
        if 'id_admin' not in vals:
            vals['id_admin'] = 2

        # Llamar al método create de la superclase para crear el registro
        return super(zonas, self).create(vals)
