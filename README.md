# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.
## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.


---
## Project Scoping Paragraph

This project frames a **predictive** modeling task: given recent market information, predict whether an asset’s next-period return will be **up (1)** or **down (0)**. I will train an XGBoost classifier on liquid assets using features constructed from lagged returns, rolling volatility, volume, technical indicators (e.g., moving averages, RSI), and calendar effects. The model will output calibrated probabilities of an up move over a defined horizon (e.g., next day), to be consumed as a trading signal rather than a price forecast.

The **primary stakeholder/end user** is a **quantitative portfolio learner** who needs an **actionable, backtestable signal** to inform entry, sizing, and risk control. A **useful answer** is a repeatable pipeline and model **artifact** that produces daily probabilities with thresholds, plus evaluation on both ML and trading metrics. Success will be measured by out-of-sample **AUC/PR-AUC**, **balanced accuracy/F1** for the positive class, and **strategy diagnostics** (long-short on top/bottom deciles with estimated costs), including **annualized Sharpe** and **drawdown**. Interpretation (feature importance/SHAP) will be included to support stakeholder trust and iteration.

| Element            | What you’ll deliver                                                     |
| ------------------ | ----------------------------------------------------------------------- |
| Problem            | Predict next-period up/down for an asset (binary classification)        |
| Stakeholder / User | Quant PM/trader (end user); you act as quant researcher                 |
| Useful Answer Type | **Predictive**; deliverables = trained XGBoost + reproducible pipeline  |
| Key Metrics        | AUC, PR-AUC, balanced accuracy/F1; portfolio Sharpe, drawdown, turnover |