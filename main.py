print("Hello Unit Tests")

import unittest

# Le code à tester doit être importable. On
# verra dans une autre partie comment organiser
# son projet pour cela.
#from mon_module import get
def get(lst, index, default=None):
    """
        Retourne l'élément de `lst` situé à `index`.

        Si aucun élément ne se trouve à `index`,
        retourne la valeur par défaut.
    """
    try:
        return lst[index]
    except IndexError:
        return default

# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT hériter de unittest.TestCase.
class TestFonctionGet(unittest.TestCase):
    # Chaque méthode dont le nom commence par 'test_'
    # est un test.
    def test_get_element(self):
        simple_comme_bonjour = ('pomme', 'banane')
        element = get(simple_comme_bonjour, 0)

        # Le test le plus simple est un test d'égalité. On se
        # sert de la méthode assertEqual pour dire que l'on
        # s'attend à ce que les deux éléments soient égaux. Sinon
        # le test échoue.
        self.assertEqual(element, 'pomme')


# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()