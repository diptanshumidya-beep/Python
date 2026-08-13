class Book:

    def __init__(self,name,book_name,book_author):
        self.name = name
        self.book_name = book_name
        self.book_author = book_author
        borrow = False

    def is_borrowed():
        print("THE BOOK HAS BEEN BORROWED")
        print("YOU HAVE TO SUMBIT IN WITHIN 1 MONTH OR A PENALTY WILL BE GIVEN")
        borrow = True

    def is_return():
        print("THE BOOK HAS BEEN RETURNED SUCESSFULLY")
        print("A VERIFICATION WILL BE SENT IN YOUR DEVICE TO VERIFY THAT YOU HAVE RETURNED THE BOOK IN THE LIBRARY")
        borrow = False
    
        
BOOKa = Book("ramu","wings of fire","APJ.ABDULKALAM")

BOOKb = Book("Prabhas Raju","ignited minds","APJ.ABDULKALAM")

BOOKc = Book("SS RAJOUMOULI","VISION 2020","APJ.ABDULKALAM")


print(BOOKa)

print(BOOKb)

print(BOOKc)