import os
import csv

from golfCourse import GolfCourse
from hole import Hole
from golfer import Golfer
from tournGolfer import TournGolfer
from tournament import Tournament
from round import Round
from golferRoundScores import GolferRoundScores

from golfTourDatabaseHelper import GolfTourDatabaseHelper


def main():
    """
    Algorithm:
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 golf courses
    4.  Call create_holes function, passing in the golf_course_holes_dict
        and retrieving the returned holes_list,
        a list of Hole objects containing information for 90 golf course holes
    5.  Call create_golfers function, passing in the input
        file name, and retrieving the returned golfer_list,
        a list of Golfer objects containing information for 30 golfers
    6.  Write out the class objects to files from:
        crate_golf_courses, create_holes, create_golfers
        ---------------------------------------------------------
    7.  Call create_tournaments function, passing in the input
        file name, and retrieving the returned tournament_list,
        a list of Tournament objects containing information for 15 tournaments
        and a tournament golfers dictionary, tournament_golfers_dict,
        whose key is the tourn_id and the value is the list of golfers
        playing in that tournament
    8.  Call create_rounds function, passing in the tournament_list from above,
        and retrieving the returned rounds_list,
        a list of Round objects containing information for 45 tournament rounds
    9.  Call create_tourn_golfers function, using the tournament_golfers_dict
        and the golfer_list from above, retrieving the returned tourn_golfers_list
        a list of TournGolfer objects containing information for 225 tournament golfers
    10. Write out the class objects to files from:
        create_tournaments, create_rounds, create_tourn_golfers
        ---------------------------------------------------------        
    11. Call create_golfer_scores function, passing in the round scores input
        file name, golfer_list returned from the create_golfers
        function, tournament_list returned from the create_tournaments
        function, and tourn_golfers_list returned from the
        create_tourn_golfers function, and retrieving the
        returned golfer_scores_list
    12. Write out the class objects to files from:
        create_golfer_scores
        ---------------------------------------------------------
    13. Remove the database, if it already exists
    14. Create a GolfTourDatabaseHelper object
    15. Use the GolfTourDatabaseHelper object to create
        the database and to create the tables.
    16. Use the GolfTourDatabaseHelper object to populate database tables
    17. Close the database connection
        ---------------------------------------------------------
    18. Write the following functions to query the database
        show_golf_course_last3_holes (database_name)
        show_tourn_scores_top5_Apex3 (database_name)
        show_golf_course_par5_holes (database_name)
        show_tournaments_for_golfer_Jo (database_name)
     """

    print("Wake Golf Tour Project 1")

    # 1. Initialize the input and output file names

    golf_courses_infile = "golfCoursesInput.csv"
    golfers_infile = "golfersInput.csv"
    tournaments_infile = "tournamentsInput.csv"
    golfer_scores_infile = "roundScoresInput.csv"

    golf_courses_file = "golfCourses.csv"
    holes_file = "holes.csv"
    golfers_file = "golfers.csv"
    tournaments_file = "tournaments.csv"
    tourn_golfers_file = "tournGolfers.csv"
    rounds_file = "rounds.csv"
    golfer_scores_file = "golferRoundScores.csv"

    # 2. Initialize the database and table names for output

    database_name = "WakeGolfTour.db"
    golf_courses_table = "GolfCourse"
    holes_table = "Hole"
    golfers_table = "Golfer"
    tournaments_table = "Tournament"
    tourn_golfers_table = "TournGolfer"
    rounds_table = "Round"
    golfer_scores_table = "GolferRoundScores"

    # 3. Call create_golf_courses function, passing in the input
    #    file name, and retrieving the returned golf_courses_list,
    #    a list of 5 golf course objects and the golf_course_holes_dict,
    #    containing information about the holes for each of the golf courses

    golf_course_list, golf_course_holes_dict = create_golf_courses(golf_courses_infile)

    # 4. Call create_holes function, passing in the golf_course_holes_dict
    #    and retrieving the returned holes_list,
    #    a list of Hole objects containing information for 90 golf course holes

    holes_list = create_holes(golf_course_holes_dict)

    # 5. Call create_golfers function, passing in the input
    #    file name, and retrieving the returned golfer_list,
    #    a list of 30 golfer objects

    golfer_list = create_golfers(golfers_infile)

    # 6. Write out the lists returned from the create functions:
    #    create_golf_courses, create_golfers, create_tournaments

    write_objs_to_file(golf_courses_file, golf_course_list)
    write_objs_to_file(holes_file, holes_list)
    write_objs_to_file(golfers_file, golfer_list)

    # 7. Call create_tournaments function, passing in the input
    #    file name and golf_course_list, retrieving the returned tournament_list,
    #    a list of 15 tournament objects, and a dictionary with the tourn_id as the key
    #    and a list of golfers for that tournament as the value

    tournament_list, tourn_golfers_dict = create_tournaments(tournaments_infile, golf_course_list)

    # 8. Call create_rounds function, passing in the input
    #    file name and the tournament_list, retrieving the returned rounds_list,
    #    a list of Round objects

    rounds_list = create_rounds(tournament_list)

    # 9. Call create_tourn_golfers function, using tourn_golfers_dict
    #    and the golfers_list, retrieving the returned tourn_golfers_list,
    #    a list of TournGolfer objects

    tourn_golfers_list = create_tourn_golfers(tourn_golfers_dict, golfer_list)

    # 10. Write out the lists returned from the create functions:
    #    create_holes, create_rounds, create_tourn_golfers

    write_objs_to_file(tournaments_file, tournament_list)
    write_objs_to_file(rounds_file, rounds_list)
    write_objs_to_file(tourn_golfers_file, tourn_golfers_list)
    
    # 11. Call create_golfer_scores function, passing in the
    #     golfer_scores_list returned from the read_golfer_scores
    #     function, golfers_list returned from the read_golfers
    #     function, tourns_list returned from the create_tournaments
    #     function, rounds_list returned from the create_rounds
    #     function, and the tourn_golfers_list returned from the
    #     create_tourn_golfers function, and retrieving the
    #     returned golfer_scores_list

    golfer_scores_list = create_golfer_scores(golfer_scores_infile,
                                              golfer_list,
                                              tournament_list,
                                              rounds_list,
                                              tourn_golfers_list)

    # 12. Write out the class objects to a file from:
    #     create_golfer_scores

    write_objs_to_file(golfer_scores_file, golfer_scores_list)
    print()
    
    # 13. Remove the database, if it already exists

    if os.path.exists(database_name):
        os.remove(database_name)

    # 14. Create a GolfTourDatabaseHelper object

    db_helper = GolfTourDatabaseHelper(database_name)

    # 15. Use the GolfTourDatabaseHelper object to create
    #     the database and to create the tables.

    db_helper.create_database()

    # 16. Use the GolfTourDatabaseHelper object to populate database tables

    db_helper.save_to_database(golf_courses_table, golf_courses_file)
    db_helper.save_to_database(holes_table, holes_file)
    db_helper.save_to_database(golfers_table, golfers_file)
    db_helper.save_to_database(tournaments_table, tournaments_file)
    db_helper.save_to_database(tourn_golfers_table, tourn_golfers_file)
    db_helper.save_to_database(rounds_table, rounds_file)
    db_helper.save_to_database(golfer_scores_table, golfer_scores_file)

    # 17. Close the database connection

    db_helper.close_connection()

    # 18. Write the following functions to query the database

    show_golf_course_last3_holes(database_name)
    show_tourn_scores_top5_Apex3(database_name)
    show_golf_course_par5_holes(database_name)
    show_tournaments_for_golfer_Jo(database_name)
    
    # Add the call to your own function here:
    show_my_query(database_name)
     
    
