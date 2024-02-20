class posts:
    def __init__(self, user, type, info, price, place):
        self.likes = []
        self.comments = []
        self.type = type
        self.info = info
        self.available = True
        self.price = price
        self.place = place
        self.user = user

    def like(self, user1):
        if not any(user1 == self.likes for users in self.likes):
            self.likes.append(user1)
            if self.user.name != user1.name:
                self.user.add_notifications(user1.name + " liked your post")
                print("notification to " + self.user.name + ": " + user1.name + " liked your post")

    def unlike(self, user1):
        if any(user1 == self.likes for users in self.likes):
            self.likes.remove(user1)

    def comment(self, user1, comm):
        self.comments.append((user1, comm))
        if self.user.name != user1.name:
            self.user.add_notifications(user1.name + " commented on your post")
            print("notification to " + self.user.name + ": " + user1.name + " commented on your post: " + comm)

    def discount(self, percent, password):
        if self.type == "Sale" and password == self.user.password:
            self.price = self.price * (1 - 0.01 * percent)
            priceS = str(self.price)
            print("Discount on " + self.user.name + " product! the new price is: " + priceS)

    def sold(self, password):
        if self.type == "Sale" and password == self.user.password:
            self.available = False
            print(self.user.name + "'s product is sold")

    def display(self):
        if self.type == "Image":
            self.available = False
            print("Shows picture")

    def __str__(self):
        if self.type == "Text":
            result = self.user.name + " published a post:\n"+'"'+self.info+'"'
            return result+"\n"
        elif self.type == "Image":
            return self.user.name + " posted a picture\n"
        elif self.type == "Sale":
            result = self.user.name + " posted a product for sale:\n"
            if self.available:
                result += "For sale! " + self.info + ", price: " + str(self.price) + ", pickup from: " + self.place + "\n"
            else:
                result += "Sold! " + self.info + ", price: " + str(
                    self.price) + ", pickup from: " + self.place + "\n"
            return result

