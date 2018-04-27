
class Person:
    """
    information about person his parents, sister and brother
    """
    brothers = []
    sisters = []

    def __init__(self, name, sex, mother=None, father=None):
        """
        assigns parents for the person
        :param name:name of person, who is going to be added as son and daughter
        :param sex: sex of person "M" for male, "F" for female
        :param mother: mother as a instance of Person class
        :param father: Father as a instance of Person class
        """
        self.name = name
        self.sex = sex
        self.mother = mother
        self.father = father
        self.sons = []
        self.daughters = []
        self.spouse = None
        self.generation = None

    def add_child(self, child):
        """
        adds son into persons son's list
        :param child: child as a instance of Person class
        """
        if child.sex == "M":
            self.sons.append(child)
        else:
            self.daughters.append(child)

    def add_spouse(self, spouse):
        """
        adds a person as spouse of this person
        :param spouse: a Person instance of a person, who is going to get married to this person
        """
        self.spouse = spouse
