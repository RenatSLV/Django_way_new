from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

from App1.models import User

from decimal import Decimal

def list_user(request):
    users = User.objects.all()
    return render(request, 'base.html', {'users': users})

def transfer_money(request):
    users = User.objects.all()
    context = {}
    
    if request.method == 'POST':
        sender_id = request.POST.get('sender_id')
        receiver_id = request.POST.get('receiver_id')
        amount = request.POST.get('amount')

        if not sender_id or not receiver_id or not amount:
            context.update({'error': "Заполните все поля"})
        
        try:
            amount = Decimal(amount)
            if amount < 0:
                context.update({'error': "Сумма должна быть положительной"})
        except ValueError:
            context.update({'error': "Некорректная сумма"})
        
        try:
            with transaction.atomic():
                sender = get_object_or_404(User, id=sender_id)
                receiver = get_object_or_404(User, id=receiver_id)

                if sender.balance <= 0:
                    context.update({'error': "Недостаточно средств"})
                
                sender = User.objects.select_for_update().get(id=sender_id)
                receiver = User.objects.select_for_update().get(id=receiver_id)

                sender.balance -= amount
                receiver.balance += amount

                sender.save()
                receiver.save()
            return redirect('list_user')
        
        except Exception as e:
            context.update({'error': f"Ошибка перевода: {str(e)}"})

    context.update({'users': users})
    return render(request, 'transfer.html', context)
