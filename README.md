# aws-boto3-ce

# aws-cost-calculator

Retrieves the cost of the each AWS account.

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Requirment and Major Packages 
```
- Python3 > 3.8.10
- Mysql 
- Boto3
- Docker
```

## Application Deployment 
```
# Mysql server 
$ docker-compose -f docker-compose.yml up -d --build 
$ pip3 install -r requirements.txt
```

## Adding New Project

Create a Policy and attach it to the IAM user from the AWS console. IAM User and IAM Key will be required for later steps. 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ce:DescribeCostCategoryDefinition",
                "ce:GetCostAndUsage",
                "ce:GetRightsizingRecommendation",
                "ce:GetSavingsPlansUtilization",
                "ce:GetAnomalies",
                "ce:GetReservationPurchaseRecommendation",
                "ce:GetCostForecast",
                "ce:GetPreferences",
                "ce:ListTagsForResource",
                "ce:GetReservationUtilization",
                "ce:GetCostCategories",
                "ce:GetSavingsPlansPurchaseRecommendation",
                "ce:GetDimensionValues",
                "ce:GetSavingsPlansUtilizationDetails",
                "ce:GetAnomalySubscriptions",
                "ce:GetCostAndUsageWithResources",
                "ce:DescribeReport",
                "ce:GetReservationCoverage",
                "ce:GetSavingsPlansCoverage",
                "ce:GetAnomalyMonitors",
                "ce:DescribeNotificationSubscription",
                "ce:GetTags",
                "ce:GetUsageForecast"
            ],
            "Resource": "*"
        }
    ]
}

```

Note: For the fresh accounts we will also require to enable AWS Cost Managment from Billing section. 
Run the project-addition.py script using command 

```
python3 project-addition.py
```

Adding the project name in automation.py from gitlab repo. Note that name should match the project name provided in the previous step. 

## Add the automation.sh in crontab. 

Add in the crontab to automate the price retrival on a required basis. 
