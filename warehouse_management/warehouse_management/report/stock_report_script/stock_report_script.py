# Copyright (c) 2022, Gokul and contributors
# For license information, please see license.txt

from pkgutil import get_data
import frappe


def execute(filters=None):
    columns = [
	{
      "fieldname": "name",
      "fieldtype": "Data",
      "label": "Stock ID",
      "width": 100
    },
	{
      "fieldname": "doctypename",
      "fieldtype": "Link",
      "options": 'DocType',
      "label": "DocType Name",
      "width": 100
    },
	{
      "fieldname": "id",
      "fieldtype": "Dynamic Link",
      "options": 'doctypename',
      "label": "ID",
      "width": 100
    },
	{
      "fieldname": "item_name",
      "fieldtype": "Link",
      "options": 'Item Manager',
      "label": "Item Name",
      "width": 100
    },
	{
      "fieldname": "date",
      "fieldtype": "Date",
      "label": "Date",
      "width": 100
    },
	{
      "fieldname": "qantity_left",
      "fieldtype": "Int",
      "label": "Qantity Left",
      "width": 100
    },
	{
      "fieldname": "qantity_sold",
      "fieldtype": "Int",
      "label": "Qantity Sold",
      "width": 100
    },
	{
      "fieldname": "qantity_bought",
      "fieldtype": "Int",
      "label": "Qantity Bought",
      "width": 100
    },
	{
      "fieldname": "seller_name",
      "fieldtype": "Data",
      "label": "Seller Name",
      "width": 100
    },
	{
      "fieldname": "buyer_name",
      "fieldtype": "Data",
      "label": "Buyer Name",
      "width": 125
    }
	]
    data =get_data(filters)
    return columns, data
def get_data(filters):
	result = []
	data =[]
	if(filters.buyer_name and filters.seller_name):
		if(filters.buyer_name):
			data=frappe.db.sql(""" 
			select name,doctypename,id ,item_name,date,qantity_left,qantity_sold,qantity_bought,seller_name,buyer_name
			from `tabStock Manager`
			where
			date>="{fdate:}"
			and date<="{tdate:}"
			and seller_name="{sname:}"
			or buyer_name="{bname:}"
			""".format(fdate=filters.from_date,tdate=filters.to_date,sname=filters.seller_name,bname=filters.buyer_name))
			#print(3)
			return data
	elif(filters.seller_name):
		data=frappe.db.sql(""" 
		select name,doctypename,id ,item_name,date,qantity_left,qantity_sold,qantity_bought,seller_name,buyer_name
		from `tabStock Manager`
		where
		date>="{fdate:}"
		and date<="{tdate:}"
		and seller_name="{sname:}"
		""".format(fdate=filters.from_date,tdate=filters.to_date,sname=filters.seller_name))
		#print(1)
		return data
	elif(filters.buyer_name):
		data=frappe.db.sql(""" 
		select name,doctypename,id ,item_name,date,qantity_left,qantity_sold,qantity_bought,seller_name,buyer_name
		from `tabStock Manager`
		where
		date>="{fdate:}"
		and date<="{tdate:}"
		and buyer_name="{bname:}"
		""".format(fdate=filters.from_date,tdate=filters.to_date,bname=filters.buyer_name))
		#print(2)
		return data
	else:
		data=frappe.db.sql(""" 
		select name,doctypename,id ,item_name,date,qantity_left,qantity_sold,qantity_bought,seller_name,buyer_name
		from `tabStock Manager`
		where
		date>="{fdate:}"
		and date<="{tdate:}"
		""".format(fdate=filters.from_date,tdate=filters.to_date))
		#print(4)
		return data