# coding=utf-8
import url_manager
import html_downloader
import html_parser
import html_outputer
import logging


class CrawlerMain(object):
    def crawl(self, root_url):
        # 限制抓取的链接数
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            # noinspection PyBroadException
            try:
                new_url = self.urls.get_new_url()
                print("抓取到的链接: ", count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_datas = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_datas)
                if count == 200:
                    break
                count += 1
            except Exception as e:
                logging.exception(e)
            # 爬取结束
            self.outputer.output_html()

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/清水理纱'
    obj = CrawlerMain()
    obj.crawl(url)
