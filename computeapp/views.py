import subprocess
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    return render(request, 'base.html')


def run_code(code):
    try:
        code = 'print(' + code + ')'
        output = subprocess.check_output(['python', '-c', code], universal_newlines=True, stderr=subprocess.STDOUT,
                                         timeout=30)
    except subprocess.CalledProcessError as e:
        output = '公式格式错误'
    return output


@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    code = code.replace('÷', '/').replace('×', '*')
    result = run_code(code)
    return JsonResponse(data={'result': result})