# CDK Github Actions Demo
## Description
This repository contains a simple example Github Action pipeline that uploads a text file to S3 whenever a contributor pushes to the `main` branch. The pipeline is configured to use ephemeral AWS credentials through OpenID Connect (OIDC), this is done using [aws-actions/configure-aws-credential](https://github.com/aws-actions/configure-aws-credentials). In addition, the source contains an AWS Cloud Development Kit (CDK) application that defines all of the required, including the OIDC provider.

## Background
[Github](https://github.com/) provides a built-in mechanism to automate development workflows through [Github actions](https://github.com/features/actions). Workflows can include anything from building a package, to deploying code to infrastructure. Integrating workflows with AWS services is a common use case, however, many tutorials suggest the path of least resistance - introducing sharp edges. Sharp edges in this context includes the use of:

1. Long lasting IAM principals
1. Overly permissive policies
1. Accidentally exposing sensitive data
1. Not leveraging [github repository secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
1. Sharing AWS credentials with untrusted open source github actions

This repository demonstrates a modern CDK example that avoids these sharp edges.