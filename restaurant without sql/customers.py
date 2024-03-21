
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
    
    @property
    def given_name(self):
        return self._given_name
    
    @property
    def family_name(self):
        return self._family_name
    
    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers
    
    def restaurants(self):
        return list(set(review.restaurant for review in self.reviews))
    
    def add_review(self,restaurant,review):
        new_review = review(self,restaurant,review)
        self.reviews.append(new_review)
    
    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None 

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]
    