
# 广告关键词表

# 广告总数据

# 作用 1.用于找到对应的产品基础表， 2. 算总点击
class AdCampaign:

    # 广告活动名称为 key ，广告对象为value
    # 存放自动和手动广告
    ManualAd_dict: dict = {}
    AutomaticAd_dict: dict = {}

    def __init__(self, Ad_portfolio_name):
        self.Ad_portfolio_name = Ad_portfolio_name  # 广告组合名称


    # 添加手动广告词
    def add_ManualAd_keyword(self,adKeyword):
        self.ManualAd_dict.update()

# 关键词


class AdKeyword:

    def __init__(self,campaign_name,Ad_Group_Name,match_type, keyword,  impressions, clicks, ctr, cpc, spend, sales_revenue, acos, sales,cr):
        self.campaign_name = campaign_name  # 自动广告的匹配方式（如：自动匹配）
        self.Ad_Group_Name = Ad_Group_Name
        self.match_type = match_type
        self.keyword = keyword  # 客户搜索词
        self.impressions = impressions
        self.clicks = clicks
        self.ctr = ctr  # 展示量 转点击率
        self.cpc = cpc
        self.spend = spend
        self.sales_revenue = sales_revenue
        self.acos = acos
        self.sales =sales
        self.cr = cr  # 销售转化率










