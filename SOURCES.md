# Real-World Source Material Research Dossier

## 1. SAP Data Streams
* **Format**: Standard flat-file tables (`BSEG` / `EKPO`).
* **Messy Parameters**: German structural naming labels (`MENG` for quantity, `MEINS` for unit), cryptic facility references instead of named tags, and localized date layouts (`DD.MM.YYYY`).
* **Breaking Point**: If an enterprise configuration updates its unit text codes from English to another language, the string match logic will fail until conversion maps are updated.

## 2. Utility Portals
* **Format**: Multi-column text fields containing spaces and text strings.
* **Messy Parameters**: Non-aligned billing timelines and extreme consumption surges from bad meter reads.
* **Breaking Point**: If a utility company adjusts its column names or headers, the position-based reading index fails.

## 4. Concur Travels
* **Format**: Structural multi-segment itinerary JSON logs.
* **Messy Parameters**: Lack of raw mileage metrics, requiring explicit translation maps to resolve ticket location tags (`JFK -> LHR`).
* **Breaking Point**: Ingesting ticket modifications or cancellation updates without clear tracking IDs will result in duplicate carbon calculations.
