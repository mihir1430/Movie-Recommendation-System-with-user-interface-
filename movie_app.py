import streamlit as st
import pickle
import base64

# Load movie data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found. Please try another title."]
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommendations

# Function to encode the image in Base64
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    return encoded_img

# Apply background image
def set_background(image_path):
    encoded_img = get_base64_encoded_image(image_path)
    bg_css = f"""
    <style>
        .stApp {{
            background: url("data:image/jpeg;base64,{encoded_img}") no-repeat center center fixed;
            background-size: cover;
        }}
        .movie-title {{
            font-size: 22px;
            font-weight: bold;
            color: white;
            text-align: center;
        }}
        .input-label {{
            font-size: 18px;
            font-weight: bold;
            color: white;
        }}
        .stTextInput {{
            font-size: 16px;
            color: black;
        }}
        .recommend-btn {{
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 8px 16px;
            border: none;
        }}
        .recommend-btn:hover {{
            background-color: #e63946;
        }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Set the background image
set_background(r"D:\jupyter_env\Scripts\movie app bg image.jpg")

# Streamlit UI
st.markdown("<h1 class='movie-title' style='color:yellow;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)

# Input field
st.markdown("<label class='input-label' style='color:yellow; font-weight:bold;'>Enter a movie name:</label>", unsafe_allow_html=True)
movie_name = st.text_input("", key="movie_input", placeholder="Type a movie name here")

# Recommend button
if st.button("Recommend", key="recommend_btn"):
    recommendations = recommend(movie_name)

    st.markdown("<h3 style='color:yellow;'>Recommended Movies:</h3>", unsafe_allow_html=True)
    for rec in recommendations:
        st.markdown(f"<li style='color:white;'>✅ {rec}</li>", unsafe_allow_html=True)
