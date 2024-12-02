

#产品业务表信息类
#每一个子Sku为一个类

"""
parentasin 父Aisn
chilasin 子asin
title 标题   (只需要前面一段
session 会话 （去重点点击量
pageviews 浏览量（没有去重的点击量
orders 总订单量
"""
class Product:

#为所有形参加上默认属性None

    def __init__(self,datetime=None, parentasin=None, childasin=None, title=None,
                 n_pageviews=None, n_orders=None, n_sales=None, n_averagePrice=None, n_conversionRate=None,
                 a_pageviews=None, a_ppc=None, a_spend=None, a_orders=None,a_sales=None, a_acos=None, a_conversionRate=None,
                 t_pageviews=None, t_session=None, cart_percentage=None, t_sales=None, t_conversionRate=None, t_orders=None):

        self.datetime = datetime
        self.parentasin = parentasin
        self.childasin = childasin








