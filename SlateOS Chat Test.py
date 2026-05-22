import requests
import time
import random

BaseUrl = "http://localhost:3001"
UserId = "User1"

def SafeRequest(Response):
    try:
        return Response.json()
    except:
        print("Non-JSON response received:")
        print(Response.status_code)
        print(Response.text[:300])
        return None

def SendMessage(To, Message):
    try:
        Response = requests.post(
            f"{BaseUrl}/API/SlateOSMessaging/Send",
            headers={
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "From": UserId,
                "To": To,
                "Message": Message
            },
            timeout=10
        )
        return SafeRequest(Response)

    except:
        print("POST failed, trying GET...")

        Response = requests.get(
            f"{BaseUrl}/API/SlateOSMessaging/Send",
            params={
                "From": UserId,
                "To": To,
                "Message": Message,
                "t": int(time.time() * 1000)
            },
            headers={
                "Cache-Control": "no-cache",
                "Pragma": "no-cache"
            },
            timeout=10
        )

        return SafeRequest(Response)


def GetMessageHistory(OtherUser):
    return requests.get(
        f"{BaseUrl}/API/SlateOSMessaging/History/{OtherUser}",
        params={
            "User": UserId
        }
    ).json()


def GetConversationList():
    return requests.get(
        f"{BaseUrl}/API/SlateOSMessaging/Conversations/{UserId}"
    ).json()


if __name__ == "__main__":
    print("Conversation List:")
    print(GetConversationList())
    print("\n\nMessage History with User2:")
    print(GetMessageHistory("User2"))

    print("\nSending message to User2...")
    SendMessage("User2", "Hello, User2!")
    print("\nMessage History with User2 after sending message:")
    print(GetMessageHistory("User2"))