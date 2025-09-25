# Use the same base image
FROM sbarrachina/open5gs-base:v2.4.0

WORKDIR /

ENV DEBIAN_FRONTEND=noninteractive

# Clone Open5GS v2.7.5 and build
RUN git clone https://github.com/open5gs/open5gs --branch v2.7.5 && \
    cd open5gs && \
    meson build --prefix=$(pwd)/install/ && \
    ninja -C build && \
    ninja -C build install && \
    cd ..

# Keep the container running
CMD ["sh", "-c", "tail -f /dev/null"]

