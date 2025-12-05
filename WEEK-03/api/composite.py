import json

# def merge_json_files(file_paths, output_file):
#     merged_data = []
#     for path in file_paths:
#         with open(path, 'r') as file:
#             data = json.load(file)
#             merged_data.append(data)
#     with open(output_file, 'w') as outfile:
#         json.dump(merged_data, outfile)


# file_paths = ["01.json", "02.json"]

# output_file = "merged.json"

# merge_json_files(file_paths, output_file)

# print(f"Merged data written to '{output_file}'")


###########################################3

# files = ["01.json","02.json"]
# merged_data=[]
# for file in files:
#     with open(file,'r') as f:
#         data = json.load(f)
#         merged_data.append(data)
# with open("merged1.json",'w')as f:
#     # f.write(json.dump(merged_data,indent=4))
#     json.dump(merged_data,f,indent=4)

###

import json

files = ["01.json", "02.json"]
merged_data = []

for file in files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)

            # ----------- VALIDATION START -----------

            # File must contain a list
            if not isinstance(data, list):
                print(f"Error: {file} must contain a JSON list")
                continue

            # Validate each object inside list
            valid_items = []
            for item in data:

                # Must be a dict
                if not isinstance(item, dict):
                    print(f"Error in {file}: Each entry must be a JSON object")
                    continue

                # Must contain required fields
                if "id" not in item or "name" not in item:
                    print(f"Error in {file}: Missing 'id' or 'name': {item}")
                    continue

                # Type validation
                if not isinstance(item["id"], int):
                    print(f"Error in {file}: 'id' must be integer → {item}")
                    continue

                if not isinstance(item["name"], str):
                    print(f"Error in {file}: 'name' must be string → {item}")
                    continue

                # If all good → accept item
                valid_items.append(item)

            # Append only valid entries from this file
            merged_data.extend(valid_items)

            # ----------- VALIDATION END -----------

    except FileNotFoundError:
        print(f"Error: File {file} not found")

# Save final merged data
with open("merged11.json", 'w') as f:
    json.dump(merged_data, f, indent=4)

print("Merging completed. Valid data saved to merged1.json")
