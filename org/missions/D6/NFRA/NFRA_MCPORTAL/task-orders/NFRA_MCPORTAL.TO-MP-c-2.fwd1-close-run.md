# NFRA_MCPORTAL task order -- `MP-c-2` -- ROUND 5, R-15 (MP-c-1 re-cut UNCHANGED): the FWD-1 close run -- one colleague narrowed, answered within the limit, widened back

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-c-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-c-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one close run; no cron, alarm, monitor or cadence.
comp-iam: RUN by AC2 (the gateway role's `sts:AssumeRole` on the operator role, read live from the gateway host).
comp-adversary: DECLARED-NOT-APPLICABLE -- A1n's refusal arms are the adversary read.
EGRESS CLASS, declared: none beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `MP-c-2` (round 5, decomposition section R5.1; the re-cut of round 3's MP-c-1)

PRD acceptance A1 (FWD-1): *one colleague's data grant narrowed from the Entitlements tab; their next MCP call answered
within the new limit and no wider; widened back; both writes in Recent Changes with before and after.* And A1n: *each
refused before any store call: a write reaching the writer with no owner header; with a valid header for a non-owner;
with an owner header past the window; and a direct `sts:AssumeRole` from the gateway role on the operator role.*

Andrew has ALREADY done the human half before this order was spawned: he narrowed the colleague's grant from the
dashboard, the colleague asked a real question, he widened it back, and the colleague asked again. The issuer wrote
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/c1_run.json` with `t0`, `t1`,
`principal_sha256` (sha256 of `"<tid>/<oid>"`), and `raw_dir`, an OFF-repo folder holding the colleague's raw
exchanges.

**Your work:**
1. **The transcript.** From `raw_dir`, write
   `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/c1_transcript.md`: the BEFORE-narrow,
   AFTER-narrow and AFTER-widen exchanges, in that order. Keep each question and each answer's SHAPE (which fields, how
   many rows, any error or refusal text, verbatim). REDACT every value the grant covers (account numbers, holdings,
   balances, names of clients) as `<REDACTED:kind>`, and write NO email or person's identifier. At the top, state what
   the narrowing changed (the scope `before` -> `after` from the writer's table items, the scope keys only).
2. **The two writes.** AC1 reads them from the writer's table. In your report, name the two items' `when` and
   `action`, never the `who` field. That field is row Z-S10's subject, and you must not copy it anywhere.
3. **A1n's live-reachable arms.** AC2 invokes the deployed writer with no owner header, and from the gateway host
   tries `sts assume-role` on `opal-gateway-access-admin`. Arms (ii), a valid non-owner header, and (iii), an owner
   header past `exp`, need an ALB-signed header no seat can mint. They stand on the writer's in-package tests in
   `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/`: run them once, and cite the test names and the
   pass line in your report.

## 2. BOUNDS

1. Read-only against the world except AC2's single no-header invoke (a REFUSED record). No grant write, no revert, no
   invoke with any header.
2. Nothing from `raw_dir` is committed unredacted, and `raw_dir` itself is never copied into the repo.
3. Standing: no push and no vendor call. REFUSE a criterion you cannot meet as written, with its measurement. Never
   repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `raw_dir` (from `c1_run.json`), `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W1-S<k>` (the next free k for W1).

## 4. PROOF OF SPEC (literal; run from your worktree root after the transcript is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-c-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/c1.AC1.sh; echo "exit=$?"</invocation><expect>colleague WRITTEN in window>=2; sequence has narrow then widen; before+after on all=True; verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-c-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/c1.AC2.sh; echo "exit=$?"</invocation><expect>arm (i) no header -> REFUSED NO-OWNER-HEADER; arm (iv) ssm status=Success, AccessDenied, denied=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-c-2" judgment="true"/>
</proof_of_spec>

AC3 (JUDGMENT, WORLD, graded by the project's CVO (`3.0.0_SA_CVO~O`, or its stand-in `3.0.0_SA_CVO~Z`) at L9, never self-graded; record it in the instance as
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO): from the committed `c1_transcript.md`, the narrowed
answer is a REAL answer confined to the new grant, not an error, an empty result, or a refusal that happens to pass the
mechanical check; and the widened-back answer matches the original.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-c-2.fwd1-close-run.proof_of_spec.json`.
Report once, with:
- the two writes' `when` and `action`;
- the transcript path;
- A1n's four arms (two live, two by test name);
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** R-15 of ROUND_ANALYSIS.round4.md @460bc0af2f: round 3's MP-c-1 re-cut UNCHANGED, after MP-c-1 was
superseded @39ea2d5e3e to clear the project-grain L10. It uses the same checks (`round3/checks/c1.AC1.sh`, `c1.AC2.sh`) and
the same slot `~1`. The only text changes are the ids and the CVO naming the stand-in.

SPAWN ONLY when **G-CLOSE** holds:
- gateway r29 is live;
- Andrew's hold is lifted (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_200xZ_OPLGTW_THREE_CALLS_RECS_APPROVED_ROUND32_FWD10_13_ALYSSA_HOLD.md`,
  which names r29 and nothing more);
- Andrew's sitting with Alyssa is done (narrow, she asks, widen, she asks);
- the issuer has written `c1_run.json`.
The staging plan is `deliverables/2.0.0_SA_COO~MP/round3/G-CLOSE_STAGING_ALYSSA_20261001.md` @154894312f.

<status>cancelled -- Andrew-direct 2026-10-19 ~16:3xZ, the human half is no longer owed (org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_163xZ_SIX_HANGING_OPEN_CALLS_RESOLVED.md); the ACs read files the human half would have written and cannot run as written. CTO ruling 1.0.0_SA_CTO~Z msg 36018 (YES, cancel citing the record). FWD grading is the CVO's on the evidence the project holds; no replacement human act is cut.</status>
<round>5</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
