# TO NFRA_TRNSPT.TO-TR-r4 -- the transcripts route and gate G-TEAMS-TX, measured from the record

<to_id>NFRA_TRNSPT.TO-TR-r4</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-r-4` (`decompositions/NFRA_TRNSPT_DECOMP_R4.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-r-4` (CTO round-3 analysis @c2b5eb89a4, section 4, T1): "The transcripts route, measured (FWD-1 hops 1-2). From NFRA_OPLGTW's
release record and gate G-TEAMS-TX: is `/hx/transcripts` released, and does Andrew's tenant setting allow attributed transcripts.
(1) one record naming route state (released at a commit, or not) and G-TEAMS-TX state, each with its source line; no gateway call
from dell2."

**Where the record lives (read-only; start here, newest first):**
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md`
- `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-tx-2.transcript-reach-live.md` and `...TO-OG-tx-1.transcript-tools.md`
- `org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md`, the project's PRD under `org/missions/D9/NFRA/NFRA_OPLGTW/prd/`,
  its surprise channel, and its `deliverables/`
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-4_HALF_20261003.md`, `cvoO_NFRA_OPLGTW_PRD_v1.7_RATIFIED_TEXT_REVIEW_20261003.md`
- `org/tier1_exec/2.0.0_SA_COO~O/logs/2026-10-02/og-rl-3_hx_teams_release_1723-1958Z.md`
- `infra/aws/ec2/opal-gateway/app/server.py` (the route's code; code present is NOT released -- a release names a deployed commit)
- Use `Grep` for `G-TEAMS-TX` and `hx/transcripts` across `org/` and `infra/aws/ec2/opal-gateway/` for anything newer. The latest
  dated record decides; say which you took and why.

**Build:** write `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R4_TRANSCRIPTS_ROUTE_RECORD.md` containing,
each on its own line, exactly:

```
ROUTE: released@<deployed commit hash> SOURCE: <repo-relative path>:<line>
   or
ROUTE: not-released SOURCE: <repo-relative path>:<line>
G-TEAMS-TX: <one-token state as the record names it, e.g. OPEN | CLOSED | PENDING-ANDREW> SOURCE: <repo-relative path>:<line>
```

then a short paragraph per line: the cited line's text quoted, its date, any newer record that disagrees, and whether Andrew's tenant
setting for attributed transcripts is named anywhere (cite it, or write `tenant setting: NOT FOUND in the record`). The SOURCE line
must be the line that states the fact. Print the bytes at the cited line to confirm before you write it.

### ACCEPTANCE

<criterion id="TR4-r4-AC1" cell_refs="TR-r-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R4_CHECKS/r4_checks.py r4-record</invocation><expect>R4-R4-RECORD-OK</expect></criterion>
`TR4-r4-AC1` -- the record names both states, each with a `path:line` source that exists in the tree.

<expected_criteria>TR4-r4-AC1</expected_criteria>

Dry-run at the base (CLOUD b6a856bfb9): AC1 `R4-R4-RECORD-FAIL absent` -- FAIL as expected. Whether the cited line SAYS what the record
claims is graded by 3.0.0_SA_CVO at the compile, not by this check.

## BOUNDS

- **Grant.** Your deliverables folder, this order's file and the investigation file. Nothing else is written.
- **LOCAL, READ-ONLY.** No gateway call, no HTTP request, no AWS call. The repo record only.
- **Refusal clause.** If the record does not settle a state, write the line with the state the record DOES show and cite it, and file a
  surprise row (id `NFRA_TRNSPT-W1-S<k>`, next unused) naming what is missing; never invent a state.

<paths>
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ and
never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R4.md</decomp_doc> (round 4), cell `TR-r-4`.
<owned_cells>TR-r-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR4-r4-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-r4.transcripts-route-record.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR4-r4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two lines, the record you chose for each and why, the tenant-setting finding, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only record.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no write outside deliverables.
comp-adversary: RUN -- 30 files carry G-TEAMS-TX or hx/transcripts (native Grep, limit 30 reached, so more may exist; BLIND beyond those 30); "code present" vs "released" is the trap; the face names it and the CVO grades the citation.
lane: deliverables + investigation only.
</preflight>

Source: CTO round-3 analysis @c2b5eb89a4 section 4 T1; decomposition round 4 cell TR-r-4.
