# This is the shopping_cart.py file

# Import packages
import os
from pandas import read_csv
from datetime import datetime 
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

# CSV File Reading & Input Reading
# If there are products you would like to add or take off from the inputs, do so in the products.csv file 
csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")

df = read_csv(csv_filepath)

# convert input DataFrame to a list of dictionaries
products = df.to_dict('records')

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#USER INFORMATION CAPTURE
cust_total = 0
selected_ids = []

while True: 
    product_id = input("Please input a product identifier, or 'DONE' if there are no remaining items: ")
    if product_id == "DONE":
        break
    else:
       selected_ids.append(product_id)

# PRINTING RECEIPT
MARKET_NAME = os.getenv("STORE_NAME", default = "MY MARKET")
MARKET_EMAIL = os.getenv("STORE_EMAIL", default = "HELP@MYMARKET.COM" )
print('------------------------------------------')
print(MARKET_NAME)
print("(202)-687-0100", "|", "3700 O ST. NW WASHINGTON, DC 20057" )
print(f"QUESTIONS? REACH US AT: {MARKET_EMAIL}")

print('------------------------------------------')

now =datetime.now()
today = now.strftime("%Y-%m-%d %H:%M %p")

print("CHECKOUT AT:", today)

print('------------------------------------------')

# Loop through products and store selected products via list comprehension, and print the result for the customer 
html_receipt = ""
for product_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    cust_total = cust_total + matching_product["price"]
    print("SELECTED PRODUCT:" + matching_product['name'], to_usd(matching_product['price']))
    html_receipt += f"<li>{matching_product['name']} ({to_usd(matching_product['price'])}) </li>" 
print("TOTAL PRICE:", to_usd(cust_total))

# Customer Total
print('------------------------------------------')
print("SUBTOTAL:", to_usd(cust_total))

tax_rate = float(os.getenv("TAX_RATE", default = 0.0875))
total_tax = tax_rate * cust_total
print(f"TAX: ({to_usd(total_tax)})")

print("CUSTOMER TOTAL:", to_usd(total_tax + cust_total))
print('------------------------------------------')

# Sending Receipts via Email
# Clyde assisted with  the HTML language text setup 
cust_e_choice = input("Would you like an email copy of your receipt? (Y/N):")
if cust_e_choice == "Y":
    cust_email = input("Please enter a valid email address:")

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="Please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="Please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    subject = f"Your receipt from {MARKET_NAME}"

    html_content = f"""
    <h1> {MARKET_NAME} </h1>

    <h3> Customer Receipt: </h3> 

    <p>Date: {today} </p>

    <ol>
        {html_receipt}
    </ol>

    <p>SUBTOTAL: {to_usd(cust_total)} </p>
    <p>TAX DUE: +{to_usd(total_tax)} </p>
    <p>TOTAL: {to_usd(total_tax + cust_total)} </p>

    <h3>Thank you for shopping with us today! </h3>
    """

    print("HTML:", html_content)
    message = Mail(from_email=SENDER_ADDRESS, to_emails=cust_email, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) 
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)

    print("RECEIPT SENT. HAVE A NICE DAY!")

else: #if the customer does not want an emailed receipt
    print("THANK YOU FOR SHOPPING WITH US. PLEASE COME AGAIN SOON!")

