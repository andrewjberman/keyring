# NFRA_OPALAI task order -- `OA-e-8` -- ROUND 2, E8: speed, real exchanges timed stage by stage (MEASURE ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~12</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only audit reads through the existing host role, if used; no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- a measurement; nothing is changed.
EGRESS CLASS, declared: reads on Opal's own plane only (the gateway, the host's audit trail).
</preflight>

## 1. THE CELL -- `OA-e-8` (round 2, decomposition section R2.1)

PRD C9 (`org/missions/D6/NFRA/NFRA_OPALAI/prd/NFRA_OPALAI_PRD.md`): speed is MEASURED, not asserted. FWD-3 (a routine
answer inside the conversation) is graded with the OPAL_ANALYST PRD's section-11 method
(`docs/architecture/OPAL_ANALYST_PRD.md`, section 11.1): real exchanges, two clocks, each stage timed with its own
instrument, compared with the 2026-08-20 baseline. **The baseline:** one exchange, question to answer 5m45s = 345 s; the
data layer 0.92 s.

The stages, as the baseline names them:

| Stage | What it spans |
|---|---|
| `A_DETECTION` | question posted, then the watch notices it |
| `B_WAKE` | the watch emits, then the agent's turn begins |
| `C_TURN_OVERHEAD` | the turn begins, then the first act |
| `D_RESEARCH` | classify, route, retrieve, extract |
| `E_COMPOSE_SEND` | compose, then the reply is created |

**Measure ONLY. The remedies are cut from what you find, not by you.** Use at least one REAL exchange: the item-0 close
run's exchange with the close run's named colleague (its artifact is in
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/`), plus any later real exchange the runtime served.
1. **Two clocks per exchange:** the question's and the reply's Graph `createdDateTime`. Read them through the gateway's
   `read_chat_messages` with the operator's token, as the parent watch's `read_chat()` does. Import
   `.claude/skills/teams-assist/teams-watch.py` BY PATH; it is LIVE production for the D7 intake runner, so never edit
   it, save it or run its `main()`.
2. **Per stage**, use the instrument that separates it and name that instrument:
   - the runtime watch's own emit and cursor timestamps in `Opal_Agent`'s `state_dir` (`C:\opal_runtime\state`);
   - the gateway's audit rows for the Analyst's `opal_asker_query` call in that window: the host audit trail, read-only
     over SSM on `i-07dccb1615503ac99`, or the S3 audit lake;
   - the runtime's thread-memory files.
   **A stage no instrument separates is recorded `{"unmeasured": "<reason>"}`.** The baseline itself left B_WAKE
   unmeasured. Never estimate a stage.
3. **Write** `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~12/E8_SPEED_STAGES.json`:
   - `method`: the section-11.1 citation;
   - `baseline`: `{"source": "docs/architecture/OPAL_ANALYST_PRD.md", "total_seconds": 345, "data_layer_seconds": 0.92}`;
   - `exchanges`: a list of `{chat_id, question_created, answer_created, total_seconds, stages: {A_DETECTION, B_WAKE,
     C_TURN_OVERHEAD, D_RESEARCH, E_COMPOSE_SEND}}`. Each stage is `{seconds, instrument}` or `{unmeasured}`.
   Persist no message text and no token.

## 2. BOUNDS

1. Read-only everywhere: no edit to the runtime, the watch, the gateway or any account; no deploy.
2. Standing: no push, no install. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~12/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `docs/architecture/OPAL_ANALYST_PRD.md`, `.claude/skills/teams-assist/teams-watch.py`,
`C:\opal_runtime\state\`, the close-run artifact.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W12-S<k>`
(next free k for W12).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the measurement file is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-8"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e8.AC1.sh; echo "exit=$?"</invocation><expect>exchanges>=1, well-formed = exchanges (total = the two Graph clocks +-1 s; 5 stages present; measured>=3 of 5; measured sum <= total+2 s) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-8"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e8.AC2.sh; echo "exit=$?"</invocation><expect>file baseline=[docs/architecture/OPAL_ANALYST_PRD.md 345 0.92]; source s.11.1 lines with 5m45s>=1, with 0.92s>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~12/NFRA_OPALAI.TO-OA-e-8.speed-stage-measure.proof_of_spec.json`.
Report once: the stage table per exchange beside the baseline, each instrument named, what stayed unmeasured and why,
and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E8 (FWD-3, S9). The stage names follow the section-11.1 baseline table (A-E), which C9 points at. The
decomposition's shorter phrasing (posted, noticed, asker query, reply sent) maps onto A, D and E. AC1's floor of 3 of 5
measured stages is the issuer's choice. The baseline measured 4 of 5.

**Dry-run at base** (main tree, CLOUD `7cb7c7f33d`):
- e8.AC1 base: FAIL as expected (the file is absent).
- e8.AC2 base: FAIL as expected (the file is absent).

Checker arms were exercised with a synthetic file, then removed:
- GREEN: AC1 PASS (90 s against the clocks, 3 of 5 measured). AC2 PASS: the section-11.1 bytes at HEAD carry `5m45s`
  and `0.92s`.
- RED: AC1 FAIL when the total disagrees with the clocks.

**SPAWN ONLY WHEN** the item-0 close run is done and its artifact is committed under
`deliverables/2.0.0_SA_COO~AI/round2/`. The slot continues here after OA-t-1.

<status>pending</status>
<round>2</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
