class Car(object):

    condition = "new"

    def __init__(self, model, color, mpg):

        self.model = model

        self.color = color

        self.mpg   = mpg



    def display_car(self):

        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)



my_car = Car("Toyota","silver", 88)

print my_car.display_car()