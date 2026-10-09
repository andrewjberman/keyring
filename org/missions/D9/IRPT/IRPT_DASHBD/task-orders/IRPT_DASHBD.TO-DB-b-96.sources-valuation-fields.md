# TO IRPT_DASHBD.TO-DB-b-96 -- E2: each custody source in sources.json carries valuation_source, fee_treatment and price_basis as structured fields, and the returns manifest reads them and never defaults to the custodian method -- a source with no entry writes absent (W66-S1)

<to_id>IRPT_DASHBD.TO-DB-b-96</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~71</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's R44 CTO half @fa8d2c2961 and ADDENDUM 13.1 (msg 3413), enrichment item E2 | **Decomp cell:** `DB-b-96` (decomposition section 49) | **outcome_ref:** FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-71`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~71/`.

**The cell (`DB-b-96`).** The CTO ruled (ADDENDUM 13.1, msg 3413) that the Cottonwood returns method is carried as STRUCTURED fields of the
firm's sources entry, never as a new `return_basis` value. `return_basis` stays "which arithmetic produced total_return_daily": `TWR`, or
`NOT_MEASURABLE` with its reason. There is NO enum edit.

In `C:/dev/wk-irpt-dashbd-71/data/assets/scripts/gold/irpt_reporting/`:
1. **`sources.json`.** Every custody source entry gains:
   - `valuation_source`: `custodian_reported` for the existing custodian channels;
   - `fee_treatment`;
   - `price_basis`.

   If a Cottonwood channel is declared in this file at your base, give it `positions_x_as_traded_close`, `net_of_fees` and `as_traded`
   (COTBKF ADDENDUM 8). If none is declared, say so in the record; do not invent one.
2. **`account_return_daily.py`.** The manifest `emit_day` writes reads the three fields from the source's entry. Its `method` text must not state
   the custodian method for a source whose `valuation_source` is not `custodian_reported`. A source missing the fields writes
   `valuation_source: absent` (and the same for the others), and never a default. A consumer can reject on the field.
3. **Tests:**
   - the manifest carries the source's three fields;
   - NEGATIVE arm: a source with no fields writes `absent`, and the method text names no custodian method;
   - every existing producer test still passes.
4. Record `SOURCES_FIELDS.json` {tests: {passed, failed, new_test, negative_test}, sources: {<name>: {the three fields}}, cottonwood_entry:
   present|absent}.

No deploy and no AWS call. The CB-al-2 mint (ADVI_COTBKF) is held until this drains.

<criterion id="DB47-2-AC1" cell_refs="DB-b-96"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r47/p47_round47.py" . DB47-2-AC1</invocation><expect>DB47-2-AC1 PASS</expect></criterion>
`DB47-2-AC1` -- every source carries the three fields, and the manifest reads them with an absent arm, tested. Base: FAIL.

<expected_criteria>DB47-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the returns producer, its sources.json and its tests folder. No deploy.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~71/
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-96.sources-valuation-fields.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 49 (round 47), cell `DB-b-96`.
<owned_cells>DB-b-96</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB47-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~71/IRPT_DASHBD.TO-DB-b-96.sources-valuation-fields.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB47-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the fields per source, whether a Cottonwood entry exists, the tests, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the returns producer and its declaration; it reaches served output only through a later release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB47-2-AC1 FAIL at base (no record; no fields in sources.json). Row W66-S1; CTO ADDENDUM 13.1.
lane: the <paths> block IS the grant.
</preflight>
