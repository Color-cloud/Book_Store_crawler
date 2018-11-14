import logging

from twisted.enterprise import adbapi

from bookstore.settings import MYSQL_SETTINGS, SPIDER_DB_OP_DISPACH


class MYSQLPIPELINE(object):
    def __init__(self, dbpool):
        self.__dbpool = dbpool

    @classmethod
    def from_crawler(cls, *args, **kwargs):
        dbparms = dict(
            host=MYSQL_SETTINGS['HOST'],
            db=MYSQL_SETTINGS['DATABASE'],
            user=MYSQL_SETTINGS['USER'],
            password=MYSQL_SETTINGS['PASSWORD'],
            charset=MYSQL_SETTINGS['CHARSET']

        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        defferd = self.__dbpool.runInteraction(self.db_insert_handle, item)
        defferd.addErrback(self.db_insert_error_handle, item, spider)
        return item

    def db_insert_handle(self, cursor, item):
        key = item.get_name()
        insert_sql = SPIDER_DB_OP_DISPACH['bs'][key][0]
        item_fields = SPIDER_DB_OP_DISPACH['bs'][key][1]
        field_count = len(item_fields)
        item_values = []
        for index in range(field_count):
            item_values.append(item[item_fields[index]])
        print(1111111111111111111111111111111111)
        cursor.execute(insert_sql, item_values)
        print(22222222222222222222222222222222222)
        return True

    def db_insert_error_handle(self, error, item, spider):
        error = f"{spider.name}db_insert_error_handle has error with {error}, {item}"
        logging.error(error)
        print(error)
        return False
