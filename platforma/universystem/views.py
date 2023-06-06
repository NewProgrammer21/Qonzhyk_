from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin,View
from .forms import UserRegistrationForm, ProfileForm, Lesson_form, MessageForm, CommentsForm,LessonZert_form, LessonWork_form
from .models import Profile, Lesson, EnrollCource, Message,SRP, Comment,laboratorywork,News

class UserRegistrationView(TemplateResponseMixin, View):
    template_name = 'registration/registration.html'

    def get(self,request):
        registration_form = UserRegistrationForm()
        profile_form = ProfileForm()
        return self.render_to_response({'registration_form': registration_form, 'profile_form': profile_form})

    def post(self, request):
        registration_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, files=request.FILES)
        if registration_form.is_valid() and profile_form.is_valid():
            new_user = registration_form.save(commit=False)
        # Set the chosen password
            new_user.set_password(
            registration_form.cleaned_data['password'])
        # Save the User object
            new_user.save()
            profile = profile_form.save(commit = False)
            profile.user = new_user
            profile.save()
            return redirect('universystem:login')
        return self.render_to_response({'registration_form': registration_form, 'profile_form': profile_form})

class RedirectView(View):
    
    def get(self,request):
        if Profile.objects.filter(user= request.user,roles=2).exists():
            return redirect('universystem:StudentProfileIndexView')
        elif Profile.objects.filter(user= request.user,roles=1).exists():
            return redirect('universystem:TeacherView') 

class IndexView(TemplateResponseMixin,View):
    template_name = 'index.html'
    def get(self,request):
        profile = Profile.objects.all()
        news = News.objects.all()
        return self.render_to_response({'profile': profile,'news':news})

class TeacherView(TemplateResponseMixin,View):
    template_name = 'teacher/home.html'
    def get(self,request):
        profile = Profile.objects.get(user = request.user)
        return self.render_to_response({'profile': profile})


class LessonCreateView(TemplateResponseMixin,View):
    template_name = 'teacher/courses/form.html'

    def get(self,request):
        lesson_form = Lesson_form()
        return self.render_to_response({'lesson_form': lesson_form})
    
    def post(self,request):
        lesson_form = Lesson_form(request.POST, request.FILES)
        if lesson_form.is_valid():#тексеру
            courses_obj = lesson_form.save(commit=False)
            courses_obj.author = request.user
            courses_obj.save()
            return redirect('universystem:LessonView')
        return self.render_to_response({'lesson_form': lesson_form})

class LessonZertView(TemplateResponseMixin,View):
    template_name = 'teacher/courses/form_zert.html'

    def get(self,request):
        lessonZert_form = LessonZert_form()
        return self.render_to_response({'lessonZert_form': lessonZert_form})
    
    def post(self,request):
        lessonZert_form = LessonZert_form(request.POST, request.FILES)
        if lessonZert_form.is_valid():#тексеру
            courses_obj = lessonZert_form.save(commit=False)
            courses_obj.author = request.user
            courses_obj.save()
            return redirect('universystem:LessonView')
        return self.render_to_response({'lessonZert_form': lessonZert_form})

class LessonWorkView(TemplateResponseMixin,View):
    template_name = 'teacher/courses/form_work.html'

    def get(self,request):
        lessonWork_form = LessonWork_form()
        return self.render_to_response({'lessonWork_form': lessonWork_form})
    
    def post(self,request):
        lessonWork_form = LessonWork_form(request.POST, request.FILES)
        if lessonWork_form.is_valid():#тексеру
            courses_obj = lessonWork_form.save(commit=False)
            courses_obj.author = request.user
            courses_obj.save()
            return redirect('universystem:LessonView')
        return self.render_to_response({'lessonWork_form': lessonWork_form})

class LessonView(TemplateResponseMixin,View):
    template_name = 'teacher/courses/lesson.html'

    def get(self,request):
        search_text = request.GET.get('search_text', '')
        lesson = Lesson.objects.filter(author = request.user).order_by('-id');
        if search_text:
            lesson = Lesson.objects.filter(title__icontains=search_text).order_by('-id')
        return self.render_to_response({'lesson': lesson, 'search_text': search_text})
        

class LessonDetailView(TemplateResponseMixin,View):
    template_name = 'teacher/courses/lesson-detail.html'
    def get(self,request, id):
        lesson = Lesson.objects.get(id=id)
        work = laboratorywork.objects.filter(lesson = id)
        srp = SRP.objects.filter(lesson = id)
        return self.render_to_response({'lesson': lesson, 'work':work,'srp':srp})


