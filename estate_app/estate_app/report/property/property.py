# Copyright (c) 2024, Eng and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
from frappe import _
import frappe
# import dateutil.parser

def execute(filters=None):
	
	return get_columns(), get_data(filters)

def get_data(filters):
	print(f"\n\n\n{filters}\n\n\n")

	# _from, to = filters.get('from'), filters.get('to')  date range
    # conditions
	conditions = "1=1" # when work date add and to begin conditions
	if(filters.get('property')):conditions += f"AND name like '%{filters.get('property')}'"
	if(filters.get('agent')):conditions += f"AND agent= '{filters.get('agent')}'"
	if(filters.get('statas')):conditions += f"AND statas= '{filters.get('statas')}'"
    # sql don't work, why?????
	data = frappe.db.sql(f"""select name, property_name, address, property_type, 
					  statas, property_price, discount, grant_total, agent, agent_name from 
					  `tabProperty` where {conditions}; """) # when work date add (creation between '{_form}' and '{to}') befor word conditions
	return  data



def get_columns():
	return [
         "ID:Link/Property:70",
		 "Property Name:Data:150",
		 "Address:Data:150",
		 "Type:Data:50",
		 "Statas:Data:80",
		 "Price:Currency:100",
		 "Discount:Percent:20",
		 "Grant Total:Currency:100",
		 "Agent:Data:100",
		 "Agent Name:Data:150",
	]
