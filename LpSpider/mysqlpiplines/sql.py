import pymysql.connections


MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '***********'
MYSQL_PORT = '3306'
MYSQL_DB = 'zhilian'

cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB, charset='utf8mb4')
cur = cnx.cursor()

class sql:
    @classmethod
    def select_name(cls, pos_id):
        sql = "SELECT EXISTS(SELECT 1 FROM em_info WHERE pos_id=%(pos_id)s)"
        value = {
            'pos_id':pos_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert(cls, postname, salary, location, company, companytype, welfare, experience, education, pos_id):
        sql = "INSERT INTO em_info (postname, Salary, Location, Company, Company_type, welfare, Experience, Education, pos_id) VALUES (%(postname)s, %(salary)s, %(location)s, %(company)s, %(companytype)s, %(welfare)s, %(experience)s, %(education)s, %(pos_id)s)"
        value = {
            'postname':postname,
            'salary':salary,
            'location':location,
            'company':company,
            'companytype':companytype,
            'welfare':welfare,
            'experience':experience,
            'education':education,
            'pos_id':pos_id
        }
        cur.execute(sql, value)
        # print(sql, value)
        cnx.commit()
