# TO IRPT_DASHBD.TO-DB-b-79 -- E3: land Orion's gross-of-fees account TWR for Inflection as a silver input with its as-of, at an address() output, so the tie-out reads a landed figure and never a live pull (W53-S1, CTO Decision 2)

<to_id>IRPT_DASHBD.TO-DB-b-79</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~57</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-37 ADDENDUM 6 @fb5579ddfc (on ADJUDICATION_v22 @153e101791), enrichment item E3 | **Decomp cell:** `DB-b-79` (decomposition section 40) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-75 (master 4698, drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-57`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~57/`.

**The cell (`DB-b-79`).** Round 37 (DB-b-76, row D2-W53-S1) read Orion's gross return LIVE. The saved query defines only net, so gross came
from overriding the performance option in the Generate request body (`feeMethod` "Gross Of Fees"), which returned "Gross of Fees" on 3,129 of
3,129 rows. The CTO ruled (ADDENDUM 6, Decision 2) that the figure lands as a silver input with its own as-of, and the tie-out reads the landed
figure.

1. **The pull.** Start from round 37's script `deliverables/0.9.0_WK_IRPT_DASHBD~53/orion_gross_fee_pull.py`, copied into your folder. Pull
   Orion's gross-of-fees account TWR for Inflection (database 4698), read-only, for the same accounts and Rolling 3-Year window.
2. **The address.** Resolve the silver address with `lib/opal_naming.py` `address()` for master `4698` (registered @5f08e14443).
   - Print the call and its output into the record as `builder_call` {call, output}.
   - A builder REFUSAL is a missing registry row: file a row naming it, and never type an address by hand (rule 30).
3. **Land it.** Write one parquet plus a manifest (with `as_of` and the query) under that address. Record `address`, `as_of`, `rows`,
   `objects` (by listing after the write) and `columns`.

Record `ORION_GROSS_SILVER.json`. Use hashed account keys in committed files.

<criterion id="DB38-2-AC1" cell_refs="DB-b-79"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-2-AC1</invocation><expect>DB38-2-AC1 PASS</expect></criterion>
`DB38-2-AC1` -- Orion's gross TWR landed under a silver address with its as-of, rows and object count read by listing. Base: FAIL.

<criterion id="DB38-2-AC2" cell_refs="DB-b-79"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-2-AC2</invocation><expect>DB38-2-AC2 PASS</expect></criterion>
`DB38-2-AC2` -- the address is lib/opal_naming address() output, printed. Base: FAIL.

<expected_criteria>DB38-2-AC1,DB38-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception (law 4d77a9c3ea: egress open, Orion is not Bloomberg; CTO Decision 2):**
  - READ-ONLY Orion query calls for Inflection, with the credential read from its secret for the call only and never printed, written or
    committed;
  - ONE silver write (a parquet plus a manifest) under the `address()` output for master 4698.
- No other S3 write, no write to Orion, no delete.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~57/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-79.orion-gross-silver.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 40 (round 38), cell `DB-b-79`.
<owned_cells>DB-b-79</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB38-2-AC1, DB38-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~57/IRPT_DASHBD.TO-DB-b-79.orion-gross-silver.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB38-2-AC1,DB38-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the address and builder call, rows, objects, as_of, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one new silver prefix (address() output for master 4698) written once; no consumer reads it until DB-b-80; nothing served moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the box's own credentials; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB38-2-AC1/AC2 FAIL at base (no record). Row D2-W53-S1; CTO ADDENDUM 6 Decision 2.
lane: the <paths> block IS the grant.
</preflight>
