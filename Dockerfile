FROM hashicorp/terraform:latest as terraform

FROM python:3.9.13-slim
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
RUN apt-get install -y vim less && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install svn requests

# install aws
RUN apt-get install -y curl unzip groff-base && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip

# install terraform
COPY --from=terraform /bin/terraform /bin/terraform

WORKDIR /app
