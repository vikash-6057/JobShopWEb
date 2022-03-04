from django.shortcuts import render,redirect
from .models import JobModel
from .forms import JobForm
from .JobShopImp.ion.Job import Job
from .JobShopImp.service.JobSchedulerServiceImpl import JobSchedulerServiceImpl


# Create your views here.
def index(request):
    jobScheduler = JobSchedulerServiceImpl()
    jobs = list()
    # Note: Number of machine is fixed(we can change it)
    no_machines = 2
    job_data = JobModel.objects.all()[:1]
    input_file_name = job_data[0].job.path
    input_file = open(input_file_name,"r")
    for line in input_file:
        name,duration,priority,deadline,user_type = line.split(',')
        job = Job()
        job.setDeadline(int(deadline))
        job.setJobName(name)
        job.setDuration(int(duration))
        job.setPriority(int(priority))
        job.setUserType(int(user_type))
        jobs.append(job)
    input_file.close()
    fcfs = jobScheduler.firstComeFirstServe(no_machines, jobs)
    print()
    sjf = jobScheduler.shortestJobFirst(no_machines, jobs)
    print()
    fps = jobScheduler.fixedPriorityScheduling(no_machines, jobs)
    print()
    edf = jobScheduler.earliestDeadlineFirst(no_machines, jobs)
    context = {
        'fcfs':fcfs,
        'sjf':sjf,
        'fps':fps,
        'edf':edf
    }
    return render(request, 'Index.html',context)

def show_data(request):
    job_data = JobModel.objects.all()[:1]
    input_file_name = job_data[0].job.path
    input_file = open(input_file_name,"r")
    file = input_file.read()
    input_file.close()
    return render(request,'success.html',{'file':file})

def upload(request):
    if request.method=='POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = JobForm()
    return render(request,'upload.html',{'form':form})
        