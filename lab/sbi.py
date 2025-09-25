import os

folder = "templates/core"
exclude_file = "upf-cmap.yaml"

# Block to append (already indented)
sbi_block = """
    sbi:
        server:
          no_tls: true
        client:
          no_tls: true
"""

for filename in os.listdir(folder):
    if filename.endswith("-cmap.yaml") and filename != exclude_file:
        filepath = os.path.join(folder, filename)

        with open(filepath, 'a') as f:
            f.write(sbi_block)

        print(f"✅ Appended SBI block to: {filename}")
