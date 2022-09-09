# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesManager(Document):
	def before_save(self):
		self.paid = self.qantity_sold * self.price
		if frappe.db.exists("Stock Manager",{"item_name":self.item_name}):
			qantity_left=frappe.db.get_value("Stock Manager",{"item_name":self.item_name},"qantity_left")
			if qantity_left>0:
				qantity_sold=self.qantity_sold
				if qantity_sold>qantity_left:
					frappe.throw("Insufficient Stock,Reduce the order or Cancel")
			else:
				frappe.throw("No stock left ,Purchase other item or Cancel this sale")
		else:
			frappe.throw("No product sold of this name search valid name or other product")
	def before_submit(self):
		new_stock=frappe.new_doc("Stock Manager")
		new_stock.doctypename=self.doctype
		new_stock.id=self.name
		new_stock.item_name=self.item_name
		new_stock.qantity_left=frappe.db.get_value("Stock Manager",{"item_name":self.item_name},"qantity_left")
		new_stock.date=self.date
		new_stock.buyer_name=self.buyer_name
		new_stock.save()