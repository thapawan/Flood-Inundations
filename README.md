# Near Real-Time Flood Inundation Mapping Using Multi-Sensor Satellite Data and Automated Processing on Google Earth Engine (NRTFIM-GEE)
This repository contains code for a flood mapping methodology that combines Sentinel-1 radar data, Sentinel-2 optical data, historical water occurrence data (JRC), and DEM-derived slope within the Google Earth Engine (GEE) platform.

## Methodology

1.  **Data Acquisition:**
    * Retrieves Sentinel-1 GRD data (VV polarization, IW mode).
    * Retrieves Sentinel-2 Surface Reflectance data.
    * Loads JRC Global Surface Water dataset.
    * Loads DEM and calculates slope.
2.  **Sentinel-1 Flood Mapping:**
    * Calculates dynamic threshold based on regional mean of VV polarization.
    * Identifies potential flood areas using thresholding.
    * Refines flood detection using JRC water occurrence and slope.
3.  **Sentinel-2 Flood Mapping (Partial):**
    * Creates cloud masks.
    * AWEI index calculation (to be implemented).
4.  **Application:**
    * Maps Sentinel-1 flood mapping function over time series.

## Novel Aspects

* **Multi-Sensor Data Integration:** Combines Sentinel-1, Sentinel-2, JRC water data, and DEM-derived slope for improved accuracy.
* **Dynamic Thresholding:** Uses adaptive thresholding for Sentinel-1.
* **Historical Water and Slope Incorporation:** Reduces false positives.
* **Potential AWEI Implementation:** Lays groundwork for Sentinel-2 water index.

## Potential Contributions

* Improved flood mapping accuracy.
* Enhanced understanding of flood dynamics.
* Robust and adaptable methodology.
* Contribution to disaster management.

## To Enhance Contribution

* Implement AWEI calculation.
* Validate flood maps with independent data.
* Conduct sensitivity analysis.
* Apply methodology to specific flood events.
* Add code to export flood maps.

## Usage

1.  Clone this repository.
2.  Open the code in the Google Earth Engine Code Editor.
3.  Modify the region of interest (ROI) and time range as needed.
4.  Run the script.
5.  Visualize or export the generated flood maps.

## Dependencies

* Google Earth Engine (GEE) account.
* Python (for potential post-processing or external validation).

## Author

\[Your Name]

## License

\[Your License]
