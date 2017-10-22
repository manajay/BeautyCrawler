# coding=utf-8


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加新的链接地址
    def add_new_url(self, new_url):
        if new_url is None:
            return
        if new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)

    # 添加新的链接地址集合
    def add_new_urls(self, urls):
        if urls is None:
            return
        for url in urls:
            self.add_new_url(url)

    # 获取新的链接地址
    def get_new_url(self):
        if self.has_new_url() is True:
            new_url = self.new_urls.pop()
            self.old_urls.add(new_url)
            return new_url

    # 是否有新的链接地址
    def has_new_url(self):
        return len(self.new_urls) != 0
