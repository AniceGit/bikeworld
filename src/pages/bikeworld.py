import streamlit as st
from controllers.produit_controller import get_top_3_ventes
from models.produit import Produit


def afficher_produits_stars():
    st.markdown("#")
    st.markdown("<h2 style='text-align: center;'>Top Ventes</h2>", unsafe_allow_html=True)

    liste_top_ventes:list[Produit] = get_top_3_ventes()

    nb_colonnes = 3
    colonnes = st.columns(nb_colonnes)

    #Parcourir les produits et le top 3 des ventes
    for i, produit in enumerate(liste_top_ventes):
        column_index = i % nb_colonnes
        with colonnes[column_index]:
            if produit.image:
                st.image(produit.image, use_container_width=True)

                # Utiliser des colonnes pour aligner le nom et le bouton
                nom_col, button_col = st.columns([3, 1])
                with nom_col:
                    st.markdown(
                        f"""
                        <div style='background-color: #141312; padding: 4px; border-radius: 5px;'>
                            <p style='font-size: 20px; font-weight: bold; margin: 0;'>{produit.nom}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                with button_col:
                    if st.button("Détail", key=produit.id):
                        st.session_state["produit"] = produit
                        st.switch_page("pages/produit.py")

                # Afficher le prix en dessous
                st.markdown(
                        f"""
                            <div style='background-color: #141312; padding: 1px; border-radius: 5px;'>
                                <p style='font-size: 23px; margin: 0'>Prix: {produit.prix:.2f} €</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                    )
            else:
                st.write("Aucune image disponible")



    # Organiser les produits en forme de pyramide
    # Afficher "Top Ventes" au milieu

    # Produit le plus vendu en haut
#     if len(liste_top_ventes) >= 1:
#         produit_top = liste_top_ventes[0]
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             if produit_top.image:
#                 st.image(produit_top.image, width=200)  # Utilisation d'une largeur fixe
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #494341; padding: 4px; border-radius: 5px;'>
#                         <p style='font-size: 24px; font-weight: bold; margin: 0;'>{produit_top.nom}</p>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#                 prix_col, button_col = st.columns([1, 1])
#                 with button_col:
#                     if st.button("Détail", key=produit_top.id):
#                         st.session_state["produit"] = produit_top
#                         st.switch_page("pages/produit.py")
#             else:
#                 st.write("Aucune image disponible")

#     # Deuxième et troisième produits en dessous
#     if len(liste_top_ventes) >= 3:
#         col1, col2 = st.columns(2)
#         with col1:
#             produit_2 = liste_top_ventes[1]
#             if produit_2.image:
#                 st.image(produit_2.image, width=200)
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #494341; padding: 4px; border-radius: 5px;'>
#                         <p style='font-size: 24px; font-weight: bold; margin: 0;'>{produit_2.nom}</p>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#                 prix_col, button_col = st.columns([1, 1])
#                 with button_col:
#                     if st.button("Détail", key=produit_2.id):
#                         st.session_state["produit"] = produit_2
#                         st.switch_page("pages/produit.py")
#             else:
#                 st.write("Aucune image disponible")

#         with col2:
#             produit_3 = liste_top_ventes[2]
#             if produit_3.image:
#                 st.image(produit_3.image, width=200)
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #494341; padding: 4px; border-radius: 5px;'>
#                         <p style='font-size: 24px; font-weight: bold; margin: 0;'>{produit_3.nom}</p>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#                 prix_col, button_col = st.columns([1, 1])
#                 with button_col:
#                     if st.button("Détail", key=produit_3.id):
#                         st.session_state["produit"] = produit_3
#                         st.switch_page("pages/produit.py")
#             else:
#                 st.write("Aucune image disponible")
#afficher_produits_stars()