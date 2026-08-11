# Session 0240-0301Z — crash recovery: L-B applied-truth read + L-C QA fire

**archetype:** MIXED (VALIDATE + COORDINATE)

## Context
Fabric crashed ~0200Z mid-MDPF-atomic-window (ledger `20260811T0150Z_mdpf-atomic-window.md`);
respawned by MSTR with a startup hint (024030Z): RP-W5b CLOSED (not re-run), sync with CTO
before touching leg state.

## Work
1. **Recovery mechanics:** /watcher armed (Monitor task ba0efo4le, TaskOutput->running, no
   orphan found pre-arm; predecessor PID 31532 read OFFLINE before register — dual-session
   discriminator applied). Startup A.1–A.3/B/D/E clean (PATH 96/97, forwarder exercised on
   output not rc). Zero crons.
2. **L-B leg-state read (the MSTR-ordered deliverable):** commit `9eff54d274` (mine, 015732Z,
   RP-W3 five-schedule ET->UTC cadence + RP-W4 step-i selectors) — APPLIED + LIVE-VERIFIED.
   Evidence: 7/7 live primitives match committed values (scheduler get-schedule x4, events
   describe-rule x1, both selector Inputs), and `terraform plan` on all 3 dirs shows ZERO diff
   on every cadence/selector resource — the apply's state write closed cleanly pre-crash.
   Reported to CTO (025405Z; independently corroborated by CTO's own read 025537Z), COO
   (025421Z; legs L-A+L-B CLOSED in ledger @13a4cecce8), MSTR (025427Z).
3. **Pre-existing drift surfaced (touched nothing):** mdpf `aws_s3_object.mdpf_route_bindings`
   content-sha (committed-but-never-deployed, MDPF_CANPLAT P2-1 in-flight);
   opal-assets `bd49f_reporting_io` declared-but-UNAPPLIED ReadTaxsmaRoster grant (Rule 22a
   class); smartx 3-lambda source_code_hash drift (vintage 07-16). CTO folded into finding log;
   targeted-apply binding (000333Z) stands on all 3 roots.
4. **Pre-crash debris committed:** RP-W3 TO status staged->pending @`3cf88872d0` (own author
   line, safe-commit -F). Status stays `pending` — acceptance bar is the 13:30Z unattended
   cycle, COO adjudicates.
5. **L-C fired on COO GO (025551Z):** `mdpf-gold-lambda` invoked in qa_local mode
   (CTO-ruled 015625Z instrument; full build, dry_run, ZERO S3 writes, fence intact) with
   qa_return_bodies. Read (item 1, mine): 49financial + inflection EMIT 3/3 each (6/12 A4);
   cottonwood SCOPE FAILED on the condition-1 guard — VALUE_DATE COLLISION WITH DIFFERENT
   DOLLARS at value_date=2026-08-06 (08-07 run $133,914,199.99 vs 08-08 run $139,213,957.62),
   refusal correct, never averaged; global fold SKIPPED honestly (I-1 pins require cottonwood).
   NOT a window failure — collision predates the window (open cottonwood-causation thread).
   ⚠ Surfaced to COO: the 13:30Z bar cycle reads the same data — 12/12 will fail on this
   pre-existing question absent resolution/adjudication (~10.5h runway). DS pointed at items
   2+3 (bodies at machine-local scratchpad path — deliberately uncommitted per the QA fence;
   log stream `2026/08/11/[$LATEST]31b81ca2a2a648528c3a5004c1e349fb`).

## Blockers
NONE at my seat. Held items are adjudications owned elsewhere: window close + bar reading
(COO), cottonwood data question (DS/COO), integrator push of the ~10 window commits + tags at
close (CTO-sequenced 025537Z: NOT unilateral, NOT before the bar).

## Next steps
- Event-driven: act on window-close coordination; cut the 3 pipeline tags with the integrator
  push at close (CTO 025537Z sequencing).
- Respond to DS items 2+3 verdicts if they need the invoker again (one fenced instrument,
  re-fireable).

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-pipescript | `deployed dim_mdpf_aggregate_aua_timeseries.py --pipeline mdpf` | MATCH (L-A precondition read; first attempt flagless -> rc=2 REFUSED as designed) |
| comp-pipescript | `deployed build_mdpf_spine.py --pipeline mdpf` | MATCH |
| comp-find | `mdpf_gold_consolidator` (infra/aws/lambda) | 1 hit w/ denominator (6456 files) — located handler source for the qa_local payload contract |
| (raw, rail-checked) | `aws scheduler get-schedule` x5 / `events describe-rule` / `list-targets-by-rule` / `logs get-log-events` | applied-truth + run-detail reads a TF-parsing comp-tool structurally cannot make (DESIRED vs APPLIED; single-invocation logs) |
| terraform | `plan -detailed-exitcode` x3 dirs | cadence/selector resources 0-diff; 3 pre-existing drift items enumerated + routed |
