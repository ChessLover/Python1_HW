# Suppose that you want to order some food with a delivery. 
# Use Facade Design Pattern and classes of your choice to simulate a scenario of ordering using an application, 
# you can have a dispatcher, a restaurant, a delivery guy and other actors of your choice. 
# The most important thing is that you should have some method which will organize the priority of the steps that need 
# to be taken when you order the delivery and will "ask" the right parties to do their job. 
# This should happen without intervention of the client.


class Consumer:

    def __init__(self, food):
        self.food = food

    def make_call(self):
        print(f'Ordering {self.food} ...')

    def receive_order(self):
        print(f'Receiving the order of {self.food}.')


class Dispatcher:

    def __init__(self, food):
        self.food = food

    def receive_call(self):
        print(f'Receiving an order of {self.food} ...')


class Restaurant:

    def __init__(self, food):
        self.food = food

    def cook(self):
        print(f'Cooking {self.food} ...')


class Delivery:

    def __init__(self, food):
        self.food = food

    def deliver(self):
        print(f'Delivering the order of {self.food} ...')


class FoodOrdering:

    def __init__(self, food):
        self.consumer = Consumer(food)
        self.dispatcher = Dispatcher(food)
        self.restaurant = Restaurant(food)
        self.delivery = Delivery(food)

    def execute(self):
        self.consumer.make_call()
        self.dispatcher.receive_call()
        self.restaurant.cook()
        self.delivery.deliver()
        self.consumer.receive_order()

ordering = FoodOrdering('pizza')
ordering.execute()