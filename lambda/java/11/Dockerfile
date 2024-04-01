FROM scratch



ADD 53166686a8e2cf46e18184fed9c5e2c0342de63fa80e5ba84d52c1f19264e099.tar.xz /
ADD 6cafbaa35bf13546f924978de4947297ec64a0fcef397a24c848d64514a59b7e.tar.xz /
ADD b17bd0a724d5b30abf80b865dd6cb140f74fb48a8aa7beb8e70a4b48fcbff657.tar.xz /
ADD bc17f57d2df1ad6cf6ac3af4de407d9e6a39b2e25027be60239ef740d86e5268.tar.xz /
ADD dcbc2fee61d27bbbe5e7a0d7668b970b83b248e459a635282d41e3f8162fade5.tar.xz /
ADD e8d5b02077128fd417e80f90768bfb58ec7b1d4f3e6704c626fd8015d17ae4c1.tar.xz /
ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
