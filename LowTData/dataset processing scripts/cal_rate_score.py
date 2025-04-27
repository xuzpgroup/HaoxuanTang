import json

# Assuming json_data is already loaded JSON data
path = ''
file = ''
with open(f'{path}{file}', 'r') as f:
    json_data = json.load(f)


# Weight initialization function
def weight_init(default_weight):
    return {
        "materials": {
            "mat_type": default_weight,
            "mat_name": default_weight,
            "composition": default_weight,
            "ratio_type": default_weight,
        },
        "processing": {
            "proc_para": default_weight,
            "ingot_desc": default_weight,
            "ingot_size": default_weight,
            "surf_para": default_weight,
        },
        "testing": {
            "test_type": default_weight,
            "test_tem": default_weight,
            "test_env": default_weight,
            "refrigerant": default_weight,
            "test_mac": default_weight,
            "test_standard": default_weight,
            "load_ctrl": default_weight,
            "rate": default_weight,
            "spec_desc": default_weight,
            "spec_shape": default_weight,
            "spec_size": default_weight,
            "spec_standard": default_weight,
            "spec_dir": default_weight,
        },
        "mech_prop": {
            "temperature": default_weight,
            "yield_strength": default_weight,
            "ultimate_strength": default_weight,
            "elongation": default_weight,
        },
    }


# Fill rate calculation function
def fill_rate_field(field, weight):
    tot = 0
    fill = 0
    for key in field:
        w = weight.get(key, 0)
        tot += w
        if field[key]:  # Check if the field is not empty
            fill += w
    return tot, fill


# Rating score calculation function
def cal_rating_score(ds, weight):
    tot = 0
    fill = 0

    # Calculate the fill rate for each part and accumulate
    for field in ["materials", "processing", "testing", "mech_prop"]:
        t, f = fill_rate_field(ds.get(field, {}), weight[field])
        tot += t
        fill += f

    # Calculate the total score
    score = fill / tot if tot > 0 else 0
    return score


# Initialize default weight
default_weight = 1
weight = weight_init(default_weight)



# Traverse the JSON data and calculate scores
for article in json_data["L-T"]["articles"]:
    for ds in article["scidata"]["datasets"]:
        # Calculate the score and add it to the dataset
        ds["score"] = cal_rating_score(ds, weight)

# Write the updated data to a new JSON file
with open('.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