def create_golf_courses(filename):
    """
    Each line of input contains:
    golf_course_name, par_h1, par_h2, ..., par_h18

    where golf_course_name is the name of the golf course and each
          par_h# is a par value for the hole #.
    
    Note: string input needs to be stripped of any whitespace
             integer strings need to be changed to ints 

    Create a new GolfCourse object containing 
        golf_course_id, golf_course_name, total_par
          
    Return a list,  where each element is a GolfCourse object
    """

    print("\nGolf Course List: golf_course_list\n")

    # 1. Create an empty list called golf_course_list that will contain
    #    GolfCourse objects whose data comes from the input file

    golf_course_list = []

    # 2. Create an empty dictionary called golf_course_holes_dict
    #    whose key is the golf_course_id and the value is a tuple
    #    containing hole_number and par_value
    
    golf_course_holes_dict = dict()

    # 3. Initialize the golf_course_id to 1

    golf_course_id = 1

    # 4. Use a try/except block to capture a File Not Found Error

    try:
        # a. Open the input_file object for reading the input file

        input_file = open(filename, 'r')

        # b. Call the csv.reader function, passing in the input file
        #    and capturing the CSV file contents.

        file_lines = csv.reader(input_file)

        # c. Create a list from the file contents: courses_list

        courses_list = list(file_lines)

        # d. Create an outer loop to read each golf course in
        #    courses_list

        for golf_course in courses_list:

            # Outer Loop
            # 1. The first element (golf course name) is stripped
            #    of whitespace.

            golf_course_name = golf_course[0].strip()

            # 2. Create an inner loop to traverse the 18 hole
            #    par values using the range function

            total_par = 0
            holes = []
            for i in range(1,19):
                # Inner Loop
                # a. Convert the string hole par values to ints
                par = int(golf_course[i])

                # b. Add value to total par
                total_par = total_par + par

                # c. Append hole_num and par to list for dictionary
                holes.append((i, par))

            # 3. Add entry for this golf course's holes to the golf_course_holes_dict
            golf_course_holes_dict[golf_course_id] = holes

            # 4. Create a new GolfCourse object, call it golf_course,
            #    passing in golf_course_id, golf_course_name, and total_par

            golf_course = GolfCourse(golf_course_id, golf_course_name, total_par)

            # 5. Append the golf_course object to the golf_course_list

            golf_course_list.append(golf_course)

            # 6. Increment the golf_course_id

            golf_course_id = golf_course_id + 1

        # e. Close input_file object

        input_file.close()

    except IOError:
        print("File Not Found Error.")

    # 5. Print the golf_course_list objects to the console

    for gc in golf_course_list:
        print(gc)

    # 6. Return the golf_course_list and golf_course_holes_dict

    return golf_course_list, golf_course_holes_dict
    
    
