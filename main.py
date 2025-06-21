from argparse import ArgumentParser

from app.writer import Writer


def main() -> None:
    parser = ArgumentParser()

    parser.add_argument("--files", nargs="+", help="Считывание CSV файлов")
    parser.add_argument(
        "--where", default=None, help="Фильтрует по столбцу price(знаки >, <, ="
    )
    parser.add_argument(
        "--aggregate",
        default=None,
        help="Ищет max, min, avg значение по столбцу price(через знак =)",
    )

    args = parser.parse_args()
    writer = Writer(args.files)
    writer.write(args.where, args.aggregate)


if __name__ == "__main__":
    main()
