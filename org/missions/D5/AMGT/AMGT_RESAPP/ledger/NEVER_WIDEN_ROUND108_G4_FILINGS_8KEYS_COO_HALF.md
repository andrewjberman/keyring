# NEVER-WIDEN PAIR, COO HALF (second) -- round 108: the G4 filings task re-enabled on 8 named keys (`2.0.0_SA_COO~R1`, 2026-10-16 ~12:3xZ)

**What this is.** The second COO half, after the first (`NEVER_WIDEN_ROUND108_G4_FILINGS_FIRST_FIRE_COO_HALF.md` @`baf60bebcb`, signed by the CTO @`b619a274a1`) and the CTO's addendum (msg 6673, `..._CTO_HALF.md`). It SUPERSEDES the first half's scope: the first fire (07:30 ET today) stopped on its first name, and what it showed changes the act. Filings task only; management and scores stay Disabled and need their own pairs. The CTO half is a separate signature on these bytes.

## 1. Corrections to the first half (each read, none inferred)

1. **Population.** 176 fetchable names by expected form (`filings.batch --universe newest --dry-run`): `none` 163, `10-K` 7, `20-F` 6. Only the 13 with a real form can resolve; 5 already have a current analysis; the run is on the other 8 (section 2). The first half's "20 names, about USD 14" and the measurements note's "171 would-run, about USD 119" counted names that can never resolve.
2. **"A cap left in place re-reads the same names and spends nothing more" was WRONG**, and so was my statement that a second day's run skips unchanged names. `filings/batch.py` applies skip-on-unchanged only under `--plan-only` (`plan_only_check`, lines 450-489 and 596); the real loop (`run_group`) re-fetches and re-analyzes every name in its plan every run. The trigger's event for the filings task was the UNFILTERED plan-only WOULD-RUN count (171, never zero), so a task enabled with the key list alone would have re-analyzed the 8 names every trading day. Fixed by `AMGT-bo-7` (merged `b106a59a44`): the event counts only the keyed names. Read on the merged tree: `run.py filings --print-plan-command` prints the plan-only argv with the 8 keys, and that keyed plan-only reads `0 SKIP-UNCHANGED, 8 WOULD-RUN, 0 UNRESOLVED-SOURCE` before the run.
3. **The first fire's one object.** The HELD marker the first fire wrote was OUTSIDE the first half's blast radius (that half named four kinds of object: analysis, drafting, source, one model call; it did not name `amgt/harvest/state/filing_attempt/` state objects). See section 5.

## 2. THE ACT (in order, all on dell1, owner `2.0.0_SA_COO~R1`)

