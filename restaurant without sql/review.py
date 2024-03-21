from customers import Customer
from restaurant import Restaurant

class Review:
    all_reviews = [] 

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self) 

    def get_rating(self):
        return self._rating 
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews
    