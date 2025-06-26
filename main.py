import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

df = pd.read_csv("profils_achat.csv")
df.head()

sns.scatterplot(x="Age",y="Salaire",hue="Acheté",data=df)
plt.show()

x = df[["Age","Salaire"]]
y = df["Acheté"]

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3,random_state=42)

ia = LogisticRegression()
ia.fit(xtrain,ytrain)

predict = ia.predict(xtest)

print(accuracy_score(ytest,predict))
print(confusion_matrix(ytest,predict))

def devine_achat():

  rejouer = 1

  while rejouer == 1:

    while True:

      a = input("\nEntrez l'âge : ")
      if a.isdigit():
        a = int(a)
        if 18<a<110:
          b = input("\nEntrez le salaire annuel : ")
          if b.isdigit():
            b = int(b)
            break
          else :
            print("\nVeuillez entrer un nombre")
        else :
          print("\nVeuillez entrer un âge valide")
      else :
        print("\nVeuillez entrer un nombre")



    new_pred = pd.DataFrame([[a, b]], columns=["Age", "Salaire"])

    if ia.predict(new_pred) == 0:
      print("\nN'achètera pas\n")
    else:
      print("\nAchètera\n")


    while True:
        choix = input("Voulez-vous réessayer ? 1 pour oui, 0 pour non : ")
        if choix == "1":
            break  # relance la boucle principale
        elif choix == "0":
            print("\nMerci d'avoir utilisé notre outil\n")
            return  # quitte complètement la fonction
        else:
            print("\nEntrée invalide. Tapez 1 ou 0 uniquement\n")

if __name__ == "__main__":
  devine_achat()

