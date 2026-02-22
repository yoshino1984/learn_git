# Project: 股票量化估值判断决策系统

## 项目简介
基于 Python 的股票量化分析系统，用于估值判断和投资决策支持。

## 技术栈
- 语言: Python 3.x
- 数据处理: pandas, numpy
- 数据获取: yfinance, akshare, tushare
- 数据库: SQLite / PostgreSQL
- 可视化: matplotlib, plotly
- 机器学习: scikit-learn (可选)

## 代码风格
- 遵循 PEP 8 规范
- 使用类型注解 (Type Hints)
- 优先使用 async/await 进行异步操作
- 函数使用 docstring 进行文档说明
- Maximum line length: 100 characters

## 重要规则
- NEVER commit to main directly - 使用 feature 分支开发
- Always run tests before pushing - 推送前必须运行测试
- 数据敏感信息（API key 等）使用环境变量存储
- 定期备份数据和配置文件

## 代码组织
- 数据获取模块: `data_fetcher.py`
- 数据分析模块: `analysis.py`
- 估值模型模块: `valuation.py`
- 决策支持模块: `decision.py`
- 配置文件: `config.py`
- 工具函数: `utils.py`
