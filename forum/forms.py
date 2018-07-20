from django import forms

from .models import Topic,TopicComment

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ["title","content"]

class TopicCommentForm(forms.ModelForm):
	class Meta:
		model = TopicComment
		fields = ["content"]
