class Address:
    def __init__(self, postcode, city, street, building, apartment):
        self.postcode = postcode
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return f"{self.postcode}, {self.city}, {self.street}, {self.building}-{self.apartment}"