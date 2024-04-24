FROM scratch




ADD 1670fe193e3251e2a7230ad4cba97e559ebede766694e45de817d19b0afa18c7.tar.xz /
ADD 45919fb6227ce1c0e3cbb073f7e687728004c0fe93b21c997e11e64a165b1c0c.tar.xz /
ADD a6fb32a81911e96bce471ac5fbe0fbc082f132a31078ba2fd03fbd010314a1e5.tar.xz /
ADD a96569de874eca5a15ccf6f6e53210f108ce49461bd1209a59a2c6bf8f034399.tar.xz /
ADD ac5353101b82489f5e11c48c309e586b6947ece7662efb06f55d80f05eff4ea4.tar.xz /
ADD bb1e9403ade1361458a22a82641bad20151e603443e2d2863550d3ad5af357eb.tar.xz /
ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
