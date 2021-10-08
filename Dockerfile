FROM python:3

# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal
# without being first buffered and that you can see the output of your application in real time
ENV PYTHONUNBUFFERED 1

# Copy needed stuff to container, install requirements and set the work dir for other commands
RUN mkdir /usr/dependency_manager
COPY ./requirements.txt /usr/dependency_manager/requirements.txt
RUN pip install -r /usr/dependency_manager/requirements.txt

RUN mkdir /usr/dependency_manager/app
COPY ./app /usr/dependency_manager/app
WORKDIR /usr/dependency_manager/app

RUN mkdir /usr/dependency_manager/data
COPY ./data /usr/dependency_manager/data

RUN mkdir /usr/dependency_manager/tests
COPY ./tests /usr/dependency_manager/tests
