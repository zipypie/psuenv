from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg.views import OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView
from studentorg.views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
from studentorg.views import CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView
from studentorg.views import ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from studentorg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.HomePageView.as_view(), name= 'home'),
    path('organization_list' , OrganizationList.as_view(), name= 'organization-list'),
    path('organization_list/add' , OrganizationCreateView.as_view(), name= 'organization-add'),
    path('organization_list/<pk>' , OrganizationUpdateView.as_view(), name= 'organization-update'),
    path('organization_list/<pk>/delete' , OrganizationDeleteView.as_view(), name= 'organization-delete'),
    path('orgmember_list/', OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmember_list/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/<pk>', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/<pk>/delete', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('student_list/add/', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('college_list/', CollegeListView.as_view(), name='college-list'),
    path('college_list/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),
    path('program_list/', ProgramListView.as_view(), name='program-list'),
    path('program_list/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),

    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

]
