class Article:
    def __init__(self, title, date, body):
        self.title = title
        self.date = date
        self.body = body

    def get_title(self):
        # print("News title is " + self.title)
        return self.title

    def get_date(self):
        return self.date

    def get_body(self):
        return self.body

# a1 = Article(article_title, article_date, article_body)
# a1.get_title()
