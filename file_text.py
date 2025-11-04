def remove_even_lines(in_filename: str, out_filename: str) -> None:
    with open(in_filename, "r", encoding="utf-8") as infile, \
         open(out_filename, "w", encoding="utf-8") as outfile:

        for index, line in enumerate(infile, start=1):
            if index % 2 == 1:
                outfile.write(line)


if __name__ == "__main__":
    in_file = "input.txt"
    out_file = "output.txt"
    remove_even_lines(in_file, out_file)
    print(f"Готово — файлът без четни редове е записан в '{out_file}'.")
