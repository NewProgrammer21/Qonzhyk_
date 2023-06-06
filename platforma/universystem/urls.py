from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'universystem'

urlpatterns =[
	path('login/',auth_views.LoginView.as_view(),name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	path('main/',views.IndexView.as_view(), name='IndexView'),
	path('',views.RedirectView.as_view(), name='RedirectView'),
	path('teacher/',views.TeacherView.as_view(), name='TeacherView'),
	path('teacher/lessonCreate',views.LessonCreateView.as_view(), name='LessonCreateView'),
	path('teacher/addZert',views.LessonZertView.as_view(), name='LessonZertView'),
	path('teacher/addWork',views.LessonWorkView.as_view(), name='LessonWorkView'),
	path('teacher/lessons',views.LessonView.as_view(), name='LessonView'),
	path('teacher/lessons/detail/<int:id>',views.LessonDetailView.as_view(), name='LessonDetailView'),
	path('teacher/inbox',views.InboxView.as_view(), name='InboxView'),
	path('teacher/addinbox',views.AddInboxView.as_view(), name='AddInboxView'),
	path('teacher/inbox/detail/<int:id>',views.DetailInboxView.as_view(), name='DetailInboxView'),
	path('student/',views.StudentProfileIndexView.as_view(), name='StudentProfileIndexView'),
	path('student/lessons',views.LessonsView.as_view(), name='LessonsView'),
	path('student/mylessons',views.MyLessonsView.as_view(), name='MyLessonsView'),
	path('student/lessons/detail/<int:id>',views.LessonsDetailView.as_view(), name='LessonsDetailView'),
	path('student/mylesson/mylessondetail/<int:id>',views.MyLessonsDetailView.as_view(), name='MyLessonsDetailView'),
	path('student/inbox',views.StudentInboxView.as_view(), name='StudentInboxView'),
	path('student/addinbox',views.StudentAddInboxView.as_view(), name='StudentAddInboxView'),
	path('student/inbox/detail/<int:id>',views.StudentDetailInboxView.as_view(), name='StudentDetailInboxView'),
	path('user/registration', views.UserRegistrationView.as_view(), name='user_registration_page'),
	path('test/',views.TestIndexView.as_view(), name='TestIndexView'),
	path('srp/',views.SrpView.as_view(), name='SrpView'),
	path('work/',views.WorkView.as_view(), name='WorkView'),
]