import requests
import json

print("=" * 60)
print("PROBANDO LAS APIs")
print("=" * 60)

# Test 1: Status de API A
print("\n1. GET /status en API A:")
response = requests.get("http://localhost:5000/status")
print(f"   Status Code: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}")

# Test 2: Status de API B
print("\n2. GET /status en API B:")
response = requests.get("http://localhost:5001/status")
print(f"   Status Code: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}")

# Test 3: Procesar número en API A (que llama a API B)
print("\n3. POST /request-process con número (25):")
response = requests.post(
    "http://localhost:5000/request-process",
    json={"value": 25}
)
print(f"   Status Code: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}")

# Test 4: Procesar texto en API A (que llama a API B)
print("\n4. POST /request-process con texto ('hola mundo'):")
response = requests.post(
    "http://localhost:5000/request-process",
    json={"value": "hola mundo"}
)
print(f"   Status Code: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}")

# Test 5: Procesar directamente en API B (número)
print("\n5. POST /process directo en API B con número (100):")
response = requests.post(
    "http://localhost:5001/process",
    json={"value": 100}
)
print(f"   Status Code: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}")

# Test 6: Procesar directamente en API B (texto)
print("\n6. POST /process directo en API B con texto ('prueba tecnica'):")
response = requests.post(
    "http://localhost:5001/process",
    json={"value": "prueba tecnica"}
)
print(f"   Status Code: {response.status_code}")
print(f"   Response: {json.dumps(response.json(), indent=2)}")

print("\n" + "=" * 60)
print("TODAS LAS PRUEBAS COMPLETADAS")
print("=" * 60)
