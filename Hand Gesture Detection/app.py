import streamlit as st
st.sidebar.title('ElevateAI Detection App')
app_mode = st.sidebar.selectbox('Select Page', ['Home', 'NLP Emotion Detection', 'Face Mask Detection', 'Hand Gesture Recognition'])

if app_mode == 'Home':
    st.title('About This Project')
    st.markdown("This is an AI powered app that helps to detect Emotion in texts, faces and face-masks in images and hand gestures especially Hand Sign Language.")

elif app_mode == 'NLP Emotion Detection':
    link = '[NLP Emotion Detection](https://nerry-axl-elevateai-nlp-emo-detection--app-7dd47z.streamlitapp.com/)'
    st.markdown(link, unsafe_allow_html=True)

elif app_mode == 'NLP Emotion Detection':
    link = '[Face Mask Detection](https://nerry-axl-elevateai-face-mask-st-face-mask-detector-expl-q3ecr7.streamlitapp.com/)'
    st.markdown(link, unsafe_allow_html=True)
    
elif app_mode == 'NLP Emotion Detection':
    link = '[Hand Gesture Recognition](https://nerry-axl-elevateai-hand-gesture-detection-app-dnu60r.streamlitapp.com/)'
    st.markdown(link, unsafe_allow_html=True)