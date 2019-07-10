from django.urls import path

from poll.views import index_view,details_view,vote_view,results_view

app_name='poll'

urlpatterns = [
	path('<int:qid>/results',results_view,name='results'),
	path('<int:qid>/vote/',vote_view,name='vote'),
	path('<int:qid>',details_view,name='details'),
	path('',index_view,name='index'),
]