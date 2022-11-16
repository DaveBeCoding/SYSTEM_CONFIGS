#/usr/bin/env python3

"""
      Trilinos Status Table Automation Script
"""

import io
import pytablewriter as ptw

def main():
    status = ":white_check_mark:"
    

   #generate end date and start date based on current time -> check module(s) "dates"
   #add script Args/kwargs for pr merge count failed, waiting pr count, open pr count, Successful mm count, Jira-ticket#
   #status -> args . PR_status MM_Status

    test_date = "3031-99-88"  
    end_date = "2022-09-01"
    start_date = "2022-08-31"
    #replace date spread with var
    
    pr_merge_count = str(-1)

    npr_merge = "["+pr_merge_count+"]"+"(https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A"+start_date+"T12%3A00%3A00-07%3A00.."+end_date+"T12%3A00%3A00-07%3A00+base%3Adevelop)"

    # writer = ptw.MarkdownTableWriter(
    #       table_name="Trilinos Status Table",
    #       headers=["Date", "PR Status", "Number of PRs Merged", "Number of Failed PRs", "Number of PRs Waiting for Build & Test", "Total Numbr of Open PRs", "MM Status", "Number of Successful Master Merges","Jira Ticket #"],
    #       value_matrix=[
    #           [test_date,   status,      npr_merge, "[3](https://tinyurl.com/2kd9ygc7)",   "[6](https://tinyurl.com/2kd9ygc7)", 64, ":white_check_mark:", "[0](https://tinyurl.com/2kd9ygc7)", "[TrilFrame-423](https://tinyurl.com/2kd9ygc7)"],
    #           [end_date,   status,      npr_merge, "[3](https://tinyurl.com/2kd9ygc7)",   "[6](https://tinyurl.com/2kd9ygc7)", 64, ":white_check_mark:", "[0](https://tinyurl.com/2kd9ygc7)", "[TrilFrame-423](https://tinyurl.com/2kd9ygc7)"],
    #           ["23 Aug 2022",   ":warning:",      4, 3,   6, 64, ":white_check_mark:", 0, "TrilFrame-405"],
    #           ["22 Aug 2022",   ":x:",      4, 3,   6, 64, ":white_check_mark:", 0, "TrilFrame-404"]
    #       ],
    #   )


    writer = ptw.MarkdownTableWriter(
          table_name="Trilinos Status Table",
          headers=["Date", "PR Status", "Number of PRs Merged", "Number of Failed PRs", "Number of PRs Waiting for Build & Test", "Total Numbr of Open PRs", "MM Status", "Number of Successful Master Merges","Jira Ticket #"],
          value_matrix=[
              ["08 Sep 2022",   ":white_check_mark:",      "[1](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-09-07T12%3A00%3A00-07%3A00..2022-09-08T12%3A00%3A00-07%3A00+base%3Adevelop+)", "[6](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-09-07T12%3A00%3A00-07%3A00..2022-09-08T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)",   "[7](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-09-07T12%3A00%3A00-07%3A00..2022-09-08T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 70, ":white_check_mark:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)","[TrilFrame-435](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"],
              ["07 Sep 2022",   ":white_check_mark:",      "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-09-06T12%3A00%3A00-07%3A00..2022-09-07T12%3A00%3A00-07%3A00+base%3Adevelop+)", "[8](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-09-06T12%3A00%3A00-07%3A00..2022-09-07T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)",   "[9](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-09-06T12%3A00%3A00-07%3A00..2022-09-07T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 71, ":white_check_mark:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)","[TrilFrame-435](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"],
              ["06 Sep 2022",   ":warning:",      "[1](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-09-05T12%3A00%3A00-07%3A00..2022-09-06T12%3A00%3A00-07%3A00+base%3Adevelop+)", "[6](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-09-05T12%3A00%3A00-07%3A00..2022-09-06T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)",   "[7](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-09-05T12%3A00%3A00-07%3A00..2022-09-06T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 69, ":warning:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)","[TrilFrame-435](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"],
              ["02 Sep 2022",   ":warning:",      "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-09-01T12%3A00%3A00-07%3A00..2022-09-02T12%3A00%3A00-07%3A00+base%3Adevelop+)", "[1](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-09-01T12%3A00%3A00-07%3A00..2022-09-02T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)",   "[1](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-09-01T12%3A00%3A00-07%3A00..2022-09-02T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 69, ":warning:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)","[TrilFrame-435](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"],
              ["01 Sep 2022",   ":warning:","[2](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-31T12%3A00%3A00-07%3A00..2022-09-01T12%3A00%3A00-07%3A00+base%3Adevelop+)", "[5](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-08-31T12%3A00%3A00-07%3A00..2022-09-01T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-08-31T12%3A00%3A00-07%3A00..2022-08-31T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 69, ":warning:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)", "[TrilFrame-435](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-435)"],
              ["31 Aug 2022",   ":white_check_mark:", "[3](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-30T12%3A00%3A00-07%3A00..2022-08-31T12%3A00%3A00-07%3A00+base%3Adevelop+)","[3](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-08-30T12%3A00%3A00-07%3A00..2022-08-31T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure+)","[12](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-08-30T12%3A00%3A00-07%3A00..2022-08-31T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 62, ":warning:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)", ["[TRILFRAME-432](https://sems-atlassian-son.sandia.gov/jira/projects/TRILFRAME/issues/TRILFRAME-432?filter=allopenissues)","[TRILFRAME-433](https://sems-atlassian-son.sandia.gov/jira/projects/TRILFRAME/issues/TRILFRAME-433?filter=allissues)"]],
              ["24 Aug 2022",   ":white_check_mark:",      "[4](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-23T12%3A00%3A00-07%3A00..2022-08-24T12%3A00%3A00-07%3A00+base%3Adevelop)", "[3](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-08-23T12%3A00%3A00-07%3A00..2022-08-24T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure)",   "[6](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-08-23T12%3A00%3A00-07%3A00..2022-08-24T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 64, ":white_check_mark:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)", "[]()"],
              ["23 Aug 2022",   ":warning:", "[1](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Adevelop)", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+updated%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Afailure)",   "[1](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+is%3Aopen+updated%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Adevelop+status%3Apending+)", 64, ":white_check_mark:", "[0](https://github.com/trilinos/Trilinos/pulls?q=is%3Apr+merged%3A2022-08-22T12%3A00%3A00-07%3A00..2022-08-23T12%3A00%3A00-07%3A00+base%3Amaster+)", "[TRILFRAME-423](https://sems-atlassian-son.sandia.gov/jira/browse/TRILFRAME-423)"]
          ],
      )



    # writer instance writes a table to stdout by default
    #writer.write_table()
    #writer.write_null_line()

    # change the stream to a string buffer to get the output as a string
    # you can also get tabular text by using dumps method
    writer.stream = io.StringIO()
    writer.write_table()
    print(writer.stream.getvalue())

    # change the output stream to a file
    with open("sample.md", "w") as f:
        writer.stream = f
        writer.write_table()

    # or you can use dump method to file if you just output a table to a file
    # writer.dump("sample.md")


if __name__ == "__main__":
   #status-var
    main()
