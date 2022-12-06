def sommaire():
    print("""
                    ***********   Bienvenue sur << CRYPTO_TRADE_ALLcase >>   ***********
 Version plus généralisée de <CRYPTO_TRADE> qui affiche tous les cas possibles en fonction des leviers existants 
    **********************************************************************************************************
                    !!!! Veuillez entrer uniquement des valeurs entières ou décimales !!!!!

    Ce programme vous aide à calculer vos potentiels bénéfices / Pertes en fonction de :
                        - La fluctuation de la valeur de la crypto
                        - Du Stop loss choisi 
                                            (en mode Short/Long)
     
        =========================================== LEGENDE ===========================================================
          1 ===> exposition   | Somme que vous souhaitez miser en €
          2 ===> crypto_value | Valeur actuelle de la crypto en €
          3 ===> fluct        | Variation de la valeur de la crypto en %
          4 ===> stop_loss    | Un stop_loss de 30%\ est idéal (permet de limiter votre perte en fonction des leviers)
        ================================================================================================================

    """)
    return Choix_mode()


def Choix_mode():
    mode = input("""  Veuillez choisir un mode de Trade :

                  [ Entrez A ] ====> SHORT | Pari sur la Baisse
                  [ Entrez B ] ====> LONG  | Pari sur la Hausse
                  
                  ======>  """)    
    match mode:
        case "A" | "a":
            print("""  
                        Mode de Trade = SHORT   
                                                    """)
            exposition =   input("""          -------------------- exposition  ----------------------------
                        1 ===>  """)                                                                     
            crypto_value = input("""          -------------------- crypto_value  --------------------------     
                        2 ===>  """)
            fluct =        input("""          -------------------- fluct ( 1 => fluct = -1% ) -------------     
                        3 ===>  """)                                                                      
            stop_loss =     input("""         -------------------- stop_loss ( 30 => stop_loss = 30%) -----    
                        4 ===>  """)                                                                   
            return Short(float(exposition), float(crypto_value), float(fluct), int(stop_loss))
        case "B" | "b":
            print("""  
                        Mode de Trade = LONG   
                                                    """)
            exposition =   input("""          -------------------- exposition  ----------------------------
                        1 ===>  """)                                                                     
            crypto_value = input("""          -------------------- crypto_value  --------------------------     
                        2 ===>  """) 
            fluct =        input("""          -------------------- fluct ( 1 => fluct = 1% ) --------------    
                        3 ===>  """)                                                                     
            stop_loss =     input("""         -------------------- stop_loss ( 30 => stop_loss = 30%) -----    
                        4 ===>  """)                                                                   
            return Long(float(exposition), float(crypto_value), float(fluct), int(stop_loss))
        
        case _:
            return print(" ERREUR : Veuillez choisir un Mode Valide [A ou B], Relancez le programme")
            

def Long(exposition ,crypto_value, fluct_pourcent, stop_loss=30):
    
    leverage = [25,50,100,125]
    print(f"""
        -------------------------  Mode de Trade : LONG  ---------------------------------- """)
    fluct_pourcent = fluct_pourcent/100
    crypto_value_fluct = crypto_value + crypto_value*fluct_pourcent
    stop_loss = stop_loss/100
    loss = exposition*stop_loss
    for i in range(len(leverage)):
        real_rexposition = exposition*leverage[i]
        liquid = 1/leverage[i]
        benefit = fluct_pourcent*real_rexposition
        limit_loss = -stop_loss*liquid
        stop_crypto_value = crypto_value + crypto_value*limit_loss
        print(f"""  
         =================================================================================                        
        |                           Levier : x{leverage[i]}                               
        |=================================================================================
        |   - Votre Mise : {exposition} €                                                 
        |   - Exposition après levier : {real_rexposition} €                              
        |   - Valeur initiale crypto : {crypto_value} €                                   
        |   - Fluctuation : {fluct_pourcent*100} %                                        
        |   - Valeur Crypto après Fluctuation : {crypto_value_fluct} €                    
        |=================================================================================
        |           Position liquidée pour une fluctuation de : -{liquid*100} %               
        |           stop_loss : {stop_loss*100} %                                         
        |           Fixez l'arrêt du Trade pour une crypto_value de {stop_crypto_value} € 
        |                    |=======================================                    
        |                    | Bénéfice potentiel    : {benefit} €                      
        |                    | Perte max potentielle : {loss} €                         
        |                    |=======================================                    
        ==================================================================================        
                            """)
        print()

def Short(exposition ,crypto_value, fluct_pourcent, stop_loss=30):

    leverage = [25,50,100,125]
    print(f"""
        -------------------------  Mode de Trade : SHORT  ---------------------------------- """)
    fluct_pourcent = -fluct_pourcent/100
    crypto_value_fluct = crypto_value + crypto_value*fluct_pourcent
    stop_loss = stop_loss/100
    loss = exposition*stop_loss
    for i in range(len(leverage)):
        real_rexposition = exposition*leverage[i]
        liquid = 1/leverage[i]
        positive_fluct_pourcent = -fluct_pourcent
        benefit = positive_fluct_pourcent*real_rexposition
        limit_loss = stop_loss*liquid
        stop_crypto_value = crypto_value + crypto_value*limit_loss
        print(f"""  
         =================================================================================                      
        |                           Levier : x{leverage[i]}                             
        |=================================================================================
        |   - Votre Mise : {exposition} €                                                 
        |   - Exposition après levier : {real_rexposition} €                              
        |   - Valeur initiale crypto : {crypto_value} €                                   
        |   - Fluctuation : {fluct_pourcent*100} %                                        
        |   - Valeur Crypto après Fluctuation : {crypto_value_fluct} €                    
        |=================================================================================
        |           Position liquidée pour une fluctuation de : +{liquid*100} %               
        |           stop_loss : {stop_loss*100} %                                         
        |           Fixez l'arrêt du Trade pour une crypto_value de {stop_crypto_value} € 
        |                    |=======================================                    
        |                    | Bénéfice potentiel    : {benefit} €                      
        |                    | Perte max potentielle : {loss} €                          
        |                    |=======================================                    
        ==================================================================================       
                            """)
        print()

sommaire()