# Stage 1: Prepare JAR and module dependencies
FROM amazoncorretto:17-alpine AS corretto-deps

# Copy the built JAR
COPY ./api/target/*.jar /app/app.jar

# Unzip and analyze modules
RUN unzip /app/app.jar -d temp && \
    jdeps \
      --print-module-deps \
      --ignore-missing-deps \
      --recursive \
      --multi-release 17 \
      --class-path "./temp/BOOT-INF/lib/*" \
      --module-path "./temp/BOOT-INF/lib/*" \
      /app/app.jar > /modules.txt

# Stage 2: Build a custom JRE using jlink
FROM amazoncorretto:17-alpine AS corretto-jdk

COPY --from=corretto-deps /modules.txt /modules.txt

# hadolint ignore=DL3018,SC2046
RUN apk add --no-cache binutils && \
    jlink \
      --verbose \
      --add-modules "$(cat /modules.txt),jdk.crypto.ec,jdk.crypto.cryptoki" \
      --strip-debug \
      --no-man-pages \
      --no-header-files \
      --compress=2 \
      --output /jre

# Stage 3: Final minimal image with JRE + zip/unzip
# hadolint ignore=DL3007
FROM alpine:3.20.3

# Set up custom JRE
ENV JAVA_HOME=/jre
ENV PATH="${JAVA_HOME}/bin:${PATH}"
COPY --from=corretto-jdk /jre $JAVA_HOME

# Install zip/unzip so JAR can be updated inside container
RUN apk add --no-cache zip unzip bash

# Expose port
EXPOSE 8008

# Copy the JAR and the external application.yml
COPY --from=corretto-deps /app/app.jar /app/app.jar
COPY ./api/src/main/resources/application.yml /app/application.yml
WORKDIR /app

# Optional: automatically inject application.yml into the JAR at build time
# RUN zip -u app.jar -j application.yml

CMD ["java", "-cp", ".", "-jar", "app.jar"]
