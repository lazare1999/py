# ამოცანა 7.
# შექმენით კლასი Country, რომელსაც გააჩნია ორი წევრი ცვლადი CountryName და Countrypopulation. Country კლასს დაამატეთ კლასის
# კონსტრუქტორი. შექმენით Country კლასის შვილობილი კლასი City, რომელსაც განუსაზღვრეთ წევრი ცვლადი CityName. City კლასს დაამატეთ
# კლასის კონსტრუქტორი რომელსაც გადაეცემა სამი პარამეტრი CountryName , Countrypopulation და CityName და გამოიძახებს Country კლასის
# კონსტრუქტორს (Parent Class Constructor)

class Country:

    def __init__(self, country_name, country_population):
        self.country_name = country_name
        self.country_population = country_population


class City(Country):

    def __init__(self, country_name, country_population, city_name):
        Country.__init__(self, country_name, country_population)
        self.city_name = city_name

    def __str__(self):
        return self.country_name + " " + str(self.country_population) + " " + self.city_name


city = City("geo", 22, "tbilisi")
print(city)
