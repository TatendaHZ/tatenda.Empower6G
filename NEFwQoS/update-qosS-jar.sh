#!/bin/bash

# Name of your NEF pod
POD_NAME=$(kubectl get pods | grep nef | awk '{print $1}')

# File paths
YML_FILE="/app/application.yml"
JAR_FILE="/app/app.jar"
TEMP_DIR=$(mktemp -d)

echo "📌 Copying application.yml from pod..."
kubectl exec -it $POD_NAME -- cat $YML_FILE > tmp-application.yml

echo "📌 Updating qosS values in application.yml..."
sed -i 's/marBwDl: "200 Kbps"/marBwDl: "30 Mbps"/' tmp-application.yml
sed -i 's/marBwUl: "200 Kbps"/marBwUl: "30 Mbps"/' tmp-application.yml

echo "📌 Copying updated application.yml back into pod..."
kubectl cp tmp-application.yml $POD_NAME:$YML_FILE

echo "📌 Updating application.yml inside app.jar..."
# Copy JAR locally
kubectl cp $POD_NAME:$JAR_FILE $TEMP_DIR/app.jar

# Extract application.yml from JAR
unzip -p $TEMP_DIR/app.jar BOOT-INF/classes/application.yml > $TEMP_DIR/application.yml

# Update qosS in extracted file
sed -i 's/marBwDl: "200 Kbps"/marBwDl: "30 Mbps"/' $TEMP_DIR/application.yml
sed -i 's/marBwUl: "200 Kbps"/marBwUl: "30 Mbps"/' $TEMP_DIR/application.yml

# Replace the file inside the JAR
(cd $TEMP_DIR && zip -u app.jar BOOT-INF/classes/application.yml)

# Copy updated JAR back to pod
kubectl cp $TEMP_DIR/app.jar $POD_NAME:$JAR_FILE

# Cleanup
rm -rf $TEMP_DIR tmp-application.yml

echo "✅ qosS updated in both application.yml and app.jar inside pod $POD_NAME"
