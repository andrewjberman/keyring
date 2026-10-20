# NFRA_MCPINDEX task order -- `MX-y-5` -- attribute the `harvest_query_columns` date disagreement: why an answer dated 2026-10-09 sits beside source data that ends 2026-10-08 (code, catalog, battery or data), with the evidence and the owner

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md</decomp_doc>
<owned_cells>MX-y-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-y-5.harvest-date-attribution</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~88</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the planted negatives inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-y-5` (round 25, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-24 analysis `ledger/ROUND_ANALYSIS.round24.md`, item 2)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 24's source compare listed the source of each answer and compared dates. For 25 tools the answer's date is among the source dates; for exactly one tool it is not. The CTO's ruling: "the answer must not be dated after its source. A code fault goes to `2.0.0_SA_COO~O`."

**What was seen (the issuer's notes; verify them, do not trust them).** In `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/SOURCE_COMPARE_20261020.json`, the entry for `harvest_query_columns` (case `H15`) reads `answer_as_of` `2026-10-09T10:34:23Z`, source `s3` bucket `opal-data-harvest` prefix `amgt/harvest/gold/chatter_daily/`, `source_dates` ending `2026-10-08`, `agrees` false, reason "answer date 2026-10-09 is not among the source dates". The compare instrument lists the prefix with a `/` delimiter, so its dates are the `date=YYYY-MM-DD` partition folders; the answer's `as_of` is a UTC clock time. The case is `H15` (`dataset chatter_daily`, columns `security_key`, `day`, `articles_total`, one security key, limit 3) and its result in `results_all_20261020.json` has `as_of` `2026-10-09T10:34:23Z`.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~88/harvest_date_attribution.json`, one object, and no other deliverable.

### The contract (verbatim from the decomposition; it is the whole specification)

**Y5 HARVEST DATE ATTRIBUTION.** `harvest_date_attribution.json`, schema `gateway_harvest_date_attribution/1`: `{"schema","tool":"harvest_query_columns","answer_as_of":str,"source_newest":str,"cause":"code"|"catalog"|"battery"|"data","owner":str,"evidence":[str,...],"fix":str}`. Read the code that builds the answer's `as_of` (the harvest module under `infra/aws/ec2/opal-gateway/app/`), the case and result (`cases_all_20261019.json`, `results_all_20261020.json`, case id of `harvest_query_columns`), and the source listing in `SOURCE_COMPARE_20261020.json`; decide whether the as_of is a read time or a data date (the answer 2026-10-09T10:34:23Z carries a clock time), whether the source listing the instrument used is the prefix the tool read, and whether the answer may be dated after its source. `evidence` entries are `<path>:<line>` that exist or `<results file>#<case_id>`; `cause` `code` names owner `2.0.0_SA_COO~O`, `catalog` or `battery` names `2.0.0_SA_COO~MI`, `data` names the producing project; `fix` is at least eight ASCII words; at least two evidence entries.

