from django.db import models

class DataIngestionBatch(models.Model):
    source_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename_or_endpoint = models.CharField(max_length=255)
    raw_payload_snapshot = models.TextField()

class NormalizedEmissionActivity(models.Model):
    batch = models.ForeignKey(DataIngestionBatch, on_delete=models.CASCADE, related_name='records')
    status = models.CharField(max_length=20, default='PENDING')
    category = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    facility_identifier = models.CharField(max_length=100)
    raw_value_reported = models.DecimalField(max_digits=15, decimal_places=4)
    raw_unit_reported = models.CharField(max_length=20)
    normalized_value = models.DecimalField(max_digits=15, decimal_places=4)
    normalized_unit = models.CharField(max_length=20)
    calculated_co2e_kg = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    system_flags = models.JSONField(default=list)
    analyst_notes = models.TextField(blank=True, default="")
