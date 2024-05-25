# Copyright (c) 2024, Eng and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class Property(Document):
    def after_insert(self):
        frappe.msgprint((f"Document {self.name} inserted successfully"));
	# validate
    # def validate(self):
    ################################################# lesson error log######################################################
            #   try:
            #           frappe.db.sql("""select name, tenant, friend from `tabProperty`;""")
            #   except Exception as e:
            #           error = frappe.log_error(frappe.get_traceback(), f"{e}")
            #           frappe.msgprint((f"An error occurred see <a href = '/app/error-log/{error.name}'><b>{error.name}</b></a>"));
	 #######################################################################################################
    # 	if(self.property_type=="Flat"):
	# 		for amenity in self.amenities:
	# 			if (amenity.amenity=="Outdoor Kitchen"):
	# 				frappe.throw((f'Property of type <b>Flat</b> should not have amenity <b>{amenity.amenity}</b>'))
            # sql
			# amenity = frappe.db.sql(f"""select amenity from `tabProperty Amenity Detail` where parent="000002" and parenttype="Property" and amenity ="Outdoor Kitchen";""",as_dict=True)
			# if(amenity):
			# 	frappe.throw((f'Property of type <b>Flat</b> should not have amenity <b>{amenity[0].amenity}</b>'))
     