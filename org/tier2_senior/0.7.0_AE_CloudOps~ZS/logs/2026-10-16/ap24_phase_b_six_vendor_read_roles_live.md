# 2026-10-16 session log -- 0.7.0_AE_CloudOps~ZS (re-seated ~02:20Z)

**archetype:** DEPLOY

## What was done

1. **Startup.** `/watcher` (registered, one inbox Monitor, re-armed once on its 30-minute expiry), `/cloud-ops` once. Three never-widen halves of
   `NFRA_OPLGTW.TO-OG-ap-24` arrived by mail and were checked against the files, not the relays: COO `947810faa8`, CTO `1ef958e44b`, CVO `5b66771763`,
   all at `.tf` sha256-16 `21a54e8f197eeea2` (re-hashed by this seat before the first apply). The CTO relay called the COO half "last owed"; it was already signed (msg 34633).
2. **OG-ap-24 Phase B, GO msg 34663 (02:36Z).** Ledger `nfra-oplgtw-grants-ap24` opened first (8 legs, entry and sentinel committed), then six role + inline-policy pairs applied ONE at a
   time through `safe-apply`, targeted, each plan 2/0/0 and apply 2 added: inf-orion, inf-eclipse, 49f-blackdiamond, cot-commonwealth, cot-blackdiamond, smartx. Each read back
   from IAM (trust principal `opal-gateway-role` only, no Condition, 1 inline policy, 0 attached) and re-planned No changes. 12-target re-plan No changes. Live
   `gateway-blackdiamond-read-policy` `4893211d4408180a` and `gateway-schwab-read-role-policy` `a3e8ca81172af8cc` unchanged. `iam simulate-principal-policy`,
   one resource per call, 6 of 6 roles: in-prefix GetObject allowed; other prefix, `opal-data-bd` and PutObject explicitDeny; each first table prefix holds objects (KeyCount 5; Commonwealth 1).
   Ledger CLOSED, `GR_APPLIED.json` written (`19b3257eb9`). Local tag `opal-gateway-v1.7.1` at that commit.
3. **Proof.** AC1 PASS. AC2: the order's `<expect>` needs `; policy live yes`, which `ap24.AC2.sh` never prints, and the script's role list names the pre-existing BD role, not the 49F role. Recorded
   AC2 FAIL with the true output, instance VALID; BLOCKING row `NFRA_OPLGTW-Z-S158` (disarm_owner `2.0.0_SA_COO~O`); commit `c0f73fe730`. Order left `pending`. Reported once to the issuer.

## State left

- Push state: LOCAL @c0f73fe730; origin `box/sitez` read `253bc0fe3f` (ls-remote 03:1xZ). The tag is local too. Not this seat's push.
- Open for `OG-ap-23` (not this order): CVO C1 (one real AssumeRole, needs the gateway instance role) and C2 (SmartX two-firm arm). The roles are unused until then.
- Nothing is held open: ledger closed, no worktree created, no scheduled task touched.

## Compiler Tools

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | six targeted applies, rc 0; `market_update_s3_root` has no default and was fed the `address()` value as `variables.tf` says |
| `deploy_ledger.py` | PASS | `open` commits itself; `close` left the closed entry and the sentinel deletion uncommitted, so they went in the Phase B commit |
| `proof-of-spec-check.py` | PASS | first run INVALID (kind `other`, AC2 expect mismatch, aws row path); kind fixed, AC2 recorded as the script printed it, then VALID |
| `comp-schedule --drift` | gap | carrier C2 read "scanned 0 of 25 ledger entries; BUDGET PARTIAL", not read as zero; no schedule is added by this order |
| `iam simulate-principal-policy` | PASS | one resource per call; existence read beside each prefix |

## Later in the same session: OG-ap-24 closed, OG-ap-25 done

4. **OG-ap-24 closed.** The issuer amended `ap24.AC2.sh` at `d55475e545` (Z-S158); AC2 re-run PASS, instance VALID, order flipped complete (`dcc3ac9174`). Row `Z-S159` records the condition met.
5. **NFRA_OPLGTW.TO-OG-ap-25 (etf-classifications read grant), complete.** Phase A 04:53Z-05:03Z (GO 34735): one `aws_iam_role_policy` on `opal-gateway-role`, `dynamodb:GetItem` on the table ARN, plan 1/0/0, 0 of 24 role policies named the table, AC1 PASS (`31f5f961c1`). Halves signed CTO `9fc726f92a`, COO `d87f790253`, CVO `be6d23b7f6` at `.tf` c51c268d41b63e8f / ask 01861a288d2b. Phase B 05:12Z-05:22Z (GO 34744): ledger `nfra-oplgtw-grants-ap25`, one targeted `safe-apply` (1 added), read back (one statement, GetItem only, the table ARN), simulator GetItem allowed / Scan, Query, PutItem implicitDeny with a positive control, describe-table ACTIVE, re-plan No changes, ledger CLOSED (`3ba4af364d`). AC1 and AC2 PASS, instance VALID, status flipped. The policy is unused until the OG-ac-2 release.

