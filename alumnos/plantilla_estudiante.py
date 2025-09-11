"""
Plantilla para estudiantes.

Instrucciones:
1) Cambia los valores de NAME y ROLE por los tuyos.
2) Guarda el archivo.
3) Ejecuta: python plantilla_estudiante.py (opcional, para probar).
"""

NAME = ""
ROLE = ""


def presentacion(name: str = NAME, role: str = ROLE) -> str:
    """Devuelve un saludo breve usando name y role."""
    return f"Hola, soy {name} y me dedico a {role}."


if __name__ == "__main__":
    print(presentacion())