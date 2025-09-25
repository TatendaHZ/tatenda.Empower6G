FROM sbarrachina/open5gs-base:v2.4.0

WORKDIR /

ENV DEBIAN_FRONTEND noninteractive

RUN git clone https://github.com/open5gs/open5gs --branch v2.4.0 && \
 cd open5gs && meson build --prefix=`pwd`/install/ && ninja -C build && \
 cd build && ninja install && \
 cd ..

 CMD ["sh", "-c", "tail -f /dev/null"]