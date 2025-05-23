import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

lesDonneesDesComptes = {
    'usernames': {
        'valWCS': {
            'name': 'valWCS',
            'password': 'ceciestmonmdp',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
    st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")

st.write(st.session_state["authentication_status"])

if st.session_state["authentication_status"]:
  accueil()

with st.sidebar:

    if st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    if st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être rempli')
    if st.session_state["authentication_status"] is True:
        selection = option_menu(menu_title="Home", options=["Accueil", "Photos"], icons=["house", "camera"], menu_icon="cast", default_index=0, )
    authenticator.logout("Déconnexion")

if selection == "Accueil":
    st.write("Bienvenue !")
    st.image("hello_there.gif", width=2000)
elif selection == "Photos":
    st.write("Bienvenue sur l'album photo des corgis !")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("corgi_eyes.jpg")
    with col2:
        st.image("corgi_lunettes.jpg")
    with col3:
        st.image("corgi_doubt.jpg")
        
        
