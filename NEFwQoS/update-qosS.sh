#!/bin/bash

# Name of your NEF pod
POD_NAME=$(kubectl get pods | grep nef | awk '{print $1}')

# Paths inside pod
FILE_PATH="/app/application.yml"
JAR_PATH="/app/app.jar"

# Path to the txt file with new qosS values (local)
QOS_FILE="qosS-values.txt"

# 1️⃣ Copy the file locally from the pod
kubectl exec -i $POD_NAME -- cat $FILE_PATH > tmp-application.yml

# 2️⃣ Read qosS values from the txt file and update tmp-application.yml
while IFS= read -r line
do
    # Extract key and value from each line
    key=$(echo "$line" | cut -d: -f1 | xargs)
    value=$(echo "$line" | cut -d: -f2- | xargs)
    
    # Use sed to replace the line under qosS:
    sed -i "/qosS:/,/^[[:space:]]*[^ ]/ s/^[[:space:]]*$key:.*/      $key: $value/" tmp-application.yml
done < "$QOS_FILE"

# 3️⃣ Copy updated file back into the pod
kubectl cp tmp-application.yml $POD_NAME:$FILE_PATH

# 4️⃣ Update the application.yml inside the app.jar
kubectl exec -i $POD_NAME -- sh -c "
mkdir -p /app/BOOT-INF/classes &&
cp /app/application.yml /app/BOOT-INF/classes/ &&
cd /app &&
zip -ur app.jar BOOT-INF/classes/application.yml &&
rm -rf /app/BOOT-INF
"

# 5️⃣ Optional: Verify changes
kubectl exec -i $POD_NAME -- sh -c "
echo '✅ Loose file:'; grep -A 3 'qosS:' $FILE_PATH;
echo '✅ Inside JAR:'; unzip -p $JAR_PATH BOOT-INF/classes/application.yml | grep -A 3 'qosS:'
"

# 6️⃣ Clean up local temporary file
rm tmp-application.yml

echo "✅ qosS successfully updated in $FILE_PATH and inside $JAR_PATH of pod $POD_NAME"
