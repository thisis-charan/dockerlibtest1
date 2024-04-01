FROM scratch

ADD 0fe4077db319f96a395e49a9708c6bd3052d805c9a39054d824e0d2ce01039f3.tar.xz /
ADD 3bd71806f8aea66ec0fb849c413e6923d6c69c7ee38403ce1dd42281351e0857.tar.xz /
ADD 53166686a8e2cf46e18184fed9c5e2c0342de63fa80e5ba84d52c1f19264e099.tar.xz /
ADD b17bd0a724d5b30abf80b865dd6cb140f74fb48a8aa7beb8e70a4b48fcbff657.tar.xz /
ADD bc17f57d2df1ad6cf6ac3af4de407d9e6a39b2e25027be60239ef740d86e5268.tar.xz /
ADD dcbc2fee61d27bbbe5e7a0d7668b970b83b248e459a635282d41e3f8162fade5.tar.xz /

ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
