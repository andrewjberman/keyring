# TO ADVI_COTBKF.TO-CB-aw-1.ard-apply-mode -- round 49 CB-aw-1: the Cottonwood account_return_daily adapter gains a guarded --apply mode

<to_id>ADVI_COTBKF.TO-CB-aw-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~76</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aw-1` (`decompositions/ADVI_COTBKF_DECOMP.round49.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`data/assets/scripts/silver/commonwealth_account_return_daily.py` builds Cottonwood's `account_return_daily` days locally through
IRPT_DASHBD's producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`. It calls `emit_day(..., upload=False)` at
:336 for the address and census, and writes each day frame to `.scratch/advi_cotbkf/ard_cottonwood_r47/date=<D>/data.parquet`.

Its manifest is `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~74/ard_cottonwood_manifest.json`, which has per-day
`sha256`, `content_sha256`, `manifest_sha256` and the address, over 3,325 days. Today the adapter has only `--out` (build) and
`--verify-served`.

The mint (round 38, CB-al-2, on the applier `0.7.0_AE_CloudOps~CB2`, under a never-widen pair) must land each day through the
producer's own `emit_day(..., upload=True)`. That function writes `<address>/data.parquet` and `<address>/manifest.json`. No entry
point does that today, and the applier does not write code.

**Your item.** Code and tests only. No real S3 write: S3 is faked in the tests.

1. **Add `--apply --pair <coo_half_path> --pair <cto_half_path> --manifest <manifest path>`.** It:
   - (a) refuses unless both pair files exist and are committed (`git ls-files --error-unmatch`);
   - (b) re-hashes every local day file, and refuses on any mismatch with the manifest's `sha256`;
   - (c) lists the target prefix, and refuses if ANY key exists (a mint only);
   - (d) for each day in date order, reads the local frame and calls the producer's `emit_day(s3, frame, SCOPE, day, upload=True,
     ..., src=entry)` with the same arguments the build used, printing `LANDED date=<D> etag=<e> bytes=<b>`;
   - (e) prints the LAST line `ARD-COTTONWOOD-APPLY days=<n> landed=<k>`.
   - It never writes any other key and never deletes.
2. **`--verify-served`** compares each served day's CONTENT hash (`content_sha256`, the same content definition the build used) with
   the manifest. Its LAST line is `ARD-COTTONWOOD-VERIFY days=<n> match=<k>/<n>`.
3. **Tests:** `data/assets/scripts/silver/tests/test_commonwealth_ard_apply.py`, with S3 faked (moto or a stub), asserts:
   - (a) a refusal without the pair files;
   - (b) a refusal on a sha mismatch;
   - (c) a refusal on a non-empty prefix;
   - (d) a happy path lands N days through `emit_day(upload=True)` (assert the producer function is the one called), and
     `--verify-served` then reads `match=N/N`.
   Commit the test ALONE first; it must fail at the base.

### ACCEPTANCE

<criterion id="CB49aw1-AC1" cell_refs="CB-aw-1"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_ard_apply.py -q</invocation><expect>passed</expect></criterion>
`CB49aw1-AC1` -- assertions (a)-(d) pass on faked S3. The test alone was committed first and failed at the base.

<expected_criteria>CB49aw1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No real S3 write.** The producer is never edited. The silver suite stays green.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W76-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/test_commonwealth_ard_apply.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round49.md</decomp_doc> (round 49), cell `CB-aw-1`.
<owned_cells>CB-aw-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB49aw1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~76/ADVI_COTBKF.TO-CB-aw-1.ard-apply-mode.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB49aw1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pytest lines (the test and the silver suite); the apply mode's guards; commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change; the mint is CB-al-2 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE no real AWS act.
comp-adversary: RUN -- the test alone first; three refusals tested (pair, sha, non-empty prefix); the producer's own writer is the only writer; no delete path; BLIND: a producer-side upload failure mid-run (the apply prints per-day LANDED lines so a partial run is visible).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: issuer ruling (obligation 7): CB-al-2 has no apply entry point.
