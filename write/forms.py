from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'name', 'bodyText', 'productType', 'productNum', 'email', 'address', 'picture']
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'input-box', 'name':'title', 'placeholder':'Title'}), 
            'name': forms.TextInput(attrs={'class':'input-box', 'name':'name', 'placeholder':'user name'}), 
            'bodyText': forms.Textarea(attrs={'class':'desc', 'name':'bodyText'}),
            'productType': forms.TextInput(attrs={'class':'input-box', 'name':'productType', 'placeholder':'Type of product'}), 
            'productNum': forms.NumberInput(attrs={'class':'input-box', 'name':'productNum', 'placeholder':'num'}),  
            'email': forms.TextInput(attrs={'class':'input-box', 'name':'email', 'placeholder':'email'}), 
            'address': forms.TextInput(attrs={'class':'input-box', 'name':'address', 'placeholder':'destination'}), 
            'picture': forms.FileInput(attrs={'class':'input-img', 'name':'picture'}),
        }
        labels = {
            'title': '제목',
            'name': '이름',
            'bodyText': '신청 내용',
            'productType': '희망 물품',
            'productNum': '희망 수량',
            'email': '이메일',
            'address': '희망 수령 장소',
            'picture': '관련 이미지',
        }
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostForm, self).__init__(*args, **kwargs)


        