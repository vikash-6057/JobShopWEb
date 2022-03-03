from django.shortcuts import render
from .models import JobModel
from .JobShopImp.ion.Job import Job
from .JobShopImp.service.JobSchedulerServiceImpl import JobSchedulerServiceImpl

# Create your views here.
def index(request):
    # jobScheduler = JobSchedulerServiceImpl()
    # jobs = list()
    # job = Job()
    # no_machines = 1
    # no_machines = int(input("Enter number of machine(s) :"))
    # input_file_name = input("Select a '.txt' file : ")
    # print()
    # input_file = open(input_file_name,"r")
    # for line in input_file:
    #     name,duration,priority,deadline,user_type = line.split(',')
    #     job = Job.Job()
    #     job.setDeadline(int(deadline))
    #     job.setJobName(name)
    #     job.setDuration(int(duration))
    #     job.setPriority(int(priority))
    #     job.setUserType(int(user_type))
    #     jobs.append(job)
    # jobScheduler.firstComeFirstServe(no_machines, jobs)
    # print()
    # jobScheduler.shortestJobFirst(no_machines, jobs)
    # print()
    # jobScheduler.fixedPriorityScheduling(no_machines, jobs)
    # print()
    # jobScheduler.earliestDeadlineFirst(no_machines, jobs)
    return render(request, 'Index.html')
