from person import Person
from utility import Utility


class Family:
    """
    Handles a family members and gives information about the members through functions
    """
    members = []
    relation_list = ["Brothers", "Sisters", "Cousins", "Paternal Uncles",
                     "Maternal Uncles", "Paternal Aunts", "Maternal Aunts",
                     "Brother in laws", "Sister in laws", "Mother",
                     "Father", "Children", "Son", "Daughter", "Granddaughter"]

    def __init__(self, leader_man):
        """
        fundamental person for a family(right now its king), with that Man, we will start a family
        :param leader_man: first man in the family
        """
        self.leader_man = leader_man
        self.members.append(leader_man)

    def marriage_of_a_family_member(self, member, spouse):
        """
        new wedding in family, spouse is new person in family
        :param member: member of the family, who is going to get married
        :param spouse: new person who is going to get married to family member and going to added in family
        """
        member.add_spouse(spouse)
        spouse.add_spouse(member)
        # set the generation number tp new spouse member in family
        spouse.generation = member.generation
        self.add_member_in_family(spouse)

    def add_new_born(self, parent_name, child_name, sex):
        """
        adds a new born to family and also to its parents
        :param parent_name: parent name either of mother or father
        :param child_name: new child name, which is going to be added in family
        :param sex: child sex
        """
        parent = self.find_member_by_name(parent_name)
        if parent is None:
            print("No person name " + parent_name)
        if parent.spouse is None:
            print("Single parent can't have children")
        if parent.sex == "M":
            child = Person(child_name, sex, mother=parent.spouse, father=parent)
            child.generation = parent.generation + 1
            Utility.connect_new_born_to_parent(child, [parent, parent.spouse])
        else:
            child = Person(child_name, sex, mother=parent, father=parent.spouse)
            child.generation = parent.generation + 1
            Utility.connect_new_born_to_parent(child, [parent, parent.spouse])
        self.add_member_in_family(child)

    def add_member_in_family(self, new_member):
        """
        adds a new member to the family
        :param new_member:  new member that is a instance of Person class
        """
        self.members.append(new_member)

    def find_member_by_name(self, name):
        """
        finding a person with his name in the family
        :param name: name of a person in string format
        :return: a Person object or None
        """
        for member in self.members:
            if member.name == name:
                return member
        return None

    @staticmethod
    def get_brothers(person):
        """
        gets a list of brothers of given person
        :param person: person an Instance of Person
        :return: a list of brothers(Instances of Person Class) of given person
        """
        if person is None:
            return []
        brothers_list = []
        if person.father:
            brothers_list = person.father.sons.copy()
            if person in brothers_list:
                brothers_list.remove(person)
        return brothers_list

    @staticmethod
    def get_sisters(person):
        """
        gets a list of sisters of given person
        :param person: person an Instance of  Person Class
        :return: a list of sisters(Instances of Person Class) of given person
        """
        if person is None:
            return []
        sisters_list = []
        if person.father:
            sisters_list = person.father.daughters.copy()
            if person in sisters_list:
                sisters_list.remove(person)
        return sisters_list

    @staticmethod
    def get_brother_in_laws(person):
        """
        :param person: person an Instance of Person class
        :return: a list of person objects of brother-in-laws of given person
        """
        if person is None:
            return []
        brother_in_laws = []
        # brother-in_laws are spouse's brothers and husbands of siblings(girl siblings)
        # get spouse's brothers
        spouse_brothers = Family.get_brothers(person.spouse)
        brother_in_laws.extend(spouse_brothers)
        # husbands of siblings
        girl_siblings = Family.get_sisters(person)
        for girl in girl_siblings:
            if girl.spouse:
                brother_in_laws.append(girl.spouse)
        return brother_in_laws

    @staticmethod
    def get_sister_in_laws(person):
        """
        :param person: person an Instance of Person class
        :return: a list of person objects of sister-in-laws of given person
        """
        if person is None:
            return []
        sister_in_laws = []
        # brother-in_laws are spouse's brothers and husbands of siblings(girl siblings)
        # get spouse's brothers
        spouse_sisters = Family.get_sisters(person.spouse)
        sister_in_laws.extend(spouse_sisters)
        # husbands of siblings
        boy_siblings = Family.get_brothers(person)
        for boy in boy_siblings:
            if boy.spouse:
                sister_in_laws.append(boy.spouse)
        return sister_in_laws

    @staticmethod
    def get_paternal_uncles(person):
        """
        :param person: person an Instance of Person class
        :return: a list of person objects of paternal uncles of given person
        """
        if person is None:
            return []
        # paternal uncles are father's brothers and fathers's brother-in-law's
        paternal_uncles = []
        if person.father and person.father.father:
            fathers_brother = Family.get_brothers(person.father)
            paternal_uncles.extend(fathers_brother)
        fathers_brother_in_laws = Family.get_brother_in_laws(person.father)
        paternal_uncles.extend(fathers_brother_in_laws)
        return paternal_uncles

    @staticmethod
    def get_maternal_uncles(person):
        """
        :param person: person an Instance of Person class
        :return: a list of person objects of maternal uncles of given person
        """
        if person is None:
            return []
        # maternal uncles are mother's brothers and mother's brother-in-law's
        maternal_uncles = []
        if person.mother and person.mother.father:
            mothers_brother = Family.get_brothers(person.mother)
            maternal_uncles.extend(mothers_brother)
        mothers_brother_in_laws = Family.get_brother_in_laws(person.mother)
        maternal_uncles.extend(mothers_brother_in_laws)
        return maternal_uncles

    @staticmethod
    def get_paternal_aunt(person):
        """
        :param person: person an Instance of Person class, that given Familys relatives are going to be retrieved
        :return: a list of person objects of paternal aunts of given person
        """
        if person is None:
            return []
        # paternal aunt are father's sisters and fathers's sister-in-law's
        paternal_aunts = []
        if person.father and person.father.father:
            fathers_sisters = Family.get_sisters(person.father)
            paternal_aunts.extend(fathers_sisters)
        fathers_sister_in_laws = Family.get_sister_in_laws(person.father)
        paternal_aunts.extend(fathers_sister_in_laws)
        return paternal_aunts

    @staticmethod
    def get_maternal_aunt(person):
        """
        :param person: person an Instance of Person class, that given Familys relatives are going to be retrieved
        :return: a list of person objects of maternal aunts of that given person
        """
        if person is None:
            return []
        # maternal aunt are mother's sisters and mother's sister-in-law's
        maternal_aunts = []
        if person.mother and person.mother.father:
            mother_sisters = Family.get_sisters(person.mother)
            maternal_aunts.extend(mother_sisters)
        mother_sister_in_laws = Family.get_sister_in_laws(person.mother)
        maternal_aunts.extend(mother_sister_in_laws)
        return maternal_aunts

    @staticmethod
    def get_children(person):
        """
        :param person: person an Instance of Person class, that given Familys relatives are going to be retrieved
        :return: a list of person objects of children of that given person
        """
        if person is None:
            return []
        return person.sons + person.daughters

    @staticmethod
    def get_cousins(person):
        """
        :param person: person an Instance of Person class, that given Familys relatives are going to be retrieved
        :return: a list of person objects of cousins of that given person
        """
        if person is None:
            return []
        mother = person.mother
        father = person.father
        cousins = []
        mother_sibling = Family.get_brothers(mother) + Family.get_sisters(mother)
        for sibling in mother_sibling:
            cousins.extend(Family.get_children(sibling))
        father_sibling = Family.get_brothers(father) + Family.get_sisters(father)
        for sibling in father_sibling:
            cousins.extend(Family.get_children(sibling))
        return cousins

    @staticmethod
    def get_grand_daughter(person):
        offsprings = person.sons + person.daughters
        grand_daughters = []
        for person in offsprings:
            grand_daughters.extend(person.daughters)
        return grand_daughters

    @staticmethod
    def get_mother(person):
        if person.mother:
            return [person.mother]
        return []

    @staticmethod
    def get_father(person):
        if person.father:
            return [person.father]
        return []

    @staticmethod
    def get_sons(person):
        return person.sons

    @staticmethod
    def get_daughters(person):
        return person.daughters
