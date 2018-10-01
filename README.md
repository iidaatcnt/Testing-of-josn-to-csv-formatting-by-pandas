# Testing-of-josn-to-csv-formatting-by-pandas
Personal tools

```
.
├── Docs
│   └── coding_policy.md
├── README.md
├── formater_001.py
├── formater_002.py
├── homeworks.ipynb
├── input
│   ├── greenbay_players.csv
│   ├── greenbay_players.json
│   ├── input_data.json
│   ├── sample.csv
│   ├── sample.json
│   ├── sample2.json
│   └── sample3.json
├── jupyter
│   ├── allyouneedis.ipynb
│   ├── formater.ipynb
│   ├── pattern_fillna_int_or_float.ipynb
│   ├── pattern_list_to_vertical.ipynb
│   ├── sample_pandas_normal.csv
│   └── test001.ipynb
├── output
│   └── output.csv
├── test_formater_001.py
├── test_sample.py
└── tests
    ├── __pycache__
    │   ├── test_basic.cpython-36.pyc
    │   └── test_sample.cpython-36.pyc
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
