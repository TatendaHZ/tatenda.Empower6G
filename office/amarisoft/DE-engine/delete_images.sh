#!/bin/bash

# Docker Hub credentials
USERNAME="tatendaupc"
PASSWORD="Hamenikoko11."

# Images/tags to delete
IMAGES=(
  "nef-all"
  "nef-coded"
  "nef-tr"
  "nef-hry"
  "net-final"
  "nef-ury"
  "nef-fry"
  "nef-tttry"
  "nef-ttry"
  "nef-try"
  "tatenda-nef-bw"
)

# Step 1: Get JWT token from Docker Hub API
TOKEN=$(curl -s -H "Content-Type: application/json" \
  -X POST -d "{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}" \
  https://hub.docker.com/v2/users/login/ | jq -r .token)

if [ -z "$TOKEN" ] || [ "$TOKEN" == "null" ]; then
  echo "Login failed. Check your credentials."
  exit 1
fi

# Step 2: Delete each image (latest tag)
for IMAGE in "${IMAGES[@]}"; do
  echo "Deleting $USERNAME/$IMAGE:latest ..."
  curl -s -X DELETE -H "Authorization: JWT $TOKEN" \
    "https://hub.docker.com/v2/repositories/$USERNAME/$IMAGE/tags/latest/"
done

echo "All requested images deletion attempted."
