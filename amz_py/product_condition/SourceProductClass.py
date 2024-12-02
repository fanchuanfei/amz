

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

    def __init__(self,datetime=None,parentasin=None,childasin=None,title=None,
                n_pageviews=None,n_orders,n_sales,n_averagePrice,n_conversionRate,
                a_pageviews,a_ppc,a_spend,a_orders,a_sales,a_acos,a_conversionRate,
                t_pageviews,t_session,cart_percentage,t_sales,t_conversionRate,t_orders):






