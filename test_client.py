import requests


BASE_URL = "http://127.0.0.1:8015"


def test_chat():

    payload = {
        "question": "Why is furniture making loss?"
    }

    res = requests.post(
        f"{BASE_URL}/ai-chat",
        json=payload
    )

    print("Status:", res.status_code)
    print("Response:")
    print(res.json())


if __name__ == "__main__":

    test_chat()
