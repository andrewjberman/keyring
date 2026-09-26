# Hop-3 full-path IAM simulation -- 2.0.0_SA_COO~P's corroborating run (CTO 101275 / 101309)

Pairs: ~Y's `IRPT_MVP_Y/IAM_PAIRS_GENERATE.json` (25) and `IAM_PAIRS_RESIDENT.json` (40) @2789ac3bbd, from an AST census of
the deployed code. The ONE conditioned pair per list -- `kms:*` on the users-table key 64f25291 -- carries the grant's
context (kms:ViaService dynamodb.us-east-1, EncryptionContext tableName opal-users-v2), as ~Y's tool does. Instrument:
P's own `iam_simulate_pairs.py` (identity plane only; bucket and key policies are separate planes).

## irpt-ycharts-generate-role
```
OK   allowed   s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/original_holdings/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/original_holdings/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/original_holdings/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/request_compositions/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/request_compositions/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/request_compositions/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   dynamodb:GetItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:PutItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:PutItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:UpdateItem      arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:Query           arn:aws:dynamodb:us-east-1:313476888478:table/opal-users-v2/index/email-index (expect allowed)
OK   allowed   dynamodb:GetItem         arn:aws:dynamodb:us-east-1:313476888478:table/opal-users-v2 (expect allowed)
OK   implicitDeny dynamodb:Query           arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect denied)
OK   allowed   sqs:SendMessage          arn:aws:sqs:us-east-1:313476888478:irpt-generation (expect allowed)
OK   allowed   kms:GenerateDataKey      arn:aws:kms:us-east-1:313476888478:key/7f4d3042-10d8-49a7-b55e-3c963cea8111 (expect allowed)
OK   allowed   kms:Decrypt              arn:aws:kms:us-east-1:313476888478:key/7f4d3042-10d8-49a7-b55e-3c963cea8111 (expect allowed)
OK   allowed   kms:Decrypt              arn:aws:kms:us-east-1:313476888478:key/64f25291-4015-42c5-ad41-40e42325deb7 (expect allowed) [context]
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-cot/investor-reporting/directory/directory.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-cot/platinum/cottonwood/ownership_map.json (expect allowed)
OK   allowed   secretsmanager:GetSecretValue arn:aws:secretsmanager:us-east-1:313476888478:secret:ycharts/session/current-AbCdEf (expect allowed)
OK   implicitDeny s3:DeleteObject          arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect denied)
OK   implicitDeny dynamodb:DeleteItem      arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect denied)
OK   implicitDeny s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/platinum/analysis_reports/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect denied)
irpt-ycharts-generate-role: 21 of 25 allowed; 25 of 25 met their expectation
```

## irpt-ycharts-runner-role (the resident)
```
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/original_holdings/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/original_holdings/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/request_compositions/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/request_compositions/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/vendor_documents/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/vendor_documents/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/vendor_documents/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/extraction_evidence/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/extraction_evidence/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/state/extraction_evidence/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:PutObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/platinum/analysis_reports/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObject             arn:aws:s3:::opal-data-irpt/irpt/cottonwood/platinum/analysis_reports/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   s3:GetObjectVersion      arn:aws:s3:::opal-data-irpt/irpt/cottonwood/platinum/analysis_reports/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect allowed)
OK   allowed   dynamodb:GetItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:PutItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:UpdateItem      arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:Query           arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:ConditionCheckItem arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect allowed)
OK   allowed   dynamodb:GetItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:PutItem         arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:UpdateItem      arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:Query           arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:ConditionCheckItem arn:aws:dynamodb:us-east-1:313476888478:table/irpt-requests (expect allowed)
OK   allowed   dynamodb:Query           arn:aws:dynamodb:us-east-1:313476888478:table/opal-users-v2/index/email-index (expect allowed)
OK   allowed   dynamodb:GetItem         arn:aws:dynamodb:us-east-1:313476888478:table/opal-users-v2 (expect allowed)
OK   allowed   sqs:ReceiveMessage       arn:aws:sqs:us-east-1:313476888478:irpt-generation (expect allowed)
OK   allowed   sqs:ChangeMessageVisibility arn:aws:sqs:us-east-1:313476888478:irpt-generation (expect allowed)
OK   allowed   sqs:DeleteMessage        arn:aws:sqs:us-east-1:313476888478:irpt-generation (expect allowed)
OK   allowed   secretsmanager:GetSecretValue arn:aws:secretsmanager:us-east-1:313476888478:secret:ycharts/session/current-AbCdEf (expect allowed)
OK   allowed   secretsmanager:PutSecretValue arn:aws:secretsmanager:us-east-1:313476888478:secret:ycharts/session/current-AbCdEf (expect allowed)
OK   allowed   secretsmanager:GetSecretValue arn:aws:secretsmanager:us-east-1:313476888478:secret:ycharts/login/credentials-AbCdEf (expect allowed)
OK   allowed   kms:GenerateDataKey      arn:aws:kms:us-east-1:313476888478:key/7f4d3042-10d8-49a7-b55e-3c963cea8111 (expect allowed)
OK   allowed   kms:Decrypt              arn:aws:kms:us-east-1:313476888478:key/7f4d3042-10d8-49a7-b55e-3c963cea8111 (expect allowed)
OK   allowed   kms:Decrypt              arn:aws:kms:us-east-1:313476888478:key/64f25291-4015-42c5-ad41-40e42325deb7 (expect allowed) [context]
OK   implicitDeny s3:DeleteObject          arn:aws:s3:::opal-data-irpt/irpt/cottonwood/platinum/analysis_reports/ART-0000000000000000000000000000000000000000000000000000000000000000/x.json (expect denied)
OK   implicitDeny dynamodb:DeleteItem      arn:aws:dynamodb:us-east-1:313476888478:table/irpt-jobs (expect denied)
OK   implicitDeny sqs:SendMessage          arn:aws:sqs:us-east-1:313476888478:irpt-generation (expect denied)
irpt-ycharts-runner-role: 37 of 40 allowed; 40 of 40 met their expectation
```
