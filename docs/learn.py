# learn.py - Week 7: AgriEvidence mini evidence report

# STRING
project = "AgriEvidence"
tagline = "Evidence about the land, not just the farm"
country = "Nigeria"
state = "Cross River"
study area = "Akamkpa"
print(project.upper())
print(tagline)
print("Country: " + study area + " Study area, " + state + " State")

# Integer
datasets_used = 6
print("Datasets used:", datasets_used)

# Float
farm_area_ha = 50.0
min_elevation_m = 112.5
max_elevation_m = 148.2
forest_loss_ha = 1.5

# Boolean
overlaps_protected_area = False
forest_loss_recorded = forest_loss_ha > 0   # boolean from a comparison

# List
landcover_classes = ["Forest", "Cropland", "Built-up", "Bare land"]
landcover_ha = [12.0, 30.0, 3.0, 5.0]
print("Land-cover classes found:", len(landcover_classes))

# Function
def percent_of_farm(part, total):
    return part / total * 100

def forest_status(forest_percent):
    

    if forest_percent >= 40:
        return "High forest cover"
    elif forest_percent >= 20:
        return "Moderate forest cover"
    else:
        return "Low forest cover"

LOOP
print("\nLAND COVER")
total_ha = 0.0
for i in range(len(landcover_classes)):
    pct = percent_of_farm(landcover_ha[i], farm_area_ha)
    print(landcover_classes[i] + ":", landcover_ha[i], "ha (" + str(round(pct, 1)) + "%)")
    total_ha = total_ha + landcover_ha[i]


if total_ha == farm_area_ha:
    print("Check passed: land-cover areas add up to the farm area")
else:
    print("Warning: land-cover areas do not match the farm area")

forest_pct = percent_of_farm(landcover_ha[0], farm_area_ha)
print("Forest status:", forest_status(forest_pct))

print("\nTERRAIN")
print("Elevation range:", min_elevation_m, "to", max_elevation_m, "m")

print("\nFOREST CHANGE")
if forest_loss_recorded:
    print("Recorded forest loss:", forest_loss_ha, "ha")
else:
    print("No recorded forest loss")

print("\nPROTECTED AREA")
if overlaps_protected_area:
    print("Overlap: Yes")
else:
    print("Overlap: No")