# Session 1257-1430Z — MDPF_TRGALN cycle day: 3/3 labels at 08-13; INF intervention closed at the authorized boundary; full evidence set filed

**archetype:** MIXED (DIAGNOSE / VALIDATE / SCRIBE)

## Headline
Today's untouched scheduled cycle served ALL THREE firms labeled as-of 2026-08-13 (publish
13:50:46-50Z, roster-complete). COT + 49F are value-clean. INF's 08-13 point carries a disclosed
$185,201.05 / 0.088% understatement (my tonight-refresh QA pull's date-key collision, remedied to
the authorized boundary and closed PASS_WITH_DISCLOSURE per PRD v1.4 §9.5; tomorrow's clean cycle
is the named closing read whose failure REOPENS).

## The arc (full narrative + timeline: deliverables/MDPF_TRGALN/INF_INTERVENTION_RECORD_20260814.md)
COO wake 12:57Z (sentinel watch) → mechanism found in the producer's log (RESUME skip on my QA
date key) → COO GO (A) backup-first delete+re-pull → deletes+re-pulls completed pre-STOP → MSTR
HOLD (S3-delete Andrew-reserved) → freeze + hash-verified recoverability → four instrument swings,
each reported the turn it was measured (producer log → editedDate [RETRACTED: position-edit stamp,
not a valuation clock] → matched-row value-diff [24,976/35,285 prices moved 02:12→09:09 ET] →
mirror/converter source mechanics) → cleared remedy (runner→mirror) healed the RAW layers →
blocked at the silver converter's partition_exists idempotency with no deployed force path → COO
stand-down of the pointless trio legs → CTO ruling: PASS_WITH_DISCLOSURE with the reopen condition.

## Evidence set filed (this commit)
- proof_TO-0.json FINAL rev 2: Part B appended — B1 CONFIRMED PASS (07:30 ET window works;
  vendor-attested T-1 all 5 tables); B2 = values present by 09:09 ET, slot adjudication rides
  tomorrow; fork table: outcome (a), no fork fired.
- proof_TO-1.json rev 2: verdict PASS (session 11:31:44Z all-tables T-1; fact_holdings 11:46:04Z
  <= 12:50Z spec; served cottonwood 08-13; 13:00Z sweep fired; double-run held as pre-registered).
- proof_TO-2.json rev 2: verdict PASS — TriggeredRules prove all 9 retimed rules fired exactly
  once at their new slots (09:50Z…13:05Z); vintage disclosure pointered, separate axis.
- proof_TO-3.json rev 2: verdict PASS (trio ordering held; publish 13:50:46-50Z, 4 scopes, 1 pass).
- proof_TO-4.json rev 1: labels claim + COT/49F/INF value legs; INF = PASS_WITH_DISCLOSURE with
  both CTO conditions verbatim (delta+instrument+named closing read; failure REOPENS).
- INF_INTERVENTION_RECORD end-state §5.

## Banked (CTO carries, one class, three sightings)
Resume/idempotency force-path gaps: assets-pull --no-resume unreachable from its handler; silver
converter force unreachable from lambda_entry; plus the two-producer raw/parquet asymmetry on
bronze/assets. Class lesson: a pre-roll QA pull that claims a production date key collides with
every resume layer downstream; §8.1-style exercises need key hygiene.

## Blockers
NONE for me. Andrew holds: the (A)-delete adjudication (crossed by COO's GO pre-hold, on their
record) + the staged one-word INF completion (delete stale fact_assets date=2026-08-14 partition →
converter re-fires on healed raw → trio → tie-out).

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-find | eclipse_qa; build_dim/... (earlier session) | this window: source reads targeted by prior findings |
| live primitives | filter-log-events (assets 11:17Z run, converter aa57254f, sweep 03d70fa8), get-metric-statistics TriggeredRules x9, s3 head/list/cp, lambda invoke (cleared remedy), ssm reads | every claim in the proofs carries its own read |
| python value-diff | matched-row (accountNumber+ticker) across three pull vintages | THE decisive instrument of the day; replaced two wrong metadata proxies |
| (comp-trigger) | not re-run | no schedule changed this window; TriggeredRules is the exercised instrument |

What worked: reporting each instrument swing the turn it was measured; grounding one layer deeper
before every fire (the no-op mirror and the no-op trio were both caught pre-fire). What failed:
two metadata proxies (LastModified/rowcount, editedDate) briefly carried claims — both retracted
within minutes by the content diff; the class is now named in the record. Gap: the force-path
class (filed).
