

from datetime import datetime

# 产品业务表信息类
# 每一个子Sku为一个类

"""
parentasin 父Aisn
chilasin 子asin
title 标题   (只需要前面一段
session 会话 （去重点点击量
pageviews 浏览量（没有去重的点击量
orders 总订单量
tacos :广告花费/全店销售
adsales :广告销售/全店销售
"""
from dataclasses import dataclass


@dataclass
class Product:
    # 产品基础信息
    datetime: datetime
    parentasin: str = None
    childasin: str = None
    title: str = None

    # 订单自然数据
    n_pageviews: int = None
    n_salesVolume: int = None
    n_sales: float = None
    n_averagePrice: float = None
    n_conversionRate: float = None

    # 订单广告数据
    a_pageviews: int = None
    a_ppc: float = None
    a_spend: float = None  #广告花费
    a_salesVolume: int = None
    a_sales: float = None
    a_acos: float = None
    a_conversionRate: float = None

    # 订单整体数据
    t_pageviews: int = None
    t_orders: int = None
    t_salesVolume: int = None
    t_tacos: float = None
    t_adSales: float = None
    t_conversionRate: float = None
    t_ranking: int = None
    t_rating: float = None
    t_session: int = None
    t_cartPercentage: float = None
    t_sales: float = None

    # Getter and Setter for each field
    def get_datetime(self):
        return self.datetime

    def set_datetime(self, value: datetime):
        self.datetime = value

    def get_parentasin(self):
        return self.parentasin

    def set_parentasin(self, value: str):
        self.parentasin = value

    def get_childasin(self):
        return self.childasin

    def set_childasin(self, value: str):
        self.childasin = value

    def get_title(self):
        return self.title

    def set_title(self, value: str):
        self.title = value

    def get_n_pageviews(self):
        return self.n_pageviews

    def set_n_pageviews(self, value: int):
        self.n_pageviews = value

    def get_n_salesVolume(self):
        return self.n_salesVolume

    def set_n_salesVolume(self, value: int):
        self.n_salesVolume = value

    def get_n_sales(self):
        return self.n_sales

    def set_n_sales(self, value: float):
        self.n_sales = value

    def get_n_averagePrice(self):
        return self.n_averagePrice

    def set_n_averagePrice(self, value: float):
        self.n_averagePrice = value

    def get_n_conversionRate(self):
        return self.n_conversionRate

    def set_n_conversionRate(self, value: float):
        self.n_conversionRate = value

    def get_a_pageviews(self):
        return self.a_pageviews

    def set_a_pageviews(self, value: int):
        self.a_pageviews = value

    def get_a_ppc(self):
        return self.a_ppc

    def set_a_ppc(self, value: float):
        self.a_ppc = value

    def get_a_spend(self):
        return self.a_spend

    def set_a_spend(self, value: float):
        self.a_spend = value

    def get_a_salesVolume(self):
        return self.a_salesVolume

    def set_a_salesVolume(self, value: int):
        self.a_salesVolume = value

    def get_a_sales(self):
        return self.a_sales

    def set_a_sales(self, value: float):
        self.a_sales = value

    def get_a_acos(self):
        return self.a_acos

    def set_a_acos(self, value: float):
        self.a_acos = value

    def get_a_conversionRate(self):
        return self.a_conversionRate

    def set_a_conversionRate(self, value: float):
        self.a_conversionRate = value

    def get_t_pageviews(self):
        return self.t_pageviews

    def set_t_pageviews(self, value: int):
        self.t_pageviews = value

    def get_t_orders(self):
        return self.t_orders

    def set_t_orders(self, value: int):
        self.t_orders = value

    def get_t_salesVolume(self):
        return self.t_salesVolume

    def set_t_salesVolume(self, value: int):
        self.t_salesVolume = value

    def get_t_tacos(self):
        return self.t_tacos

    def set_t_tacos(self, value: float):
        self.t_tacos = value

    def get_t_adSales(self):
        return self.t_adSales

    def set_t_adSales(self, value: float):
        self.t_adSales = value

    def get_t_conversionRate(self):
        return self.t_conversionRate

    def set_t_conversionRate(self, value: float):
        self.t_conversionRate = value

    def get_t_ranking(self):
        return self.t_ranking

    def set_t_ranking(self, value: int):
        self.t_ranking = value

    def get_t_rating(self):
        return self.t_rating

    def set_t_rating(self, value: float):
        self.t_rating = value

    def get_t_session(self):
        return self.t_session

    def set_t_session(self, value: int):
        self.t_session = value

    def get_t_cart_percentage(self):
        return self.t_cartPercentage

    def set_t_cart_percentage(self, value: float):
        self.t_cartPercentage = value

    def get_t_sales(self):
        return self.t_sales

    def set_t_sales(self, value: float):
        self.t_sales = value
