from django import forms

from django.contrib.auth.models import User


from .models import Post, PostReply

# BEGIN Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'text',
        ]
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
# END Post




# BEGIN PostReply
class PostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply
        fields = [
            'text',
        ]
    
    def __init__(self, *args, **kwargs):
        super(PostReplyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'
# END PostReply