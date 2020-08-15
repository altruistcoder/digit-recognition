from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .model_prediction import digit_prediction
import numpy as np
import cv2 as cv


@csrf_exempt
def DigitAppHomeView(request, *args, **kwargs):
    if request.method == "GET":
        context = {
            "title": "Digit Recognizer"
        }
        return render(request, "digit_app/home.html", context)

    elif request.method == "POST":
        image = request.FILES.get('numImg')
        img = cv.imdecode(np.fromstring(image.read(), np.uint8), 1)
        prediction = digit_prediction(img)
        context = {
            "prediction": prediction
        }
        return render(request, 'digit_app/success.html', context)
