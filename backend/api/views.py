import os
import uuid
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .nlp_utils import extract_text, get_extracted_skills, match_all_roles

class AnalyzeResumeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('resume')

        if not file_obj:
            return Response({"error": "No resume file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Save the file with a UUID to prevent overwriting
        # Create media directory if it does not exist
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        
        ext = os.path.splitext(file_obj.name)[1]
        unique_filename = f"{uuid.uuid4()}{ext}"
        file_path = os.path.join(settings.MEDIA_ROOT, unique_filename)

        with open(file_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        # Re-open the saved file for extraction
        with open(file_path, 'rb') as saved_file:
            # Extract text from the saved file
            text = extract_text(saved_file, file_obj.name)
            
        if not text.strip():
            return Response({"error": "Could not extract text from the provided file."}, status=status.HTTP_400_BAD_REQUEST)

        # Extract skills
        extracted_skills = get_extracted_skills(text)

        # Match against all roles
        top_matches = match_all_roles(extracted_skills)

        return Response({
            "extracted_skills": extracted_skills,
            "top_matches": top_matches,
            "saved_file": f"{settings.MEDIA_URL}{unique_filename}"
        }, status=status.HTTP_200_OK)
