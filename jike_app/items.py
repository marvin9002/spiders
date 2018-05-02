# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


# def set_default_value(value):
#     if value is None or '':
#         return 'no_data'


class jikeAppItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class DRecommenDationItem(scrapy.Item):
    """
    主题字段
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    topicId = scrapy.Field()
    subscribersCount = scrapy.Field()
    thumbnailUrl = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = "insert into jike_recommendation(category, re_id, re_topic_id, re_content, re_subscribersCount, re_thumbnailUrl)" \
                     " VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            self["category"], self["id"], self["topicId"], self["content"], self["subscribersCount"],
            self["thumbnailUrl"])
        return insert_sql, params


class DMessagesItem(scrapy.Item):
    """
    主题内容字段
    """
    topic_category = scrapy.Field()
    topic_content = scrapy.Field()
    topic_type = scrapy.Field()
    topic_focus_count = scrapy.Field()
    # id
    id = scrapy.Field(

    )
    # 类型
    type = scrapy.Field()
    # 文字信息
    content = scrapy.Field()
    # 状态
    status = scrapy.Field()
    # 点赞数
    like_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 转发数
    repost_count = scrapy.Field()
    # 时间
    #create_time = scrapy.Field()
    # 是否为视频
    is_video = scrapy.Field()
    # 是否为图文
    is_img = scrapy.Field()