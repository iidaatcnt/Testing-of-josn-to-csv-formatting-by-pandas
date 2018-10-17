# 対応状況

## 1. 010の作成

### `pattern_list_to_vertical_010.py`を作成

010_指定した列内のリストを展開し、縦持ちの1行1データのデータフレームに変換する

主関数

`def pattern_list_to_vertical(update_dfm, to_vertical_column):`

必要な入力データ

- 対象列名

`to_vertical_column = str`

- 更新tbl

`update_dfm = pd.DataFrame(..)`

必要な内部関数

- 無し

【補足】

(2018-10-10 追加): 縦持ちに変換後、各列のデータ型をインプットdfmに合わせるコードを追加

### pep8とpylintの構文チェック

pep8: 問題なし

pylint: W0611 「numpyが読み込めない」という注意が出ている

-> 実行できているので、無視（使用している仮想環境の影響？）

### noseテスト

testsディレクトリで`nosetests test_pattern_list_to_vertical_010.py`を実行

- `test_pattern_list_to_vertical()`: 最初に与えられた例でpattern_list_to_vertical()をテスト
    - 問題なし

## 2. 020の作成

### `pattern_fillna_int_or_float_020.py`を作成

020_以下の条件に沿って、欠損値を穴埋め
- 既定値の値もデータ型もそのまま変えずに穴埋め
- 欠損箇所を埋める既定値は列ごとにある
- データはintとflortの場合がある
- 列内のNoneのところだけに穴埋め処理し、他は影響なし
- 空文字はNone扱い
- 列名ミスなどでNaNとなっている部分は放置
- 穴埋めの既定値は基本的にint型。
- float型で穴埋めしたい列名を引数でリスト形式で指定
    - 未対応
    - （既定値を99.0のようにfloatにすればfloat型で埋まるが、それでは不足か）

主関数

`def pattern_list_to_vertical(update_dfm, to_vertical_column):`

必要な入力データ

- 対象列名と既定値のdict

`default_val_dict = dict`

- 更新tbl

`update_dfm = pd.DataFrame(..)`

必要な内部関数

`def fill_none(dfm, col_name, default_val):`

`def set_default(val):`

`def set_type(dfm, dfm_type, col_name, default_val):`

【補足】

### pep8とpylintの構文チェック

pep8: 問題なし

pylint: R1705 「elseが不要」という注意が出ている

-> 可読性を考慮し、無視

### noseテスト

testsディレクトリで`nosetests test_pattern_fillna_int_or_float_020.py`を実行

- `test_pattern_fillna_int_or_float()`: 最初に与えられた例でpattern_fillna_int_or_float()をテスト
    - 問題なし

## 3. 030の作成

### `fillnan_mst_030_1.py`を作成

030_1 以下の条件に沿って、参照dfmを元に欠損値を埋める
- tblのvalの欠損値の時に穴埋め処理をする。
  具体的なルールは以下の３つ（ルール２からルール４）。
- tblのcdの値がFで始まる文字列の場合（例：F001）の場合は、
  fmstのval値で（例：F001なので1）欠損値の穴埋めをする
- tblのcdの値がEで始まる文字列の場合（例：E001）の場合は、
  emstのval値で（例：E001なので4）欠損値の穴埋めをする
- tblのcdの値の始まりがFでもEでもない場合（例：X001）は欠損値のままにしておく。

for文による処理版
行方向への繰り返し処理のため、処理が遅くなりがち
マージ（結合）による処理ができたのでfor文による処理は不要
コードは短く、理解しやすい
参考程度

主関数

`def fillnan_mst_for(tbl, fmst, emst):`

必要な入力データ

- 参照df その１

`fmst = pd.DataFrame(..)`

- 参照df その２

`emst = pd.DataFrame(..)`

- 更新tbl

`tbl = pd.DataFrame(..)`

必要な内部関数

`def is_not_nan(val):`

`def set_new_val(tbl_merged, x_val):`

【補足】

### pep8とpylintの構文チェック

pep8: 問題なし

pylint: 問題なし

### noseテスト

testsディレクトリで`nosetests test_fillnan_mst_030_1.py`を実行

- `test_fillnan_mst_for_small()`: 最初に与えられた例でfillnan_mst_for()をテスト
    - 問題なし

- `test_fillnan_mst_for_large()`: cdにバリエーションのある例でfillnan_mst_for()をテスト
    - 問題なし


## 4. 030を左結合した中間DFを介して処理をし高速にできる版の作成

### `fillnan_mst_030_2.py`を作成

030_2 以下の条件に沿って、参照dfmを元に欠損値を埋める
- tblのvalの欠損値の時に穴埋め処理をする。
  具体的なルールは以下の３つ（ルール２からルール４）。
- tblのcdの値がFで始まる文字列の場合（例：F001）の場合は、
  fmstのval値で（例：F001なので1）欠損値の穴埋めをする
