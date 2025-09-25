FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    gstreamer1.0-tools \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    net-tools iproute2 curl bash && \
    rm -rf /var/lib/apt/lists/*

# Copy video into container
COPY video /video

# Video source and RTP port
ENV VIDEO_FILE=/video/test.mp4
ENV RTP_PORT=5004

# Expose RTP port
EXPOSE 5004/udp

# Entry point: play your video file over RTP using bash to expand env variables
CMD ["bash", "-c", "gst-launch-1.0 -v filesrc location=$VIDEO_FILE ! decodebin ! x264enc tune=zerolatency ! rtph264pay config-interval=1 pt=96 ! udpsink host=0.0.0.0 port=$RTP_PORT"]
