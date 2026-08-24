# 0.7.0_AE_CloudOps~Z -- ETFS_INGEST.TO-1 deployed + exercised; ETFS_POSITIONING.TO-5 advanced to two routed forks

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Window:** 2026-08-24T20:06Z (spawn) -> 22:40Z. Prior log: `session_close_0821T1945-0824T1352Z.md`.
**Seat:** `0.7.0_AE_CloudOps~Z`, site Z, pid 5024. Spawned by `0.0.0_AB_MSTR~Z` on Andrew's C4 ruling.
**Commits (3, all ON `origin/SITEZ`):** `aaec8e05c6`, `d6e5fbe667`, `cd315ac325`. Tag `etfs-netassets-v1.4.0`.

---

## What this session did

**ETFS_INGEST.TO-1: COMPLETE.** The TrueShares holdings CALL SITE (@`4e5800fde0`) is deployed to
`etfs-netassets-daily` and EXERCISED on the 22:00Z scheduled fire. 29 DIVZ + 44 IDVZ constituent rows
landed where five consecutive fires had silently landed none. 5/5 criteria PASS, proof-of-spec VALID,
deploy ledger CLOSED with all 7 legs proven, in-session per NEVER#6.

**ETFS_POSITIONING.TO-5: advanced, not started as an apply.** Preconditions re-derived 3/3, design call
made and stated, schedule MEASURED, run_class classifier authored and exercised 12/12 with a mutant
control. Two structural forks routed rather than taken. **No TF written, no ledger opened, nothing
applied** -- deliberately, because both forks bear on `source_dir` and `handler`.

---

## The defect TO-1 closed (PRD s.3 F2 / channel Z-S1)

The deployed package carried `fetch_trueshares_holdings` ONCE -- its `def` at `:420` -- and no call
site, while the applied env carried `TS_HOLDINGS_ENABLED=1`. **A grant to a code path the running bytes
did not contain: Rule 22a's exact specimen.** DESIRED passed, APPLIED passed, the scheduled run was
GREEN, and all three were true of the wrong bytes. The deployed code could not even print the `SKIP:`
line, because the else-branch that prints it existed only at HEAD.

---

## Deployment Sequence (AE role addition) -- ACTUAL output

```
1. BUILD    bash infra/aws/lambda/ci/build-and-upload.sh etfs-netassets etfs-netassets-daily
            SHA256:  BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=
            OK s3://opal-313476888478-lambda-artifacts/etfs-netassets/etfs-netassets-daily.zip
               (write VERIFIED: size=19948, sha256 metadata match)

2. APPLY    HALT_ACK=1 SAFE_APPLY_TERRAFORM=$(command -v terraform) .tools/safe-apply.sh \
              -chdir=infra/aws/terraform/etfs-netassets apply -input=false -no-color -auto-approve
            ~ source_code_hash "tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI=" ->
                               "BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo="
            ~ s3_object_version "LHVGHRZbz5ruxDazzJmR9SjC32Iyj.6H" -> "n09ipru8mC3uQqkiXaQmqZVnO1KAjAkc"
            Plan: 0 to add, 1 to change, 0 to destroy.
            Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

3. 0-DIFF   terraform plan -detailed-exitcode  (owning root infra/aws/terraform/etfs-netassets/)
            *** RE-PLAN rc=0 (captured immediately, NO pipe) ***
            No changes. Your infrastructure matches the configuration.

4. RECORD   PYTHONUTF8=1 record-terraform-deploy.sh etfs-netassets --version etfs-netassets-v1.4.0
            [SITEZ aaec8e05c6] ci: record deploy etfs-netassets @ fcdf0429 [skip ci]
            -> then fix-forward d6e5fbe667 (see "A defect I put in my own commit")

5. TAG      git tag -a etfs-netassets-v1.4.0   (rc=0; pushed by MSTR~Z on my report, verified remote)
```

