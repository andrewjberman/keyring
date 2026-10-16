# NFRA_OPLGTW task order -- `OG-rc-1` -- round-close proof hygiene: three proof instances the round-close check calls PROOF-BAD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rc-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rc-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- records only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the issuer's round-close read (`python .tools/round-close-check.py --project NFRA_OPLGTW --round 37` printed PROOF-BAD for these three orders at 2026-10-16 ~04:55Z).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-rc-1` (decomposition addendum R3-T.84, workstream ROUND-CLOSE-HYGIENE, FWD-22)

Run `python .tools/round-close-check.py --project NFRA_OPLGTW --round 37` from your worktree root and read the `PROOF-BAD` lines. Three are yours to clear; all other lines stay as they are.

1. **`TO-OG-gf-1`: "no proof instance named NFRA_OPLGTW.TO-OG-gf-1.gf-wave-b-remainder.proof_of_spec.json under deliverables/".** Worker ~110 wrote `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~110/NFRA_OPLGTW.TO-OG-gf-1.classified-remainder.proof_of_spec.json`, but the order's slug is `gf-wave-b-remainder`. `git mv` that file to `NFRA_OPLGTW.TO-OG-gf-1.gf-wave-b-remainder.proof_of_spec.json` in the same folder (content unchanged; the checker read it VALID under `--governing-order` the gf-1 order). Commit the removal of the old path and the add of the new one together.
2. **`TO-OG-cl-7` and `TO-OG-cl-8`: "FAIL row(s) AC2".** Their AC2 failed at your report because the commit-time naming gate did not read `name_rulings.json`; the gate was fixed (`OG-ng-2`, merged f1b3aeb579) and the issuer closed both orders. Re-run each order's mechanical criteria NOW at your current trunk (your HEAD is the trunk the issuer syncs you to): for `cl-7` its AC1 (`cl7.AC1.sh`) and AC2 (`cl7.AC2.sh`); for `cl-8` its AC1 (`cl7.AC1.sh`), AC2 (`cl7.AC2.sh`) and AC3 (`cl8.AC3.sh`), all under `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/`. Update the AC2 acceptance row of each instance (`NFRA_OPLGTW.TO-OG-cl-7.client-naming-conformance.proof_of_spec.json` and `NFRA_OPLGTW.TO-OG-cl-8.vendor-identifier-name-rulings.proof_of_spec.json` under your own `deliverables/0.9.0_WK_NFRA_OPLGTW~111/`) to the TRUE re-run output and status, and add under the row a note that it is a re-run after the gate fix (the instance's own `session_log` or notes field, in the shape the file already uses). Do not edit any other row. Validate each with `python .tools/proof-of-spec-check.py <instance> <the criteria ids> --governing-order <its order>`; both must read VALID (rc=0) with AC2 PASS. If a re-run does NOT pass, do not change the row to PASS: file a BLOCKING surprise row with the true output.
3. Re-run the round-close check: the three orders must no longer appear as `PROOF-BAD`.

## 2. BOUNDS

- Records only: the three proof instances and the investigation file. No code, no registry, no order file, no `<status>` change (the orders are already `complete`).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; invent a PASS; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~110/NFRA_OPLGTW.TO-OG-gf-1.classified-remainder.proof_of_spec.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~110/NFRA_OPLGTW.TO-OG-gf-1.gf-wave-b-remainder.proof_of_spec.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/NFRA_OPLGTW.TO-OG-cl-7.client-naming-conformance.proof_of_spec.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/NFRA_OPLGTW.TO-OG-cl-8.vendor-identifier-name-rulings.proof_of_spec.json
org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-gf-1.gf-wave-b-remainder.md
org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cl-7.client-naming-conformance.md
org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cl-8.vendor-identifier-name-rulings.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE only the four proof-instance paths (the first two are the rename) and the investigation file (append rows only if you hit a surprise); the three order files you only READ. Rows: id `NFRA_OPLGTW-Z-W111-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rc1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)round-close PROOF-BAD lines for cl-7, cl-8, gf-1: 0 \(want 0\); PROOF-BAD lines in all: \d+.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the round-close check no longer lists OG-cl-7, OG-cl-8 or OG-gf-1 as PROOF-BAD.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rc-1.round-close-proof-hygiene.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSES, and report once (commit hash, the AC1 line, the true re-run output lines of cl-7 AC2 and cl-8 AC2).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream ROUND-CLOSE-HYGIENE (decomposition addendum R3-T.84). The lane TREE_DELIVERABLES admits a deliverables folder only to its serial, so the issuer cannot rename or re-prove another seat's instance; a worker under an order naming the paths can. The remaining PROOF-BAD lines (OG-ap-14 and OG-hv-2: no acceptance row for AC3, a judgment criterion) and the 5 ungraded judgment criteria are the CVO's L9 and the appliers' to clear, not this cell's.
- Pre-cut: rc1.AC1 base FAIL as expected (cl-7, cl-8 and gf-1 listed PROOF-BAD).

<status>complete</status>
<round>37</round>
<workstream>ROUND-CLOSE-HYGIENE</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
