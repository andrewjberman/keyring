# TO NFRA_SCHWABBF.TO-BF-r3 -- the two hand-parsing readers (they read 0833) back to their pre-round bytes

<to_id>NFRA_SCHWABBF.TO-BF-r3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-r-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-r-3`. PRD v0.7 C-SCOPE and C-KEYFORM: 08335338 (0833) stays on today's key ("they keep their daily pull and their current keys byte-for-byte"). Andrew-direct ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
Two canonical readers parse the OLD layout by hand, and both read master 08335338: `data/canonical/schwab/build_canonical_daily.py` (`CANON_MASTER`, the RPS partitions) and `data/canonical/schwab/silver/build_fact_tax_1099div.py` (`MASTER`, the `tnn` feed). Round 2 (merged `ef38445985`) moved them to the firm form, which is now wrong for the master they read: they would list a firm folder that holds nothing of 0833's and report "nothing to do" or "not moved". They need NO change under v0.7.
Put these THREE files back to their pre-round bytes, byte for byte, in ONE commit:

1. `data/canonical/schwab/build_canonical_daily.py`
2. `data/canonical/schwab/silver/build_fact_tax_1099div.py`
3. `data/canonical/schwab/tests/test_canonical_daily_date_axis.py`

The pre-round bytes are the blobs at commit `5f1ad506a4`. Use `git show 5f1ad506a4:<path> > <path>` for each, never retyping. Touch nothing else.

### ACCEPTANCE

<criterion id="BF3-r3-AC1" cell_refs="BF-r-3"><invocation>python org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SB/R3_CHECKS/restore_readers_check.py</invocation><expect>^RESTORE-OK files=3$</expect></criterion>
`BF3-r3-AC1` -- the three blobs at HEAD equal the blobs at `5f1ad506a4`.

<criterion id="BF3-r3-AC2" cell_refs="BF-r-3"><invocation>python -m pytest data/canonical/schwab/tests/test_canonical_daily_date_axis.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-r3-AC2` -- the control: the pre-round test file passes against the pre-round builder (16 passed expected; 17 at the round-2 head).

<expected_criteria>BF3-r3-AC1,BF3-r3-AC2</expected_criteria>

Dry-run at the base: AC1 `RESTORE-FAIL differing=3 of 3` (rc 1) -- FAIL as expected; AC2 PASS as expected (a control).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. LOCAL: no S3, no network, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W2-S<k>` and use the next), and do not weaken the check.

<paths>
data/canonical/schwab/build_canonical_daily.py
data/canonical/schwab/silver/build_fact_tax_1099div.py
data/canonical/schwab/tests/test_canonical_daily_date_axis.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-r-3`.
<owned_cells>BF-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-r3-AC1, BF3-r3-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-r3.readers-back-to-pre-round.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-r3-AC1,BF3-r3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the RESTORE-OK line, the pytest summary line, the one commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- restore of three files.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; this cell touches no IAM and no network; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 2 (the readers read 0833, so v0.7 needs no change) is the reason for the order.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.7 C-SCOPE, C-KEYFORM; decomposition round 3 cell BF-r-3.
