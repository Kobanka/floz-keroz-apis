from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Income, Expense  # Importer tes modèles

# Créer une session
engine = create_engine('sqlite:///instance/budget.db')  # Remplace par l'URL de ta base de données
Session = sessionmaker(bind=engine)
session = Session()

# Pour chaque table, mets à jour les 'id' pour qu'ils soient des UUIDs
for table in [User, Income, Expense]:
    for record in session.query(table).filter(table.id < 0).all():  # Choisir un critère pour identifier les entiers
        record.id = uuid4()  # Attribuer un UUID unique
    session.commit()

print("Mise à jour des IDs terminée")
