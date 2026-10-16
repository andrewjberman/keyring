# MP-pf-9 -- the bundle-only gateway release (lane 0.7.0_AE_CloudOps~MQ)

**archetype:** DEPLOY

Order: `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pf-9.gateway-page-bundle-only-release.md` (amendment A1 @`66a4be01d8`). Close report:
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-pf-9_CLOSE_REPORT.md`.

## Current State

**Complete.** `opal-gateway` on `i-07dccb1615503ac99` runs release commit `d14445961dd6d04275ca8186372a4df4c4fcc5cc` (branch `rel-nfra-mcportal-pf`, worktree `C:/tmp/mp-pf-rel`, LOCAL), cut on the live
base `38fe44d5cb`; the dashboard bundle is the build of mcportal `c66ca82952`. AC1 PASS, AC2 PASS, proof instance VALID rc=0, ledger `nfra-mcportal-pf-bundle-release` CLOSED (4 of 4 legs).
/health 200; MCP tool names 127 before and 127 after (0 added, 0 removed); no-identity `/` and `/gateway` 401; pull-and-restart 20 s.

## Deployment Sequence

1. GO-PREP (msg 34994): release tree on the live ref (S3 `git-ref` 38fe44d5cb), one-line pin `3cc7017f1f`, census, resolve-only, bun precheck 77 of 77, tests (11 failed: 5 excused class, 6 AssertionError -> row Z-S67, ruled in A1).
2. Rollback proven: old pin rebuilt in a clean detached tree equals the host's dashboard on all four members by sha256; the new build differs in `index.html` and the CSS. ASK `be51a362cd`; halves CTO `08e2ffae65`, COO `e8eb2d5f5d`.
3. GO (msg 35010): re-read live ref (equal), ledger open + pre-act record (`d14445961d`), host world before (SSM `7b6faefe-...`), deploy: first run refused before upload (row Z-S68), second run landed at 13:24Z, host world after (SSM `4dba1956-...`), manifest record `bddaf03886`, ledger close `864f262ffc`, pointer re-added `f829a3eaa8`, AC1/AC2.

## Verification (actual output)

AC1: `entry files at HEAD=1; sentinel=no; listed OPEN/HELD=0 ... is c66ca82952: yes; descends from 090b9cdc85: yes ... gateway files changed between them=0 ... RESULT: PASS`.
AC2: `/health=200; no-identity / =401 /gateway=401 ... host bundle == build of c66ca82952: yes; index.html names exactly the two assets: yes ... RESULT: PASS`.

## Blockers

None. Three things sit with the issuer: disposition of rows Z-S67 (ruled), Z-S68 and Z-S69; the drain of `rel-nfra-mcportal-pf`; flipping the order's `<status>`.

## Compiler Tools

- `.tools/deploy_ledger.py` open / close-leg x4 / close: PASS; `close` drops a hand-added Log line (re-added after).
- `safe-ec2-deploy.sh` + `deploy-to-ec2.sh`: first run refused pre-upload (sparse tree lacked `/data/mdpf/config/`), second PASS 102 s; the wrapper's manifest commit failed on the tree-local naming gate (vintage), recorded by hand.
- `bun_cache_precheck.py`: 77 of 77 twice. `.tools/safe-commit.sh` run from the trunk inside the release tree: PASS. `.tools/proof-of-spec-check.py`: VALID rc=0 after two `introduces` tokens were corrected (a token must be absent at the pin's parent and present at the pin).
- `comp-find` once (bun precheck path); the rail denied two blind greps and each was re-run in the form it named.
- Gap: no tool measures the host's tool-name registry; the read is a base64'd python snippet run over SSM (`C:/tmp/pf9_hostread.py`).

## Next Steps

1. `[2.0.0_SA_COO~MP]` Read the close report; disposition Z-S68 / Z-S69; drain `rel-nfra-mcportal-pf`; flip the order's `<status>`; the graded 390 / 1280 px read.
2. `[0.7.0_AE_CloudOps~MQ]` Hold `C:/tmp/mp-pf-rb`, `C:/tmp/mp-pf-mcp-old`, `-new` (and the earlier rollback trees) until the round closes. No open task order.
