import datetime
import logging
from sys import exit

import feedparser
from Classes.article import Article


def get_rss(url):
    try:
        NewsFeed = feedparser.parse(url)
        entry = NewsFeed.entries[1]

        rss_count = int(len(NewsFeed.entries))
        logging.debug('Number of RSS posts : {}'.format(rss_count))
        print('Number of RSS posts :', rss_count)

        articles = []
        for elem in NewsFeed.entries:
            entry = elem
            article_title = entry.title
            article_date = entry.published_parsed
            article_summary = entry.summary
            article_link = entry.link
            article_body = entry['yandex_full-text']

            a1 = Article(article_title, article_date, article_body)
            articles.append(a1)

    except Exception as ex:
        logging.exception(f'Cant parse RSS.\n{ex}')
        exit(2)
    return articles


# # DEBUG
# if __name__ == '__main__':
#     get_rss("https://fomag.ru/news/icbexp/")
