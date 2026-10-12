# Deploy Completion Record
**Date opened:** 2026-10-12T11:34:24.082722+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-w-10 (S9110, THIRD pair): release the CODE of ONE function, opal-portal-data-proxy, by ONE safe-apply of infra/aws/terraform/market-overview at pin 5a0dfc9af8, so lambda_handler stops printing json.dumps(event) (callers bearer tokens) and prints one line Request: method, path, request_id; the firm_page_access.py member differs from the live one in its GENERATED header line only. AUTHORITY: order NFRA_CTLPLN.TO-CT-w-10 AMENDMENT 1 (issuer 2.0.0_SA_COO~C, msg 108522). BOTH HALVES READ WHOLE BEFORE THIS ENTRY: COO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/CT-w-10_PAIR_20261012.md (53 lines, @f716ffd301) and CTO half org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/1.0.0_SA_CTO/NEVER_WIDEN_CT_W10_S9110_LOG_REDACTION_CTO_HALF.md (46 lines, msg 108521). BUILD INPUT THREE members at the pin: lambda_function.py a9c7a40316ec9c92f48ac6a69764df9ec2e5b2c5ab222bdfbba04f643b5adc49, session_tracker.py 00f8c6a31aab295973a9c573f6f8eec83a4e68dbb1eb0cf5c531f4e50873ef40, firm_page_access.py 7365de94fa8059c9a196f86bfe0a457f6825278507c9ec8f827f047bb2b3e868 (all three equal the pair values when read from the pin blobs). LIVE TODAY (second pair): CodeSha256 aWwkzuxRL6SQ49HHgyeoHoFGvSZoLXLymYOQi9dWiWY=, members 17b122b0... 00f8c6a3... 80590106.... ARTIFACT KEY market-overview/opal-portal-data-proxy.zip; PREVIOUS (rollback) version id iuIjViflW5mz8ggUo9w.jxijqwIEKE8p (25996 bytes, content-sha256 equal to the live CodeSha256); rollback = re-point s3_object_version to it by one safe-apply, one resource moved, then re-read R1; a rollback re-opens the Event print and is reported at once. CONSUMERS: a Lambda pulls no task family or image tag; none exist. CALLERS of the exercise: the second pair rulings; ui_walker_account.py takes no second account id (PK constant), so option (a), one synthetic row on firm 49financial tier advisor created and deleted inside this entry, token <=60 min, never printed. BOUNDS: one function code only; no IAM, API Gateway, authorizer, env, layer, log-group or retention change; the log group is NOT purged; no update-function-code; no token or cookie VALUE printed or stored anywhere; a long-lived credential found in the pre-apply measure is a STOP with one line to Andrew for a purge.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE state, PRE log-group measure and P0 | BEFORE state recorded; PRE: counts over the whole 14 day log group of JWT-shaped lines, lines with Cookie/cookie/refresh and lines with Set-Cookie, KEY NAMES only, and whether any is a long-lived credential (STOP if so); P0: the three deployed members equal the second pair pin |  | OPEN |
| L2 | s3-prefix | build three members at the pin and upload | zip member list read back = exactly three, all hashes equal to the pin; deployed vs built firm_page_access.py diff with the single GENERATED header line excluded is EMPTY, differing-line count printed (expected 1); uploaded version id and content-sha256 recorded |  | OPEN |
| L3 | activation | plan then ONE safe-apply | Branch A exactly 0 to add 1 to change 0 to destroy on aws_lambda_function.portal_data_proxy; anything else STOP and apply nothing |  | OPEN |
| L4 | verify | after-reads, exercise and the new log lines | CodeSha256 equals the built file; deployed package diffed member by member both directions; env and layers unchanged; internal and partner GET /aum/metrics 200; partner class-(ii) route 403; log events written after the apply: counts, jwt_shaped=0, bearer=0, one example line redacted; replan 0-diff |  | OPEN |
| L5 | git | record the deploy | record-terraform-deploy.sh run, source map stamped, annotated tag, push state stated as a measured value |  | OPEN |
| L6 | verify | cleanup | walker disarmed by its own tool; synthetic row deleted only after token exp and read back ABSENT with a control; census of synthetic rows zero |  | OPEN |

## Log

- 20261012T113424Z OPENED by 0.7.0_AE_CloudOps~U7 with 6 leg(s)
