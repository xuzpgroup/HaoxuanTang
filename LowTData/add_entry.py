import json

# JSON file 
path = ''
file = ''

# Define the function to add a data entry to the database
def add_data_entry(db, entry, epath, data, unit):
    # Check if the unit field exists
    if 'unit' not in db:
        db['unit'] = {}
    if entry in db['unit']:
        print(f"Warning: the unit of entry {entry} exists, added as {entry}_user")
        db['unit'][f"{entry}_user"] = unit
    else:
        db['unit'][entry] = unit

    # Initialize the data entry for each article and dataset
    for art_id, ds_id, value in data:
        try:
            art = db['articles'][art_id-1]
            ds = art['scidata']['datasets'][ds_id-1]
            path_parts = epath.strip('.').split('.')
            current_dict = ds
            for part in path_parts:
                current_dict = current_dict.setdefault(part, {})
            current_dict[entry] = value
        except IndexError:
            print(f"Failed to add value at article {art_id}, dataset {ds_id}")

    return db

# Load JSON data
with open(f'{path}{file}', 'r') as f:
    db = json.load(f)

# Define the data entry to be added
entry = 'hardness'  # Name of the data entry
epath = '.static_mech'  # Path from fatigue datasets to the destination
unit = 'HV'  # Unit of the data entry
data = [(1, 1, [300]), (2, 3, [200])]  # Each tuple is a data triplet: (article ID, dataset ID, value)

# Add the data entry to the database
db = add_data_entry(db, entry, epath, data, unit)

# Write the updated data to the JSON file
with open(f'{path}{file}', 'w') as f:
    json.dump(db, f, indent=4)


