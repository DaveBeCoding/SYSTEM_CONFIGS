#terminal tool to view markdown -> mdv
from pytablewriter import MarkdownTableWriter
# crate <list> that will contains the markdown string

def main():
    writer = MarkdownTableWriter(
        table_name="example_table",
        headers=["int", "float", "str", "bool", "mix", "time"],
        value_matrix=[
            [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
            [2,   "-2.23",  "foo",  False,  None,   "2017-12-23 45:01:23+0900"],
            [3,   0,        "bar",  "true",  "inf", "2017-03-03 33:44:55+0900"],
            [-10, -9.9,     "",     "FALSE", "nan", "2017-01-01 00:00:00+0900"],
        ],
    )
    return writer.write_table()

def table_container(item):
    status = []
    status.append(item())
    return status 


# use string formatting to insert links
# print("The name's {last_name}, {first_name} {last_name}.".format(first_name="James", last_name="Bond"))



# the links can be scraped or grab from the api (whichever is easiest

# once string has been formatted, append to <list>

# cycle through all index's and append/overwrite to TrilinosStatus.md file

# Display on github/trilinos Wiki

#
#
#

### Trilinos Status Table 


if __name__ == "__main__":
   stat = table_container(main())
   print(stat[0])
   #main()
