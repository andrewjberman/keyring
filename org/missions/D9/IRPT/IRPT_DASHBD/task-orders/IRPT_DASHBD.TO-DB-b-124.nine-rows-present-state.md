# TO IRPT_DASHBD.TO-DB-b-124 -- the present state of the nine rows compiled before today: each closed with its evidence or confirmed open -- read-only, the round's FIRST cell

<to_id>IRPT_DASHBD.TO-DB-b-124</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~99</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_68_20261011.md` @0005d9fd9a, section 4 item 1, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` @806d057711 | **Rows:** IRPT_DASHBD-D2-W86-S1, W86-S2, W87-S1, W85-S1, W88-S1 (ARMED), W88-S3 (ARMED), W89-S1, W96-S2, W96-S3 | **Decomp cell:** `DB-b-124` (decomposition section 70) | **outcome_ref:** FWD-11, FWD-12 | **depends_on:** none; it runs FIRST and ALONE, before any other cell of the round.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-99` (branch `wk-irpt-dashbd-68-99`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~99/`. Read first: section 1 and 3 of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why this is first.** Thirteen rounds of adjudication were held behind one blocked order and landed today in one remediation file. Nine of
its ten rows were compiled up to a day ago, and work has happened since. The CTO: "the round's first cell is a read of their present state,
before anything is built on them." You build NOTHING. You change no code.

**The cell (`DB-b-124`).** For EACH of the nine row ids above, read what it claims, then read the tree (and, only where a row's state lives
nowhere else, one live resource) AS IT IS NOW, and record in `ROW_STATE.json` -> `rows`: {id, state, evidence, how, reason}:
- `CLOSED_BY_EVIDENCE`: something that exists today makes the row's hazard or question moot. Cite it (`file` + `line`, or `commit`).
- `STILL_OPEN`: the row's condition still holds today. Cite what shows it.
- `NOT_ESTABLISHED`: you could not read it. Say why.
Start from these, each to be CONFIRMED OR REFUTED, never assumed:
- **W86-S1, W86-S2:** ruled today (analysis section 3: the date test; CONVENTION accepted as a floor). State is the ruling plus whether the
  record that shows the number says "floor" where it is shown.
- **W87-S1:** the last apply (DB-b-123, 2026-10-11) named a WORKER as applier again; read its record
  (`deliverables/0.9.0_WK_IRPT_DASHBD~98/METHOD_ROW3_APPLY.json`) and the ledger entry, and say which gates ran in which mode.
- **W85-S1:** is `MEASURED_THRESHOLDS_R1.json` tracked today at a path `handler.thresholds_path()` reads? (`git ls-files`, and the function
  in `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`.)
- **W88-S1 (ARMED) and W88-S3 (ARMED):** a later packet exists,
  `deliverables/0.9.0_WK_IRPT_DASHBD~92/NEVER_WIDEN_PACKET_R45_RELEASE_REFRESH_2.md`, with four members including `sources.json`, and
  DB-b-115 changed the handler to pass the source to the manifest. Do those disarm the rows AS WRITTEN (method_version equal on all rows of
  the kit day; the manifest stating method_version 2)? The CTO has VOIDED its half on R45, so the release is not applicable today either
  way: say what, exactly, each row still waits on. `armed`: [{id, disarmed, what_disarms}].
- **W89-S1:** read `data/assets/scripts/silver/commonwealth_account_return_daily.py` today: are the two stale statements (the docstring and
  the `COLUMNS_NULL` entry on `method_version`) still there? Method row 3's income statement changed today (DB-b-122, DB-b-123).
- **W96-S2:** ruled today as a direction for a later addendum (analysis section 3); state is that ruling.
- **W96-S3:** has anyone measured the gold's account id against the directory's since? (2.0.0_SA_COO~C2's messages are not in the tree;
  read the tree only and say NOT_ESTABLISHED if the tree does not show it.)

<criterion id="DB68-1-AC1" cell_refs="DB-b-124"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r68/p68_round68.py" . DB68-1-AC1</invocation><expect>DB68-1-AC1 PASS</expect></criterion>
`DB68-1-AC1` -- each of the nine rows is read at its present state with evidence, and the two ARMED rows carry whether they are disarmed and by what. Base: FAIL.

<expected_criteria>DB68-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS reads are limited to a `get` / `head` / `describe` of ONE named resource where a row's state can only be read live; a denial is recorded, not worked around.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~99/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W99-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~99/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-124.nine-rows-present-state.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 70 (round 68), cell `DB-b-124`.
<owned_cells>DB-b-124</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB68-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~99/IRPT_DASHBD.TO-DB-b-124.nine-rows-present-state.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB68-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; ONE table, a row per row id: its state today, the evidence (file:line or commit), whether you READ or RAN it; the two ARMED rows with whether each is disarmed and by what; everything NOT_ESTABLISHED and why; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a read-only cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; at most single-resource reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
