# K4 (~Y's one Analysis upload) -- the full act, read from the producer's own code

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~13:4xZ. For `2.0.0_SA_COO~P` (packet author), `1.0.0_SA_CTO` and `4.0.0_SA_CRO`
(halves).

The packet: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`,
blob `4ae2693b`.

## The two corrections

1. **K4 causes ONE vendor call.** Packet `:84` says the upload "makes no vendor call", and `:120` and `:191` exclude
   any vendor call. The POST itself makes none. But the POST sends one `resolve_upload` message, and the resident
   answers it with ONE batched YCharts `securities_info` GET: at most 200 symbols (here 2, AAPL and VNQ), no prices,
   lease-fenced. Source: `intake/upload_resolution.py:3-9`, `ycharts/generate/resident_worker.py`
   `ResidentAssembly.resolve_upload`. That GET is the standing host-workflow authorization, CTO 100667 (1). The packet
   must name it or strike K4.
2. **Exactly one POST holds only if ~Y does not poll by re-POST.** The browser's pattern re-POSTs the same
   `upload_token` (`upload_resolution.py:9`), which the audit's class table grades as branch (d) (`:130`, `:137`). ~Y
   therefore POSTs ONCE and observes the outcome by read-only DynamoDB and S3 reads, never through a second
   `/analysis/inputs` request. With a single POST, a lost queue message is not redriven; it stays RESOLVING and is
   reported as such.

## The write set, per branch

Written by the POST (`irpt-ycharts-generate`, `intake/uploads.py`), tenant `cottonwood`:
- the retained original (S3 object, `artifacts.put`, `:189`);
- row `UPLOAD#<upload_id>` in `irpt-requests` (`:167`, `:198`);
- row `NORMALIZATION#<upload_id>#<revision>` in state RESOLVING, with `dispatched_at` (`:208`);
- ONE SQS message `{kind: resolve_upload, tenant, upload_id, normalization_revision}` on the generation queue.

Written by the resident (`resolve_deferred`), one of three branches:
- **NORMALIZED:** the NORMALIZED_PORTFOLIO artifact (S3 object, `:256`), row `INPUT#<input_id>` (`:261`), and the
  NORMALIZATION# row flipped to NORMALIZED by a conditional put on `state = RESOLVING`.
- **NEEDS_CORRECTION** (a symbol refused by name): the NORMALIZATION# row flipped with the reason and findings. No
  INPUT# row and no normalized artifact.
- **RETRY** (provider outage): nothing is flipped; the message returns to the queue and the row stays RESOLVING.

Not read from Y's code: any lease or journal entry that the resident session itself writes around the GET.
`2.0.0_SA_COO~P` names it from the installation, or the packet states it as the session's own bookkeeping.

## Retention

Everything above is kept as the acceptance evidence (packet K4 RETENTION). ~Y's log names each row key and object key.
