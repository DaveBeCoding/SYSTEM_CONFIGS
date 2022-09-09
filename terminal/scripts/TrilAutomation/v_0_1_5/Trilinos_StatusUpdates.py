#/usr/bin/env python3

"""
      Trilinos Status Table Automation Script
      
      tablestatus.py <pr_status, pr_merged, failed_pr, 
                                waiting_pr, open_pr, mm_status, successful_mm, jira_ticket>
"""
from ast import If
from datetime import timedelta
import pytablewriter as ptw
from datetime import date
import sys
# import io # part of optional code output below

def main():
    # PR_STATUS = create a list using using kwargs/args -> 0 == success, 1 == warning 3 == failure
    mm_status = [":white_check_mark:", ":warning:", ":x:"]
    pr_status = [":white_check_mark:", ":warning:", ":x:"]
    status_example = ":white_check_mark:"
    
    stat_container = sys.argv[1:] # 8 args
   
   # Get today's date
    today = date.today()
    
   # Yesterday date
    yesterday = today - timedelta(days = 1)
    
    try:
        # pr_status[int(stat_container[0])] # 3 flavors
        number_of_pr_merged = stat_container[1]
        number_of_failed_pr = stat_container[2]
        number_of_waiting_pr = stat_container[3]
        number_open_pr = stat_container[4]
        # mm_status[int(stat_container[5])] # 3 flavors
        number_of_successful_mm = stat_container[6]
        jira_ticket_number = stat_container[7]
    except:
        print("Requires more arguments ... Example: Trilinos_StatusUpdates.py 0 1 6 4 72 0 0 435")
    try:
        NUMBER_OF_PRs_MERGED = "["+number_of_pr_merged+"]"+"(https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A"+str(yesterday)+"T12%3A00%3A00-07%3A00.."+str(today)+"T12%3A00%3A00-07%3A00+base%3Adevelop)"
        NUMBER_OF_FAILED_PRs = "["+number_of_failed_pr+"]"+"(https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A"+str(yesterday)+"T12%3A00%3A00-07%3A00.."+str(today)+"T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)"
        NUMBER_OF_PRs_WAITING = "["+number_of_waiting_pr+"]"+"(https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A"+str(yesterday)+"T12%3A00%3A00-07%3A00.."+str(today)+"T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)"
        NUMBER_SUCCESSFUL_MM = "["+number_of_successful_mm+"]"+"(https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A"+str(yesterday)+"T12%3A00%3A00-07%3A00.."+str(today)+"T12%3A00%3A00-07%3A00+base%3Amaster+)"
        JIRA_TICKETS = "[TrilFrame-"+jira_ticket_number+"]"+"(https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"
                    # = "["TrilFrame-435](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"
    except:
        print("Missing required argument(s)... Example: Trilinos_StatusUpdates.py 0 1 6 4 72 0 0 435")
   
    # npr_merge = "["+pr_merge_count+"]"+"(https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A"+start_date+"T12%3A00%3A00-07%3A00.."+end_date+"T12%3A00%3A00-07%3A00+base%3Adevelop)"
    
    try:
        writer = ptw.MarkdownTableWriter(
              table_name="Trilinos Status Table",
              headers=["Date", "PR Status", "Number of PRs Merged", "Number of Failed PRs", "Number of PRs Waiting for Build & Test", "Total Numbr of Open PRs", "MM Status", "Number of Successful Master Merges","Jira Ticket #"],
              value_matrix=[
                    [str(today), pr_status[int(stat_container[0])], NUMBER_OF_PRs_MERGED, NUMBER_OF_FAILED_PRs, NUMBER_OF_PRs_WAITING, number_open_pr , mm_status[int(stat_container[5])], NUMBER_SUCCESSFUL_MM, JIRA_TICKETS]
              ],
          )
    except:
        print("Not enough arguments ... Example: Trilinos_StatusUpdates.py 0 1 6 4 72 0 0 435")
    #change the output stream to terminal 
    # writer.stream = io.StringIO()
    # writer.write_table()
    # print(writer.stream.getvalue())

    # change the output stream to a file
    try:
        with open("Trilinos_Table_Updates.md", "w") as f:
            writer.stream = f
            writer.write_table()
    except:
        print("Can not write to file, missing arguements ... Example: Trilinos_StatusUpdates.py 0 1 6 4 72 0 0 435")
    # or you can use dump method to file if you just output a table to a file
    # writer.dump("sample.md")


if __name__ == "__main__":
    main()