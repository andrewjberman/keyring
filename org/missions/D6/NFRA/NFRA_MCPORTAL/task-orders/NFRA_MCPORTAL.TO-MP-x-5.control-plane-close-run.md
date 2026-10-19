# NFRA_MCPORTAL task order -- `MP-x-5` -- ROUND 5, E3: the FWD-14 close run -- Andrew names one box's projects from the page alone

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-x-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-x-5</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~5</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one close run; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only; the store read is the gateway's own grant, applied by MP-x-3.
comp-adversary: DECLARED-NOT-APPLICABLE -- the JUDGMENT criterion compares Andrew's words with the store at the same minute.
EGRESS CLASS, declared: none beyond Opal's own AWS (S3 read, SSM).
</preflight>

## 1. THE CELL -- `MP-x-5` (round 5, decomposition section R5.1; analysis R-14)

FWD-14: *Andrew opens the control-plane page and sees, without asking any seat, which box is working on what right now.*
DONE WHEN: *EXERCISED -- Andrew names one box's projects this afternoon from the page alone.* A14: *one box's projects named
from the page and matched to the store; a not-reporting box reads so.*

Andrew has ALREADY done the human half before this order was spawned. He opened `https://mcp.opalinvest.dev/control-plane`
and named one box and its projects. The issuer recorded his words and the time in
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~5/x5_seen.json`:
`{"seen_at": ISO-UTC, "box": "...", "projects": [...], "hours": N, "words": "<his sentence>"}`.

**Your work:**
1. **The window file.** Write `deliverables/0.9.0_WK_NFRA_MCPORTAL~5/x5_run.json` =
   `{"t0": seen_at minus 10 min, "t1": seen_at plus 5 min, "box": ..., "projects": [...]}`, copying box and projects from
   `x5_seen.json` exactly.
2. **The store at that minute.** Run `python .tools/fabric-activity.py boxes --hours <N>` and `who` for the named box, as
   close to `seen_at` as the store allows. Record in `deliverables/0.9.0_WK_NFRA_MCPORTAL~5/x5_store.md`:
   - for the named box, its commits, seats and projects in the window ending at `seen_at`;
   - every roster box's status;
   - the read time and the records scanned.
   Put each count beside its denominator. Name no person and copy no commit subject.
3. **The not-reporting arm.** In `x5_store.md`, state which roster box, if any, had no record in the window. Record whether
   the page's "not reporting" for it is the true state, from the store's own listing of `box=<name>/` for those days.

## 2. BOUNDS

1. Read-only. No write to the store, no gateway call beyond what AC1 reads, and no message to anyone.
2. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~5/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/fabric-activity.py`, `infra/aws/ec2/opal-gateway/app/admin_fabric.py`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W5-S<k>` (the next free k for W5). `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`. Rows are
append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after `x5_run.json` and `x5_store.md` are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-x-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/x5.AC1.sh; echo "exit=$?"</invocation><expect>ssm status=Success; fabric/boxes 200s in window>=1; run file box named, projects named>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-x-5" judgment="true"/>
</proof_of_spec>

AC2 is the JUDGMENT criterion (WORLD), graded by the project's CVO at L9 and never self-graded. Record it in the instance as
`UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming the CVO. The question: from `x5_seen.json` and `x5_store.md`,
do the box and projects Andrew named match the store's read for that minute, and does a box with no record read
"not reporting" on the page?

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~5/NFRA_MCPORTAL.TO-MP-x-5.control-plane-close-run.proof_of_spec.json`.
Report once, with:
- the window;
- the named box and projects;
- the store's figures for them;
- the not-reporting arm;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E3 of ROUND_ANALYSIS.round4.md @460bc0af2f (R-14). It is the round's plausibility oracle and its only
JUDGMENT criterion. Check dry-run at base: AC1 FAILS (no window file).

**SPAWN ONLY when G-SEE holds:**
- MP-x-4 has drained with AC3 PASS;
- the issuer has carded Andrew ONCE;
- Andrew has opened the page and named one box's projects;
- the issuer has written `x5_seen.json` with his words and the time.

<status>cancelled -- Andrew-direct 2026-10-16 ~18:5xZ closed its call 21c5 ("we can close the name one box projects i see those displaying cleanly", org/tier1_exec/2.0.0_SA_COO~MP/deliverables/ANDREW_DIRECT_20261016_185xZ_CLOSE_21C5_21D9_44EB_GATEWAY_READS_WELL.md); the AC reads x5_seen.json, which needs a named box and its projects that his words do not carry, and the issuer will not invent them. Same route as MP-q-1/v-2/c-2 (CTO~Z msg 36018, YES). FWD-14 is graded by the CVO on the evidence in org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/EVIDENCE_FOR_CVO_FWD_1_2_15_16_17_20261019.md section FWD-14; no replacement human act is cut.</status>
<round>5</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
