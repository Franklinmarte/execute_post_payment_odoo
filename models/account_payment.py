from odoo import api, fields, models 


class AccountPayment(models.Model):
	_inherti = 'account.payment'

	def executePost(self, post_id):
		payment_obj = self.browse(post_id)
		return payment_obj.post()
