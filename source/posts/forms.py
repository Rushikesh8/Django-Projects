from django import forms
from tinymce.widgets import TinyMCE
from posts.models import Post
from posts.models import Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','description','thumbnail','categories','previous_post','next_post']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control',
    'placeholder':'Type your comment','id':'usercomment','rows':'4',
    }))
    class Meta:
        model = Comment 
        fields = ['content']       