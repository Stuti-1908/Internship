import requests

def test_multiple_quotes():
    for i in range(3):
        response = requests.get("https://dummyjson.com/quotes/random")
        data = response.json()
        print(f"\nQuote {i+1}: {data['quote']}")
        print(f"Author: {data['author']}")
        assert isinstance(data["quote"], str)
        assert isinstance(data["author"], str)

