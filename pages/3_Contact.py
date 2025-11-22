import streamlit as st

st.title("Contact Me 📩")

# --- LOAD CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.write("I'd love to connect! Whether you have a question, a project idea, or just want to say hi.")

st.write("---")

# --- SOCIAL LINKS ---
st.header("Get in Touch")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📧 Email**")
    st.write("sandipsc6815@gmail.com") # Replace with actual email if desired

with col2:
    st.markdown("**🔗 LinkedIn**")
    st.markdown("https://www.linkedin.com/in/sandip-ahir-a19062277/") # Replace with actual link

with col3:
    st.markdown("**💻 GitHub**")
    st.markdown("https://github.com/sandip9664") # Replace with actual link

st.write("---")

# --- CONTACT FORM ---
st.header("Send a Message")
st.write("Feel free to leave a message below:")

contact_form = """
<form action="https://formsubmit.co/sandipsc6815@gmail.com" method="POST" target="_blank">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Note: For the form to work, you'll need to replace 'YOUR_EMAIL_HERE' with your actual email address.
# FormSubmit is a free service that forwards submissions to your email.
