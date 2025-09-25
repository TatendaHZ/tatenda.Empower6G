# Use an Ubuntu base image
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Uninstall any existing WebUI (as per instructions)
RUN curl -fsSL https://open5gs.org/open5gs/assets/webui/uninstall | sudo -E bash -

# Install the latest WebUI
RUN curl -fsSL https://open5gs.org/open5gs/assets/webui/install | sudo -E bash -

# Expose the port used by the WebUI (default is 3000)
EXPOSE 3000

# Command to run the WebUI
# Replace with the actual command to start the WebUI if needed
CMD ["node", "/usr/local/lib/node_modules/@open5gs/webui/app.js"]
