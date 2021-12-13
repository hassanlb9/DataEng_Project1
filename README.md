# DataEng_Project1 - Web application Sentiment Analysis -

This project is for the course "Data Engineering II”, made by:

* Alain NGOMEDJ
* Emeric BERTIN
* BACHACHA Hassan

## Introduction:

The goal of this project is to combine all the skills collected throughout the course thus far, and provide a solid example of real-life application development in a DevOps environment.

The application we've made is a sentiment analysis application, which, given a piece of text, should be able to reply with its sentiment as being positive, negative, or neutral.

* The text language used must be English
* The application should have a web interface with an input form and a submit button, where users can input their sentences, and hit submit, and the sentiment of their sentence will be presented.
* The accuracy of the sentiment analyzer should be above 80%
* The application must be easily deployable

## Project Organization

* __static__ : the root to the css project
* __templates__ : The html code
* __Dockerfile__ : The text document that contains the instructions to assemble a Docker image
* __main.py__: A py file used to deploy the model using flask 
* __requirements.txt__: This file is used by pip to install required python packages
* __ReadMe.md__ : The file you are currently reading

## Prerequisites

This app is built using Python 3.6.6

# Start the project

TTo install the Python packages for the project, clone the repository and run:

* docker image build -t "img_name" .
* docker image ls
* docker run -p 8000:5000 -d "img_name"

#### Test the app
* Open Browser: http://localhost:8000.
* 
