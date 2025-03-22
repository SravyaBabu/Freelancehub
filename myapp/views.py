from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"home.html")

def buyerregister(request):
    if request.POST:
        username =  request.POST["username"]
        buyername =  request.POST["buyername"]
        photo = request.FILES["photo"]
        mobile =  request.POST["mobile"]
        dob =  request.POST["dob"]
        address =  request.POST["address"]
        password =  request.POST["password"]
        role = request.POST["role"]
        if Login.objects.filter(username=username).exists():
            messages.info(request,"Already Have Registered")
        log = Login.objects.create(username=username,usertype='Buyer',viewPassword=password)
        log.save()
        buyerregister = Buyer.objects.create(loginid=log,username=username,fullname=buyername,photo=photo,mobile=mobile,dob=dob,address=address,role=role)
        buyerregister.save()
        return redirect('/login')
    return render(request,"BuyerRegister.html")



def coderregister(request):
    if request.POST:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        dob = request.POST["dob"]
        intro = request.POST["intro"]
        role = request.POST["role"]
        password = request.POST["password"]
        photo = request.FILES["photo"]
        if Login.objects.filter(username=username).exists():
            messages.info(request,"Already Have Registered")
        log = Login.objects.create(username=username,usertype='Coder',viewPassword=password,status="Pending")
        log.save()
        coderregister = Coder.objects.create(loginid=log,fullname=fullname,username=username,address=address,dob=dob,mobile=mobile,intro=intro,role=role,photo=photo)
        coderregister.save()
        return redirect('/login')
    return render(request,"register.html")

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userlogin = Login.objects.filter(username=username,viewPassword=password).first()
        if userlogin is not None:
            request.session['uid']=userlogin.id
            if userlogin.usertype=="Admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/admindashboard")
            elif userlogin.usertype=="Coder":
                messages.info(request,"Welcome To The Coder Dashboard")
                return redirect("/coderprofile")
            elif userlogin.usertype=="Buyer":
                messages.info(request,"Welcome To The Buyer Dashboard")
                return redirect("/buyerprofile")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
        else:
            messages.info(request,"Invalid Username Or Password")
            return redirect("/login")
    return render(request,'login.html')

def admindashboard(request):
    projects = Projects.objects.all()
    return render(request,"Admin/admindashboard.html",{'projects':projects})


