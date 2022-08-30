From python:3.11-rc-bullseye

RUN useradd -ms /bin/bash user
USER user

WORKDIR /home/user

COPY requirments.txt .
RUN pip3 install -r requirements.txt && rm requirements.txt
