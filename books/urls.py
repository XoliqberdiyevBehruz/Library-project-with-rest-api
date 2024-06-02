from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ListApiView, DetailApiView, UpdatelApiView, DeleteApiView, CreateApiView, ListCreateApiView, \
    RetrieveDestroyApiView, RetrieveDestroyUpdateApiView, BookViewSet

router = SimpleRouter()
router.register("books", BookViewSet, basename="books")


urlpatterns = [
    # path("books/", ListApiView.as_view()),
    # path("books/<int:id>/", DetailApiView.as_view()),
    # path("books/<int:id>/update/", UpdatelApiView.as_view()),
    # path("books/<int:id>/delete/", DeleteApiView.as_view()),
    # path("books/create/", CreateApiView.as_view()),
    # path("books/lc/", ListCreateApiView.as_view()),
    # path("books/<int:id>/dd/", RetrieveDestroyApiView.as_view()),
    # path("books/<int:id>/dud/", RetrieveDestroyUpdateApiView.as_view()),
]

urlpatterns += router.urls