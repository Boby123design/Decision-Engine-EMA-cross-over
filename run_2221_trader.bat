@echo off
cd /d %~dp0
python -m streamlit run live_trader_2221.py --server.port 8505
pause