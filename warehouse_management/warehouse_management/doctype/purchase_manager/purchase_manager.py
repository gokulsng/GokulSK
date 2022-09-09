# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class PurchaseManager(Document):
	def before_save(self):
		self.expense = self.qantity_bought * self.price
		if frappe.db.exists("Stock Manager",{"item_name":self.item_name}):
			qantity_left=frappe.db.get_value("Stock Manager",{"item_name":self.item_name},"qantity_left")
			self.qantity_left=qantity_left+self.qantity_bought
		else:
			self.qantity_left=self.qantity_bought
	def before_submit(self):
		new_stock=frappe.new_doc("Stock Manager")
		new_stock.doctypename=self.doctype
		new_stock.id=self.name
		new_stock.item_name=self.item_name
		new_stock.qantity_left=self.qantity_left
		new_stock.qantity_bought=self.qantity_bought
		new_stock.date=self.date
		new_stock.save()