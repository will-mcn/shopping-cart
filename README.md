# shopping-cart

## Packages & Setup
Running this program requires setting up a virtual environnment in order to utilize certain packages and set up the environment variables imbedded within the program.

```
conda create -n sc-env python=3.8
conda activate sc-env
```

Required Python packages include:
+ python dot-env
+ sendgrid
+ pandas

To utilize the above packages, load the requirements.txt file into the virtual environment:

```
pip install -r requirements.txt
```

### CSV File / Inventory Management
The inventory of products used in the program can be updated given the market's needs and changing product offerings. To update, make a copy of the "data/default_products.csv" and save as "data/products.csv" in your copied repo. This will allow for customization of product inventory whenever necessary without affecting the version control.

### Environment Variables
Environment variables in this program include the tax rate, sender email for the receipt, the store name, as well as your sendgrid API key. In order to edit these, make and add a     .env file to your repository with the following definitions:

Tax rate:
```
TAX_RATE = desired tax rate
```
Sender Email Address for Receipt:
```
SENDER_ADDRESS = "johndoe@gmail.com"
```

sendgrid API key:
```
SENDGRID_API_KEY = API key
```

Market name (default will be My Store unless changed):
```
MARKET_NAME = my store name 
```

Market Email & Phone Number (to offer the customer your Customer Service contact information):
```
MARKET_EMAIL = help@mymarket.com
MARKET_PHONE=(202)-687-0100
```

Market Location:
```
MARKET_LOC= Store address
```

## Running the Program
To utilize the program, navigate to the repository via the terminal and input into the command line:
```
python shopping_cart.py
```

Happy Shopping!