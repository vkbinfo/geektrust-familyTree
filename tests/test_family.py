import sys
sys.path.insert(0, '../')
from unittest import TestCase, main
from familyTree import FamilyTree
from person import Person


class TestFamily(TestCase):
    def setUp(self):
        self.family = FamilyTree.construct()

    def test_marriage_of_a_family_member(self):
        member = self.family.find_member_by_name("Jata")
        new_member = Person('Simone','F')
        self.family.marriage_of_a_family_member(member, new_member)
        self.assertEqual(member.spouse, new_member)
        self.assertEqual(member, new_member.spouse)

    def test_add_new_born(self):
        parent_name = "Drita"
        child_name = "Simone"
        sex = "F"
        self.family.add_new_born(parent_name, child_name, sex)
        new_member = self.family.find_member_by_name(child_name)
        self.assertTrue(parent_name in [new_member.mother.name, new_member.father.name])

    def test_add_member_in_family(self):
        new_member = Person('Simone', 'F')
        self.family.add_member_in_family(new_member)
        self.assertEqual(self.family.members[-1], new_member)

    def test_find_member_by_name(self):
        person_name = "Drita"
        member = self.family.find_member_by_name(person_name)
        self.assertEqual(member.name, person_name)

    def test_get_brothers(self):
        self.fail()

    def test_get_sisters(self):
        self.fail()

    def test_get_brother_in_laws(self):
        self.fail()

    def test_get_sister_in_laws(self):
        self.fail()

    def test_get_paternal_uncles(self):
        self.fail()

    def test_get_maternal_uncles(self):
        self.fail()

    def test_get_paternal_aunt(self):
        self.fail()

    def test_get_maternal_aunt(self):
        self.fail()

    def test_get_children(self):
        self.fail()

    def test_get_cousins(self):
        self.fail()

    def test_get_grand_daughter(self):
        self.fail()

    def test_get_mother(self):
        self.fail()

    def test_get_father(self):
        self.fail()

    def test_get_sons(self):
        self.fail()

    def test_get_daughters(self):
        self.fail()
