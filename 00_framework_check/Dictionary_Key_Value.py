print("========== DICTIONARY ==========")
dict_sample = {
    "env": "qa-1",
    "tag": "pubs",
    "use_grid": "false"
}

collect_list = []

for key, value in dict_sample.items():
    print(f"{key} --- {value}")
    if key == "tag":
        print(f"THIS IS TAG -> {key} - {value}")
    collect_list.append(key)
    collect_list.append(value)

print("Collect List -> {}".format(collect_list))