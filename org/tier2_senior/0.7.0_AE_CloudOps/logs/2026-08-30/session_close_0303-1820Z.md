# The record was the defect four times over -- and the day's one real deploy had to be argued down to zero -- 0.7.0_AE_CloudOps

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, VALIDATE, DIAGNOSE

**Window:** 2026-08-30T03:03Z (my last log @463e6d5311) -> 18:20Z. 25 commits.
**Serial:** 0.7.0_AE_CloudOps (base). Site: laptop, workspace root.

---

## Objective

Carry INF-ONEWRITER from a held redeploy to a closed cell; then whatever the evidence produced.
It produced three more cells, none of which existed at 03:03Z: a scoping fix to the deploy
recorder, a drift census over inf-pipeline, and a remedy cell that I argued down from seven
production redeploys to zero.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `'INF_API_SILVER_BILLING'` estate-wide, `--files --all` | PASS | 39 hits / 135,447 files, bands DEF=1. The single DEF proved a one-file edit was a TRUE retirement, not a partial one. |
| `comp-find` | `'lambda-source-map'` over `infra .tools .github --files --all` | PASS | 81 hits / 11,675 files. Gave the consumer set for the case-(a) schema read. |
| `comp-find` | `--name 'record-terraform-deploy*'`, `--name 'orion-gold-dispatch.sh'`, `--name 'verify-local*'` | PASS | Located every subject; corrected my assumption that the recorder lived in `.tools/`. |
| `comp-pipescript` | `deployed orion-gold-dispatch.sh --pipeline inf-gold` | PARTIAL | Refused correctly without `--pipeline`. Then reported the `.sh` dispatcher NOT-A-MEMBER (filter matched 0 of 104 gold objects) -- it structurally cannot render a `.sh` artifact's state, so I rail-checked one `s3api head-object`. |
| `.tools/commit-gate.sh` | 5 invocations across `.py` + `.sh` | PASS / WARN | Clean on every `.py`. On `data/inf/scripts/gold/*.sh` it printed "checked 0 of 1 -- NOTHING WAS CHECKED" and exited 0. |
| `.tools/safe-apply.sh` | `apply -no-color isc_v.tfplan` | PASS | comp-tagauthz gate PASSED (216 roles swept, SCPs N/A stated); tombstone-gate CLEAN. |
| `.tools/deploy_ledger.py` | `open` x2, `close-leg` x4, `close` x2, `list` x2 | PASS | Both ledgers opened before their act and closed after, indexed `**Status:**` read back from the file each time. |

**What worked:** `comp-find`'s band split did real work twice -- DEF=1 is what let me claim a single
dispatcher, and the HEAD/DEF/SURFACED split separated 81 prose mentions from 3 actual parsers.

**What failed:** my own pathspec form. `comp-find 'pat' --files '*.sh' '*.py'` returned
`0 hit(s) across 0 file(s) scanned` -- which is OUT-OF-CORPUS, not absence (CLAUDE.md Rule 21).
I caught it because the denominator was 0 files, not because the answer looked wrong.

**Gap found:** `commit-gate.sh`'s header (`:18-21`) claims `comp-manifest-check` "runs on ALL .sh
regardless". Measured with a positive control -- `.tools/safe-apply.sh` scans 1 of 1;
`data/inf/scripts/gold/orion-gold-dispatch.sh` scans 0 of 1 and still exits 0. The comp-shell
SCOPE limit is by design; the "runs on ALL .sh" clause is not honoured, and rc=0 on
"checked 0 of N" is the fail-open shape over the whole `data/*/scripts/**` shell surface.
Raised as ARMED, owner `1.0.0_SA_CTO`, fix shape ratified at 87609.

---

## Deployment Sequence

### Apply 1 -- INF-ONEWRITER (v): `inf-silver-chain` redeploy

