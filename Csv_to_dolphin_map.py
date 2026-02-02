import csv

INPUT_CSV  = r"D:\\eu_symbols.csv"
OUTPUT_MAP = r"D:\\test.map" 

with open(INPUT_CSV, newline="", encoding="utf-8") as csvfile, \
     open(OUTPUT_MAP, "w", encoding="utf-8") as outfile:

    reader = csv.DictReader(csvfile)

    outfile.write(".text section layout\n")

    for row in reader:
        name      = row.get("name", "").strip()
        ram       = row.get("ram_addr", "").strip()
        size      = row.get("size", "").strip()
        file_obj  = row.get("namespace", "").strip() 
        sec_file  = row.get("file_addr", "").strip()

        if not name or not ram or not size:
            continue

        ram_addr   = ram.upper()
        load_addr  = ram.upper()
        unused     = "0"
        object_    = file_obj if file_obj else "-"
        file_name  = sec_file if sec_file else "-"

        outfile.write(f"{ram_addr} {size.upper()} {load_addr} {unused} {name} {object_} {file_name}\n")

print("Finished:", OUTPUT_MAP)