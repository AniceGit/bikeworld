import streamlit as st
import pandas as pd
import time
from src.tools.session import init_session
from pages.sidebar import afficher_sidebar
from src.controllers.commande_controller import supprimer_commande, get_commandes, get_adresse_commande
from src.controllers.produit_controller import get_produit_nom_by_id


init_session()
if not st.session_state["utilisateur"]:
    st.switch_page("pages/connexion.py")

afficher_sidebar()
st.title("Vos commandes")

commandes = get_commandes(st.session_state["utilisateur"].id)

data = []

for cmd in commandes:

    data.append({
        "ID": cmd.id,
        "Date": cmd.date_commande,
        "Frais de livraison (€)": f"{cmd.frais_livraison:.2f}",
        "Total (€)": f"{cmd.prix_total:.2f}",
        "Etat": cmd.etat
    })

df = pd.DataFrame(data)

st.dataframe(df, column_config={
        "Frais de livraison (€)": st.column_config.NumberColumn(format="euro"),
        "Total (€)": st.column_config.NumberColumn(format="euro")
    }, hide_index=True)

commande_ids = [cmd.id for cmd in commandes]
selected_id = st.selectbox("Sélectionner une commande :", commande_ids)

if selected_id:
    cmd = next((c for c in commandes if c.id == selected_id), None)
    if cmd:
        st.subheader(f"🧾 Détails de la commande {cmd.id}")
        st.write(f"Date : {cmd.date_commande}")
        adresse = get_adresse_commande(cmd.id)
        st.write(f"Adresse : {adresse.numero} {adresse.type_voie} {adresse.nom_voie}, {adresse.code_postal} {adresse.ville}")
      
        ligne_df = pd.DataFrame([{
            "Produit": get_produit_nom_by_id(l.id_produit),
            "Quantité": l.quantite,
            "Prix unitaire (€)": f"{l.prix:.2f}",
            "Total (€)": f"{l.quantite * l.prix :.2f}"
        } for l in cmd.liste_produit_commande])

#        st.table(ligne_df)
        st.dataframe(ligne_df, column_config={
            "Prix unitaire (€)": st.column_config.NumberColumn(format="euro"),
            "Total (€)": st.column_config.NumberColumn(format="euro")
        }, hide_index=True)

        if cmd.etat == "Validee":
            if st.button(f"🗑️ Supprimer la commande {cmd.id}", key=f"delete_{cmd.id}"):
                supprimer_commande(cmd.id)
                with st.spinner(text="Veuillez patienter", show_time=False):
                    st.success(f"Commande {cmd.id} supprimée.")
                    time.sleep(2)
                st.switch_page("pages/commandes.py")
