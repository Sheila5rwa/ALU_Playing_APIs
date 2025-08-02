FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        openssh-server sudo iputils-ping ca-certificates && \
    mkdir /run/sshd && \
    if ! id -u ubuntu >/dev/null 2>&1; then \
        useradd --create-home --uid 1000 --shell /bin/bash ubuntu; \
    fi && \
    echo 'ubuntu:pass123' | chpasswd && \
    usermod -aG sudo ubuntu && \
    sed -ri 's/#?PermitRootLogin.*/PermitRootLogin no/'  /etc/ssh/sshd_config && \
    sed -ri 's/#?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN ssh-keygen -A
CMD ["/usr/sbin/sshd","-D"]
