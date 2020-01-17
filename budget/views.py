from django.shortcuts import render
from django.http import HttpResponse
from .models import AddincomeModel,AddexpenseModel
import datetime
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.


def add_income(request):
    if request.method == 'POST':
        a = AddincomeModel()
        date = request.POST.get('date')
        datecon = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
        a.date = datecon
        a.text = request.POST.get('text')
        a.amount = request.POST.get('amount')
        a.save()
        return render(request, 'budget/day.html')

    else:
        return render(request, 'budget/addincome.html')

def add_expense(request):
    if request.method == 'POST':
        b = AddexpenseModel()
        date = request.POST.get('date')
        datecon = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
        b.date = datecon
        b.text = request.POST.get('text')
        b.amount = request.POST.get('amount')
        b.save()
        return render(request, 'budget/day.html')

    else:
        return render(request, 'budget/addexpense.html')


def day_view(request):
    ctx={}
    incomeview=[]
    expenseview=[]
    income = 0
    expense = 0
    savings = 0
    url_parameter = request.GET.get("viewdate")
    if url_parameter:
        incomeview = AddincomeModel.objects.filter(date__icontains=url_parameter)
        expenseview = AddexpenseModel.objects.filter(date__icontains=url_parameter)
        for i in incomeview:
            income += i.amount
        for i in expenseview:
            expense += i.amount
        savings=income-expense
    ctx["incomeview"] = incomeview
    ctx["expenseview"] = expenseview

    if request.is_ajax():
        html = render_to_string(
            template_name = "budget/viewday-results.html", context={"incomeview":incomeview, "expenseview":expenseview, "income":income, "expense":expense, "savings":savings}
        )

        data_dict = {"html_from_view":html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'budget/day.html', context=ctx)


def month_view(request):
    ctx={}
    incomeview=[]
    expenseview=[]
    income = 0
    expense = 0
    savings = 0
    url_parameter = request.GET.get('viewdate')
    if url_parameter:
        incomeview = AddincomeModel.objects.filter(date__icontains=url_parameter)
        expenseview = AddexpenseModel.objects.filter(date__icontains=url_parameter)
        for i in incomeview:
            income += i.amount
        for i in expenseview:
            expense += i.amount
        savings=income-expense
    ctx["incomeview"] = incomeview
    ctx["expenseview"] = expenseview

    if request.is_ajax():
        html = render_to_string(
            template_name = "budget/viewday-results.html", context={"incomeview":incomeview, "expenseview":expenseview, "income":income, "expense":expense, "savings":savings}
        )

        data_dict = {"html_from_view":html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'budget/month.html', context=ctx)


def year_view(request):
    ctx={}
    incomeview=[]
    expenseview=[]
    income = 0
    expense = 0
    savings = 0
    url_parameter = request.GET.get("viewdate")
    if url_parameter:
        incomeview = AddincomeModel.objects.filter(date__icontains=url_parameter)
        expenseview = AddexpenseModel.objects.filter(date__icontains=url_parameter)
        for i in incomeview:
            income += i.amount
        for i in expenseview:
            expense += i.amount
        savings=income-expense
    ctx["incomeview"] = incomeview
    ctx["expenseview"] = expenseview

    if request.is_ajax():
        html = render_to_string(
            template_name = "budget/viewday-results.html", context={"incomeview":incomeview, "expenseview":expenseview, "income":income, "expense":expense, "savings":savings}
        )

        data_dict = {"html_from_view":html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'budget/year.html', context=ctx)
