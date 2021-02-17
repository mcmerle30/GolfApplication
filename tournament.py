from datetime import datetime


class Tournament:
    """
    Tournament object derived from data in the tournamentsInput.csv

    Instance variables:
        tourn_id       a unique id for this tournament (to be used as a primary key when stored in the database)
        tourn_name     the name for the tournament
        course_id      the id of the golf course where the tournament was played
        start_date     the date of the first round of this tournament
                       NOTE: tournamentsInput.csv has this field in the format 'm-dd-yy',
                             but the database expects it in the format 'YYYY-mm-dd',
                             so it needs converted

        num_rounds     number of rounds for this tournament (2, 3, or 4)
        num_golfers     number of golfers that played in the tournament

    """
    # Please provide your definition here from Project 1-B
    def __init__(self, tourn_id, name, course_id, start_date,
                 num_rounds, num_golfers):
        """
        constructor of class Tournament
        """
        self.__tourn_id = tourn_id
        self.__tourn_name = name
        self.__course_id = course_id
        self.__start_date = self.to_SQL_date(start_date)
        self.__num_rounds = num_rounds
        self.__num_golfers = num_golfers

    # get_tourn_id

    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    # get_tourn_name

    def get_tourn_name(self):
        """
        return the tourn_name to the caller
        """
        return self.__tourn_name

    # get_course_id

    def get_course_id(self):
        """
        return the course_id to the caller
        """
        return self.__course_id

    # get_start_date

    def get_start_date(self):
        """
        return the start_date to the caller
        """
        return self.__start_date

    # get_num_rounds

    def get_num_rounds(self):
        """
        return the num_rounds to the caller
        """
        return self.__num_rounds

    # get_num_golfers

    def get_num_golfers(self):
        """
        return the num_golfers to the caller
        """
        return self.__num_golfers

    # to_SQL_date(self, start_date):

    def to_SQL_date(self, start_date):
        """
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        return the converted date
        """
        date_type = "%m-%d-%y"

        converted_date = datetime.strptime(start_date, date_type)

        converted_date = converted_date.date()

        return str(converted_date)

    #  __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_str = "{0},{1},{2},{3},{4},{5}".format(
            self.__tourn_id, self.__tourn_name, self.__course_id, self.__start_date, self.__num_rounds,
            self.__num_golfers)
        return csv_str
