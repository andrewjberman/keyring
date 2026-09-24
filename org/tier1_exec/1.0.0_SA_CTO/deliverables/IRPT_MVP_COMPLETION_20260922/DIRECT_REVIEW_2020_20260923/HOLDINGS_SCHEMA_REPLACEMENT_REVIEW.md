# Holdings schema replacement: exact saved-plan GO

CTO decoded the actual saved Terraform plan using the initialized Holdings module providers. SHA256 30f1d202bf7a50fa063e7d96eee2e6ae5ed7465c23471cf1d670230f780d5f02: zero creates, one update, zero destroys. Only module.irpt_holdings.aws_lambda_function.this changes: s3_object_version and source_code_hash; both are known exact values. IAM, environment, handler, layers and routes unchanged.

Independently downloaded S3 artifact investor-reporting/irpt-holdings.zip from opal-313476888478-lambda-artifacts at VersionId nWRHWWilAp0fu9f7swCfvS1zXHEaTfXC. SHA256 97f190ac5704bd63153f24666401a8a102ed35dc1a1c07be0afcbfdb71540c35; all33members compared against previous deployed artifact. Only snapshot.py and BUILD_MANIFEST.json differ. snapshot.py equals reviewed M3e913e9ce9. Actual final archive mounted at /var/task with actual common5 at /opt/python in pinned Lambda Python3.12 image, network none/read-only: entry import and packaged schema load PASS.

Under Andrew's existing Proceed/build authority and CTO worker-fork adjudication, P may apply ONLY that saved plan via canonical apply, then independently read code/version/config back and close exact-function ledger. Drift invalidates this GO. This is not a new vendor authorization, coverage publication permission, or authenticated E2E PASS. M coverage plan is separately reviewed.
