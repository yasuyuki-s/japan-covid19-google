# GoogleによるCOVID-19感染予測と実報告数の推移
## What's this?
Googleの公開する「COVID-19感染予測(日本版)」による陽性者数の推移を予測基準日毎に実際の報告数と比較したグラフを作図します。
下記の公開URLでは1日3回（09時、22時、24時）データを自動取得し更新しています。
## フォルダ構造
整理中...
## 凡例
- Forecast(MMDD)…Googleによる予測値(予測基準日） ※95%予測区間も併記
- Historic(MMDD)…実報告数（最終更新日）
- Historic(7dSMA)…実報告数（7日移動平均線）
## 実報告数について
○が付いている都道府県は各自治体の公開する最新の陽性報告数のデータを反映しています。(毎日更新)
それ以外の都道府県の陽性報告数は、「NHKまとめ」のデータを利用しています(毎日更新)
## 公開URL
http://covid19graph.japanwest.cloudapp.azure.com/
## 参照データ 
- Google 
https://datastudio.google.com/u/0/reporting/8224d512-a76e-4d38-91c1-935ba119eb8f/page/ncZpB?s=nXbF2P6La2M
- NHK
https://www3.nhk.or.jp/news/special/coronavirus/data/
- 北海道
https://www.harp.lg.jp/opendata/dataset/1369.html
- 東京都
https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068
- 大阪府
https://covid19-osaka.info/
- 広島県
https://www.pref.hiroshima.lg.jp/soshiki/19/opendata-covid19.html
- 愛媛県
https://www.pref.ehime.jp/opendata-catalog/dataset/2174.html
- 福岡県
https://ckan.open-governmentdata.org/dataset/401000_pref_fukuoka_covid19_patients
