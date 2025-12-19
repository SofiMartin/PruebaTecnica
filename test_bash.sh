#!/bin/bash

echo "============================================================"
echo "PROBANDO LAS APIs CON CURL"
echo "============================================================"

echo ""
echo "1. GET /status en API A:"
curl -s http://localhost:5000/status | jq . 2>/dev/null || curl -s http://localhost:5000/status

echo ""
echo "2. GET /status en API B:"
curl -s http://localhost:5001/status | jq . 2>/dev/null || curl -s http://localhost:5001/status

echo ""
echo "3. POST /request-process con número (25):"
curl -s -X POST http://localhost:5000/request-process \
  -H "Content-Type: application/json" \
  -d '{"value": 25}' | jq . 2>/dev/null || curl -s -X POST http://localhost:5000/request-process \
  -H "Content-Type: application/json" \
  -d '{"value": 25}'

echo ""
echo "4. POST /request-process con texto ('hola mundo'):"
curl -s -X POST http://localhost:5000/request-process \
  -H "Content-Type: application/json" \
  -d '{"value": "hola mundo"}' | jq . 2>/dev/null || curl -s -X POST http://localhost:5000/request-process \
  -H "Content-Type: application/json" \
  -d '{"value": "hola mundo"}'

echo ""
echo "5. POST /process directo en API B con número (100):"
curl -s -X POST http://localhost:5001/process \
  -H "Content-Type: application/json" \
  -d '{"value": 100}' | jq . 2>/dev/null || curl -s -X POST http://localhost:5001/process \
  -H "Content-Type: application/json" \
  -d '{"value": 100}'

echo ""
echo "6. POST /process directo en API B con texto ('prueba tecnica'):"
curl -s -X POST http://localhost:5001/process \
  -H "Content-Type: application/json" \
  -d '{"value": "prueba tecnica"}' | jq . 2>/dev/null || curl -s -X POST http://localhost:5001/process \
  -H "Content-Type: application/json" \
  -d '{"value": "prueba tecnica"}'

echo ""
echo "============================================================"
echo "TODAS LAS PRUEBAS COMPLETADAS"
echo "============================================================"
