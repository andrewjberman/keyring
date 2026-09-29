# AMGT_RESAPP task order -- `AMGT-vv-2` -- THE SCOPED API CARRIES THE TEAM'S CASES, CITED, BESIDE THE RULE'S BASE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-vv-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~170</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell's own acts (local S3 reads in the checks). The Lambda's read of the dossier prefix is a grant the redeploy (vv-4) adds under its never-widen pair.
comp-adversary: RUN by the issuer at the cut -- AC1 compares the served cases to the ONE dossier read field by field, so a converted, re-worded or inferred unit FAILS; AC2 runs the read with the PDF library unimportable, which is how the Lambda runs.
EGRESS CLASS, declared: NONE beyond read-only S3 GET/LIST of Opal's own gold. No vendor, no write.
</preflight>

## 1. THE CELL -- `AMGT-vv-2` (round 47, decomposition s.55)

AMGT_CORPUS serves each name's research dossier; its `fields.cases` holds the TEAM's own cases -- `base`, `upside`, `downside` --
each either `{value: <the pack's case table as written, e.g. {"EPS": {"2026E": "31.59", ...}, "Multiple": {...}, "Price": {...},
"Return": {...}}>, unit: <as written, may be null>, citation: {report_key, report_id, locator, passage}}` or
`{value: null, absent: "<reason>"}` (28 of 95 names carried case content at the cut). The ONE read is
`lib.research.corpus.dossier.read_dossier(security_key)` -- never re-implement its pick rule.

**Build** `scoped_amgt._team_cases(security_key) -> {"base", "upside", "downside"}`, and carry it in the `/thesis` payload at
`model.team_cases`, BESIDE `model.cases` (the rule's Base, which does not change):
- a case with a non-null `value` -> `{"status": "SERVED", "table": <value, unchanged>, "citation": <citation, unchanged>, plus EVERY
  unit/currency key the dossier case carries (`unit`, and `unit_as_written` / `currency` if present), copied as-is}` -- a null
  stays null; NOTHING is converted, rounded, re-worded or inferred (CTO ruling: the unit is the team's symbol as written; the
  render, which is not this cell's, says "as written in the team's pack" and never places it beside the Price tile);
- a case with a null `value` -> `{"status": "ABSENT", "reason": <the dossier's `absent` text, unchanged>}`;
- no dossier for the name (`LookupError`) or a failed read -> all three ABSENT with a reason naming that, never an empty object.
**Payload only:** neither the page nor the rich export renders `team_cases` in this cell (FWD-30's page/export parity must not move).

**Begin only when all three hold** (the issuer spawns you then): `AMGT-vv-1` is drained on CLOUD (it also edits `scoped_amgt.py`:
the `label` on `_model_cases`'s base -- keep it); AMGT_CORPUS `TO-CRPS-l-1` (the case unit carries its claim) is complete and merged
on CLOUD; and `lib.research.corpus.dossier` imports no PDF library at module import (AC2's precondition; asked of AMGT_CORPUS, which
owns that file). You do not edit `lib/research/corpus/`.

## 2. BOUNDS

1. **The adapter only.** No page file, no export file, no `lib/research/corpus/` file, no model-case rule change.
2. **No S3 write, no deploy, no server.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`; add tests that pin each branch (served, absent, no dossier).

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/*.py
lib/research/api/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~170/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; S3 `amgt/harvest/gold/research-dossier/` through `read_dossier`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-vv-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-2.AC1.py; echo "exit=$?"</invocation><expect>TEAM CASES CARRIED AS THE DOSSIER HOLDS THEM: 2 of 2 names -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-vv-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-2.AC2.py; echo "exit=$?"</invocation><expect>TEAM-CASE READ RUNS WITHOUT A PDF LIBRARY: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-vv-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-3.AC2.py; echo "exit=$?"</invocation><expect>PAGE AND EXPORT PRINT THE SAME CASES: 2 of 2 names -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the payload against the one dossier read; AC2 the read where the Lambda runs; AC3 the bound (page/export parity unmoved).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~170/AMGT_RESAPP.TO-AMGT-vv-2.the-scoped-api-carries-the-teams-cases.proof_of_spec.json`. Report once: what you changed and where, how many live names carry SERVED team cases, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-46 analysis s.4 item 2 (ruling 3, @0e405cc330) + CTO msg 26430 (CORPUS round-9 ruling 1). Base: AC1 FAIL
(no `_team_cases`), AC2 FAIL (dossier -> extract -> `import fitz` at `extract.py:56`), AC3 FAIL at portal DEV 5fac7a37 until vv-5 lands (the harness does not load). EXTERNAL DEPENDENCY: spawned
only after AMGT_CORPUS `CRPS-l-1` lands and `dossier.py` imports no PDF library (asked of `2.0.0_SA_COO~X`, msg 20260929T045710Z).
The Lambda's grant for `amgt/harvest/gold/research-dossier/` is NOT in the pool-prefix list at the cut (29 entries read) -- vv-4's
pair names it. SERVED: reaches the Lambda at vv-4.

<status>pending</status>
<round>47</round>
<slot>~170</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
