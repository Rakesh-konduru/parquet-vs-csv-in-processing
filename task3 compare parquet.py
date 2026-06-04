# Databricks notebook source
df = spark.table("workspace.default.customer_data")

# COMMAND ----------

df.write.mode("overwrite") \
  .option("header", True) \
  .csv("/Volumes/workspace/default/rakesh/customer_csv")

# COMMAND ----------

df_csv = spark.read.option("header", True).option("inferSchema", True) \
    .csv("/Volumes/workspace/default/rakesh/customer_csv")

df_csv.show(5)

# COMMAND ----------

df_csv.write.mode("overwrite").parquet("/Volumes/workspace/default/rakesh/parquet_data")

# COMMAND ----------

df_csv = spark.read.option("header", True).option("inferSchema", True) \
    .csv("/Volumes/workspace/default/rakesh/customer_csv")

df_csv.show(10)

# COMMAND ----------

df_parquet = spark.read.parquet("/Volumes/workspace/default/rakesh/parquet_data")

df_parquet.show(10)

# COMMAND ----------

print("size compared ")


# COMMAND ----------

print("Query performance should be measured for both formats.")

# COMMAND ----------

import time

start = time.time()

df_csv.filter("payment_method = 'Credit Card'") \
      .groupBy("payment_method") \
      .count() \
      .show()

print("CSV Time:", time.time() - start)

# COMMAND ----------

start = time.time()

df_parquet.filter("payment_method = 'Credit Card'") \
          .groupBy("payment_method") \
          .count() \
          .show()

print("Parquet Time:", time.time() - start)

# COMMAND ----------

print("parquet execution time < csv execution  time")

# COMMAND ----------

print("now compare it with partitioned ")

# COMMAND ----------

df.write.mode("overwrite") \
  .partitionBy("payment_method") \
  .option("header", True) \
  .csv("/Volumes/workspace/default/rakesh/partitioned_csv")

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/workspace/default/rakesh/partitioned_csv"))

# COMMAND ----------

df_part_csv = spark.read.option("header", True).option("inferSchema", True) \
    .csv("/Volumes/workspace/default/rakesh/partitioned_csv")

df_part_csv.show(5)

# COMMAND ----------

import time

start = time.time()

df_part_csv.filter("payment_method = 'Credit Card'") \
           .count()

print("Partitioned CSV Time:", time.time() - start)

# COMMAND ----------

df.write.mode("overwrite") \
  .partitionBy("payment_method") \
  .parquet("/Volumes/workspace/default/rakesh/partitioned_parquet")

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/workspace/default/rakesh/partitioned_parquet"))

# COMMAND ----------

df_part_parquet = spark.read.parquet("/Volumes/workspace/default/rakesh/partitioned_parquet")

df_part_parquet.show(5)

# COMMAND ----------

import time

start = time.time()

df_part_parquet.filter("payment_method = 'Credit Card'") \
               .count()

print("Partitioned Parquet Time:", time.time() - start)