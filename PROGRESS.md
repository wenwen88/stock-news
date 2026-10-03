# 進度

## 目前狀態
初始化完成（2026-10-02）。git repo 已建於本目錄，藍圖見 `AGENTS.md`。

## 里程碑
- [x] M0 環境初始化（git repo + 藍圖/進度檔 + gh CLI）
- [ ] M1 資料來源接入（選定 API、接金鑰、第一批數據落地）
- [x] M2 產出第一份日報（三面向 HTML，離線 SVG 圖表）→ 10/02 報告已 push；固定化管線/cron 待建

## TODO
- [ ] 確定專案範圍：哪些標的（ETF/個股）、什麼頻率（日報/實時）
- [ ] 選定資料 API（如 Yahoo、Alpha Vantage、Finnhub…）並填入 env
- [ ] 選定技術棧（Python? 版本?）並補 AGENTS.md 指令區

## 最近變更
- 2026-10-03 產出 2026-10-02 美股·台股三面向日報（`stock-report-20261002.html`），純 SVG 離線圖表，已 push。
- 2026-10-02 專案初始化：git init、建立 AGENTS.md / PROGRESS.md、安裝 gh CLI。