**HALT-GATE fired TWICE and both were correct.** (a) IDENTITY UNRESOLVED, fail-closed, refusing to
guess which agent it was -- I wrote `org/mcp/sessions/<session-id>.serial` per the gate's OWN prescribed
fix, which is NOT an override: it makes the gate scan MY inbox instead of a stranger's. (b) 2 pending
messages surfaced (the 08-21 WA-APPLY / GW-APPLY withdrawals), both read at startup, both explicitly
"nothing is asked of you", neither a STOP, neither touching this root -> `HALT_ACK=1`.

**Rule 5 CONFIRMED, not changed:** live MemorySize 1024 / Timeout 300 / runtime python3.11 post-apply.

---

## Verification (AE role addition) -- ACTUAL output

**AC1 (pre-apply re-derivation, corrected Z-S4 oracle).** Download sha-verified as THE RUNNING
ARTIFACT FIRST -- zip sha256(b64) == live `CodeSha256` -- so the bytes censused are the running bytes,
not a same-named copy.

```
                              DEPLOYED            HEAD (== @4e5800fde0)
  lambda_function.py        f306aa237e3e 49,995B  e6f9fe5391da 51,885B
  NORMALIZED vs 541a393798  EQUAL                 (the commit actually deployed)
  NORMALIZED vs HEAD        DIFFERENT             (correctly: HEAD has the call site)
  landing_guard.py          5,998 B both sides, RAW MATCH, LF   <- discriminating control member
  fetch_trueshares_holdings lines 1/3   occ 1/3
  TS_HOLDINGS_ENABLED       lines 1/5   occ 2/6   (delta is line 392 carrying the token TWICE)
  fetch_filepoint (pos ctl) 3 / 4
  zzz_no_such_token_9999    0 / 0       (negative control, both sides)
PROVENANCE: 6 commits scanned, 1 matched -> 541a393798. Positive control HEAD-vs-HEAD PASS;
negative control bogus ref -> real `fatal: invalid object name` rc=128, stderr NOT discarded.
```

**IAM (comp-iam insufficient exactly as the TO predicted).** `comp-iam service` returned
UNRESOLVABLE-RESOURCE for both S3 ops (`Bucket=` a runtime value). Resolved the grammar from source
(`local.monolith_sources = ["trueshares","pathfinder","msn"]`; code passes `source="trueshares"`),
confirmed the grant is APPLIED live, then the live primitive:

```
  simulate-principal-policy, ONE --resource-arns per call, each a SEPARATE invocation:
    trueshares/DIVZ/bronze/holdings/20260824/divz_holdings.csv   allowed
    trueshares/IDVZ/bronze/holdings/20260824/idvz_holdings.csv   allowed
    opal-data-inf/gold/meta/pipeline-complete.json               implicitDeny   <- NEGATIVE CONTROL
```
The instrument DISCRIMINATES, and independently confirms the TF comment's claim that this role cannot
write the INF trigger key ("the fence is IAM, not intent").

**AC3 (post-apply, per member, normalized).** Re-downloaded; zip sha == live CodeSha256.

```
  lambda_function.py  51,885 B  RAW MATCH vs its HEAD blob (e6f9fe5391da)
  landing_guard.py     5,998 B  RAW MATCH vs its HEAD blob (a715b04be314)
  call site PRESENT :550 / :552, SKIP else :559.  lines 1083 -> 1126.
  *** THE NEW PACKAGE IS LF, NOT CRLF *** -- both members match RAW, so Z-S4 does not recur here.
```

**AC4 (EXERCISED, on the SCHEDULED fire).**

