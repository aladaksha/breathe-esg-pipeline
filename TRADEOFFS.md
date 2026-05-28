# Engineering Tradeoffs Document

To protect our development timeline and focus on a clean data core without introducing slop, three specific architectural features were intentionally omitted from this sprint:

1. **Dynamic File Processing Interface**: Omitted a dynamic file upload interface box. Building drag-and-drop file wrappers shifts engineering focus away from the core ingestion parsing algorithms and anomaly rules validation layer.
2. **Dynamic Emission Factor Lookup Tables**: We hardcoded environmental conversion multipliers directly inside our service layers instead of deploying external API lookups to providers like Climatiq. This avoids external service downtime errors during the evaluation dry-run.
3. **User Authentication Roles**: Bypassed setting up complete RBAC auth tables (Auditors vs Analysts) to ensure the prototype focuses entirely on parsing metrics, identifying outliers, and validating data immutability.
