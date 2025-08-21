# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
This project aims to build a **predictive model** that forecasts whether an asset’s next-period return will move **up (1)** or **down (0)**. Financial markets are noisy and volatile, and identifying a reliable edge can meaningfully improve risk-adjusted returns. By using **XGBoost**, a gradient boosting algorithm, combined with features such as lagged returns, volatility, trading volume, technical indicators (e.g., moving averages, RSI), and calendar effects, the model provides **probabilities of upward price movement**. These probabilities will be consumed as **trading signals**, not raw price forecasts, supporting disciplined entry and exit decisions.

## Stakeholder & User
The **primary stakeholders** are **quantitative portfolio managers and traders**.  
- Portfolio managers need systematic and repeatable signals for risk management and capital allocation.  
- Traders need **clear, backtestable trading signals** that can be integrated into daily workflows.  

Both groups benefit from an interpretable signal that reduces reliance on intuition and enhances decision-making.

## Useful Answer & Decision
The useful deliverable is a **repeatable prediction pipeline** that outputs daily probabilities of upward movement.  
- **Type of answer:** Predictive  
- **Metric:** Model + artifact (trained XGBoost model with inference script)  
- **Evaluation:** Machine learning metrics (AUC, PR-AUC, F1) + strategy diagnostics (Sharpe ratio, drawdown, turnover)  
- **Decision:** Entry/exit signal for trading strategies  

## Assumptions & Constraints
- Data availability: liquid assets with sufficient historical returns, volume, and technical indicators.  
- Capacity: assumes computational resources for feature engineering and model training.  
- Latency: predictions must run daily (overnight or intraday), not in real-time HFT.  
- Compliance: signals must align with institutional trading and risk management rules.  

## Known Unknowns / Risks
- Uncertainty in model generalization to unseen market regimes.  
- Risk of overfitting to historical data.  
- Feature relevance may drift as market conditions change.  
- Need to monitor performance stability and recalibrate thresholds.  

## Lifecycle Mapping
Goal → Stage → Deliverable  
- **Goal A:** Define and scope predictive task → Problem Framing & Scoping (Stage 01) → Project proposal & stakeholder memo  
- **Goal B:** Build baseline pipeline → Data acquisition & preprocessing (Stages 04–06) → Training-ready dataset  
- **Goal C:** Train & validate model → Modeling stage → XGBoost model + evaluation metrics  
- **Goal D:** Backtest and analyze signal → Outliers/Risk Assumptions (Stage 07) → Trading diagnostics report  

## Repo Plan
- `/data/` → raw and processed datasets  
- `/src/` → feature engineering, modeling scripts  
- `/notebooks/` → exploratory analysis and experiments  
- `/docs/` → stakeholder memo, reports, project documentation  
- Cadence: updated weekly as project progresses  
