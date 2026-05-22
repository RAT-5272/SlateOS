import requests

BaseUrl = "http://wiki.velkonianfederation.uk"
UserId = """User1"""


def SendMessage(To, Message):
    return requests.post(
        f"{BaseUrl}/API/SlateOSMessaging/Send",
        json={
            "From": UserId,
            "To": To,
            "Message": Message
        }
    ).json()


def GetMessageHistory(OtherUser):
    return requests.get(
        f"{BaseUrl}/API/SlateOSMessaging/History/{OtherUser}",
        params={"User": UserId}
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
    #print("\nSending message to User2...")
    #SendMessage("User2", "Hello, User2!")
    #print("\nMessage History with User2 after sending message:")
    #print(GetMessageHistory("User2"))