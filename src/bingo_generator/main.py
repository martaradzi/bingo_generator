from pathlib import Path

import click
import pandas as pd
from tqdm import tqdm

from bingo_generator.generator import generate_boards
from bingo_generator.input import read_file


@click.command(name="main")
@click.option(
    "--input_path",
    type=click.Path(
        exists=True,
        readable=True,
        file_okay=True,
        path_type=Path,
    ),
    default=Path.cwd() / "input.txt",
    show_default=True,
)
@click.option(
    "--board_count",
    help="How many sheets to print",
    default=5,
)
def main(input_path: Path, board_count: int) -> None:

    input_data = read_file(input_path)

    with pd.ExcelWriter("bingo_board.xlsx") as writer:

        for i in tqdm(range(board_count), desc="Generating sheets"):
            sheet_name = f"board_{i}"
            df = generate_boards(input_data)

            df.to_excel(writer, sheet_name=sheet_name)


if __name__ == "__main__":
    main()
