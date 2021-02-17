class Hole:
    """
    Hole object derived from data in the golfCoursesInput.csv

    Instance variables:
        hole_id         a unique id for this hole (to be used as a primary key when stored in the database)
        course_id      the id of the golf course where this hole is played
        hole_num        the number of the hole (1-18)
        par             the par value for this hole (3,4, or 5)
    """
    # Please provide your definition here from Project 1-A
    # __init__
    def __init__(self, hole_id, course_id, h_num, par):
        self.__hole_id = hole_id
        self.__course_id = course_id
        self.__hole_num = h_num
        self.__par = par

    # get_hole_id
    def get_hole_id(self):
        return self.__hole_id

    # get_course_id
    def get_course_id(self):
        return self.__course_id

    # get_hole_num
    def get_hole_num(self):
        return self.__hole_num

    # get_par
    def get_par(self):
        return self.__par

    # __str__
    def __str__(self):
        csv_str = "{0},{1},{2},{3}".format(self.__hole_id, self.__course_id,
                                           self.__hole_num, self.__par)
        return csv_str
