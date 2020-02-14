"""
Contains functionality for representing a pitcher
and for getting the data of the player from baseball reference
"""


class Pitcher:
    """
    Class for representing a pitcher
    """
    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name
        #self.bref_id = playerid_lookup(last_name, first_name)

    def get_logs(self, start_date, end_date):
        """
        Get pitchers Game Logs from start date
        to end date
        """
        return (self, start_date, end_date)
