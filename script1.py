class Books:
    def __init__(self,title,author,is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def __str__(self):
        return f"{self.title}:{self.author}"
    def __repr__(self):
        return f"{self.title}:{self.author}""
class Library:
    l={}
    def __add__(self,o2):
        if len(o2.title)>7:
            Library[o2.title]=o2
            return Library.l
        else:
            return "length of title is short"
