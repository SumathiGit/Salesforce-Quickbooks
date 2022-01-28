from simple_salesforce import Salesforce
import requests
import json
from sqlalchemy import null

session = requests.Session()
sf = Salesforce(
   username='sumathi@sabbatech.com', password='Dhanya@1234', 
   security_token='WpQdoaC54yfSsQPWpuahQLax',session=session)

####CREATE CONTACT######
contact = sf.Contact.create({'LastName':'PSJJ','Email':'psjj@example.com'})
contact_id = contact.get("id")
print(contact_id)
data = sf.Contact.get(contact_id)
#### GET JSON DATA ####
json_object = json.dumps(data, indent = 4) 
print(json_object)


####CREATE OPPORTUNITY#####
invoice = sf.Opportunity.create({'name':"PJJJ", 'amount':6000, 
"StageName": "Posted", "CloseDate": "2026-11-14"})  #json Invoice
invoice_id = invoice.get('id')
print(invoice_id)
output = sf.Opportunity.get(invoice_id)
#### GET JSON DATA ####
json_obj = json.dumps(output, indent = 4) 
print(json_obj)


pj = sf.Opportunity.get("0065j00000RHGmS")
js = json.dumps(pj, indent=4)
print(js)





