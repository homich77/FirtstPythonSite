from django.db import models
from django.db.models import Avg

#from .models import Cookie, Review


class CookieManager(models.Manager):
    rating_from = 4
    rating_top = 10

    def get_query_set(self):
        cookie = super(CookieManager, self).get_query_set()
        return cookie.annotate(avg_mark=Avg('review__mark'))

    def best(self):
        cookie = self.get_query_set()
        return cookie.filter(avg_mark__gte=self.rating_from)\
                     .order_by("-avg_mark")[:self.rating_top]

    def best_for_user(self, user_obj):
        cookie = self.get_query_set()
        return cookie.filter(review__user_id=user_obj,
                             review__mark__gte=self.rating_from)\
                     .order_by("-review__mark")


class ReviewManager(models.Manager):
    latest_count = 10

    def latest_review(self, user_obj):
        return super(ReviewManager, self).get_query_set()\
                                         .filter(user_id=user_obj)\
                                         .order_by("-date")[:self.latest_count]
