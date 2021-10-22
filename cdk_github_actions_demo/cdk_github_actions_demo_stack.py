from aws_cdk import (
    core as cdk,
    aws_iam as iam,
    aws_s3 as s3
)


class CdkGithubActionsDemoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        github_oidc_provider = iam.OpenIdConnectProvider(
            self,
            "GithubOIDC",
            url="https://token.actions.githubusercontent.com",  # https://github.com/aws-actions/configure-aws-credentials/issues/271#issuecomment-941870100
            thumbprints=["a031c46782e6e6c662c2c87c76da9aa62ccabd8e"],
            client_ids=[
                "sts.amazonaws.com"  # https://github.com/aws-actions/configure-aws-credentials/commit/036a4a1ddf2c0e7a782dca6e083c6c53e5d90321
            ]
        )

        github_actions_role = iam.Role(
            self,
            "DeployToBucketRole",
            max_session_duration=cdk.Duration.seconds(3600),
            role_name="github-actions-role",
            description="Github actions deployment role to S3",
            assumed_by=iam.FederatedPrincipal(
                federated=github_oidc_provider.open_id_connect_provider_arn,
                conditions={
                    "StringLike": {
                        "token.actions.githubusercontent.com:sub": 'repo:arbitraryrw/cdk-github-actions-demo:*'  # https://github.com/aws-actions/configure-aws-credentials/issues/271#issuecomment-941870100
                    }
                },
                assume_role_action="sts:AssumeRoleWithWebIdentity"
            )
        )

        bucket = s3.Bucket(
            self,
            f"example_bucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        bucket.grant_read_write(github_actions_role)
