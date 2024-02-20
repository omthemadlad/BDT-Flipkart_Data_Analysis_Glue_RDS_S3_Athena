# Flipkart_Data_Analysis_using_RDS_S3_Glue_Athena_Tableau
AWS Project on Big Data -> Flipkart Sales Data Analysis

Steps to implement -
1. Create a S3 bucket to store the incoming Sales data.
2. Create RDS where the Products Data will be stored.
3. Now using SAM, Create two Glue Jobs named Sales_Glue_Job, Products_Glue_Job & one Lambda Function named Sals_Trigger.
4. Use provided .py scripts for the Glue Jobsand Lambda Function.
5. After CloudFormation stack has been successfully deployed add S3 Trigger in your Lambda Function.
6. Create SNS Topic and add desired EMAIL Subscribers to it.
7. Finish !
