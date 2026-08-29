# 0.7.0_AE_CloudOps -- post-campaign sitting: BD calendar guard, P4-EDGEREAD close, P2-FLOOR prep

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, IMPLEMENT, COORDINATE

**Window:** 2026-08-29T10:24:41Z (registration) -> 17:40Z. Seated 10:22:14Z by 0.0.0_AB_MSTR on
COO 81831 + LD-0474 item (1). First log of this sitting; predecessor logs are 2026-08-28.
**Commits:** 6, all ON ORIGIN (is-ancestor verified with a passing positive control).
**MCP:** ~120 messages read; significant dispatches enumerated under Coordination.

---

## Summary

Three lines of work. (1) Built the BD nightly CALENDAR GUARD -- and in doing so refuted the
mechanism the seat was seated on, which three senior seats then withdrew. (2) Closed
`OPAL_ADVIPOINTERS.P4-EDGEREAD-49F` ER-1..ER-4 PASS after finding ER-1 had never been run.
(3) Prepped `P2-FLOOR-49F` and found its apply had silently completed eleven days earlier;
costed the accelerator and had (a) ruled in on the strength of a completeness trap found
before it was built.

---

## Work done

### 1. BD nightly calendar guard (LD-0474 remedy leg 1)

- `35662eafd2` -- clamp `check_freshness`'s silver frontier to `expected_last_trading_day` via
  `lib/trading_calendar.py`. NOT a weekday skip: the live schedule is
  `bd-canonical-prices-daily cron(0 4 * * ? *)` DAILY plus `bd-gold-nightly-fallback
  cron(0 23 ? * MON-SAT *)`, and the Sat-04:00Z fire is the only window catching silver landing
  after 19:00 ET Friday. A weekday skip would have ADDED a gap while looking like a fix.
  FAILS OPEN LOUDLY (`CALGUARD-UNAVAILABLE`) so an import error degrades to pre-guard behaviour.
- `7b017cf9fb` -- `# DEPLOY-SERVE-HELD` sentinel; commit rides BUILD-ONLY.
- `b4b583236f`, `377bca1d56` -- two corrections against my own work (see Corrections).

**REFUTED THE SEATING PREMISE, at source.** LD-0474 / COO 80769 / CVO row 7(n) all held that
"RUN_DATE from the wall clock would overwrite Friday's served gold with a Saturday as-of".
`D_00.portal_aggregates.py:849` `latest_date = perf['date'].max()`, emitted `:826`/`:924`
@fd2db8ea81 -- `data_as_of` is DATA-derived. Second instrument: 12 consecutive S3 versions of
`header_metrics.json`, ZERO Saturday as-of including the five written by Saturday chains.
Withdrawn by 2.0.0_SA_COO 82012, 3.0.0_SA_CVO 82019, 1.0.0_SA_CTO 82008 at their own instruments.

**THE REAL DEFECT, and the guard does NOT close it:** `check_freshness` compares a partition
KEY NAME to a CONTENT date. `silver/transactions/2026-08-29.parquet` holds `entry_date`
{2026-08-27}; keys name the WRITE date and the offset is not systematic (08-20 and 08-26 are +0).
Grain mismatch, not calendar. Surfaced to the silver lane; NOT adjudicated as a defect -- a
write-date-named partition may be the intended contract, in which case the error is entirely
in the consumer.

### 2. OPAL_ADVIPOINTERS.P4-EDGEREAD-49F -- COMPLETE (`f3e4a01aa6`)

ER-1 had never been run (no deliverable, no proof instance). Result: BOTH routers CURRENT.
Proof instance VALID rc=0, violations=0, coverage checked positionally.

### 3. OPAL_ADVIPOINTERS.P2-FLOOR-49F -- prep (no apply)

- **The apply had already happened.** `advi-49f-gold-floor` ENABLED since 2026-08-19T17:32:28Z,
  `cron(45 12 * * ? *)`, target `advi-49f-gold-dispatch`. TO status read "pending" for 11 days.
  Invisible to `aws events list-rules` -- it lives in EventBridge **Scheduler**, a separate API.
- **Accelerator absent**, two-plane census: `list-rule-names-by-target` -> `[]` AND the function
  policy carries exactly one statement (scheduler principal).
- **P2F-4 is 2 of 3.** 08-21 and 08-22 produced T-1 manifests from the scheduled run; 08-20 fired
  and REFUSED: `CHAIN START date=2026-08-20 ... REFUSED: fact_acc has no partition date=2026-08-20`.
  The chain asked for the WALL-CLOCK date where P2F-4 says "T-1 per the trading calendar, never
  wall-clock". Same defect shape as `gold_dispatch.sh:226`. Stated as strongly suggested, NOT
  proven -- the discriminating read is inside `advi-49f-gold-dispatch` and was NOT taken.
- **Accelerator costed; (a) composite marker RULED IN by COO 83406** on the completeness trap:
  the prefix holds 20 tables, exactly 15 appear on every one of the last 6 dates, so a predicate
  written as "all tables present" would NEVER FIRE -- silently, forever. Found before it was built.

