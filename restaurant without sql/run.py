from review import Review
from customers import Customer
from restaurant import Restaurant


# customer

customer1 = Customer("Runner", "Rade")
customer2 = Customer("Kingsly", "Jas")
customer3 = Customer("Jaseh", "Onfroy")
customer4 = Customer("Huey", "Freeman")
customer5 = Customer("Peter", "Griffen")


# Restaurant

restaurant1 = Restaurant("Hot Eats")
restaurant2 = Restaurant("Treetops Hotel")
restaurant3 = Restaurant("Views Hotel")
restaurant4 = Restaurant("Cape Hotel")
restaurant5 = Restaurant("Big Man Hotel")


# Review

review1 = Review(customer1, restaurant1, 7)
review2 = Review(customer2, restaurant2, 9)
review3 = Review(customer3, restaurant1, 4)
review4 = Review(customer1, restaurant1, 8)
review5 = Review(customer1, restaurant2, 4)
review6 = Review(customer3, restaurant1, 5)
review7 = Review(customer1, restaurant3, 10)
review8 = Review(customer3, restaurant3, 6)

print("All customers")
print("_"*60)
for customer in Customer.all():
    print(customer.full_name())

print("_"*60)
print("All Restaurant")
print("_"*60)
for restaurant in Restaurant.all():
    print(Restaurant.name)

print("_"*60)
print("\nAll Reviews:")
print("_"*60)

for review in Review.all():
    print(f"Customer: {review.customer.full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.get_rating()}")