def create_holes(golf_course_holes_dict):
    """
    Use the dictionary created in the create_golf_courses function
    to create a list of Hole objects. The dictionary has golf_course_id as the key,
    and a list of 18 tuples containing (hole_num, par_value) as the value
        Each entry will have:
         golf_course_id: [(hole_num, par_value), 
                          (hole_num, par_value), ..., 
                          (hole_num, par_value)]
                                 
    Create a Hole object for each hole_num and par_value
    containing - 
        hole_id, golf_course_id, hole_num, and par_value

    Return a list,  where each element is a Hole object
                                 
    """
    print("\nThe Hole object list:\n")
    
    #  Create an empty list called holes_list 
    holes_list = []

    hole_id = 1
    for golf_course_id, hole_info in golf_course_holes_dict.items():
        for hole_num, par in hole_info:
            hole = Hole(hole_id, golf_course_id, hole_num, par)
            holes_list.append(hole)
            hole_id += 1

    for hole_info in holes_list:
        print(hole_info)

    return holes_list


def create_golfers(filename):
    """
    Each line of input contains:
    golfer_name, golfer_birthdate

    where golfer_name is the name of the golfer and
          golfer_birthdate is the day the golfer was born.

    Note: string input needs to be stripped of any whitespace

    Create a Golfer object from each line in the input file:
    containing -
    golfer_id, golfer_name, golfer_birthdate

    A list is returned, where each element is a Golfer object

    """
    print ("\nThe Golfer object list:\n")


    golfer_list = []
    golfer_id = 1
    try:
        input_file = open(filename, 'r')
        file_lines = csv.reader(input_file)
        golfer_input_list = list(file_lines)

        for golfer_name, golfer_birthdate in golfer_input_list:
            golfer_name = golfer_name.strip()

            golfer_birthdate = golfer_birthdate.strip()

            player = Golfer(golfer_id, golfer_name, golfer_birthdate)

            golfer_list.append(player)

            golfer_id = golfer_id + 1

        input_file.close()
    except IOError:
        print("File Not Found Error.")

    for golfer_info in golfer_list:
        print(golfer_info)

    return golfer_list

