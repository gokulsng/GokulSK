# Copyright (c) 2022, Gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ReturnManager(Document):
	def before_save(self):
		if frappe.db.exists("Stock Manager",{"item_name":self.item_name}):
			if frappe.db.exists("Stock Manager",{"Buyer_name":self.buyer_name}):
				self.qantity_sold=frappe.db.get_value("Sales Manager",{"item_name":self.item_name,"buyer_name":self.buyer_name},'qantity_sold')
				self.price=frappe.db.get_value("Sales Manager",{"item_name":self.item_name,"buyer_name":self.buyer_name},'price')
			else:
				frappe.throw("Enter Valid Buyer Name!!!")
		if(self.qantity_return>self.qantity_sold):
			frappe.throw("Entered Return value is excess!!!")
		sales_id=frappe.db.get_value("Sales Manager",{"item_name":self.item_name,"buyer_name":self.buyer_name},'name')
	def before_submit(self):
		self.qantity_sold=self.qantity_sold-self.qantity_return
		new_stock=frappe.new_doc("Stock Manager")
		new_stock.sales_id=frappe.db.get_value("Sales Manager",{"item_name":self.item_name,"buyer_name":self.buyer_name},'name')
		new_stock.doctypename=self.doctype
		new_stock.id=self.name
		new_stock.item_name=self.item_name
		new_stock.qantity_left=frappe.db.get_value("Stock Manager",{"item_name":self.item_name},"qantity_left")
		new_stock.qantity_return=self.qantity_return
		new_stock.qantity_sold=self.qantity_sold
		new_stock.date=self.date
		new_stock.buyer_name=self.buyer_name
		new_stock.save()