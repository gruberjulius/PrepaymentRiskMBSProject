# Prepayment Risk in Mortgage-Backed Securities

This project investigates  **prepayment risk in MBS (Mortgage-Backed Securities)** , with a focus on modeling borrower behavior under varying economic and loan-level conditions. The work was conducted as part of the Baruch MFE program.

## 📊 Overview

Mortgage prepayments are critical for understanding the risk and pricing of mortgage-backed securities. Our project explores two related prediction tasks:

1. **Task 1 – Static prediction (4-year horizon)**

   *Will a loan prepay within four years of origination?*
2. **Task 2 – Dynamic prediction (month-to-month)**

   *Given a loan at time tt**t**, what is the probability it prepays at t+1t+1**t**+**1**?*

We combine **loan-level features** with **macro and regional variables** (interest rates, unemployment, HPI) and benchmark machine learning approaches.

## 🔍 Data

* **Loan classification** : Standard (CRT-eligible) vs Non-Standard loans
* **Origination features** : LTV, CLTV, DTI, FICO, property type, insurance, geography
* **Performance data** : Monthly loan balance, delinquency, termination events (prepayment, foreclosure, REO)
* **Macro/regional data** : Mortgage rates, unemployment, HPI at zip and state level

## ⚙️ Methodology

* **EDA** : Prepayment timing analysis (most occur ~7 years after origination). Cutoff used for modeling train/test splits.
* **Modeling approaches** :
* **LightGBM** for tabular learning with categorical variables & missing data
* **Neural Networks** (deep architecture inspired by  *Deep Learning for Mortgage Risk* )
* **Evaluation metrics** : Accuracy, ROC, Precision-Recall, Feature importance, Training dynamics

## 📈 Results

* Both LightGBM and Neural Networks achieve  **strong predictive performance** , though some overfitting is visible.
* Feature importance highlights borrower characteristics (FICO, LTV/CLTV) and macro drivers (interest rates, HPI).
* Task 2 faced computational bottlenecks — future improvements could leverage **cloud compute** or a  **database backend** .

## 🖼️ Key Figures

You can find the main visuals in the [`figures/`]() folder. Recommended plots for the README:

* [Prepayment timing distribution]() (Slide 4)
* [Prepayment vs interest rates]() (Slide 6)
* [Flow chart of methodology]() (Slide 15)
* [LightGBM &amp; NN accuracy]() (Slide 17)
* [ROC curves]() (Slide 18)
* [Precision-Recall]() (Slide 19)
* [Feature importance &amp; NN loss]() (Slide 20)

*(Export these directly from the slides: [presentation PDF]())*

## 🛠️ Technical Notes

* **Polars vs Pandas** : Polars shows significant speedups for large MBS datasets.
* **Data storage** : Parquet format outperforms CSV/TXT in speed and compression.
* **Scalability challenges** : Memory issues prevented full Task 2 implementation — future work includes migrating to cloud-based or database-backed pipelines.

## 🚀 Next Steps

* Optimize dynamic prepayment modeling (Task 2) using distributed compute
* Explore **survival analysis with exogenous covariates**
* Implement **production-ready pipelines** for prepayment risk modeling
