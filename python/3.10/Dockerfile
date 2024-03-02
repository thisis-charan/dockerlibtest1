FROM scratch

LABEL maintainer="Cloud Platform Engineering <saipcharan32@gmail.com>"
ARG image_name="python3.10"
ARG image_tag
LABEL cpe_base_image=${image_name}:${image_tag} creator="CPE" base_image_support="saipcharan32@gmail.com"

ADD 03c680b33a6fca213db06ee5f64afa356e37d0d14fd35703a15d488c273f25ba.tar.xz /
ADD 1c1fee2ab693751c3b462976a58eb7e0d12585b64254213beb873ab882607343.tar.xz /
ADD 60b0b5573909e77c93eb984a14ba1602229f8fef69409cf9bccc0da3f0e9f792.tar.xz /
ADD 616f3701720eb335d2753805c6423309bc07500dfd2ceff637fdf6b6f8d07cb6.tar.xz /
ADD a8f0d3464a18695926b76cdbda6b9626c3fb95a4768dff528d558bf5c144b97d.tar.xz /
ADD f47ba085d0f827e942340d8b2bbc5af468a78d9a155c31770046ce5855b9ecbd.tar.xz /

ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]