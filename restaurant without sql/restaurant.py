class Restaurant:
    
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self.reviews = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("Restaurant name cannot be changed.")

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def add_review(self,review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews
    
    def get_customers(self):
        return list(set(review.customer for review in self.reviews))
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating/ len(self.reviews)