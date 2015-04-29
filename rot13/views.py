from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

def do_rot13(s):
    s=s.encode(encoding="rot-13")
    return s
#        return write_form(ciphered_string)
def cipher(request):
    def write_form(text=""):
        return render(request,'rot13/form.html',{"t":text})
    if(request.method=='GET'):
        return write_form()
    if(request.method=='POST'):
        input_txt=request.POST.get('txt','')
        ciphered_string=do_rot13(input_txt)
        return write_form(ciphered_string)
