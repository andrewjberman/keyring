# TO MDPF_SECCLASS.TO-SC-e105.firm-mix-summary-writer-and-readers -- round 26 SC-e-105: name the writer of `platinum/firm/mix_summary.json` and read every reader for dependence on key order

<to_id>MDPF_SECCLASS.TO-SC-e105</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~95</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-105` (`decompositions/MDPF_SECCLASS_DECOMP_R26.md`) |
**outcome_ref:** FWD-1 (record hygiene) | **depends_on:** none | **source:** CTO round-25 analysis section 2 item 3

---

## WORKER FACE

### THE CELL

`SC-e-105`. The served object `platinum/firm/mix_summary.json` (the firm Mix summary the Advisor Intelligence page reads) is written with `json.dumps` in the order the script builds it. Round 25 gave the writer of `mix_daily_summary.json` (C_06) sorted keys; `mix_summary.json` is a different object with a different writer, and it is still unsorted. The question this cell answers, with evidence: WHO writes it, and does ANY reader depend on its key order. The issuer then either orders a sort under its own pair (some reader depends) or records that none does and closes. Starting point, to be checked and not trusted: `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` builds `summary` and calls `_write_batch([(summary, 'platinum/firm/mix_summary.json')], ...)` at about line 578; other firms' scripts (cot, inf) and `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` write objects of a similar name, and you decide which of them write THIS key (the Black Diamond firm `49financial` path) and say how you know.

**What you build:**
1. Write the record `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~95/FIRM_MIX_SUMMARY_WRITER_AND_READERS.md`. It carries:
   a. one line `WRITER: <repo path>:<line>` naming the file and the line holding `mix_summary.json` for the Black Diamond firm's object (the check opens that line), and a paragraph on every OTHER script that writes a similarly named object and why it is not this key;
   b. **the reader table**, one markdown row per reader FILE, in exactly this shape (the check parses it): `| <repo path>:<line> | ORDER-DEPENDENT: yes | <one line why> |` or `ORDER-DEPENDENT: no`. A reader is ORDER-DEPENDENT only if its result changes when the same object's keys arrive in another order: it takes the first or last element of an object, iterates an object and uses the position, compares the raw bytes or an ETag, or hashes the body. Reading by key name is not order-dependent. The check computes the census of candidate files itself (tracked code under `data/`, `infra/`, `lib/` and `portal/src` that mentions `firm/mix_summary` or `mix_summary.json`, minus tests and the writer) and refuses a missing or extra row; if you find a reader the census misses (a constant that builds the key), add its row too and say how you found it;
   c. the line `DECISION-FIRM-MIX-SUMMARY: SORT-UNDER-PAIR` (at least one row says yes) or `DECISION-FIRM-MIX-SUMMARY: NO-ORDER-DEPENDENT-READER` (every row says no), then a paragraph: for SORT-UNDER-PAIR, the one-line change in the writer and the served objects whose bytes would move with no content change; for the other, the sentence that closes the question.
2. Portal source is a nested repository: search it with `git -C portal grep`, read the files at `portal/src/...`. Do not edit anything.

### ACCEPTANCE

<criterion id="SC26-e105-AC1" cell_refs="SC-e-105"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R26_CHECKS/check_firm_mix_summary_record.py org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~95/FIRM_MIX_SUMMARY_WRITER_AND_READERS.md</invocation><expect>FIRMMIX-RECORD ok=True</expect></criterion>
`SC26-e105-AC1` -- the writer line opens on `mix_summary.json`, every census reader has a row, no row names a file outside the census, and the decision follows from the rows.

<criterion id="SC26-e105-AC2" cell_refs="SC-e-105"><invocation>bash -c 'git diff --name-only box/dell1...HEAD -- data infra lib | wc -l'</invocation><expect>0</expect></criterion>
`SC26-e105-AC2` -- the control that you changed no code.

<expected_criteria>SC26-e105-AC1, SC26-e105-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-16 ~03:5xZ): AC1 FAILS as expected (`FIRMMIX-RECORD ok=False record=ABSENT`, rc 3); AC2 PASSES as expected (`0`). The check's green arm (a generated record, 8 census files, all `no`) read `ok=True`; its negative arm (one row flipped to `yes` with the decision left at NO-ORDER-DEPENDENT-READER) read `consistent=False`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pandas, pyarrow and boto3 are already installed.
- **No AWS call of any kind.** Nothing is deployed.
- **Never edit** anything outside the `<paths>` block; the check scripts under `R26_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W95-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check, and do not edit a check to make it pass.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~95/FIRM_MIX_SUMMARY_WRITER_AND_READERS.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R26.md</decomp_doc> (round 26), cell `SC-e-105`.
<owned_cells>SC-e-105</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC26-e105-AC1, SC26-e105-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~95/MDPF_SECCLASS.TO-SC-e105.firm-mix-summary-writer-and-readers.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC26-e105-AC1,SC26-e105-AC2`.
</proof_of_spec>

**REPORT:** the record file, each criterion's output verbatim, the census denominator the check printed, any reader the census missed and how you found it, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a reader marked `no` because the file was skimmed (the row's why-line must cite what the code does with the object); a writer named from a similar filename (item a asks for the other writers and why they differ); BLIND: a reader outside the repo (a dashboard or notebook).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-25 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_25_20261016.md`, msg 6457); DECOMP_R26.
