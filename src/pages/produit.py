import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.produit_controller import get_details_produit
from src.tools.session import init_session


init_session()
afficher_sidebar()
id = st.session_state["produit"].id
produit = get_details_produit(id)


st.title(produit.nom)

col1, col2 = st.columns([1, 2])
with col1:
    if produit.image:
        st.image(produit.image, caption=produit.nom, use_container_width=True)
    else:
        st.write("Aucune image disponible")
    with col2:
        st.write(
            f"<span style='font-size: 20px;'>**Description**</span>:",
            unsafe_allow_html=True,
        )
        st.write(f"{produit.description}", unsafe_allow_html=True)
        st.write(
            f"<span style='font-size: 20px;'>**Spécifications Techniques**</span>:",
            unsafe_allow_html=True,
        )
        st.write(f"{produit.spec_tech}")
        st.write(
            f"<span style='font-size: 20px;'>**Couleur**</span>: {produit.couleur}",
            unsafe_allow_html=True,
        )
        st.write(
            f"<span style='font-size: 20px;'>**Prix**</span>: {produit.prix:.2f}",
            unsafe_allow_html=True,
        )
        st.write(
            f"<span style='font-size: 20px;'>**Stock**</span>: {produit.stock}",
            unsafe_allow_html=True,
        )
        if st.button("Ajouter au panier", key=produit.id):
            panier = st.session_state.panier
            if panier:
                for produit_quantite in panier["liste_produits_quantite"]:
                    p_id = produit_quantite["produit_id"]

                    if p_id == produit.id:
                        if produit_quantite["quantite"] + 1 > produit.stock:
                            st.error(
                                f"Stock insuffisant pour le produit {produit.nom} !"
                            )
                            break
                        else:
                            produit_quantite["quantite"] += 1
                            panier["total_panier"] += produit.prix
                            panier["total_panier"] = round(panier["total_panier"], 2)
                            produit_quantite["total"] = (
                                produit.prix * produit_quantite["quantite"]
                            )
                            produit_quantite["total"] = round(
                                produit_quantite["total"], 2
                            )
                            st.session_state.panier = panier
                            st.success(f"{produit.nom} a été ajouté au panier !")
                            break

                else:
                    if produit.stock == 0:
                        st.error(f"Stock insuffisant pour le produit {produit.nom} !")
                    else:
                        panier["total_panier"] += produit.prix
                        panier["total_panier"] = round(panier["total_panier"], 2)
                        panier["liste_produits_quantite"].append(
                            {
                                "produit_id": produit.id,
                                "produit": produit.nom,
                                "quantite": 1,
                                "prix": produit.prix,
                                "total": produit.prix,
                            }
                        )
                        st.session_state.panier = panier
                        st.success(f"{produit.nom} a été ajouté au panier !")
