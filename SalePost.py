class SalePost():
    def __init__(self, user,type, info, price, place, available):
        self.user = user
        self.info = info
        self.type = type
        self.price = price
        self.place = place
        self.available = available

    def __str__(self):
        if self.available:
            status = "For sale"
        else:
            status = "Sold"
        return (self.user.name + " posted a product for sale:\n" +
                status + "! " + self.info + ", price: " + str(self.price) +
                ", pickup from: " + self.place + "\n")

    def sold(self):
        if self.available:
            self.available = False

    def discount(self, percent, password):
        if password == self.user.password:
            self.price *= (1 - percent / 100)