import logging
from datetime import datetime, timedelta, timezone
from time import mktime
from datetime import date

import pytz
from pytz import timezone
import time
from Helpers.rssTools import get_rss
from Classes.article import Article
from Mssql.dbConnector import insert_news_in_bitrix
from settings import debug, weeks_delay, hours_delay, minutes_delay
from sys import exit


def main():
    # log_level = logging.INFO
    if debug == 'true':
        log_level = logging.DEBUG
    if debug == 'false':
        log_level = logging.ERROR

    logging.basicConfig(filename='rssimport.log', format='%(asctime)s - %(levelname)s:%(message)s', level=log_level)
    logging.debug('Started RSS_Import v. 0.0.8')

    try:
        articles = get_rss("https://fomag.ru/news/icbexp/")
        for elem in articles:
            # Берем только новости, свежие, сегодня
            print(elem.title)
            dat_struct = elem.date
            dt_article = datetime.fromtimestamp(mktime(dat_struct))
            moscow = timezone('Europe/Moscow')
            # loc_dt = moscow.localize(dt_article)
            dt_article = pytz.utc.localize(dt_article, is_dst=None).astimezone(moscow)
            print(dt_article)
            logging.debug(f'Заголовок новости из RSS - {elem.title}\nДата новости - {dt_article}')
            today = datetime.now()
            today = today.replace(tzinfo=None).astimezone(tz=moscow)

            publish_date = dt_article + timedelta(hours=0, minutes=15)  # +15 min
            insert_news_in_bitrix(elem.title, elem.body, publish_date)
            time.sleep(1)
            # if weeks_delay == 0:
            #     # print(f'Задержка по неделям = {weeks_delay}')
            #     h_delay = today - timedelta(hours=hours_delay, minutes=minutes_delay)  # minutes = 0
            #     print(f'Ищем новость начиная с {h_delay}')
            #     if today > dt_article > h_delay:
            #         publish_date = dt_article + timedelta(hours=0, minutes=15)  # +15 min
            #         insert_news_in_bitrix(elem.title, elem.body, publish_date)
            #         time.sleep(1)
            # else:
            #     test_days_delay = today - timedelta(weeks=weeks_delay)  # Only for TEST!
            #     if today > dt_article > test_days_delay:
            #         publish_date = dt_article + timedelta(hours=0, minutes=15)  # +15 min
            #         insert_news_in_bitrix(elem.title, elem.body, publish_date)
            #         time.sleep(1)
    except Exception as ex:
        logging.exception(f'Ошибка: {ex}')
        exit(1)
    # if debug == 'true':
    #     input()
    exit(0)


if __name__ == '__main__':
    main()
