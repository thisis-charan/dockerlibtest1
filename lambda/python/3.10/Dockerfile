FROM scratch



ADD 3e32e7f29fea1da8d3be54632c3435c91e7ebe8f7fb412db6dd0602e107ae12d.tar.xz /
ADD 45919fb6227ce1c0e3cbb073f7e687728004c0fe93b21c997e11e64a165b1c0c.tar.xz /
ADD a0e86a4a44c5a20d4468cd73c0fdf2b9f438b7ab058ff9791c7a6275cc3656a5.tar.xz /
ADD a452b7e143737d18e9ca0d051b59a28b7627ffe72660b745ccf0e6d710d342bd.tar.xz /
ADD de0401296e0df7509809af440992adc72e630cecffc29598f073bc36a02b2ea3.tar.xz /
ADD faa96d0f21ab7d9d4ae236b77519316927956cbd282261788953b54a7af5eebf.tar.xz /
ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
