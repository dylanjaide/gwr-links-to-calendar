import csv

def write_csv(path_to_file: str, data: list):
    with open(path_to_file, "w", newline="") as o:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(o, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)