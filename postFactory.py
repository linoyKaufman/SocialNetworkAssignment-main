class PostFactory:
    @staticmethod
    def create_post(user, post_type, info, price=None, place=None):
        if post_type == "Text":
            return TextPost(user, info)
        elif post_type == "Image":
            return ImagePost(user, info)
        elif post_type == "Sale":
            return SalePost(user, info, price, place)