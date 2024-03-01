from django.urls import path
from .views import LogListView, LogDetailView, LogCreateView, LogUpdateView, SolutionDetailView, SolutionsCreateView

urlpatterns = [
    path('', LogListView.as_view(), name='home'),
    path('new-question', LogCreateView.as_view(), name='log-create'),
    path('question/<slug:question>', LogDetailView.as_view(), name='log-detail'),
    path('question/update/<slug:question>', LogUpdateView.as_view(), name='log-update'),
    path('add-solution/<slug:question>', SolutionsCreateView.as_view(), name='log-solution-create'),
    path('solution/<slug:solution>', SolutionDetailView.as_view(), name='log-solution'),

]
