import numpy as np
import pandas as pd
class DataExplorer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def shape(self):
        return self.df.shape

    def preview(self, n=5):
        return self.df.head(n)
    

    def disease_rate_by(self,col):
        return self.df.groupby(col)['HeartDisease'].mean()
    
    def cond_prob(self,col,val):
        return self.df.loc[self.df[col]==val, 'HeartDisease'].mean()
    
    def null_report(self):
        """
        Return missing-value count and percentage for each column.
        """
        report = pd.DataFrame({
            "missing_count": self.df.isna().sum(),
            "missing_percent": self.df.isna().mean().mul(100).round(2)
        })

        return report
    
    def zero_report(self, columns=None):
        """
        Checks zero values in selected numeric columns.
        Useful for detecting disguised missing values.
        """
        if columns is None:
            columns = ["Cholesterol", "RestingBP"]

        report = []

        for col in columns:
            zero_count = (self.df[col] == 0).sum()
            zero_percent = (self.df[col] == 0).mean() * 100

            report.append({
                "column": col,
                "zero_count": zero_count,
                "zero_percent": round(zero_percent, 2)
            })

        return pd.DataFrame(report)

    def prior_prob(self):
        """
        Calculates prior probability of heart disease.
        """
        probability = self.df["HeartDisease"].mean()
        return round(probability * 100, 1)

    def bayes_verify(self, column, value):
        """
        Verifies Bayes theorem for:
        P(Disease | column = value)
        """
        event = self.df[column].eq(value)
        disease = self.df["HeartDisease"].eq(1)
        p_event_given_disease = event[disease].mean()
        p_disease = disease.mean()
        p_event = event.mean()
        bayes_result = (p_event_given_disease * p_disease) / p_event
        direct_result = self.df.loc[event, "HeartDisease"].mean()

        return pd.DataFrame({
            "calculation": ["Direct filtering", "Bayes theorem"],
            "probability_percent": [
                round(direct_result * 100, 1),
                round(bayes_result * 100, 1)
            ]
        })

    def add_age_group(self):
        self.df["Age_group"] = pd.cut(
            self.df["Age"],
            bins=[0, 50, 60, np.inf],
            labels=["under 50", "50 - 60", "over 60"],
            right=False
        )

        return self.df[["Age", "Age_group"]].head()

    def rate_by_two_groups(self, group1, group2):
        result = (
            self.df.groupby([group1, group2], observed=True)["HeartDisease"]
            .mean()
            .mul(100)
            .reset_index(name="disease_rate")
            .sort_values("disease_rate", ascending=False)
        )

        result["disease_rate"] = result["disease_rate"].round(1)

        return result
