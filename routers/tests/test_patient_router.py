from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_patient():
    response = client.post("/patients", json={
  "name": "Jully",
  "age": "34",
  "sex": "Female",
  "weight": "50",
  "height": "20",
  "phone": "09042424213"
})    
    assert response.status_code == 201
    assert response.json().get("data").get("phone") == "09042424213"

def test_get_all_patients():
    response = client.get("/patients")
    assert response.status_code == 200
    assert len(response.json().get("data")) == 3

def test_get_student():
    response = client.get("/patients/3")
    assert response.status_code == 200 

def test_get_student_not_found():
    response = client.get("/patients/4")
    assert response.status_code == 404

def test_update_patient():
    response = client.put("/patients/2", json={
  "name": "Perry",
  "age": "34",
  "sex": "Male",
  "weight": "53",
  "height": "22",
  "phone": "0908935835"
})

    assert response.status_code == 200
    assert response.json().get("data").get("phone") == "0908935835"

def test_update_patient_not_found():
    response = client.put("/patients/4", json={
  "name": "Perry",
  "age": "34",
  "sex": "Male",
  "weight": "53",
  "height": "22",
  "phone": "0908935835"
})
    assert response.status_code == 404
    assert response.json() == {"detail": "patient not found"}

def test_delete_patient():
    response = client.delete("/patients/1")
    assert response.status_code == 204

def test_delete_patient_not_found():
    response = client.delete("/patients/5")
    assert response.status_code == 404
    assert response.json() == {"detail": "patient not found"}
    