## Compiler Tools (OG-ap-25)

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | one targeted apply, rc 0 |
| `deploy_ledger.py` | PASS | 3 legs closed with proof; `close` leaves its own records uncommitted |
| `comp-schedule --drift --budget 420` | PASS | 6 of 6 carriers in 211 s; C4 and C5 PARTIAL_OR_BLIND, not read as zero |
| `terraform init` | note | a new `opal_name` module call needs it before any plan ('Module not installed'); no tracked file changed |
| `proof-of-spec-check.py` | PASS | VALID first run (kind `aws_resource` used for the IAM row) |

## OG-ap-26: the etf-classifications grant moved to the internal reader role

6. **NFRA_OPLGTW.TO-OG-ap-26, complete.** The issuer's placement error in OG-ap-25 (the tool reads as `gateway-global-internal-reader-role`). Phase A 06:18Z-06:23Z (GO 34754): the `role` line of the one policy changed to `aws_iam_role.int_reader.id`, plan 1/0/1, internal reader at 4,112 of 10,240 inline characters with it, AC1 PASS (`52b0ff8f89`). Halves signed CTO `4d0a8d3c0d`, COO `90b589c58f`, CVO `f2cf55e41e` at `.tf` 867087958bac89b9 / ask 69466be19798. Phase B 06:31Z-06:41Z (GO 34769): ledger `nfra-oplgtw-grants-ap26`, one targeted `safe-apply` (1 added, 1 destroyed), read back on both roles (present on the internal reader, same document hash `609426e6a083440b`; absent from the instance role, 25 -> 24), simulator internal reader GetItem allowed / Scan implicitDeny, instance role GetItem implicitDeny, positive control allowed, re-plan No changes, ledger CLOSED (`d2e1fd6cef`). AC1 and AC2 PASS, instance VALID, status flipped. The COO was told AC2 was green at once, because OG-ap-23's deploy waits on it.

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | one targeted apply, rc 0, destroy then create in about a second |
| `deploy_ledger.py` | PASS | 3 legs closed with proof |
| `comp-schedule --drift --budget 420` | PASS | 6 of 6 carriers in 253 s |
| `iam list-attached-role-policies --query ... --output text` | trap | on a role with NO attached policies the text query exits non-zero through the `.tools/aws` shim; read it as `--output json` |
| `proof-of-spec-check.py` | PASS | VALID first run |

## OG-ap-27: the four denied prefixes granted to the internal reader

