from odoo import models, fields, api
from odoo.exceptions import UserError


class usuarios(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    # Verificamos el tipo de usuario
    is_admin = fields.Boolean(string="Admin")
    is_client = fields.Boolean(string="Client")

    # Comprueba que solo sea o Invitado o Librero nunca ambas a la vez
    @api.constrains('groups_id')
    def _check_user_group(self):
        for user in self:
            groups = user.groups_id
            group_names = groups.mapped('name')
            if "Admin" in group_names:
                if "Cliente" in group_names:
                    raise UserError("El usuario solo puede pertenecer a un grupo")

    cliente_entrada_ids = fields.One2many("grupo3c.entradas", 'client_id', string="Id entrada")
    admin_entrada_ids = fields.One2many("grupo3c.entradas", 'admin_id', string="Id entrada")
    admin_zonas_ids = fields.One2many("grupo3c.zonas", 'id_admin', string="Id zona")
    admin_animales_ids = fields.One2many("grupo3c.animales", 'admin_id', string="Id animal")
