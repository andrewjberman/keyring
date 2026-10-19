# NFRA_MCPORTAL task order -- `MP-q-1` -- WORKSTREAM CP2 ROUND 1: the close run for FWD-15..17 (STAGED on G-SEE2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-q-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-q-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~12</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time read of what Andrew did; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (S3 GetObject of three records, the gateway's access log over SSM).
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1 reads the server's log and the box's own records, never the page's claim.
EGRESS CLASS, declared: none beyond AWS reads in Opal's own account.
</preflight>

## 1. THE CELL -- `MP-q-1` (workstream CP2 round 1, decomposition sections CP2.1 and CP2.6)

The three outcomes being closed, from the PRD:
- **FWD-15:** *Andrew sees where two or more boxes are on the same surface, rated by risk.* DONE WHEN: *one real overlap
  read on the page and checked against the store.*
- **FWD-16:** *Andrew sees each box's git state.* DONE WHEN: *one box whose work is not on the trunk is seen as such the
  same day.*
- **FWD-17:** *Andrew reads every open call on every box and closes one with his ruling from the page.* DONE WHEN: *one
  real call closed from the page.* A17: *one call closed from the page and read back from that box's list.*

Andrew has ALREADY done the human half before this order was spawned. He opened `https://mcp.opalinvest.dev/control-plane`
and `/open-calls`, read one overlap and one box's git state, and closed one OPEN call with his ruling. The issuer recorded
his words and the times in `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~12/q1_seen.json`:
```
{"seen_at": ISO-UTC, "overlap_surface": "<key>", "gitstate_box": "<box>", "gitstate_state": "<state>",
 "closed": {"box": "<box>", "call_id": "<id>", "request_id": "<rid>", "at": ISO-UTC}, "words": "<his sentences>"}
```

**Your work:**
1. **The run file.** Write `deliverables/0.9.0_WK_NFRA_MCPORTAL~12/q1_run.json` =
   `{"t0": the earlier of seen_at and closed.at, minus 10 min, "t1": the later plus 5 min, "box": closed.box,
   "call_id": closed.call_id, "request_id": closed.request_id, "overlap_surface": ..., "gitstate_box": ...}`. Copy every
   value from `q1_seen.json` exactly.
2. **Wait for the box to apply the close.** The box's scan runs about every 10 minutes. Read
   `s3://opal-313476888478-globgrph/fabric/open-calls/v1/box=<box>/request_results/<request_id>.json` with `.tools/aws s3
   cp`, at most once every 2 minutes, for at most 40 minutes.
   - If it never appears, record that, run AC1 anyway, and report: the FAIL is the finding.
3. **The store, for the other two outcomes.** Record in `deliverables/0.9.0_WK_NFRA_MCPORTAL~12/q1_store.md`:
   - **FWD-15:** the overlap surface's records in the activity store for the window ending at `seen_at`. Run `python
     .tools/fabric-activity.py overlap --hours 6 --all` and quote its line for that surface. Then state whether an open
     deploy on any box's `open_deploys.json` names it.
   - **FWD-16:** the named box's `gitstate/box=<box>/latest.json` at the nearest record to `seen_at` (its `at`, the
     counts, `behind_trunk`). State whether the page's state matches the rule: unpushed > 0 means "committed, not
     pushed"; else pushed-not-on-trunk > 0 means "pushed, not on trunk"; else "on trunk".
   - **FWD-17:** the result object, and the call's row in that box's `open_calls.json` after the close.

   Put each count beside its denominator. Name no person beyond Andrew and copy no commit subject.

## 2. BOUNDS

1. Read-only. No write to any store, no gateway call beyond what AC1 reads, and no message to anyone.
2. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~12/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/fabric-activity.py`, `.tools/open-calls-scan.py`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W12-S<k>` (the next free k for W12). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after `q1_run.json` and `q1_store.md` are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-q-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/q1.AC1.sh; echo "exit=$?"</invocation><expect>ssm status=Success; close POST 202s in window>=1; result state=APPLIED; call state=CLOSED -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-q-1" judgment="true"/>
</proof_of_spec>

AC2 is the JUDGMENT criterion, graded at L9 by the CVO and never by you. Did Andrew read a real overlap, a real off-trunk
box and close a real call from the page alone, with each matching the store? Record it in your instance as
`UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~12/NFRA_MCPORTAL.TO-MP-q-1.cp2-close-run.proof_of_spec.json`.
Report once, with:
- the AC1 output;
- `q1_store.md`'s three findings;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the CP2 issuance (decomposition v6). G-SEE2: MP-r-2 drained, then the issuer cards Andrew ONCE
and writes `q1_seen.json` from his words before the spawn. Check dry-run at base 2851a9190d: AC1 FAIL (no run file). The
negative arm is in the check: a request with no result reads `UNREAD:` and fails. Slot `~12` is spawned only at G-SEE2.

<status>cancelled -- Andrew-direct 2026-10-19 ~16:3xZ, the human half is no longer owed (org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_163xZ_SIX_HANGING_OPEN_CALLS_RESOLVED.md); the ACs read files the human half would have written and cannot run as written. CTO ruling 1.0.0_SA_CTO~Z msg 36018 (YES, cancel citing the record). FWD grading is the CVO's on the evidence the project holds; no replacement human act is cut.</status>
<round>1</round>
<workstream>CP2</workstream>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
