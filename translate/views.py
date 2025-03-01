from django.shortcuts import render
from deep_translator import GoogleTranslator
# Create your views here.


def translate(request):
    translated_text = ''

    if request.method == 'POST':
        text = request.POST.get('text')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')

        if text and source_language and target_language:
            translated_text = GoogleTranslator(source = source_language, target = target_language).translate(text)

    return render(request, 'translate.html', {'translated_text' : translated_text})