# TO MDPF_SECCLASS.TO-SC-e103.fwd45-b01b-e18-disposition -- round 26 SC-e-103: the disposition record for the two gold scripts that still use the old classification list (FWD-4 / FWD-5), no code change

<to_id>MDPF_SECCLASS.TO-SC-e103</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~93</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-103` (`decompositions/MDPF_SECCLASS_DECOMP_R26.md`) |
**outcome_ref:** FWD-4 / FWD-5 | **depends_on:** none | **source:** CTO round-25 analysis section 2 item 1 (FWD-4/5 open work: B_01b and E_18, named in the round-24 analysis section 1)

---

## WORKER FACE

### THE CELL

`SC-e-103`. Two Black Diamond gold scripts still read or write the OLD copy of the security-classification list, the DynamoDB table `bd-securities` (us-east-1): `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py` (a chain step between B_01 and B_02: it finds new (ticker, name) pairs, asks an outside model (OpenAI) to classify them and WRITES them into `bd-securities`) and `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` (detects new securities; it READS `bd-securities` for the set of known tickers, for name-prefix matching of truncated Black Diamond names, and through the shared module `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` function `default_bd_securities_lookup`; its classification of a new ticker already goes to the canonical table `etf-classifications`). The project goal FWD-4 is a check that finds no second definition of a class; FWD-5 deletes the old table once nothing reads it. This cell makes the next round's build a build with no discovery: it records, line by line, what each remaining use does and what replaces it. **You change no code.**

**What you build:**
1. Read both scripts in full, `data/black_diamond/scripts/gold/gold_dispatch.sh` (the chain: `CHAIN_CANONICAL`, the `PHASE_B3` / `PHASE_B3b` blocks, the `B_01b` and `E_18` rows) and the shared module's `default_bd_securities_lookup` and `plan_rows`.
2. Write the record `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~93/FWD45_B01B_E18_DISPOSITION.md`. It carries, in this order:
   a. **The line table.** One markdown row per line of B_01b.py and E_18.py that matches (case-insensitive) `bd-securities`, `BD_SECURITIES_TABLE` or `bd_securities`, in exactly this shape (the check parses it): `| B_01b:42 | DOC | <replacement or why none is needed> |` where the first cell is `B_01b:<line>` or `E_18:<line>`, the class is one of `DOC` (a comment or docstring), `DEAD` (a constant or import nothing uses), `READ-KNOWN-SET`, `READ-NAME-PREFIX`, `READ-LOOKUP`, `WRITE`, and the third cell names what replaces the line (an `etf-classifications` attribute, a step, or `nothing: the line goes`). There are 24 such lines at the base; the check recomputes the set live and refuses a missing or extra row.
   b. **What `etf-classifications` carries.** Read five live rows by `get_item` (tickers `IEFA`, `DIVZ`, `IDVZ`, and two rows whose key starts `NAME::` that you find) and list each row's attribute names; count the rows whose key starts `NAME::` with a paginated scan (`Select=COUNT`, `FilterExpression=begins_with(ticker, :p)`), printing the page count and the total. State, from those rows only, whether the table can answer E_18's three uses (known tickers, name-prefix resolution of a truncated name, the lookup).
   c. **Who else calls the shared lookup.** Every file in the repo that imports or calls `default_bd_securities_lookup` (use `comp-find`, report the denominator it prints), with what each does with the answer.
   d. **The chain.** Whether B_02 or any later step of `CHAIN_CANONICAL` reads a class that B_01b wrote (the `gold_dispatch.sh` comment says B_02 does; a census of `data/black_diamond/scripts/gold/` for `bd-securities` shows B_02 does not name it; print the census with its denominator and say which is true), as the line `B_02-READS-BD-SECURITIES: yes` or `B_02-READS-BD-SECURITIES: no`.
   e. **Three decision lines**, each alone on its line, each with a one-paragraph reason beneath it: `DECISION-B_01b: RETIRE-FROM-CHAIN` or `DECISION-B_01b: REPOINT-TO-ETF-CLASSIFICATIONS` or `DECISION-B_01b: OTHER:<text>`; and `DECISION-E_18: REPOINT-TO-ETF-CLASSIFICATIONS` or `DECISION-E_18: OTHER:<text>`. Rule for B_01b: if no later step reads what B_01b wrote and E_18 already classifies new tickers into the canonical table, choose RETIRE-FROM-CHAIN (the outside model call and the old table's only writer go); otherwise choose by what you measured and say why.
   f. **What round 27 builds**, as a numbered list of at most six items, each with the files it would touch and the one check that proves it.
3. Nothing else. Do not edit B_01b, E_18, `gold_dispatch.sh`, the shared module or any script.
**Report (not a criterion):** the numbers you measured (live line count, NAME:: row count and pages, caller count and the denominator).

### ACCEPTANCE

<criterion id="SC26-e103-AC1" cell_refs="SC-e-103"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/check_fwd45_disposition.py org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~93/FWD45_B01B_E18_DISPOSITION.md</invocation><expect>FWD45-DISPOSITION ok=True</expect></criterion>
`SC26-e103-AC1` -- every live reference line has a row with a class and a replacement, the three decision lines are present.

<criterion id="SC26-e103-AC2" cell_refs="SC-e-103"><invocation>bash -c 'git diff --name-only box/dell1...HEAD -- data infra lib | wc -l'</invocation><expect>0</expect></criterion>
`SC26-e103-AC2` -- the control that you changed no code (the branch you commit on carries no change under `data`, `infra` or `lib` relative to box/dell1).

<expected_criteria>SC26-e103-AC1, SC26-e103-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-16 ~03:5xZ): AC1 FAILS as expected (`FWD45-DISPOSITION ok=False record=ABSENT`, rc 3); AC2 PASSES as expected (`0`). The check's own green and negative arms were run on generated records (one row dropped -> `ok=False missing=[('B_01b', 3)]`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pandas, pyarrow and boto3 are already installed.
- **AWS is READ-ONLY** (get, list, head, query, scan, list_object_versions): no write to any bucket or table, no deploy, no invoke. Never push.
- **Never edit** anything outside the `<paths>` block; the check scripts under `R26_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W93-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check, and do not edit a check to make it pass.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~93/FWD45_B01B_E18_DISPOSITION.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R26.md</decomp_doc> (round 26), cell `SC-e-103`.
<owned_cells>SC-e-103</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC26-e103-AC1, SC26-e103-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~93/MDPF_SECCLASS.TO-SC-e103.fwd45-b01b-e18-disposition.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC26-e103-AC1,SC26-e103-AC2`.
</proof_of_spec>

**REPORT:** the record file, each criterion's output verbatim, the measured numbers, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a record whose table rows are typed from memory rather than from the live lines (the check recomputes the set); a decision that rests on a comment (`gold_dispatch.sh` says B_02 reads the table) not on a census; BLIND: consumers outside the BD gold tree (the shared module's other callers are item c).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-25 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_25_20261016.md`, msg 6457); DECOMP_R26.
