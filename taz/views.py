from django.shortcuts import render


# Create your views here.


def get_index(request):
    return render(request, 'index.html')


def get_menu(request):
    return render(request, 'menu.html')


def get_voucher(request):
    return render(request, 'voucher.html')


def get_reservation(request):
    return render(request, 'reservation.html')


def get_contact(request):
    return render(request, 'contacts.html')


def get_opening(request):
    return render(request, 'opening.html')


def get_location(request):
    return render(request, 'location.html')


def get_breakfast(request):
    return render(request, 'Breakfast.html')


def get_lunch(request):
    return render(request, 'Lunch.html')


def get_dinner(request):
    return render(request, 'dinner.html')


def get_dessert(request):
    return render(request, 'dessert.html')


def get_base(request):
    return render(request, 'base.html')
