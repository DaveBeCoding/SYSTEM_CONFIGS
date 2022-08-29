#/usr/bin/env python3

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import io

import pytablewriter as ptw


def main():
   # writer = ptw.MarkdownTableWriter(
   #     table_name="zone",
   #     headers=["zone_id", "country_code", "zone_name"],
   #     value_matrix=[
   #         ["1", "AD", "Europe/Andorra"],
   #         ["2", "AE", "Asia/Dubai"],
   #         ["3", "AF", "Asia/Kabul"],
   #         ["4", "AG", "America/Antigua"],
   #         ["5", "AI", "America/Anguilla"],
   #     ],
   # )


    writer = ptw.MarkdownTableWriter(
          table_name="Trilinos Status Table",
          headers=["Date", "PR Status", "Number of PRs Merged", "Number of Failed PRs", "Number of PRs Waiting for Build & Test", "Total Numbr of Open PRs", "MM Status", "Number of Successful Master Merges","Jira Ticket #"],
          value_matrix=[
              ["24 Aug 2022",   ":white_check_mark:",      "[4](https://tinyurl.com/2kd9ygc7)", "[3](https://tinyurl.com/2kd9ygc7)",   "[6](https://tinyurl.com/2kd9ygc7)", 64, ":white_check_mark:", "[0](https://tinyurl.com/2kd9ygc7)", "[TrilFrame-423](https://tinyurl.com/2kd9ygc7)"],
              ["23 Aug 2022",   ":warning:",      4, 3,   6, 64, ":white_check_mark:", 0, "TrilFrame-405"],
              ["22 Aug 2022",   ":x:",      4, 3,   6, 64, ":white_check_mark:", 0, "TrilFrame-404"]
          ],
      )


    # writer instance writes a table to stdout by default
    writer.write_table()
    writer.write_null_line()

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
    main()
