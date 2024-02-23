import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import when, col
from awsglue.dynamicframe import DynamicFrame 

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Relational DB
RelationalDB_node1707473645992 = glueContext.create_dynamic_frame.from_options(
    connection_type="mysql",
    connection_options={
        "useConnectionProperties": "true",
        "dbtable": "product",
        "connectionName": "Mysql connection",
    },
    transformation_ctx="RelationalDB_node1707473645992",
    additional_options={"jobBookmarkKeys": ["indexing"], "jobBookmarkKeysSortOrder": "asc"}
)

# Convert dynamic frame to DataFrame
df = RelationalDB_node1707473645992.toDF()

# Fill missing values in DataFrame
df = df.withColumn("brand_name", when(col("brand_name") == "", "UN-KNOWN").otherwise(col("brand_name")))
df = df.withColumn("manufacturer_name", when(col("manufacturer_name") == "", "LOCAL").otherwise(col("manufacturer_name")))

# Convert DataFrame back to dynamic frame
dynamic_frame_filled = DynamicFrame.fromDF(df, glueContext, "dynamic_frame_filled")


# Script generated for node Change Schema
ChangeSchema_node1707477382758 = ApplyMapping.apply(
    frame=dynamic_frame_filled,
    mappings=[
        ("product_id", "int", "product_id", "int"),
        ("product_name", "string", "product_name", "string"),
        ("unit", "string", "unit", "string"),
        ("product_type", "string", "product_type", "string"),
        ("brand_name", "string", "brand_name", "string"),
        ("manufacturer_name", "string", "manufacturer_name", "string"),
        ("l0_category", "string", "l0_category", "string"),
        ("l1_category", "string", "l1_category", "string"),
        ("l2_category", "string", "l2_category", "string"),
        ("l0_category_id", "int", "l0_category_id", "int"),
        ("l1_category_id", "int", "l1_category_id", "int"),
        ("l2_category_id", "int", "l2_category_id", "int"),
    ],
    transformation_ctx="ChangeSchema_node1707477382758",
)

# Script generated for node Amazon S3
AmazonS3_node1708110424343 = glueContext.getSink(
    path="s3://flipkart-dataset/product_output/",
    connection_type="s3",
    updateBehavior="LOG",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1708110424343",
)
AmazonS3_node1708110424343.setCatalogInfo(
    catalogDatabase="flipkart-data", catalogTableName="Product_via_CFT"
)
AmazonS3_node1708110424343.setFormat("glueparquet", compression="uncompressed")
AmazonS3_node1708110424343.writeFrame(ChangeSchema_node1707477382758)
job.commit()
