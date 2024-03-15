class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (
            isinstance(title, str)
            and 5 <= len(title) <= 50
            and not hasattr(self, "title")
        ):
            self._title = title
        else:
            return None
            

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return None
            
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            return None
            

    
class Author:
    def __init__(self, name):
        self.name = name
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name and not hasattr(self, "name"):
            self._name = name
        else:
            return None
            
    def articles(self):
        return [article for article in Article.all if article.author is self]
        

    def magazines(self):
        return list({article.magazine for article in self.articles()})
        

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        

    def topic_areas(self):
        return (
            list({magazine.category for magazine in self.magazines()})
            if self.magazines()
            else None
        )
        

class Magazine:
    all = [

    ]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            return None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and category:
            self._category = category
        else:
            return None
            

    def articles(self):
        return [article for article in Article.all if article.magazine is self]
        

    def contributors(self):
        return list({article.author for article in self.articles()})

        

    def article_titles(self):
        return (
            [article.title for article in self.articles()] if self.articles() else None
        )

        

    def contributing_authors(self):
    
        non_unique_authors = [article.author for article in self.articles()]
        if unique_contributors := list(
            {
                author
                for author in non_unique_authors
                if non_unique_authors.count(author) > 2
            }
        ):
            return unique_contributors
        else:
            None

    @classmethod
    def top_publisher(cls):
        return (
            max(cls.all, key=lambda magazine: len(magazine.articles()))
            if Article.all
            else None
        )