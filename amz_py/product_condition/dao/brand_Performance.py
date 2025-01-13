

# 品牌绩效
class ProductPerformance:
    def __init__(self, asin=None, title=None, brand_name=None,
                 avg_customer_review=0.0, # 评分
                 customer_reviews_count=0, # 评分数量
                 sales_rank=0):  #销售排名
        self.asin = asin
        self.title = title
        self.brand_name = brand_name
        self.avg_customer_review = avg_customer_review
        self.customer_reviews_count = customer_reviews_count
        self.sales_rank = sales_rank

    # Getters and Setters for each attribute
    def get_asin(self):
        return self.asin

    def set_asin(self, asin):
        self.asin = asin

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_brand_name(self):
        return self.brand_name

    def set_brand_name(self, brand_name):
        self.brand_name = brand_name

    def get_avg_customer_review(self):
        return self.avg_customer_review

    def set_avg_customer_review(self, avg_customer_review):
        self.avg_customer_review = avg_customer_review

    def get_customer_reviews_count(self):
        return self.customer_reviews_count

    def set_customer_reviews_count(self, customer_reviews_count):
        self.customer_reviews_count = customer_reviews_count

    def get_sales_rank(self):
        return self.sales_rank

    def set_sales_rank(self, sales_rank):
        self.sales_rank = sales_rank
