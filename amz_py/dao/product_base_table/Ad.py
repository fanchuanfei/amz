
# 广告关键词表

# 广告总数据

# 作用 1.用于找到对应的产品基础表， 2. 算总点击
class AdCampaign:

    # 广告活动名称为 key ，广告对象为value
    ManualAd_dict: dict = {}
    AutomaticAd_dict: dict = {}

    def __init__(self, Ad_portfolio_name):
        self.Ad_portfolio_name = Ad_portfolio_name  # 广告组合名称


    def get_campaign_name(self):
        return self.campaign_name

    def set_campaign_name(self, campaign_name):
        self.campaign_name = campaign_name

    def get_impressions(self):
        return self.impressions

    def set_impressions(self, impressions):
        self.impressions = impressions

    def get_clicks(self):
        return self.clicks

    def set_clicks(self, clicks):
        self.clicks = clicks

    def get_spend(self):
        return self.spend

    def set_spend(self, spend):
        self.spend = spend

    def get_acos(self):
        return self.acos

    def set_acos(self, acos):
        self.acos = acos

    def get_ctr(self):
        return self.ctr

    def set_ctr(self, ctr):
        self.ctr = ctr

    def get_cpc(self):
        return self.cpc

    def set_cpc(self,cpc):
        self.cpc = cpc

    def get_sales(self):
        return self.sales

    def set_sales(self,sales):
        self.sales = sales

    def get_sales_revenue(self):
        return self.sales_revenue

    def set_sales_revenue(self,sales_revenue):
        self.sales_revenue = sales_revenue

# 关键词

class ManualAdKeyword(AdCampaign):


    def __init__(self, keyword, match_type, campaign_name, impressions, clicks, spend, acos, ctr, cpc, sales,
                 sales_revenue):
        super().__init__(campaign_name, impressions, clicks, spend, acos, ctr, cpc, sales, sales_revenue)
        self.keyword = keyword  # 客户搜索词

    def get_keyword(self):
        return self.keyword

    def set_keyword(self, keyword):
        self.keyword = keyword


class AutomaticAdKeyword(AdCampaign):


    def __init__(self, keyword, match_type, campaign_name, impressions, clicks, spend, acos, ctr, cpc, sales,
                 sales_revenue):
        super().__init__(campaign_name, impressions, clicks, spend, acos, ctr, cpc, sales, sales_revenue)
        self.keyword = keyword  # 客户搜索词

    def get_keyword(self):
        return self.keyword

    def set_keyword(self, keyword):
        self.keyword = keyword



# 手动广告

class ManualAd(AdCampaign):

    accurate_keywords: dict = {}
    widely_keywords: dict = {}
    phrase_keywords: dict = {}

    def __init__(self, campaign_name, impressions, clicks, spend, acos, ctr, cpc, sales, sales_revenue,
                 Ad_portfolio_name):
        super().__init__(Ad_portfolio_name)

        self.impressions = impressions  # 展示量
        self.clicks = clicks  # 点击量
        self.spend = spend  # 花费
        self.acos = acos  # 广告成本销售比(ACOS)
        self.ctr = ctr  # 点击率(CTR)
        self.cpc = cpc  # 每次点击成本
        self.sales = sales  # 销量
        self.sales_revenue = sales_revenue  # 销售额

    def add_accurate_keywords(self, keyword: Keyword):
        self.accurate_keywords.update({keyword.keyword: keyword})

    def get_accurate_keywords(self):
        return self.accurate_keywords

# 自动广告

class AutomaticAd(AdCampaign):

    accurate_keywords: dict = {}
    widely_keywords: dict = {}
    phrase_keywords: dict = {}

    def __init__(self, campaign_name, impressions, clicks, spend, acos, ctr, targeting_type, cpc, sales, sales_revenue):
        super().__init__(campaign_name, impressions, clicks, spend, acos, ctr, cpc, sales, sales_revenue)
        self.targeting_type = targeting_type  # 自动广告的匹配方式（如：自动匹配）

    def get_targeting_type(self):
        return self.targeting_type

    def set_targeting_type(self, targeting_type):
        self.targeting_type = targeting_type




