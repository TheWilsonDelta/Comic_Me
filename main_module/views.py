import base64
import datetime
import re
import uuid

from PIL import Image
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main_module.models import *


@login_required
@csrf_exempt
def create(request):
    if request.is_ajax():
        title = (request.POST['comictitle'])
        dataurl = (request.POST['imageBase64'])
        language = (request.POST['language'])
        category = (request.POST['category'])

        filename = "_".join([str(uuid.uuid4()), datetime.datetime.now().strftime("%y%m%d_%H%M%S")]) + ".png"

        imgstr = re.search(r'data:image/png;base64,(.*)', dataurl).group(1)
        location = '/usr/src/app/media/' + filename
        output = open(location, 'wb')
        decoded = base64.b64decode(imgstr)
        output.write(decoded)
        output.close()

        form = Image(name=title, user=request.user, main_image=filename,
                     language=Language.objects.get(name=language), category=Category.objects.get(name=category))
        form.save()

        return HttpResponse(status=200)
    context = {
        'category': Category.objects.all(),
        'language': Language.objects.all()
    }
    return render(request, 'main_module/editor.html', context=context)


@login_required
def home(request):
    return render(request, "main_module/home.html", {})


@login_required
def comics(request):
    context = {
        'comics': Image.objects.filter(user=request.user).order_by('-uploaded_at')
    }
    return render(request, "main_module/comics.html", context=context)


@staff_member_required
def staff_list(request):
    context = {
        'image': Image.objects.all().order_by('-uploaded_at')
    }
    return render(request, "main_module/staff_list.html", context=context)


@login_required
def logout_now(request):
    logout(request)
    return render(request, "../templates/registration/logout.html", {})


@login_required
def help(request):
    return render(request, "main_module/help.html", {})
