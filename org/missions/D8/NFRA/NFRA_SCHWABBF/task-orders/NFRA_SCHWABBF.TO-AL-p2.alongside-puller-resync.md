# TO NFRA_SCHWABBF.TO-AL-p2 -- re-sync the Alongside puller copy to the 49F puller as amended (the exact-copy rule)

<to_id>NFRA_SCHWABBF.TO-AL-p2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~16</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-state</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-p-2` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `BF-w-3` and `BF-v-5` (merged; the amended 49F puller is in your base)

---

## WORKER FACE

### THE CELL

`AL-p-2`. Andrew-direct 2026-10-20 ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box." Cell `AL-p-1` copied the 49F puller on 2026-10-20 ~16:xxZ. Since then `~SB`'s cells amended the 49F puller (`BF-w-3` landed the firm form for the firm-form set only and kept `08242234`, `08335338` on the pre-round form; `BF-v-5` made a firm-form master's run records land in the firm bucket's state tier). The Alongside copy at `infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1` is therefore behind. Make it a fresh copy of the 49F source at your base, with the same two differences as before. Nothing is uploaded or run; WORLD only because the file sits under `infra/`.

**Build.**
1. Overwrite `infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1` with `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` as it is at YOUR BASE (first confirm the source contains `function Get-StateBucket`; if it does not, STOP with a surprise row: your base predates `BF-v-5`). Then the copy differs from the source in EXACTLY two ways, both already in the current copy and to be reproduced:
   - the `[ValidateSet(...)]` on the `$Master` parameter lists the four Cottonwood masters `'08719286','08134043','08165601','08480305'` (and none of the 49F masters; the source's list is `'08242234','08335338','08403355'`);
   - the top header comment block (before the `param(` line) gains the same first two comment lines the current copy carries (read them from the current copy before you overwrite it: the first names "THE ALONGSIDE SCHWAB BOX copy of the 49F Schwab Box puller" and the masters, the second states the exact-copy rule). No other byte changes. ASCII only.
2. `data/canonical/schwab/tests/test_alongside_puller.py`: keep every existing test as it is (they must stay green on the new copy). ADD a test whose name contains `state_tier`: the copy contains the functions `Get-StateBucket`, `Get-StateKey` and `Get-RunRecordDests`; its `Get-StateBucket` map sends `cottonwood` to `opal-data-cottonwood`; the four Cottonwood masters are firm-form per the copy's own firm-form test function (read its name in the source), so a pull of one of them writes its run records to the state tier.
3. A ONE-TIME copy check in YOUR deliverables folder (NOT a standing test; Andrew's veto on a standing parity comparator): write `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~16/check_copy_diff.py`, the same check the earlier cell wrote at `.../deliverables/0.9.0_WK_NFRA_SCHWABBF~13/check_copy_diff.py` (read it; copy it; it is in the repo at your base): it prints `COPY-DIFF-OK changed_non_comment_lines=1` when the only changed non-comment line is the ValidateSet line and every other difference is a comment line in the header block before `param(`; otherwise `COPY-DIFF-FAIL` with the first offending hunk and exit 1.

### ACCEPTANCE

<criterion id="AL2-p2-AC1" cell_refs="AL-p-2"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_puller.py -q -p no:cacheprovider --color=no -k "master_set or syntax or state_tier"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL2-p2-AC1` -- the copy still accepts exactly the four Cottonwood masters, parses, and carries the state-tier functions.

<criterion id="AL2-p2-AC2" cell_refs="AL-p-2"><invocation>python org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~16/check_copy_diff.py</invocation><expect>^COPY-DIFF-OK changed_non_comment_lines=1$</expect></criterion>
`AL2-p2-AC2` -- the one-time proof that the Alongside puller is again the 49F puller with only the master list and a header comment changed.

<expected_criteria>AL2-p2-AC1,AL2-p2-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 has no `state_tier` test yet but the other selected tests pass (5 passed) -- this is a CONTROL, the build is the new `state_tier` arm: write it FIRST and watch it fail against the stale copy (which lacks `Get-StateBucket`). AC2: the check script does not exist at the base (rc 2) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit, including the 49F puller (`~SB` owns it).
- **WORLD floor, nothing uploaded or run.** No S3 upload, no Schwab call, no AWS.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W16-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken the test or the check.

<paths>
infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_alongside_puller.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-p-2`.
<owned_cells>AL-p-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL2-p2-AC1, AL2-p2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~16/NFRA_SCHWABBF.TO-AL-p2.alongside-puller-resync.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-p2-AC1,AL2-p2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed regions of the copy with line numbers, the check script's printed line, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule edit.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell (AL-i-2 carries the state-tier grant).
comp-adversary: DECLARED-NOT-APPLICABLE -- the finding is drift between two live boxes' pullers; guarded once here, not by a standing comparator.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-ALONGSIDE, C-TIERS; `AL-p-1`; `~SB`'s `BF-w-3` and `BF-v-5`.
