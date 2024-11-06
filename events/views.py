from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, month, year):
    name = "Brethren"
    month = month.title() #To allow lowercase or uppercase (capitalize will also work)
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number) #Makes sure its an integer

    # crete a calendar
    cal = HTMLCalendar().formatmonth(
        year, month_number)
    
    # Get current year
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%I:%M %p')

    return render(request, 
        'home.html', {
        "name":name,
        "month":month,
        "year":year,
        "month_number":month_number,
        "cal":cal,
        "current_year":current_year,
        "time":time,
        })
