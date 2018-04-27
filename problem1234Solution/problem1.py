import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from family import Family


class Problem1:
    @staticmethod
    def get_relation_function(x):
        """ gives a function related to relation number in relation list
        :param x : integer that will choose the function from below dictionary"""
        return {0: Family.get_brothers,
                1: Family.get_sisters,
                2: Family.get_cousins,
                3: Family.get_paternal_uncles,
                4: Family.get_maternal_uncles,
                5: Family.get_paternal_aunt,
                6: Family.get_maternal_aunt,
                7: Family.get_brother_in_laws,
                8: Family.get_sister_in_laws,
                9: Family.get_mother,
                10: Family.get_father,
                11: Family.get_children,
                12: Family.get_sons,
                13: Family.get_daughters,
                14: Family.get_grand_daughter,
                }[x]

    @staticmethod
    def get_members_in_relation(family, relation_number, name):
        """
        gets member in the relation of the person
        :param family : An Instance of family that contains information about members and functions
        :param relation_number: relation number from the list of relation(index of relation)
        :param name: person name of that relatives we are going to get
        :return returns a list of members that are relatives of the person(name is in the argument)
         for relation_list[relation_number]
        """
        person = family.find_member_by_name(name)
        # let's get our function(ex.. get brothers, or get sisters) so we can retrieve the members
        # that is given relation
        get_members_in_relation = Problem1.get_relation_function(relation_number)
        members_in_relation = get_members_in_relation(person)
        return members_in_relation

    @staticmethod
    def print_relatives_of_member(family):
        """
        prints relatives of a member that will be given by user, and gets members after given relation from family
        :param family : An Instance of family that contains information about members and functions
        """
        print("\n problem 1 :-")
        person_name = input("Person : ")
        # get number for relation from user
        for index, relation in enumerate(family.relation_list):
            print("Enter " + str(index) + " For " + relation + ".")
        relation_number = int(input("Choose Relation: "))
        members_in_relation = Problem1.get_members_in_relation(family, relation_number, person_name)
        print(person_name + " " + family.relation_list[relation_number] + " :")
        print(", ".join([x.name for x in members_in_relation]))


if __name__ == "__main__":
    family = FamilyTree().construct()
    Problem1.print_relatives_of_member(family)




