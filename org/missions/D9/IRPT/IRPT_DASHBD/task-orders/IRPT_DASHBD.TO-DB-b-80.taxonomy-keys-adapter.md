# TO IRPT_DASHBD.TO-DB-b-80 -- E2: the ADOPTED taxonomy amendment -- account_boundary on the four entries and the 48 header in orion_cashflow_taxonomy.yaml; the adapter reads the keys from the ratified file (the orion_sources.json departure removed); the tie-out re-read on both bases from the landed gross

<to_id>IRPT_DASHBD.TO-DB-b-80</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~56</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-37 ADDENDUM 6 @fb5579ddfc (on ADJUDICATION_v22 @153e101791), enrichment item E2 | **Decomp cell:** `DB-b-80` (decomposition section 40) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-79 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-56`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~56/`.

**The cell (`DB-b-80`).** It starts after DB-b-79 has landed and drained; the issuer spawns it then. The CTO ADOPTED the rule-24 proposal
(ADDENDUM 6, Decision 1; proposal `deliverables/0.9.0_WK_IRPT_DASHBD~54/ORION_TAXONOMY_AMENDMENT_PROPOSAL.md`).

1. **The taxonomy edit.** In `C:/dev/wk-irpt-dashbd-56/data/inf/scripts/silver/orion_cashflow_taxonomy.yaml`:
   - Internal Account Journal In gets `account_boundary: in`; Internal Account Journal Out gets `account_boundary: out`.
   - Federal Tax Withheld and State Tax Withheld each get `account_boundary: out` and `account_boundary_when: before_tax_return`.
   - No `bucket` or `nna_direction` moves. Foreign Tax Withheld, Foreign Dividend Tax and Tax Credit stay untagged.
   - Correct the header count (title, comment and `schema_collapse_audit.total_type_desc_entries_v2`) to 48, the number of `types` entries
     (W54-S1).
   - Add a `ratification_history` entry citing ADDENDUM 6 @fb5579ddfc.
2. **The adapter.** Copy round 37's adapter (`deliverables/0.9.0_WK_IRPT_DASHBD~53/`) into your folder. Make it read `account_boundary` from
   the ratified file, and remove `orion_sources.json`'s `inter_account_comment` and `tax_withheld_comment` departure. There is one source of
   truth.
3. **The tie-out on both bases.**
   - Gross: read the LANDED gross (`deliverables/0.9.0_WK_IRPT_DASHBD~57/ORION_GROSS_SILVER.json` names its address and as_of).
   - Net: read the landed net, as round 36 did.
   - Same sample, 0.35 pp.
   - Record `INF_TIEOUT_R38.json` with `gross` {denominator, within}, `net` {denominator, within}, `gross_source` (the s3 address) and
     `as_of`.

<criterion id="DB38-3-AC1" cell_refs="DB-b-80"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-3-AC1</invocation><expect>DB38-3-AC1 PASS</expect></criterion>
`DB38-3-AC1` -- the four entries carry account_boundary as adopted, no other entry does, and the header reads 48. Base: FAIL.

<criterion id="DB38-3-AC2" cell_refs="DB-b-80"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-3-AC2</invocation><expect>DB38-3-AC2 PASS</expect></criterion>
`DB38-3-AC2` -- the adapter reads the keys from the ratified taxonomy file and the departure comments are gone. Base: FAIL.

<criterion id="DB38-3-AC3" cell_refs="DB-b-80"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-3-AC3</invocation><expect>DB38-3-AC3 PASS</expect></criterion>
`DB38-3-AC3` -- the tie-out on both bases, gross from the landed silver. Base: FAIL.

<expected_criteria>DB38-3-AC1,DB38-3-AC2,DB38-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit `data/inf/scripts/silver/orion_cashflow_taxonomy.yaml`, the four entries' keys plus the header count
  and one history entry, as ADDENDUM 6 adopts. No `bucket`, `nna_direction` or other entry moves (CTO: served NNA does not move).
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~56/
data/inf/scripts/silver/orion_cashflow_taxonomy.yaml
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-80.taxonomy-keys-adapter.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 40 (round 38), cell `DB-b-80`.
<owned_cells>DB-b-80</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB38-3-AC1, DB38-3-AC2, DB38-3-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~56/IRPT_DASHBD.TO-DB-b-80.taxonomy-keys-adapter.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB38-3-AC1,DB38-3-AC2,DB38-3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the yaml diff in one line, the within counts on both bases, the gross source, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- additive keys on four taxonomy entries; no bucket or nna_direction moves, so served NNA readers of the file see no changed value.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB38-3-AC1/AC2/AC3 FAIL at base (no keys, header 43, no record). Rows W49-S3, W54-S1; CTO ADDENDUM 6 Decision 1.
lane: the <paths> block IS the grant.
</preflight>
