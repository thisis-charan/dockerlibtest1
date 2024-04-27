FROM scratch



ADD 45919fb6227ce1c0e3cbb073f7e687728004c0fe93b21c997e11e64a165b1c0c.tar.xz /
ADD 4e7bb75c3513c5ba80250be34a1a59a6baca3385866e643e5700720bef3aa71d.tar.xz /
ADD 9ef4d1dd17674e13dd69fec8d9b660dc87764b7a08b34bcdb2313fc0a701f1e6.tar.xz /
ADD ad7dd3ee42584ff86b3a077c5c4b5042f007bf5758faf9d8e377892209783973.tar.xz /
ADD b489651ea95fa3e7b8e447fc46c5cf911d1fbeaaefb7b9f6eb30f1ed901fd0c8.tar.xz /
ADD b6dc7f8ef4ce741d50f00c9f28e8571f6f00baf102c29c625d6bf0b774503fa8.tar.xz /
ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
