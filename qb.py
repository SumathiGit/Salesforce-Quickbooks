from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.account import Account
from quickbooks.objects.salesreceipt import SalesReceipt



auth_client = AuthClient(
    client_id = "ABReJcA0mlEPksY8MLzZdecQ0QexZdgvpmCeCMN8nLZDoRDJlo" # from QB website
    ,client_secret = "DQcxveegV0PxVSdi3KLQQaCp2MsZGHz77A50LVcO" # from QB website
    ,environment = 'sandbox' # or 'production'
    ,redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
)

client = QuickBooks(
    auth_client = auth_client
    ,refresh_token = "AB11652071121U36Gtl6Xx5inGSFQgHD5ClaKJVXZXx7r03xkY"
    ,company_id = "4620816365204373380"
)

###QUERY CUSTOMERS####
customers = Customer.all(qb=client)
customers = Customer.filter(start_position=1, max_results=5,qb=client)
print(customers)


##QUERY INVOICE####
invoices = Invoice.filter(start_position=1, max_results=5, qb=client)
print(invoices)

#####READ INVOICE#####

inv = Invoice.get(id="150", qb = client)
json_data = inv.to_json()
print(json_data)

####CREATE INVOICE####

salesreceipt = SalesReceipt()
salesreceipt.from_json(
{
  "Line": [
    {
      "Description": "Pest Control Services", 
      "DetailType": "SalesItemLineDetail", 
      "SalesItemLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        }, 
        "Qty": 1, 
        "UnitPrice": 35, 
        "ItemRef": {
          "name": "Pest Control", 
          "value": "10"
        }
      }, 
      "LineNum": 1, 
      "Amount": 35.0, 
      "Id": "1"
    }
  ]
}
)
salesreceipt.save(qb=client, request_id="153")

###QUERY SALESRECEIPT###
sr = SalesReceipt.get(id="153", qb = client)
jso_data = sr.to_json()
print(jso_data)