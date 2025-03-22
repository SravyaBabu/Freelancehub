"""
URL configuration for Projecthub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('buyerregister/',views.buyerregister),
    path('coderregister/',views.coderregister),
    path('login/',views.login),
    path('admindashboard/',views.admindashboard),
    path('manageusers/',views.manageusers),
    path('approveuser/',views.approveuser),
    path('deleteuser/', views.deleteuser),
    path('viewcoders/',views.viewcoders),
    path('viewbuyer/',views.viewbuyer),
    path('coderprofile/',views.coderprofile),
    path('editcoderprofile/',views.editcoderprofile),
    path('buyerprofile/',views.buyerprofile),
    path('buyeredit/',views.buyeredit),
    path('addskills/',views.addskills),
    path('buyerdata/',views.buyerdata),
    path('buyerviewcoders/',views.buyerviewcoders),
    path('viewcoderskills/',views.viewcoderskills),
    path('addprojects/',views.addprojects),
    path('viewprojects/',views.viewprojects),
    path('coderviewprojects/',views.coderviewprojects),
    path('coderprojectdetails/',views.coderprojectdetails),
    path('buyerprojectdetails/',views.buyerprojectdetails),
    path('buyerprojectedit/',views.buyerprojectedit),
    path('projectdelete',views.projectdelete),
    path('applyproject',views.applyproject),
    path('updateskills',views.updateskills),
    path('proposals/',views.proposals),
    path('approvecoder/',views.approvecoder),
    path('disapprovecoder/',views.disapprovecoder),
    path('rejected/',views.rejected),
    path('approvedproposals',views.approvedproposals),
    path('appliedprojects',views.appliedprojects),
    path('activeprojects',views.activeprojects),
    path('viewactiveproject/',views.viewactiveproject),
    path('uploadwork/',views.uploadwork),
    path('completed/',views.completed),
    path('final/',views.final),
    path('payment/',views.payment),
    path('reviews/',views.reviews),
    path('approvesample/',views.approvesample),
    path('disapprovesample/',views.disapprovesample),
    path('finalproject/',views.finalproject),
    path('uploadzip/',views.uploadzip),
    path('paidcoder/',views.paidcoder),
    path('buyercoderreviews/',views.buyercoderreviews),
    path('historybuyer/',views.historybuyer),
    path('writereview/',views.writereview),
    path('viewcoderreviews/',views.viewcoderreviews),
    path('viewcompletedprojects/',views.viewcompletedprojects),
    path('coderprofilefull/',views.coderprofilefull),
    path('admincoderprofilefull/',views.admincoderprofilefull),
    path('reply/',views.reply),
    path('chat/',views.chat)








    

    

    












]
