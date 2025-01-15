
# 广告关键词表

# 广告总数据

# 作用 1.用于找到对应的产品基础表， 2. 算总点击
class AdCampaign:

    # 广告活动名称为 key ，广告对象为value
    # 存放自动和手动广告
    manualAd_list: list = []
    automaticAd_list: list = []

    def __init__(self, Ad_portfolio_name):
        self.Ad_portfolio_name = Ad_portfolio_name  # 广告组合名称

    # 添加手动广告词
    def add_ManualAd_keyword(self, m_adKeyword):
        self.manualAd_list.append(m_adKeyword)

    def get_ManualAd_keyword(self):
        return self.manualAd_list

    def add_automaticAd_keyword(self, a_adKeyword):
        self.automaticAd_list.append(a_adKeyword)

    def get_automaticAd_keyword(self):
        return self.automaticAd_list


    def get_ad_sum(self):
        combined_list = self.manualAd_list + self.automaticAd_list

        # 初始化累加器\
        total_impressions = 0
        total_clicks = 0
        ctr_sum = 0
        cpc_sum = 0
        acos_sum = 0
        cr_sum = 0
        ctr_count = 0
        cpc_count = 0
        acos_count = 0
        cr_count = 0
        total_spend = 0
        total_sales_revenue = 0
        total_sales = 0

        # 遍历对象并累加属性值
        for ad in combined_list:
            total_impressions += ad.impressions
            total_clicks += ad.clicks
            total_spend += ad.spend
            total_sales_revenue += ad.sales_revenue
            total_sales += ad.sales

            # 累加需要平均值的指标
            ctr_sum += ad.ctr
            ctr_count += 1
            cpc_sum += ad.cpc
            cpc_count += 1
            acos_sum += ad.acos
            acos_count += 1
            cr_sum += ad.cr
            cr_count += 1

        # 计算平均值
        average_ctr = ctr_sum / ctr_count if ctr_count > 0 else 0
        average_cpc = cpc_sum / cpc_count if cpc_count > 0 else 0
        average_acos = acos_sum / acos_count if acos_count > 0 else 0
        average_cr = cr_sum / cr_count if cr_count > 0 else 0

        total_values = {
            "total_impressions": total_impressions,
            "total_clicks": total_clicks,
            "average_ctr": average_ctr,
            "average_cpc": average_cpc,
            "total_spend": total_spend,
            "total_sales_revenue": total_sales_revenue,
            "average_acos": average_acos,
            "total_sales": total_sales,
            "average_cr": average_cr
        }

        return total_values





# 关键词


class AdKeyword:

    def __init__(self,campaign_name,Ad_Group_Name,match_type, keyword,impressions, clicks, ctr, cpc, spend, sales_revenue, acos, sales,cr):
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










