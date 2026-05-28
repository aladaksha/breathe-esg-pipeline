# Engineering Ambiguity Resolution Ledger

## 1. SAP Reality Selection (Fuel & Procurement)
* **Chosen Format**: Nightly Flat-File CSV Drop via automated file directories (`AL11`).
* **Justification**: Live OData or BAPI direct connections break down due to security parameters and legacy firewall constraints. Batch-processing flat-files represents the real-world enterprise norm.
* **Ignored Subsets**: Erased vendor tax codes, currency translation fluctuations, and purchasing group reference numbers.

## 2. Utility Electricity Reality Selection
* **Chosen Format**: Automated Portal CSV Statement Export extracts.
* **Justification**: Municipal utilities lack uniform developer APIs. PDF parsing via OCR is too brittle for consistent enterprise tracking pipelines. 
* **Ambiguity Fixed**: Billing frequencies crossing calendar months (e.g., Nov 14 to Dec 15) are mapped to actual system dates, allowing the backend logic to handle fractional adjustments.

## 3. Business Travel Reality Selection (Concur API)
* **Chosen Format**: Itinerary Route Payload Segment JSON Object dumps.
* **Justification**: Travel engines do not return emissions values. They return airport pairs (`JFK` to `LHR`) and cabin classes. Our ingestion engine converts these variables into standard distances (`pkm`) and appends multipliers based on tickets (`Business` vs `Economy`).
