FROM python:3.11-rc-bullseye AS builder

# TRICK TO
#FROM python:3.11-rc-alpine3.16 AS builder
#ARG PYTHON_VERSION=3.7.0-alpine3.8
#FROM python:${PYTHON_VERSION} as builder

ARG REQS=base
ARG VENV=/usr/local/gval_env
ARG PROJ=/gval

COPY requirements/$REQS.txt /tmp

RUN apt update --fix-missing && \
    DEBIAN_FRONTEND=noninteractive \
        apt install -qy \
            gdal-bin=3.2.2+dfsg-2+deb11u1 \
            libgdal-dev=3.2.2+dfsg-2+deb11u1 \
            python3-gdal=3.2.2+dfsg-2+deb11u1 && \
    apt auto-remove -y && \
    python3 -m venv $VENV && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \
    $VENV/bin/pip install -r /tmp/$REQS.txt

RUN pip install -r /tmp/$REQS.txt && \
    rm -rf /tmp/*

###############################################################################################
# development stage
###############################################################################################
FROM python:3.11-rc-bullseye AS development

## SETTING ENV VARIABLES ##
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
# ensures stdout stderr are sent straight to terminal
ENV PYTHONUNBUFFERED=TRUE 

## Virtual and project directories ##
ARG VENV=$PROJ_env
ARG PROJ=$PROJ

# Label docker image
LABEL version="" \
      maintaner="Fernando Aristizabal" \
      release-date=""

# RETRIEVE BUILT DEPENDENCIES
COPY --from=builder $VENV $VENV

# set path to virtual env so that future python commands use is it
ENV PATH="$VENV:$PATH"

## ADDING USER GROUP ##
ARG UID=1001
ARG UNAME=user
RUN useradd -Ums /bin/bash -u $UID $UNAME
USER $UNAME
WORKDIR /home/$UNAME

###############################################################################################
# runtime stage
###############################################################################################
#FROM development AS rutime

#COPY . $PROJ
#WORKDIR $PROJ
#RUN $VENV/bin/pip install $PROJ

#CMD ["./.venv/bin/python", "-m", "$PROJ/main.py"]
