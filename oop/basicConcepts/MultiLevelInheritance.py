class GrandParents:
    
    def PropertyLand(self):
        print("Property Land for farming given by Grand parents ****")

    
class Parents(GrandParents):

    def PropertyHome(self):
        print("Property Home constructed by Parents ***")


class Child(Parents):

    def PropertyVehicle(self):
        print("Property Porsche purchased by Child **")



first_born = Child()
first_born.PropertyLand()
first_born.PropertyHome()
first_born.PropertyVehicle()
