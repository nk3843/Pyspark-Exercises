# PySpark exercises

Hands-on PySpark practice, from loading a CSV to window functions, cohort analysis, and streaming. Each notebook
starts with the task in comments and solves it with the DataFrame API, using the small CSV/JSON files in this repo.

## Notebooks

| Notebook | Task | Spark features |
|---|---|---|
| [exercise_1](exercise_1.ipynb) | Filter people by age and select columns | `read.csv`, `filter`, `select` |
| [exercise_2](exercise_2.ipynb) | Total sales per category | `groupBy`, `agg`, sorting |
| [exercise_3](exercise_3.ipynb) | Split order timestamps into date and time; filter by date | `to_timestamp`, `to_date`, `date_format` |
| [exercise_4](exercise_4.ipynb) | Clean customer data: drop null rows, or fill missing age with the average and missing city with "unknown" | `dropna`, `na.fill`, `avg` |
| [exercise_5](exercise_5.ipynb) | Per-player game sessions from event gaps | `lag`, `unix_timestamp`, window functions |
| [grades](grades.ipynb) | Rank students within each subject | `Window.partitionBy`, `rank` |
| [file_handling](file_handling.ipynb) | Build a DataFrame from JSON records; write JSON and Parquet | `createDataFrame`, `write.json`, `write.parquet` |
| [full_name](full_name.ipynb) | Initials from full names, with a Python UDF and a vectorized pandas UDF | `udf`, `pandas_udf` |
| [User Engagement Analysis](User%20Engagement%20Analysis%20.ipynb) | Time between events within each user session | window functions over sessions |
| [cohort_analysis](cohort_analysis.ipynb) | Signup-month cohorts: how many users from each cohort buy in each later month | `date_trunc`, `last(..., ignorenulls)` over a window, `countDistinct` |
| [Streaming](Streaming.ipynb) | Word counts over a live socket stream | Spark Streaming (`StreamingContext`) |
| [Synthetic_data_generator](Synthetic_data_generator.ipynb) | Generate the e-commerce events dataset | pandas, NumPy |

Also here:

- `socket_wordcount.py`: the streaming word count as a script.
- `my_pyspark.py`, `test_spark.py`, `test_pyspark.py`: checks that a local Spark session starts.
- `script.py`: an unrelated practice problem (assign requests to the least-loaded server with a heap).

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install pyspark pandas pyarrow jupyter
jupyter notebook
```

PySpark needs Java (11 or 17). For the streaming example, open a text socket first with `nc -lk 9999`, run
`python socket_wordcount.py`, then type lines into the `nc` window.
