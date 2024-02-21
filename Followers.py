class Followers:
    def __init__(self):
        self.followers = []

    def add_follower(self, follower):
        self.followers.append(follower)

    def remove_follower(self, follower):
        self.followers.remove(follower)

    def notify_follower(self, notification):
        for follower in self.followers:
            follower.notifications.append(notification)
