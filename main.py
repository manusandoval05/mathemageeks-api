from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import anthropic
from anthropic_tools import answer_schema_recursive

load_dotenv()
app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # or "*" to allow any origin
  allow_methods=["GET","POST","PUT","DELETE","OPTIONS"],
  allow_headers=["*"],
)

security = HTTPBearer()

def verify_bearer(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    expected = os.getenv("BEARER_TOKEN")
    if not expected or expected not in token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing Bearer Token"
        )
class ExpressionList(BaseModel):
    expressions: list[str]
@app.post("/get-expression", dependencies=[Depends(verify_bearer)])
def get_expression(expressions_request: ExpressionList):
    print("Hello client")
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=12000,
        temperature=1,
        system="Eres un doctor en matemáticas, especialista en encontrar relaciones que tienen los conceptos matemáticos entré sí. Vas a recibir un expresión matemáticas o lógicas escritas en TeX. Quiero saber en qué se relaciona cada relación con diferentes conceptos. Contesta preguntas para cada expresión como 'se resuelve con', 'es una instancia de', 'es caso particular de', 'es equivalente a', 'tiene aplicación en'. Siempre incluye en tu respuesta 'se demuestra con', para resolver la demostración escribe una lista de expresiones necesarias para demostrarla. Todas las expresiones siguen la misma estructura, hasta que se pueden llegar hasta los axiomas. Es decir, cada expresión con la que se demuestra contesta en sí 'es una instancia de', 'se demuestra con', etc en forma de árbol. Las hojas del árbol acaban cuando se llega a un axioma. Usa el tool 'analyze_mathematical_concept' to express the answer, asegúrate de seguir el schema al pie de la letra",
        thinking={
            "type": "enabled",
            "budget_tokens": 5000
        },
        tools=[
            answer_schema_recursive
        ], 
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": expressions_request.expressions[-1]
                    }
                ]
            }
        ]
    )
    print(message.content[-1].input)
    return {
        "response": message.content[-1].input
    }
