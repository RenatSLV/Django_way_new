from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import signing

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        # Сохраняем в сессию и куки
        request.session['name'] = name
        response = redirect('result')
        response.set_cookie('username', name, max_age=3600)

        # Уведомление
        messages.success(request, f"Имя '{name}' успешно сохранено!")

        # Сохраняем подписанные данные в сессию
        signed_name = signing.dumps(name)
        request.session['signed_name'] = signed_name

        return response

    return render(request, 'main/index.html')


def result(request):
    name = request.session.get('name')
    signed_name = request.session.get('signed_name')

    try:
        verified_name = signing.loads(signed_name)
    except signing.BadSignature:
        verified_name = "Неверная подпись"

    cookie_name = request.COOKIES.get('username', 'Нет в cookies')

    return render(request, 'main/result.html', {
        'name': name,
        'cookie_name': cookie_name,
        'verified_name': verified_name,
    })
