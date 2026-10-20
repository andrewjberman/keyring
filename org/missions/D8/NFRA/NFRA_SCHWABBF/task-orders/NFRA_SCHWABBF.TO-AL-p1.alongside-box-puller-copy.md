# TO NFRA_SCHWABBF.TO-AL-p1 -- the Alongside Schwab Box puller: the 49F daily puller copied for the four Cottonwood masters (nothing uploaded or run)

<to_id>NFRA_SCHWABBF.TO-AL-p1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~13</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>alongside</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-p-1` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** cell `BF-w-2` (workstream `keyform`) merged on `box/laptop`; the issuer spawns this order only after that merge, and your first act checks it (below)

---

## WORKER FACE

### THE CELL

`AL-p-1`, the puller of PRD v0.5 C-ALONGSIDE. Andrew-direct 2026-10-20 ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box". The Alongside Schwab Box runs the SAME daily puller as the 49F box, restricted to the four Cottonwood masters (08719286, 08134043, 08165601, 08480305). You make that copy and prove it is a copy. Nothing is uploaded, run, or sent to Schwab or AWS. WORLD only because the file sits under `infra/`.

**FIRST ACT (before any edit).** Open `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` at your base. It must contain a function named `Get-FirmOf` and a master-to-firm map for seven masters (the firm-form edit of cell `BF-w-2`). If it does NOT, STOP: write a surprise row (id `NFRA_SCHWABBF-W13-S1`, `surfaced_at` = `date -u +%FT%TZ`) saying the base predates `BF-w-2`'s merge, report, and make no edit.

**Build.**
1. Copy that file to `infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1` (the folder may already exist from another cell; create it if not). The copy differs from the source in EXACTLY two ways:
   - the `[ValidateSet(...)]` on the `$Master` parameter lists the four Cottonwood masters (and none of the 49F masters);
   - comment lines are added or changed ONLY in the top header comment block (before the `param(` line): add a first line `# THE ALONGSIDE SCHWAB BOX copy of the 49F Schwab Box puller (PRD v0.5 C-ALONGSIDE, FWD-8). Masters: 08719286 08134043 08165601 08480305 (firm cottonwood).` and one line stating that any logic change is made in BOTH pullers or the exact-copy rule (Andrew-direct 2026-10-20 ~13:5xZ) is broken. No other byte of the script changes: not the session lock, the quarantine, the vendor-master guard, the fire-time notes, the SNS parameter, the work directories or the key function. ASCII only.
2. Test `data/canonical/schwab/tests/test_alongside_puller.py` (reads text; runs nothing against Schwab):
   - MASTER SET (name contains `master_set`): the `ValidateSet` of the copy equals the `masters` of the registry rows in `infra/logic/registry/scopes.json` whose `firm` is `cottonwood` and `vendor` is `schwab`, both ways; the copy's `Get-FirmOf` map still sends each of those four to `cottonwood`; the ValidateSet of the 49F source does not appear in the copy's ValidateSet.
   - SYNTAX (name contains `syntax`): the copy parses with the PowerShell parser through `subprocess` (`powershell.exe -NoProfile -Command` calling `[System.Management.Automation.Language.Parser]::ParseFile`) with zero errors; if `powershell.exe` is not on PATH print `SKIP: powershell.exe not on PATH` and pass. The copy is pure ASCII and its first line names the Alongside Schwab Box.
3. A ONE-TIME copy check in YOUR deliverables folder (this is NOT a standing test and you do not put it under `tests/`): write `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~13/check_copy_diff.py`. It reads the 49F source and the Alongside copy, diffs them line by line (`difflib`), and prints `COPY-DIFF-OK changed_non_comment_lines=1` when the only changed non-comment line is the ValidateSet line and every other difference is a comment line inside the header block before `param(`; otherwise it prints `COPY-DIFF-FAIL` with the first offending hunk and exits 1. Do NOT commit it anywhere but your deliverables folder (a committed standing comparator between the two pullers is vetoed: Andrew, "no standing parity comparator").

### ACCEPTANCE

<criterion id="AL1-p1-AC1" cell_refs="AL-p-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_puller.py -q -p no:cacheprovider --color=no -k "master_set or syntax"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-p1-AC1` -- the copy accepts exactly the four Cottonwood masters (matching the registry both ways), keeps the firm map, and parses.

<criterion id="AL1-p1-AC2" cell_refs="AL-p-1"><invocation>python org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~13/check_copy_diff.py</invocation><expect>^COPY-DIFF-OK changed_non_comment_lines=1$</expect></criterion>
`AL1-p1-AC2` -- the one-time proof that the Alongside puller is the 49F puller with only the master list and a header comment changed.

<expected_criteria>AL1-p1-AC1,AL1-p1-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 and AC2 both "file or directory not found" (rc 4 / rc 2) -- FAIL as expected. Write the test and the check script FIRST, watch both fail, then make the copy.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit, including the 49F puller (`~SB`'s cell `BF-w-2` owns it) and every Terraform file.
- **WORLD floor, nothing uploaded or run.** You do not upload to S3, run the puller, contact Schwab, or call AWS.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W13-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test or the check to pass.

<paths>
infra/aws/ec2/alongside-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_alongside_puller.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, round 1), cell `AL-p-1`.
<owned_cells>AL-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL1-p1-AC1, AL1-p1-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~13/NFRA_SCHWABBF.TO-AL-p1.alongside-box-puller-copy.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL1-p1-AC1,AL1-p1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the two changed regions of the copy with line numbers, the check script's printed line, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the copy changes no schedule; fire times live in AL-s-1.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 4 (204 until entitled) is handled by the entitlement read before any pull (release act A5); exact-copy drift is guarded once, here, not by a standing comparator.
lane: the <paths> block IS the grant.
</preflight>

Cell AL-p-1 waits on BF-w-2's merge (workstream keyform, 2.0.0_SA_COO~SB). Source: PRD v0.5 C-ALONGSIDE, C-BACKFILL, C-DAILY; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-p-1, ruling 9.
