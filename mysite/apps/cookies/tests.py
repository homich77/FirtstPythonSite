from django.test import TestCase

from apps.cookies.models import Cookie, Review
'''
from apps.main.tests import MainTest



def create_cookie(name='test_cookie', description='description test cookie'):
    return Cookie.objects.create(name=name,
                                 description=description)


def create_review(user, cookie, text='', mark=5):
    return Review.objects.create(user_id=user,
                                 cookie_id=cookie,
                                 text=text, mark=mark)


class ReviewTest(MainTest):
    def test_create_review(self):
        cookie = create_cookie()
        review = create_review(self.user, cookie, 'test review', 5)
        review_from_database = Review.objects.get(pk=review.id)
        self.assertEqual(review_from_database.text,
                            review.text,
                            '--- Review was not created correctly')
'''
'''    # Allow only one review from user about cookie
    def test_create_more_one_review(self):
        cookie = create_cookie()
        review1 = create_review(self.user, cookie, 'test review 1', 5)
        try:
            review2 = create_review(self.user, cookie, 'test review 2', 5)
            self.assertFalse(review2.id)
        except:
            self.assertFalse()
'''