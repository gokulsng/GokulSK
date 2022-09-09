// Copyright (c) 2022, Gokul and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Stock Report Script"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "seller_name",
			"label": __("Seller Name"),
			"fieldtype": "Data",
			"default": frappe.defaults.get_user_default("Seller_Name")
		},
		{
			"fieldname": "buyer_name",
			"label": __("Buyer Name"),
			"fieldtype": "Data",
			"default": frappe.defaults.get_user_default("Buyer_Name")
		}
	]
};
