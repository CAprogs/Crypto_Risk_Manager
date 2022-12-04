#     ----------------------------- "Pari sur un Long --> Hausse" ---------------------------------

# Exemple pour un stop loss de 50% ; une mise de 100€ en fonction d'un effet de levier x25 ( fluct*leverage = stop_loss ) 
#    -------- Valeur_crypto : 17000 €  | Levier : x25 | Stop_loss : 50% ----------
#
#    Pour une exposition de :  100 €
#    Votre limite devrai être établie à : 16660.0 €
#    Fluctuation de la crypto de :  2.0 %
#    Vous aurez perdu : 50 €
#
#    ----------------------------------------------------------------------------------------------------------
#    ----------------------------------------------------------------------------------------------------------

def Risk_Management():
    print("""
            *********    Bienvenue sur << CRYPTO_RISK_MANAGER >>   *********** 
    *************************************************************************************
          !!!! Veuillez entrer uniquement des valeurs entières ou décimales !!!!!

    """)
    exposition = input("""                      ------- Somme à mettre en jeu -------- 
                        ===>  """)                                                                       # votre mise
    stop_loss = input("""                       ------- Votre Stop Loss (--> entrez 10 pour un stop_loss de 10%) --------       
                        ===>  """)                                                                       # le pourcentage de mise que vous êtes prêt à perdre
    crypto_value = input("""                    ------- La valeur de la crypto en cours de Trade --------       
                        ===>  """)                                                                       # Valeur actuelle/fictive de la crypto sur laquelle vous souhaitez Trader
    return float(exposition), float(stop_loss), float(crypto_value)      


exposition, stop_loss, crypto_value = Risk_Management()                          # On affecte les valeurs entrées par l'utilisateur aux différents éléments respectifs du programme
leverage = [25,50,100,125]                                                       # les différents leviers disponibles
fluct_associate = []                                                             # permet de calculer la valeur à laquelle vous devez vous retirer selon l'effet de levier choisi
for i in leverage:
    fluct_associate.append(stop_loss/i)
for i in range(len(leverage)):
    limit = crypto_value*fluct_associate[i]/100
    print(f"""
    -------- Valeur_crypto : {crypto_value} €  | Levier : x{leverage[i]} | Stop_loss : {stop_loss}% ----------

    Pour une exposition de :  {exposition} €
    Votre limite devrai être établie à : {crypto_value-limit} €
    Pour une fluctuation de la crypto de : {fluct_associate[i]}%
    Vous êtes prêt à perdre : {exposition*stop_loss/100} €

    ----------------------------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------------------------

    """)
print("         -$-$-$-$-$-$-$-$-$- N'INVESTISSEZ QUE CE QUE VOUS POUVEZ ACCEPTER DE PERDRE -$-$-$-$-$-$-$-$-$- ")
print()