def create_tournaments(filename, golf_course_list):
    """
    The tournamentsInput.csv has two different record types in the file.
    Hint: Open the file and see how it is organized.
    The first record type has

    golf_course_name, tourn_name, start_date, num_rounds, num_golfers

    where golf_course_name is the name of the golf course,
          tourn_name is the name of the tournament,
          start_date is the first day of the tournament,
          num_rounds is the number of rounds played in this tournament, and
          num_golfers is the number of golfers playing in this tournament

    The second record type is just a single golfer name.
    The number of these records is specified by the num_golfers field from the first record type
        golfer1_name
        golfer2_name
        ...
        golfer15_name

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Create a Tournament object 
    containing - 
        golfer_id, golfer_name, golfer_birthdate

    Create dictionary entry value for this tourn_id_key, 
        the value is a list to be filled in with the golfer names 
        as they are read from the input file. 
   
    Return the tournament_list and tourn_golfers_dict
    """
    print("\nThe Tournament object list:\n")

    golf_course_name_to_id = dict()
    for item in golf_course_list:
        # golf_course name will be the golf_course_list[1]
        golf_course_name = GolfCourse.get_course_name(item)
        # golf_course_id will be the golf_course_list[0]
        golf_course_id = GolfCourse.get_course_id(item)
        golf_course_name_to_id.update({golf_course_name: golf_course_id})

    # Create an empty list called tournament_list
    tournament_list = []

    # Create an empty dictionary called tourn_golfers_dict
    tourn_golfers_dict = dict()

    tourn_id = 1

    tourn_id_key = 0

    try:
        input_file = open(filename, 'r')
        file_lines = csv.reader(input_file)
        tournament_input_list = list(file_lines)
        for tourn_info in tournament_input_list:
            if len(tourn_info) > 1:  # Processing tournement records

                course_name = tourn_info[0].strip()
                tourn_name = tourn_info[1].strip()
                start_date = tourn_info[2].strip()
                num_rounds = int(tourn_info[3].strip())
                num_golfers = int(tourn_info[4].strip())
                golf_course_id = golf_course_name_to_id[course_name]

                tournament = Tournament(tourn_id, tourn_name, golf_course_id, start_date, num_rounds, num_golfers)

                tournament_list.append(tournament)
                tourn_id_key = tourn_id
                golfer_names = []
                tourn_golfers_dict.update({tourn_id_key: golfer_names})
                tourn_id = tourn_id + 1

            elif len(tourn_info) == 1:  # Processing Golfer Records
                golfer_name = tourn_info[0].strip()
                golfer_names.append(golfer_name)
        input_file.close()

    except IOError:
        print("File Not Found Error.")

        # 5. Print the tournament_list objects to the console
    for tourn in tournament_list:
        print(tourn)

        # 6. Return the tournament_list and tourn_golfers_dict
    return tournament_list, tourn_golfers_dict

def create_rounds(tournament_list):
    """
    Use the tournament_list object list, that was
    returned from the create_tournaments function, which
    contains 15 Tournament objects with the following
    instance variables:

    tourn_id, tourn_name, golf_course_id, start_date,
    num_rounds, num_golfers, golfers...

    Create num_rounds Round objects from every
    Tournament object element in tournament_list:
    Add in the following as instance variables values

    round_id, tourn_id, day

    A list is returned, where each element is a Round object

    """
    print("\nThe Round object list\n")
    rounds_list = []

    round_id = 1

    for tourn in tournament_list:
        number_rounds = Tournament.get_num_rounds(tourn)
        tourn_id = Tournament.get_tourn_id(tourn)

        num_rounds = number_rounds

        for item in range(number_rounds):
            if num_rounds == 4:
                day = "Thu"
            elif num_rounds == 3:
                day = "Fri"
            elif num_rounds == 2:
                day = "Sat"
            elif num_rounds == 1:
                day = "Sun"

            num_rounds = num_rounds - 1

            round = Round(round_id, tourn_id, day)

            rounds_list.append(round)

            round_id = round_id + 1

    for round_info in rounds_list:
        print(round_info)

    return rounds_list


def create_tourn_golfers(tourn_golfers_dict,  golfer_list):
    """
    Use the tourn_golfers_dict, that was
    returned from the create_tournaments function, which contains
    entries with the key being the tourn_id, and the value is a list following format:
    of golfer_names

    Use the golfers_list object list parameter, that was
    returned from the create_golfers function, which
    contains 30 Golfer objects with the following instance
    variables:

    golfer_id, golfer_name, golfer_birthdate

    Create a TournGolfer object from every golfer_name listed
    in the tourn_golfers_dict.
    Add in the following as instance variables values -

        tourn_golfer_id, tourn_id, golfer_id

    A list is returned, where each element is a TournGolfer object
    
    """

    print("\nThe TournGolfer object list\n")
    golfer_name_to_id = {}
    for item in golfer_list:
        # golfer_name will be the golfer_list[1]
        golfer_name = Golfer.get_golfer_name(item)
        # golfer_id will be the golfer_list[0]
        golfer_id = Golfer.get_golfer_id(item)
        golfer_name_to_id.update({golfer_name: golfer_id})

    tourn_golfers_list = []
    tourn_golfer_id = 1

    for tournament_id, golfer_name_list in tourn_golfers_dict.items():

        for golfer_name in golfer_name_list:
            golfer_id = golfer_name_to_id[golfer_name]
            tourn_golfer = TournGolfer(tourn_golfer_id, tournament_id, golfer_id)
            tourn_golfers_list.append(tourn_golfer)
            tourn_golfer_id = tourn_golfer_id + 1
    for tg in tourn_golfers_list:
        print(tg)

    return tourn_golfers_list

    
