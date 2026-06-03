from django.urls import path
from . import views
from rest_framework.authtoken import views as authviews

urlpatterns = [
    path('api/get-users-list/', views.GetUsersList.as_view(), name='get_users_list'),
    path('api/get-user-details/<int:pk>', views.GetUserDetails.as_view(), name='get_user_details'),
    path('api/search-user/<str:username>', views.SearchUser.as_view(), name='seach_user'),
    path('api/update-user/<int:pk>', views.UpdateUser.as_view(), name='update_user'),
    path('api/delete-user/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),
    path('api/login/', authviews.obtain_auth_token, name="login_user"),
    path('api/logout/', views.LogoutUser.as_view(), name='logout_user'),
    path('api/register/', views.RegisterUser.as_view(), name='register_user'),
    path('api/check-auth-token/', views.CheckAuthToken.as_view(), name="check_auth_token"),
    path('api/get-tasks-list/', views.GetTasksList.as_view(), name='get_tasks_list'),
    path('api/get-task-details/<int:pk>', views.GetTaskDetails.as_view(), name="get_task_details"),
    path('api/search-task/<str:username>', views.SearchTask.as_view(), name='search_task'),
    path('api/add-task/', views.AddTask.as_view(), name='add_task'),
    path('api/update-task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
    path('api/delete-task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
  
]