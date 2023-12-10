# 分析用プロジェクト

## プロジェクトの説明
分析用プロジェクトのテンプレート

## 目次
<!-- 目次部分(リンクになるところ) -->
1. [プロジェクト構成](#anchor1)
2. [環境構築](#anchor2)
3. [実行方法](#anchor3)

<a id="anchor1"></a>

## プロジェクトの構成図
このプロジェクトは以下のようなフォルダで構成されている。  

```bash
THE_PROJECT
    ├── LICENSE
    │
    ├── README.md          <- このプロジェクトを使用する開発者向けの説明書.
    │
    ├── data
    │   ├── external       <- サードパーティのソースからのデータ.
    │   ├── interim        <- 変換された中間データ.
    │   ├── processed      <- モデリング用の最終的な正規データセット.
    │   ├── raw            <- 元のオリジナルデータ.
    │   └── results        <- 予測結果, 保持する必要がある出力データ.
    │
    ├── mkdocs             <- markdown形式で記述する静的サイトジェネレータ.
    │
    ├── models             <- 訓練されたモデル, シリアライズされたモデル.
    │
    ├── notebooks          <- Jupyter notebooks. 命名規則は, 番号 (順序付け用), 作成者のイニシャル, および`-`で区切られた短い説明.
    │                        `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- データ辞典, マニュアル, その他の説明資料.
    │
    ├── reports            <- HTML, PDF, LaTeXなどで生成された分析レポート.
    │   └── figures        <- レポートで使用される生成されたグラフィックスや図.
    │
    ├── src                <- プロジェクトで使用するソースコード.
    │   ├── __init__.py    <- モジュール化用.
    │   │
    │   ├── utils          <- プロジェクトで使用されるユーティリティ スクリプト.
    │   │
    │   ├── data           <- データをダウンロードまたは生成するためのスクリプト.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- 生データからモデリング用の特徴量に変換するスクリプト.
    │   │   └── build_features.py
    │   │
    │   ├── models         <- モデルの学習と予想のスクリプト.
    │   │   │ 
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- EDAと予測結果の可視化スクリプト.
    │       └── visualize.py
    │
    └── requirements.txt   <- 分析プロジェクトの環境を再現するための要件ファイル.
                              `pip freeze > requirements.txt` で生成
```

<a id="anchor2"></a>

## 環境構築
環境構築の方法は以下通りである。


<a id="anchor3"></a>

## 実行方法
**venv** or **conda** の仮想環境を利用し、以下の手順で実行する。

