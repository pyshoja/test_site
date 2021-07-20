from django import forms
from account.models import User
from first_app.models import Post , support


class profileform (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(profileform, self).__init__(*args,**kwargs)

        self.fields['username'].help_text = None
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['is_author'].disabled = True
            self.fields['special_user'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_author', 'special_user', 'image']



class supportcreateform (forms.ModelForm):

    class Meta:
        model = support
        fields = ['author','title_suppurt','name_user','phone_user','email_user','description_user']

    def clean(self):

        phone_user = self.cleaned_data.get('phone_user')
        email_user = self.cleaned_data.get('email_user')

        if phone_user == None and email_user == None:
            self.add_error('phone_user', ('فیلد اجباری'))
            self.add_error('email_user', ('فیلد اجباری'))
            super().clean()



class postform (forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author',
                  'preview',
                  'parent',
                  'title',
                  'slug',
                  'introduction',
                  'description',
                  'image',
                  'status',
                  'title_post',
                  'audio',
                  'video',
                  'link',
                  ]



    def clean(self):

        author = self.cleaned_data.get('author')
        preview = self.cleaned_data.get('preview')
        parent = self.cleaned_data.get('parent')
        title = self.cleaned_data.get('title')
        slug = self.cleaned_data.get('slug')
        introduction = self.cleaned_data.get('introduction')
        description = self.cleaned_data.get('description')
        image = self.cleaned_data.get('image')
        status = self.cleaned_data.get('status')
        title_post = self.cleaned_data.get('title_post')
        audio = self.cleaned_data.get('audio')
        video = self.cleaned_data.get('video')
        link = self.cleaned_data.get('link')

        if title_post == 1:   #مقاله
            if parent == None or \
               title == None or introduction == None or \
               description == None or image == None:
                self.add_error('parent', ('فیلد اجباری'))
                self.add_error('title', ('فیلد اجباری'))
                self.add_error('introduction', ('فیلد اجباری'))
                self.add_error('description', ('فیلد اجباری'))
                self.add_error('image', ('فیلد اجباری'))
            super().clean()

        if title_post == 2:   #پادکست
            if parent == None or title == None or \
               introduction == None or description == None or \
               image == None or audio == None:
                self.add_error('parent', ('فیلد اجباری'))
                self.add_error('title', ('فیلد اجباری'))
                self.add_error('introduction', ('فیلد اجباری'))
                self.add_error('description', ('فیلد اجباری'))
                self.add_error('image', ('فیلد اجباری'))
                self.add_error('audio', ('فیلد اجباری'))
            super().clean()

        if title_post == 3:   #ویدئو
            if parent == None or \
               title == None or introduction == None or \
               description == None or image == None or \
               video == None and link == None:
                self.add_error('parent', ('فیلد اجباری'))
                self.add_error('title', ('فیلد اجباری'))
                self.add_error('introduction', ('فیلد اجباری'))
                self.add_error('description', ('فیلد اجباری'))
                self.add_error('image', ('فیلد اجباری'))
                self.add_error('video', ('فیلد اجباری'))
                self.add_error('link', ('فیلد اجباری'))
            super().clean()

        else:
            if title_post == None:
                self.add_error('title_post', ('فیلد اجباری'))
            super().clean()