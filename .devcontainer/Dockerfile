FROM python:3.6.9-slim-buster

ENV DEBIAN_FRONTEND noninteractive 
 
RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \ 
  git \
  vim \
  libqt4-network \
  libgomp1 \
  zlib1g \
  libstdc++6 \
  sudo \
  build-essential \
  libcurl4-openssl-dev

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN echo "deb http://http.debian.net/debian buster main" > /etc/apt/sources.list.d/debian-unstable.list

RUN apt-get install -y --no-install-recommends \
				r-base \
				r-recommended \
				r-cran-devtools \
				libopenblas-base

#setup R configs
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('tidyverse')"
RUN Rscript -e "install.packages('dplyr')"
RUN Rscript -e "install.packages('tibble')"
RUN Rscript -e "install.packages('tidyr')"

RUN Rscript -e "install.packages('ggplot2')"
RUN Rscript -e "install.packages('graphics')"
RUN Rscript -e "install.packages('cowplot')"
RUN Rscript -e "install.packages('ggrepel')"
RUN Rscript -e "install.packages('lubridate')"
RUN Rscript -e "install.packages('chron')"
RUN Rscript -e "install.packages('scales')"
RUN Rscript -e "install.packages('grid')"
RUN Rscript -e "install.packages('gridExtra')"

RUN Rscript -e "install.packages('qcc')"
RUN Rscript -e "install.packages('ggQC')"
RUN Rscript -e "install.packages('MSQC')"
RUN Rscript -e "install.packages('IQCC')"
RUN Rscript -e "install.packages('yhatr')"
RUN Rscript -e "install.packages('MSstats')"
RUN Rscript -e "install.packages('pracma')"

RUN Rscript -e "install.packages('anomalize')"
RUN Rscript -e "install.packages('DMwR')"
RUN Rscript -e "install.packages('outliers')"

RUN apt-get install -y --no-install-recommends \
    gfortran \
    pandoc
RUN Rscript -e "install.packages('plotly')"
RUN Rscript -e "install.packages('htmlwidgets')"

#RUN Rscript -e "install.packages('devtools')"
ENV R_LIBS_USER ~/R/x86_64-pc-linux-gnu/3.5
ENV R_LIBS_SITE /usr/local/lib/R/site-library:/usr/lib/R/site-library:/usr/lib/R/library
RUN Rscript -e "install.packages('Rcpp')"
RUN Rscript -e "library('devtools'); install_github('twitter/AnomalyDetection')"

#RUN echo 'install.packages(c("ggplot2", "plyr", "reshape2", "RColorBrewer", "scales", "FactoMineR", \
#"Hmisc", "cowplot", "shiny"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
#&& Rscript /tmp/packages.R

RUN pip install pip --upgrade
RUN pip install setuptools --upgrade
RUN pip install numpy mypy jupyter rpy2 flask pytest
RUN pip install --force-reinstall 'pytest<=5.0.1'
RUN pip install -U git+https://github.com/bigbio/mzqc-pylib.git#egg=mzqc-pylib
RUN pip install pronto biopython pandas requests plotly-express toposort click
RUN pip install pyopenms==2.5.* 

#RUN pip install -e .  # devcontainer.json: "postCreateCommand": "pip install -e ."

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME 
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
    
#USER 1000  # "runArgs": ["-u", "1000"]
#extrawurst fuer vscode
#RUN mkdir -p /root