FROM scratch



ADD 438162687605f966e5dc30393fab72659dd57564a97f3b4c68c0bb4c10957f94.tar.xz /
ADD 45919fb6227ce1c0e3cbb073f7e687728004c0fe93b21c997e11e64a165b1c0c.tar.xz /
ADD 7b16d50e37422a42598890d186ff9af52560e873b421d1c9edccd0721388aae0.tar.xz /
ADD 9563fc8f130858469acc18b49040216ca84a2b5b30b437d7777f24a9c7bf32fd.tar.xz /
ADD d6eb57203756f5a2a6b90b855347c5a8781778cee59c30a7250e87ec6d14a8c6.tar.xz /
ADD da16d563d428edcb8f158f4eabc9c5377dffa8a6a3f6d5e2285c2c7e032d9348.tar.xz /
ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
