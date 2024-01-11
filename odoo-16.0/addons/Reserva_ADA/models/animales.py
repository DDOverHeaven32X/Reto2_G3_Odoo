# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions


class animales(models.Model):
   _name = 'grupo3c.animales'
   #Nombre del animal
   nombre = fields.Text(required= True, string="Nombre")
   genero = fields.Text(required= True, string="Genero")
   edad = fields.Integer(required= True, string="Edad")
   peso = fields.Float(required= True, string="Peso")
   altura = fields.Float(required= True, string="Altura")
   especie = fields.Text(required= True, string="Especie")
   alimentacion = fields.Selection([
                      ('carnivoro', 'Carnivoro'),
                      ('herbivoro', 'Herbivoro'),
                      ('omnivoro', 'Omnivoro')
                   ], string ='Alimentacion', required = True)
   salud = fields.Selection([
                      ('sano', 'Sano'),
                      ('enfermo', 'Enfermo')
                   ], string ='Salud', required = True)


   admin_id = fields.Many2one('res.users', string="Admin")
   zona_id = fields.Many2one('grupo3c.zonas', string="codigo_zona")


   @api.constrains('nombre')
   def _validate_nombre(self):
       for animales in self:
           if not animales.nombre.isalpha():
               raise exceptions.ValidationError("Solo puedes introducir letras")


   @api.constrains('genero')
   def _validate_genero(self):
       for animales in self:
           if not animales.genero.isalpha():
               raise exceptions.ValidationError("Solo puedes introducir letras")


   @api.constrains('edad')
   def _validate_edad(self):
       for animales in self:
           if animales.edad.isalpha():
               raise exceptions.ValidationError("Solo puedes introducir numeros")


   @api.constrains('peso')
   def _validate_peso(self):
       for animales in self:
           if animales.peso.isalpha():
               raise exceptions.ValidationError("Solo puedes introducir numeros")


   @api.constrains('altura')
   def _validate_altura(self):
       for animales in self:
           if animales.altura.isalpha():
               raise exceptions.ValidationError("Solo puedes introducir numeros")


   @api.constrains('especie')
   def _validate_especie(self):
       for animales in self:
           if not animales.especie.isalpha():
               raise exceptions.ValidationError("Solo puedes introducir letras")


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