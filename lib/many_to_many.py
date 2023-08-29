class Author:
    all=[]

    def __init__(self, name):
        if isinstance(name, str):
            self.name = name 
        else: 
            raise Exception("the name must be of type str class")

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
        # Contract(author: self, book: book, date: date, royalties: royalties) => unable to do mass assignment

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    all=[]
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title 
        else: 
            raise Exception("the title must be of type str class")
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    


class Contract:
    all=[]

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author 
        else: 
            raise Exception("this is not of type Author class")
        if isinstance(book, Book):
            self.book = book 
        else: 
            raise Exception("this is not of type Book class")
        if isinstance(date, str):
            self.date = date 
        else: 
            raise Exception("this is not an string")
        if isinstance(royalties, int):
            self.royalties = royalties 
        else: 
            raise Exception("this is not an integer")
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)
    #This test does not match what the readme states
        # return [contract for contract in cls.all if contract.date == date]
    

    # def check_valid_property(func):
    #     def wrapper(property, target_type):
    #         if isinstance(property, target_type):
    #             func()
    #         else:
    #             raise Exception(f"{property} is not of {target_type} class")
    
    # def set_property(self, property):
    #     self.property = property