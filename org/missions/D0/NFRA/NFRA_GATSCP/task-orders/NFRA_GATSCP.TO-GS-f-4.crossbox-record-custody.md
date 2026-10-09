# TO NFRA_GATSCP.TO-GS-f-4 -- round 3 GS-f-4: a crossbox record's receiving lane commits its own record, and the integrate folds a record written on both ends

<to_id>NFRA_GATSCP.TO-GS-f-4</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.9.0_WK_NFRA_GATSCP~11</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** dell1 | **Decomp cell:** `GS-f-4` (`decompositions/NFRA_GATSCP_DECOMP.round3.md`) | **outcome_ref:** FWD-7 |
**rows:** D1-S10, Z-S1 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

A cross-box order travels as `org/devices/crossbox/XB-*.json`, one record per file (`crossbox-call.py`; fields include
`id`, `from_serial`, `to_serial`, `sent`, `ack`). The lane `DEVICES_CROSSBOX` (`.owned-paths.yaml:822-827`, path rule :2937) admits
only `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`, `2.0.0_SA_COO~C`. On 2026-10-09 the receiving site-Z lane `0.7.0_AE_CloudOps~ZG` could not
commit its own ACK (row Z-S1), and box/sitez's integrate HELD on the record because each side had written a field (row D1-S10).
`.tools/owned-paths-validate.py` resolves a lane by longest glob (`resolve_lane` :268) and `check_agent(agent, path, lanes,
paths_config, grant=None, root=None, cache=None)` (:289-351) has no per-record permit (the worker `<paths>` grant is for
`0.9.0_WK_*` serials only). Its CLI today: `<yaml>` and `--check-agent <agent> <yaml>` (main, :516). `crossbox-call.py` `ack`
writes `ack.at`/`ack.by` on the receiving box; `merge --id --ref` (:597-625) already folds a record's fields and refuses a field
both copies hold differently. `.tools/merge-resolve-known.py` knows three classes (channel union, the generated index, APPEND_ONLY
logs) and answers `not a known multi-writer class` for anything else (:464). The CTO ruled (R5): the receiving lane commits ITS
OWN record, DEVICES_CROSSBOX admits it for that record only, never another's; the integrate resolver unions by record id, never by
line.

### THE CELL

`GS-f-4`. A crossbox record's receiving lane commits its own record, and the integrate folds a record written on both ends.

**Build:**
1. `owned-paths-validate.py`: in `check_agent`, for a path matching `org/devices/crossbox/XB-*.json`, permit the agent
   when the record's `to_serial` (read from the index git resolves, `git show :<path>`, falling back to HEAD for a deletion) is
   exactly the agent's full serial. Nothing else changes for that lane. Add the CLI `--check-path <agent> <path>`: loads
   `.owned-paths.yaml` as `--check-agent` does, prints `PERMIT` or `REFUSE <reason>`, exits 0 / 1. Keep `--self-test` green and
   add arms for it.
2. `merge-resolve-known.py`: a fourth class for `org/devices/crossbox/XB-*.json`: parse the base, ours and theirs records (same
   `id`), fold field by field (a field changed on one side only takes that side; a field changed on both sides to the same value
   takes it; a field changed on both sides to different values REFUSES the path), write the folded JSON blob, and print
   `RESOLVED <path> <blob> crossbox-fold`. Use the same field fold `crossbox-call.py merge` uses, reading that code, without
   editing `crossbox-call.py`.

### ACCEPTANCE

<criterion id="GF4-AC1" cell_refs="GS-f-4"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/r3_xbox_custody.py" lane</invocation><expect>GS-F4-LANE ok=True</expect></criterion>
`GF4-AC1` -- the receiving lane named in the staged record is permitted; another Codex lane and an unnamed COO lane are refused.

<criterion id="GF4-AC2" cell_refs="GS-f-4"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round3_prep/checks/r3_xbox_custody.py" resolver</invocation><expect>GS-F4-RESOLVER ok=True</expect></criterion>
`GF4-AC2` -- a record written on both ends (ack on one, sent on the other) folds with both fields; a same-field clash is refused.

<expected_criteria>GF4-AC1,GF4-AC2</expected_criteria>

Read every check before you build. Each prints its arms and ONE last line, which the expectation is matched against. You do not
edit the checks. Report the last line of the tool's own self-test after your change where the tool has one.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~11/` and this
  order's file.
- No edit outside the grant. No push, no merge into a shared branch, no override at any commit.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_GATSCP-D1-W11-S<k>`, `surfaced_at` = `date -u +%FT%H:%MZ` at filing) in the investigation file, and do not weaken the
  check or the expected value. A fact in this order that the repository contradicts is also one row; keep working on what it does
  not block.

<paths>
.tools/owned-paths-validate.py
.tools/merge-resolve-known.py
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it, in particular the check files under
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round3.md</decomp_doc> (round 3), cell `GS-f-4`.
<owned_cells>GS-f-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: GF4-AC1, GF4-AC2. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.9.0_WK_NFRA_GATSCP~11/NFRA_GATSCP.TO-GS-f-4.crossbox-record-custody.proof_of_spec.json` (the order file's stem) with `to_id` `NFRA_GATSCP.TO-GS-f-4`,
validated with `python .tools/proof-of-spec-check.py <instance> GF4-AC1,GF4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** every criterion's last line whole; the self-test's last line; rows; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- each criterion carries its negative or control arm (decomposition round 3, battery); BLIND: a census's conclusions are the CTO's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: ROUND_ANALYSIS.round2.md @0ef2dc8325 (with ADDENDUM 1); CTO msg 2258 for D1-S5; decomposition round 3. Base dry-run: see the
issuance commit.