```
  stream 2026/08/24/[$LATEST]25ae2df9e21247ff9868c0dcf1089251
  RequestId 5ec70c09-1b87-4cb7-971c-6ae755ad2715  firstEvent 22:00:08.209Z (8s after cron)
  Duration 7800.26 ms  1024MB / 252MB max used
  LOG CARRIES THE DEPLOYED CODE'S OWN LINES (the old bytes could not emit them under any input):
    OK: [divz] trueshares holdings captured: 29 row(s)
    OK: [idvz] trueshares holdings captured: 44 row(s)
    GUARD OK bronze trueshares/DIVZ/bronze/holdings/20260824/: 1 landed == 1 enumerated
  BRONZE  DIVZ 0 -> 1  divz_holdings.csv 2,705 B  22:00:11Z  (UTC via s3api)
          IDVZ 0 -> 1  idvz_holdings.csv 4,026 B  22:00:12Z
          BOTH INSIDE the invocation window 22:00:08.209 -> 22:00:12.027Z
          sibling positive control netassets 40 -> 41 each; negative control ZZZNOFUND 0
  SILVER  2026-08-24.parquet 21,073 B 22:00:17Z
          rows 114 -> 187 | DIVZ 0 -> 29 | IDVZ 0 -> 44 | PFDE 90 -> 90 | PFOE 24 -> 24
```
Pre-fire baseline captured TWICE (me 20:55:24Z, `3.0.0_SA_CVO~Z` 21:13:47Z): NO 2026/08/24 stream
existed. **NO ad-hoc invoke was fired by anyone** -- permitted by the TO, declined deliberately,
because an ad-hoc artifact is byte-identical downstream and firing one destroys the ability to say
which run produced the evidence.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-trigger` | `comp-trigger etfs-netassets-daily` | PASS | ENABLED, `cron(0 22 * * ? *)`, target = the function, FIRED 7x. DENOMINATOR 136 events-rules + 18 schedules. Matches the TO. |
| `comp-iam` | `comp-iam service etfs-netassets-daily` | PARTIAL | Both ops `[UNRESOLVABLE-RESOURCE]`. Insufficient BY DESIGN -- models `(action)` never `(action,resource)`. Treated as a FLOOR and escalated to the live primitive, which is what the TO's `if_mismatch` prescribes. |
| `comp-find -i` | `-i "opal-assets-silver-etf-sweep-daily"`; `-i "silver-etf-sweep"`; `-i "etfs-netassets-daily" infra/aws/terraform/` | PASS | Z-S10. Repo-wide 31 hits / 27,970 files (1 UNREADABLE, declared), ZERO in any `.tf`. Positive control returned 18 hits in HEAD band incl. `name = "etfs-netassets-daily"`. Ran the broader `silver-etf-sweep` form deliberately to catch a partially-interpolated name. |
| `comp-find --name` | `--name "trading_calendar.py"` | PASS | 5 hits / 28,002 files -- found the four-home duplication that decides TO-5's packaging fork. |
| `comp-closure` | `.tools/comp-closure compile etfs-netassets-daily` | WARN | `equivalence=UNMEASURED` exactly as the TO predicted (landing_guard three homes). Post-deploy member rows flipped `eq_head` false -> TRUE with no tool change. **NOT on PATH** -- see Gap. |
| `deploy_ledger.py` | `open --window-hours 6` (7 legs); `close-leg` x7; `close`; `check` | PASS | Opened at deploy-START, not retroactively. Closed in-session, final sweep clean of my slug. |
| `proof-of-spec-check` | `<instance> ETFS...AC1..AC5` (positional, rc read unpiped) | PASS | rc=0 VALID, 5 rows, 0 violations -- after 34 -> 1 -> 0 violations by reading the schema directly. |
| live AWS primitives | `get-role-policy`; `simulate-principal-policy` (ONE arn/call, controls isolated) | PASS | The APPLIED plane comp-iam structurally cannot reach. |

**What worked.** `comp-trigger`'s printed denominator made the schedule claim checkable rather than
assertable. `comp-find`'s BAND classification separated a config/doc hit from a source hit in one call
on Z-S10 -- the whole disarm rested on there being ZERO `.tf` hits among 31.

**What failed.** `comp-iam` returned UNRESOLVABLE-RESOURCE on both operations of the function under
deploy -- correct and honest behaviour, and it means the tool contributed no coverage to the IAM
question; the live primitive did all of it. Its own header says so, which is why it is a WARN and not
a defect.

**Gap found.** `.tools/comp-closure` **is not on PATH on site Z.** The file exists (1,463 B,
executable) but `command -v comp-closure` fails while the control `comp-find` resolves -- a missing
`~/bin` forwarder. Per Rule 20's own lesson a caller guarding with `command -v` **silently skips**
rather than failing loud, so any gate reaching for it on this box does nothing and reports nothing.
Surfaced to CTO~Z/CVO~Z; remedy (`provision-path-shims.sh`) is the tooling lane's call, not mine to
run mid-cell.

---

## A defect I put in my own commit

`record-terraform-deploy.sh` died on a cp1252 `UnicodeDecodeError` (the source map carries a mojibake
`0x9d` at offset 31494). Re-run under `PYTHONUTF8=1` it committed **the right data in a wrong file**:
2,860 insertions / 2,860 deletions for a 4-field change, because the Python text-mode write flipped the
file LF -> CRLF, plus 8 lines of `ensure_ascii` churn in FIND_INSURE / news-pipeline rows.

**What caught it:** the insertion count. `2860 + 2860` is the file's line count twice over -- the
line-ending signature, not a rewrite. Same arithmetic that caught Z-S4 in the Lambda member an hour
earlier, one layer up, in my own work this time.

**The fix:** verified the churn SEMANTIC-ZERO first (200 functions, 0 changed fields after neutralising
my own 3), then **PROVED a lossless round-trip on the UNMODIFIED parent before rewriting anything**
(re-serialising at `indent=2, ensure_ascii=False, trailing newline` reproduces the parent bytes
exactly). Only then applied the 4 edits. Fix-forward `d6e5fbe667`; net diff vs the pre-deploy parent =
8 lines = exactly my 4 fields, CRLF=0, 200 functions, JSON valid.

**Routed, not absorbed:** the tool defect (fails closed on cp1252; CRLF-ifies under the UTF-8
workaround; its CHANGELOG leg dies on a JS syntax error at `rdeploy-changelog-*.js:18`) went to
`1.0.0_SA_CTO~Z` for the tooling lane. Not fixed inside this cell.

---

## Findings surfaced (all routed, none absorbed)

- **Z-S4 post-deploy criterion ANSWERED, prior FALSIFIED.** The new package is LF. The stated prior
  ("if your build runs on this Windows box it probably is CRLF") is wrong, and it was falsifiable in
  advance from source: `build-and-upload.sh:279-290` zips via `ReadAllBytes -> stream.Write`, a PURE
  BINARY COPY that cannot translate newlines. The CRLF in `541a393798` was baked at EDIT time on the
  box that built it. Predicted from source before applying, then measured. **Bound adopted from CVO~Z:
  this establishes THIS BUILD is LF and does not establish the mechanism cannot recur -- the
  normalized-per-member oracle stays.**
- **Z-S10 DISARMED** -- `opal-assets-silver-etf-sweep-daily` is UNMANAGED. Deliberately NOT rested on
  the text miss, which COO~Z and CVO~Z correctly bounded as declared-ness only (an interpolated TF name
  is invisible to any grep). The discriminator is a LIVE TAG: every TF-managed rule carries
  `ManagedBy=Terraform` (stamped by the provider's `default_tags`); this one carries `Project`+`System`
  only. **Residual named: a multi-root `terraform state` sweep is UNRUN**, and state is the only
  instrument that fully closes the interpolation hole.
- **Z-S18** -- `proof-of-spec-check` returns rc=0 VALID on a criterion that never ran. `UNCOMPUTABLE`
  is a legal status, so the gate certifies SHAPE and COVERAGE and structurally cannot certify that the
  WORK HAPPENED. CVO~Z sharpened it better than I had: the tool is **strict on a row that CLAIMS a
  pass and silent on a row that declines to** -- an incentive gradient, not just a blind spot.
  CTO~Z ruled: an `UNCOMPUTABLE` on an EXERCISED-class criterion is NOT a close.
- **Z-S16 mechanism located at source, and it is WIDER than DIVZ/IDVZ.** `:838` sets `data_as_of` from
  `net_assets_as_of`; `:902` sets `date` from that. **Both holdings date fields come from the
  NET-ASSETS page, for every fund, from one assignment** -- the issuer's own holdings date is never
  consulted. Byte-identical at `541a393798` and HEAD; @`4e5800fde0` touched it ZERO times, so it
  predates this deploy. **PFDE/PFOE were never correct, they were COINCIDENTALLY correct**, because for
  filepoint the two dates fall on the same day. TrueShares is the first source where they differ.
- **The `2026-08-23` partition already stamped PFDE/PFOE `date=2026-08-24`** -- a date ahead of its own
  partition key and write time, on the filepoint side, before this deploy existed. Reported as a
  MEASUREMENT, explicitly not a defect verdict (a forward-dated NAV effective date is a legitimate
  vendor convention and the 23rd was a non-trading day). Two partitions only; no history walk.
- **Deployment Rule 6's second half was silently dropped** -- `git push origin SITEZ` moves commits but
  not tags, so `etfs-netassets-v1.4.0` sat local-only. Reported; MSTR~Z pushed it, verified from the
  remote, AND censused every other local tag (zero other local-only tags) -- one gap, not a pattern.
- **`ETFS_POSITIONING.TO-5`'s `<status>` read ACTIVE while the hold lived in prose at `:63`**, and
  `to-check.py` parses `status` (32 refs) -- so the dashboard rendered a held TO as active. Same class
  as the defect the hold exists to prevent: a machine-readable field disagreeing with the prose beside
  it, where the machine field is what an instrument reads.

## Corrections taken against me, both accepted

- **COO~Z (RAVC 4):** my AC4 regression evidence said `PFDE 90 -> 90 / PFOE 24 -> 24 UNCHANGED`. That is
  a claim about ROW COUNTS and VALUES and I wrote it as though it covered the table. **`is_cash` changed
  bool -> object** (73 nulls from DIVZ/IDVZ promote a pure-bool column). PFDE/PFOE rows ARE affected --
  not in values, in the TYPE a consumer reads. I checked the axis I expected to break and called the
  table unchanged. Asked COO~Z to amend the RAVC record rather than let my sentence stand.
- **CTO~Z:** `platinum/etfs/positioning_data.json` is a LIVE SERVED KEY -- an ad-hoc TO-5 run overwrites
  production serving in place, and DE~Z's Z-S12 evidence rests on those bytes. I had not surfaced that.

---

## ETFS_POSITIONING.TO-5 -- state at window close

**Done:** preconditions 3/3 re-derived (corrected contract all four parts; producer source exists; **my
own ordering constraint discharged** -- DS~Z's `8bf8b39131` + `14b67e4cf3` landed, so no build over
uncommitted code). Design call **ONE Lambda both stages** -- two with an ordering edge would make stage 2
a pipeline whose only trigger is another pipeline's success, the defect this TO exists because of; DS~Z's
in-process measurement (138 MiB, no growth) backs it. **Schedule MEASURED** (the figure DS~Z explicitly
declined to guess): `OPAL_BBGTML_daily_pull` fires 07:00 local, host TZ measured UTC-4, so the bbg
landing is **11:00Z** and `cron(0 13)` sits 2h after -- **breathing to 1h in EST, since a UTC cron does
not track a LOCAL-time task.** `run_class` classifier authored and **EXERCISED 12/12 with a MUTANT
CONTROL that discriminates on 8/12** (I ran the negative form CTO~Z ruled against, because without it
12/12 would have been true and worthless).

**Blocked on others (both routed with full specs, neither assumed):**
1. `0.4.0_DS_ClientPlatform~Z` -- `lambda_handler` + `run_class` in the producer (their Rule-13 lane; the
   estate pattern puts the handler INSIDE the data/ script, `crawl_web_bronze.py:516`). ACKed at 22:34Z.
2. `1.0.0_SA_CTO~Z` -- the packaging fork. `build-and-upload` requires files under one `source_dir`
   (0 of 200 Lambdas use `../`), and `trading_calendar.py` already has **FOUR byte-identical homes**.
   **The premise that decides it is MINE and has EXPIRED:** I argued against a layer because "a layer is
   needed only if the module must be SHARED ACROSS FUNCTIONS -- which was never this contract's reason."
   Correct then, against one function. It is now four, and TO-5 makes five.

---

## Blockers

**None at this seat.** TO-1 is closed. TO-5's two open items are with named seats, both routed with
executable specs, and neither is waiting on me. **ETFS_POSITIONING.TO-5 remains HELD-then-LIFTED with
nothing staged**, so no half-landed state exists anywhere.

---

## Current State (written for zero prior context)

- **`etfs-netassets-daily`** (us-east-1, acct 313476888478) runs `CodeSha256
  BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=`, LastModified 2026-08-24T20:31:09Z, python3.11,
  1024 MB / 300 s, env `TS_HOLDINGS_ENABLED=1 BRONZE_BUCKET=opal-data-assets BRONZE_GRAMMAR=monolith
  ETFS_BUCKET=opal-data-etfs SILVER_ROOT=""`. Trigger `cron(0 22 * * ? *)`, ENABLED.
- **Terraform root** `infra/aws/terraform/etfs-netassets/` (backend key `etfs-netassets/tfstate`) is at
  **0-diff**. Module `../modules/yang-lambda`; layer
  `arn:aws:lambda:us-east-1:313476888478:layer:pandas-pyarrow-requests-layer:1`.
- **Source map** `infra/aws/lambda/ci/lambda-source-map.json` row `etfs-netassets-daily`:
  `artifact_sha256 = BEITykjh...`, `last_deployed_commit = 4e5800fde082...`,
  `last_deployed_at = 2026-08-24T20:35:52Z`. All three current.
- **Artifacts now landing daily:** `s3://opal-data-assets/trueshares/{DIVZ,IDVZ}/bronze/holdings/{d8}/`
  and `s3://opal-data-etfs/silver/holdings/{date}.parquet` (187 rows, four funds).
