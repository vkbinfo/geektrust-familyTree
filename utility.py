

class Utility:

    @staticmethod
    def connect_new_born_to_parent(child, parents):
        """
        Connects a child(a Person object) to its parents(adding into sons and daughters list)
        :param child: Child who is going to get added into list of sons or daughters
        :param parents: list of parents of child
        """
        if child.sex == "M":
            for parent in parents:
                parent.sons.append(child)
        else:
            for parent in parents:
                parent.daughters.append(child)



