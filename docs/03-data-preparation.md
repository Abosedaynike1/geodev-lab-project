# Data Preparation

This document records how the data was prepared in QGIS for AgriEvidence.
Study area: Akamkpa LGA, Cross River State, Nigeria.

## 1. Coordinate Reference System

- **Working CRS:** EPSG:32632 (WGS 84 / UTM zone 32N)
- **Why:** Akamkpa LGA lies within UTM Zone 32N. A projected CRS gives
  distance, perimeter and area in metres, which is needed for farm
  boundary digitising and area calculations.

## 2. Reprojection Log

All layers were reprojected (not just assigned a CRS) to EPSG:32632.

| Dataset | Original CRS | Working CRS | Type |
|---------|--------------|-------------|------|
| Akamkpa LGA boundary | EPSG:4326 | EPSG:32632 | Vector |
| Sentinel-2 imagery (natural colour, 2020) | <check in QGIS> | EPSG:32632 | Raster |
| Global Forest Watch forest data | EPSG:4326 | EPSG:32632 | Raster |

## 3. Clipping

All datasets were clipped to the Akamkpa LGA boundary to limit the
analysis to the study area and reduce file size.

| Output | Description | Size |
|--------|-------------|------|
| Akamkpa boundary (clipped) | Vector | 108 KB |
| `gfw_forest_akamkpa_clipped.tif` | Forest data | 17.8 MB |
| `sentinel2_akamkpa_clipped.tif` | Natural colour, 10 m | 642 MB (stored locally) |

## 4. Quality Checks

### Check 1: CRS alignment
- **Result:** Pass
- **Finding:** All layers share EPSG:32632 with no on-the-fly
  projection warnings in QGIS.
- **Action taken:** Reprojected all inputs from their original CRS.

### Check 2: Spatial overlap
- **Result:** Pass
- **Finding:** Clipped rasters align with the LGA boundary with no offset.
- **Action taken:** Used the reprojected boundary as the clipping mask.

### Check 3: Attribute table and geometry
- **Result:** Pass
- **Finding:** No null geometries or empty attributes in the boundary layer.
- **Action taken:** Added an area field calculated in EPSG:32632.

### Check 4: Raster values and bands
- **Result:** Pass
- **Finding:** Pixel values are within the expected range, with no band
  corruption or data gaps.
- **Action taken:** Set the Sentinel-2 display to bands 4-3-2 (natural
  colour) and NoData to 0 for transparency.

### Check 5: Extent
- **Result:** Pass
- **Finding:** Extents fall within the expected UTM Zone 32N range for
  Akamkpa LGA.
- **Action taken:** Confirmed all layers use matching metre-based extents.

## 5. Area Calculation

- **Method:** `$area` in the Field Calculator, using EPSG:32632
- **Akamkpa LGA area:** 5,389.06 km² (about 538,906 hectares, or
  5.389 × 10⁹ square metres)

## 6. Why GeoPackage

Outputs were saved as GeoPackage (.gpkg) because it stores several layers
in one file, has no field-name limits, and works across GIS software.

## 7. Problems and Decisions

- **Projection mismatch:** source data was in geographic coordinates, which
  prevents metric area calculations. All layers were standardised to
  EPSG:32632.
- **NoData black borders and file locking:** exported rasters had opaque
  black NoData padding, and existing GeoPackages were locked on export.
  NoData was set to 0 for transparency, and outputs were exported to a
  new GeoPackage.

## 8. Analysis-Ready Data

- **Location:** `data/processed/akamkpa_analysis_ready.gpkg`
- **Stored locally only (too large for GitHub):** Sentinel-2 clipped raster


