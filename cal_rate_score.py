import json

# 假设json_data是已经加载的JSON数据
path = ''
file = 'LT_5_26.json'
with open(f'{path}{file}', 'r') as f:
    json_data = json.load(f)


# 权重初始化函数
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


# 填充率计算函数
def fill_rate_field(field, weight):
    tot = 0
    fill = 0
    for key in field:
        w = weight.get(key, 0)
        tot += w
        if field[key]:  # 检查字段是否不为空
            fill += w
    return tot, fill


# 评分计算函数
def cal_rating_score(ds, weight):
    tot = 0
    fill = 0

    # 计算每个部分的填充率并累加
    for field in [ "materials", "processing", "testing", "mech_prop"]:
        t, f = fill_rate_field(ds.get(field, {}), weight[field])
        tot += t
        fill += f

    # 计算总分
    score = fill / tot if tot > 0 else 0
    return score


# 初始化默认权重
default_weight = 1
weight = weight_init(default_weight)



# 遍历JSON数据并计算评分
for article in json_data["L-T"]["articles"]:
    for ds in article["scidata"]["datasets"]:
        # 计算评分并将结果添加到 dataset 中
        ds["score"] = cal_rating_score(ds, weight)

# 将更新后的数据写入新的 JSON 文件
with open('LT_5_26_updated.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)