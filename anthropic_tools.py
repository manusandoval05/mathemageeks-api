answer_schema = {
    "name": "analyze_mathematical_concept",
    "description": "Analiza conceptos matemáticos y sus relaciones, incluyendo demostraciones y aplicaciones",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "La expresión matemática en formato TeX rodeado del caracter $"
            },
            "name": {
                "type": "string",
                "description": "Nombre de la expresión"
            }, 
            "se_resuelve_con": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Métodos o técnicas para resolver la expresión"
            },
            "es_instancia_de": {
                "type": "array", 
                "items": {"type": "string"},
                "description": "Conceptos generales de los que esta expresión es un ejemplo"
            },
            "es_caso_particular_de": {
                "type": "array",
                "items": {"type": "string"}, 
                "description": "Teoremas o conceptos más generales. Escribe una expresión TeX rodeado del caracter $"
            },
            "es_equivalente_a": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Expresiones matemáticamente equivalentes. Escribe la expresión en TeX"
            },
            "tiene_aplicacion_en": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Áreas donde se aplica este concepto"
            },
            "se_demuestra_con": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string", 
                            "description": "La expresión matemática en formato TeX rodeado del caracter $"
                        },
                        "es_instancia_de": {"type": "array", "items": {"type": "string"}},
                        "se_demuestra_con": {"type": "array", "items": {"type": "string"}},
                        "es_axioma": {"type": "boolean"}
                    },
                    "required": ["expresion"]
                },
                "description": "Estructura de árbol de la demostración hasta llegar a axiomas"
            }
        },
        "required": ["expression", "se_resuelve_con", "es_instancia_de", "se_demuestra_con"]
    }
}

answer_schema_recursive = {
    "name": "analyze_mathematical_concept",
    "description": "Analiza conceptos matemáticos y sus relaciones, incluyendo demostraciones y aplicaciones",
    "input_schema": {
        "type": "object",
        "$id": "mathematical_concept",
        "properties": {
            "expression": {
                "type": "string",
                "description": "La expresión matemática en formato TeX rodeado del caracter $"
            },
             "name": {
                "type": "string",
                "description": "Nombre de la expresión"
            },
            "se_resuelve_con": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Métodos o técnicas para resolver la expresión"
            },
            "es_instancia_de": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Conceptos generales de los que esta expresión es un ejemplo"
            },
            "es_caso_particular_de": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Array de expresiones de teoremas o conceptos más generales. Escribe un arreglo de Strings, donde cada string es un string TeX rodeado del caracter $"
            },
            "es_equivalente_a": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Array de expresiones matemáticamente equivalentes a la expresión original. Escribe la expresión en TeX rodeado del caracter $. Es un arreglo de strings, no un solo string"
            },
            "tiene_aplicacion_en": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Áreas donde se aplica este concepto"
            },
            "se_demuestra_con": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "$ref": "#"  
                        },
                        {
                            "type": "object",
                            "properties": {
                                "expression": {
                                    "type": "string",
                                    "description": "La expresión matemática en formato TeX rodeado del caracter $"
                                },
                                "es_axioma": {
                                    "type": "boolean",
                                    "description": "Indica si esta expresión es un axioma (hoja del árbol)"
                                }
                            },
                            "required": ["expression", "es_axioma"]
                        }
                    ]
                },
                "description": "Estructura de árbol de la demostración hasta llegar a axiomas"
            }
        },
        "required": ["expression", "se_resuelve_con", "es_instancia_de", "se_demuestra_con"]
    }
}

answer_schema_v2 = {
    "name": "analyze_mathematical_concept",
    "description": "Analiza conceptos matemáticos y sus relaciones, incluyendo demostraciones y aplicaciones",
    "input_schema": {
        "type": "object",
        "$id": "mathematical_concept",
        "properties": {
            "expression": {
                "type": "string",
                "description": "La expresión matemática en formato TeX rodeado del caracter $"
            },
            "se_resuelve_con": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Métodos o técnicas para resolver la expresión. Es un arreglo de strings, no un solo string"
            },
            "es_instancia_de": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Conceptos generales de los que esta expresión es un ejemplo"
            },
            "es_caso_particular_de": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Teoremas o conceptos más generales. Escribe todo en TeX rodeado del caracter $. Es un arreglo de strings, no un solo string"
            },
            "es_equivalente_a": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Expresiones matemáticamente equivalentes. Escribe la expresión en TeX rodeado del caracter $"
            },
            "tiene_aplicacion_en": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Áreas donde se aplica este concepto"
            },
            "se_demuestra_con": {
                "type": "array",
                "items": {
                    "$ref": "#"
                },
                "description": "Estructura de árbol de la demostración hasta llegar a axiomas. Si es_axioma es true, este array debe estar vacío. Tiene las mismas llaves que el objeto padre"
            },
            "es_axioma": {
                "type": "boolean",
                "description": "Indica si esta expresión es un axioma (hoja del árbol). Si es true, se_demuestra_con debe estar vacío.",
                "default": False
            }
        },
        "required": ["expression", "se_resuelve_con", "es_instancia_de", "es_axioma"]
    }
}
