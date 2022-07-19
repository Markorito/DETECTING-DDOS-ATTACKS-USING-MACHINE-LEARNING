# DETECTING DDOS ATTACKS USING MACHINE LEARNING
## BACKGROUND
 Final year project creating a simple classifier to detect DDOS attacks
This project is a simple project made using Scikit-Learn models deployed via Django and accessed via the REST API
It uses a combination of random forest classifiers and extra trees classifiers to classify whether networking packets are benign normal packets or a part of a botnet designed to carry out a DDOS attack


## USAGE
To run the code, you need Django installed in your machine as well Scikit-Learn.
Navigate to the backend folder then the server folder with your terminal of choice, then run the following code


*python manage.py runserver*


Voila, you have the server running. The server should have some tests running. In order to make predictions you need to parse your dataset in json format. 
There are a few folders in the code, like the research folder which contains the model objects used for prediction and and the Untitled notebook used to convert a dataset into json.
There's the ab test jupyter notebook used to run ab tests.


## FURTHER IMPROVEMENTS
This could be implemented in a production server with some further improvements and building out some of the code might be outdated due to the versions of the packages used.
