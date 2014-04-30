from django.forms import ModelForm

from apps.cookies.models import Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['mark', 'text']

    def save(self, user, cookie):
        obj = super(ReviewForm, self).save(commit=False)
        obj.user_id = user
        obj.cookie_id = cookie
        return obj.save()
