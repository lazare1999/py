class University:

    def __str__(self):
        return f"{self.name}, address {self.address}"

    def __init__(self, address, name):
        self.address = address
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


class GeorgianUniversity(University):

    def __str__(self):
        return f"{self.name}, address {self.address} have {self.__student_count} students"

    def __init__(self, student_count, name, address):
        super().__init__(address, name)
        self.__student_count = student_count

    def to_str(self):
        return super().__str__()

    def set_student_count(self, student_count):
        self.__student_count = student_count

    def get_student_count(self):
        return self.__student_count


gu = GeorgianUniversity(100, 'gu', "tbilisi")
print(gu)
