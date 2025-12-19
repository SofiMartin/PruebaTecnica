# Prueba Técnica - APIs REST con Flask y Docker

Este proyecto implementa dos APIs REST independientes usando Flask que se comunican entre sí vía HTTP, desplegadas usando Docker Compose en una red compartida.

## Estructura del Proyecto

```
Prueba Tecnica/
├── api_a/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── api_b/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## Descripción de las APIs

### API B (Puerto 5001)

**Endpoints:**

1. `GET /status`
   - Responde con JSON indicando que el servicio está activo
   - Ejemplo de respuesta:
   ```json
   {
     "status": "active",
     "service": "API B",
     "timestamp": "2024-12-18T17:00:00.000000"
   }
   ```

2. `POST /process`
   - Recibe JSON con un campo `value` (número o texto)
   - Procesa el valor:
     - Si es número: devuelve el doble
     - Si es texto: devuelve la longitud
   - Request:
   ```json
   {
     "value": 10
   }
   ```
   - Response:
   ```json
   {
     "original_value": 10,
     "processed_result": 20,
     "request_id": "550e8400-e29b-41d4-a716-446655440000",
     "timestamp": "2024-12-18T17:00:00.000000"
   }
   ```

### API A (Puerto 5000)

**Endpoints:**

1. `GET /status`
   - Responde con JSON indicando que el servicio está activo
   - Ejemplo de respuesta:
   ```json
   {
     "status": "active",
     "service": "API A",
     "timestamp": "2024-12-18T17:00:00.000000"
   }
   ```

2. `POST /request-process`
   - Recibe JSON con un campo `value`
   - Envía el JSON a API B `/process`
   - Devuelve la respuesta combinada
   - Request:
   ```json
   {
     "value": "hello"
   }
   ```
   - Response:
   ```json
   {
     "original_data": {
       "value": "hello"
     },
     "api_b_response": {
       "original_value": "hello",
       "processed_result": 5,
       "request_id": "550e8400-e29b-41d4-a716-446655440000",
       "timestamp": "2024-12-18T17:00:00.000000"
     },
     "message": "procesado correctamente",
     "timestamp": "2024-12-18T17:00:00.000000"
   }
   ```

## Manejo de Errores

API A maneja los siguientes errores de comunicación con API B:

- **502 Bad Gateway**: Cuando API B no responde, devuelve error, o hay timeout
- **500 Internal Server Error**: Para errores internos de la API

Ejemplo de respuesta de error:
```json
{
  "error": "Cannot connect to API B",
  "details": "API B is not available or not responding"
}
```

## Despliegue con Docker

### Requisitos Previos

- Docker instalado
- Docker Compose instalado

### Comandos para Ejecutar

1. **Construir y levantar los contenedores:**
   ```bash
   docker-compose up --build
   ```

2. **Levantar en modo detached (background):**
   ```bash
   docker-compose up -d
   ```

3. **Ver logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Detener los contenedores:**
   ```bash
   docker-compose down
   ```

### Red Docker

Ambas APIs se ejecutan en una red compartida llamada `api_network`, lo que permite la comunicación entre contenedores usando los nombres de servicio como hostnames.

## Pruebas con cURL

### Probar API B directamente:

```bash
# Status
curl http://localhost:5001/status

# Process con número
curl -X POST http://localhost:5001/process \
  -H "Content-Type: application/json" \
  -d "{\"value\": 15}"

# Process con texto
curl -X POST http://localhost:5001/process \
  -H "Content-Type: application/json" \
  -d "{\"value\": \"hola mundo\"}"
```

### Probar API A (que se comunica con API B):

```bash
# Status
curl http://localhost:5000/status

# Request-process con número
curl -X POST http://localhost:5000/request-process \
  -H "Content-Type: application/json" \
  -d "{\"value\": 25}"

# Request-process con texto
curl -X POST http://localhost:5000/request-process \
  -H "Content-Type: application/json" \
  -d "{\"value\": \"prueba tecnica\"}"
```

## Flujo de Comunicación

```
Usuario → API A (/request-process) → API B (/process) → API A → Usuario
```

1. El usuario envía una petición a API A
2. API A recibe la petición y la reenvía a API B
3. API B procesa el valor y responde a API A
4. API A combina los datos y responde al usuario

## Tecnologías Utilizadas

- **Python 3.11**
- **Flask 3.0.0**: Framework web
- **Requests 2.31.0**: Cliente HTTP para comunicación entre APIs
- **Docker**: Containerización
- **Docker Compose**: Orquestación de contenedores
