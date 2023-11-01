FROM python:3.12-bullseye

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    unzip \
    git \
    make \
    lldb \
    sudo \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash developer && \
    usermod -aG sudo developer && \
    chown developer:developer /home/developer && \
    echo 'developer:developer' | chpasswd && \
    echo 'developer ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN sudo -u developer sh -c "curl -sSL https://install.python-poetry.org | python3 -"