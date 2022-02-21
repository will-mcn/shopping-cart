# shopping-cart

## Usage
```
python shopping_cart.py
```

## Packages & Setup
Running this program requires setting up a virtual environnment in order to utilize the environment and set the environment variables imbedded within the program.

```
conda create -n sc-env python=3.8
conda activate sc-env
```

To utilize a number of external Python packages, load the requirements.txt file into the virtual environment:

```
pip install -r requirements.txt
```

Required Packages include:
+ python dot-env
+ sendgrid
+ pandas

### CSV File / Invetory Management
The inventory of products used in the program can be updated given the market's needs and changing product offerings. To update, make a copy of the "data/default_products.csv" and save as "data/products.csv" in your copied repo. This will allow for customization of the inputs of inventory whenever necessary without affecting the version control.


### Environment Variables
Environment variables in this program include the tax rate, sender email for the receipt, the store name, as well as your sendgrid API key. In order to edit these, make and add a     .env file to your repository with the following definitions:

Tax rate:
```
TAX_RATE = desired tax rate
```
Email Address:
```
EMAIL_ADDRESS = "johndoe@gmail.com"
```

sendgrid API key:
```
SENDGRID_API_KEY = key
```

Store name (default will be My Store unless changed):
```
STORE_NAME = my store name 
```

## Running the Program
To utilize the program, navigate to the repository via the terminal and input into the command line:
```
python shopping_cart.py
```
