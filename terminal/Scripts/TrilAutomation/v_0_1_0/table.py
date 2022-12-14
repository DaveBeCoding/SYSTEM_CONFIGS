from pytablewriter import MarkdownTableWriter

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
    writer.write_table()

if __name__ == "__main__":
    main()
