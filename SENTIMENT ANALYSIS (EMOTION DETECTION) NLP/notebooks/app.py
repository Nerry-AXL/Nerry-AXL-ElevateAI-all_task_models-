from streamlit import text_input, form, form_submit_button, markdown, write, success, button
import joblib
import sklearn


def main():
    markdown("<h1 style='text-align: center; color: White;background-color: #e84343'>EMOTION DETECTION</h1>",
             unsafe_allow_html=True)

    write("<h8 style='text-align: left; color: White'> Predicting your emotions through text.</h8>",
          unsafe_allow_html=True)


if __name__ == '__main__':
    main()

with form(key='emotion'):
    name = text_input('Your full name: ')
    prompt = text_input("Tell us something and we'll tell you how you sound")
    submit_button = form_submit_button(label='Submit')

if submit_button:
    success('Predicting your emotions through your input text')


if button('Predict your emotion now'):
    file = 'emotion_classifier_pipe_lr.pkl'
    with open(file, 'rb') as f:
        model = joblib.load(f)

    prompt1 = [prompt]
    result = model.predict(prompt1)
    mod = result[0]
    success(f'{name}, we have detected {mod} in your text')
