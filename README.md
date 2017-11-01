# MedicApp

A Django web application designed to help medical students across the globe prepare for their exams without the need to assemble hundreds of pages of notes and flash cards.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation
#### Prerequisites
This project has only been tested on macOS High Sierra and Ubuntu 16.04 operating systems so with that in mind please be aware that the project may not run as intended on any other operating system. 

All of the commands used to run this project are carried out on a _bash_ shell. 

To set up the virtual environment I used [virtualenv](https://virtualenv.pypa.io) and installed it just outside of the repository for this project.  To initiate the virtual environment from inside your git repo, run the following command:

```
source ../env/bin/activate
```
Once you have run this command, your _bash_ prompt should look similar to this:

```
(envmedicapp) Your-Macbook-Pro:medicapp yourname$
```

You will find all requirements for this project in [requirements.txt](medicapp/requirements.txt) and once you have set up and initiated your virtual environment, you can run the following command to install all of the requirements for this project:

```
pip install -r requirements.txt
```

#### Test Server
Once you have set up all of the prerequisites and have your virtual environment initiated, ensure that you are in the directory that contains the file [manage.py](medicapp/manage.py) and run the following command to start running the test server on your local machine:

```
python manage.py runserver
```
By default, the server will set up on [http://localhost:8000/](http://localhost:8000/). Ensure that you append the name of the app to this _url_ to access the web application. To land on the home page you should enter the link in your browser as [http://localhost:8000/quiz](http://localhost:8000/quiz) and you can start playing around with the application and reviewing any changes you make in your fork.

## Running the tests

Automated tests are currently being generated for this project.


## Deployment

This application has been deployed on Amazon Web Services using Elastic Beanstalk, however there are other options out there including Heroku which I also hold in very high regard.

## Built With

* [Python 2.7](https://www.python.org/) - Python 2
* [Django 1.11](https://www.djangoproject.com/) - Web Framework used
* [Bootstrap](http://getbootstrap.com/) - Bootstrap provided some front end glue to the project.


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Tom Elliott** - *Project lead* - [tomxelliott](https://www.github.com/tomxelliott)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to the creators and maintainers of both Django & Python for excellent documentation that made creating this project far more manageable. 
* Thanks to my sister for the inspiration behind this project.
