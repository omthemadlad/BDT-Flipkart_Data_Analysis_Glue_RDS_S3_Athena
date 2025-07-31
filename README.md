# 🛒 Flipkart Grocery Sales Analysis 📊

## Overview
In this comprehensive Big Data project, we delve into the Flipkart Grocery transaction data, extracting valuable insights into sales patterns, discount effects, and brand performance. Our tech stack, including AWS Glue, AWS Crawler, AWS S3, AWS RDS, AWS Athena, Kafka, GitHub Actions, and Tableau, powers a data pipeline for both batch and real-time data.

## Technologies Used
- **AWS Glue:** Applied for ETL operations, enabling seamless data integration and transformation.
- **AWS S3:** Scalable and durable storage for raw and processed data.
- **AWS RDS:** Hosted a relational database for structured data, forming a robust foundation for analysis.
- **AWS Athena:** Used for querying data directly in S3 using SQL, enabling quick and efficient analytics.
- **GitHub Actions:** Automated the data pipeline process, ensuring a streamlined workflow with each repository update.
- **AWS SNS:** Implemented fot notification of Glue Job runs.
- **Tableau:** Visualized insights through an interactive dashboard, providing a user-friendly interface.

## Data Pipeline Workflow

![FinalArchitecture-ezgif com-video-to-gif-converter](https://github.com/omthemadlad/BDT-Flipkart_Data_Analysis_Glue_RDS_S3_Athena/assets/66026855/ac355103-a9e2-4157-9cb9-20d9fc16ebf3)

## Insights and Achievements
- 🚀 **Best-Selling Items:** Identified top-performing products for strategic decision-making.
- 💸 **Sales Patterns and Discount Effects:** Unveiled and measured the impact of discounts on sales, guiding pricing strategies.
- 🏆 **Brand Performance Evaluation:** Evaluated brand performance to inform partnerships, marketing strategies, and inventory management.

## How to Use
- **Clone Repository:**
  
gh repo clone omthemadlad/BDT-Flipkart_Data_Analysis_Glue_RDS_S3_Athena

## Deployment Steps
Prerequisites:

An AWS account with necessary permissions.
AWS CLI configured and credentials set.

1. Create an S3 Bucket:
Purpose: Store incoming sales data.
Instructions: Use the AWS CLI or console to create a bucket.

2. Set up an RDS:
Purpose: Store products data.
Instructions: Use the AWS console or CloudFormation to create an RDS instance.

3. Use SAM to Create Glue Jobs and Lambda Function:
Jobs: Sales_Glue_Job and Products_Glue_Job.
Function: Sales_Trigger.
Instructions:
Use the provided .py scripts for Glue Jobs and Lambda Function.
Define a SAM template.yaml file configuring these resources.
Use deploy to deploy the CloudFormation stack.

4. Add S3 Trigger:
Add an S3 Trigger to the Lambda Function.
Instructions: Use the AWS console or CloudFormation to configure an S3 trigger on the bucket pointing to the Sales_Trigger Lambda function.

5. Create SNS Topic:
Create an SNS Topic for communication.
Instructions: Use the AWS console or CloudFormation to create an SNS topic.

6. Add Email Subscribers:
Add desired email subscribers to the SNS Topic.
Instructions: Use the AWS console to subscribe desired email addresses to the topic.
