from django import forms
from .models import Log, Comments, Solutions


# class QuestionForm(forms.ModelForm):

#     title = forms.CharField(label='What is your error?', max_length=500)
#     content = forms.CharField(
#         label='Please explain in detail: ', required=True, widget=forms.Textarea)
#     image = forms.ImageField(required=False)

#     class Meta:
#         model = Log
#         fields = ['title', 'content', 'image']
#     def form_valid(self, form):

#         form.instance.author = self.request.user
#         return super().form_valid(form)



class QuestionEditForm(forms.ModelForm):

    title = forms.CharField(label='What is your error?', max_length=500)
    content = forms.CharField(
        label='Please explain in detail: ', required=True, widget=forms.Textarea)
    image = forms.ImageField(required=False)

    class Meta:
        model = Log
        fields = ['title', 'content', 'image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





class CommentForm(forms.ModelForm):

    comment = forms.CharField(label=False)

    class Meta:
        model = Comments

        fields = ['comment', ]


class SolutionForm(forms.ModelForm):

    solution = forms.CharField(
        label='Please explain in detail: ', required=True, widget=forms.Textarea)
    image = forms.ImageField(required=False)

    class Meta:
        model = Solutions
        fields = ['solution', 'image']
