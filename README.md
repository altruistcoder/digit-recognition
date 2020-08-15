# DIGIT RECOGNIZER

Digit Recognizer is a simple Django application which can be used to recognize handwritten digits.


* You can see the code for training the model in this [notebook](https://github.com/altruistcoder/digit-recognition/blob/master/Digit_Recognition_Training.ipynb).

* This repository also consists of already trained weights for this model which you can find [here](https://github.com/altruistcoder/digit-recognition/tree/master/src/digit_app/my_mnist_model).

## Instructions

1. Get the source code on your pc via git.

```
  git clone https://github.com/altruistcoder/digit-recognition
```
2. Create a virtual environment to install the required dependencies of the application.

```
  virtualenv venv
```

3. Activate the virtual environment (You have to activate it every time you are working on project).

```
  For mac users:

    source venv/bin/activate  

  For windows users:

    .\venv\Scripts\activate

  For Linux users:

    source venv/bin/activate
```

4. Now, install python dependencies.

```
  pip install -r requirements.txt
```

5. Now, navigate to the **src** directory (containing the **manage.py** file).

6. Run following command:

```
  python manage.py migrate
  python manage.py runserver
```
7. Digit Recognizer is ready for use. You can run it at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
