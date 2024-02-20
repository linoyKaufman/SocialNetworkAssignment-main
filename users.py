from posts import posts


class users:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.status = False
        self.followers = []
        self.post = []
        self.notifications = []

    def set_status(self):
        self.status = not self.status

    def follow(self, user1):
        if self not in user1.followers and self != user1:
            user1.followers.append(self)
            print(self.name + " started following " + user1.name)

    def unfollow(self, user1):
        if self in user1.followers and self != user1:
            user1.followers.remove(self)
            print(self.name + " unfollowed " + user1.name)

    def publish_post(self, type, info, price=None, place=None):
        if type == "Text" or type == "Image" or type == "Sale":
            post1 = posts(self, type, info, price, place)
            print(post1)
            self.post.append(post1)
            for user in self.followers:
                user.add_notifications(self.name + " has a new post")
            return post1

    def print_notifications(self):
        print(self.name + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def add_notifications(self, notif):
        self.notifications.append(notif)

    def __str__(self):
        return "User name: " + self.name + ", Number of posts: " + str(
            len(self.post)) + ", Number of followers: " + str(len(self.followers))
