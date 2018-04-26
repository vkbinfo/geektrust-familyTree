import sys

sys.path.insert(0, '../')
from unittest import TestCase, main
from familyTree import FamilyTree
from person import Person
from family import Family


class TestFamily(TestCase):
    family = FamilyTree().construct()

    def test_marriage_of_a_family_member(self):
        member = self.family.find_member_by_name("Jata")
        new_member = Person('Sita', 'F')
        self.family.marriage_of_a_family_member(member, new_member)
        self.assertEqual(member.spouse, new_member)
        self.assertEqual(member, new_member.spouse)

    def test_add_new_born(self):
        parent_name = "Drita"
        child_name = "Simona"
        sex = "F"
        self.family.add_new_born(parent_name, child_name, sex)
        new_member = self.family.find_member_by_name(child_name)
        self.assertTrue(parent_name in [new_member.mother.name, new_member.father.name])
        self.tearDown()

    def test_add_member_in_family(self):
        new_member = Person('Simone', 'F')
        self.family.add_member_in_family(new_member)
        self.assertEqual(self.family.members[-1], new_member)

    def test_find_member_by_name(self):
        person_name = "Drita"
        member = self.family.find_member_by_name(person_name)
        self.assertEqual(member.name, person_name)

    def test_get_brothers(self):
        person_name = "Satvy"
        person_bothers = ["Savya", "Saayan"]
        person = self.family.find_member_by_name(person_name)
        brothers = Family.get_brothers(person)
        brother_name_list = [x.name for x in brothers]
        for brother in brother_name_list:
            self.assertTrue(brother in person_bothers)
        for brother in person_bothers:
            self.assertTrue(brother in brother_name_list)

    def test_get_sisters(self):
        person_name = "Vich"
        person_sister = ["Satya"]
        person = self.family.find_member_by_name(person_name)
        sisters = Family.get_sisters(person)
        sister_name_list = [x.name for x in sisters]
        for sister in sister_name_list:
            self.assertTrue(sister in person_sister)
        for sister in person_sister:
            self.assertTrue(sister in sister_name_list)

    def test_get_brother_in_laws(self):
        # a man's brother in laws
        person_name = "Vyan"
        brother_in_laws_names = ["Ish", "Chit", "Vich"]
        person = self.family.find_member_by_name(person_name)
        brother_in_laws = Family.get_brother_in_laws(person)
        brother_in_laws_in_tree = [x.name for x in brother_in_laws]
        for name in brother_in_laws_in_tree:
            self.assertTrue(name in brother_in_laws_names)
        for name in brother_in_laws_names:
            self.assertTrue(name in brother_in_laws_in_tree)
        # a woman's brother in laws
        person_name = "Lika"
        brother_in_laws_names = ["Ish", "Chit"]
        person = self.family.find_member_by_name(person_name)
        brother_in_laws = Family.get_brother_in_laws(person)
        brother_in_laws_in_tree = [x.name for x in brother_in_laws]
        for name in brother_in_laws_in_tree:
            self.assertTrue(name in brother_in_laws_names)
        for name in brother_in_laws_names:
            self.assertTrue(name in brother_in_laws_in_tree)

    def test_get_sister_in_laws(self):
        # a man's brother in laws
        person_name = "Saayan"
        sister_in_laws_names = ["Krpi"]
        person = self.family.find_member_by_name(person_name)
        sister_in_laws = Family.get_sister_in_laws(person)
        sister_in_laws_in_tree = [x.name for x in sister_in_laws]
        for name in sister_in_laws_in_tree:
            self.assertTrue(name in sister_in_laws_names)
        for name in sister_in_laws_names:
            self.assertTrue(name in sister_in_laws_in_tree)
        # a woman's sister in laws
        person_name = "Lika"
        sister_in_laws_names = ["Satya"]
        person = self.family.find_member_by_name(person_name)
        sister_in_laws = Family.get_sister_in_laws(person)
        sister_in_laws_in_tree = [x.name for x in sister_in_laws]
        for name in sister_in_laws_in_tree:
            self.assertTrue(name in sister_in_laws_names)
        for name in sister_in_laws_names:
            self.assertTrue(name in sister_in_laws_in_tree)

    def test_get_paternal_uncles(self):
        person_name = "Satvy"
        paternal_uncle_names = ["Ish", "Chit", "Vich"]
        person = self.family.find_member_by_name(person_name)
        paternal_uncle = Family.get_paternal_uncles(person)
        paternal_uncle_in_tree = [x.name for x in paternal_uncle]
        for name in paternal_uncle_in_tree:
            self.assertTrue(name in paternal_uncle_names)
        for name in paternal_uncle_names:
            self.assertTrue(name in paternal_uncle_in_tree)

    def test_get_maternal_uncles(self):
        person_name = "Driya"
        maternal_uncle_names = ["Vrita"]
        person = self.family.find_member_by_name(person_name)
        maternal_uncle = Family.get_maternal_uncles(person)
        maternal_uncle_in_tree = [x.name for x in maternal_uncle]
        for name in maternal_uncle_in_tree:
            self.assertTrue(name in maternal_uncle_names)
        for name in maternal_uncle_names:
            self.assertTrue(name in maternal_uncle_in_tree)

    def test_get_paternal_aunt(self):
        person_name = "Vila"
        paternal_aunt_names = ["Satya", "Ambi"]
        person = self.family.find_member_by_name(person_name)
        paternal_aunt = Family.get_paternal_aunt(person)
        paternal_aunt_in_tree = [x.name for x in paternal_aunt]
        for name in paternal_aunt_in_tree:
            self.assertTrue(name in paternal_aunt_names)
        for name in paternal_aunt_names:
            self.assertTrue(name in paternal_aunt_in_tree)

    def test_get_maternal_aunt(self):
        person_name = "Vila"
        maternal_aunt_names = ["Satya"]
        person = self.family.find_member_by_name(person_name)
        maternal_aunt = Family.get_maternal_aunt(person)
        maternal_aunt_in_tree = [x.name for x in maternal_aunt]
        for name in maternal_aunt_in_tree:
            self.assertTrue(name in maternal_aunt_names)
        for name in maternal_aunt_names:
            self.assertTrue(name in maternal_aunt_in_tree)

    def test_get_children(self):
        person_name = "Satya"
        children_names = ["Satvy", "Savya", "Saayan"]
        person = self.family.find_member_by_name(person_name)
        children = Family.get_children(person)
        children_in_tree = [x.name for x in children]
        for name in children_in_tree:
            self.assertTrue(name in children_names)
        for name in children_names:
            self.assertTrue(name in children_in_tree)

    def test_get_cousins(self):
        person_name = "Vila"
        cousin_names = ["Satvy", "Savya", "Saayan", "Drita", "Vrita"]
        person = self.family.find_member_by_name(person_name)
        cousin = Family.get_cousins(person)
        cousin_in_tree = [x.name for x in cousin]
        for name in cousin_in_tree:
            self.assertTrue(name in cousin_names)
        for name in cousin_names:
            self.assertTrue(name in cousin_in_tree)

    def test_get_grand_daughter(self):
        person_name = "King Shan"
        grand_daughter_names = ["Satvy", "Chika"]
        person = self.family.find_member_by_name(person_name)
        grand_daughter = Family.get_grand_daughter(person)
        grand_daughter_in_tree = [x.name for x in grand_daughter]
        for name in grand_daughter_in_tree:
            self.assertTrue(name in grand_daughter_names)
        for name in grand_daughter_names:
            self.assertTrue(name in grand_daughter_in_tree)

    def test_get_mother(self):
        person_name = "Vila"
        mother_name = "Lika"
        person = self.family.find_member_by_name(person_name)
        mother = Family.get_mother(person)[0]
        self.assertEqual(mother_name, mother.name)

    def test_get_father(self):
        person_name = "Vila"
        mother_name = "Vich"
        person = self.family.find_member_by_name(person_name)
        father = Family.get_father(person)[0]
        self.assertEqual(mother_name, father.name)

    def test_get_sons(self):
        person_name = "Vyan"
        sons_names = ["Savya", "Saayan"]
        person = self.family.find_member_by_name(person_name)
        sons = Family.get_sons(person)
        sons_in_tree = [x.name for x in sons]
        for name in sons_in_tree:
            self.assertTrue(name in sons_names)
        for name in sons_names:
            self.assertTrue(name in sons_in_tree)

    def test_get_daughters(self):
        person_name = "Vyan"
        daughters_names = ["Satvy"]
        person = self.family.find_member_by_name(person_name)
        daughters = Family.get_daughters(person)
        daughters_in_tree = [x.name for x in daughters]
        for name in daughters_in_tree:
            self.assertTrue(name in daughters_names)
        for name in daughters_names:
            self.assertTrue(name in daughters_in_tree)


if __name__ == "__main__":
    main()
