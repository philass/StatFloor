# Class for a player. Encapsulates Retrieving there data, from
# baseball reference. 


import pids


class Batter:
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.bref_id = playerid_lookup(last_name, first_name)

  def get_logs(self, start_date, end_data):
    """
    Get game Logs from start date to end Date

    """

    # Check if needed data exists in file system

    # If it does not

    # download from bbreference (Might be done with previous code)
    
    #read CSV Logs

    return logs

  
  def next_oppenent(self):
    """
    Get Next team
    """
    return None

    



    



 
