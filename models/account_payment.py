from odoo import api, fields, models 
import logging
_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
	_inherit = 'account.payment'

	def executePost(self, post_id):
		_logger.info("HEMOS ENTRADO\n")
		payment_obj = self.browse(post_id)
		_logger.info("VALUE: %s" % payment_obj)
		return payment_obj.post() if payment_obj else {}
