from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import base64
import cv2 as cv
from skimage.feature import hog
from sklearn.externals import joblib
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(BASE_DIR, "digi_vision")

clf, preproc = joblib.load(
    DIR+'\mnist_clf_svm.pkl')


def get_ict(img):  # returns image, contours and threshold
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray, (7, 7), 0)
    _, thresh = cv.threshold(blur, 100, 255, cv.THRESH_BINARY_INV)
    _, contour, hier = cv.findContours(
        thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    return img, contour, thresh


@csrf_exempt
def DigiView(request, *args, **kwargs):
    if request.method == "GET":
        print(DIR+'\mnist_clf_svm.pkl')
        context = {
            "title": "Snapper",
        }
        return render(request, "index.html", context)

    elif request.method == "POST":

        b = request.POST.get("abc")
        encoded_data = b.split(',')[1]
        imgdata = base64.b64decode(encoded_data)
        filename = 'some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)

        img = cv.imread(BASE_DIR+'\some_image.jpg')

        # Comment from here for single digit

        result = ''
        img, contours, threshold = get_ict(img)
        if len(contours) > 0:
            contour = max(contours, key=cv.contourArea)
            if cv.contourArea(contour) > 1500 and cv.contourArea(contour) < 5000:
                x, y, w, h = cv.boundingRect(contour)

                newimg = threshold[y:y + h, x:x + w]

                newimg = cv.resize(newimg, (28, 28))
                newimg = np.array(newimg)

                hog_ft = hog(newimg, orientations=9, pixels_per_cell=(14, 14),
                             cells_per_block=(1, 1), block_norm='L2')

                hog_ft = preproc.transform(np.array([hog_ft], 'float64'))
                result = clf.predict(hog_ft)

        # constructing bounding rectangles
        x, y, w, h = 0, 0, 300, 300
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(img, "svm : " + str(result), (10, 320),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Stays commented to remove single digit

        # FOR MULTI-DIGIT

        # result = ''

        # if len(contours) > 0:
        #     for ctr in contours:
        #         if cv.contourArea(ctr) > 1000 and cv.contourArea(ctr) < 5000:
        #             x, y, w, h = cv.boundingRect(ctr)

        #             ctrimage = threshold[y:y+h, x:x+w]

        #             ctrimage = np.array(cv.resize(ctrimage, (28, 28)))

        #             hog_features = hog(ctrimage, orientations=9, pixels_per_cell=(
        #                 14, 14), cells_per_block=(1, 1), block_norm='L2')
        #             hog_features = preproc.transform(
        #                 np.array([hog_features], 'float64'))

        #             result = clf.predict(hog_features)

        #             cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        #             cv.putText(
        #                 img, str(int(result[0])), (x, y), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # REMAINS COMMENTED TILL HERE FOR MULTI-DIGIT RECOGNITION

        cv.imshow("IMAGE", img)
        cv.imshow("Thresh", threshold)
        cv.waitKey(0)
        context = {
            "img": request.body,
        }
        return HttpResponse(b)