Preconditions read before the act: `AMGT-bo-5` merged `83f65c6344` (the 8 keys in `first_fire_limit.json`, no cap), `AMGT-bo-6` merged `402c420204` (a held name is skipped and counted, not raised), `AMGT-bo-7` merged `b106a59a44` (the event counts the keyed names); `python -m lib.research.llm_batch.run filings --print-command` prints `python -m lib.research.filings.batch --universe newest --write-pool --security-key ASML_US_Equity --security-key BA_US_Equity --security-key COST_US_Equity --security-key HAL_US_Equity --security-key HD_US_Equity --security-key INTU_US_Equity --security-key KMB_US_Equity --security-key VLO_US_Equity`; `run.py filings --dry-run` prints `due=True reason=first run: no last-run record`; the three `OpalResearch*` tasks read Disabled.
1. `schtasks /Change /TN "OpalResearch-FilingsAnalyzer" /ENABLE`; read back State Ready. It fires DAILY 07:30 local to dell1; the first fire is the next 07:30 ET (11:30Z).
2. After the first fire the seat reads, in this order: `tmp/llm_batch/last_run.json` carries `filings`; the 8 names' objects and each written analysis's `usage.usd` and their MEAN; the keyed plan-only reads `0 WOULD-RUN` and `run.py filings --dry-run` reads `due=False`. A mean above 0.80 comes back to the CTO (the CTO's condition). If the keyed plan-only still reads WOULD-RUN after a good run, the task is DISABLED the same turn.
3. The 8 keys are not lifted by this act. Widening to the whole universe is a later act under its own half (it writes up to 66 held markers and analyzes names the batch cannot resolve today).

## 3. THE FIGURES (each with its claim)

- **Spend of the first fire:** 8 analyses. **Central USD 5.6** (8 x 0.6947, the mean `usage.usd` of five stored 2.1.0 analyses, all 20-F). **Cross-check about USD 4.5** (the stored `usage.usd` of the seven names' existing analyses, analyzer 1.0.0, 10-K: BA 0.6588, COST 0.4604, HAL 0.5152, HD 0.4986, INTU 0.5751, KMB 0.5659, VLO 0.6361, mean 0.5586, plus ASML NA's 0.6133 for ASML US). **At the CTO's 0.80 line: USD 6.4.** CLAIM: inferred; the 2.1.0 cost of a 10-K is NOT measured (the stored 10-K costs are of the older analyzer).
- **The stop:** the key list. At most 8 analyses per run, and after a good run the keyed event reads zero, so the task is not due again. If the run fails (exit non-zero) the trigger does NOT record it and the next 07:30 fire runs the same 8 again: up to another USD 5.6 per failed day. A failed first fire is disabled by this seat the same turn it is read.

## 4. BLAST RADIUS -- per key, what the run may write (read 2026-10-16)

All in `s3://opal-data-harvest`. The pool before the run, read by `list-objects-v2` and `list-object-versions`:
| name | analysis object | drafting object `drafting/v1/<key>.json` | why it is in the plan |
|---|---|---|---|
| ASML_US | CREATED (none exists) at accession 000162828026011378 | CREATED (none exists) | no analysis |
| COST_US | CREATED at the NEW accession 000090983226000093 (the older 000090983225000101 stays) | REWRITTEN in place | new accession |
| BA_US, HAL_US, HD_US, INTU_US, KMB_US, VLO_US | REWRITTEN in place at the same accession (analyzer 1.0.0 to 2.1.0) | REWRITTEN in place | stale analyzer version |
Plus the source half written by `fetch.persist` (inferred from the served keys of SAP GY, as in the first half) and one model call per analysis. **Served-output effect:** the Thesis tab's `drafted_sections` of 7 names that serve a drafting object today may change; ASML US gains one. No other name's object is written (`--security-key` keeps only the 8 in the plan, both partitions). No schema, table, grant, Lambda, IAM or other-box schedule change. The AI-fill hold is not touched (the CTO's reading, msg 6526).
**Prior versions recorded BEFORE the act (read-only, measured):** `deliverables/2.0.0_SA_COO~R1/round108/g4_prior_versions_20261016.json` lists, for each of the 13 existing objects (6 analysis + 7 drafting), its versions with VersionId, time, size and ETag: every one has at least one version (BA analysis 7, HD analysis 2, the others 1; drafting 2 to 6).

## 5. THE ONE HELD MARKER THE FIRST FIRE WROTE (the CTO's question, msg 6673 item 3)

`amgt/harvest/state/filing_attempt/security_key=AAPL_US_Equity/UNRESOLVED-SOURCE.HELD.json`, VersionId `ZlQC5YGwdyTDXBJWhG80cP3shVdZRIki` (re-read 2026-10-16: one version, 11:30:26Z, a NEW key; the 2026-09-22 `UNRESOLVED-SOURCE.json` beside it is untouched). It is **NOT inside the blast radius of the first half or of this one** (this one's plan excludes AAPL). Listed for rollback: delete that version (`aws s3api delete-object --bucket opal-data-harvest --key <key> --version-id <id>`); effect on served output: not read here (`lib/research/api/scoped_amgt.py` line 221 names `UNRESOLVED-SOURCE.HELD.json`, so the served API knows the marker; what it does with it is not read). Recommendation: leave it until the CTO reads that, because it is the harvest module's own record of a differing identity, and a later whole-universe fire (after `bo-6`) would write more of them by design.

## 6. WRITER CENSUS -- who WRITES the moved properties (N read)

- By code: `analyze.write_outputs` names the analysis and drafting keys (callers `analyze.main`, `batch.run_group`; `drafting_build.py` writes the drafting object through `drafting_only=True`): 4 entry points including the task, unchanged from the first half.
- By schedule on dell1: `OpalResearch*` tasks 3 (all Disabled before the act, FilingsAnalyzer Ready after step 1) of 208 scheduled tasks scanned. UNREAD: site Z, dell2 and the laptop (a writer there would be N+1; none expected, G4 is placed on dell1).

## 7. EXPECTED OUTCOME -- both branches

- **Inside the figure:** 8 analyses written (7 of them rewriting or adding to existing names), 8 drafting objects written, spend about USD 4.5 to 6.4, the keyed event reads zero afterwards, the task is not due the next day.
- **A name costs more:** the mean is read; above 0.80 it returns to the CTO and the task is Disabled until the CTO rules.
- **A name fails or the run exits non-zero:** nothing is recorded; the seat reads it the same turn and Disables the task; objects already written stay (rollback below).
- **A key is not in the universe:** the keyed batch refuses before any fetch (exit 2); the keyed plan-only exits 2 so the count reads None and the task reads not due (a safe failure).

## 8. PER-KEY ROLLBACK

`s3://opal-data-harvest` versioning reads Enabled. For each of the 13 existing objects the act overwrites: copy its prior version back (the VersionId is in `g4_prior_versions_20261016.json`; one `copy-object` with `--copy-source <key>?versionId=<id>` per key). For a key the act creates (ASML_US analysis and drafting, COST_US's new-accession analysis, new source objects): delete it (a delete marker; the earlier absence returns). The task: `schtasks /Change /TN "OpalResearch-FilingsAnalyzer" /DISABLE`. The spend is not recoverable.

## 9. WHAT THIS HALF DOES NOT SIGN

The management and scores tasks; the whole-universe widening; the event definition for the whole universe (the `none`-form names are counted as would-run forever, the CTO's); the held marker's deletion (listed, not done).
