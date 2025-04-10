# 📢 Telegram Mass DM Bot (Python + Telethon)

This Telegram Mass DM Bot allows you to automatically send custom messages to a list of usernames via Telegram using your own Telegram account (session login). It also tracks which usernames have already been messaged to avoid duplication.

Built using **Python** and **Telethon**, this tool is ideal for automated messaging and community outreach (on a small or controlled scale).


---

## 📄 File Details

### ✅ `message.txt`
Write the message you want to send in this file.

Example:
```
Hey! Hope you're doing well 😊 I’d love to connect with you on Telegram!
```

> Only one message is supported per run.

---

### ✅ `target_usernames.txt`
Paste the Telegram usernames (without `@`) of the people you want to message — **one per line**.

Example:
```
user1
user2
user3
```

---

### ✅ `sent_usernames.txt`
You **don’t need to create this manually**.  
Once the bot sends a message to a user, it will **automatically store the username here** to avoid re-sending.

Example after the script runs:
```
user1
user2
```

---

## 🧰 Requirements

Install required packages using:

```bash
pip install -r requirements.txt
```

### Sample `requirements.txt`:
```
telethon
```

You must also have:
- A Telegram account
- Telegram API ID and API Hash from [https://my.telegram.org](https://my.telegram.org)

---

## 🔐 First-Time Setup

When you run the script for the first time, you'll be asked to:
1. Enter your **API ID** and **API Hash**
2. Enter the **phone number** linked to your Telegram account
3. Enter the **OTP code** sent to your Telegram

After that, your session will be saved automatically (you won’t be asked again).

---

## 🚀 How to Run the Bot

```bash
python main.py
```

The bot will:
- Read your message from `message.txt`
- Load usernames from `target_usernames.txt`
- Send your message to each user (one by one)
- Skip any user already listed in `sent_usernames.txt`
- Update `sent_usernames.txt` after every successful message

---

## ⚠️ Important Notes

- ❗ Do not abuse Telegram automation. Only use on a **small, tested group**.
- ❗ Avoid messaging unknown users at scale — Telegram can **restrict or ban your account**.
- ✅ This bot is built for testing, learning, and responsible communication.

---

## ⚠️ Disclaimer

> This project is for **educational purposes only**.  
> Please **do not misuse** this script for spam or harassment.  
> By using this tool, you agree that:
> - You take full responsibility for your actions  
> - You understand the risks of account bans, limitations, or legal issues  
> - **I, Junaid Mansoori, am not responsible** for any misuse, suspension, or damage caused

---
