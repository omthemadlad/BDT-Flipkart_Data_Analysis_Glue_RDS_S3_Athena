Flipkart Grocery Sales Analysis

Overview
In this comprehensive Big Data project, I conducted an in-depth analysis of Flipkart Grocery transaction data to unveil valuable insights into sales patterns, measure discount effects, and evaluate brand performance. Leveraging a robust tech stack including AWS Glue, AWS Crawler, AWS S3, AWS RDS, AWS Athena, Kafka, GitHub Actions, and Tableau, I designed a powerful data pipeline capable of handling both batch and real-time streaming data.

Technologies Used
AWS Glue: 
Applied for Extract, Transform, Load (ETL) operations, enabling seamless data integration and transformation.

AWS S3: 
Leveraged as a scalable and durable storage solution for storing raw and processed data.

AWS RDS: 
Employed for hosting a relational database to store structured data, providing a robust foundation for analysis.

AWS Athena: 
Utilized for querying data directly in S3 using SQL, enabling quick and efficient analytics.

GitHub Actions: 
Automated the data pipeline process, triggering workflows with each update to the repository, ensuring a streamlined and efficient workflow.

Kafka: 
Implemented as a real-time streaming data source, enriching the analysis with up-to-the-minute insights. (Add on)

Tableau: 
Visualized the derived insights through an interactive dashboard, providing users with a user-friendly interface to explore the data dynamically.

AWS SNS: 
Implemented facilitating communication and notification functionalities in real-time.

Data Pipeline Workflow
#Add architecture

Insights and Achievements
Best-Selling Items: Identified the top-performing products through thorough analysis, enabling strategic decision-making.

Sales Patterns and Discount Effects: Unveiled and measured the impact of discounts on sales, providing actionable insights for pricing strategies.

Brand Performance Evaluation: Evaluated brand performance to inform partnerships, marketing strategies, and inventory management.


How to Use
Clone Repository: Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
Setup Environment: Follow the setup instructions in the documentation to configure the project environment.
Steps to implement -
1. Create a S3 bucket to store the incoming Sales data.
2. Create RDS where the Products Data will be stored.
3. Now using SAM, Create two Glue Jobs named Sales_Glue_Job, Products_Glue_Job & one Lambda Function named Sals_Trigger.
4. Use provided .py scripts for the Glue Jobsand Lambda Function.
5. After CloudFormation stack has been successfully deployed add S3 Trigger in your Lambda Function.
6. Create SNS Topic and add desired EMAIL Subscribers to it.
7. Finish !