def create_golfer_scores(filename, golfer_list, tournament_list,
                         rounds_list, tourn_golfers_list):
    """
    Create GolferRoundScores objects from data in the input file,
    and using previously created object lists to convert names to ids.

    Each line of input contains:
        golfer_name, tourn_name, day, score_h1, score_h2, ..., score_h18

    where golfer_name is the name of the golfer,
          tourn_name is the name of the tournament,
          day is the round day,
          and each score_h# is the golfer's score for that hole

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Use the golfers_list parameter, that was
    returned from the create_golfers function, with the
    following instance variables:

        golfer_id, golfer_name, golfer_birthdate

    Use the tourns_list parameter, that was
    returned from the create_tournaments function, with the
    following instance variables:

        tourn_id, tournament_name, golf_course_id, start_date,
        num_rounds, and num_golfers

    Use the rounds_list object list parameter, that was
    returned from the create_rounds function, with the
    following instance variables:

        round_id, tourn_id, day

    Use the tourn_golfers_list parameter, that was
    returned from the create_tourn_golfers function, with the
    following instance variables:

        tourn_golfers_id, tourn_id, golfer_id

    Create a GolferRoundScores object from every entry in the
    golfer_scores_list:  Add in the following as instance
    variables values:

        golfer_scores_id, tourn_golfer_id, round_id, total_round_score,
        and a list of scores (score_h1, score_h2, ..., score_h18)

    A list is returned, where each element is a GolferRoundScore object

    """

    print("\nThe GolferRoundScores object list\n")
    # dictionaries init
    golfer_name_to_id = dict()
    tourn_name_to_id = dict()

    # Initial list
    round_scores_list = []

    # Initial values
    golfer_scores_id = 1

    # Populate the lookup dictionaries
    for golfer_object in golfer_list:
        golfer_name_to_id[golfer_object.get_golfer_name().strip()] = golfer_object.get_golfer_id()

    for tourn_object in tournament_list:
        tourn_name_to_id[tourn_object.get_tourn_name().strip()] = tourn_object.get_tourn_id()

    try:
        # Open a file
        score_file = open(filename, 'r')

        # Call the csv reader and and populate a list
        golfer_scores_list = list(score_file)

        # Close file
        score_file.close()
    except IOError:
        print("File Not Found Error.")

        # Outer loop to read each set of scores in 'golfer_scores_list'
    for golfer_info in golfer_scores_list:
        golfer_info = golfer_info.split(',')
        golfer_name = golfer_info[0].strip()
        tourn_name = golfer_info[1].strip()
        day = golfer_info[2].strip()
        scores_list = golfer_info[3:]
        scores_list = list(map(int, scores_list))
        golfer_id = golfer_name_to_id[golfer_name]
        tourn_id = tourn_name_to_id[tourn_name]
        round_id = get_round_id(rounds_list, tourn_id, day)
        tourn_golfer_id = get_tourn_golfer_id(tourn_golfers_list, tourn_id, golfer_id)
        total_round = sum(scores_list)
        golfer_scores = GolferRoundScores(golfer_scores_id, tourn_golfer_id, round_id, total_round, scores_list)
        round_scores_list.append(golfer_scores)
        golfer_scores_id = golfer_scores_id + 1

    # Print the round_scores_list objects to the console.
    for rs in round_scores_list:
        print(rs)

    return round_scores_list


def get_tourn_golfer_id(tourn_golfers_list, tourn_id, golfer_id):
    """
    Helper function to get the tourn_golfer_id
    based on the specified tourn_id and golfer_id
    """

    for tourn_golfer in tourn_golfers_list:
        if tourn_golfer.get_golfer_id() == golfer_id:
            if tourn_golfer.get_tourn_id() == tourn_id:
                return tourn_golfer.get_tourn_golfer_id()

    # tg not found - just return 0
    return 0


