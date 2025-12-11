# generate ydata report
from ydata_profiling import ProfileReport
import pandas as pd

def generate_eda_report(data: pd.DataFrame, report_name: str = "EDA_Report") -> None:
    """
    Generates an exploratory data analysis (EDA) report using ydata_profiling.

    Parameters:
    data (pd.DataFrame): The input DataFrame for which the report is to be generated.
    report_name (str): The name of the output HTML report file (without extension).

    Returns:
    None: The function saves the report as an HTML file.
    """
    profile = ProfileReport(data, title="Exploratory Data Analysis Report", explorative=True)
    profile.to_file(f"eda_reports/{report_name}.html")
    print(f"EDA report saved as eda_reports/{report_name}.html")

# Example usage:
if __name__ == "__main__":
    # Load sample data
    files = ["data/sample_submission.csv", "data/test.csv", "data/train.csv"]

    for file in files:
        df = pd.read_csv(file)
        report_file_name = file.split("/")[-1].split(".")[0] + "_EDA_Report"
        generate_eda_report(df, report_file_name)

    