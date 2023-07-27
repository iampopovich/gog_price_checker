import requests
import re
from threading import Thread
import sys
import logging
COUNTRIES = {
    "US": "United States",
    "AR": "Argentina",
    "BS": "Bahamas",
    "BR": "Brazil",
    "CA": "Canada",
    "CL": "Chile",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "GL": "Greenland",
    "MX": "Mexico",
    "PA": "Panama",
    "VE": "Venezuela",
    "AL": "Albania",
    "AD": "Andorra",
    "AT": "Austria",
    "BE": "Belgium",
    "BA": "Bosnia and Herzegovina",
    "BG": "Bulgaria",
    "HR": "Croatia",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "EE": "Estonia",
    "FI": "Finland",
    "FR": "France",
    "DE": "Germany",
    "GR": "Greece",
    "HU": "Hungary",
    "IS": "Iceland",
    "IE": "Ireland",
    "IM": "Isle of Man",
    "IT": "Italy",
    "LV": "Latvia",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MT": "Malta",
    "MD": "Moldova",
    "MC": "Monaco",
    "ME": "Montenegro",
    "NL": "Netherlands",
    "MK": "North Macedonia",
    "NO": "Norway",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "RS": "Serbia",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "ES": "Spain",
    "SE": "Sweden",
    "CH": "Switzerland",
    "TR": "Turkey",
    "UA": "Ukraine",
    "UK": "United Kingdom",
    "AU": "Australia",
    "BD": "Bangladesh",
    "KH": "Cambodia",
    "CN": "China",
    "HK": "Hong Kong SAR China",
    "IN": "India",
    "ID": "Indonesia",
    "JP": "Japan",
    "MY": "Malaysia",
    "MN": "Mongolia",
    "NZ": "New Zealand",
    "PH": "Philippines",
    "SG": "Singapore",
    "LK": "Sri Lanka",
    "TW": "Taiwan",
    "VN": "Vietnam",
    "DZ": "Algeria",
    "AM": "Armenia",
    "EG": "Egypt",
    "GE": "Georgia",
    "IL": "Israel",
    "KZ": "Kazakhstan",
    "MA": "Morocco",
    "NG": "Nigeria",
    "QA": "Qatar",
    "SA": "Saudi Arabia",
    "ZA": "South Africa",
    "AE": "United Arab Emirates"}

GOG_API_URL = "https://api.gog.com / products"
GOG_PRICE_URL = "https://api.gog.com/products/%ID%/prices?countryCode=%CODE%"
COUNTRY_PRICES = {}

logging.basicConfig(
    level=logging.DEBUG,
)

def extract_product_id(url):
    html = requests.get(url)
    # TODO: 27.07.2023-10:51 регулярка на продакт ид
    raw_card_product = re.search(r"card-product=\"\d*\"", html.text).group()
    product_id = re.search(r"(\d+)", raw_card_product).group()
    logging.debug(f"raw product id: {raw_card_product}")
    logging.debug(f"product id: {product_id}")
    return product_id


def request_price(product_id, country_code):
    url = f"https://api.gog.com/products/{product_id}/prices?countryCode={country_code}"
    logging.debug(url)
    response = requests.get(url)
    logging.debug(response.json())



def request_prices(product_id):
    request_price(product_id, "AR")


def sort_prices():
    pass


def out_result():
    pass


def main(args):
    game_url = "https://www.gog.com/game/diablo"
    product_id = extract_product_id(game_url)
    request_prices(product_id)
    out_result()


if __name__ == "__main__":
    args = sys.argv
    main(args)


{'_links':
     {'self':
          {'href': '/api/products/1412601690/prices?countryCode=AR'},
      'product':
          {'href': 'https://api.gog.com/api/products/1412601690'}
      },
 '_embedded': {
     'prices': [
         {'currency': {'code': 'USD'}, 'basePrice': '999 USD', 'finalPrice': '999 USD', 'bonusWalletFunds': '0 USD'}]}}
