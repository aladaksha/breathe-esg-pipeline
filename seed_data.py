from django.core.management.base import BaseCommand
from datetime import datetime
from decimal import Decimal
from core.models import DataIngestionBatch, NormalizedEmissionActivity

class Command(BaseCommand):
    help = "Seeds database with complex, realistic raw corporate ESG data streams"

    def handle(self, *args, **options):
        # 1. Clear out previous records to ensure a fresh clean state
        NormalizedEmissionActivity.objects.all().delete()
        DataIngestionBatch.objects.all().delete()

        # 2. Build Ingestion Sources Snapshots (Your Baseline Audit Trail)
        sap_b = DataIngestionBatch.objects.create(
            source_type='SAP', 
            filename_or_endpoint='AL11_DUMP_04.csv', 
            raw_payload_snapshot="WERKS=PL99, MENG=12500, MEINS=GAL"
        )
        ut_b = DataIngestionBatch.objects.create(
            source_type='UTILITY', 
            filename_or_endpoint='pge_billing_q3.csv', 
            raw_payload_snapshot="Usage=185000 kWh, Start=10/14, End=11/13"
        )
        tr_b = DataIngestionBatch.objects.create(
            source_type='TRAVEL', 
            filename_or_endpoint='concur_api_v4', 
            raw_payload_snapshot="JFK->LHR, Class=Business"
        )

        # 3. Row 1: Messy SAP Fuel entry containing an unsupported unit conversion and bad plant code
        NormalizedEmissionActivity.objects.create(
            batch=sap_b, status='FLAGGED', category='FUEL',
            start_date=datetime.now().date(), end_date=datetime.now().date(),
            facility_identifier="Unknown Plant Lookup (PL99)", raw_value_reported=Decimal('12500'),
            raw_unit_reported='GAL', normalized_value=Decimal('47317.6'), normalized_unit='Liters',
            calculated_co2e_kg=Decimal('126811.2'), system_flags=['UNKNOWN_FACILITY_CODE', 'OUTLIER_DETECTED']
        )

        # 4. Row 2: Messy Utility Meter Entry showing an irregular billing period split and a massive usage spike
        NormalizedEmissionActivity.objects.create(
            batch=ut_b, status='FLAGGED', category='ELECTRICITY',
            start_date=datetime.strptime('2026-03-01', '%Y-%m-%d').date(), end_date=datetime.strptime('2026-04-15', '%Y-%m-%d').date(),
            facility_identifier="Meter: MTR-8821A (Main Plant)", raw_value_reported=Decimal('185000'),
            raw_unit_reported='kWh', normalized_value=Decimal('185000'), normalized_unit='kWh',
            calculated_co2e_kg=Decimal('74000.0'), system_flags=['OUTLIER_DETECTED', 'IRREGULAR_BILLING_PERIOD']
        )

        # 5. Row 3: Clean Ingested Scope 3 Business Travel Flight Segment
        NormalizedEmissionActivity.objects.create(
            batch=tr_b, status='PENDING', category='TRAVEL',
            start_date=datetime.now().date(), end_date=datetime.now().date(),
            facility_identifier="Travel Segment: JFK to LHR", raw_value_reported=Decimal('1'),
            raw_unit_reported='Trip', normalized_value=Decimal('8308.5'), normalized_unit='pkm',
            calculated_co2e_kg=Decimal('1246.2'), system_flags=[]
        )

        self.stdout.write(self.style.SUCCESS("Database loaded with complex multi-source data parameters successfully."))
