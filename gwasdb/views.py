from django.http                        import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts                   import get_object_or_404, render, redirect
from django.urls                        import reverse
from django.views.decorators.csrf       import csrf_exempt
from django.conf                        import settings
from django.apps                        import apps
from django.db.models                   import Q

from .forms                             import *
# from .runbash                           import ManageGiveData
from collections import defaultdict
import json
import re
import os
import glob

PPLS = ['AFR', 'AMR', 'EAS', 'EUR']

def findBy(**kwargs):
    chrs = kwargs.get('chrs', '')
    r2 = kwargs.get('r2', '')
    ppl = kwargs.get('ppl', '')
    snps = kwargs.get('snps', '')
    model_name = chrs.capitalize() + 'A' + ppl.lower()
    crit = Q()
    for snp in snps:
        crit |= Q(stop1=snp)
        crit |= Q(stop2=snp)
    crit = (Q(r2__gte=r2) & crit)
    data = apps.get_model('gwasdb', model_name).objects.filter(crit)
    res = list()
    for d in data:
        res.append([chrs, d.stop1,d.stop2,d.r2])
    print(res)
    return res

def find(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        results = []
        # create a form instance and populate it with data from the request:
        form1 = LargeForm(request.POST)
        form2 = ChrSNPForm(request.POST)
        form3 = UploadSNPs(request.POST, request.FILES)
        form4 = DiseaseName(request.POST)
        # check whether it's valid:
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            data = request.POST
            file = request.FILES.get('file', None)
            # print(data)
            input_way = data.get('inputWay')
            if input_way == '1':
                r2 = float(data.get('r2'))
                ppl = PPLS[int(data.get('ppl'))]
                if file:
                    queries = defaultdict(list)
                    lines = file.readlines()
                    for l in lines:
                        try:
                            ch, _, stop = l.decode("utf-8").split('\t')
                        except:
                            continue
                        queries[ch].append(int(stop))
                    for chrs, snps in queries.items():
                        res = findBy(chrs = chrs, snps = snps, r2 = r2, ppl = ppl)
                        if res:
                            results.extend(res)

                else:
                    chrs = 'chr' + str(int(data.get('chrs'))+1)
                    snp = int(data.get('snp'))
                    res = findBy(chrs = chrs, snps = [snp], r2 = r2, ppl = ppl)
                    if res:
                        results.extend(res)
            elif input_way == 2:
                pass
            else:
                pass
        print(results,len(results))
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = LargeForm()
        form2 = ChrSNPForm()
        form3 = UploadSNPs()
        form4 = DiseaseName()
        results = None
        

    context = {
        'title':'Find LD SNPs', 
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'results': results
    }
    return render(request, 'gwasdb/find.html', context)