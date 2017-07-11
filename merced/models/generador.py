from odoo import api, exceptions, fields, models

class Generador(models.Model):
    _inherit = 'product.template'

    class_id = fields.Many2one('classification.product', string="Clasificacion")
    msj_error = fields.Char(readonly=True)

    @api.multi
    def imprimir(self):
        try:
	    prov_id = self.seller_ids[0].name
	    ident_prov = prov_id.x_identificador
	    if ident_prov == False:
	    	print "*************************************** elif"
	        self.write({'barcode': ''})
	       	self.write({'msj_error': 'Por favor agregue un identificador al proveedor'})	
	    else:
	       numero = 1000000000 + self.id
	       num_str = str(numero)
	       cod_barras = str(ident_prov) + str(num_str[1:10])
               self.write({'barcode': cod_barras})
	       self.write({'msj_error': ' '})
	except IndexError as e:
	    self.write({'barcode': ' '})
	    self.write({'msj_error': 'Por favor agregue un proveedor '})
