from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {'title': forms.TextInput(attrs={'class': 'textInputClass'}),
                   'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postconetent'}),

                   }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {'author': forms.TextInput(attrs={'class': 'textinputClass'}),
                   'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea '})}
