# IRPT_ANLREQ: two back-end items from Andrew's 2026-10-20 walk (for `1.0.0_SA_CTO~DELL2` to place)

Author `4.0.0_SA_CRO~TCKT`. Authority:
- `ANDREW_DIRECT_20261020_14xxZ_TCKT_WALKTHROUGH_VOICE_MEMO.md` @9de85135f0;
- `ANDREW_DIRECT_20261020_15xxZ_TCKT_SYNTHESIS_ANSWERS.md` @f2581e90b9.

Evidence is the read-only research of 2026-10-20 ~13:4xZ at origin/CLOUD 227b7eea80f (M = measured, I = inferred). This
seat does not build these: both sit in the engine and resident surface that `~G2` and `~Y2` are cutting in round 43, and
each lands through a resident or door release.

## Item A: "No" on a replacement prompt reaches a named proxy (the Kimi/OpenAI swap Andrew says is built)

**Andrew:** hitting No "would be a decision for Opal staff ... operated in the back end ... a Kimmy or open AI swap
workflow scenario, which we've already built."

**Built (M):**
- The pick rule: `ycharts/research/swap_replacement.py` (`CLASS_LONGEST_YAHOO_HISTORY`).
- The live pass: `ycharts/research/swap_pass.py:180-215`.
- It ran on 10-17 (`swaps[1]`, status `NO_REPLACEMENT`).

**Not wired (M):**
- `swap_pass.py` calls `choose_replacement(symbol, classification, pool_rows, [], history_days)`. The model proposals are
  a literal `[]`.
- No model classifies a ticker that is absent from `etf-classifications`. That is C-SWAP step 3: kimi-k2.6 with web
  search, below 0.80 flagged.
- Neither `kimi_port.py` (the resident's Kimi transport) nor `intake/resolution_kimi.py` (the door's) feeds `classify` or
  `model_proposals`.
- So an unknown ticker always reads NO_REPLACEMENT.

**Done when:**
- A filing whose holding is unknown, with the filer pressing No, produces a report that names the proxy for that holding:
  `proxy_for`, `proxy`, `method`, `confidence` and `sources` in run.json `swaps[]`.
- A low-confidence pick is flagged.
- The prompt-to-proxy path is driven on purpose, once, as a run.

**Bounds:**
- The model widens the pool and classifies. It never decides the pick (C-SWAP as written).
- Vendor egress follows C-SWAP's existing ruling; no new vendor.

## Item B: the audit record, formalized (Andrew: "a structured JSON for that audit reporting ... in a designated bucket")

**Andrew:** step 11's cards are an audit function; formalize a structured JSON; "an analysis-report folder in each
firm's bucket ... using lgic naming standards".

**What exists (M):**
- run.json IS the per-request trace. It is family `YCHARTS_RUN` (`infra/logic/registry/reporting_policies.json:56-71`).
- It is written by `address("irpt", firm, "state", "ycharts_runs", "request=<REQ>", object="run.json")` in the firm
  bucket, schema string `irpt-ycdgen-run-v2`.
- The ~400 "Open report" cards are its `elements[]`.

**Gaps (M unless marked):**
1. There is no published JSON Schema for `irpt-ycdgen-run-v2`; it is a version string only.
2. There is no ticket linkage: run.json carries no `ticket_id`, form answers, filer principal, door upload id or
   findings, package pointers, commentary ref or hop failure. Those live in `opal-tickets`, `irpt-requests` and
   `irpt-jobs`.
3. Retention is `irpt-retention-v1`: 30 days unreferenced, 2,555-day ceiling. That is short for an audit record (I).
4. The folder is `ycharts_runs`, not an "analysis-report" folder. A new table name means a registry row through the
   builder (rule 30). Renaming the existing producer's home is a migration, never a rider (R19).

**Done when:**
- Each analysis request has ONE audit JSON in its firm's bucket, at a builder-made address, with a published schema.
- It carries the four linkages: ticket, form as filed, filer, and the package and commentary pointers.
- A consumer rejects a malformed record.

**Two questions for Andrew (not answered in his words; never assumed):**
- (a) How long must an audit record be kept?
- (b) Is the existing run.json extended in place, or is a new `analysis-report` family started beside it? The CRO
  recommends a new family, so `ycharts_runs` is not migrated mid-round.

## Not in these items (placed elsewhere)

- The front-end rulings: `cand/dell2/anlreq-andrew-walk` @f41b4fce, approval row `dell2-20261020T150743Z-500c`.
- The report engine, Core then parity: `docs/briefs/irpt-anlreq-report-engine-core-then-parity-brief-20261020.md`
  @e197f63e58.
- Ticket status: NO change (Andrew item 9).
- Partners filing every request type: the ticket service admits CLIENT on SUBMIT-FORM for any type (M,
  `lambda_function.py:188`). Trade attachments and meeting fields are INTERNAL-only (M, :202-206), and the partner page
  shows the Analysis Request only. This is parked while the Ticket Center is internal-only (PRD v0.6); it un-parks when
  Andrew shows it to client users.
