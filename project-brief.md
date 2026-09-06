# Project Brief: AgriEvidence
Tagline:Evidence about the land, not just the farm.

## Part 1: The Question
Which agricultural sites in Akamkpa Local Government Area,overlap with or sit within 1 kilometer of protected forest reserves and experienced forest cover loss from 2020 to present?

## Part 2: Why It Matters
Agricultural expansion in Akamkpa LGA frequently encroaches on protected tropical rainforest boundaries.Environmental compliance officers, carbon-credit developers, and agricultural investors currently lack a single tool to quickly verify whether a farm's history involves recent deforestation. AgriEvidence compiles these layers into an automated report to prove sustainable, non-deforested production.

## Part 3: The Data Needed
- Farm boundaries (polygons defining individual agricultural production sites)
- Sentinel-2 satellite imagery (multi-temporal multispectral observations)
- Historical land cover data (regional baseline land-cover classification)
- Forest-change data (annual tree cover loss and disturbance alerts)
- Protected area boundaries (delineation of national parks and forest reserves)
- Administrative boundaries (State, LGA, and Ward boundaries)

## Part 4: Data Sources
- **Farm Boundaries:** Extracted using Segment Anything Model (SAM) applied to Copernicus Sentinel-2 imagery.
  - *Link:* https://dataspace.copernicus.eu/
- **Sentinel-2 Satellite Imagery:** Copernicus Data Space Ecosystem.
  - *Link:* https://dataspace.copernicus.eu/
- **Historical Land-Cover Data:** FAO Agro-Informatics Platform (New Land Cover Data for Nigeria, 2024).
  - *Link:* https://data.apps.fao.org/
- **Forest-Change Data:** Global Forest Watch (Tree Cover Loss Dataset for Cross River).
  - *Link:* https://www.globalforestwatch.org/dashboards/country/NGA/9/
- **Protected Area Boundaries:** World Database on Protected Areas (WDPA) via Protected Planet.
  - *Link:* https://www.protectedplanet.net/country/NGA
- **Administrative Boundaries:** GRID3 Nigeria Administrative Boundaries (Akamkpa LGA & Wards).
  - *Link:* https://data.grid3.org/

  ## Part 5: What I Will Build
I will build AgriEvidence, an automated geospatial engine that ingests farm boundary coordinates and checks them against forest disturbance and protected area layers. The system will auto-generate an Agricultural Land Evidence Report showing the farm's spatial boundary, historic land cover, and environmental compliance status.