- **Deploy ledger** `org/critical_paths/change_management/20260824T2025Z_etfs-ingest-to1-...md` CLOSED,
  7/7 legs. **Proof-of-spec** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/
  ETFS_INGEST.TO-1_PROOF_OF_SPEC.json` VALID, 5/5 PASS.
- **NOT built:** there is no `infra/aws/terraform/etfs-positioning*` root. `etf-positioning-producer`
  does not exist on the applied plane and is absent from the source map. **Gold has never run; platinum
  is unmoved** (`platinum/etfs/positioning_data.json` 76,149 B @ 2026-08-24T12:30:47Z).

---

## Next Steps

- [`0.4.0_DS_ClientPlatform~Z`] Land `lambda_handler` + `run_class` in the producer per spec (msg 5430;
  classifier verbatim, comment included, both stages' manifests). ACKed 22:34Z.
- [`1.0.0_SA_CTO~Z`] Rule the TO-5 packaging fork (msg 5448). My rec is (C): take option (A) to ship
  TO-5, and file the shared-layer question as its own item with its own owner rather than deciding it
  inside an apply.
- [`0.7.0_AE_CloudOps~Z`] On both answers: write the TF root (IAM per the corrected contract, `yang-lambda`
  512 MB / 120 s, `cron(0 13 * * ? *)`, **NO gold env vars**), source-map row, build, `safe-apply`,
  verify DESIRED/APPLIED/CODE + INV-4 (**env block READ and NON-EMPTY via a key known set, AND neither
  gold key present** -- a bare absence assertion passes on a broken query, which I hit at 20:1xZ),
  notify DE~Z, ad-hoc exercise (adhoc-direction ONLY), close the ledger.
- [`0.7.0_AE_CloudOps~Z`] **AC7 tomorrow ~13:00Z** -- observe the FIRST SCHEDULED fire at its own
  invocation record; artifact must carry `run_class: scheduled`. A follow-on OBSERVATION obligation on a
  completed deploy, **not** a stranded ledger leg (CTO~Z 5393).
- [`3.0.0_SA_CVO~Z`] `trading_calendar.py`'s four byte-identical homes may want their own coordinate
  regardless of the fork's outcome -- the copies exist whatever TO-5 does, on the module NEVER#1 calls
  "the ONE frontier definition".
