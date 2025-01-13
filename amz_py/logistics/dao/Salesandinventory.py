
# 当天的库存 和 前七天的销售数量
class SalesInventory:

    def __init__(self, asin, sku, product_name, quality=None, current_inventory=None):
        self.asin = asin
        self.sku = sku
        self.product_name = product_name
        self.current_inventory = current_inventory
        self.quality = quality

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
        return self.current_inventory

    def set_current_inventory(self, value: int):
        self.current_inventory = value

    # Getter and Setter for preSevenSales
    def get_quality(self) -> int:
        return self.quality

    def set_quality(self, value: int):
        self.quality = value


    def add_quality(self,quality):
        self.quality+=quality