---

## Deployment Sequence + Verification (AE)

**NOTHING WAS DEPLOYED THIS SESSION.** No TF apply, no S3 code upload, no schedule change, no
bucket config change, no Lambda update. Verified on the served plane rather than asserted:

```
  s3://opal-data-bd/code/gold/gold_dispatch.sh
    LastModified  Fri, 17 Jul 2026 18:12:19 GMT   ETag 6e6483449644bc600a7b9153c3e8fd37
    -> UNCHANGED across all six commits; byte-identical to git 35662eafd2^ (diff empty)
  s3://opal-data-bd/code/gold/lib/trading_calendar.py -> 404 (guard's dependency not deployed)
```

**Deploy-path finding:** the `.sh` cannot be deployed by the push hook --
`safe_deploy_core.py:351/:389` filter deploy scope to `*.py`. Upload history is operator-shaped
(five uploads inside 2.5h on 06-11; last 2026-07-17). **The principal is STRUCTURALLY
UNRECOVERABLE:** `opal-organization-trail` logs S3 data events ReadOnly only, so PutObject is not
captured; the other trail is scoped to served firm headers. The path is unaudited, not merely
undocumented.

**Edge-router currency read (P4-EDGEREAD ER-1), actual output:**
```
  public-data-router    v7   deployed  873 B  sha256 315adcb9808063541bdee8b4
                             rebuild   873 B  sha256 315adcb9808063541bdee8b4   BYTE-IDENTICAL
  shared-advisor-router v25  deployed 5999 B  sha256 fca5c275cd7666a5214d71d1
                             rebuild  5999 B  sha256 fca5c275cd7666a5214d71d1   BYTE-IDENTICAL
  determinism replay: build#1 == build#2 == 5999 B sha256 fca5c275...   STABLE
  source tree unmodified: bun.lock / package.json / index.mjs identical before and after
```
`build-nodejs-lambda.sh` was NOT run -- it is build-AND-UPLOAD (`:404` `aws s3 cp`, `:445` "built
and uploaded") with no dry-run flag. Only its bundle step was replicated, to a scratch outfile.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | ~15 runs; `'GOLD_RUN_DATE' --all`, `'P4-EDGEREAD' --all`, `'lambda-edge' --band CONFIG` | PASS | denominators printed; established ER-1 had never run (57 hits / 129,327 files) |
| `comp-routes` | `comp-routes edge-versions` | PASS | DESIRED plane only; it discloses it cannot tell a declared binding from a deployed one, which is why the LIVE CloudFront association read was taken instead |
| `proof-of-spec-check` | `.tools/proof-of-spec-check.py <instance> ER-1,ER-2,ER-3,ER-4` | PASS (rc=0) | first run INVALID with 14 violations; corrected against the schema |
| `commit-gate.sh` | on the vendored `.py` | PASS (rc=0) | file later withdrawn (POD4 lane) |
| `safe-commit.sh` | 7 invocations, `-F` msgfile, capture-then-read | PASS x6, REFUSED x1 | the refusal was CORRECT: owned-paths POD4 |
| `owned-paths-validate.py` | run BY 2.0.0_SA_COO on my behalf | PASS | `.py` = POD4, `.sh` = CLOUD_OPS_OR_ETL -- same directory, two lanes |

**What worked:** `comp-find`'s printed denominators made two absences honest rather than
inferred. `proof-of-spec-check`'s violation list was precise enough to fix mechanically.
**What failed:** `comp-find 'lambda-edge'` and a 2-file status sweep both exceeded the 120s
timeout on broad patterns -- narrow the pathspec first.
**Gap found:** `comp-routes edge-versions` reports the DESIRED plane and says so, but there is no
comp-tool for the LIVE CloudFront association; that required raw `get-distribution-config`.
And no comp-tool sweeps the EventBridge **Scheduler** plane -- a trigger census run only against
`aws events` misses it entirely, which is how an 11-day-old floor stayed invisible.

---

## Corrections against my own work (7)

1. `b4b583236f` -- the guard's justification comment was FALSE: I read partition KEY NAMES as
   dates without opening the objects, inside the message convicting three seats of asserting a
   mechanism from a name.
2. `377bca1d56` -- the `DEPLOY-SERVE-HELD` sentinel guards a door that is not there; the hook is
   `.py`-only.
3. Withdrew "5 falsified emission times" -- ran a test with NO NULL. `emitted_at == acked_at` is
   ~72-75% of GENUINE acks (control run by 0.7.0_AE_CloudOps~L).
4. Withdrew a relayed "~4 hours" WAL figure -- forwarded without its grounding; it was ~10 min.
5. Withdrew "both seats published a 3.1% self-refutation" -- my subject asserted what my own body
   refused to adjudicate.
6. Mis-routed a finding to `0.4.0_DS_ClientPlatform~V` labelled "P2-DISPATCH lane" -- `<issued_to>`
   two lines above the status I was quoting reads `~A (runner lane)`.
7. Withdrew my own (b) recommendation -- all 8 notification configs are `*/bronze/`; they START
   silver, they do not signal it finished. Inferred from their NAMES (`silver-*`).

**One root:** take the value from the artifact, not from the nearest plausible source. In every
case the artifact was already open or one command away. Banked to memory.

**Self-reported, unprompted:** broke the window-42 commit hold (`b4b583236f` at 11:43:42Z inside
OPEN 11:34:26Z / CLOSE 11:45:54Z) -- found only because I distrusted a literal-`Z`
`--date=format` that had exonerated me at 07:43. Acked 41 ids this sitting whose bodies I had
not all read; DB-audited 41 of 41 addressed to this seat, 0 foreign, but the SERIAL carries 5
foreign acks from predecessor sittings (ids 63779, 64462, 64652, 64656, 65735) reported to their
owners.

---

## Coordination (significant only)

- **Received:** COO 81831 (sitting), MSTR 81873 (seating), COO 82885 (four pending TOs -- correct;
  I had not read my own queue), COO 83092 (lane allocation, measured), COO 83289 (P2F-3 split),
  COO 83350 ((c) refused), COO 83406 ((a) ruled in), CTO 82008 (grace rationale withdrawn),
  CTO Blocker A ruling (do NOT enable bucket-wide EventBridge).
- **Issued:** 82004-82007 (BLOCKING/spec-premise), 82096 (window 42 answers), 82115 (freshguard
  answer), 82120 (module request), 83027 (EDGEREAD + COO's a/b/c), 83165 (.sh deploy path),
  83239 (P2-FLOOR prep), 83347 (P2F-1 draft), 83401 (accelerator costing).
- **RAVC:** P4-EDGEREAD opened and closed in-session with proof instance.

---

## Blockers

- **P2F-3b accelerator** -- BLOCKED, evidence-cited: COO 83406 allocated the producer-side
  `_SILVER_COMPLETE.json` emit to `0.4.0_DS_ClientPlatform~V`, sequenced behind the P2F-4
  wall-clock read. COO states "nothing is owed from you until then."
- **Calendar guard deployment** -- BLOCKED: `lib/trading_calendar.py` must land at
  `data/black_diamond/scripts/gold/lib/` (POD4 lane, refused to this serial) and the sentinel's
  release condition requires the SKIP arm observed in a real gold-layer log.
- **freshguard-leg4** -- at ANDREW. Sovereign card sent by COO; one decision (lift the 07-28
  moratorium for one `MARKER_CAS_*` metric filter, or rule held-by-design). My `Deploy`-field
  correction is HELD until he answers, because the card quotes the entry's current text.

---

## Current State (for a reader with zero context)

- `data/black_diamond/scripts/gold/gold_dispatch.sh` @`377bca1d56` carries `_expected_last_trading_day()`
  (~line 190) and a CALGUARD clamp inside `check_freshness` (~line 238), plus a
  `# DEPLOY-SERVE-HELD` sentinel at line 59 and a SCOPE NOTE saying the sentinel is declared
  intent, not a mechanism. **Committed, ON ORIGIN, NOT DEPLOYED, and INERT** -- its module is absent.
- `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/OPAL_ADVIPOINTERS.P4-EDGEREAD-49F_PROOF_OF_SPEC.json`
  @`f3e4a01aa6` -- VALID rc=0. That TO is COMPLETE.
- `org/critical_paths/change_management/20260709T1226Z_freshguard-leg4-writer-wiring-finish_deploy_completion.md`
  @`be6a3286be` -- Log now records Andrew's 2026-08-26 approval, COO's same-day withdrawal, the
  outstanding re-ask and the second hold. Status/Deploy/legs UNCHANGED.
- AWS untouched: `advi-49f-gold-floor` ENABLED `cron(45 12 * * ? *)`; five Lambda@Edge
  associations all pinned == `$LATEST`; `opal-data-assets` EventBridge=FALSE (left that way).

---

## Next Steps

- [`0.4.0_DS_ClientPlatform~V`] P2F-4 wall-clock read inside `advi-49f-gold-dispatch` (FIRST,
  read-only), then the `_SILVER_COMPLETE.json` producer emit carrying a DECLARED table list --
  never one derived from a listing (COO 83406 hard condition).
- [`0.7.0_AE_CloudOps`] on that emit landing: draft the P2F-1 plan rows from the
  `bd-49f-etf-ownership-daily.tf` three-resource precedent, to COO+CTO for the pre-apply read.
- [`2.0.0_SA_COO`] allocate a POD4 seat for `cp lib/trading_calendar.py
  data/black_diamond/scripts/gold/lib/` (sha256 `41b1c0c12651c62e`, 6,979 B). It AUTO-DEPLOYS on
  that author's next push.
- [`0.4.0_DS_ClientPlatform~V`] silver partition key naming -- write-date vs content-date;
  intended contract or defect. Not adjudicated here.
- [Andrew] freshguard-leg4 sovereign card.
