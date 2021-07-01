**Импорт на СПБ сайт** нужно делать с задержкой в 15 мин от времени, которое указано у каждой новости в RSS.
Берем:
* Заголовок новости из тега - <title>
* Дату и время ставим на момент импорта
* Текст новости из тега - <yandex:full-text> с преобразованием в HTML

- [X] Если параметр  WEEKS_DELAY = 0 => новости публикуются за HOURS_DELAY, елси WEEKS_DELAY!=0, то за указанный период 
  в неделях
  
1. Install `pip install auto-py-to-exe`
2. Build `auto-py-to-exe` 
3. Navigate to `output` folder -> run `main.exe`
4. Create `.env` file with config
5. `pip freeze > requirements.txt`

Структура .env файла: 
```
# Уровень вывода ошибок в логи
DEBUG=true
# MsSQL DB Connection
DB_SERVER=tcp:localhost	
DB_NAME=
DB_USER=
DB_PASS=
# Период за который новости читаются
WEEKS_DELAY=30
HOURS_DELAY=1
```
Exit Code:
0 - Завершена работа (0xFFFFFFFF)= -1
1 - Ошибка в main.py
2 - Невозможно спарсить RSS rssTools.py
3 - Ошибка вставки новости в таблицу АНАЛИТИКИ dbConnector.py [b_IBlockElement]
4 - Ошибка вставки в таблицу Financial One [b_IBlockElementInSection] 
5 - Ошибка поиска новости в таблице АНАЛИТИКИ dbConnector.py [b_IBlockElement]