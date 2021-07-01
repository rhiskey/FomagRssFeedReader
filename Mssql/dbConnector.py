import datetime
import logging
import time
import pyodbc
from settings import db_name, db_pass, db_user, db_server, db_driver
from sys import exit

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = db_server
database = db_name
username = db_user
password = db_pass
driver = db_driver


def insert_row_in_iblockeelement(news_title, news_body, active_date):
    try:
        cnxn = pyodbc.connect(
            'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()

        # Convert current DateTime to string:
        now = datetime.datetime.now()
        update_date = now
        create_date = now
        iblock_id = 29
        active = 'Y'
        active_from_date = active_date
        sort = 500
        prev_text_type = 'H'
        detail_text_type = 'H'
        views_count = 0
        is_sent = 0

        # Sample insert query
        cursor.execute("""
        INSERT INTO dbo.b_IBlockElement ([UpdateDate]
               ,[CreateDate]
               ,[IBlockID]
               ,[Active]
               ,[ActiveFromDate]
               ,[Sort]
               ,[Name]
               ,[PreviewTextType]
               ,[DetailText]
               ,[DetailTextType]
               ,[ViewsCount]
               ,[IsSent]) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                       update_date, create_date, iblock_id, active, active_from_date, sort, news_title, prev_text_type,
                       news_body, detail_text_type, views_count, is_sent)

        # Getting id of latest inserted record
        cursor.execute("SELECT @@IDENTITY AS ID;")
        id = cursor.fetchone()[0]

        cnxn.commit()
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        logging.exception(f'Cant insert new row in ANALYTICS Bitrix Table.\n{sqlstate}')
        exit(3)
    # row_id = insert_row_in_iblockeelementinsection(id)
    except Exception as e:
        logging.exception(f'Cant insert ANALYTICS\n{e}')
        exit(3)

    return id


def check_article_in_iblockeelement(news_title):
    article_id = 0
    try:
        cnxn = pyodbc.connect(
            'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()

        # Getting id of latest inserted record
        cursor.execute("SELECT TOP(1) ID, Name FROM dbo.b_IBlockElement WHERE Name in ((?)) ORDER BY CreateDate DESC;",
                        news_title)
        article_id = cursor.fetchone()[0]
        print(article_id)
        cnxn.commit()

    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        logging.exception(f'Cant find article in ANALYTICS Bitrix Table.\n{sqlstate}')
        article_id = 0
        exit(5)
    # row_id = insert_row_in_iblockeelementinsection(id)
    except Exception as e:
        article_id = 0
        logging.exception(f'Cant find article in ANALYTICS\n{e}')
        return False, article_id
        # exit(5)

    if article_id != 0:
        return True, article_id
    else:
        return False, article_id


def insert_row_in_iblockeelementinsection(elem_id):
    try:
        cnxn = pyodbc.connect(
            'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()

        sec_id = 19
        # Sample insert query
        cursor.execute("""
        INSERT INTO dbo.b_IBlockElementInSection ([SectionId]
               ,[ElementId]) 
        VALUES (?,?)""",
                       sec_id, elem_id)
        # Getting id of latest inserted record
        cursor.execute("SELECT @@IDENTITY AS ID;")
        row_id = cursor.fetchone()[0]
        cnxn.commit()
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        logging.exception(f'Cant insert new row in FINANCIAL ONE Bitrix Table.\n{sqlstate}')
        exit(4)
    # except pyodbc.OperationalError as oe:
    except Exception as e:
        logging.exception(f'Cant insert FINANCIAL ONE\n{e}')
        exit(4)

    return row_id


def insert_news_in_bitrix(title, body, date):
    # Check if already have this article, if not ->
    is_title_exist, article_id = check_article_in_iblockeelement(title)
    if is_title_exist:
        print('---Новость уже существует в базе, пропускаем----')
        logging.debug(
            f'\n!!!!!Новость уже существует в базе, пропускаем ID = {article_id}:"{title}"!!!!!\n')

    else:
        print('*******************')
        print('---Новость будет добавлена в базу---')
        logging.debug(
            f'\n---Новость будет добавлена в базу "{title}"----\n')
        print(f'Дата публикации в битрикс: {date}')
        print('*******************')
        logging.debug(
            f'\n*****ПУБЛИКАЦИЯ*****\nЗаголовк: {title}\nДата '
            f'публикации в битрикс: {date}\n*****ПУБЛИКАЦИЯ*****')
        el_id = insert_row_in_iblockeelement(title, body, date)
        # time.sleep(1)
        row_id = insert_row_in_iblockeelementinsection(el_id)
        return row_id


# if __name__ == '__main__':
#     insert_news_in_bitrix("Расписание вебинаров от AlorSchool на апрель","<table></table>",'2021-04-16 13:55:00+03:00' )
