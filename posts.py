from postFactory import postFactory
from matplotlib import pyplot as plt, image as mpimg


class posts:
    def __init__(self, user, type, info, price, place):
        self.likes = []
        self.comments = []
        self.post = postFactory.create_post(user, type, info, price, place, True)

    def like(self, user1):
        if user1 != self.post.user and user1 not in self.likes:
            self.likes.append(user1)
            self.post.user.add_notifications(user1.name + " liked your post")
            print("notification to " + self.post.user.name + ": " + user1.name + " liked your post")

    def unlike(self, user1):
        if user1 in self.likes:
            self.likes.remove(user1)

    def comment(self, user1, comm):
        self.comments.append((user1, comm))
        if user1 != self.post.user:
            self.post.user.add_notifications(user1.name + " commented on your post")
            print("notification to " + self.post.user.name + ": " + user1.name + " commented on your post: " + comm)

    def __str__(self):
        return str(self.post)

    def display(self):
        if self.post.type == "Image":
            print("Shows picture")
            try:
                with open(self.post.info, 'rb') as img_file:
                    img_data = img_file.read()
            except FileNotFoundError:
                return None
            plt.imshow(img_data)
            plt.axis('off')
            plt.show()

    def discount(self, percent, password):
        if password == self.post.user.password:
            self.post.price *= (1 - percent / 100)
            print("Discount on " + self.post.user.name + "'s product! the new price is: " + str(self.post.price))

    def sold(self, password):
        if password == self.post.user.password:
            self.post.available = False
            print(self.post.user.name + "'s product is sold")