def admincoderprofilefull(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coderid = request.GET.get('coderid')
    coder = Coder.objects.get(id=coderid)
    projects = Projects.objects.filter(doneby=coder)
    coderskills = Skills.objects.filter(coderid = coder)
    coderreview = CoderReview.objects.filter(coderid=coder)
    return render(request, "Admin/coderprofilefulladmin.html", {'buyer':buyer,'coder':coder,'projects':projects,'coderskills':coderskills,'coderreview':coderreview})



def manageusers(request):
    coderregister = Coder.objects.all()
    buyerregister = Buyer.objects.all()
    userlist = list(buyerregister) + list(coderregister)
    return render(request,'Admin/manageusers.html',{'userlist':userlist})

def approveuser(request):
    id = request.GET.get('id')
    approvinguser = Login.objects.filter(id=id).update(status="Approved")
    return redirect('/admindashboard')

def deleteuser(request):
    id = request.GET.get('id')
    deleteinguser = Login.objects.filter(id=id).update(status="Inactive")
    messages.info(request,"User Deleted")
    return redirect('/admindashboard')



def viewcoders(request):
    uid=request.session['uid']
    coderregister = Coder.objects.all()
    skills = Skills.objects.all()
    return render(request,'Admin/viewcoders.html',{'coderregister':coderregister,'skills':skills})

def viewbuyer(request):
    buyerregister = Buyer.objects.all()
    return render(request,'Admin/viewbuyer.html',{'buyerregister':buyerregister})

def coderprofile(request):
    uid=request.session['uid']
    coder = Coder.objects.get(loginid = uid)
    coderskills = Skills.objects.filter(coderid = coder)
    return render(request,'Coder/coderprofile.html',{'coder':coder,'coderskills':coderskills})

def editcoderprofile(request):
    uid=request.session['uid']
    coder = Coder.objects.filter(loginid=uid).first()
    if request.POST:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        dob = request.POST["dob"]
        intro = request.POST["intro"]
        role = request.POST["role"]
        coder.fullname = fullname
        coder.username = username
        coder.mobile = mobile
        coder.address = address
        coder.dob = dob
        coder.intro = intro
        coder.role = role
        if request.FILES:
            photo = request.FILES["photo"]
            coder.photo=photo
        coder.save()
        return redirect('/coderprofile')
    context = {'coder':coder}
    return render(request,'Coder/editprofile.html',context)

def buyerprofile(request):
    uid=request.session['uid']
    buyer = Buyer.objects.get(loginid = uid)
    buyerdata = BuyerData.objects.filter(buyerid = buyer)
    return render(request,'Buyer/buyerprofile.html',{'buyer':buyer,'buyerdata':buyerdata})

def buyeredit(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    if request.POST:
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        dob = request.POST["dob"]
        role = request.POST["role"]
        buyer.fullname = fullname
        buyer.username = username
        buyer.mobile = mobile
        buyer.address = address
        buyer.dob = dob
        buyer.role = role
        if request.FILES:
            photo = request.FILES["photo"]
            buyer.photo=photo
        buyer.save()
        return redirect('/buyerprofile')
    context = {'buyer':buyer}
    return render(request,'Buyer/buyeredit.html',context)

def addskills(request):
    uid=request.session['uid']
    coder = Coder.objects.filter(loginid=uid).first()
    if request.POST:
        skills = request.POST["skills"]
        coderskills = Skills.objects.create(coderid=coder,skills=skills)
        coderskills.save()
        return redirect('/coderprofile')
    return render(request,'Coder/addskills.html',{'coder':coder})

def updateskills(request):
    return render(request,'Coder/addskills.html')



def buyerdata(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    if request.POST:
        company = request.POST["company"]
        companydetails = request.POST["companydetails"]
        buyerdetails = request.POST["buyerdetails"]
        buyerdata = BuyerData.objects.create(buyerid=buyer,companydetails=companydetails,company=company,buyerdetails=buyerdetails)
        buyerdata.save()
        return redirect('/buyerprofile')
    return render(request,'Buyer/buyerdata.html',{'buyer':buyer})

def buyerviewcoders(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    uid = request.session.get('uid')
    logins = Login.objects.filter(status="Approved") 
    coderregister = Coder.objects.filter(loginid__in=logins) 
    return render(request, 'Buyer/viewcoders.html', {'buyer': buyer, 'coderregister': coderregister})


def viewcoderskills(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coderid = request.GET.get('coderid')
    coder = Coder.objects.filter(id=coderid).first()
    coderskills = Skills.objects.filter(coderid=coder)
    return render(request, 'Buyer/coderskills.html', {'coderskills': coderskills,'coder':coder,'buyer':buyer})

def addprojects(request):
    today = datetime.now()
    today = today.strftime('%Y-%m-%d')
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    if request.POST:
        title = request.POST['title']
        jobtype = request.POST['jobtype']
        categories = request.POST['categories']
        duration = request.POST['duration']
        salary = request.POST['salary']
        experience = request.POST['experience']
        careerlevel = request.POST['careerlevel']
        description = request.POST['description']
        attachment = request.FILES['attachment']
        projects = Projects.objects.create(buyerid=buyer,title=title,jobtype=jobtype,categories=categories,duration=duration,salary=salary,experience=experience,careerlevel=careerlevel,description=description,attachment=attachment,status="Published",today=today)
        projects.save()
        return redirect('/buyerprofile')
    return render(request,'Buyer/addprojects.html',{'buyer':buyer})


def viewprojects(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    projects = Projects.objects.filter(buyerid=buyer)
    return render(request,'Buyer/viewprojects.html',{'buyer':buyer,'projects':projects})

def coderviewprojects(request):
    uid=request.session['uid']
    coder = Coder.objects.filter(loginid=uid).first()   
    projects = Projects.objects.exclude(assignstatus="Assigned")
    return render(request,'Coder/buyerprojects.html',{'coder':coder,'projects' :projects,})

def coderprojectdetails(request):
    uid=request.session['uid']
    coder = Coder.objects.filter(loginid=uid).first()   
    id = request.GET.get('id')
    projects = Projects.objects.filter(id=id).first()   
    return render(request,'Coder/coderprojectdetails.html',{'coder':coder,'projects':projects})

def buyerprojectdetails(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    id = request.GET.get('id')
    projects = Projects.objects.filter(id=id).first()

    return render(request,'Buyer/buyerprojectdetails.html',{'buyer':buyer,'projects':projects})

def buyerprojectedit(request):
    todays = datetime.now()
    todays = todays.strftime('%Y-%m-%d')
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    id = request.GET.get('id')
    projects = Projects.objects.filter(id=id).first()
    if request.POST:
        title = request.POST["title"]
        jobtype = request.POST["jobtype"]
        categories = request.POST["categories"]
        duration = request.POST["duration"]
        salary = request.POST["salary"]
        experience = request.POST["experience"]
        careerlevel = request.POST["careerlevel"]
        description = request.POST["description"]
        projects.title = title 
        projects.jobtype = jobtype
        projects.categories = categories
        projects.duration = duration
        projects.salary = salary
        projects.experience = experience
        projects.careerlevel = careerlevel
        projects.description = description
        projects.status = "Published"
        projects.today = todays
        if request.FILES:
            attachment = request.FILES["attachment"]
            projects.attachment=attachment
        projects.save()
        return redirect('/viewprojects')
    return render(request,'Buyer/buyerprojectedit.html',{'buyer':buyer,'projects':projects})

def projectdelete(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    id = request.GET.get('id')
    projects = Projects.objects.filter(id=id).update(status="Inactive")
    return render(request,'Buyer/viewprojects.html',{'buyer':buyer,'projects':projects})


def applyproject(request):
    todays = datetime.now().strftime('%Y-%m-%d')
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    project_id = request.GET.get('id')
    project = get_object_or_404(Projects, id=project_id)
    apply = ApplyProject.objects.create(projectid=project, coderid=coder, date=todays)
    return redirect('/coderviewprojects',{'coder': coder}) 


def proposals(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(buyerid=buyer)
    proposals = ApplyProject.objects.filter(projectid__in=project,status="Pending") 
    return render(request,'Buyer/projectproposals.html',{'buyer':buyer,'proposals':proposals})

def disapprovecoder(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    id = request.GET.get('id')
    apply = ApplyProject.objects.filter(id=id).update(status="Rejected")
    return redirect('/proposals',{'buyer':buyer})

    
def approvecoder(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    id = request.GET.get('id') 
    project =  request.GET.get('project') 
    apply = ApplyProject.objects.filter(id=id).update(status="Approved")
    projects = Projects.objects.filter(id=project).update(assignstatus="Assigned")
    return redirect('/proposals',{'buyer':buyer})

def rejected(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(buyerid=buyer)
    proposals = ApplyProject.objects.filter(projectid__in=project) 
    return render(request,'Buyer/Rejected.html',{'buyer':buyer,'proposals':proposals})

def approvedproposals(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(buyerid=buyer)
    proposals = ApplyProject.objects.filter(projectid__in=project) 
    return render(request,'Buyer/ApprovedPro.html',{'buyer':buyer,'proposals':proposals})

def appliedprojects(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    proposals = ApplyProject.objects.filter(coderid=coder) 
    return render(request,'Coder/appliedprojects.html',{'coder':coder,'proposals':proposals})

def activeprojects(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    proposals = ApplyProject.objects.filter(coderid=coder) 
    return render(request,'Coder/activeprojects.html',{'coder':coder, 'proposals':proposals})

def viewactiveproject(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    id = request.GET.get('id')
    projects = Projects.objects.filter(id=id)
    return render(request,'Coder/coderprojectdetails.html',{'coder':coder,'projects':projects})

def uploadwork(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    todays = datetime.now().strftime('%Y-%m-%d')  
    id = request.GET.get('id')
    project = request.GET.get('project')
    projects = Projects.objects.filter(id=project).first()
    if request.method == "POST":
        finalupload = request.FILES.get("finalupload")  
        if finalupload: 
            projects.finalupload = finalupload
            projects.doneby = coder
            projects.uploaddate = todays
            projects.save() 
            return redirect('/coderviewprojects') 
    return render(request, 'Coder/uploadworks.html', {'coder': coder, 'projects': projects})


def completed(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    apply = ApplyProject.objects.exclude(finalstatus="Approved")
    return render(request,'Buyer/completed.html',{'buyer':buyer,'apply':apply})

def approvesample(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coder = request.GET.get('coder')
    project = request.GET.get('project')
    apply = ApplyProject.objects.filter(coderid=coder,projectid=project).update(finalstatus="Approved")
    return redirect('/completed',{'buyer':buyer})

def disapprovesample(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coder = request.GET.get('coder')
    project = request.GET.get('project')
    apply = ApplyProject.objects.filter(coderid=coder,projectid=project).update(finalstatus="Rejected")
    projects = Projects.objects.filter(id=project).update(finalupload=None,doneby=None,uploaddate=None)
    return redirect('/completed',{'buyer':buyer})


def final(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(buyerid=buyer)
    return render(request,'Buyer/final.html',{'buyer':buyer,'project':project})


def uploadzip(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    todays = datetime.now().strftime('%Y-%m-%d')  
    id = request.GET.get('id')
    project = request.GET.get('project')
    projects = Projects.objects.filter(id=project).first()
    if request.method == "POST":
        prototype = request.FILES.get("prototype")  
        if prototype: 
            projects.prototype = prototype
            projects.doneby = coder
            projects.uploaddate = todays
            projects.save() 
            messages.info(request,"File Uploaded")
            return redirect('/finalproject') 
    return render(request, 'Coder/uploadzip.html', {'coder': coder, 'projects': projects})

def finalproject(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    apply = ApplyProject.objects.filter(finalstatus="Approved",coderid=coder)
    return render(request,'Coder/finalupload.html',{'coder':coder,'apply':apply})

def payment(request):
    uid = request.session.get('uid')
    buyer = Buyer.objects.filter(loginid=uid).first()
    project_id = request.GET.get('id')
    project = Projects.objects.filter(id=project_id, buyerid=buyer).first()
    if not project:
        return redirect('/final')
    return render(request, 'Buyer/payment.html', {'buyer': buyer, 'project': project})


def paidcoder(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id")  
    else:
        project_id = request.GET.get("id")  
    uid = request.session.get('uid')
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(id=project_id, buyerid=buyer).first()
    project.projectstatus = "Completed"
    project.save()
    messages.success(request, "Payment successful! Project status updated.")
    return redirect('/final') 


def reviews(request):
    uid = request.session.get('uid')
    coder = Coder.objects.filter(loginid=uid).first()   
    coderreview = CoderReview.objects.filter(coderid=coder)
    return render(request,'Coder/reviews.html',{'coder':coder,'coderreview':coderreview})

def buyercoderreviews(request):
    uid=request.session['uid']
    coderid = request.GET.get('coderid')
    coder = Coder.objects.filter(id=coderid).first()
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(buyerid=buyer,projectstatus="Completed")
    return render(request,'Buyer/reviewcoder.html',{'buyer':buyer,'project':project})

def historybuyer(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    project = Projects.objects.filter(buyerid=buyer,projectstatus="Completed")
    coderreview = CoderReview.objects.filter(buyerid=buyer)
    return render(request,'Buyer/historybuyer.html',{'buyer':buyer,'project':project,'coderreview':coderreview})

def writereview(request):
    uid=request.session['uid']
    coderid = request.GET.get('coderid')
    coder = Coder.objects.filter(id=coderid).first()
    buyer = Buyer.objects.filter(loginid=uid).first()
    if request.method == "POST":
        review = request.POST.get("review")
        feedback = request.POST.get("feedback")
        CoderReview.objects.create(coderid=coder,buyerid=buyer,review=int(review),feedback=feedback)
        return redirect("/buyercoderreviews")
    return render(request, "Buyer/writereview.html", {"coder": coder,'buyer':buyer})

def viewcoderreviews(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coderid = request.GET.get('coderid')
    coder = Coder.objects.get(id=coderid)
    coderreview = CoderReview.objects.filter(coderid=coder)
    return render(request, "Buyer/viewcoderreviews.html", {'buyer':buyer,'coderreview':coderreview,'coder':coder})

def viewcompletedprojects(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coderid = request.GET.get('coderid')
    coder = Coder.objects.get(id=coderid)
    projects = Projects.objects.filter(doneby=coder,projectstatus="Completed")
    return render(request, "Buyer/viewcompletedprojects.html", {'buyer':buyer,'projects':projects,'coder':coder})

    
def coderprofilefull(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    coderid = request.GET.get('coderid')
    coder = Coder.objects.get(id=coderid)
    projects = Projects.objects.filter(doneby=coder)
    coderskills = Skills.objects.filter(coderid = coder)
    coderreview = CoderReview.objects.filter(coderid=coder)
    return render(request, "Buyer/coderprofilefull.html", {'buyer':buyer,'coder':coder,'projects':projects,'coderskills':coderskills,'coderreview':coderreview})




def chatsbuyer(request):
    uid=request.session['uid']
    buyer = Buyer.objects.filter(loginid=uid).first()
    return render(request, "Buyer/chatbuyer.html", {'buyer':buyer})

def chat(request):
    uid = request.session["uid"]
    name = ""
    artistData = Buyer.objects.all() #To get all the data of reciever  
    id = request.GET.get("id")
    getChatData = Chat.objects.filter(
        Q(coderid__loginid=uid) & Q(buyerid=id))
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    userid = Coder.objects.get(loginid=uid)
    if id:
        buyerid = Buyer.objects.get(id=id)
        name = buyerid.fullname 
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chat.objects.create(
            coderid=userid, message=message, buyerid=buyerid, time=formatted_time, utype="Coder")
        sendMsg.save()
    return render(request, "Coder/chatcoder.html", {"artistData": artistData, "getChatData": getChatData, "buyerid": name, "id": id})



def reply(request):
    uid = request.session["uid"]
    name = ""
    userData = Coder.objects.all()
    id = request.GET.get("id")
    getChatData = Chat.objects.filter(
        Q(buyerid__loginid=uid) & Q(coderid=id))
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    buyerid = Buyer.objects.get(loginid=uid)
    if id:
        userid = Coder.objects.get(id=id)
        name = userid.fullname
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chat.objects.create(
            coderid=userid, message=message, buyerid=buyerid, time=formatted_time, utype="Buyer")
        sendMsg.save()
    return render(request, "Buyer/chatbuyer.html", {"userData": userData, "getChatData": getChatData, "userid": name, "id": id})
