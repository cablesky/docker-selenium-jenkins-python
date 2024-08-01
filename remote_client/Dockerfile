FROM ubuntu:latest

# SSH install
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y openssh-server

RUN useradd remote_user && \
    echo "remote_user:1234" | chpasswd && \
    mkdir /home/remote_user/.ssh -p && \
    chmod 700 /home/remote_user/.ssh && \
    chown remote_user:remote_user /home/remote_user/.ssh && \    
    mkdir -p -m0755 /var/run/sshd

RUN chown remote_user:remote_user -R /home/remote_user

# Java 17 install
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk ant ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f && \
    rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk17-installer

# Fix certificate issues, found as of 
# https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/983302
RUN apt-get update && \
    apt-get install -y ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer;

# Install python modules
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt install python3-pip -y
RUN mkdir -p ~/.config/pip && echo "[global]\nbreak-system-packages = true" > ~/.config/pip/pip.conf
RUN pip3 --version
RUN pip3 install selenium
RUN pip3 install -U pytest

RUN mkdir /home/remote_user/selenium
RUN chmod 777 /home/remote_user/selenium
RUN chown remote_user:remote_user -R /home/remote_user/selenium


CMD /usr/sbin/sshd -D
