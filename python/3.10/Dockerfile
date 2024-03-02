FROM scratch

LABEL maintainer="Cloud Platform Engineering <saipcharan32@gmail.com>"
ARG image_name="python3.10"
ARG image_tag
LABEL cpe_base_image=${image_name}:${image_tag} creator="CPE" base_image_support="saipcharan32@gmail.com"

ADD 1038ce783a65e4455d58ba51f9bbd77bb3c04bf891530cc8931f5d5f0452acb3.tar.xz /
ADD 3c9c6d0addbdcc6a2ad1225166070be1fabab4a5ce9c613e6245db862cbccf6c.tar.xz /
ADD 4f87b6fbe2ca0329143f9a49c6707a38b6f654179bcc92fb9f45ed8fe5a1270f.tar.xz /
ADD 616f3701720eb335d2753805c6423309bc07500dfd2ceff637fdf6b6f8d07cb6.tar.xz /
ADD d5b589e092c7c8ef1b010d6c0dae42ac81907ec28253856e02598af0020df09f.tar.xz /
ADD f762784e95915b061db153ad2700e5a711c4718aefb619bd00c26f18807de931.tar.xz /

ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]