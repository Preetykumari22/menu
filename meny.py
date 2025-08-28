import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import requests
import tweepy


# ---------------- EMAIL ----------------
def send_email():
    sender = "preetyprincess2212@gmail.com"
    receiver = "preety04fe@gmail.com"
    password = "Preety1234@"

    msg = MIMEText("Hello! This is a test email sent from Python.")
    msg["Subject"] = "Python Email"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print(" Email sent successfully!")
    except Exception as e:
        print(" Error:", e)


# ---------------- SMS ----------------
def send_sms():
    account_sid = "AC844e4e18de113b549745e761930e0f83"
    auth_token = "0474d1a5fea2db8386bc42a7699e8e99"
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body="Hello! This is a test SMS from Python.",
            from_="+1234567890",  # Twilio number
            to="+918709554389"
        )
        print(" SMS sent successfully:", message.sid)
    except Exception as e:
        print(" Error:", e)


# ---------------- PHONE CALL ----------------
def make_call():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    call = client.calls.create(
    twiml='<Response><Say>Hello, this is a test call from Twilio!</Say></Response>',
    from_='+1 205 405 9248',
    to='+918709554389'
        
    print(call.sid)
    print("calling....")
    


# ---------------- LINKEDIN ----------------
def post_linkedin():
    access_token = "hjfgdfchghvjkhljhghf"
    api_url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    post_data = {
        "author": "urn:li:person:your_linkedin_id",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "Hello, posting on LinkedIn via Python!"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    try:
        response = requests.post(api_url, headers=headers, json=post_data)
        print(" LinkedIn Post response:", response.json())
    except Exception as e:
        print(" Error:", e)


# ---------------- TWITTER ----------------
def post_twitter():
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    access_token = "your_access_token"
    access_secret = "your_access_secret"

    try:
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        api = tweepy.API(auth)
        api.update_status("Hello from Python! #Python #TwitterAPI")
        print(" Tweet posted successfully!")
    except Exception as e:
        print(" Error:", e)


# ---------------- FACEBOOK ----------------
def post_facebook():
    page_access_token = "your_page_access_token"
    page_id = "your_page_id"
    message = "Hello! Posting on Facebook using Python."

    url = f"https://graph.facebook.com/{page_id}/feed"
    payload = {"message": message, "access_token": page_access_token}

    try:
        response = requests.post(url, data=payload)
        print(" Facebook Post response:", response.json())
    except Exception as e:
        print(" Error:", e)


# ---------------- INSTAGRAM ----------------
def insta():
    USERNAME = 'cloud.learner'
    PASSWORD = 'Preety@123'
    IMAGE_PATH = r'C:\Users\HP\Downloads\world.jpeg'
    CAPTION = 'I posted this image using python'

    cl = Client()

    # Login to Instagram
    print("Logging in to Instagram...")
    try:
        cl.login(USERNAME, PASSWORD)
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # Try uploading the photo with retries in case of errors
    max_retries = 5
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            # Post the image with a caption
            print("Uploading photo to Instagram...")
            media = cl.photo_upload(IMAGE_PATH, CAPTION)
            print("Photo uploaded successfully.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Photo upload failed.")

    # Logout from Instagram
    cl.logout()
    print("Logged out from Instagram.")


# ---------------- WHATSAPP ----------------
def whatsapp():
    account_sid = 'AC844e4e18de113b549745e761930e0f83'
    auth_token = '0474d1a5fea2db8386bc42a7699e8e99'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='Hello preety',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918709554389'
)

    print(message.sid)
    print("message sent successfully!!")


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n--- Python Automation Menu ---")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Make Phone Call")
        print("4. Post on LinkedIn")
        print("5. Post on Twitter")
        print("6. Post on Facebook")
        print("7. Post on Instagram")
        print("8. Send WhatsApp Message")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_email()
        elif choice == "2":
            send_sms()
        elif choice == "3":
            make_call()
        elif choice == "4":
            post_linkedin()
        elif choice == "5":
            post_twitter()
        elif choice == "6":
            post_facebook()
        elif choice == "7":
            post_instagram()
        elif choice == "8":
            send_whatsapp()
        elif choice == "9":
            print("Exiting... ")
            break
        else:
            print(" Invalid choice, try again.")


# Run the menu
if __name__ == "__main__":
    menu()
