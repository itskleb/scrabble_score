import streamlit as st
import pandas as pd

st.set_page_config(page_title='Scrabble Score')


p1_score = 0
p2_score = 0
flag = False


st.session_state.player1 = st.sidebar.text_input('Player 1 Name',disabled = flag,
                                                    placeholder = 'Player 1')
st.session_state.player2 = st.sidebar.text_input('Player 2 Name',disabled = flag,
                                                    placeholder = 'Player 2')


def run_it_back():
    st.session_state.prev1_score += p1s
    st.session_state.p1list.append(p1s)

def run_it_back_2():
    st.session_state.prev2_score += p2s
    st.session_state.p2list.append(p2s)



col1, col2 = st.columns(2)

with col1:
    if "prev1_score" not in st.session_state:
        st.session_state.prev1_score = p1_score
        st.session_state.p1list = []
    st.header(st.session_state.player1+" Score: {0}".format(st.session_state.prev1_score))
    #st.write("Score: {0}".format(st.session_state.prev1_score))
    p1s = st.number_input('Word Score',min_value = 0,step = 1,key="Player1")
    st.button('Score1',on_click=run_it_back)
    st.write(st.session_state.player1+"\'s last 3 scores")
    if len(st.session_state.p1list)<=3:
        for i in st.session_state.p1list:
            st.write(i)
    else:
        for i in st.session_state.p1list[-4:-1]:
            st.write(i)

with col2:
    if "prev2_score" not in st.session_state:
        st.session_state.prev2_score = p2_score
        st.session_state.p2list = []
    st.header(st.session_state.player2 + " Score: {0}".format(st.session_state.prev2_score))
    #st.write("Score: {0}".format(st.session_state.prev2_score))
    p2s = st.number_input('Word Score',min_value = 0,step = 1,key="Player2")
    st.button('Score2',on_click=run_it_back_2)
    st.write(st.session_state.player2+"\'s last 3 scores")
    if len(st.session_state.p2list)<=3:
        for i in st.session_state.p2list:
            st.write(i)
    else:
        for i in st.session_state.p2list[-4:-1]:
            st.write(i)
def party():
    if st.session_state.prev1_score > st.session_state.prev2_score:
        st.header('{0} WINS!!!!'.format(st.session_state.player1))
        st.image('https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif')
    else:
        st.header('{0} WINS!!!!'.format(st.session_state.player2))
        st.image('https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif')
st.button('Game Over',on_click=party)
