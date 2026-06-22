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

        # Ensure file pointer is at the beginning
        file_obj.seek(0)

        # Extract text directly from the in-memory file stream
        text = extract_text(file_obj, file_obj.name)
            
        if not text.strip():
            return Response({"error": "Could not extract text from the provided file."}, status=status.HTTP_400_BAD_REQUEST)

        # Extract skills
        extracted_skills = get_extracted_skills(text)

        # Match against all roles
        top_matches = match_all_roles(extracted_skills)

        return Response({
            "extracted_skills": extracted_skills,
            "top_matches": top_matches,
            "saved_file": None
        }, status=status.HTTP_200_OK)
