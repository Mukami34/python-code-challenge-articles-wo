class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def articles(self):
        return self._articles

    @classmethod
    def all(cls):
        return cls._all_magazines

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all_magazines if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        titles = [article.title() for magazine in cls._all_magazines for article in magazine.articles()]
        return titles

    def contributors(self):
        authors = [article.author() for article in self._articles]
        contributor_counts = {}
        for author in authors:
            contributor_counts[author] = contributor_counts.get(author, 0) + 1
        return [author for author, count in contributor_counts.items() if count > 2]