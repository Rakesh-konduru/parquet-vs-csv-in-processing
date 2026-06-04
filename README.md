# Parquet vs CSV in Data Processing

## Overview

This project demonstrates the difference between processing data in CSV format and Parquet format. The goal is to understand how data storage format impacts performance, storage efficiency, and query execution.

## Introduction

CSV is a row-based storage format where data is processed row by row. In contrast, Parquet is a columnar storage format where data is processed column by column. This difference makes Parquet more efficient for analytical workloads.

## Key Concept

CSV processes data row-wise, which means the entire row must be read even if only a few columns are needed.
Parquet processes data column-wise, allowing only required columns to be read, which improves performance.

## Data Conversion

When CSV data is converted into Parquet format, the data is stored in a compressed and optimized binary format. This format is not human-readable but is highly efficient for processing.

## Advantages of Parquet

Faster data processing
Efficient storage with reduced file size
Column-wise data access
Improved query performance
Better support for analytical operations such as max, min, average, and aggregations

## Observations

The file size reduces after converting CSV data to Parquet format
Query execution time is lower when compared to CSV
Data processing becomes faster due to columnar storage

## Conclusion

Parquet is more suitable than CSV for large-scale data processing and analytics due to its columnar storage, compression, and performance benefits. This makes it widely used in modern data engineering pipelines.
