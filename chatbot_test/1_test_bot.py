import requests

def test_chatbot_response():
    url = "https://dummyjson.com/quotes/1"

    response = requests.get(url)
    
    assert response.status_code == 200  
    
    data = response.json()
    print("Bot Response:", data["quote"])
    print("Author:", data["author"])
    assert "quote" in data
    assert isinstance(data["quote"], str)