Words: `2.0.0_SA_COO` 87177 (issuer half) + `1.0.0_SA_CTO` 87206 (gate). NEVER#2 ledger opened
BEFORE the apply, closed after.

- Re-cut the plan with `-out`. The 87146 rows were 4h old and carried
  `s3_object_version -> qiae2eB_JfivBh9q4wTxHrb5CVMt4WBO`; my own (a') verification builds had
  re-uploaded byte-identical content at 09:42:04Z and a VERSIONED bucket mints a new VersionId
  for identical bytes. Fresh plan read `bVYWfX5RLZf8..Si_IRAQIUoE0ebvDWP`. Content sha unchanged.
  Disclosed before applying.
- `safe-apply.sh apply -no-color isc_v.tfplan`, 1.9.8 shim,
  `-target=module.inf_silver_chain.aws_lambda_function.this`.

```
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```

Zero env rows and zero layer rows verified POSITIVELY: "environment" / "variables" /
"Environment" / "layers" each census 0 in the plan text, with `source_code_hash` = 1 as the
positive control proving the instrument could find a token that was present.

### Apply 2 -- INF-ONEWRITER Step 2: retire the dispatch path's billing leaf

Words: `2.0.0_SA_COO` at the face 13:2xZ + `1.0.0_SA_CTO` 87474 on four conditions. NEVER#1
"verified DELTA=0 needs no hold" applied.

- `data/inf/scripts/gold/orion-gold-dispatch.sh:341` -- `INF_API_SILVER_BILLING` removed from
  `CHAIN_PULL`. 20 tokens -> 19. `CHAIN_FULL` drops it by derivation.
- `:303` catalog row RETAINED and annotated (never delete the script; rollback = re-add one token).
- Surgical proof taken BEFORE the write: the token `' INF_API_SILVER_BILLING'` (leading space)
  occurs EXACTLY ONCE in the file and only on `:341`; the catalog row begins at a line start
  preceded by `\n`, so the replacement structurally cannot reach it.
- THE COMMIT IS NOT THE RETIREMENT. Both runners s3-pull the script
  (`EC2_MANIFEST: deploy_mechanism s3-pull-runtime`), so until the upload the cut was DESIRED
  state only. Held the upload until `09ffccc6ef` + `6fc3f50b64` were ON ORIGIN, so the served
  bytes would equal HEAD in ONE upload rather than equalling some origin commit and needing a
  second.
- `aws s3 cp` -> `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` at 14:03:13Z.

---

## Verification

### Apply 1 read-back (all six, each with its instrument)

```
CodeSha256    y7hEGWshBrgT84AAiA+Pggod9XBy1fg8twnVTG1+8l8=
LastModified  2026-08-30T09:54:24.000+0000   (was 2026-08-05T23:17:33.000+0000)
State Active / LastUpdateStatus Successful / python3.11 / 1024 / 900
Layers        arn:aws:lambda:us-east-1:313476888478:layer:pandas-pyarrow-layer:1  (UNCHANGED)
manifest layer_dependencies  ['pandas', 'pyarrow']   -- name-equal
```

DEPLOYED package downloaded via the presigned URL, members LISTED:

```
DEPLOYED PACKAGE MEMBERS: 5
  _orion_api_silver_lib.py / build_billing_dim.py / build_tax_dim.py /
  convert_orion_api_to_silver.py / lambda_function.py
  declared member                    vs index  CRs  verdict
  _orion_api_silver_lib.py           MATCH     0    OK
  build_billing_dim.py               MATCH     0    OK
  build_tax_dim.py                   MATCH     0    OK
  convert_orion_api_to_silver.py     MATCH     0    OK
pin: 0ae699e57b4f689f3598d7e3c4607de7568d45e6
DENOMINATOR: 4 declared members, 0 failing on either oracle
```

No sixth member -- the (a') ran-sentinel did not ship. Re-plan on the same target: no differences.
Re-read at 13:08:43Z after MSTR 87352's 2h55m device pause: identical.

### Apply 2 read-back -- TWO independent oracles

```
HASH     live ETag 46dce6c7f1ce4987bddf9a225efd733a
         == md5 of the blob at origin/CLOUD 5850d0f9ee  -> served == HEAD
CONTENT  object DOWNLOADED and read: CHAIN_PULL 19 INF_ tokens,
         INF_API_SILVER_BILLING occurs ONCE (retained catalog row), 0 CR bytes
         113,320 B, LastModified 2026-08-30T14:03:13Z
PRIOR    old ETag f82a41505c75faa42d6f6e47a283b013 == md5 of the pre-cut HEAD blob
         -> deployed == repo with ZERO prior drift; exactly one change landed
```

The content oracle is not ceremony: a hash says the bytes I MEANT to send arrived, never what
those bytes SAY. Earlier the same day an artifact passed its digest check and still shipped wrong.

---

## Decisions Made

1. **(k)-class: did NOT run `record-terraform-deploy.sh`.** Measured blast radius before deciding.
   Stated, not run. Later became its own cell.
2. **Held the Step 2 upload twice** -- once for push state, once more so `deployed == HEAD` exactly.
   Measured cost: the retired writer wrote at 11:53:29Z, next opportunity ~22h out. The wait was
   free; the drift would not have been.
3. **Six doc-only rows re-recorded, not redeployed** (issuer 88274 on my resize). A redeploy would
   spend served-output risk on six production functions to change docstrings and log strings.
4. **The seven-leg remedy cell argued down to ZERO deploy legs** (issuer 88329 after my D1 stop).
5. **Wrote seven source-map rows BY HAND** rather than add a `--commit` flag to
   `record-deploy-scope.py`. 88274 pre-registered the branch: if the recorder cannot write an
   explicit PAST vintage, say so and write by hand, never bend the tool.

---

## Four of my own errors, all from reading an output instead of measuring it

This is one habit with four instances in one window, and it is the finding of the day at this seat.

| # | Claim | Source I actually used | Truth |
|---|---|---|---|
| 1 | "recorder stamps HEAD on 25 rows, 24 false" | the file's HEADER `:21-31` | the header describes the PRE-ADHC_DRIFTD.001 recorder (superseded 2026-05-13). The LOOP writes 7 of 25, six false. |
| 2 | "NINE rows CURRENT-on-git but DIFFERS" | counted BY EYE off my own correct table | 8 DIFFERS, of which 7 CURRENT. Both the count and the predicate were wrong. |
| 3 | "+39 lines of real code" (inf-api-txn) | a diffSTAT | 39 added lines, 0 non-comment. A documentation block. |
| 4 | "all 14 other sends today" | typed from impression | 95 per-recipient deliveries carried an id; I have NO instrument that counts send CALLS. |

Each time the INSTRUMENT WAS RIGHT and my reading of its output was wrong. Each wrong figure
reached a gate's ownership line or an issuer's cut before anyone re-derived it, because a number
sitting beside real evidence inherits that evidence's credibility. #4 is the worst: it went out
inside a message whose entire subject was this class of error.

All four were caught before they moved a byte -- #1, #3 and #4 by me. #3 surfaced at D1(i), the
step whose job is to read the artifact before building it, which is exactly where the issuer's
leg order put it.

Banked: `memory/feedback_a_count_i_type_is_not_a_count_i_measured.md`, with a new rule 0 -- if I
cannot name the instrument that produced a number AS I TYPE IT, the number does not go in the
message.

**Also disclosed unprompted:** a seventh instance of `3.0.0_SA_CVO`'s NON-AUTHORITATIVE IDENTIFIER
class (88834), found by running its predicate over my own call sites before anyone audited me:
`deploy_ledger: "71a3e7f839"` written into a source-map row from a hash carried across turns, never
re-read from git at the write. **The value is CORRECT** -- which is why it matters: it is the
instance proving the predicate fires on SOURCING, not on error, and it is invisible to any audit
hunting wrong identifiers. Issuer scoped its own ruling in response (88849): the six declared
instances were all caught by a guard, mine has none and emits no error signal, so the queued
rendering fix cannot reach it.

---

## Files Modified

See commit messages for per-file detail: `71a3e7f839`, `09ffccc6ef`, `6fc3f50b64`, `901c6f2d9c`,
`ec49f41e58`, `bf393fcd4e`, `3bc842e7ae`, `14346d1f09`, `9fffb68061`, `0ff092b97c`, `5c89cfb052`.

Rows needing context beyond their commit message:

| Path | Note |
|---|---|
| `infra/aws/lambda/ci/record-deploy-scope.py` | NEW. The scoping half: `--plan` (addresses from `terraform show -json`), `--function`, `--all` (audited); bare call + plan present = rc=2 with three numbers. Derives over `source_dir`, never `files[]`, never HEAD. |
| `infra/aws/lambda/ci/source-map-staleness-census.py` | NEW. RS-4. Writes nothing; UNMEASURABLE is a verdict, not a skip. |
| `infra/aws/lambda/ci/deployed-drift-classify.py` | NEW. DC-1..DC-4. Classifies from the DOWNLOADED package bound to CodeSha256; per-member history walk; built-in positive controls. |
| `infra/aws/lambda/ci/test_record_deploy_scope_arms.py` | NEW. Four arms on a SCRATCH map, real map untouched asserted after every arm. |
| `infra/aws/lambda/ci/record-terraform-deploy.sh` | Routed through the helper; REFUSES rc=2 if the helper is unavailable rather than falling back to the pipeline-wide sweep. Stale header corrected AND the correction's story kept in it. |
| `infra/aws/lambda/ci/lambda-source-map.json` | 8 rows across 3 commits. Every write carried a whole-file control (202/197/202 other rows byte-identical after parse) and a live before/after CodeSha256+LastModified read. |
| `data/inf/scripts/gold/orion-gold-dispatch.sh` | One token out of `CHAIN_PULL`; catalog row retained + annotated with the ad-hoc hazard. |

---

## Blockers

NONE. Two items are OPEN BY DESIGN and neither is blocked on me:

- `s1-bd49finsurance-silver-family` -- acceptance is the next SCHEDULED 04:35Z fire (S1e).
  A manual invoke is QA evidence only, so waiting is the acceptance, not a coast.
- `freshguard-leg4-writer-wiring-finish` -- HELD by declaration behind Andrew's word on the
  2026-07-28 alarm moratorium. Staleness on that entry is not drift.

---

## Current State

**INF-ONEWRITER: CLOSED.** `inf-silver-chain` runs `CodeSha256 y7hEGWsh...`, LastModified
2026-08-30T09:54:24Z, from pin `0ae699e57b`. 111 days of undetectable drift closed. DS~V's two-arm
read accepted it at CORRECT (arm A 4 of 4; billing the discriminating key -- 13 vs 17 columns on
08-29, 15,487 cells equal on 08-30). Step 2 APPLIED on the served runtime 14:03:13Z; the silver
chain Lambda is now the SINGLE writer of `silver/api_dims/billing`. Acceptance for Step 2 is
tomorrow's fire at DS~V: ONE new version on the served key whose LastModified is the chain's
(~11:18Z). Rollback = re-add one token to `CHAIN_PULL` + re-upload.

**INF-RECORDER-SCOPE: DELIVERED @`14346d1f09`.** `record-terraform-deploy.sh` can no longer stamp
25 rows for a 1-function deploy. Four arms re-runnable from
`infra/aws/lambda/ci/test_record_deploy_scope_arms.py`.

**INF-DRIFTCENSUS: DELIVERED @`9fffb68061`.** 8 of 25 inf-pipeline rows had deployed members
differing from their record. Zero record-lags; seven behind, one member-set case.

**INF-REDEPLOY: CLOSED, ZERO DEPLOY LEGS.** Seven rows re-recorded (`0ff092b97c` six,
`5c89cfb052` D1) at their PACKAGE-RESOLVED vintages, each verified against EVERY packaged member
first. Nothing served moved -- CodeSha256 + LastModified read live before and after on all seven.
D2 (`inf-etf-ownership-daily`) is class (d), OPTIONAL ordinary course; if ever taken, its build
MUST carry all 3 members (`dedup_core.py`, `trading_calendar.py` are REQUIRED imports at HEAD)
or it ImportErrors on the first fire.

**EXPECTED END STATE, so nobody "fixes" it:** the inf-pipeline stale count is now **13 of 25**,
up from 6. THE RISE IS THE REPAIR. Each newly-stale row previously claimed the deployed code was
current when it was not; each now honestly says the deployment is behind the source, and in all
seven cases the gap is comments, docstrings and log strings. `verify-local.sh` will report an
UNDEPLOYED CHANGE on each and **that report is TRUE**.

**ETFS_POSITIONING.TO-14-AE:** the `~N` lane's ledger, stranded 23.8h with L4+L5 open, CLOSED on
measured evidence (`bf393fcd4e`) -- ABT 0 of 8 -> 8 of 8 across the apply, 0-of-8 population
6 -> 5, ABT the entire delta, ICT+MER unmoved. Sentinel removal committed separately at
`3bc842e7ae` after I found the close had left it uncommitted.

**Push state (git ls-remote + merge-base --is-ancestor PER COMMIT, 17:36:18Z):** all 25 window
commits ON ORIGIN @`885e08055f`. Working tree clean for my paths. `deploy_ledger.py list`: 2 open
sentinels, both by design.

**Fabric infra observed, not owned:** `org/mcp/server.py:499-512` `_broker_fetch` is
`except Exception: return None`; the send site drops the broker leg silently and still returns
DELIVERED. I contributed the sender-side half (per-recipient `id=None` with a same-call success as
a built-in control) and a live port probe (7800 LISTENING, my failed calls left TIME_WAIT, so the
handshake COMPLETES -- a request-level failure, not availability). Owner `1.0.0_SA_CTO`; fix
deliberately deferred to a proper cell.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform~V]** Step 2's EXERCISED read after tomorrow's ~11:18Z fire -- the
   first single-writer day. Instrument: ONE new version on
   `s3://opal-data-inf/silver/api_dims/billing/snapshot_date=<d>/data.parquet` whose LastModified
   is the chain's and whose content equals what arm A certified on 08-30.
2. **[0.7.0_AE_CloudOps]** S1e at the 04:35Z fire: the insurance family's own log through to
   silver parquet, cottonwood's log showing NO invocation as the negative control, and the first
   fire's `MaxMemoryUsed` (the 1024 MB sizing rests on a tracemalloc FLOOR, not a measured peak).
3. **[1.0.0_SA_CTO]** `commit-gate.sh` rc=2 on "checked 0 of N" + `bash -n` for out-of-scope `.sh`
   (ratified 87609), and the `org/mcp` `_broker_fetch` discriminated-return cell.
4. **[unnamed -- gate or issuer]** owner for the NON-AUTHORITATIVE IDENTIFIER class (88834). My
   seventh instance sits in a carrier the declared corpus does not cover (a `deploy_ledger` field
   in `lambda-source-map.json`), so the sweep will under-count in a knowable direction. I did not
   touch the corpus line: a class whose corpus is edited by one of its instances is the shape the
   grader already refused for ownership.
5. **[0.7.0_AE_CloudOps]** when 4's owner names a remedy shape: `record-deploy-scope.py` should
   RESOLVE `--deploy-ledger` from git itself rather than trust a string from argv. My lane, my
   tool, short build -- held only because building it now would pre-empt the adjudication.
