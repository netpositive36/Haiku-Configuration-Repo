from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout

from .models import Component
from .models import Device

def index(request):
    all_components = Component.objects.all().order_by('-date_modified')[:5]
    all_devices = Device.objects.all().order_by('-date_modified')[:5]
    context = {
        'all_devices' : all_devices,
        'all_components' : all_components
    }

    return render(request, 'repo/index.html', context)

def loginIndex(request):
    return render(request, 'repo/login.html', {})

def authenticateLogin(request):
    username = password = ""

    if request.POST:
        username = request.POST.get('login_email')
        password = request.POST.get('login_password')

        logout(request)

        user = authenticate(username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)

    return HttpResponseRedirect(reverse('repo:index'))

def componentList(request):
    all_components = Component.objects.all()
    context = { 'all_components' : all_components }

    return render(request, 'repo/component_list.html', context)

def sortComponents(request):
    sort_name = request.POST['name_to_sort']

    # sorting based on name
    all_components = Component.objects.all()
    sorted_components = []
    for grabbed_component in all_components:
        if sort_name in grabbed_component.name:
            sorted_components.append(grabbed_component)

    context = { 'all_components' : sorted_components }

    return render(request, 'repo/component_list.html', context)

def deviceList(request):
    all_devices = Device.objects.all()
    context = {'all_devices' : all_devices}

    return render(request, 'repo/device_list.html', context)

def sortDevices(request):
    sort_name = request.POST['name_to_sort']

    # sorting based on name
    all_devices = Device.objects.all()
    sorted_devices = []
    for grabbed_device in all_devices:
        if sort_name in grabbed_device.name:
            sorted_devices.append(grabbed_device)

    context = {'all_devices' : sorted_devices}

    return render(request, 'repo/device_list.html', context)

def deviceDetail(request, device_id):
    myDevice = get_object_or_404(Device, pk=device_id)
    context = {
        'device_name' : myDevice.name,
        'all_devices' : [myDevice]
    }

    return render(request, 'repo/device.html', context)

def componentDetail(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = {
        'component_name' : myComponent.name,
        'all_components' : [myComponent]
    }

    return render(request, 'repo/component.html', context)

def addTest(request):
    return render(request, 'repo/add_test.html', {})

def createTest(request):
    if request.user.is_authenticated():
        component_name = request.POST['component_name']
        device_name = request.POST['device_name']

        author = request.user.username
        author_email = request.user.email

        if component_name != '':
            rating = request.POST['component_rating']
            is_working = "Failed"
            notes = request.POST['component_test_notes']
            component_category = request.POST['component_category']

            try:
                if str(request.POST['group1']) == "on":
                    is_working = "Passed"
            except:
                pass

            newComponent = Component(name = component_name,
                rating = rating,
                is_working = is_working,
                notes = notes,
                author = author,
                author_email = author_email,
                category = component_category)
            newComponent.save()

        if device_name != '':
            rating = request.POST['device_rating']
            is_working = "Failed"
            notes = request.POST['device_test_notes']

            device_cpu = request.POST['device_cpu']
            device_motherboard = request.POST['device_motherboard']
            device_hard_drive = request.POST['device_hard_drive']
            device_sound = request.POST['device_sound']
            is_sound_working = "Failed"
            device_display_name = request.POST['device_display_name']
            device_display_config = request.POST['device_display_config']
            is_display_working = "Failed"
            device_dedicated_graphics = request.POST['device_dedicated_graphics']
            is_dedicated_graphics_working = request.POST['device_dedicated_graphics']

            try:
                if str(request.POST['group9']) == "on":
                    is_working = "Passed"
            except:
                pass

            try:
                if str(request.POST['group3']) == "on":
                    is_sound_working = "Passed"
            except:
                pass

            try:
                if str(request.POST['group5']) == "on":
                    is_display_working = "Passed"
            except:
                pass

            try:
                if str(request.POST['group7']) == "on":
                    is_dedicated_graphics_working = "Passed"
            except:
                pass

            newDevice = Device(name = device_name,
                rating = rating,
                is_working = is_working,
                notes = notes,
                author = author,
                author_email = author_email,
                cpu = device_cpu,
                motherboard = device_motherboard,
                hard_drive = device_hard_drive,
                sound = device_sound,
                is_sound_working = is_sound_working,
                display = device_display_name,
                display_configuration = device_display_config,
                is_display_working = is_display_working,
                graphics_card = device_dedicated_graphics,
                graphics_card_is_working = is_dedicated_graphics_working)
            newDevice.save()

    return HttpResponseRedirect(reverse('repo:index'))

def myTests(request):
    return
