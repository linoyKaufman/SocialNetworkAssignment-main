from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class postFactory:
    @staticmethod
    def create_post(user, post_type, info, price=None, place=None, available=None):
        if post_type == "Text":
            return TextPost(user,post_type, info)
        elif post_type == "Image":
            return ImagePost(user,post_type, info)
        elif post_type == "Sale":
            return SalePost(user, post_type, info, price, place, available)