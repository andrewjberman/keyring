# MDPF_HEALGAP -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_HEALGAP-W<n>-S<k>`; seat rows `MDPF_HEALGAP-S<k>`.

```json
[
  {
    "id": "MDPF_HEALGAP-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T08:34:00Z",
    "one_line": "FWD-3 asks for the eleven missing model_detail days 2026-08-31..09-10 to be repaired by one act, but the runner sends Black Diamond no as-of date: a --date repair would land TODAY's model composition under those eleven dates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py @c21432885a: ingest() (lines 400-458) uses `date` only to build landing keys; the vendor calls are POST /api/models/strategies/search and POST /api/accounts/search with body {skip,take,sort,searchString} (line 231) and GET /api/models/{id} (line 313), none carrying a date",
        "the brief's own control (PART VI.3): the 2026-09-01T02:50Z one-shot re-run for 2026-08-31 landed models and accounts, i.e. current-state pages written under a past date"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-3: the eleven missing days of 2026-08-31 to 2026-09-10 repaired by one act; afterwards exactly those are present. ACT 2: the word is asked for only when the hop-0 read predicts that the repair will fill the days.",
    "world_is": "The Rebalancer endpoints the runner uses return current state only (no as-of parameter is sent, and none is known to exist). A repair can fill the eleven keys, but with 2026-10-xx compositions, not the compositions in force on those days. Whether any endpoint serves historical composition is unread. The disclosure ACT 2 owes Andrew changes from 'may return empty' to 'would fill the days with the wrong-dated composition unless a historical source exists'. Not a round-1 act (FWD-3 is enrichment 2); no vendor call made."
  },
  {
    "id": "MDPF_HEALGAP-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T08:34:00Z",
    "one_line": "Hop 0's cause read is answered in the repo, not unread: the count-reconcile self-gate raised between accounts and model_detail on 2026-08-31..09-10, fixed by c53e48f7fb and deployed 2026-09-11T03:26Z; the runner's log group keeps only 14 days, so the original failure lines are gone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda_function.py _reconcile_counts docstring (lines 337-363) at HEAD; git log c53e48f7fb 2026-09-10 22:17 -0400 'a count mismatch is DISCLOSED, not fatal -- one closed account froze the Cottonwood model chain for 11 days'",
        "aws lambda get-function cot-rebalancer-runner 2026-10-07: LastModified 2026-09-11T03:26:00Z",
        "aws s3api list-objects-v2 opal-data-assets blackdiamond/cottonwood/meta/2026-09-0 -> no complete-stamp; meta/2026-10-01..07-complete.json present, each ~06:01Z",
        "aws logs describe-log-groups /aws/lambda/cot-rebalancer-runner: retentionInDays 14; filter-log-events 2026-09-05T05:50Z+1h returns nothing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD section 2 hop 0 and brief PART VII.1: why rebalancer_model_detail stopped 2026-09-01..09-10 while its siblings landed is UNREAD and must be read before building.",
    "world_is": "It is a second cause class (a vendor-maintained counter treated as a fail-closed gate), already closed in code and deployed. Its primary evidence (the runner's log) has aged out at 14 days, which also bounds FWD-2: 'read from the run's own result' cannot mean the CloudWatch log for anything older than two weeks."
  },
  {
    "id": "MDPF_HEALGAP-W1-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~1",
    "surfaced_at": "2026-10-07T08:56:59Z",
    "one_line": "The commit gate refuses every commit of lambda_function.py on this device: installed ruff is 0.16.10, the gate pins 0.15.11, and 0.16.10's default rule set raises 30 errors on the untouched base file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m ruff --version -> ruff 0.16.10; .tools/commit-gate.sh line 46 pins 0.15.11; `ruff check --target-version py39 --extend-select FA` on the base lambda_function.py (git show 474ec88e5a) -> Found 30 errors (UP031, I001, UP037, BLE001); the same call with ruff 0.15.11 -> All checks passed.",
        "Worker workaround, uncommitted: ruff 0.15.11 wheel unpacked under .scratch/ruff1511 and a PYTHONPATH shim .scratch/shim/ruff/__main__.py exec-ing it; commit 8af853ce59 landed through the unchanged gate on that shim. Also: no git committer identity on this device, supplied by GIT_COMMITTER_NAME/EMAIL env only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-HG-t1 commit step: safe-commit.sh runs the commit-gate (py_compile + ds-precommit + ruff py39) and a conforming edit passes.",
    "world_is": "Any worker commit of a .py file with the device's ruff 0.16.10 is blocked regardless of the edit (--force does not bypass). Sibling HG-t-2 edits the same file and meets the same block unless it carries the shim or the install is repaired.",
    "notes": "Not fixed here: the gate and the installed ruff are outside this order's write grant."
  },
  {
    "id": "MDPF_HEALGAP-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T09:12:00Z",
    "one_line": "Disarms MDPF_HEALGAP-W1-S1 (owner 2.0.0_SA_COO~G1): the ruff drift has no live effect on round 1, the box-wide repair is routed to 0.0.0_AB_MSTR~DELL1, and the worker's ruff 0.15.11 wheel has an unread provenance.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Round 1 has one more .py write: none. HG-t-2's <paths> is a .tf file only (task-orders/MDPF_HEALGAP.TO-HG-t2...md), so W1-S1's 'sibling HG-t-2 edits the same file' does not hold.",
        "HG-t-1 drained through safe-merge.sh at ca914096d7 (merge commits are not re-graded by ruff); the shim lives only in /c/tmp/wk-healgap-1/.scratch, uncommitted, and no gate file changed.",
        "python -m ruff --version -> 0.16.10 on dell1; .tools/commit-gate.sh:46 pins 0.15.11 (read 2026-10-07).",
        "/c/tmp/wk-healgap-1/.scratch/ruffwhl held ~11.5 MB at 08:53Z and ruff1511/ruff-0.15.11.dist-info was unpacked from it; whether the wheel came from the local pip cache or from PyPI is UNREAD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W1-S1: ARMED, disarm owner 2.0.0_SA_COO~G1; any worker .py commit on dell1 is refused and HG-t-2 meets the same block.",
    "world_is": "Disarmed for this project: no remaining round-1 order writes Python, and the issuer cuts no further .py order on dell1 that relies on a worker-fetched shim. The device repair (installed ruff matching the gate's 0.15.11 pin) is the box integrator's and is routed to 0.0.0_AB_MSTR~DELL1. If the wheel was fetched from PyPI it was package egress after 1.0.0_SA_CTO~DELL1 msg 71 noted that a PyPI install needs Andrew's egress word; that read is the CVO's to adjudicate."
  }
]
```
