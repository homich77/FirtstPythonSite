from django.forms import ModelForm, Textarea

from apps.cookies.models import Review


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['mark', 'text']
        widgets = {
            'text': Textarea(attrs={'rows': 4, 'cols': 70})
        }

    def save(self, user, cookie):
        obj = super(ReviewForm, self).save(commit=False)
        obj.user_id = user
        obj.cookie_id = cookie
        return obj.save()
