import streamlit as st
import pandas as pd
from pages.sidebar import afficher_sidebar
from src.tools.session import init_session
from src.controllers.commande_controller import transformer_panier
from src.models.panier import Panier
import time, datetime


init_session()
afficher_sidebar()
st.title("Mon Panier")


panier = st.session_state.panier
panier.total_panier = panier.recalculer_total_panier()

if panier.total_panier == 0.00:
    st.write("Votre panier est vide")
else:
    panier.frais_livraison = panier.get_frais_livraison()
    st.write(f"Date: {panier.date_panier}")

    df_total = pd.DataFrame(
        [
            {
                "Frais de livraison (€)": f"{panier.frais_livraison:.2f}",
                "Total du panier (€)": f"{panier.total_panier + panier.frais_livraison:.2f}",
            }
        ]
    )

    df = pd.DataFrame(
        [
            {
                "Produit": produit_quantite["produit"],
                "Quantité": produit_quantite["quantite"],
                "Prix unitaire (€)": f"{produit_quantite['prix']:.2f}",
                "Total (€)": f"{produit_quantite['total']:.2f}",
            }
            for produit_quantite in panier.liste_produits_quantite
        ]
    )

    st.dataframe(
        df,
        column_config={
            "Prix unitaire (€)": st.column_config.NumberColumn(format="euro"),
            "Total (€)": st.column_config.NumberColumn(format="euro"),
        },
        hide_index=True,
    )

    st.dataframe(
        df_total,
        column_config={
            "Frais de livraison (€)": st.column_config.NumberColumn(format="euro"),
            "Total du panier (€)": st.column_config.NumberColumn(format="euro"),
        },
        hide_index=True,
    )

    ligne_panier = [produit_quantite["produit"] for produit_quantite in panier.liste_produits_quantite]
    selected_id = st.selectbox("Sélectionner un produit à supprimer :", ligne_panier)

    if selected_id:
        ligne_panier = next((produit_quantite for produit_quantite in panier.liste_produits_quantite if produit_quantite["produit"] == selected_id), None)

    if st.button("Supprimer du panier"):
        liste_panier = panier.liste_produits_quantite
        liste_panier.remove(ligne_panier)



        panier.total_panier = panier.recalculer_total_panier()
        panier.frais_livraison = panier.get_frais_livraison()

        with st.spinner(text="Veuillez patienter", show_time=False):
            time.sleep(2)
        st.switch_page("pages/panier.py")


    if st.button("Passer la commande"):
        if not st.session_state["utilisateur"]:
            st.switch_page("pages/connexion.py")
        else:
            transformer_panier()

            st.session_state.panier = Panier(str(datetime.date.today()), 0.0)

            with st.spinner(text="Veuillez patienter", show_time=False):
                time.sleep(2)
            st.switch_page("pages/commandes.py")
