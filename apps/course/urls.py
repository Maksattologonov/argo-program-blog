from django.urls import path
from .views import (CategoriesWithCourses, CourseDetails,
                    CompanyDetails, AllCourses,
                    CategoryCourses, RatingCreate,
                    CommentCreate, CommentUpdate, CommentDelete,
                    FavoritesList, FavoriteAdd, FavoriteDelete)

urlpatterns = [
    path('', CategoriesWithCourses.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryCourses.as_view(),
         name='category_courses'),
    path('courses/', AllCourses.as_view(), name='all_courses'),
    path('course/<str:pk>/', CourseDetails.as_view(), name='course_details'),
    path('about_us/', CompanyDetails.as_view(), name='about_us'),
    path('course/<str:pk>/rating_create/', RatingCreate.as_view(),
         name='rating_create'),
    path('course/<str:pk>/comment_create/', CommentCreate.as_view(),
         name='comment_create'),
    path('course/<str:course_pk>/comment_update/<int:pk>/',
         CommentUpdate.as_view(), name='comment_update'),
    path('course/<str:course_pk>/comment_delete/<int:pk>/',
         CommentDelete.as_view(), name='comment_delete'),
    path('favorites/', FavoritesList.as_view(), name='favorites'),
    path('favorite_add/', FavoriteAdd.as_view(), name='add_favorite'),
    path('favorite_delete/<int:pk>/', FavoriteDelete.as_view(),
         name='delete_favorite'),
    
]
