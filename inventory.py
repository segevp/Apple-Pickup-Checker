from utils import compose_url_params
from requests import get

REQUEST_URL = "https://www.apple.com/shop/fulfillment-messages"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT
}


class InventoryLookup:
    def __init__(self, model, zipcode):
        self.model = model
        self.zipcode = zipcode
        self.stores = self.request_stock()
        self.model_name = self.stores[0]['partsAvailability'][model]['storePickupProductTitle']

    def request_stock(self):
        params = {
            "parts.0": self.model,
            "location": self.zipcode,
            "pl": "true",
            "cppart": "UNLOCKED/US"
        }
        formatted_url = f"{REQUEST_URL}/{compose_url_params(params)}"
        response = get(formatted_url, headers=REQUEST_HEADERS).json()
        all_stores = response['body']['content']['pickupMessage']['stores']
        return all_stores

    def is_available(self, store):
        return store['partsAvailability'][self.model]['pickupDisplay'] == 'available'

    @property
    def available_stores(self):
        return [store for store in self.stores if self.is_available(store)]
