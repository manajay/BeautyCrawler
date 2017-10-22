# -*- coding: utf-8 -*-  
import urlparse
from bs4 import BeautifulSoup
import re
import types


class HtmlParser(object):

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        pattern = re.compile(r'/item/')
        links = soup.find_all("a", href=pattern)
        for link in links:
            """
            注意点:
                ① link 对象是一个 Tag对象,不能直接link['herf']获取链接
                ② 编码问题,链接获取的字符串是unicode编码,需要转换成str格式,否则解析异常
                  详细参考 ruler_01.md
            """
            new_url = link.attrs['href'].encode('utf-8')
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        res_data = dict()
        res_data['url'] = page_url

        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_content):

        if page_url is None or html_content is None:
            return
        
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')

        new_urls = self._get_new_urls(page_url, soup)
        new_datas = self._get_new_data(page_url, soup)

        return new_urls, new_datas
