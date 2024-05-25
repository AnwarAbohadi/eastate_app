// Copyright (c) 2024, Eng and contributors
// For license information, please see license.txt

frappe.query_reports["Property"] = {
	"filters": [
		{
			"fieldname": "property",
			"label": __("Property Name"),
			"fieldtype": "Data",
			"width": 100,
			"reqd": 0,
		},
		// why????? don't work
		// {
		// 	"fieldname": "from",
		// 	"label": __("From Date"),
		// 	"fieldtype": "Date",
		// 	"width": 80,
		// 	"reqd": 1,
		// 	"default":dateutil.year_start()
		// },
		// {
		// 	"fieldname": "to",
		// 	"label": __("To Date"),
		// 	"fieldtype": "Date",
		// 	"width": 80,
		// 	"reqd": 1,
		// 	"default":dateutil.year_end()
		// },
		{
			"fieldname": "agent",
			"label": __("Agent Name"),
			"fieldtype": "Link",
			"options": "Agent",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "statas",
			"label": __("Statas"),
			"fieldtype": "Select",
			"options": ['','Sale', 'Rent', 'Lease'],
			"width": 100,
			"reqd": 0,
		}
	]
};

