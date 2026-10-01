# AMGT_RESAPP task order -- `AMGT-zz-8` -- THE ONE BUILD: NAMES, PLACES MOVED, THE DRIVER CHART, AND THE TIMELINE RIDER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN by the issuer at the cut -- 3 simulate calls on opal-amgt-scoped-api-role (APPLIED plane): s3:GetObject opal-data-harvest/crosswalk/v1/2026-09-29.json ALLOWED; s3:ListBucket opal-data-harvest NOT-DECIDABLE (prefix-conditioned, not a deny); the ranking-table Query NOT-DECIDABLE (resource ARN not confirmed). Coverage beside it: the deployed function's own reads at the cut returned 66 ranking rows and ASML's /thesis (zz_8_served), so the reads are exercised live. BLIND: the ASML analysis rewrite runs under the executor's credentials, which were not simulated; the plan must show NO IAM change.
comp-adversary: RUN by the issuer at the cut -- AC1-AC3 read the deployed function for each served move, each FAILING at the base; AC4 is the rider's body control (PASS at the base, 4 of 4).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-zz-8` (round 51, decomposition s.59)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` carrying `AMGT-zz-5` (lead-list `name` /
`name_source` / `places_moved`), `AMGT-zz-6`'s verification fix, `AMGT-zz-1`'s `write_pool` change (packaged, not on the served path)
and `AMGT-zz-4`'s regenerated `_harvest_prefixes.py`; AND the NAMED, NON-INERT rider AMGT_HARVST n-6 (`timeline_api.py`'s
`/timeline/day` read path, drained @`150b717373`: latency expected to move, bodies byte-equal); AND rewrite ASML's stored analysis
through `analyze.reverify_stored_thesis_driver("ASML_NA_Equity", "000162828026011378")` (committed code, `dry_run=False`).

**Begin only when all four hold:** zz-1, zz-4, zz-5 and zz-6 are `complete` and merged (the issuer's GO names the build commit); both
halves are committed -- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/NEVER_WIDEN_HALF_COO_ZZ8.md` and
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND51_ZZ8_CTO_HALF.md`; and **the base CodeSha256 the halves name
(`pVa+sgzj8XNZ9uvJqCOwRNCJn0IZhUklnWZh6JbO7B0=`) is still the live one, re-read immediately before the build -- a moved base is a STOP
and a re-sign.** **The acts, in order, under the entry opened AND COMMITTED before the build** (sentinel + entry): (1) the pre-apply
captures the halves name; (2) build + upload the ONE artifact at the GO commit (record the prior VersionId); the build now prints
`CONTENT-DIFF` lines and a `CONTENT-DIFF SUMMARY` against the deployed artifact -- save that printout to your deliverables and STOP if
a CHANGED/ADDED/REMOVED file is outside the halves' list; then ONE `safe-apply` -- print the plan first; code only; (3) the ASML
rewrite; (4) verify with the four criteria; close the entry. A criterion failing after the act is the ROLLBACK trigger named in the
halves.

## 2. BOUNDS

1. The act and nothing else. A plan beyond the function's code, a packaged file outside the halves' list, or a gate refusal is a
   REFUSAL. One object write only (ASML's analysis); no other name is rewritten.
2. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_8_served.py --what rows; echo "exit=$?"</invocation><expect>served rows R; named N (N &gt; 16), each with name_source; places_moved int &gt;= 1, every null with a reason; THE SERVED LEAD-LIST ROWS CARRY NAMES AND PLACES MOVED: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_8_served.py --what chart; echo "exit=$?"</invocation><expect>ASML chart SERVED source 'filing' points &gt;= 2; THE SERVED DRIVER CHART READS THE FILING'S VERIFIED POINTS: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-zz-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_8_timeline.py; echo "exit=$?"</invocation><expect>OLD == DEPLOYED byte-equal on 4 of 4 days, REPORT ms printed per day; THE TIMELINE DAY BODY DID NOT MOVE ON THE DEPLOYED FUNCTION: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-zz-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_8_served.py --what code; echo "exit=$?"</invocation><expect>deployed CodeSha256 differs from pVa+sgzj8XNZ9uvJqCOwRNCJn0IZhUklnWZh6JbO7B0= and LastUpdateStatus Successful; THE ONE BUILD LANDED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

A fourth criterion, reason: the one act carries two served moves and a named rider, and each keeps its own served read; AC4 is the
landing itself.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-zz-8.the-one-build.proof_of_spec.json`. Report once: the content-diff summary, the prior and new VersionId and CodeSha, ASML's rewrite receipt, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis enrichment item 8; the rider per CTO msg 26878 (HARVST round-24 ruling 1). Cell 3 is NOT carried
(row Z-S309). Base: AC1 FAIL (16 of 66 named, no name_source/places_moved); AC2 FAIL (ASML ABSENT); AC3 PASS 4 of 4 (the rider's
body control -- the deployed function still runs the OLD path); AC4 FAIL (CodeSha = pVa+sgzj). The COO half is written after
zz-1/4/5/6 land, against the landed code, zz-4's content-diff printout on a --build-only of the GO commit, and the then-live base.

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-30 ~05:5xZ):** landed; entry `amgt-resapp-zz8-one-build-20260930` CLOSED 4 of 4 legs 05:42:24Z (@40be138834), instance VALID rc=0 (@e290cafc73). The issuer re-measured on the served plane at `zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=`: AC1 PASS (66 rows, 18 named, 66 places_moved int); AC3 PASS (4 of 4 days byte-equal; the rider's latency moved 3.5x-27.6x per AE~A); AC4 PASS; **AC2 FAIL** ('ASML chart ABSENT', before and after the act). AC2's premise was the issuer's cut defect (rows Z-S311 by AE~A, Z-S312 the issuer's attribution): the served chart reads the D-1 drafting document's embedded driver, which the rewrite does not regenerate. **CTO msg 26943 (@fdd0074be3): the rollback trigger is WAIVED for AC2 only; the ASML rewrite is kept; round 52 cuts the D-1 regeneration under its own pair.** Limbs 1-7 hold. Closed on the waiver, AC2 carried to round 52, not graded met.
<status>complete</status>
<round>51</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
