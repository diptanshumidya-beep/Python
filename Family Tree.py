class Family_Member:
    def __init__(self,eye_colour,hieght_cm):
        self.eye_colour = eye_colour
        self.hieght_cm = hieght_cm




    def show_traits (self):
        print("Eye Colour",self.eye_colour)
        print("Hieght (cm)",self.hieght_cm)




class Kid(Family_Member):

    def __init__(self,name,age,eye_colour,hieght_cm):
        self.name = name
        self.age = age
        super().__init__(eye_colour,hieght_cm)

    def show_traits (self):
        print("Name",self.name)
        print("Age",self.age)
        super().show_traits()


    def fav_hobby(self,hobby):
        print(self.name,"loves",hobby)




child = Kid("Ms Dhoni",43,"blue",200)


child.show_traits()
child.fav_hobby("Farming")


print ("Is kid a subclass of Family Member?",issubclass(Kid,Family_Member))









