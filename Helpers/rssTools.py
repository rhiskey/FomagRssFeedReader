import datetime
import logging
from sys import exit

import feedparser
from Classes.article import Article


def get_rss(url):
    try:
        # Use a breakpoint in the code line below to debug your script.
        # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
        NewsFeed = feedparser.parse(url)
        entry = NewsFeed.entries[1]

        # print(entry.keys()) dict_keys(['title', 'title_detail', 'links', 'link', 'published', 'published_parsed',
        # 'summary', 'summary_detail', 'tags', 'yandex_full-text'])
        rss_count = int(len(NewsFeed.entries))
        logging.debug('Number of RSS posts : {}'.format(rss_count))
        print('Number of RSS posts :', rss_count)

        # entry = NewsFeed.entries[1]
        articles = []
        for elem in NewsFeed.entries:
            entry = elem
            article_title = entry.title
            article_date = entry.published_parsed
            article_summary = entry.summary
            article_link = entry.link
            article_body = entry['yandex_full-text']

            # print('Post Title :', article_title)
            # print(article_date)
            # print("******")
            # print(article_summary)
            # print("***Yandex Full Text***")
            # print(article_body)
            a1 = Article(article_title, article_date, article_body)
            articles.append(a1)
        # print("------News Link--------")
        # print(article_link)
        # print(entry.published_parsed)
    except Exception as ex:
        logging.exception(f'Cant parse RSS.\n{ex}')
        exit(2)
    return articles


# # DEBUG
# if __name__ == '__main__':
#     get_rss("https://fomag.ru/news/icbexp/")
