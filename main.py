import streamlit as st
import pandas as pd
import plotly.express as px

# Set up page title and layout
st.set_page_config(page_title="Virtual Herbal Garden", layout="wide")

# Title and introduction
st.title("🌿 Virtual Herbal Garden")
st.header("Explore the World of Medicinal Plants from AYUSH (Ayurveda, Unani, Siddha, Homeopathy)")
st.markdown("Discover the **healing power** of nature as you explore plants used in traditional healing systems. "
            "Learn about their benefits, usage, and where to find them!")

# Displaying an image of a herbal garden
st.image('ink painting.webp', caption='A glimpse of the Virtual Herbal Garden', use_column_width=True)

# Sidebar navigation
st.sidebar.title("Explore by Category")
option = st.sidebar.selectbox("Choose a healing tradition", ["Ayurveda", "Unani", "Siddha", "Homeopathy"])

# Function to display plant details based on the selected category
def display_plants(category):
    if category == "Ayurveda":
        plants = {'Plant Name': ['Tulsi', 'Ashwagandha', 'Brahmi'],
                  'Scientific Name': ['Ocimum tenuiflorum', 'Withania somnifera', 'Bacopa monnieri'],
                  'Medicinal Uses': ['Anti-inflammatory', 'Adaptogen, Anti-stress', 'Memory enhancer']}
    elif category == "Unani":
        plants = {'Plant Name': ['Ajwain', 'Neem', 'Henna'],
                  'Scientific Name': ['Trachyspermum ammi', 'Azadirachta indica', 'Lawsonia inermis'],
                  'Medicinal Uses': ['Digestive aid', 'Antibacterial', 'Antifungal']}
    elif category == "Siddha":
        plants = {'Plant Name': ['Aloe Vera', 'Neem', 'Thuthuvalai'],
                  'Scientific Name': ['Aloe barbadensis', 'Azadirachta indica', 'Solanum trilobatum'],
                  'Medicinal Uses': ['Skin healing', 'Antibacterial', 'Anti-asthmatic']}
    else:
        plants = {'Plant Name': ['Arnica', 'Belladonna', 'Nux Vomica'],
                  'Scientific Name': ['Arnica montana', 'Atropa belladonna', 'Strychnos nux-vomica'],
                  'Medicinal Uses': ['Pain relief', 'Fever reducer', 'Digestive aid']}

    df = pd.DataFrame(plants)
    st.table(df)

# Show the relevant plants for the chosen category
display_plants(option)

# Search feature
search = st.text_input("Search for a medicinal plant by name or property")
if search:
    st.write(f"Results for: {search}")
    # You could implement further search logic here

# Interactive map of medicinal plant gardens
st.header("Medicinal Plant Gardens Around the World 🌍")
st.markdown("Discover where medicinal plants are cultivated and preserved.")
garden_locations = pd.DataFrame({
    'lat': [28.7041, 15.3173, 19.0760], 
    'lon': [77.1025, 75.7139, 72.8777],
    'location': ['New Delhi, India', 'Pondicherry, India', 'Mumbai, India']
})
st.map(garden_locations)

# Plant information with images and columns layout
st.header("Explore Popular Medicinal Plants")
st.markdown("Here are some widely used medicinal plants and their benefits.")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("tulsi.jpg", caption="Tulsi", use_column_width=True)
    st.write("**Tulsi (Ocimum tenuiflorum)**: Anti-inflammatory, boosts immunity")
with col2:
    st.image("ashwagandha.jpg", caption="Ashwagandha", use_column_width=True)
    st.write("**Ashwagandha (Withania somnifera)**: Reduces stress, improves vitality")
with col3:
    st.image("neem.jpg", caption="Neem", use_column_width=True)
    st.write("**Neem (Azadirachta indica)**: Antibacterial, purifies the blood")

# Plotting medicinal properties comparison
st.header("Medicinal Properties of Key Plants")
df = pd.DataFrame({
    'Plant': ['Tulsi', 'Neem', 'Ashwagandha'],
    'Anti-inflammatory': [4, 5, 3],
    'Antibacterial': [2, 5, 1],
    'Stress-relief': [1, 1, 5]
})
fig = px.bar(df, x='Plant', y=['Anti-inflammatory', 'Antibacterial', 'Stress-relief'],
             title="Medicinal Properties of Selected Plants", barmode='group')
st.plotly_chart(fig)

# Quiz Section: Test your knowledge
st.header("🌿 Take a Quiz: Test Your Herbal Knowledge")
with st.form(key='quiz'):
    q1 = st.radio("Which plant is called the Queen of Herbs?", ["Tulsi", "Ashwagandha", "Neem"])
    q2 = st.radio("Which plant is well known for its antibacterial properties?", ["Tulsi", "Neem", "Aloe Vera"])
    submit = st.form_submit_button("Submit")
    
if submit:
    st.balloons()
    st.write("Your answers have been submitted!")
    st.write("Correct Answer 1: Tulsi")
    st.write("Correct Answer 2: Neem")

# Footer
st.markdown("---")
st.markdown("🌿 **Created by Akshu Grewal** | Powered by Streamlit")


