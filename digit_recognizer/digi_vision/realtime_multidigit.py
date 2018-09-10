import cv2 as cv
from skimage.feature import hog
from sklearn.externals import joblib
import numpy as np

clf, preproc = joblib.load('E:\django\project\src\digi_vision\mnist_clf_svm.pkl')

def get_ict(img): # returns image, contours and threshold
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (7,7), 0)
    _, thresh = cv.threshold(blur, 120, 255, cv.THRESH_BINARY_INV)
    _, contour, hier = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    return img, contour, thresh


def pr(image):
    return image


def maining():
    capture = cv.VideoCapture(0)

    while(capture.isOpened()):
        _, img = capture.read()

        img, contours, threshold_img = get_ict(img)

        result = ''

        if len(contours)>0:
            for ctr in contours:
                if cv.contourArea(ctr)>1000 and cv.contourArea(ctr)<5000:
                    x,y,w,h = cv.boundingRect(ctr)

                    ctrimage = threshold_img[y:y+h, x:x+w]

                    ctrimage = np.array(cv.resize(ctrimage, (28, 28)))

                    hog_features = hog(ctrimage, orientations=9, pixels_per_cell=(14,14), cells_per_block=(1,1), block_norm='L2')
                    hog_features = preproc.transform(np.array([hog_features], 'float64'))

                    result = clf.predict(hog_features)

                    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
                    cv.putText(img, str(int(result[0])), (x, y), cv.FONT_HERSHEY_PLAIN, 3, (255, 0,0), 3)
        
        cv.imshow('contours', threshold_img)
        cv.imshow('Detection', img)
        k = cv.waitKey(20)
        if k == 27:
            break


# maining()
