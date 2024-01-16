from odoo import models, fields, api, exceptions


class animales(models.Model):
    _name = 'grupo3c.animales'
    # Nombre del animal
    nombre = fields.Char(required=True, string="Nombre")
    genero = fields.Selection([('hembra', 'HEMBRA'), ('macho', 'MACHO')], string='Genero', required=True)
    edad = fields.Integer(required=True, string="Edad")
    peso = fields.Float(required=True, string="Peso")
    altura = fields.Float(required=True, string="Altura")
    especie = fields.Char(required=True, string="Especie")
    alimentacion = fields.Selection([
        ('carnivoro', 'Carnivoro'),
        ('herbivoro', 'Herbivoro'),
        ('omnivoro', 'Omnivoro')
    ], string='Alimentacion', required=True)
    salud = fields.Selection([
        ('sano', 'Sano'),
        ('enfermo', 'Enfermo')
    ], string='Salud', required=True)

    admin_id = fields.Many2one('res.users', string="Admin")
    zona_id = fields.Many2one('grupo3c.zonas', string="codigo_zona")

    @api.onchange('nombre')
    def _onchange_nombre(self):
        if isinstance(self.nombre, str) and (not self.nombre.isalpha() or len(self.nombre) > 20):
            return {
                'warning': {
                    'title': "Ha ocurrido un error",
                    'message': "CAMPO NOMBRE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras."
                }
            }

    @api.onchange('edad')
    def _onchange_edad(self):
        if not isinstance(self.edad, (int, float)):
            return {
                'warning': {
                    'title': "Ha ocurrido un error",
                    'message': "CAMPO EDAD: Los caracteres deben ser solo números."
                }
            }

    @api.constrains('edad')
    def _validate_edad(self):
        if not isinstance(self.edad, (int, float)):
            raise exceptions.ValidationError("CAMPO EDAD: Solo puedes introducir números")

    @api.onchange('peso')
    def _onchange_peso(self):
        for animales in self:
            if not isinstance(animales.peso, (int, float)):
                return {
                    'warning': {
                        'title': "Ha ocurrido un error",
                        'message': "CAMPO PESO: Los caracteres deben ser solo numeros."
                    }
                }

    @api.constrains('peso')
    def _validate_peso(self):
        for animales in self:
            if not isinstance(animales.peso, (int, float)):
                raise exceptions.ValidationError("CAMPO PESO: Solo puedes introducir numeros")

    @api.onchange('altura')
    def _onchange_altura(self):
        for animales in self:
            if not isinstance(animales.altura, (int, float)):
                animales.altura = 0

                return {
                    'warning': {
                        'title': "Ha ocurrido un error",
                        'message': "CAMPO ALTURA: Solo puedes introducir números."
                    }
                }

    @api.constrains('altura')
    def _check_altura(self):
        for animales in self:
            if not isinstance(animales.altura, (int, float)):
                raise exceptions.ValidationError("CAMPO ALTURA: Solo puedes introducir números.")

    @api.onchange('especie')
    def _onchange_especie(self):
        for animales in self:
            if isinstance(self.especie, str) and (not self.especie.isalpha() or len(self.especie) > 20):
                return {
                    'warning': {
                        'title': "Ha ocurrido un error",
                        'message': "CAMPO ESPECIE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras."
                    }
                }

    @api.constrains('especie')
    def _validate_especie(self):
        for animales in self:
            if isinstance(self.especie, str) and (not self.especie.isalpha() or len(self.especie) > 20):
                raise exceptions.ValidationError(
                    "CAMPO ESPECIE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras.")

    @api.constrains('alimentacion')
    def _check_alimentacion(self):
        for animales in self:
            allowed_values = ['carnivoro', 'herbivoro', 'omnivoro']
            if animales.alimentacion and animales.alimentacion not in allowed_values:
                raise exceptions.ValidationError("La alimentacion debe ser carnivoro, herbivoro o omnivoro.")

    @api.constrains('salud')
    def _check_salud(self):
        for animales in self:
            allowed_values = ['sano', 'enfermo']
            if animales.salud and animales.salud not in allowed_values:
                raise exceptions.ValidationError("La salud debe ser sano o enfermo.")


from odoo import models, fields, api, exceptions


