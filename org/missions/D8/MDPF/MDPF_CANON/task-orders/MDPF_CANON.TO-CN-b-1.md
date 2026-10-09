# MDPF_CANON task order -- `CN-b-1` -- THE READER CENSUS (M1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-b-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~4</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE a read-only census; no IAM is read or changed by this cell.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r2_checks.py census 2 of 4 at base (SHAPE and SURFACES fail as expected -- the file is absent; EVIDENCE vacuous; PLANTED passes)
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-b-1` (round 2, decomposition v2)

Read `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` section 3 and `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (v2.9) CONTRACTS and the DECISIONS first.

Write `deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md` (your serial folder; see AMENDMENT 1): every reader and every writer of the four surfaces the PRD retires or repoints (PRD M1; brief
IV.2 and IV.3). The four surfaces are:
- the two legacy gold trees, `opal-data-assets/gold/mdpf_revamp/` and `opal-data-assets/portal/gold/mdpf/`;
- the stale served key `json/portfolios/aum-timeseries.json`;
- the old bronze `opal-data-mdpf/mdpf/bronze/`.

1. **The census is UNSCOPED and its denominator is printed.**
   - Use `comp-find` over the whole corpus (Terraform, `EC2_MANIFEST.json`, the producer scripts, the publisher, the portal source)
     for each surface's path strings and their variants (hyphen and underscore, with and without the bucket).
   - Put a `DENOMINATOR:` line near the top with the hit counts per surface and the files read.
   - The brief's IV.2 floor is 16 definitions and 50 config sites. Reconcile your count against it.
2. **One table**, with a header naming at least `reader`, `kind` (reader / writer / both / history), `evidence` (`path:line`, as many as
   needed, separated by `;`) and `verdict` (live / repointed-in-round-1 / history / excluded-with-reason). Give at least one row for
   each of the four surfaces.
3. **An `INSTRUMENT:` line** names the instrument behind each verdict. A name census proves presence, never absence: a surface with no
   reader found says which instrument saw nothing and what that instrument cannot see.
4. **Round 1 moved nothing yet.** The gold Lambda writes the new parquet BESIDE the legacy JSON, so a legacy writer is still live.
   Say so; do not mark it repointed.

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
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `docs/briefs/d8-mdpf-canon-migration-brief-20260913.md` (IV.2, IV.3), `infra/aws/ec2/EC2_MANIFEST.json`, `data/mdpf/scripts/gold/`, the publisher. The issuer's check `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-b-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py" census; echo "exit=$?"</invocation><expect>ROUND 2 CENSUS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-b-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-2 close (never self-graded): every live reader and writer an unscoped read finds is listed or excluded with a reason, the denominator reconciled against IV.2's floor, and the instrument named per verdict.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/MDPF_CANON.TO-CN-b-1.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-2 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W4-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-09 ~22:0xZ, row MDPF_CANON-D1-W5-S1):** the PRD names `deliverables/READER_CENSUS.md` at the deliverables root, which the owned-paths lane TREE_DELIVERABLES lets NOBODY write (deliverables/<SERIAL>/** only; the issuer probed it and was refused). The document lives in the author's serial folder; `r2_checks.py` reads that path (amended). The PRD's path wording goes to the CTO. Graded by no gate limb (a modification).

**ISSUER NOTES:** round 2 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round1.md` @409182ae5a section 3, items 2-4 (item 1 and item 5 are the issuer's read of the 2026-10-10 13:30Z
daily write, not cells). Base box/dell1. LF only.

<status>pending</status>
<round>2</round>
<to_id>MDPF_CANON.TO-CN-b-1</to_id>
<slot>~4</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
