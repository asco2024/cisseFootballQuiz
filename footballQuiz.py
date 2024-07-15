import random
import streamlit as st
import time
random.seed(time.time())

questions = {
    "Who scored the first goal for AFC U10 in the Netherlands during the recent Rud Wit Tournement?" : {"choices" : ["Ivan","Cisse","Hudson","Jack","Jackson"],"answer": "Cisse"},
    "Which AFC U10 player got nominated for the best goal of the season 2023/24?" : {"choices" : ["Freddie","Nile","Jack","Carter"],"answer": "Jack"},
    "Who was the captain for AFC U10 during the recent Rud Wit Tournament in the Netherlands" : {"choices" : ["Alex","Daniel","Hudson","Ray"],"answer": "Hudson"},
    "Which team won Euro 2024?" : {"choices" : ["England","Spain","France","Germany"],"answer": "Spain"},
    "Which position did AFC U10 finish durin the recent Rud Wit Tournament?" : {"choices" : ["5th","9th","11th","1st"],"answer": "11th"},
    "How many European cups has Aberdeen FC won?" : {"choices" : ["4","2","1"],"answer": "2"},
    "Which of the following coaches has managed Aberdeen?" : {"choices" : ["Alex ferguson","Pep Guardiola","Gareth Southgate"],"answer": "Alex ferguson"},
    "who is the youngest player in Euro 2024?" : {"choices" : ["Arda Guler","Mainoo","Nico Williams","Yamal"],"answer": "Yamal"},
    "How many Scottish league titles has Aberdeen FC won?" : {"choices" : ["5","4","6"],"answer": "4"},
    "When was Aberdeen FC formed?" : {"choices" : ["1903","1826","1951"],"answer": "1903"},
    "Which of the following are left-footed defenders for AFC U10?" : {"choices" : ["Daniel and Myles","Myles and Ivan","Ivan and Alex","Daniel and Alex"],"answer": "Ivan and Alex"},
    "Which of the following are right-footed defenders for AFC U10?" : {"choices" : ["Daniel and Myles","Myles and Ivan","Ivan and Alex","Daniel and Alex"],"answer": "Daniel and Myles"},
    "Which of the following scored 5 goals in one game for AFC U10?" : {"choices" : ["Nile","Jack","","Freddie","Carter","All"],"answer": "All"},
    "Which of the following players mostly play in midfield for AFC U10?" : {"choices" : ["Daniel and Nile","Freddie and Jack","Hudson and Barclay","Alex and Russell"],"answer": "Hudson and Barclay"},
    "Which of the following is a fantastic goal stopper?" : {"choices" : ["Timmy","Harry","Reuben","None"],"answer": "Timmy"},    
    "Who is known as Big D in AFC U10?" : {"choices" : ["Cisse","Alex","Daniel","Ivan"],"answer": "Daniel"},   
    "Which of the following managed us during our AFC U9 days?" : {"choices" : ["Mark and Chris and Rob","Aaron and Jamie and Stuart","Aaron and Mark and Stuart","Jamie, Chris and Aaron"],"answer": "Mark and Chris and Rob"}, 
    "Who once forgot to bring along his football boots to an AFC U10 game in Edingburgh against Hearts?" : {"choices" : ["Myles","Timmy","Ivan","Cisse"],"answer": "Cisse"},   
    "Where did we place in the group stage at the Ruud Wit Tournament during the Group stage of the Champions League?" : {"choices" : ["5th","1st","3rd","11th"],"answer": "5th"},  
    "Which of the following is the youngest in the squad?" : {"choices" : ["Alex","Jackson","Timmy","Russell"],"answer": "Russell"},        
}

def initialize_quiz():
    items = list(questions.items())
    random.shuffle(items)
    st.session_state.quiz_questions = items
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.quiz_completed = False
    st.session_state.answer_submitted = False  # Track if the answer has been submitted

if 'quiz_questions' not in st.session_state:
    initialize_quiz()

def display_question():
    question, data = st.session_state.quiz_questions[st.session_state.current_question_index]
    st.write(question)
    choices = ["Select your answer"] + data['choices']
    user_answer = st.radio("Choose one:", choices, index=0, key=f"choice{st.session_state.current_question_index}")
    return user_answer

def handle_answer(user_answer):
    if not st.session_state.answer_submitted and user_answer != "Select your answer":
        st.session_state.answer_submitted = True  # Mark the answer as submitted
        question, data = st.session_state.quiz_questions[st.session_state.current_question_index]
        if user_answer == data['answer']:
            st.session_state.score += 1
            st.success('Correct!')
        else:
            st.error(f'Wrong! The correct answer was {data["answer"]}.')
    elif st.session_state.answer_submitted:
        # Advance to the next question or finish quiz
        if st.session_state.current_question_index < len(st.session_state.quiz_questions) - 1:
            st.session_state.current_question_index += 1
            st.session_state.answer_submitted = False  # Reset for the next question
            st.experimental_rerun()
        else:
            st.session_state.quiz_completed = True
            st.write(f"Quiz completed! Your final score is {st.session_state.score}/{len(st.session_state.quiz_questions)}.")

def reset_quiz():
    if st.button('Restart Quiz'):
        initialize_quiz()
        st.experimental_rerun()

user_answer = display_question()

button_label = "Next Question" if st.session_state.answer_submitted else "Submit Answer"
if st.button(button_label, key='submit'):
    handle_answer(user_answer)

if st.session_state.quiz_completed:
    reset_quiz()
