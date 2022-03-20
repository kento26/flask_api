FROM python:3.8.2

ARG project_directory
WORKDIR $project_directory

RUN pip install flask
RUN pip install pykakasi