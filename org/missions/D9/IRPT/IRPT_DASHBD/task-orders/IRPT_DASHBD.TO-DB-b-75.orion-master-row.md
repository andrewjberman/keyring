# TO IRPT_DASHBD.TO-DB-b-75 -- E3: register Inflection's Orion custody master in infra/logic/registry/scopes.json, so the Inflection adapter resolves its addresses by lookup() rather than a legacy alias (row W49-S1)

<to_id>IRPT_DASHBD.TO-DB-b-75</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~52</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-36 ADDENDUM 5 (on ADJUDICATION_v21 @37daf4f637; PRD v0.9 @e8f96f579c), enrichment item E3 | **Decomp cell:** `DB-b-75` (decomposition section 39) | **outcome_ref:** FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-52`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~52/`.

**The cell (`DB-b-75`).** Round 36's Inflection adapter (DB-b-72) found no custody master for Inflection: its bindings are null, and the
firm's own bucket holds only `irpt/`, so Orion data was read through the routed legacy alias (row W49-S1). Rule 30 says a builder refusal is a
missing registry row to add.

1. **Read the precedents.** In `C:/dev/wk-irpt-dashbd-52/infra/logic/registry/scopes.json`, read the MASTER rows `08335338` (Schwab ->
   49financial) and `z09` (Black Diamond -> cottonwood), and the inflection FIRM row with its `aliases`.
2. **Find where Inflection's Orion data lands.** Use the routed alias and `data/inf/` (`README.md`, `scripts/bronze`, `scripts/silver`).
   Name the Orion identity a master key should carry (the firm-instance or database id Orion issues, as `z09` is Black Diamond's). List the
   prefix and count its objects. Record `landing` {prefix, objects, read_at}.
3. **Add the row.** Add one MASTER row (`firm` "inflection", `vendor` "orion", its bucket, a `note` citing your read) and name it in the
   inflection FIRM row's `masters`.
   - Follow the registry's own conventions: read `infra/logic/registry/` for its schema or validator, and run it if one exists.
   - Record `key` in `ORION_MASTER_ROW.json`.
   - If the data lands only under the legacy alias, the row says so. Do not move any data.

<criterion id="DB37-3-AC1" cell_refs="DB-b-75"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-3-AC1</invocation><expect>DB37-3-AC1 PASS</expect></criterion>
`DB37-3-AC1` -- a MASTER row inflection/orion exists and the firm row names it. Base: FAIL.

<criterion id="DB37-3-AC2" cell_refs="DB-b-75"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-3-AC2</invocation><expect>DB37-3-AC2 PASS</expect></criterion>
`DB37-3-AC2` -- lib/opal_naming.lookup on the new key returns firm inflection. Base: FAIL.

<criterion id="DB37-3-AC3" cell_refs="DB-b-75"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-3-AC3</invocation><expect>DB37-3-AC3 PASS</expect></criterion>
`DB37-3-AC3` -- the record names where that master's data lands, with an object count read by listing. Base: FAIL.

<expected_criteria>DB37-3-AC1,DB37-3-AC2,DB37-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit `infra/logic/registry/scopes.json` (one MASTER row and the firm's `masters`). No other registry
  file, no bucket and no data move.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~52/
infra/logic/registry/scopes.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-75.orion-master-row.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 39 (round 37), cell `DB-b-75`.
<owned_cells>DB-b-75</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB37-3-AC1, DB37-3-AC2, DB37-3-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~52/IRPT_DASHBD.TO-DB-b-75.orion-master-row.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB37-3-AC1,DB37-3-AC2,DB37-3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the key, the landing prefix and count, the validator run if any, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one registry row in infra/logic/registry/scopes.json; every lookup()/address() reader of the registry sees it; no data moves and nothing deploys.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB37-3-AC1/AC2/AC3 FAIL at base (no record). Row W49-S1.
lane: the <paths> block IS the grant.
</preflight>
