
# 广告关键词表

# 广告总数据

class AdCampaign:
    def __init__(self, campaign_name, impressions, clicks, spend, acos, ctr):
        self.campaign_name = campaign_name  # 广告组合名称
        self.impressions = impressions  # 展示量
        self.clicks = clicks  # 点击量
        self.spend = spend  # 花费
        self.acos = acos  # 广告成本销售比(ACOS)
        self.ctr = ctr  # 点击率(CTR)

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

# 关键词

class Keyword:
    def __init__(self, keyword, match_type):
        self.keyword = keyword  # 客户搜索词
        self.match_type = match_type  # 匹配类型（例如："紧密"、"广泛"、"词组"）

    def get_keyword(self):
        return self.keyword

    def set_keyword(self, keyword):
        self.keyword = keyword

    def get_match_type(self):
        return self.match_type

    def set_match_type(self, match_type):
        self.match_type = match_type

# 手动广告

class ManualAd(AdCampaign):
    def __init__(self, campaign_name, impressions, clicks, spend, acos, ctr):
        super().__init__(campaign_name, impressions, clicks, spend, acos, ctr)
        self.keywords = []  # 关键词列表

    def add_keyword(self, keyword: Keyword):
        self.keywords.append(keyword)

    def get_keywords(self):
        return self.keywords

#自动广告

class AutomaticAd(AdCampaign):
    def __init__(self, campaign_name, impressions, clicks, spend, acos, ctr, targeting_type):
        super().__init__(campaign_name, impressions, clicks, spend, acos, ctr)
        self.targeting_type = targeting_type  # 自动广告的匹配方式（如：自动匹配）

    def get_targeting_type(self):
        return self.targeting_type

    def set_targeting_type(self, targeting_type):
        self.targeting_type = targeting_type




