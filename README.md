Для запуска скрипта в командной строке нужно указать:
>python {путь до файла/имя файла(если он в той же директроии что и код)} --where "price{<,>,=}value" --aggregate "price={min,max,avg}"

для where используется только знаки >, <, =

для aggregate команды min, max, avg

where и agregate выполняется по колонке price

примеры запуска скрипта:
> 1. python products.csv --where "price<1000" --aggregate "price=avg"
> 2. python python main.py --files пусть до файла --where "price>1000" --aggregate "price=min"

В коде используются классы:
1. Writer для печати таблица
2. Reader для чтения информации из файла и формирования из этой информации словаря
3. Data для использования филтров и аггрегации на данные
4. Filter для филтрации данных
5. Aggregate для агрегации данных