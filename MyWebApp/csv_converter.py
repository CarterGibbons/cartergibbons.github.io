import csv

input_file = "data/NYCTreeCensus_2015.csv"   # Change this to your actual CSV file
output_file = "treeLocations.js"  # The JS file to write the output to

# Expected columns in CSV: latitude, longitude, species
with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    tree_locations = []

    for row in reader:
        lat = row["latitude"].strip()
        lng = row["longitude"].strip()
        species = row["spc_latin"].strip().replace('"', '\\"')
        tree_locations.append(f'  {{ lat: {lat}, lng: {lng}, species: "{species}" }}')

# Write to JS file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const treeLocations = [\n")
    f.write(",\n".join(tree_locations))
    f.write("\n];\n")

print(f"Exported {len(tree_locations)} tree locations to {output_file}")