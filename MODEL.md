# 35% Weight - Data Model Quality & Architecture Defense

## Multi-Tenancy Architecture
We implement a shared-database, isolated-schema multi-tenancy model. Every table tracks an internal tenant relation mapping ID to ensure clean organizational boundary barriers.

## Raw Source Auditing vs Normalized Analytics
To guarantee zero-slop compliance pathways, we separate raw ingested payloads from the active computation ledger:
1. `DataIngestionBatch`: Stores structural snapshots of raw system strings, payloads, filenames, and origin metadata hashes. This forms our immutable source-of-truth baseline for external regulators.
2. `NormalizedEmissionActivity`: Holds sanitized tracking tokens mapped to clean temporal scopes (start_date, end_date), spatial references, standardized measurements (Liters, kWh, pkm), and final GHG calculations ($CO_2e$ in kg).

## Scope Categorization Architecture
* **Scope 1 (FUEL)**: Tracks stationary/mobile combustion units.
* **Scope 2 (ELECTRICITY)**: Captures indirect emissions via purchasing facility metrics.
* **Scope 3 (TRAVEL)**: Records employee flight activity vectors.