- tblのcdの値がEで始まる文字列の場合（例：E001）の場合は、
  emstのval値で（例：E001なので4）欠損値の穴埋めをする
- tblのcdの値の始まりがFでもEでもない場合（例：X001）は欠損値のままにしておく。

主関数

`def fillnan_mst(tbl, fmst, emst):`

必要な入力データ

- 参照df その１

`fmst = pd.DataFrame(..)`

- 参照df その２

`emst = pd.DataFrame(..)`

- 更新tbl

`tbl = pd.DataFrame(..)`

必要な内部関数

`def is_not_nan(val):`

`def set_new_val(tbl_merged, x_val):`

【補足】

### pep8とpylintの構文チェック

pep8: 問題なし

pylint: 問題なし

### noseテスト

testsディレクトリで`nosetests test_fillnan_mst_030_2.py`を実行

- `test_fillnan_mst_small()`: 最初に与えられた例でfillnan_mst()をテスト
    - 問題なし

- `test_fillnan_mst_large()`: cdにバリエーションのある例でfillnan_mst()をテスト
    - 問題なし

## 5. 032の作成

### `fillnan_mst_032.py`を作成

032_欠損値を複数の参照dfを参照して穴埋めする関数を作成(その２)

主関数

`def fillnan_mst(update_tbl, emst, fmst, mst_init):`

必要な入力データ

- init

`mst_init = 99`

- 参照df その１

`emst = pd.DataFrame(..)`

- 参照df その２

`fmst = pd.DataFrame(..)`

- 更新tbl

`update_tbl = pd.DataFrame(..)`

必要な内部関数

`def is_e_start(lcd):`

`def is_not_nan(val):`

`def set_new_price(tbl_merged, x_price):`

【補足】

(2018-10-10 追加): 欠損値処理を行う際、price列はint型であると仮定して最後にint型に変換するコードを追加

### pep8とpylintの構文チェック

pep8: E128, E502 の注意が出ている

-> 「一行80文字」というコーディングルールに合わせるため、無視

pylint: R1705 「elseが不要」という注意が出ている

-> 可読性を考慮し、無視

### noseテスト

testsディレクトリで`nosetests test_fillnan_mst_032.py`を実行

- `test_fillnan_mst_small()`: 最初に与えられた例でfillnan_mstをテスト
    - 問題なし
- `test_fillnan_mst_large()`: lcdにバリエーションのある例でfillnan_mstをテスト
    - 問題なし

## 6. 032の一部を変更した部品作成

### `fillnan_mst_032_part.py`を作成

032_part マージ後、（ tbl_merged.priceがNone）　and  （lcd がEで始まる）時にtbl_merged.priceにe_priceを代入するコード

主関数

`def fillnan_e_price(tbl_merged, cols):`

必要な入力データ

- 使用する列の指定

`cols = {"lcd": "...", "price": "...", "e_price": "..."}`

- 更新tbl

`tbl_merged = pd.DataFrame(..)`

必要な内部関数

`def is_not_nan(val):`

【補足】

(2018-10-10 追加): dfm.priceの""をNaNで埋めるコードを追加

### pep8とpylintの構文チェック

pep8: E127, E128, E502 の注意が出ている

-> 「一行80文字」というコーディングルールに合わせるため、無視

pylint: 問題なし

### noseテスト

testsディレクトリで`nosetests test_fillnan_mst_032_part.py`を実行

- `test_fillnan_e_price_small()`: 最初に与えられた例でfillnan_e_price()をテスト
    - 問題なし

## 7. 032のテストコードを作成

### `test_fillnan_mst_032.py`を作成

032のfillnan_mst()関数をテスト

expected_tableのprice列のデータ型をint型に変換してテストに使用している

`test_fillnan_mst_small()`: 最初に与えられた例でfillnan_mstをテスト

`test_fillnan_mst_large()`: lcdにバリエーションのある例でfillnan_mstをテスト

### pep8とpylintの構文チェック

pep8: E402 「モジュールが一番上に来てない」という注意が出ている

-> functiosディレクトリにあるpyファイルをテストするためにパスを設定しているのが原因。無視

pylint: E0401, C0413, R0201, W0611といった注意が出ている

-> functiosディレクトリにあるpyファイルをテストするためにパスを設定しているのが原因だったり、テストコードであることが原因だったりするようなので、無視




## 8. 040の作成

### `dfm_to_records_040.py`を作成

040_dfmをrecordsに変換する関数を作成

主関数

`def dfm_to_records(dfm):`

必要な入力データ

- recordsに変換するdfm

`dfm = pd.DataFrame(..)`

必要な内部関数

- 無し

### pep8とpylintの構文チェック

pep8: 問題なし

pylint: 問題なし

### noseテスト

testsディレクトリで`nosetests dfm_to_records_040.py`を実行

- `test_dfm_to_records()`: 14行3列のdfmでdfm_to_records()をテスト
    - 問題なし
