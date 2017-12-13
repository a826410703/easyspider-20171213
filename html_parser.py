#!C:\Python27
# -*- coding:utf-8 -*-

import re
import urlparse
from bs4 import BeautifulSoup
class HtmlParser(object):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup =  BeautifulSoup(html_cont,'html.parse',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/view/\d+\.html'))
        for link in links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data['url']=page_url
        #                  <a href="../" target="_blank" title="新闻" class="CurrChnlCls">新闻</a>
        title_node =soup.find('a',target="_blank").find('新闻')
        res_data['title']=title_node.get_text()
        summary_node = soup.find()
        res_data['summary']=summary_node.get_test()
        return res_data