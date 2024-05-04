import requests

class OdooOrderAutomation:
    """
    Class to handle the automation of getting bill orders from Odoo to an external endpoint.

    Attributes:
    - odoo_url: str
        The URL of the Odoo instance to fetch bill orders from.
    - external_endpoint: str
        The URL of the external endpoint to send the bill orders to.
    """

    def __init__(self, odoo_url: str, external_endpoint: str):
        """
        Constructor to instantiate the OdooOrderAutomation class.

        Parameters:
        - odoo_url: str
            The URL of the Odoo instance to fetch bill orders from.
        - external_endpoint: str
            The URL of the external endpoint to send the bill orders to.
        """

        self.odoo_url = odoo_url
        self.external_endpoint = external_endpoint

    def get_bill_orders_from_odoo(self):
        """
        Fetches bill orders from the Odoo instance.

        Returns:
        - dict:
            A dictionary containing the bill orders fetched from Odoo.
        """

        # Make a GET request to the Odoo URL to fetch bill orders
        response = requests.get(self.odoo_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch bill orders from Odoo. Status Code: {response.status_code}")

    def send_bill_orders_to_external_endpoint(self, bill_orders: dict):
        """
        Sends the bill orders to the external endpoint.

        Parameters:
        - bill_orders: dict
            A dictionary containing the bill orders to be sent.

        Returns:
        - str:
            A message indicating the success of sending the bill orders.
        """

        # Make a POST request to the external endpoint to send bill orders
        response = requests.post(self.external_endpoint, json=bill_orders)

        if response.status_code == 200:
            return "Bill orders sent successfully to the external endpoint."
        else:
            raise Exception(f"Failed to send bill orders to the external endpoint. Status Code: {response.status_code}")

# Example of using the OdooOrderAutomation class:

# Initialize the OdooOrderAutomation instance with Odoo URL and external endpoint URL
odoo_automation = OdooOrderAutomation("https://odoo-instance.com/bill_orders", "https://external-endpoint.com/receive_orders")

# Get bill orders from Odoo
bill_orders = odoo_automation.get_bill_orders_from_odoo()
print("Fetched bill orders from Odoo:", bill_orders)

# Send bill orders to external endpoint
response_message = odoo_automation.send_bill_orders_to_external_endpoint(bill_orders)
print(response_message)