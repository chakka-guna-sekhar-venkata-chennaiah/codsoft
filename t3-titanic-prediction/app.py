import streamlit as st
import base64
from source.utlis import Pclass_converter, embark_converter
from source.pipelines.testing_pipeline import custom_data,prediction_pipeline 

st.set_page_config(layout="wide",initial_sidebar_state="expanded",
                   page_icon='⛵',page_title='Titanic Survival Prediction')


def get_video_base64(video_path):
    with open(video_path, "rb") as file:
        video_bytes = file.read()
        base64_encoded = base64.b64encode(video_bytes).decode("utf-8")
        return base64_encoded

video_path = "deep.mp4"
video_base64 = get_video_base64(video_path)
video_html = f"""
	<style>
	#myVideo {{
		position: fixed;
		right: 0;
		bottom: 0;
		min-width: 100%; 
		min-height: 100%;
	}}
	.content {{
		position: fixed;
		bottom: 0;
		background: rgba(0, 0, 0, 0.5);
		color: #f1f1f1;
		width: 100%;
		padding: 20px;
	}}

	</style>

	<video autoplay loop muted id="myVideo">
		<source type="video/mp4" src="data:video/mp4;base64,{video_base64}">
	</video>
"""

st.markdown(video_html, unsafe_allow_html=True)

# Define custom style for the glowing text
glowing_text_style = '''
    <style>
        .glowing-text {
            font-family: 'Arial Black', sans-serif;
            font-size: 48px;
            text-align: center;
            animation: glowing 2s infinite;
        }
        
        @keyframes glowing {
            0% { color: #FF9933; } /* Saffron color */
            25% { color: #FFFFFF; } /* White color */
            50% { color: #128807; } /* Green color */
            75% { color: #0000FF; } /* Blue color */
            100% { color: #FF9933; } /* Saffron color */
        }
    </style>
'''

# Display the glowing text using st.markdown
st.markdown(glowing_text_style, unsafe_allow_html=True)
st.markdown(f'<p class="glowing-text">⛵ Titanic Survival Prediction ⛵</p>', unsafe_allow_html=True)


st.image("static/boat.jpeg", use_column_width=True)






st.subheader('Fill the Form 📄')

Pclass=st.selectbox('Choose the passenger class:',['first-class','second-class','third-class'])
Pclass=Pclass_converter(Pclass)
Sex=st.selectbox('Choose the passenger gender:',['male','female'])
Age=st.number_input("Enter the passenger's age:")
Sibsip=st.number_input('How many siblings/spouses does passenger have?')
Parch=st.number_input('How many children/parents does passenger have?')
Fare=st.number_input("Enter the passenger's fare:")
Embarked=st.selectbox('Choose the passenger embarkation',['Cherbourg','Queenstown','Southampton'])
Embarked=embark_converter(Embarked)

data=custom_data(Pclass,Sex,Age,Sibsip,Parch,Fare,Embarked)
pred_df=data.get_data_as_a_dataframe()

pred_pipe=prediction_pipeline()
final_pred=pred_pipe.predict(pred_df)

if st.button('Predict'):
    if final_pred[0]==0:
       
        st.image('static/notsurvived.jpeg')
    elif final_pred[0]==1:
        
        st.image('static/survived.png')
    st.write("""
    ---\n
    Made with ❤️ by Chakka Guna Sekhar Venkata Chennaiah.
    """)