7. **NFRA_OPLGTW.TO-OG-ap-27 (release-gap grants), complete.** The OG-ap-23 served read found four of 27 tools denied (row Z-S164). Phase A 08:41Z-08:50Z (GO 34855, follow-up 34858 to quote the CTO's model_composition ruling): two `aws_iam_role_policy` on `aws_iam_role.int_reader`, one per bucket, the four prefixes read from the committed catalog rows (`bbg/`, `snapshots/`, `mdpf/etfs/gold/new_securities/` of `opal-data-etfs`; `mdpf/feeds/model_composition/` of `opal-data-mdpf`), no `silver/*`, no firm token; plan 2/0/0; ask `7be8a06df4`. `ap27.AC1.sh` counted the condition key `s3:prefix` as an action and could not match its expect: row `Z-S165` (BLOCKING), the issuer fixed the script, the `.tf` was not bent. Halves signed CTO `c18e2e007c`, COO `b5652f6db9`, CVO `b121849fbe` at `.tf` be09d3dd3aaebdd9 / ask 38817328cc91. Phase B 08:58Z-09:12Z (GO 34868): C2 live re-read (7 inline policies, names absent), ledger `nfra-oplgtw-grants-ap27`, one targeted `safe-apply` (2 added), both policies read back (7 -> 9), simulator GetObject 4 of 4 and ListBucket 4 of 4 allowed, out-of-scope 2 of 2 and 2 of 2 not allowed, positive control allowed, re-plan No changes, ledger CLOSED (`e5d53534f6`). AC1 and AC2 PASS, instance VALID, status flipped. The COO was told AC2 was green at once (its C4: it reads AC2 itself before re-GO of OG-ap-23).

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | one targeted apply of two resources, rc 0 |
| `deploy_ledger.py` | PASS | 3 legs closed with proof |
| `comp-schedule --drift --budget 420` | PASS | 6 of 6 carriers in 197 s (second run of the day within budget) |
| `terraform init` | note | two new `opal_name` module calls needed it before any plan |
| `proof-of-spec-check.py` | PASS | VALID first run |
| catalog read | note | `DATA_CATALOG.yaml` rows are `- entity:` list items nested under `channels`; a `/tmp` file written by Git Bash is not visible to native Python on this box, so read the YAML straight from `git show` through a pipe or a scratchpad path |

## OG-ap-29: the dedicated 49F live read role

8. **NFRA_OPLGTW.TO-OG-ap-29 (49F Black Diamond live read role), complete.** CTO ruling @8b2865e461, row Z-S292. Phase A 13:49Z-14:19Z (GO 35045): one `aws_iam_role` (trust only `opal-gateway-role`) and one inline policy on `opal-data-bd` `silver/{unrealized,transactions,allocations,fees}/`, the four tables confirmed against `client_adapter_bd49f.py` and the committed catalog rows; plan 2/0/0; the instance role needs no change (the OG-ap-24 roles work by trust alone). Two walls: the naming limb refused every typed S3 address (15 graded, 0 admitted), so four read rows `gateway-client-bdlive-*` went into `legacy_addresses.json` first (`bd93455796`) and the `.tf` reads its addresses from them; that commit needed the audited override `GIT_COMMIT_AUTHOR_OVERRIDE=PLATFORM_LOGIC_DOCS` (the lane admits only the CRO; the same act passed at 00:23Z and I could not find why) and I told the COO it is a lane-coverage gap. `ap29.AC1.sh` then read typed prefixes in the `.tf` text and could not pass a naming-conformant file: row `Z-S294` (BLOCKING), the issuer fixed the script, the `.tf` was not bent. Halves signed CTO `7877e044d7`, COO `b6c6de7fbe`, CVO `6b7d6ef48d` at `.tf` 5604d8577f68a50d / ask 369a8e7a12f7. Phase B 14:40Z-14:57Z (GO 35070): C2 live re-read (role absent, instance role 24 policies, 49F role policy `ceb6ae001918528d`), ledger `nfra-oplgtw-grants-ap29`, one targeted `safe-apply` (2 added), read back (trust only the instance role, policy equals the file, instance role still 24), simulator GetObject 4 of 4 and ListBucket 4 of 4 allowed, 4 of 4 negative controls explicitDeny, positive controls allowed, existence counts KeyCount 1 each (no object read), re-plan No changes, ledger CLOSED (`50e9252cc5`). AC1 and AC2 PASS, instance VALID, status flipped. The COO was told AC2 was green at once (its C4).

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | one targeted apply of two resources, rc 0 |
| `deploy_ledger.py` | PASS | 3 legs closed with proof |
| `comp-schedule --drift --budget 420` | PASS | 6 of 6 carriers in 288 s |
| naming limb (`safe-commit.sh`) | note | refuses ANY typed S3 address in a new `.tf`; the form that passes is `jsondecode(file(legacy_addresses.json))` locals over registry rows committed first; a literal that equals a registered template is still refused |
| `GIT_COMMIT_AUTHOR_OVERRIDE` | note | used once, for the registry rows (`PLATFORM_LOGIC_DOCS`); audited at 14:10Z |
| `proof-of-spec-check.py` | PASS | VALID first run |

## Close-out: OG-ec-2 build tree removed, lane retired (rule 34)

9. **`C:/tmp/og-rel-ec2` torn down** on the issuer's message 35127 (CTO 35126). Checked first: tip `4fd05be0d3` is an ancestor of `HEAD` and of `origin/box/sitez`; 0 tracked changes, 0 untracked entries, 0 commits ahead of origin; the only content not in git was ignored and regenerable (`.terraform/` provider cache, `__pycache__`, two log files; 76 MB). `git worktree unlock`, `git worktree remove` (no force), `git branch -d rel-nfra-oplgtw-ec2` (was `4fd05be0d3`): worktree and branch absent, the commit still resolves. This is the cleanup skill's `merged-worktrees` pool and the "ref already contained in its trunk" case.
10. **Retired.** Andrew-direct 2026-10-16 ~15:4xZ (rule 34): idle single-task CloudOps lanes close. Orders OG-ap-24, -25, -26, -27 and -29 are complete; nothing is held open (no ledger, no worktree, no scheduled task). Owed to others, handed to the COO in the reply: disposition of rows Z-S158, Z-S165, Z-S294; the CTO's note that the four `gateway-client-bdlive-*` registry rows should name the new live catalog rows once `NFRA_MCPINDEX` lands them (this seat will not be here to do it); the local tag `opal-gateway-v1.7.1` (not pushed); the `PLATFORM_LOGIC_DOCS` lane gap behind the one audited override.

| tool | result | notes |
|---|---|---|
| `git worktree remove` | PASS | no `--force` needed: ignored files do not block it |
