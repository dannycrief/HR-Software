import json

from django.http import HttpResponse

from .models import DemoUserTest


def checkTheSame(request):
    if request.method == 'POST':
        currentTestID = request.body.decode('utf8').replace("'", '"')
        data = json.loads(currentTestID)
        if DemoUserTest.objects.get(id=data['id']):
            currentUserTestID = DemoUserTest.objects.get(id=data['id'])
            currentUserTestID.demoUserEmail = data['demoUserEmail']
            currentUserTestID.demoGrade = data['demoGrade']
            return HttpResponse(currentUserTestID.save())
