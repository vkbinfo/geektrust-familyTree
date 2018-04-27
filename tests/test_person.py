from unittest import TestCase, main
import sys
sys.path.insert(0, '../')
from person import Person


class TestPerson(TestCase):
    person = Person("Vic", "M")

    def test_add_spouse(self):
        spouse = Person("Simona","F")
        self.person.add_spouse(spouse)
        self.assertEqual(spouse.name,self.person.spouse.name)

    def test_add_child(self):
        child = Person("Creto", "M")
        self.person.add_child(child)
        self.assertEqual(child.name, self.person.sons[0].name)


if __name__ == "__main__":
    main()
