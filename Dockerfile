FROM public.ecr.aws/docker/library/python:3.10-slim-buster
COPY requirements.txt /application/
WORKDIR /application
RUN pip install -r requirements.txt
COPY ./ /application/
ENTRYPOINT [ "./entrypoint.sh" ]
