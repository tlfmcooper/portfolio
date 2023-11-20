# Sample project data
projects = [  # Define projects
    {
        "category": "Data Engineering",
        "title": "Data Pipeline with Apache Airflow",
        "description": "A pipeline to automate data workflows using Apache Airflow.",
        "github": "https://github.com/your_username/data-pipeline",
        "website": "https://your-website.com/data-pipeline",
    },
    # Add two more data engineering projects with similar structure
    {
        "category": "Data Science",
        "title": "Predictive Analytics with Machine Learning",
        "description": "Built a machine learning model for predictive analytics.",
        "github": "https://github.com/your_username/predictive-analytics",
        "website": "https://your-website.com/predictive-analytics",
    },
    # Add two more data science projects with similar structure
    {
        "category": "Quantitative Research",
        "title": "Financial Modeling with Quantitative Methods",
        "description": "Used quantitative techniques to analyze financial data.",
        "github": "https://github.com/your_username/financial-modeling",
        "website": "https://your-website.com/financial-modeling",
    },
    # Add two more quantitative research projects with similar structure
]
# Navigation
# Get unique categories
categories = set([p["category"] for p in projects])

# Tech stack
stack = [
    "Python",
    "R",
    "SQL",
    "Git",
    "Github",
    "Jupyter Notebooks",
    "Machine Learning",
    "MongoDB",
    "Deep Learning",
    "Azure",
    "Databricks",
]
