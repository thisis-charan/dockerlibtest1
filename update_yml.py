from ruamel.yaml import YAML
import os

def update_data(target, source):
    """
    Recursively updates the target dict using keys found in source.
    Only keys that already exist in target will be updated.
    """
    for key, source_value in source.items():
        if key in target:
            target_value = target[key]
            if isinstance(target_value, dict) and isinstance(source_value, dict):
                update_data(target_value, source_value)
            else:
                target[key] = source_value

# ================================
# For Windows:
file1_path = r"C:\Users\Sai Charan\OneDrive\Desktop\test\ci.yml"
file2_path = r"C:\Users\Sai Charan\OneDrive\Desktop\test\cicd.yml"
output_path = r"C:\Users\Sai Charan\OneDrive\Desktop\test\cicdnew.yml"



if not os.path.exists(file1_path):
    raise FileNotFoundError(f"File not found: {file1_path}")
if not os.path.exists(file2_path):
    raise FileNotFoundError(f"File not found: {file2_path}")

yaml = YAML()
# Optionally adjust indentation settings to match your original formatting.
yaml.indent(mapping=2, sequence=4, offset=2)

# Load file2 (the base file whose format you want to preserve)
with open(file2_path, 'r') as f2:
    data2 = yaml.load(f2)

# Load file1 (the file with updated values)
with open(file1_path, 'r') as f1:
    data1 = yaml.load(f1)

# Update data2 using data1 (only for keys that already exist in data2)
update_data(data2, data1)

# Write the updated data back to a file, preserving the format as much as possible.
with open(output_path, 'w') as out:
    yaml.dump(data2, out)

print("File2 has been updated successfully, preserving its original format!")
