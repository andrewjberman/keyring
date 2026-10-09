# TO ADVI_COTBKF.TO-CB-ap-1.writer-registry-local -- round 42 CB-ap-1: the cot price writer reads its firm registry from its own directory; dead check removed

<to_id>ADVI_COTBKF.TO-CB-ap-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~69</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ap-1` (`decompositions/ADVI_COTBKF_DECOMP.round42.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Round 40 made Cottonwood's price writer `data/cot/scripts/gold/build_canonical_prices_v2.py` stamp `source_firm` on every row. It
resolves the firm of each input's bucket and key prefix through `lib/opal_naming` and the registry under `infra/logic/registry/`.

In production, the cot gold run syncs ONLY `s3://opal-data-cot/code/gold/` (`data/cot/scripts/gold/gold_dispatch.sh`:497-498). The
writer there would find no `lib/` and no registry, and would stamp every row `absent` (row ADVI_COTBKF-D2-W68-S2).

**CTO ruling (ADDENDUM 14 @9a98e3b0a1).** The writer's deploy ships the ONE registry file it reads, at a `code/gold/` key, in the
same pair. The writer loads it from ITS OWN DIRECTORY: no new sync prefix, and no second path. Also remove the dead share-class check
(row W68-S1: Step 5b filters on `t1_transaction_observed`, a label the writer never emits).

**Your item.** Code and tests only. No deploy, no S3 write.

1. **Measure what the writer's firm resolution reads.** It is `scopes.json`, and possibly `org/standards/NAMING_SCHEMA.json` via
   `lookup()`.
   - The ruling names ONE file. Make the writer resolve firms from exactly one file, `<writer's own directory>/<registry file name>`,
     reading only the fields it needs: each scope's long and short forms, bucket aliases and key-prefix aliases.
   - Name the file and why, in the report. If one file truly cannot carry it, STOP that branch and file a BLOCKING row, and do not
     ship a second key.
2. **No second path.** The writer does not fall back to `lib/opal_naming` or `infra/logic/registry/`. If its own-directory file is
   missing or unreadable, every row reads `absent` and a WARN prints, never the own firm.
3. **Remove the Step 5b share-class check** (W68-S1). It is unreachable, because it filters on a label the writer never emits. Prove
   no test reached it: the full suite before and after, plus a coverage note.
4. **Tests.**
   - Update `data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py` so its fixtures place the registry file beside the
     writer (in a temp dir copy), and add:
     - (f) with the file beside the writer, a cottonwood-address input reads `cottonwood`;
     - (g) with the file absent, every row reads `absent`.
   - Commit the new assertions ALONE first; they must fail at the base.

Write `writer_registry_local.md` with: the registry file chosen, its repo path, its blob id (`git hash-object`), and its sha256. LAST
line exactly: `WRITER-REGISTRY file=<name> blob=<id> tests=<passed>`.

### ACCEPTANCE

<criterion id="CB42ap1-AC1" cell_refs="CB-ap-1"><invocation>python -m pytest data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py -q</invocation><expect>passed</expect></criterion>
`CB42ap1-AC1` -- assertions (a)-(g) pass. The new ones were committed alone first and failed at the base.

<criterion id="CB42ap1-AC2" cell_refs="CB-ap-1" judgment="true"/>
`CB42ap1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- exactly one registry file, read from the writer's own directory, with no fallback path;
- absent is never the own firm;
- the removed check was unreachable.

<expected_criteria>CB42ap1-AC1,CB42ap1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Code and tests only.** No S3 write and no deploy. `data/cot/scripts/gold/tests/` stays green.
- **The registry under `infra/logic/registry/` is READ, never edited.** The pinned copy is the deploy cell's act, not a repo copy.
- **Naming gate.** If it refuses typed firm tokens, derive them as ~68 did.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W69-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/cot/scripts/gold/build_canonical_prices_v2.py
data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round42.md</decomp_doc> (round 42), cell `CB-ap-1`.
<owned_cells>CB-ap-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB42ap1-AC1, CB42ap1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~69/ADVI_COTBKF.TO-CB-ap-1.writer-registry-local.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB42ap1-AC1,CB42ap1-AC2` BEFORE the flip. Mechanical: CB42ap1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the WRITER-REGISTRY line; the file chosen and why; the removed lines; the pytest lines (the test and the suite); commits,
with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change; the deploy is CB-ap-2.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- one file from the writer's own directory with no fallback; absent never defaults to own; the removed check proven unreachable; BLIND: a registry field the writer needs that the one file lacks (named BLOCKING).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 14 @9a98e3b0a1 (msg 3442); rows D2-W68-S1, D2-W68-S2.
