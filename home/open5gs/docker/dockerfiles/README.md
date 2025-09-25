Dockerfiles to create Open5GS Docker images.
<code>dockerfile_o5gs</code> uses the dependencies and requirements already installed in sbarrachina/open5gs-base (from <code>dockerfile_o5gs-base</code>). The idea is to make Open5GS containers as lightweight as possible.

DISCLAIMER: now we are using the same Docker image (containing whole Open5GS) for each NF. It would be a better approach to use a dedicated Docker image per NF. 

To build a Docker image:
```bash
cd ..   # cd to the directory with Docerfile and copy into it the desired Dockerfile from /dockerfiles
docker build -t sbarrachina/open5gs:v2.4.0 .
```
If using Windows, you must run Docker Desktop.