def get_round_id(rounds_list, tourn_id, tourn_day):
    """
    Helper function to get the round_id
    based on the specified tourn_id and tourn_day

    """
    for golfer_round in rounds_list:
        if golfer_round.get_tourn_id() == tourn_id:
            if golfer_round.get_day() == tourn_day:
                return golfer_round.get_round_id()

        # gr not found - just return 0
    return 0


def write_objs_to_file(filename, object_list):
    """
    This function takes a nested_list as input and writes it
    out to a csv file, where each line is a inner list

    """
    # 1. Open the output file object for writing

    output_file = open(filename, 'w')

    # 2. Create a loop to traverse the object_list parameter,
    #    where the loop variable is each object in the list:

    for obj in object_list:
        # Loop:
        # a. Set a str_obj string variable to the result of
        #    converting 'object' to a string using the
        #    __str__ method of the output file.  This can be
        #    accomplished by passing the object into the
        #    str() function.

        str_obj = str(obj)

        # b. Add a new line character to the end of the
        #     str_obj string

        str_obj += '\n'

        # c. Use the write method of the output file object
        #    to write the str_obj string to the output file,

        output_file.write(str_obj)

    # 3. Close the output file

    output_file.close()


def show_golf_course_last3_holes(database_name):
    """
    Show a list of golf course names with the total par
    and the hole number and par for the last 3 holes
    """

    print("\nLast 3 holes, of each golf course\n")

    # Get a cursor for the connection

    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query

    sql = '''
            select course_name, course_total_par,
                  hole_number, hole_par
            from GolfCourse join Hole
            on course_id = hole_course_id
            where hole_number > 15
        '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()


def show_tourn_scores_top5_Apex3(database_name):
    """
    Show the total tournament scores for the top
    five golfers, who played the 'Apex 3' tournament
    """

    print("\nTotal Scores For Top 5 Golfers in Apex 3 Tournament\n")

    # Get a cursor for the connection

    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query

    sql = '''
        select golfer_name, tourn_name, sum (grs_total_score) as total
           from GolferRoundScores
              join TournGolfer on
                   grs_tourn_golfer_id = tg_id
              join Golfer on
                   tg_golfer_id = golfer_id
              join Tournament on
                   tg_tourn_id = tourn_id
           where tourn_name = 'Apex 3'
           group by grs_tourn_golfer_id
           order by tourn_name, total
           limit 5
    '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()
    
    # Close the cursor and the database connection
    c.close()
    database_connection.close()


def show_golf_course_par5_holes(database_name):
    """
    Show a list of golf course names with the total par
    and the hole number and par for each hole where the
    par is equal to 5: 
    """
    
    print("\nShow the Par 5 Hole Numbers For Each Golf Course\n")

    # Get a cursor for the connection

    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query

    sql = '''
            select course_name, course_total_par,
                  hole_number, hole_par
            from GolfCourse join Hole
            on course_id = hole_course_id
            where hole_par = 5
        '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()


def show_tournaments_for_golfer_Jo(database_name):
    """
    Show a list of tournaments and golfer names played by golfers
    whose name begins with Jo: 
    """

    print("\nTournaments Played by Golfer's Whose Name Begins With Jo\n")
    
    # Please provide your code here
    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    # Create SQL query

    sql = '''
            select distinct golfer_name, tourn_name
               from GolferRoundScores
                  join TournGolfer on
                       grs_tourn_golfer_id = tg_id
                  join Golfer on
                       tg_golfer_id = golfer_id
                  join Tournament on
                       tg_tourn_id = tourn_id
               where golfer_name LIKE 'Jo%'
               order by golfer_name
        '''

    # Execute query and display results
    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()

    
def show_my_query(database_name):
    """
    Show data from the golf tour database
    """

    print("\nData from my query\n")
    
    # Please provide your code here from Discussion Board Assignment
    dbhelper = GolfTourDatabaseHelper(database_name)
    database_connection = dbhelper.get_connection(database_name)
    c = database_connection.cursor()

    sql = '''
                select distinct golfer_name, tourn_name
                   from GolferRoundScores
                      join TournGolfer on
                           grs_tourn_golfer_id = tg_id
                      join Golfer on
                           tg_golfer_id = golfer_id
                      join Tournament on
                           tg_tourn_id = tourn_id
                   where tourn_name LIKE 'WTCC%'
                   order by tourn_name
            '''

    for row in c.execute(sql):
        print(row)
    print()

    # Close the cursor and the database connection
    c.close()
    database_connection.close()


main()
