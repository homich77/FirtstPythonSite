import random
from django.core.urlresolvers import reverse
from django.utils.http import urlsafe_base64_decode

from apps.cookies.models import Cookie, Review
from apps.main.tests import MainTest, create_user
from apps.cookies.views import vote


def create_cookie(name='test_cookie', description='description test cookie'):
    return Cookie.objects.create(name=name,
                                 description=description)


def create_cookies(count=3):
    return [create_cookie(name='cookie%s' % i) for i in range(count)]


def create_review(user, cookie, text='', mark=5):
    return Review.objects.create(user_id=user,
                                 cookie_id=cookie,
                                 text=text, mark=mark)


def create_reviews(cookie, count=10, mark_from=0, mark_to=5):
    for i in range(count):
        user = create_user(username='test_user_%s' % i)
        create_review(user, cookie,
                      text='text%s' % i,
                      mark=random.randint(mark_from, mark_to))


def review_save(review, mark=5):
    review.mark = mark
    review.save()


class CookieTest(MainTest):
    def test_cookie_manager_best(self):
        cookie1, cookie2, cookie3 = create_cookies()

        create_reviews(cookie1, count=2, mark_from=4)
        create_review(self.user, cookie2, mark=4)
        create_review(self.user, cookie3, mark=3)

        response = self.client.get(reverse('main:main_view'))
        self.assertQuerysetEqual(
            response.context['best_cookie_list'],
            ['<Cookie: %s>' % cookie1.name, '<Cookie: %s>' % cookie2.name]
        )

    def test_cookie_manager_best_for_user(self):
        for cookie in create_cookies(5):
            create_review(self.user, cookie)

        review_temp = Review.objects.get(pk=3)
        review_save(review_temp, 3)

        response = self.client.get(reverse('login:profile',
                                           args=(self.user.username, )))
        context = response.context['best_cookies']
        self.assertNotIn(review_temp.cookie_id, context)
        self.assertEqual(len(context), 4)

        review_save(review_temp, Cookie.objects.rating_top)
        response = self.client.get(reverse('login:profile',
                                           args=(self.user.username, )))
        self.assertIn(review_temp.cookie_id,
                      response.context['best_cookies'])

    def test_search(self):
        create_cookies(5)
        response = self.client.post('/cookies/', {'search_cookie': 'kie1'})
        self.assertIsNotNone(response.context['cookies_list'])
        response = self.client.post('/cookies/', {'search_cookie': 'muf'})
        self.assertFalse(response.context['cookies_list'])

    def test_detail(self):
        cookie = create_cookie('muf', 'description muf')
        response = self.client.get(reverse('cookies:detail',
                                           args=(cookie.id, )))
        self.assertContains(response, cookie.description)

    def test_vote_invalid(self):
        cookie = create_cookie()
        url_vote = reverse('cookies:vote', args=(cookie.id, ))
        self.client.login(username=self.user.username, password='qwe')
        context = {'mark': 10, 'text': 'Hello from Test )'}

        response = self.client.post(url_vote, context)
        self.assertContains(response, 'Select a valid choice. 10 is ',
                            status_code=200)

    '''def test_vote_valid(self):
        cookie = create_cookie()
        url_vote = reverse('cookies:vote', args=(cookie.id, ))
        url_detail = reverse('cookies:detail', args=(cookie.id, ))
        self.client.login(username=self.user.username, password='qwe')

        context = {'mark': 5, 'text': 'Hello with valid data )'}
        response = self.client.post(url_vote, context, follow=True)
        self.assertNotContains(response, 'Add review')'''

    def test_vote_anonymous(self):
        cookie = create_cookie()
        url_vote = reverse('cookies:vote', args=(cookie.id, ))
        url_detail = reverse('cookies:detail', args=(cookie.id, ))
        context = {'mark': 5, 'text': 'Hello from anonymous)'}
        response = self.client.get(url_detail)
        self.assertNotContains(response, 'Add review')

        response = self.client.post(url_vote, context)
        self.assertNotContains(response, 'Add review')


class ReviewTest(MainTest):
    def test_create_review(self):
        # Insert review to database
        cookie = create_cookie()
        review = create_review(self.user, cookie, 'test review', 5)
        review_from_database = Review.objects.get(pk=review.id)
        self.assertTrue(review_from_database,
                        '--- Review was not created correctly')

    def test_latest_review(self):
        for cookie in create_cookies(15):
            create_review(self.user, cookie, 'text_%s' % cookie.id)

        count = Review.objects.latest_count
        review_list = Review.objects.order_by('date')[:count]
        response = self.client.get(reverse('login:profile',
                                           args=(self.user.username, )))
        # TODO:
        self.assertItemsEqual(response.context['latest_reviews'],
                              review_list)

    # Allow only one review from user about cookie
    # IntegrityError: columns user_id_id, cookie_id_id are not unique
'''
    def test_create_more_one_review(self):
        cookie = create_cookie()
        review1 = create_review(self.user, cookie, 'test review 1', 5)
        self.assertFalse(create_review(self.user, cookie, 'test review 2', 5))
    '''