class StudentProfileIndexView(TemplateResponseMixin,View):
    template_name = 'student/home.html'
    def get(self,request):
        profile = Profile.objects.get(user = request.user)
        return self.render_to_response({'profile': profile})

class LessonsView(TemplateResponseMixin,View):
    template_name = 'student/lesson.html'
    def get(self,request):
        search_text = request.GET.get('search_text', '')
        lesson = Lesson.objects.all().order_by('-id');
        if search_text:
            lesson = Lesson.objects.filter(title__icontains=search_text).order_by('-id')
        return self.render_to_response({'lesson': lesson, 'search_text': search_text})

class MyLessonsView(TemplateResponseMixin,View):
    template_name = 'student/mylesson.html'
    def get(self,request):
        mylesson = EnrollCource.objects.filter(student = request.user).order_by('-id')
        return self.render_to_response({'mylesson': mylesson})

class MyLessonsDetailView(TemplateResponseMixin,View):
    template_name = 'student/mylesson-detail.html'
    def get(self,request, id):
        mylesson = EnrollCource.objects.get(id=id)
        return self.render_to_response({'mylesson': mylesson})

        
class LessonsDetailView(TemplateResponseMixin,View):
    template_name = 'student/lesson-detail.html'
    def get(self,request, id):
        lesson = Lesson.objects.get(id=id)
        coments = Comment.objects.filter(lesson=lesson)
        comment_form = CommentsForm()
        return self.render_to_response({'lesson': lesson, 'id':id,  'comment_form':comment_form,'coments':coments})

    def post(self,request, id):
        lesson = Lesson.objects.get(id=id)
        coments = Comment.objects.filter(lesson=lesson)
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            obj_save = comment_form.save(commit=False)
            obj_save.lesson = lesson
            obj_save.save()
            return redirect('universystem:LessonsDetailView', id=id)
        return self.render_to_response({'lesson': lesson, 'id':id,  'comment_form':comment_form,'coments':coments})


class InboxView(TemplateResponseMixin,View):
    template_name = 'teacher/inbox.html'
    def get(self,request):
        message = Message.objects.filter(recipient = request.user.profile).order_by('-id');
        return self.render_to_response({'message': message})


class AddInboxView(TemplateResponseMixin,View):
    template_name = 'teacher/add-inbox.html'

    def get(self,request):
        message_form = MessageForm()
        return self.render_to_response({'message_form': message_form})
    
    def post(self,request):
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():#тексеру
            message_obj = message_form.save(commit=False)
            message_obj.sender = request.user.profile
            message_obj.save()
            return redirect('universystem:InboxView')
        return self.render_to_response({'message_form': message_form})


class DetailInboxView(TemplateResponseMixin,View):
    template_name = 'teacher/mesdetail.html'
    def get(self,request, id):
        message = Message.objects.get(id=id)
        return self.render_to_response({'message': message})


class StudentInboxView(TemplateResponseMixin,View):
    template_name = 'student/inbox.html'
    def get(self,request):
        message = Message.objects.filter(recipient = request.user.profile).order_by('-id');
        return self.render_to_response({'message': message})
        

class StudentAddInboxView(TemplateResponseMixin,View):
    template_name = 'student/add-inbox.html'

    def get(self,request):
        message_form = MessageForm()
        return self.render_to_response({'message_form': message_form})
    
    def post(self,request):
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():#тексеру
            message_obj = message_form.save(commit=False)
            message_obj.sender = request.user.profile
            message_obj.save()
            return redirect('universystem:StudentInboxView')
        return self.render_to_response({'message_form': message_form})

class StudentDetailInboxView(TemplateResponseMixin,View):
    template_name = 'student/mesdetail.html'
    def get(self,request, id):
        message = Message.objects.get(id=id)
        return self.render_to_response({'message': message})

class TestIndexView(TemplateResponseMixin,View):
    template_name = 'test.html'
    def get(self,request):
        lesson = Lesson.objects.all();
        return self.render_to_response({'lesson': lesson})

class SrpView(TemplateResponseMixin,View):
    template_name = 'student/srp.html'
    def get(self,request):
        src = SRP.objects.all();
        return self.render_to_response({'src': src})

class WorkView(TemplateResponseMixin,View):
    template_name = 'student/zert.html'
    def get(self,request):
        work = laboratorywork.objects.all();
        return self.render_to_response({'work': work})

