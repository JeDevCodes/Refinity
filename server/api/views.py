import sys
import os

# Add the project root (Refinity/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from intelligence.langgraph_r2.app import run_r2  #LangGraph R2 entrypoint
from intelligence.langgraph_r3.app import run_r3  #LangGraph R3 entrypoint

class R2View(APIView):
    def post(self, request):
        try:
            input_data = request.data
            code = input_data.get("code")
            context = input_data.get("context", "")

            if not code:
                return Response({"error": "Code input is required."}, status=400)

            result = run_r2(code=code, context=context)
            return Response({"result": result}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class R3View(APIView):
    def post(self, request):
        try:
            input_data = request.data
            code = input_data.get("code")
            context = input_data.get("context", "")

            if not code:
                return Response({"error": "Code input is required."}, status=400)

            result = run_r3(code=code, context=context)
            return Response({"result": result}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
