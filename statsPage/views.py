from django.shortcuts import render
from django.http import HttpResponse
from statsPage.models import Ticket

def statsPageView(request):
    return render(request, 'statsPage/showData.html')

def enterDataPageView(request):
    return render(request, 'statsPage/enterData.html')

def storeDriverPageView(request):
    #Check to see if the form method is a get or post
    if request.method == 'POST':

    #Create a new employee object from the model (like a new record)
    #     new_Driver = Driver()
    
    # #Store the data from the form to the new object's attributes (like columns)
    #     new_Driver.fName = request.POST.get('fName')
    #     new_Driver.lName = request.POST.get('lName')
    #     new_Driver.hometown = request.POST.get('homeTown')
    
    #Get all of the State objects (record or records) for the current employee state
    # new_state = State.objects.get(state_abbrev = request.POST.get('emp_state'))
    
    #Create a new Contact Information object (record)
        new_Ticket = Ticket()
    
    #Store the data from the form to the contact phone attribute (column)
        new_Ticket.fname = request.POST.get('fname')
        new_Ticket.lname = request.POST.get('lname')
        new_Ticket.date = request.POST.get('date')
        new_Ticket.amount = request.POST.get('amount')
        new_Ticket.locationStreet = request.POST.get('locationStreet')
        new_Ticket.locationCity = request.POST.get('locationCity')
        new_Ticket.speedMPH = request.POST.get('speedMPH')

    
    #Save the contact information record which will generate the autoincremented id
    #     new_Driver.save()
    
    # #Store the newly created contact information id (object or record reference) to the employee record
    #     new_Ticket.driver = new_Driver
    
    
    #Save the employee record
        new_Ticket.save()
    
    #Make a list of all of the employee records and store it to the variable
        data = Ticket.objects.all()
    
    #Assign the list of employee records to the dictionary key "our_emps"
        context = {
            "our_tickets" : data
        }
    return render(request, 'statsPage/showData.html', context) 