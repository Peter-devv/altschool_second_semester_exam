from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_doctor():
   response = client.post("/doctors", json={"name": "Dr. Grace", "specialization": "Surgeon", "phone": "07042488722", "is_available": "False"})
   assert response.status_code == 201 
   assert response.json().get("data").get("phone") == "07042488722"

def test_get_all_doctors():
   response = client.get("/doctors")
   assert response.status_code == 200
   assert len(response.json().get("data")) == 3

def test_get_doctor():
   response = client.get("/doctors/2")
   assert response.status_code == 200

def test_get_doctor_not_found():
   response = client.get("/doctors/5")
   assert response.status_code == 404

def test_update_doctor():
   response = client.put("/doctors/1", json={"name": "Dr. Jamie", "specialization": "Optometrist", "phone": "08063526221", "is_available": "False"})
   assert response.status_code == 200
   assert response.json().get("data").get("phone") == "08063526221"

def test_update_doctor_not_found():
   response = client.put("/doctors/5", json={"name": "Dr. Jamie", "specialization": "Optometrist", "phone": "08063526221", "is_available": "False"}) 
   assert response.status_code == 404
   assert response.json() == {"detail": "doctor not found"}

def test_delete_doctor():
   response = client.delete("/doctors/2")
   assert response.status_code == 204

def test_delete_doctor_not_found():
   response = client.delete("/doctors/5")
   assert response.status_code == 404
   assert response.json() == {"detail": "doctor not found"}

def test_set_availability_status():
   response = client.put("/doctors/1/set_availability_status")
   assert response.status_code == 200
   assert response.json().get("data").get("is_available") == False