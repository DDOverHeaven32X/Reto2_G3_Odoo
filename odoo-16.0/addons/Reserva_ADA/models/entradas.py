from odoo import models, fields, api, exceptions




class entradas(models.Model):
   _name = 'grupo3c.entradas'
   # Precio de la entrada
   precio = fields.Float(required=True, string="Precio");
   fecha_entrada = fields.Date(required=True, string="Fecha")
   tipo_entrada = fields.Selection([('Reducida', 'Normal', 'Infantil', 'Senior')], string="Tipo de entrada",
                                   required=True)
   client_id = fields.Many2one('res.users', string="Cliente")
   admin_id = fields.Many2one('res.users', string="Admin")
   zona_id = fields.Many2many('grupo3c.zonas', string="Código de Zona")


   @api.onchange('fecha_entrada')
   def _onchange_fecha_entrada(self):
       if self.fecha_entrada and self.fecha_entrada < fields.Date.today():
           return {
               'warning': {
                   'title': "Advertencia",
                   'message': "La fecha no puede ser inferior a la actual."
               }
           }


   @api.constrains('fecha_entrada')
   def _check_fecha_entrada(self):
       for entradas in self:
           if fields.Date.from_string(entradas.fecha_entrada) < fields.Date.from_string(fields.Date.today()):
               raise exceptions.ValidationError("La fecha no puede ser inferior a la actual")


   @api.onchange('precio')
   def _onchange_precio(self):
       if not isinstance(self.precio, (int, float)):
           return {
               'warning': {
                   'title': "Advertencia",
                   'message': "El precio debe ser un valor numérico."
               }
           }


   @api.constrains('precio')
   def _check_precio(self):
       for entradas in self:
           if entradas.precio.isalpha():
               raise exceptions.ValidationError("No puedes introducir letras en el precio")

   @api.constrains('tipo_entrada')
   def _check_tipo_entrada(self):
       for entradas in self:
           allowed_values = ['Reducida', 'Normal', 'Infantil', 'Senior']
           if self.tipo_entrada and self.tipo_entrada not in allowed_values:
               raise exceptions.ValidationError("Las posibles opciones para crear un tipo de entrada son: 'Reducida, Normal, Infantil y Senior.")

   @api.model
   def create(self, vals):
       record = super(entradas, self).create(vals)
       return record