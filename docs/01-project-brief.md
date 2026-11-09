# Project Brief: AgriEvidence
**Tagline**:Evidence about the land, not just the farm.

## Part 1: The Question
Which agricultural sites in Akamkpa Local Government Area, overlap with or sit within 1 kilometer of protected forest reserves and experienced forest cover loss from 2020 to present?

## Part 2: Why It Matters
Agricultural expansion in Akamkpa LGA frequently encroaches on protected tropical rainforest boundaries. Environmental compliance officers, carbon-credit developers, and agricultural investors currently lack a single tool to quickly verify whether a farm's history involves recent deforestation. AgriEvidence compiles these layers into an automated report to prove sustainable, non-deforested production.

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

# Data Notes

This document describes the datasets used in AgriEvidence for the pilot
area, **Akamkpa Local Government Area, Cross River State, Nigeria**.

## Summary

| # | Dataset | Type | Source | Role in project |
|---|---------|------|--------|-----------------|
| 1 | Sentinel-2 imagery (2025) | Raster | <Copernicus Browser / Data Space / Earth Engine> | Identify farm boundaries and view the land in 2020 |
| 2 | Forest data | Raster | Global Forest Watch | Show where forest was lost |
| 3 | Akamkpa LGA boundary | Vector (shapefile) | <source> | Defines the study area |

---

## 1. Sentinel-2 Imagery

- **Source:** <Copernicus Browser / Copernicus Data Space / Google Earth Engine>
- **Provider:** European Space Agency (ESA), Copernicus programme
- **Imagery time coverage:** 2025
- **Download date:** 23 September 2026
- **Spatial resolution:** 10 m
- **Band composite:** Natural colour (bands 4-3-2, red-green-blue)
- **File format:** GeoTIFF (.tif)
- **File name and size:** `sentinel2_akamkpa_clipped.tif`, 642 MB
  (673,223,290 bytes), clipped to Akamkpa LGA
- **CRS:** EPSG:32632 (WGS 84 / UTM zone 32N)
- **Licence:** Free and open under the Copernicus data policy; attribute
  "Contains modified Copernicus Sentinel data 2020"
- **Use in project:** visual identification and digitising of farm
  boundaries, and a baseline view of the land in 2020.
- **Limitations:** The imagery uses a natural-colour RGB composite, so it does not include infrared information needed for vegetation indices such as NDVI. Cloud cover can also affect Sentinel-2 imagery in Cross River State. Since this is imagery from a single period, additional dates will be needed to properly study changes in the landscape over time.

## 2. Forest Data (Global Forest Watch)

This dataset is used to understand where and when tree cover was lost in Akamkpa LGA. It will help the project investigate changes around agricultural areas and compare forest loss with farm locations and forest reserves.

- **Source:** Global Forest Watch (globalforestwatch.org)
- **Dataset:** Hansen Global Forest Change (GFC) – Tree Cover Loss
- **What it shows:** The dataset shows areas where tree cover was lost and the year the loss occurred.
- **Time coverage:** 2001–2024
- **Spatial resolution:** <pixel size, 30 m for Hansen data>
- **File format:** GeoTIFF (.tif)
- **File name and size:** `gfw_forest_akamkpa_clipped.tif`, 17.8 MB,
  clipped to Akamkpa LGA
- **CRS:** EPSG:32632 (WGS 84 / UTM zone 32N)
- **Download date:** 23 September 2026
- **How it will be used:** The project will focus on tree-cover loss from 2020 onwards. This information will be compared with farm boundaries and forest-reserve locations to help reconstruct the environmental history of agricultural land.
- **Limitations:** A detected tree-cover loss does not automatically mean deforestation. Tree cover can be lost because of forest harvesting, plantation activities, fire, or other disturbances. Also, because the data has a 30 m resolution, very small areas of tree-cover loss may not be detected.
  
## 3. Akamkpa LGA Boundary (Shapefile)

This boundary defines the study area for the AgriEvidence project. It represents Akamkpa Local Government Area in Cross River State, Nigeria, and is used to limit the analysis to the selected study area.

- **Source:** Humanitarian Data Exchange (HDX) — https://data.humdata.org
- **What it shows:** The administrative boundary of Akamkpa Local Government Area, Cross River State
- **Geometry:** Polygon
- **Original format:** Shapefile (.shp)
- **Processed file:** akamkpa_boundary_clipped.gpkg (GeoPackage, 108 KB)
- **CRS:** EPSG 32632
- **Download date:** 23 September 2026
- **How it will be Used in project:** The boundary defines the area of interest for the project. It will be used to clip the Sentinel-2 imagery and forest-change data so that the analysis focuses only on Akamkpa LGA.
- **Limitations:** Administrative boundaries may be simplified and can differ slightly between data sources. The boundary is therefore used as the project study-area boundary and may not represent every legal or survey boundary with exact positional accuracy.
---

## Data Gaps (still needed)

- Farm boundary polygons for individual agricultural sites
- Protected forest reserve boundaries (for the 1 km distance analysis)
- Historical land cover baseline
- Near-infrared Sentinel-2 band (B8) and more dates, for NDVI and change
  over time


## Month 2

- Week 5: hello.py, first Python script (screenshots/week5.png)
- Week 6: set up the project with uv and pandas (pyproject.toml, uv.lock, check.py, screenshots/week6.png)
- Week 7: analyse.py, Python basics with AgriEvidence farm data (screenshots/week7.png)
