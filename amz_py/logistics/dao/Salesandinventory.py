
# 当天的库存 和 前七天的销售数量
class SalesInventory:

    def __init__(self, asin, sku, product_name, currentAndReserve_inventory=None, Inbound_inventory=None, Sales_seven=None):
        self.asin = asin
        self.sku = sku
        self.product_name = product_name
        self.currentAndReserve_inventory = currentAndReserve_inventory
        self.Inbound_inventory = Inbound_inventory
        self.Sales_seven = Sales_seven

    def get_asin(self) -> str:
        return self.asin

    def set_asin(self, value: str):
        self.asin = value

    # Getter and Setter for sku
    def get_sku(self) -> str:
        return self.sku

    def set_sku(self, value: str):
        self.sku = value

    # Getter and Setter for product_name
    def get_product_name(self) -> str:
        return self.product_name

    def set_product_name(self, value: str):
        self.product_name = value

    # Getter and Setter for current_inventory
    def get_current_inventory(self) -> int:
        return self.currentAndReserve_inventory

    def set_current_inventory(self, value: int):
        self.currentAndReserve_inventory = value

    # Getter and Setter for preSevenSales
    def get_quality(self) -> int:
        return self.Sales_seven

    def set_quality(self, value: int):
        self.Sales_seven = value


    def add_quality(self,quality):
        self.Sales_seven+=quality