class animales(models.Model):
    _name = 'grupo3c.animales'
    # Nombre del animal
    nombre = fields.Char(required=True, string="Nombre")
    genero = fields.Selection([('hembra', 'HEMBRA'), ('macho', 'MACHO')], string='Genero', required=True)
    edad = fields.Integer(required=True, string="Edad")
    peso = fields.Float(required=True, string="Peso")
    altura = fields.Float(required=True, string="Altura")
    especie = fields.Char(required=True, string="Especie")
    alimentacion = fields.Selection([
        ('carnivoro', 'Carnivoro'),
        ('herbivoro', 'Herbivoro'),
        ('omnivoro', 'Omnivoro')
    ], string='Alimentacion', required=True)
    salud = fields.Selection([
        ('sano', 'Sano'),
        ('enfermo', 'Enfermo')
    ], string='Salud', required=True)

    admin_id = fields.Many2one('res.users', string="Admin")
    zona_id = fields.Many2one('grupo3c.zonas', string="codigo_zona")

    @api.onchange('nombre')
    def _onchange_nombre(self):
        if isinstance(self.nombre, str) and (not self.nombre.isalpha() or len(self.nombre) > 20):
            return {
                'warning': {
                    'title': "Ha ocurrido un error",
                    'message': "CAMPO NOMBRE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras."
                }
            }

    @api.onchange('edad')
    def _onchange_edad(self):
        if not isinstance(self.edad, (int, float)):
            return {
                'warning': {
                    'title': "Ha ocurrido un error",
                    'message': "CAMPO EDAD: Los caracteres deben ser solo números."
                }
            }

    @api.constrains('edad')
    def _validate_edad(self):
        if not isinstance(self.edad, (int, float)):
            raise exceptions.ValidationError("CAMPO EDAD: Solo puedes introducir números")

    @api.onchange('peso')
    def _onchange_peso(self):
        for animales in self:
            if not isinstance(animales.peso, (int, float)):
                return {
                    'warning': {
                        'title': "Ha ocurrido un error",
                        'message': "CAMPO PESO: Los caracteres deben ser solo numeros."
                    }
                }

    @api.constrains('peso')
    def _validate_peso(self):
        for animales in self:
            if not isinstance(animales.peso, (int, float)):
                raise exceptions.ValidationError("CAMPO PESO: Solo puedes introducir numeros")

    @api.onchange('altura')
    def _onchange_altura(self):
        for animales in self:
            if not isinstance(animales.altura, (int, float)):
                animales.altura = 0

                return {
                    'warning': {
                        'title': "Ha ocurrido un error",
                        'message': "CAMPO ALTURA: Solo puedes introducir números."
                    }
                }

    @api.constrains('altura')
    def _check_altura(self):
        for animales in self:
            if not isinstance(animales.altura, (int, float)):
                raise exceptions.ValidationError("CAMPO ALTURA: Solo puedes introducir números.")

    @api.onchange('especie')
    def _onchange_especie(self):
        for animales in self:
            if isinstance(self.especie, str) and (not self.especie.isalpha() or len(self.especie) > 20):
                return {
                    'warning': {
                        'title': "Ha ocurrido un error",
                        'message': "CAMPO ESPECIE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras."
                    }
                }

    @api.constrains('especie')
    def _validate_especie(self):
        for animales in self:
            if isinstance(self.especie, str) and (not self.especie.isalpha() or len(self.especie) > 20):
                raise exceptions.ValidationError(
                    "CAMPO ESPECIE: Los caracteres deben ser menores o iguales a 20. Además, deben contener solo letras.")

    @api.constrains('alimentacion')
    def _check_alimentacion(self):
        for animales in self:
            allowed_values = ['carnivoro', 'herbivoro', 'omnivoro']
            if animales.alimentacion and animales.alimentacion not in allowed_values:
                raise exceptions.ValidationError("La alimentacion debe ser carnivoro, herbivoro o omnivoro.")

    @api.constrains('salud')
    def _check_salud(self):
        for animales in self:
            allowed_values = ['sano', 'enfermo']
            if animales.salud and animales.salud not in allowed_values:
                raise exceptions.ValidationError("La salud debe ser sano o enfermo.")

    @api.model
    def create(self, vals):
        record = super(animales, self).create(vals)
        return record
