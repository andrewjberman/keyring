# Evidence and reproduction

`MEASUREMENTS.json` records fresh observations and explicitly separates peer reports, source inspection and unexercised behavior. `S3_INVENTORY.csv` contains the complete paginated 2,277-object current-key census: keys, byte sizes and modification times, not bodies. `SOURCE_MANIFEST.json` hashes the principal inspected source/contract files. File hashes bind the working-tree reads; a git pin alone would not bind uncommitted changes.

`collect_readonly.py` and `collect_supplement.py` retain the AWS/project instruments. Run from the repository root with the existing boto3/pyarrow environment; they use the caller's already configured AWS identity. They do not request or print credentials. They perform reads and write results only beneath `.runtime/cro-z-amgt-research-20260923/`. They do not invoke Lambdas, receive queue messages, mutate AWS, call publishers/the model, or modify the library. The second collector requires the first collector's inventory. Signed Lambda download URLs are used in memory and never retained in evidence.

```powershell
python org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_MVP_RESEARCH_20260923/evidence/collect_readonly.py
python org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_MVP_RESEARCH_20260923/evidence/collect_supplement.py
```

Rerunning measures a new vintage; do not overwrite this package's dated evidence with it. The first collector's operation labels were narrowed to executed operations when preserved here; no DynamoDB freshness query was performed. Status parsing in the durable collector uses anchored tag lines and their final match. Current order counts were checked against that rule before publication. The exploratory unanchored parser was discarded, not used as evidence.

The API ZIP's downloaded SHA-256 was compared to AWS CodeSha256, then 48 entry/research Python members were compared to local source with newline normalization. **44 matched, four differed.** This is not whole-ZIP dependency parity, a Terraform apply proof, or a portal-bundle comparison. Inline/attached IAM policy inspection is not a complete effective-access simulation including resource policies, permission boundaries and SCPs.

The S3 supplement hashes selected object bytes and reads only their schema/count aggregates into the durable measurement file. Numeric source records, source articles and human-written report bodies are not reproduced here. A latest modified time is not a freshness acceptance verdict. Two identical historical daily-table hashes demonstrate why physical object counts cannot be summed into unique coverage.

Local library census uses recursive file metadata beneath its 93 immediate folders. Windows scheduled-task states were freshly captured as named states. Disabled tasks and an enabled cloud schedule establish configuration only. Actual schedule execution, recent DynamoDB generations, authenticated browser behavior and analyst acceptance remain NOT_EVALUATED.

CTO message 24746 is a source-attributed late input. Its exact archived carrier is named in MEASUREMENTS.json. The unrun-review observation was not independently reproduced by reading another seat's inbox. Current path-rule definitions were read independently and are recorded in the closer contract and ownership evidence.
