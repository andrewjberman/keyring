# TO MDPF_SECCLASS.TO-SC-e37 -- round 8 SC-e-37: FWD-5 -- the old list stops growing in the Inflection tree

<to_id>MDPF_SECCLASS.TO-SC-e37</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~27</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-37` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (slot ~27's queue: after TO-SC-e36)

---

## WORKER FACE

### THE CELL

`SC-e-37`. FWD-5: "The old Black Diamond copy of the list is gone, and it can be shown that nothing needed it" (PRD
`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12). This cell is the Inflection tree's stop:
`data/inf/scripts/classification/classify_assets.py` stops writing the old list (`bd-securities`, us-east-1). You write
code and a half REQUEST. You deploy nothing.

**The writer and its caller (measured 2026-10-07 at the cut; R8 left "its caller" unread, and it is resolved here):**
- `classify_assets.py` (409 lines) has two modes:
  - a CLI, `--upload`, which classifies net-new tickers from `s3://opal-data-inf/silver/assets_v2/<date>.parquet` through
    `gpt-4o-mini` and writes them to `bd-securities`, plus a manifest at
    `s3://opal-data-inf/gold/manifests/asset_classification_<date>.json`;
  - a library, `get_classifications(tickers, asset_names)`, which READS `bd-securities`.
- **No caller found in the repo.** Nothing imports `classify_assets` or invokes it:
  - `data/inf/scripts/gold/INF_D_02b.top_holdings.py:23` names it only in a docstring;
  - the Inflection gold dispatcher `data/inf/scripts/gold/orion-gold-dispatch.sh` never names it. Its
    `INF_B_01b.classify_new_securities.py` step is, despite its name, a pure S3 ticker-coverage report ("No DynamoDB. No
    OpenAI.").
- **Not deployed:** no `classify_assets.py` sits under `s3://opal-data-inf/code/`. The newest manifest it wrote is
  `asset_classification_2026-04-28.json`. So it is a latent writer, not a daily one. Stopping it closes the path. It moves
  no served figure today; confirm that in your half.
- Seen at the cut and NOT in your grant: `s3://opal-data-inf/code/gold/B_01b.classify_new_securities.py` (7,020 bytes,
  2026-06-11). It is a Black-Diamond-named `B_01b` copy in Inflection's code bucket, and no Inflection dispatcher line
  names it. Read it (`aws s3 cp` to `.scratch/`, read-only) and report whether it would write `bd-securities` if invoked.
  Name it in the half as an issuer act (retire or delete the object), never yours.

**Build:**
1. **The writer refuses.** In `classify_assets.py`, make the first statement under `if __name__ == '__main__':` (before
   argparse and before any AWS or model client) print one line starting `RETIRED:` that names the script and
   `MDPF_SECCLASS FWD-5 SC-e-37`, then `sys.exit(3)`.
   - Keep `get_classifications` importable and unchanged. It is a reader, and readers are SC-e-38's to trace.
   - If the module makes an AWS client at import time, that may stay (no call is made at import).
   - ASCII only.
2. **The half request.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INF_OLD_LIST_WRITER_20261007.md`
   with these sections: `## The act`, `## Blast radius`, and `Rollback per key`. It must carry the word `candidate` and contain no `{{slot}}`.
   - **The act.** The repo change itself, since the script is not deployed. Name what the issuer does with the stray
     `B_01b` object above.
   - **Blast radius:**
     - the candidate diff;
     - the rows this writer added (read-only `bd-securities` scan for `classified_by` = `gpt-4o-mini`, with counts by
       month);
     - confirmation, with the reads, that no schedule or dispatcher calls it.
   - **Rollback per key.** The repo commit to revert, and the stray object's current `VersionId`.

**THE PUSH HAZARD (rows S35, S38-S41).** The pre-push deploy gate uploads changed gold scripts to S3 before a half is
signed. This file sits outside `gold/`, but commit on YOUR branch only, and the issuer holds the merge until the half is
signed. Never push and never merge.

### ACCEPTANCE

<criterion id="SC8-e37-AC1" cell_refs="SC-e-37"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_inf_old_list_writer_check.py</invocation><expect>OLD-LIST-WRITERS-RETIRED tree=inf</expect></criterion>
`SC8-e37-AC1`: `classify_assets.py --upload`, with AWS unreachable, exits 3 with a `RETIRED:` line. `get_classifications`
still imports. The Inflection dispatcher still names no `classify_assets`.

<criterion id="SC8-e37-AC2" cell_refs="SC-e-37"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INF_OLD_LIST_WRITER_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC8-e37-AC2`: the half request exists, for the issuer to sign and send.

<expected_criteria>SC8-e37-AC1,SC8-e37-AC2</expected_criteria>

Dry run at the base 2026-10-07 (@1640a0e86e):
- AC1 base: FAIL as expected (`NOT-RETIRED tree=inf writer_retired=no library=ok dispatch_live_refs=0`). Its two control
  arms, library and dispatcher, read PASS at the base;
- AC2 base: FAIL as expected (half absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under
  `.scratch/`, uncommitted.
- **No deploy, no S3 write or delete, no table write, no trigger change, no push, no merge.** Read-only reads are allowed.
- **No vendor or model call.**
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row (id
  `MDPF_SECCLASS-W27-S<k>`). Do not weaken the test.

<paths>
data/inf/scripts/classification/classify_assets.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INF_OLD_LIST_WRITER_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ everything else named here and never edit it.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-37`.
<owned_cells>SC-e-37</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e37-AC1, SC8-e37-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~27/MDPF_SECCLASS.TO-SC-e37.inf-old-list-writer-stop.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e37-AC1,SC8-e37-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the guard, the row counts by month, the stray `B_01b` object's verdict and VersionId, commits (branch only).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery: no ledger or gate names classify_assets. Cell-specific read at the cut: no dispatcher, Terraform or repo caller invokes it; newest manifest 2026-04-28.
comp-iam: RUN -- R8 battery: 0 gap lines name bd-securities; the cell changes no grant.
comp-adversary: RUN -- cell-specific reads at the cut: git grep classify_assets (only a docstring in INF_D_02b), orion-gold-dispatch.sh (0 refs; INF_B_01b is S3-only), s3 ls opal-data-inf/code (no classify_assets; a stray code/gold/B_01b.classify_new_securities.py, 2026-06-11). BLIND: an out-of-repo scheduler (SSM, instance cron); the guard refuses such a call either way.
lane: the <paths> block IS the grant.
</preflight>

Source: DECOMP_R8 @495efa3c32 cell SC-e-37; PRD v0.12 @87ad6d2e4c; CTO ruling 106036.

## CLOSE -- SUPERSEDED, CARRIED TO ROUND 9 (2.0.0_SA_COO~M1, 2026-10-07 ~10:3xZ, on 1.0.0_SA_CTO~DELL1 msg 160)

`<status>` superseded: carried to round 9: served on branch wk-MDPF_SECCLASS-27 (code 6a996787eb, half 0df2fe8a87, proof 48d2d65404 VALID there); classify_assets.py has no caller and no S3 copy, and its stop waits with SC-e-35/36 for the reader switches.
The round-8 drain-end read is `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R8_20261007.md` @572829ce3b. Gate limb: none graded this modification.
