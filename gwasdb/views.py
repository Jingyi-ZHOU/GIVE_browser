from django.http                        import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts                   import get_object_or_404, render, redirect
from django.urls                        import reverse
from django.views.decorators.csrf       import csrf_exempt
from django.conf                        import settings
from django.apps                        import apps
from django.db.models                   import Q

from .forms                             import *
# from .runbash                           import ManageGiveData

import json
import re
import os
import glob

PPLS = ['AFR', 'AMR', 'EAS', 'EUR']

def findBy(**kwargs):
    chrs = kwargs.get('chrs', '')
    r2 = kwargs.get('r2', '')
    ppl = kwargs.get('ppl', '')
    snp = kwargs.get('snp', '')
    model_name = chrs.capitalize() + 'A' + ppl.lower()
    crit = (Q(r2__gte=r2) & (Q(stop1=snp) | Q(stop2=snp)))
    data = apps.get_model('gwasdb', model_name).objects.filter(crit)

    print(data)

def find(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = LargeForm(request.POST)
        form2 = ChrSNPForm(request.POST)
        form3 = UploadSNPs(request.POST)
        form4 = DiseaseName(request.POST)
        # check whether it's valid:
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            data = request.POST
            # print(data)
            input_way = data.get('inputWay')
            if input_way == '1':
                chrs = 'chr' + str(int(data.get('chrs'))+1)
                snp = int(data.get('snp'))
                r2 = float(data.get('r2'))
                ppl = PPLS[int(data.get('ppl'))]
                results = findBy(chrs = chrs, snp = snp, r2 = r2, ppl = ppl)
            elif input_way == 2:
                pass
            else:
                pass
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = LargeForm()
        form2 = ChrSNPForm()
        form3 = UploadSNPs()
        form4 = DiseaseName()
        

    context = {
        'title':'Find LD SNPs', 
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
    }
    return render(request, 'gwasdb/find.html', context)