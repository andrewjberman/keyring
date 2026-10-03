# TO IRPT_DASHBD.TO-DB-b-18 -- P-2 packet readiness: the method-row contract bump, and the three reporting artifacts re-pinned and rehearsed from the map (nothing built, uploaded or served)

<to_id>IRPT_DASHBD.TO-DB-b-18</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~5</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer, inside its decomposition. Rounds 6-9 left three rows that bind
the P-2 packet:
- W1-S19 and W2-S3: the method row carries four columns its contract does not declare;
- W4-S1: the publish artifact does not package the opaque-id normalizer or the firm registry.
GATE (x) puts this in ROUND 10 (IRPT_BCKEND row S267). | **Decomp cell:** `DB-b-18` (decomposition section 10) | **outcome_ref:** P-2,
P-3 | **depends_on:** DB-b-15, DB-b-16, DB-b-17 (merged)

---

## WORKER FACE

**The cell.** The P-2 packet will build, upload and deploy three functions:
- `irpt-reporting-gold-lambda`
- `irpt-reporting-publish-lambda`
- `irpt-reporting-read-lambda`

It will also write the method row at `method_version` 2. This cell makes all four ready and proves it WITHOUT building or
uploading anything.

1. **The method-row contract (rows W1-S19 and W2-S3).** Bump `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json` from 0.2.0
   to 0.3.0.
   - Its `columns` must equal EXACTLY the keys `emit_method_row` emits in
     `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`. Today four are missing: `value_basis`,
     `value_basis_ruling`, `tieout_tolerance` and `tieout_tolerance_ruling`. Give each its type, nullability and meaning.
   - Add a `method_versions` entry for 2: the equity value basis, citing "1.0.0_SA_CTO RULINGS batch 193".
   - Set `supersedes` to 0.2.0 with its hash and why.
   - Recompute `schema_hash` by the file's own `schema_hash_basis` from the producer's row types. Write the provenance to say it
     is computed from the producer's row and is re-read from the served artifact at the packet's method-row write.
2. **Re-pin the three map entries** in `infra/aws/lambda/ci/lambda-source-map.json`.
   - Every `staged_from` member that rounds 6-9 changed is re-pinned to the commit that carries its current blob, with that blob's
     sha256 (hex). At least these: `account_return_daily.py` and `sources.json` (gold), and `sources.json` wherever it is staged.
   - The pins must be reachable commits on CLOUD; cite the merge commits.
   - Members that did not change keep their pins.
   - Do NOT touch `artifact_s3_key` or `artifact_sha256`: nothing is built.
3. **Package what the publish pass needs (row W4-S1).** The `irpt-reporting-read-lambda` entry already stages four members the
   publish entry lacks. Add the same four to the publish entry's `staged_from` and `files`:
   - `infra/aws/lambda/investor-reporting/_ids/ids.py` as `ids.py`
   - `infra/aws/lambda/investor-reporting/_ids/raw_keys.json` as `raw_keys.json`
   - `infra/aws/lambda/investor-reporting/_ids/data/custodian_key_seam.json` as `data/custodian_key_seam.json`
   - `data/firm_registry.json` as `firm_registry.json`
   Use the same pins as the read entry unless a newer blob is current.
4. **Rehearse.** Run the three criteria. AC2 materializes each package from the map exactly as `staged_from` and `files` say,
   imports its handler with the repo off `sys.path`, and calls the publish package's `directory_bucket("49financial")` with no
   environment variable. If a package does not import, find the missing member and stage it; do not change handler code.

<criterion id="DB10-1-AC1" cell_refs="DB-b-18"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r10/p10_1_ac1_method_contract_matches_row.py" .</invocation><expect>DB10-1-AC1 PASS</expect></criterion>
`DB10-1-AC1` -- the contract is 0.3.0 and supersedes 0.2.0. Its columns equal the emitted row's keys, and method_version 2 is
recorded citing batch 193. Base: FAIL (0.2.0).

<criterion id="DB10-1-AC2" cell_refs="DB-b-18"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r10/p10_1_ac2_packages_rehearsed.py" .</invocation><expect>DB10-1-AC2 PASS</expect></criterion>
`DB10-1-AC2` -- every pin of the three entries is sound and the changed members are packaged at HEAD. Each materialized package
imports, and the publish package resolves its directory bucket with no environment variable. Base: FAIL (the gold producer is
pinned before DB-b-13 and DB-b-15).

<criterion id="DB10-1-AC3" cell_refs="DB-b-18"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r10/p10_1_ac3_nothing_built_or_uploaded.py" .</invocation><expect>DB10-1-AC3 PASS</expect></criterion>
`DB10-1-AC3` -- the three artifacts' fields are unchanged: nothing is built or uploaded. Base: PASS (a guard).

<expected_criteria>DB10-1-AC1,DB10-1-AC2,DB10-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. In the source map, edit ONLY the three `irpt-reporting-*-lambda` entries; other seats edit
  other entries of that file.
- **AWS:** none. Never run `build-and-upload.sh` (it uploads), and no plan, apply or invoke.
- **Refusal clause.** A change to any handler, producer or test is out of bounds: stop and file a row. No client name in any record.

<paths>
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~5/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `data/`, `lib/`, `infra/logic/registry/`,
`org/standards/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 10 (round 10, workstream B), cell `DB-b-18`.
<owned_cells>DB-b-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB10-1-AC1, DB10-1-AC2, DB10-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~5/IRPT_DASHBD.TO-DB-b-18.p2-packet-readiness.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB10-1-AC1,DB10-1-AC2,DB10-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the four contract columns with their types, and the new schema_hash;
- every pin you moved (member, old pin, new pin);
- the four members staged into publish;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one standards contract's text and three functions' package manifests in the shared source map; 0 served bytes move (no build, no upload); the builds, uploads, applies, the backfill under method_version 2 and the method row's served write are the issuer's P-2 packet with both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy text changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB10-1-AC1 base FAIL (0.2.0), DB10-1-AC2 base FAIL (gold pinned before DB-b-13/15), DB10-1-AC3 base PASS (guard); AC2's checker run on a scratch map with the expected re-pins and the four publish members PASSED end to end (16, 16 and 29 members; publish resolved its directory bucket with no environment variable); dry-run at the base 2026-10-03 ~02:3xZ.
lane: the <paths> block IS the grant.
</preflight>
