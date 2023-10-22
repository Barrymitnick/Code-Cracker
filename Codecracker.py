# Made By Barry
import mona

# Spécifie le système d'exploitation cible
target = mona.process("notepad.exe")

# Analyse le code binaire de la cible
mona.find_all_calls(target)

# Recherche des vulnérabilités connues
mona.find_bugs(target)

# Affiche les résultats de l'analyse
mona.show()
