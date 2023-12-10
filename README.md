# 機械学習プロジェクト

## プロジェクトの説明
機械学習プロジェクトのテンプレート

### コミットメッセージ
#### フォーマット
メッセージのフォーマットは以下のようにする。  
```bash
<Type>: <Emoji> #<Issue Number> <Title>
```
- 例: feat: :sparkles: #123 〇〇なため、△△を追加
- TypeとTitleは必須
- Issue Numberは強く推奨
- Emojiは任意
- Description（スリーライン）は任意

#### Type
どんなコミットなのかシュッと分かるようにPrefixとしてコミットの種別を書く。  
Semantic Commit Messageと同様の種別を使う。  
- chore : タスクファイルなどプロダクションに影響のない修正
- docs : ドキュメントの更新
- feat : ユーザー向けの機能の追加や変更
- fix : ユーザー向けの不具合の修正
- refactor : リファクタリングを目的とした修正
- style : フォーマットなどのスタイルに関する修正
- test : テストコードの追加や修正

#### Emoji
[gitmoji](https://gitmoji.dev/)から選ぶのが便利。  

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
    ├── README.md            <- このプロジェクトを使用する開発者向けの説明書.
    │
    ├── data
    │   ├── external         <- サードパーティのソースからのデータ.
    │   ├── interim          <- 変換された中間データ.
    │   ├── processed        <- モデリング用の最終的な正規データセット.
    │   ├── raw              <- 元のオリジナルデータ.
    │   └── results          <- 予測結果, 保持する必要がある出力データ.
    │
    ├── mkdocs               <- markdown形式で記述する静的サイトジェネレータ.
    │
    ├── models               <- 訓練されたモデル, シリアライズされたモデル.
    │
    ├── analysis_projects    <- 各分析プロジェクトを格納.
    │
    ├── references           <- データ辞典, マニュアル, その他の説明資料.
    │
    ├── reports              <- HTML, PDF, LaTeXなどで生成された分析レポート.
    │   └── figures          <- レポートで使用される生成されたグラフィックスや図.
    │
    ├── libs                 <- プロジェクト全体で使用するカスタムライブラリ.
    │   └── __init__.py      <- モジュール化用.
    │
    ├── integrate_reqs.py    <- 複数のrequirements.txtファイルを1つのファイルに統合.
    │
    └── requirements_all.txt <- 全分析プロジェクトの環境を再現するための要件ファイル.
                                `python integrate_reqs.py` で生成.
```

<a id="anchor2"></a>

## 環境構築
環境構築の方法は以下通りである。


<a id="anchor3"></a>

## 実行方法
**venv** or **conda** の仮想環境を利用し、以下の手順で実行する。

