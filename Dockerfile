# Use an official Python runtime as a parent image
FROM python:3.8-slim
ENV PROJECT_DIR=/home/benp
WORKDIR $PROJECT_DIR
RUN yes root | passwd root
COPY "./work" ${PROJECT_DIR}

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
