from datetime import datetime


class Golfer:
    """
    Golfer object derived from data in the golfersInput.csv

    Instance variables:
        golfer_id          a unique id for this golfer (to be used as a primary key when stored in the database)
        golfer_name        the name for the golfer
        golfer_birthdate   the golfers birthdate
                           NOTE: golfersInput.csv has this field in the format 'mm-dd-yy',
                                 but the database expects it in the format 'YYYY-mm-dd', so it needs converted

    """
    # Please provide your definition here from Project 1-A
    def __init__(self, golfer_id, name, bday):
        """
        constructor of class Golfer
        """
        self.__golfer_id = golfer_id
        self.__golfer_name = name
        self.__golfer_birthdate = self.to_SQL_date(bday)

    # Please complete the following functions

    # get_golfer_id

    def get_golfer_id(self):
        return self.__golfer_id

    # get_golfer_name

    def get_golfer_name(self):
        return self.__golfer_name

    # get_golfer_birthdate

    def get_golfer_birthdate(self):
        return self.__golfer_birthdate

    # to_SQL_date(self, bday)

    def to_SQL_date(self, bday):
        date_type = "%m-%d-%y"

        converted_date = datetime.strptime(bday, date_type)

        converted_date = converted_date.date()

        return str(converted_date)

    def __str__(self):
        return "{},{},{}".format(self.__golfer_id,
                                   self.__golfer_name, self.__golfer_birthdate)