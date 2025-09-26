import streamlit as st
from twilio.rest import Client

st.set_page_config(page_title="Twilio Caller", page_icon="📞", layout="centered")
st.title("📞 Make a Call, Send SMS & WhatsApp with Twilio")

# Load secrets
account_sid = st.secrets["account_sid"]
auth_token = st.secrets["auth_token"]
client = Client(account_sid, auth_token)

# Tabs
tab1, tab2, tab3 = st.tabs(["📞 CALL", "💬 TEXT", "🟢 WHATSAPP"])

# --- CALL TAB ---
with tab1:
    to_number = st.text_input("Enter recipient number (with country code):", "+234")
    message = st.text_input("What should Twilio say?")
    if st.button("📞 Call Now"):
        if not to_number.strip() or not message.strip():
            st.error("⚠️ Please provide both a phone number and a message.")
        else:
            call = client.calls.create(
                twiml=f"<Response><Say>{message}</Say></Response>",
                to=to_number,
                from_=st.secrets["from"]  # Your Twilio number
            )
            st.success(f"✅ Call initiated! Call SID: {call.sid}")

# --- SMS TAB ---
with tab2:
    body1 = st.text_input("Enter a message to send via SMS")
    sms_number = st.text_input("Enter recipient phone number:", "+2347065749325")

    if st.button("📩 Send SMS"):
        if not body1.strip() or not sms_number.strip():
            st.error("⚠️ Please enter both number and message.")
        else:
            message = client.messages.create(
                from_=st.secrets["from"],
                body=body1,
                to=sms_number
            )
            st.success(f"✅ SMS sent successfully! SID: {message.sid}")

# --- WHATSAPP TAB ---
with tab3:
    twilio_whatsapp = "whatsapp:+19564460310"  # Twilio Sandbox number
    my_number = st.text_input("Enter your WhatsApp number:", "whatsapp:+2347065749325")
    ms = st.text_area("Enter WhatsApp message:")

    if st.button("🟢 Send WhatsApp Message"):
        if not ms.strip() or not my_number.strip():
            st.error("⚠️ Please enter both number and message.")
        else:
            message = client.messages.create(
                body=ms,
                from_=twilio_whatsapp,
                to=my_number
            )
            st.success(f"✅ WhatsApp message sent! SID: {message.sid}")
