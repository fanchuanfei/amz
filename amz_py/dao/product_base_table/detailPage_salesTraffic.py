# 详情页面销售和流量


class ParentProduct:
    def __init__(self, parent_asin=None,parent_sku=None):
        self.parent_asin = parent_asin  # 父 ASIN
        self.parent_sku = parent_sku   # 父 SKu
        self.child_count = 0  # 子类个数
        self.childs = []  # 容器，存储子类实例

    def add_child(self, child):
        """向父类中添加一个子类实例"""
        if isinstance(child, ChildProduct):
            self.childs.append(child)
            self.child_count += 1
        else:
            print("添加失败：必须是 ProductStats 类型的实例")

    def get_parent_asin(self):
        return self.parent_asin

    def set_parent_asin(self, parent_asin):
        self.parent_asin = parent_asin

    def get_parent_sku(self):
        return self.parent_sku

    def set_parent_sku(self,parent_sku):
        self.parent_sku = parent_sku

    def get_child_count(self):
        return self.child_count

    def get_childs(self):
        return self.childs

class ChildProduct:
    def __init__(self, child_asin=None, title=None, sku=None,  #（子）ASIN  标题  SKU
                 total_sessions=0, total_sessions_b2b=0,  # 会话数
                 page_views_total=0,page_views_total_b2b=0,  # 页面浏览数
                 recommended_offer_percentage=0.0, recommended_offer_percentage_b2b=0.0,  # 推荐报价百分比
                 ordered_items=0,ordered_items_b2b=0, # 已订购商品数量：订购的商品数量
                 product_session_percentage=0.0, product_session_percentage_b2b=0.0,  #商品会话百分比：转化指标（以百分比表示），指售出的商品总数与查看商品的总人数之比
                 ordered_items_sales=0.0, ordered_items_sales_b2b=0.0,  # 已订购商品销售额
                 total_ordered_products=0,total_ordered_products_b2b=0):  # 订单商品总数：订单数量

        self.child_asin = child_asin
        self.title = title
        self.sku = sku
        self.total_sessions = total_sessions
        self.total_sessions_b2b = total_sessions_b2b
        self.page_views_total = page_views_total
        self.page_views_total_b2b = page_views_total_b2b
        self.recommended_offer_percentage = recommended_offer_percentage
        self.recommended_offer_percentage_b2b = recommended_offer_percentage_b2b
        self.ordered_items = ordered_items
        self.ordered_items_b2b = ordered_items_b2b
        self.product_session_percentage = product_session_percentage
        self.product_session_percentage_b2b = product_session_percentage_b2b
        self.ordered_items_sales = ordered_items_sales
        self.ordered_items_sales_b2b = ordered_items_sales_b2b
        self.total_ordered_products = total_ordered_products
        self.total_ordered_products_b2b = total_ordered_products_b2b

    # Getters and Setters for each attribute
    def get_child_asin(self):
        return self.child_asin

    def set_child_asin(self, child_asin):
        self.child_asin = child_asin

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_sku(self):
        return self.sku

    def set_sku(self, sku):
        self.sku = sku

    def get_total_sessions(self):
        return self.total_sessions

    def set_total_sessions(self, total_sessions):
        self.total_sessions = total_sessions

    def get_total_sessions_b2b(self):
        return self.total_sessions_b2b

    def set_total_sessions_b2b(self, total_sessions_b2b):
        self.total_sessions_b2b = total_sessions_b2b

    def get_page_views_total(self):
        return self.page_views_total

    def set_page_views_total(self, page_views_total):
        self.page_views_total = page_views_total

    def get_page_views_total_b2b(self):
        return self.page_views_total_b2b

    def set_page_views_total_b2b(self, page_views_total_b2b):
        self.page_views_total_b2b = page_views_total_b2b

    def get_recommended_offer_percentage(self):
        return self.recommended_offer_percentage

    def set_recommended_offer_percentage(self, recommended_offer_percentage):
        self.recommended_offer_percentage = recommended_offer_percentage

    def get_recommended_offer_percentage_b2b(self):
        return self.recommended_offer_percentage_b2b

    def set_recommended_offer_percentage_b2b(self, recommended_offer_percentage_b2b):
        self.recommended_offer_percentage_b2b = recommended_offer_percentage_b2b

    def get_ordered_items(self):
        return self.ordered_items

    def set_ordered_items(self, ordered_items):
        self.ordered_items = ordered_items

    def get_ordered_items_b2b(self):
        return self.ordered_items_b2b

    def set_ordered_items_b2b(self, ordered_items_b2b):
        self.ordered_items_b2b = ordered_items_b2b

    def get_product_session_percentage(self):
        return self.product_session_percentage

    def set_product_session_percentage(self, product_session_percentage):
        self.product_session_percentage = product_session_percentage

    def get_product_session_percentage_b2b(self):
        return self.product_session_percentage_b2b

    def set_product_session_percentage_b2b(self, product_session_percentage_b2b):
        self.product_session_percentage_b2b = product_session_percentage_b2b

    def get_ordered_items_sales(self):
        return self.ordered_items_sales

    def set_ordered_items_sales(self, ordered_items_sales):
        self.ordered_items_sales = ordered_items_sales

    def get_ordered_items_sales_b2b(self):
        return self.ordered_items_sales_b2b

    def set_ordered_items_sales_b2b(self, ordered_items_sales_b2b):
        self.ordered_items_sales_b2b = ordered_items_sales_b2b

    def get_total_ordered_products(self):
        return self.total_ordered_products

    def set_total_ordered_products(self, total_ordered_products):
        self.total_ordered_products = total_ordered_products

    def get_total_ordered_products_b2b(self):
        return self.total_ordered_products_b2b

    def set_total_ordered_products_b2b(self, total_ordered_products_b2b):
        self.total_ordered_products_b2b = total_ordered_products_b2b