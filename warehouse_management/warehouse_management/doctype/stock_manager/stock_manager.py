# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt
from datetime import date
from sqlite3 import Date
import frappe
from frappe.model.document import Document

class StockManager(Document):
	def before_save(self):
		if frappe.db.exists(self.doctypename,self.id):
			if self.doctypename=="Sales Manager":
				item_name ,qantity_sold ,buyer_name,date= frappe.db.get_value('Sales Manager', self.id, ['item_name', 'qantity_sold', 'buyer_name','date'])
				self.item_name= item_name
				self.qantity_sold= qantity_sold
				qantity_left= frappe.db.get_value('Stock Manager',{"item_name":self.item_name},"qantity_left")
				self.qantity_left=self.qantity_left-qantity_sold
				self.buyer_name= buyer_name
				self.date=date
			else:
				item_name ,qantity_left,qantity_bought ,seller_name,date= frappe.db.get_value('Purchase Manager', self.id, ['item_name', 'qantity_left','qantity_bought','seller_name','date'])
				self.item_name= item_name
				self.qantity_left=qantity_left
				self.qantity_bought=qantity_bought
				self.seller_name= seller_name
				self.date=date