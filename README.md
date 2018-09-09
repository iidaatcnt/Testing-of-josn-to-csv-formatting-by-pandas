# Testing-of-josn-to-csv-formatting-by-pandas
Personal tools

```
.
├── README.md
├── formater_001.py
├── input
│   ├── greenbay_players.csv
│   └── greenbay_players.json
├── output
└── tests
    ├── test_basic.py
    └── test_sample.py
```

## Running a single test module:
```
$ cd MyProject
$ python -m unittest tests/test_basic
```

## Running a single test case or test method:
```
$ cd MyProject
$ python -m unittest tests.test_basic.SimplisticTest
```

## Running all tests:
```
$ cd MyProject
$ python -m unittest discover
```
