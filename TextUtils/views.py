from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')


def text(request):
    final = ''
    text1 = request.GET.get('text1', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover' 'off')
    numberremover = request.GET.get('numberremover', 'off')
    totitle = request.GET.get('totitle', 'off')
    counter = request.GET.get('counter', 'off')
    custom = request.GET.get('custom')
    find = request.GET.get('find')
    replace = request.GET.get('replace')
    if removepunc == "on":
        punctuations = '''!()-[]|{};:'"\,<>./?@#$%^&*_~'''
        for char in text1:
            if char not in punctuations:
                final = final + char
        context = {'text1': text1, 'final': final}
        return render(request, 'textutils.html', context)

    if fullcaps == "on":
        for char in text1:
            final = final + char.upper()
        params = {'text1': text1, 'final': final}
        return render(request, 'textutils.html', params)

    if newlineremover == "on":
        for char in text1:
            if char != "\n":
                final = final + char
        params = {'text1': text1, 'final': final}
        return render(request, 'textutils.html', params)

    if extraspaceremover == "on":
        final = ""
        for index, char in enumerate(text1):
            if not (text1[index] == " " and text1[index + 1] == " "):
                final = final + char
        context = {'text1': text1, 'final': final}
        return render(request, 'textutils.html', context)

    if numberremover == "on":
        numbers = '0123456789'
        for num in text1:
            if num not in numbers:
                final = final + num
        context = {'text1': text1, 'final': final}
        return render(request, 'textutils.html', context)

    if counter == 'on':
        lst = []
        for char in text1:
            lst.append(char)
            final = len(lst)
        context = {'text1': text1, 'count': final}
        return render(request, 'textutils.html', context)

    if custom:
        for char in text1:
            if char not in custom:
                final = final + char
        context = {'final': final, 'text1': text1}
        return render(request, 'textutils.html', context)

    if find and replace:
        final=text1.replace(find, replace)
        context = {'final': final, 'text1': text1}
        return render(request, 'textutils.html', context)

    if totitle == 'on':
        final = text1.title()
        context = {'final': final}
        return render(request, 'textutils.html', context)

    else:
        return HttpResponse("ERROR")
