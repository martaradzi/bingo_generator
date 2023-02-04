# Bingo Board Generator

This project generates a bingo board from a user provided input. The boards are generated in an excel format, each board being one sheet. 

NOTE:
This project uses [poetry](https://python-poetry.org/) to manage library dependencies.
Install dependencies using:
```bash
poetry shell
poetry install
```

Assuming you added your input to the `input.txt` file, to run the board generator run:
```bash
generate_board --board_count=<NUMBER OF BOARDS YOU WANT TO GENERATE>
```

You can specify a non-default input path using `--input_path` parameter. This needs to be a txt file.

The output excel file will be stored in the current dir in `bingo_board.xlsx` file.
