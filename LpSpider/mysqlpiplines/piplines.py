from .sql import sql
from LpSpider.items import LpspiderItem


class LpPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, LpspiderItem):
            pos_id = item['pos_id']
            ret = sql.select_name(pos_id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                postname = item['Postname']
                salary = item['Salary']
                location = item['Location']
                company = item['Company']
                companytype = item['Company_type']
                welfare = item['welfare']
                experience = item['Experience']
                education = item['Education']
                pos_id = item['pos_id']
                sql.insert(postname, salary, location, company, companytype, welfare, experience, education, pos_id)
                print('开始存储')