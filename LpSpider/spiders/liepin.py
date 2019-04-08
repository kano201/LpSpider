import scrapy
import json
from scrapy.http import Request
from LpSpider.items import LpspiderItem


class LP_Spider(scrapy.Spider):

    name = 'LP_Spider'
    # allowed_domains = ['sou.zhaopin.com']

    urls = ['https://fe-api.zhaopin.com/c/i/sou?start=',
            '&pageSize=90&cityId=489&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&=0&_v=0.71372110&x-zp-page-request-id=6fe0fd6fd19145e0bad650dd0900ef1e-1554273063132-870468']

    def start_requests(self):
        for i in range(0, 991, 90):
            url = self.urls[0] + str(i) + self.urls[1]
            yield Request(url, self.parse) # 调用Request获取response，并传给parse，回调函数
        # yield Request(self.first_url, self.parse)

    def parse(self, response):
        info = json.loads(response.text)
        results = info['data']['results']
        for result in results:
            yield self.get_items(result)

    # def get_result(self, response):



    def get_items(self, result):
        item = LpspiderItem()
        item['Company'] = result['company']['name']
        item['Location'] = result['city']['display']
        item['Company_type'] = result['company']['type']['name']
        item['Postname'] = result['jobName']
        item['Salary'] = result['salary']
        item['Education'] = result['eduLevel']['name']
        item['Experience'] = result['workingExp']['name']
        item['pos_id'] = result['SOU_POSITION_ID']
        welfare = ""
        for i in result['welfare']:
            welfare += i + '，'
        print(welfare)
        item['welfare'] = welfare


        # print(item['Company'])
        return item
