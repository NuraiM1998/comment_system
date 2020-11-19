'''Форма комментариев'''
from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    '''Форма коментария'''
    
    
    def __init__(self, user, post_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.post_id = post_id
    

    def save(self, commit=True):
        comment = super().save(commit=False)
        print('COMMENT >>>>>>',comment)
        print('COMMENT DIR >>>>>>',dir(comment))
        comment.user = self.user
        comment.post_id = self.post_id
        
        if commit:
            comment.save()
        
        return comment


    class Meta:
        '''Объявление полей'''
        model = Comment
        fields = [
            'content'
        ]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
