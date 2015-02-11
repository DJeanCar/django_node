from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import User
from .models import Question, LikeQuestion

class IndexView(ListView):

	template_name = 'index.html'
	model = Question

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		likes = []
		for question in context['object_list']:
			likes.append(LikeQuestion.objects.filter(question = question, like=True).count())
		context['questions'] = zip (context['object_list'], likes)
		return context

class LikeView(TemplateView):

	def get(self, request, *args, **kwargs):
		question = Question.objects.get(pk = request.GET['id'])
		question = LikeQuestion.objects.get_or_create(user = request.user, 
							question = question, 
							like = True)
		if not question[1]:
			question[0].like=False
			question[0].save()
		return redirect('/')

@csrf_exempt
def dandolike(request):
	question = Question.objects.get(pk = request.POST['id_pregunta'])
	user = User.objects.get(username = request.POST['user'])
	question = LikeQuestion.objects.get_or_create(user = user, 
						question = question, 
						like = True)
	if not question[1]:
		question[0].like=False
		question[0].save()

	count_likes = LikeQuestion.objects.filter(
		question__id = request.POST['id_pregunta'], 
		like=True).count()

	response = JsonResponse({
			'id_pregunta' : request.POST['id_pregunta'],
			'cantidad_likes' : count_likes
		})
	return HttpResponse(response.content)