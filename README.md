# shopping-cart

## Usage
```
python shopping_cart.py
```

## Packages & Setup
Running this program requires setting up a seperate virtual environnment in order to utilize the environment and set the environment variables imbedded within the program.

```
conda create -n sc-env python=3.8
conda actviate sc-env
```

To utilize a number of external Python packages, load the requirements.txt file into the virtual environment:

```
pip install -r requirements.txt
```

Environment variables in this program include the tax rate, sender email for the receipt, as well as your sendgrid API key. In order to edit these, make and add a .env file to your repository with the following definitions:

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