How the checks read it, so you write it to pass:
- `answer_as_of` is the compare entry's `answer_as_of` string exactly; `source_newest` is the greatest string of the entry's `source_dates` exactly.
- `cause` is `code` when the gateway code builds a date that is wrong for what it claims, `catalog` when a catalog row or contract states the wrong date grain, `battery` when the comparison or the case treats two different date grains as equal, `data` when the producing data itself carries the later date. `owner` for `code` is `2.0.0_SA_COO~O`; for `catalog` or `battery` it is `2.0.0_SA_COO~MI`; for `data` a project code in capitals with an underscore (for example `AMGT_HARVST`).
- `evidence` is a list of at least two DIFFERENT strings. Each is either `<repo-relative path>:<line number>` (the file must exist and the line must be inside it) or `<repo-relative results path>#<case id>` where the case id is one of this tool's cases in the compare entry (`H15`) and the file holds that case id.
- `fix` is one plain ASCII sentence of at least eight words that says what changes and where.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/SOURCE_COMPARE_20261020.json`: the compare run (find the entry whose `tool` is `harvest_query_columns`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/results_all_20261020.json` and `cases_all_20261019.json`: every result and every case of the run (case `H15`).
- `workflows/gateway_battery/source_compare.py`: the instrument (how it takes dates from a listing and compares them).
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only): the tool is `tools.py:1413` calling `harvest_figures.py:572` (`harvest_query_columns`); its answer date is `_as_of(srcs)` at `harvest_figures.py:623`, built by `_stamp_of` and `_as_of` at `harvest_figures.py:162-178` from the regular expressions at `harvest_figures.py:89-90`; the part it reads for a parquet dataset is chosen by `harvest_typed.py:233` (`newest_part`, key layout `<prefix>date=YYYY-MM-DD/part-<stamp>.parquet`); the dataset spec for `chatter_daily` is at `harvest_figures.py:95`.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The issuer has added the sparse folders `infra/aws/ec2/opal-gateway/app`, `workflows/atom_decomposition` and `workflows/gateway_battery` to your worktree; if any is missing, `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` is the only sparse change you may make.
1. Read the compare entry, the case `H15` and its result. Then read the code named above and follow the answer's `as_of` to the line that builds it: which regular expression matches first, what text of the key it reads (a `part-<stamp>` file name or the `date=` folder), and whether that text is a time the part was WRITTEN or the date the part's DATA covers.
2. Decide the three questions of the contract: is the as_of a read or write time or a data date; is the prefix the instrument listed the prefix the tool read; and can an answer be legitimately dated after its source. Then choose the `cause`. An honest `battery` or `data` cause beats a convenient `code` one, and the reverse holds too: if the gateway code states a clock time where it claims a data date, say `code`.
3. Write the file named above with the Write tool, ASCII, `indent=1`. Run both criteria of section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y5_check.py` for exactly what each arm grades.
4. Then spot-check yourself: re-read each evidence line you cited; if it does not show what your `cause` says, fix the entry. The issuer reads it at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `source_compare.py`, `members.yaml`, the catalog or its row files, the emitter, any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y5.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y5_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~88/harvest_date_attribution.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~88/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-y-5.harvest-date-attribution.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W88-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-y-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y5.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~88/harvest_date_attribution.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (tool harvest_query_columns, the real answer date and newest source date); the clean control and the six planted negatives behave; the schema; the tool; answer_as_of and source_newest equal the compare entry's; cause is code, catalog, battery or data; the owner follows the cause -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-y-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y5.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~88/harvest_date_attribution.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the clean control and the six planted negatives behave; at least two different evidence entries, each an existing repository file with the line inside it or the tool's case id inside its results file; the fix is ASCII and at least eight words -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~88/NFRA_MCPINDEX.TO-MX-y-5.harvest-date-attribution.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the `cause` and `owner` in one line with the one-sentence reason; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 25, workstream GATEWAY, worker ~88. Source: the CTO's round-24 analysis `ledger/ROUND_ANALYSIS.round24.md` (`1.0.0_SA_CTO~Z`, item 2: "Fix the `harvest_query_columns` date: the answer must not be dated after its source. A code fault goes to COO~O.") and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md` (the contract R25.3 Y5 is frozen at the cut). Base dry-runs 2026-10-20: `y5.AC1 base: FAIL as expected` and `y5.AC2 base: FAIL as expected` (the deliverable is absent; the control and planted-negative arms pass, the final arm FAILs; ARMS 8 ok 1 failed and 7 ok 1 failed). A scratch reference file (outside the repository) passes both criteria (AC1 9 of 9 arms, AC2 8 of 8) and records the issuer's own reading from the code: the answer's `as_of` is the `part-<stamp>.parquet` write stamp (`_STAMP_RE`, `harvest_figures.py:89`, wins over the `date=` folder at `:176-178`) of the newest part (`harvest_typed.py:233`), a write time that can fall on the day after the partition it sits in, while the compare instrument lists only the `date=` folders (a different date grain); the reference cause is therefore `battery` (owner `2.0.0_SA_COO~MI`) with a fix in the comparison, but the worker decides from the code and may reach `code` (the gateway states a write time where a data date is claimed) or `data`. The checks prove shape and grounding (real answer and source dates, enum, owner rule, resolving evidence, sentence-length fix), not that the cause is right: the issuer reads the attribution at the drain, and a `code` cause is carried to `2.0.0_SA_COO~O` as a defect row.

<status>issued</status>
<round>25</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
