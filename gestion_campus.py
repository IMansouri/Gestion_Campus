class Personne:
    '''represente une classe Personne'''
    def __init__(self, nom, prenom, identifiant):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''

        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant

    def __repr__(self):
        '''(Personne)->str
        retourne une representation de l'objet'''

        return ("Identifiant: " + str(self.identifiant) + " Nom: " + self.nom + " Prenom: " + self.prenom)
    

    def __eq__(self, autre):
        '''(Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes'''
        
        return ((self.nom == autre.nom) and (self.prenom == autre.prenom) and (self.identifiant == autre.identifiant))
        
class Etudiant(Personne):
    '''represente une classe Etudiant'''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)
     
     # methodes
     
    def __init__(self, nom='nom', prenom='prenom', identifiant=000000000, solde=0, cours=[]):

        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant
        self.solde = solde
        self.cours = cours

        
    def ajouterCours(self,nomCours):

        if (self.solde == 0):

            nomCours = nomCours.split()

            for i in nomCours:

                self.cours.append(i)

            return True

        else:

            return False

    def _repr_(self):

        return ("Identifiant: " + str(self.identifiant) + " Nom: " + self.nom + " Prenom: " + self.prenom + " Solde: " + str(self.solde) + " Cours: " + str(self.cours))
        

class Employe(Personne):
    '''represente un employe'''
    # tauxHoraire est un attribut de la classe Employe
    
    # methodes

    def __init__(self, nom='nom', prenom='prenom', identifiant=000000000, tauxHoraire=0):

        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant
        self.tauxHoraire = tauxHoraire

    def calculerSalaires(self,nombreHeures):

        salaire = nombreHeures * self.tauxHoraire

        return salaire

    def _repr_(self):

        return ("Identifiant: " + str(self.identifiant) + " Nom: " + self.nom + " Prenom: " + self.prenom + " Taux Horaire: " + str(self.tauxHoraire))


class Gestion:
 listEtudiant = []
 listEmploye = []
 def ajouterEtudiant(self):
    ''' none -> bool
    ajouter des etudiants dans une liste d'etudiant'''

    student = Etudiant()

    if (student.nom == 'nom') or (student.prenom == 'prenom') or (student.identifiant == 000000000):

        student.nom = input("Veuillez entrer le nom de l'etudiant: ")
        student.prenom = input("Veuillez entrer le prenom de l'etudiant: ")
        student.identifiant = int(input("Veuillez entrer le numero d'etudiant: "))
        student.solde = float(input("Veuillezz entrer la solde que l'etudiant doit payer: "))
        classes = input("Veuillez entrer les cours de l'etudiant (separes par des espaces): ")
        student.ajouterCours(classes)
        choix = input("Voulez-vous ajouter des cours pour l'etudiant " + student.prenom + ' ' + student.nom + '? (repondez par oui ou non)')                  
        choix = choix.lower()

        while (choix != 'oui') and (choix != 'non'):

                print("Votre reponse n'est pas valable")
                choix = input("SVP entrer oui ou non pour votre choix concernant l'ajout de cours: ")
                choix = choix.lower()

        if (choix == 'oui'):

            for s in Gestion.listEtudiant:

                if (s == student):

                    return False
            
            Gestion.listEtudiant.append(student)
            
            nomCours = input("Veuillez entrer les cours a ajouter pour l'etudiant (separes par des espaces): ")

            student.ajouterCours(nomCours)
            
            
        elif (choix == 'non'):
            
            for s in Gestion.listEtudiant:

                if (s == student):

                    return False

            Gestion.listEtudiant.append(student)
            
    return True
       
 def ajouterEmploye(self):
    ''' none -> bool
    ajouter des employes dans une liste d'employe'''

    
    workers = Employe()

    workers.nom = input("Veuillez entrer le nom de l'employe: ")
    workers.prenom = input("Veuillez entrer le prenom de l'employe: ")
    workers.identifiant = int(input("Veuillez entrer le numero identifiant de l'employe: "))
    workers.tauxHoraire = float(input("Veuillez entrer le taux horaire du salaire de l'employe: "))
    Gestion.listEmploye.sort()
    
    for w in Gestion.listEmploye:

                if (w == workers):

                    return False

    Gestion.listEmploye.append(workers)

    return True
    
 def SoldeNonPaye(self):
    ''' none -> int
    retourner le nombre des etudiants qui ont un solde non paye'''

    nbr_e = 0
    
    for s in Gestion.listEtudiant:

        if (int(s.solde) != 0):

            nbr_e += 1

    return nbr_e

        

        
 def salaireInd(self, employe, heures):
    '''(str) -> float
        retourne le salaire d'un employe'''
        # A completer

    trouve = 0
    
    for w in Gestion.listEmploye:

        if (w == employe):
            
            break
        
        if (w != employe) and (trouve == len(Gestion.listEmploye)-1):

            return float(0)

        trouve += 1

    salaire = employe.tauxHoraire * float(heures)
    
    return salaire

#program principal
g = Gestion()
print("Ajoutez des etudiants.")
# Ajouter des etudiants
g.ajouterEtudiant()
g.ajouterEtudiant()

# Ajouter des employes
print("Ajouter des employes.")
g.ajouterEmploye()
g.ajouterEmploye()

# Afficher le nombre des employes et des etudiants
print("il y a: ", len(Gestion.listEtudiant), " etudiants.")
print("il y a: ", len(Gestion.listEmploye), " employes.")
# Afficher le nombre des etudiants qui ont un solde a payer
print("il y a ", g.SoldeNonPaye(), "etudiants qui n'ont pas paye leur solde.")
# Afficher les salaires de tous les employes
for e in Gestion.listEmploye:
    heure = int(input("Entrez le nombre des heures pour employe " + e.prenom + " " + e.nom + " "))
    print('Le salaire de:', e.nom, e.prenom, 'est:', g.salaireInd(e, heure), '$.')

#Afficher toute la Gestion
print("Toute la gestion: ")
print(Gestion.listEtudiant)
print(Gestion.listEmploye)
