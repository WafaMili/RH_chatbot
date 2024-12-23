#!/usr/bin/env python
# src/cv_helper/main.py

import sys

from rh_chatbot.src.rh_chatbot.crew import CvHelper


def run():
    """
    Run the crew for CV matching and improvement tasks.
    """



    inputs = {
        'job_description': 'Nous recherchons un chef de projet marketing dynamique pour rejoindre notre équipe. Le candidat idéal doit avoir une expérience significative dans la gestion de projets marketing, avec une capacité démontrée à travailler sous pression et à atteindre des objectifs.',
        'cv_text': 'Je suis un chef de projet marketing avec 5 ans d\'expérience dans la gestion de campagnes numériques. J\'ai dirigé des équipes pour augmenter la visibilité de la marque de 30%.'
    }


    crew_helper = CvHelper()


    try:

        crew_helper.crew().kickoff(inputs=inputs)

        print("Le crew a été exécuté avec succès.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    run()
