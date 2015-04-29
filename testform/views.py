from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

def valid_day(day):
    if day.isdigit():
        if int(day)>0 and int(day)<32:
            return int(day)
        else:
            return None

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    for x in months:
        if month.lower()==x.lower():
            return x
    return None

def valid_year(year):
    if year.isdigit():
        if int(year)<2021 and int(year)>1899:
            return int(year)
        else:
            return None

def thanks_handler(request):
    return HttpResponse("Thanks, that's totally a valid date.")

def form(request):
    def write_form(error="",day="",month="",year=""):
        return render(request, 'testform/form.html', {"error":error,"day":day,"month":month,"year":year})
    if request.method=='GET':
        return write_form()
    if request.method=='POST':
        input_day=request.POST.get('day','')
        input_month=request.POST.get('month','')
        input_year=request.POST.get('year','')

        is_valid_day=valid_day(input_day)
        is_valid_month=valid_month(input_month)
        is_valid_year=valid_year(input_year)
        if not(is_valid_day and is_valid_month and is_valid_year):
            return write_form("Hey, that doesn't look valid to me",input_day,input_month,input_year)
        else:
            return HttpResponseRedirect('thanks')
