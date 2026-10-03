# NFRA_OPLGTW task order -- `OG-gr-2` -- why dim_position 2026-09-21 collides under the candidate grain (read-only)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gr-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only, with the identity OG-gr-1 used.
comp-adversary: DECLARED-NOT-APPLICABLE -- the question is the CTO's (analysis round 14 s.4 item 4).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `OG-gr-2` (decomposition addendum R3-T.8, item 4)

**READ-ONLY.** Andrew-direct 2026-10-03 ~17:3xZ: "it is inappropriate for agents to adjust our data engineering
operations without my explicit directive." This cell writes no data, changes no pipeline, re-runs nothing and quarantines
nothing.

Your OG-gr-1 record (`deliverables/0.9.0_WK_NFRA_OPLGTW~22/GRAIN_R13.json`, its scripts beside it as `.py.txt`) found:
- the candidate grain unique on 50 of 52 qualified snapshots;
- the two failures both `dim_position` 2026-09-21, one colliding group at EACH master;
- `quantity_cash_settled` as an added column unique on all 26 `dim_position` snapshots with 0 blanks (noted, not chosen).

1. For each master's 2026-09-21 colliding group, print the colliding rows' KEY columns and the columns that differ
   between them (column names and a per-column equal/differ flag; no account numbers, no names). Then compare the same
   key on 2026-09-20 and 2026-09-22 (or the nearest qualified dates): present, absent, or duplicated.
2. Decide which is true, citing the evidence:
   - **GRAIN_FOUND:** a grain (the candidate plus one column) is unique on ALL 52 snapshots with that column never
     blank. Record per-snapshot rows `{master, dataset, date, unique, added_blank}`.
   - **UPSTREAM_DEFECT:** the 09-21 rows are a defect in the data. Name the defect (for example a duplicated
     custodian record, a split lot, a re-statement), the colliding row count per master, and the OWNER: the pipeline
     that writes `dim_position` silver, found from its repo writer, never guessed.
3. Write `GRAIN_R15.json` (`verdict`, `writes: 0`, and the fields the verdict needs) and a short `GRAIN_R15.md`.

## 2. BOUNDS

- Read only. No data, pipeline, schedule, quarantine or S3 object is written.
- Write ONLY your deliverables and one surprise row if needed.
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gr-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/gr2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)verdict (GRAIN_FOUND|UPSTREAM_DEFECT);.*writes 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: exactly one verdict, with the evidence it needs, and no writes.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-gr-2.grain-0921-collision.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. If it PASSes, append a `complete` status tag after the
order's last status line in the same commit. Report once: the verdict, the evidence, the literal AC output, commits and
rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 15 (addendum R3-T.8, item 4). It stands alone. Read-only by Andrew's 17:3xZ directive.
- Pre-cut 18:2xZ: `gr2.AC1` FAIL (record absent).

<status>pending</status>
<round>15</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
