from django.shortcuts import render
from ipware import get_client_ip   
import os
    
def image(request):
	IP = getIP(request)
	file = "/home/people/ss99/gwas/gwaspage/static/data/%sstatic.bed"%IP
	os.system('./static/static_image.sh %s /home/people/ss99/gwas/gwaspage/static/image/static.png'%IP)

    return render(request,'imgview/image.html',{'title':'Image'})

def getIP(request):
        ip, _ = get_client_ip(request)
        if ip is None:
            # Unable to get the client’s IP address
            return “0.0.0.0”
        else:
            return ip