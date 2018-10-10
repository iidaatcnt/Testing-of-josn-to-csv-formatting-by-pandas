# 対応状況

## 1. 010の作成

### `.py`を作成

### pep8とpylintの構文チェック

### noseテスト

## 2. 020の作成

### `.py`を作成

### pep8とpylintの構文チェック

### noseテスト

## 3. 030の作成

### `.py`を作成

### pep8とpylintの構文チェック

### noseテスト

## 4. 030を左結合した中間DFを介して処理をし高速にできる版の作成

### `.py`を作成

### pep8とpylintの構文チェック

### noseテスト

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

`def is_not_nan(x):`

`def set_new_price(tbl_merged, x_price):`

【補足】

欠損値処理を行う際、price列はint型であると仮定して最後にint型に変換している

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

### `.py`を作成
マージ後、（ tbl_merged.priceがNone）　and  （lcd がEで始まる）時にtbl_merged.priceにe_priceを代入するコードの作成

### pep8とpylintの構文チェック

### noseテスト

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