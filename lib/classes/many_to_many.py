
class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title
    @property
    def author(self):
        return self._author 
    @author.setter 
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter 
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
    




class Author:
    def __init__(self, name="Author"):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not hasattr(self, '_name') and isinstance(name, str) and len(name) > 0:
            self._name = name

    def articles(self):
            return [article for article in Article.all if article.author == self and isinstance(article, Article)]
        

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self and isinstance(article.magazine, Magazine)]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set([magazine.magazine.category for magazine in Article.all if magazine.author == self]))









class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    def articles(self):
        return [magazine for magazine in Article.all if magazine.magazine == self and isinstance(magazine, Article)]

    def contributors(self):
        return list(set([magazine.author for magazine in Article.all if magazine.magazine == self]))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [magazine.title for magazine in Article.all if magazine.magazine == self and isinstance(magazine, Article)]


    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1

        contributing_authors = [author for author, x in author_count.items() if x > 2 and isinstance(author, Author)]
        
        if len(contributing_authors) == 0:
            return None
        else:
            return contributing_authors
# ipdb.set_trace()