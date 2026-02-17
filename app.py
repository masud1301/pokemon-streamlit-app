import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---- Full Dynamic Background Styling ----
st.markdown(
    """
    <style>
    /* Dynamic Background Animation Setup */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Apply the animated gradient to the app */
    .stApp {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #e73c7e, #23a6d5, #0f2027);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        background-attachment: fixed;
    }

    /* Dark overlay to make text readable */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.45);
        z-index: -1;
    }

    /* Make all text white with a shadow for better visibility */
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
        text-shadow: 2px 2px 5px black;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #00bcd4;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
    }

    /* Input Box Styling */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.6);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Load CSV Once ----
df = pd.read_csv("pokemon_50.csv")

# ---- Main Title ----
st.title("🤖 Ollama Chatbot Demo")

# ---- Greeting Section ----
name = st.text_input("What is your name?", key="name1")

if st.button("Submit", key="submit1"):
    st.success(f"Hello {name}, how can I assist you today?")

# ---- Dataset Section ----
st.write("📂 Pokemon Dataset")
st.dataframe(df)

# ---- Charts Section ----
st.subheader("📊 Stats Line Chart")

df_chart = df.set_index("Name")
st.line_chart(df_chart[["HP", "Attack", "Defense", "Speed"]])

st.subheader("📊 Attack Comparison (Top 10 Pokemon)")

top_attack = df.sort_values(by="Attack", ascending=False).head(10)
st.bar_chart(top_attack.set_index("Name")["Attack"])

# ---- Sidebar ----
st.sidebar.header("Media Examples")
st.sidebar.image("greninja.jpg", caption="Greninja")
st.sidebar.video("https://youtu.be/Ued_bez_BMw?t=8")

# ---- Markdown & Code Demo ----
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is **bold** text, this is *italic* text, [Link](http://streamlit.io).")
st.code("for i in range(5):\n    print(i)", language='python')

# ---- Input Section ----
st.subheader("📝 User Form")

user_name = st.text_input("Enter your name:", key="name2")
st.text_area("Tell us about yourself:", key="about")
st.number_input("Enter your age:", min_value=0, max_value=120, value=25, key="age")
st.slider("Choose your favorite number:", min_value=0, max_value=100, value=50, key="slider")

st.selectbox("Choose your favorite Pokemon:", options=df["Name"], key="pokemon_select")
st.multiselect("Select your favorite types:", options=df["Type"].unique(), key="type_multi")

st.checkbox("I agree to the terms and conditions", key="terms")

if st.button("Final Submit", key="submit2"):
    st.success("Form submitted successfully!")

    # Selected Pokemon ka data nikaalo
    selected_pokemon = st.session_state["pokemon_select"]
    pokemon_data = df[df["Name"] == selected_pokemon].iloc[0]

    st.subheader(f"📋 Details of {selected_pokemon}")

    st.write(f"**Type:** {pokemon_data['Type']}")
    st.write(f"**HP:** {pokemon_data['HP']}")
    st.write(f"**Attack:** {pokemon_data['Attack']}")
    st.write(f"**Defense:** {pokemon_data['Defense']}")
    st.write(f"**Sp. Attack:** {pokemon_data['Sp_Atk']}")
    st.write(f"**Sp. Defense:** {pokemon_data['Sp_Def']}")
    st.write(f"**Speed:** {pokemon_data['Speed']}")

# ---- Matplotlib Section ----
st.subheader("📈 Matplotlib Scatter Plot")
fig, ax = plt.subplots()

# Making Matplotlib background transparent to match Streamlit's dynamic background
fig.patch.set_alpha(0.0) 
ax.patch.set_alpha(0.0)

# Changing tick colors so they are visible against the dark/colored background
ax.tick_params(colors='white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')

ax.plot(df["HP"], df["Attack"], 'o', color='#00bcd4')
ax.set_xlabel("HP")
ax.set_ylabel("Attack")

st.pyplot(fig)