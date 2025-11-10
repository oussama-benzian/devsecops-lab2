import pytest
from app.app import app

@pytest.fixture
def client():
    """Test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Welcome to DevSecOps Lab2 Flask Application"
    assert data['status'] == "running"
    assert 'version' in data

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"

def test_get_users(client):
    """Test the get users endpoint"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['name'] == "John Doe"
    assert data[1]['email'] == "jane@example.com"

def test_admin_login_success(client):
    """Test successful admin login"""
    response = client.post('/api/admin/login', json={'password': 'admin123'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Login successful"
    assert 'token' in data
    assert data['user'] == "admin"

def test_admin_login_failure(client):
    """Test failed admin login"""
    response = client.post('/api/admin/login', json={'password': 'wrongpassword'})
    assert response.status_code == 401
    data = response.get_json()
    assert data['error'] == "Invalid password"

def test_admin_login_no_password(client):
    """Test admin login without password"""
    response = client.post('/api/admin/login', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == "Password required"

def test_calculate_endpoint(client):
    """Test the calculate endpoint"""
    response = client.get('/api/calculate/5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['input'] == 5
    assert data['result'] == 20  # 5 * 2 + 10 = 20
    assert data['formula'] == "number * 2 + 10"

def test_calculate_endpoint_large_number(client):
    """Test the calculate endpoint with a large number"""
    response = client.get('/api/calculate/100')
    assert response.status_code == 200
    data = response.get_json()
    assert data['input'] == 100
    assert data['result'] == 210  # 100 * 2 + 10 = 210
