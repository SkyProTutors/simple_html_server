import operator
class Order:

    all = []

    def __init__(self, number, address, amount, email):
        self.number = number
        self.address = address
        self.amount = amount
        self.email = email

        Order.all.append(self)

    def __repr__(self):
        return f"Order(number={self.number, self.amount, self.email})"

    @classmethod
    def top(cls):
        return sorted(cls.all, key=operator.attrgetter("amount"), reverse=True)

    @classmethod
    def get_all(cls):
        return cls.all


order1 = Order("1", "123 Main St.", 50, "foo@example.com")
order2 = Order("2", "456 Oak Ave.", 75, "bar@example.com")
order3 = Order("3", "789 Elm St.", 100, "baz@example.com")
order4 = Order("4", "321 Maple St.", 25, "qux@example.com")
order5 = Order("5", "654 Pine Ave.", 150, "quux@example.com")
order6 = Order("6", "987 Cedar St.", 200, "corge@example.com")
order7 = Order("7", "246 Birch Ave.", 175, "grault@example.com")
order8 = Order("8", "135 Walnut St.", 80, "garply@example.com")
order9 = Order("9", "864 Spruce Ave.", 125, "waldo@example.com")
order10 = Order("10", "279 Oak St.", 90, "fred@example.com")

print(order1.get_all())