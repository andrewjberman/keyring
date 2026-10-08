# TO NFRA_TRNSPT.TO-TR-a11 -- the securities allowlist, honored by the research fold, with the planted-token gate

<to_id>NFRA_TRNSPT.TO-TR-a11</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-a-11` (`decompositions/NFRA_TRNSPT_DECOMP_R11.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-a-11` (CTO round-10 analysis @8ce4b5098e, E1; ruling msg 1608): "a versioned allowlist built from the served security master, with its
source and row count printed; the planted-token test: a planted person name, client name and account number are wiped, and a planted
allowlisted issuer survives." Why: the mail wipe applied to Research transcripts removed most company names (row NFRA_TRNSPT-D2-S5:
Microsoft 67 raw utterances -> 0 stored).

**Inputs (read-only):**
- `data/transcripts/scripts/teams/securities_source_20261008.json` -- the issuer's snapshot of the served security master (DynamoDB
  `etf-classifications`): `_provenance` (source, read time, `table_rows` 11,172, `rows` 5,207), `version`, `securities`: `[{"ticker",
  "name"}]` (equities with a name), e.g. `{"ticker": "MSFT", "name": "Microsoft Corp"}`.
- `data/transcripts/scripts/outlook/wipe.py` -- `load_assets()` (:147) returns `Assets(..., allow=set(tokens), ...)`; the wipe checks the
  allowlist FIRST per token (rule 4, :9), except where a name context makes an allowlisted dictionary word a name (:211). Do NOT edit it.
- `data/transcripts/scripts/teams/research_fold.py` -- `build(paths)` runs `wipe.wipe_blocks(blocks, assets)` per utterance with
  `assets = wipe.load_assets()`.
- `data/transcripts/scripts/tests/test_wipe_planted.py` -- how the existing planted-token tests plant a person name, a client (firm) name and
  an account number, and assert them wiped.

**Build:**
1. `data/transcripts/scripts/teams/securities_allowlist.py`: `build_allowlist(source_path) -> dict` and a `main` that writes
   `data/transcripts/scripts/teams/securities_allowlist.json`: `{"_provenance": {"source_file": "<the source path>", "source_rows": <n>,
   "built_by": "...", "rule": "<one line>"}, "version": 1, "tokens": [...]}`. Tokens = every ticker, plus each name's DISTINCTIVE first word
   after stripping legal suffixes and punctuation (Corp, Corporation, Inc, Incorporated, Co, Company, Ltd, Limited, Plc, Holdings, Group, SA,
   NV, AG, Class/Cl A/B ...), e.g. "Microsoft Corp" -> "Microsoft", "NVIDIA Corp" -> "NVIDIA", "ExxonMobil Holdings Corp" -> "ExxonMobil".
   Keep the original case of the token in the file; matching in the wipe is the wipe's own. Print `source_rows` and the token count.
   Commit the generated JSON.
2. `research_fold.py`: load the allowlist and widen the assets once per `build`: `assets = wipe.load_assets();
   assets = assets._replace(allow=assets.allow | <tokens>)` (or the equivalent for the Assets type), so an allowlisted issuer survives in the
   research text. Everything else in the fold is unchanged.
3. `data/transcripts/scripts/tests/test_securities_allowlist.py`, at least: `test_gate_person_client_account_wiped_issuer_survives` -- one
   SYNTHETIC utterance planting a person name (from the wipe's given-name/surname dictionaries, NOT an issuer), a client firm name (as
   `test_wipe_planted.py` plants one), an account number, and "Microsoft"; after the research fold's wipe, the first three are gone and
   "Microsoft" is present; plus a test that the allowlist builder strips suffixes ("Apple Inc" -> "Apple") and includes tickers.

### ACCEPTANCE

<criterion id="TR11-a11-AC1" cell_refs="TR-a-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R11_CHECKS/r11_checks.py a11-list</invocation><expect>R11-A11-LIST-OK</expect></criterion>
`TR11-a11-AC1` -- the versioned allowlist names its source and rows and carries the four companies' names and tickers.

<criterion id="TR11-a11-AC2" cell_refs="TR-a-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R11_CHECKS/r11_checks.py a11-gate</invocation><expect>R11-A11-GATE-OK</expect></criterion>
`TR11-a11-AC2` -- the planted person, client and account are wiped; the allowlisted issuer survives.

<expected_criteria>TR11-a11-AC1, TR11-a11-AC2</expected_criteria>

Dry-run at the base (box/dell2 1c4acb766b): AC1 `FAIL absent`, AC2 `FAIL absent` -- FAIL as expected. Keep `test_research_fold.py`, `test_research_store.py`,
`test_research_read.py` and `test_wipe_planted.py` green. The re-fold, re-write and read-back are the issuer's TR-b-11.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. `outlook/wipe.py` and the source snapshot are READ only.
- **LOCAL.** No AWS, gateway or HTTP call. Synthetic test text only; never print or store real transcript text. Do not edit another
  order's proof instance.
- **Refusal clause.** If widening `allow` cannot keep the planted person name wiped (e.g. the person dictionary word is also an issuer
  token), choose a different planted person name that is not an issuer, say so in the report, and never weaken the gate.

<paths>
data/transcripts/scripts/teams/securities_allowlist.py
data/transcripts/scripts/teams/securities_allowlist.json
data/transcripts/scripts/teams/research_fold.py
data/transcripts/scripts/tests/test_securities_allowlist.py
data/transcripts/scripts/tests/test_research_fold.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R11.md</decomp_doc> (round 11), cell `TR-a-11`.
<owned_cells>TR-a-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR11-a11-AC1, TR11-a11-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-a11.securities-allowlist.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR11-a11-AC1,TR11-a11-AC2` BEFORE the flip. Commit the code first, then pin
each artifact to a commit that actually contains it.
</proof_of_spec>

**REPORT:** source_rows and token count, the dry re-fold's whole-word counts (numbers only) for Microsoft, Apple, Broadcom, NVIDIA and Exxon
over the 29 local files after the change, the held_out row count, the two check lines, the four suites' lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a data asset and a fold change; the served re-write is the issuer's TR-b-11.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the issuer read the security master (DynamoDB scan, read-only).
comp-adversary: RUN -- 4 sources read (the 5,207-row snapshot, wipe load_assets/rule 4, research_fold, test_wipe_planted); BLIND to which issuer names are also person surnames in these meetings (stated as a known limit in the decomposition). Traps: editing the mail wipe, a weakened gate, a planted person who is also an issuer; the face forbids each.
lane: two new teams files, the fold, two tests, the investigation file.
</preflight>

Source: CTO round-10 analysis @8ce4b5098e E1; ruling msg 1608; decomposition round 11 cell TR-a-11 and issuer rulings 1-4.
