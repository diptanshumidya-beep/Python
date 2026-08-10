class India ():

    def capital(self):
        print("New Delhi is the capital of INDIA")

    def LANGUAGE(self):
            print("HINDI IS THE PIMARY LANGUAGE OF INDIA")
    
    def TYPE(self):
            print("INDIA is a DEVELOPING COUNTRY")
    
    
class USA ():

    def capital(self):
        print("New York is the capital of USA")

    def LANGUAGE(self):
            print("English IS THE PIMARY LANGUAGE OF USA")
    
    def TYPE(self):
            print("USA is a DEVELOPED COUNTRY")


obj_INdia = India()

obj_USA = USA()


for country in (obj_INdia,obj_USA ):

    country.capital()
    country.LANGUAGE()
    country.TYPE()















