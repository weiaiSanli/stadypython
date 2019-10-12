# -*- encoding: utf-8 -*-
"""
@File    : Handler.py
@Time    : 2019-9-30 14:30
@Author  : shiq
@Email   : shiqiang_xd0529@163.com
@Software: PyCharm
"""
from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://reeoo.com/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div[class^="thumb"]').items():
            detail_url = each('a').attr.href
            print(detail_url)
            self.crawl(detail_url, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):

        header = response.doc('body > article > section > article > header')
        title = header('h1').text()
        print('当前title', title)
        tags = []

        for each in header.items('a'):
            tags.append(each.text())

        content = response.doc('div[id = "post_content"]')
        desc = content('blockquote > p').text()

        website_url = content('a').attr.href

        image_url_list = []

        for each in content.items('img[data-src]'):
            image_url_list.append(each.attr('data-src'))

        return {
            "title": title,
            "tags": tags,
            "description": desc,
            "image_url_list": image_url_list,
            "website_url": website_url,
        }

    def on_result(self, result):
        if not result:
            return

        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = client['pyspyspider_projectdb']
        coll = db['website']

        data = {
            'title': result['title'],
            'tags': result['tags'],
            'description': result['description'],
            'website_url': result['website_url'],
            'image_url_list': result['image_url_list']
        }

        data_id = coll.insert(data)
        print(data)
