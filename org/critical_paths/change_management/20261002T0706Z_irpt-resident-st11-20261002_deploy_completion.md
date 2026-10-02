# Deploy Completion Record
**Date opened:** 2026-10-02T07:06:53.729017+00:00
**Status:** OPEN
**Deploy:** st11: the resident st10 -> st11 at CLOUD 4f68a17d3a (item 19: a BUSY resolve re-sends a fresh delayed message, 60-minute deadline, RESOLVE_PROVIDER_BUSY) and irpt-ycharts-runner-role + sqs:SendMessage on irpt-generation (CTO batches 120-121); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | tar and install script on new keys in opal-313476888478-lambda-artifacts ec2/investor-reporting-ycharts/resident | both read back by S3 version with sha256 equal to the built bytes | irpt-resident-4f68a17d3a-st11.tar.gz version iifNrF9aaIxbauvQAWUBqui7BpLHfGq2 read back sha256 27d8107f585d998be269c165587e61f866d899699ec3717ad333aa5cead0e7be (762644 bytes, 404 before); resident_host_install_4f68a17d3a-st11.sh version Of7y6LTygJwlezKP0MuY3TBi5rmRM8XB read back sha256 51a21c45ea57203256f6c2c444c06d99064230eb0ad489c74e9aa7ee649c9b78 (8705 bytes, 404 before), byte-equal to ST11/resident_host_install_4f68a17d3a-st11.sh; gate ST11/GATE_OUTPUT_20261002.txt PASS (243 members, 8 changed) | CLOSED 20261002T070814Z |
| I1 | verify | ONE targeted safe-apply of aws_iam_role_policy.runner_resident in the ycharts root (adds sqs:SendMessage on irpt-generation only), BEFORE the install | apply output; the applied policy read back lists the five actions; a re-plan reads no changes |  | OPEN |
| D1 | ec2-baked-asset | install on i-0167fd745ad906a66 through Systems Manager, both halves at HEAD first | the script's output: tar and member checks, factory check, unit restart, poll; or its rollback |  | OPEN |
| V1 | verify | the running root and digests read back on the host | root 4f68a17d3a-st11; resident_worker and resolution_broker digests equal the packet's; unit active and polling; queue 0/0 |  | OPEN |

## Log

- 20261002T070653Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T070814Z LEG U1 closed: irpt-resident-4f68a17d3a-st11.tar.gz version iifNrF9aaIxbauvQAWUBqui7BpLHfGq2 read back sha256 27d8107f585d998be269c1655
