from aws_cdk import (
    core as cdk,
    aws_iam as iam,
    aws_s3 as s3
)


class CdkGithubActionsDemoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


