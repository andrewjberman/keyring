# MDPF_CANON task order -- `CN-b-2` -- THE COMBINED SLICE'S WRITTEN BASIS (M7, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-b-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~5</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE a document and one ledger row; no IAM is read or changed.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r2_checks.py basis 0 of 3 at base (the file is absent; the ledger X2 row exists and does not cite it)
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-b-2` (round 2, decomposition v2)

Read `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` section 3 and `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and the DECISIONS first.

Write `deliverables/0.9.0_WK_MDPF_CANON~5/X2_GLOBAL_BASIS.md` (your serial folder; see AMENDMENT 1): why the combined all-firms (`global`) figure reveals nothing about any single firm's clients
(PRD DEC-7, FWD-3). It must have three headings:
1. **Aggregation level:** what one `global` figure sums over (firms, models, accounts), read from the producer code
   (`mdpf_gold_consolidator.py`'s global fold) with `path:line`.
2. **Minimum firm count:** the fewest firms any `global` figure combines, an integer, with its evidence. If any figure can combine fewer
   than 2 firms, say which and stop: file a row; do not write the basis.
3. **Why no per-firm or per-account row survives:** the fold's output shape, field by field.

Then add the basis file's path (the serial-folder path above) to the X2 row of `infra/logic/06_CONFORMANCE_LEDGER.md` as its citation. Do not change the row's
status: moving X2 from OWED to GRANTED is Andrew's later acknowledgement, not this cell's.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no IAM call, not even from a test (round 1's
   row D1-S4 is what a test write into a live bucket costs). A read-only `get`/`describe`/`head`/`list` is allowed. No install, no push.
   The issuer has CloudOps apply after the drain. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Every NEW address and name comes from the builders**: `lib/opal_naming.py` `address()`/`key()`/`name()` and the `../modules/opal_name`
   Terraform module, never a typed bucket, key or role name (PRD CONTRACTS; DEC-15; CLAUDE.md rule 30). A builder REFUSAL is a row.
4. **Never** (PRD DEC-14):
   - change the conformant compute chain's schedules or platinum's shape;
   - move `platinum/mdpf/global/`;
   - touch `opal-data-mdpf/code/scripts/gold/`;
   - add a second writer, a shadow prefix or a standing comparator;
   - move a served key.
5. **CLIENT DATA:** never print a client figure or account id.
6. Keep each file's line endings as you find them (read them first). No non-ASCII. Use the Edit tool for existing files.
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/logic/06_CONFORMANCE_LEDGER.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~5/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`, `infra/logic/06_CONFORMANCE_LEDGER.md`. The issuer's check `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-b-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py" basis; echo "exit=$?"</invocation><expect>ROUND 2 BASIS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-b-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-2 close (never self-graded): a reader asked why `global` did not move points at the paragraph; the minimum firm count is read from the producer, not asserted.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~5/MDPF_CANON.TO-CN-b-2.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-2 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W5-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-09 ~22:0xZ, row MDPF_CANON-D1-W5-S1):** the PRD names `deliverables/X2_GLOBAL_BASIS.md` at the deliverables root, which the owned-paths lane TREE_DELIVERABLES lets NOBODY write (deliverables/<SERIAL>/** only; the issuer probed it and was refused). The document lives in the author's serial folder; `r2_checks.py` reads that path (amended). The PRD's path wording goes to the CTO. Graded by no gate limb (a modification).

**ISSUER NOTES:** round 2 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` @409182ae5a section 3, items 2-4 (item 1 and item 5 are the issuer's read of the 2026-10-10 13:30Z
daily write, not cells). Base box/dell1. LF only.

<status>complete</status>
<round>2</round>
<to_id>MDPF_CANON.TO-CN-b-2</to_id>
<slot>~5</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
