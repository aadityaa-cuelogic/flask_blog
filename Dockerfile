# Use an official Python runtime as a parent image
FROM python:2.7-slim

MAINTAINER Aaditya Agrawal

#RUN sudo apt-get update && sudo apt-get install postgresql postgresql-contrib

# Create Directory
RUN mkdir /flask_blog

# Set the working directory to /flask_blog
WORKDIR /flask_blog

# Copy the current directory contents into the container at /app
ADD . /flask_blog


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT  sleep 2m &&\
			rm -rf migrations &&\
			python manage.py db init &&\
			python manage.py db migrate &&\
			python manage.py db upgrade &&\
			python run.py --host 0.0.0.0


# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]

