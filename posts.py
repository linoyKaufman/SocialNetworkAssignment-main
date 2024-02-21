from postFactory import postFactory
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
        self.post = postFactory.create_post(user, type, info, price, place, self.available)

    def like(self, user1):
        if user1 != self.user and user1 not in self.likes:
            self.likes.append(user1)
            self.user.add_notifications(user1.name + " liked your post")
            print("notification to " + self.user.name + ": " + user1.name + " liked your post")

    def unlike(self, user1):
        if user1 in self.likes:
            self.likes.remove(user1)

    def comment(self, user1, comm):
        self.comments.append((user1, comm))
        if user1 != self.user:
            self.user.add_notifications(user1.name + " commented on your post")
            print("notification to " + self.user.name + ": " + user1.name + " commented on your post: " + comm)
    def __str__(self):
        return str(self.post)

    def display(self):
        print("Shows picture")

    def discount(self, percent, password):
        if password == self.user.password:
            self.price *= (1 - percent / 100)
            self.post.price *= (1 - percent / 100)
            print("Discount on " + self.user.name + "'s product! the new price is: " + str(self.price))

    def sold(self, password):
        if password == self.user.password:
            self.available = False
            self.post.available = False
            print(self.user.name + "'s product is sold")
