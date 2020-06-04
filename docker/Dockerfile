FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHON_VERSION 3.7.1
ENV PYTHON_ROOT $HOME/local/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$PATH
ENV PYENV_ROOT $HOME/.pyenv

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
  build-essential \
  curl \
  git \
  libbz2-dev \
  libffi-dev \
  liblzma-dev \
  libncurses5-dev \
  libncursesw5-dev \
  libreadline-dev \
  libsqlite3-dev \
  libssl-dev \
  llvm \
  make \
  python-dev \
  python-pip \
  tk-dev \
  vim \
  wget \
  xz-utils \
  zlib1g-dev

# Install Python
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT \
  && $PYENV_ROOT/plugins/python-build/install.sh \
  && /usr/local/bin/python-build -v $PYTHON_VERSION $PYTHON_ROOT \
  && rm -rf $PYENV_ROOT

# Install pytorch
# RUN git clone --branch master --recursive https://github.com/pytorch/pytorch.git
# WORKDIR /pytorch
# RUN git submodule update --init --recursive

WORKDIR /mmsr
COPY codes/requirements.txt /mmsr/

# Upgrade pip
RUN pip install --upgrade pip
RUN pip install -r /mmsr/requirements.txt

COPY . /mmsr
