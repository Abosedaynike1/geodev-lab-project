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
- **Limitations:** Natural colour (RGB) has no infrared band, so it cannot
  be used for vegetation indices such as NDVI. Cloud cover is common in
  Cross River State. 2020 is a single time period, so more dates are
  needed to show change over time.

## 2. Forest Data (Global Forest Watch)

- **Source:** Global Forest Watch (globalforestwatch.org)
- **Dataset:** <dataset name, e.g. Tree cover loss / Hansen Global Forest Change>
- **What it shows:** <tree cover loss by year, and tree cover in 2020>
- **Time coverage:** e.g. 2020 to 2021
- **Spatial resolution:** <pixel size, 30 m for Hansen data>
- **File format:** GeoTIFF (.tif)
- **File name and size:** `gfw_forest_akamkpa_clipped.tif`, 17.8 MB,
  clipped to Akamkpa LGA
- **CRS:** EPSG:32632 (WGS 84 / UTM zone 32N)
- **Download date:** 23 September 2026
- **Use in project:** identify where forest was lost from 2020 onwards,
  and compare it with farm sites and forest reserves.
- **Limitations:** at this resolution, small clearings can be missed.
  "Loss" means tree cover was removed. It can include plantation harvest
  or fire, so it does not always mean deforestation.

## 3. Akamkpa LGA Boundary (Shapefile)

- **Source:** <https://data.humdata.org>
- **What it shows:** administrative boundary of Akamkpa Local Government
  Area, Cross River State
- **Geometry:** Polygon
- **Original format:** Shapefile (.shp)
- **Processed file:** `akamkpa_boundary_clipped.gpkg` (GeoPackage, 108 KB)
- **CRS:** EPSG 32632
- **Download date:** 23 September 2026
- **Use in project:** defines the study area and is used to clip the
  Sentinel-2 and forest datasets.
- **Limitations:** administrative boundaries can be simplified and may
  differ slightly between sources.

---

## Data Gaps (still needed)

- Farm boundary polygons for individual agricultural sites
- Protected forest reserve boundaries (for the 1 km distance analysis)
- Historical land cover baseline
- Near-infrared Sentinel-2 band (B8) and more dates, for NDVI and change
  over time
