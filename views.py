from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, serializers
from .models import NormalizedEmissionActivity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalizedEmissionActivity
        fields = '__all__'

class ActivityListView(generics.ListAPIView):
    queryset = NormalizedEmissionActivity.objects.all().order_by('-id')
    serializer_class = ActivitySerializer

class AuditActionReviewView(APIView):
    def post(self, request, pk):
        try:
            record = NormalizedEmissionActivity.objects.get(pk=pk)
        except NormalizedEmissionActivity.DoesNotExist:
            return Response({'error': 'Record missing'}, status=status.HTTP_404_NOT_FOUND)

        if record.status == 'VALIDATED':
            return Response({'error': 'Immutability Guard: Locked for audit.'}, status=status.HTTP_400_BAD_REQUEST)

        action = request.data.get('action')
        notes = request.data.get('notes', '')

        if action == 'APPROVE':
            record.status = 'VALIDATED'
        elif action == 'FLAG':
            record.status = 'FLAGGED'
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

        record.analyst_notes = notes
        record.save()
        return Response({'id': record.id, 'status': record.status})
