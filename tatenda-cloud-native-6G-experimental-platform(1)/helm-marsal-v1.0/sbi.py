import os
import shutil

source_folder = "core"
target_folder = "templates/core"
excluded_files = {"upf-cmap.yaml", "upf-exporter-cmap.yaml"}

# SBI block to append
sbi_block = """
    sbi:
        server:
          no_tls: true
        client:
          no_tls: true
"""

# Step 1: Copy and replace all YAML files from core/ to templates/core/
for filename in os.listdir(source_folder):
    if filename.endswith(".yaml"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(target_folder, filename)
        shutil.copyfile(src_path, dst_path)
        print(f"📁 Copied and replaced: {filename}")

# Step 2: Append SBI block to eligible cmap files
for filename in os.listdir(target_folder):
    if filename.endswith("-cmap.yaml") and filename not in excluded_files:
        filepath = os.path.join(target_folder, filename)
        with open(filepath, 'a') as f:
            f.write(sbi_block)
        print(f"✅ Appended SBI block to: {filename}")
