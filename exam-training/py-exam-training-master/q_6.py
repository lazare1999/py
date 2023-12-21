# ამოცანა 6.
# შექმენით კლასი ნებისმიერი სახელწოდებით და მოიყვანეთ კლასის დონის (Class Level) და
# ობიექტის დონის (Instance level) ცვლადების მაგალითები, აღწერეთ რა სხვაობაა მათ შორის.

class Shark:

    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")

# კლასის დონეზე ცვლადებს კლასის ცვლადებად მოიხსენიებენ, ხოლო ობიექტის დონეზე ცვლადებს ინსტანციის ცვლადებს უწოდებენ.

# ეს დიფერენციაცია საშუალებას გვაძლევს გამოვიყენოთ Class Level ცვლადები ობიექტების ინიციალიზაციისთვის ცვლადებისთვის
# მინიჭებული კონკრეტული მნიშვნელობით და გამოვიყენოთ სხვადასხვა ცვლადები თითოეული ობიექტისთვის Instance level ცვლადებით.