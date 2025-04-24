# 📦 Installation recommandée dans Colab ou local : pip install streamlit openai
# 🚀 Lancer avec : streamlit run app.py

import streamlit as st
import openai

# Configuration de l'API OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Ou mettre directement votre clé ici

# Titre de l'app
st.set_page_config(page_title="Générateur IA pour Freelances", layout="centered")
st.title("🧠 Micro-services IA pour Freelances")
st.subheader("Générez vos textes pros en quelques secondes grâce à l'intelligence artificielle")

# Choix du service
service = st.selectbox("Quel type de contenu voulez-vous générer ?", [
    "Bio Instagram / TikTok / LinkedIn",
    "Email de prospection",
    "Script vidéo TikTok / Shorts",
    "Pitch commercial ou page de vente"
])

# Saisie de quelques infos
nom = st.text_input("Votre prénom ou nom de marque")
secteur = st.text_input("Votre domaine d'activité (ex : coach sportif, freelance web, créateur TikTok...)")
objectif = st.text_area("Objectif ou message clé à faire passer", height=100)

# Bouton pour générer
if st.button("✨ Générer mon contenu"):
    if nom and secteur and objectif:
        with st.spinner("Génération IA en cours..."):
            prompt = f"""
            Tu es un expert en copywriting.
            Génére un texte adapté pour : {service}.
            Nom / Marque : {nom}
            Domaine : {secteur}
            Objectif : {objectif}
            Format professionnel, naturel et engageant.
            """
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=500
                )
                texte = response["choices"][0]["message"]["content"]
                st.success("✅ Contenu généré :")
                st.text_area("📄 Votre contenu :", value=texte, height=300)
            except Exception as e:
                st.error(f"Erreur lors de la génération : {e}")
    else:
        st.warning("Merci de remplir tous les champs pour générer votre contenu.")

# Pied de page
st.markdown("---")
st.markdown("Créé avec ❤️ par un générateur IA pour indépendants. Bientôt en version PRO !")
