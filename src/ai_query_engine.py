import pandas as pd


def analyze_question(df, question):

    question = question.lower()

    if "highest revenue region" in question or "highest revenue" in question:

        region = df.groupby("Region")["Revenue"].sum().idxmax()

        return f"The region with the highest revenue is {region}"


    elif "top product" in question or "most sold product" in question:

        product = df.groupby("Product")["Units"].sum().idxmax()

        return f"The most sold product is {product}"


    elif "total revenue" in question:

        revenue = df["Revenue"].sum()

        return f"Total revenue is {revenue}"


    elif "average revenue" in question:

        avg = df["Revenue"].mean()

        return f"Average revenue per transaction is {avg:.2f}"


    elif "best category" in question:

        category = df.groupby("Category")["Revenue"].sum().idxmax()

        return f"The best performing category is {category}"


    else:

        return "I could not understand the question. Try asking about revenue, product, or region."