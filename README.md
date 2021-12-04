# CDK Github Actions Demo
## Description
This repository contains a simple example Github Action pipeline that uploads a text file to S3 whenever a contributor pushes to the `main` branch. The pipeline is configured to use ephemeral AWS credentials through OpenID Connect (OIDC), this is done using [aws-actions/configure-aws-credential](https://github.com/aws-actions/configure-aws-credentials). In addition, the source contains an AWS Cloud Development Kit (CDK) application that defines all of the required, including the OIDC provider.

