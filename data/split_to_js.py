import json
import os

source_file = "/Users/daviddrover/Documents/postcode_to_wardkey.json"

with open(source_file, "r", encoding="utf-8") as f:
    data = json.load(f)

grouped = {}
for postcode, wardkey in data.items():
    prefix = postcode.strip().split(" ")[0].upper()
    key = postcode.lower().replace(" ", "")
    if prefix not in grouped:
        grouped[prefix] = {}
    grouped[prefix][key] = wardkey

for prefix, entries in grouped.items():
    filename = f"{prefix}.js"
    with open(filename, "w", encoding="utf-8") as f_out:
        js_content = (
            "window.postcodeToWardKey = window.postcodeToWardKey || {};\n"
            "Object.assign(window.postcodeToWardKey, "
            + json.dumps(entries)
            + ");\n"
        )
        f_out.write(js_content)

print(f"✅ Success! Created {len(grouped)} .js files.")
