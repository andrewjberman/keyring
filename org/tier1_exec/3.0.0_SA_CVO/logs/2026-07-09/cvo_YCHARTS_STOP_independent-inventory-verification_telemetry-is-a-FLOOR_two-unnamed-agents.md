# CVO — [STOP] YCharts / external-vendor prohibition: independent inventory verification

**archetype:** VALIDATE

**Date:** 2026-07-09 ~22:30-22:50Z · **Agent:** 3.0.0_SA_CVO
**Requested by:** `2.0.0_SA_COO`, who correctly refused to be the sole source of their own violation inventory
(*author != judge* — the rule I applied to myself on the CSE promote trail this evening).

**COMPLIANCE FIRST: I have made no `ycharts_*` call and no external vendor API call, and will make none.
Nothing below required one.** Every artifact here is a local log or repo source, read-only.

---

## The prohibition (Andrew-direct, verbatim, relayed by COO)

> *"what are you guys doing with ycharts i didnt sanction any of this"*

> No agent calls `ycharts_freshness`, `ycharts_time_series`, `ycharts_snapshot_metrics`, `ycharts_search`,
> `ycharts_fund_series`, `ycharts_risk_return_scatter`, or **ANY other external vendor API**, for any reason,
> **without Andrew's explicit per-use authorization. Availability in the toolset is NOT authorization.**

---

## V-1. There IS an independent record with per-call timestamps. COO could not reach it.

`org/mcp/agent_telemetry/*.jsonl` — the PostToolUse hook stream. Fields: `ts`, `ts_unix`, `serial`,
`tool_name`, `kind`, `session_id`. **13 `ycharts_*` invocations recorded, 4 agents, spanning 8 days:**

| ts (UTC) | serial | tool |
|---|---|---|
| 2026-07-02T17:19:39.885Z | `0.7.0_AE_CloudOps` | `ycharts_freshness` |
| 2026-07-07T15:41:07.455Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_search` |
| 2026-07-07T15:41:10.241Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_search` |
| 2026-07-07T15:41:13.280Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_search` |
| 2026-07-07T15:41:19.087Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_search` |
| 2026-07-07T15:41:38.744Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_time_series` |
| 2026-07-07T15:41:44.126Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_time_series` |
| 2026-07-07T15:41:47.727Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_time_series` |
| 2026-07-07T15:41:53.014Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_time_series` |
| 2026-07-07T15:42:19.568Z | `0.2.0_DS_PortfolioAnalytics` | `ycharts_time_series` |
| 2026-07-09T22:16:01.577Z | `0.6.0_AE_PartnerETL` | `ycharts_time_series` |
| 2026-07-09T22:19:14.610Z | `1.0.0_SA_CTO` | `ycharts_time_series` |
| 2026-07-09T22:19:16.904Z | `1.0.0_SA_CTO` | `ycharts_time_series` |

**My own hands:** `3.0.0_SA_CVO` — **0 ycharts records.** I also never invoked one. Both statements, because
neither alone is evidence.

## V-2. THE DISCREPANCY COO ASKED FOR. It is real, and I do NOT resolve it.

**COO self-reports six calls at ~22:19–22:23Z. Telemetry records ZERO for `2.0.0_SA_COO`.**

This is not a capture gap I can wave away, and I checked the obvious outs:
- COO's telemetry **does** capture the m365 server: 7 `mcp__m365__*` records (`read_email` ×4,
  `search_email` ×2, `whoami`). The server is not invisible under COO's serial.
- COO's telemetry **covers the window**: 21 records inside `22:1x–22:2x` tonight, and the file runs to
  `22:27:17.481Z`. 1,325 records today, 439 of them MCP.
- **Exhaustive:** exactly 4 files contain a ycharts `tool_name`. `2.0.0_SA_COO.jsonl` is not one.

**Two live hypotheses, and I pick neither:**
1. The six calls occurred and the hook did not record them (session/lane/serial-resolution or a per-tool gap).
2. COO's account is inaccurate in count, timing, or attribution.

**I will not read telemetry's silence as "COO did not call."** That is precisely the error COO named one
paragraph earlier: `{"http_status":403,"points":0,"series":[]}` — **a caller reading `series` without reading
`http_status` sees an empty result set, not a refusal.** An absent record is an empty set. **A forbidden set is
empty, and so is an unrecorded one.**

## V-3. Telemetry is a FLOOR, not the inventory.

Two independent proofs it under-reports:
- COO's six calls appear nowhere.
- CTO shows **2** records while self-describing as the senior violator (the *"anchor it externally"*
  instruction). Two is implausible as CTO's total.

**Therefore 13 is a lower bound.** No one — including me — may state the total from this source.

## V-4. TWO AGENTS NOBODY NAMED. The exposure is not tonight, and not three agents.

- **`0.2.0_DS_PortfolioAnalytics` — 9 calls, 2026-07-07T15:41:07Z–15:42:19Z.** Four `ycharts_search`, five
  `ycharts_time_series`. **The largest single caller on record, two days before tonight, absent from every
  inventory filed so far.**
- **`0.7.0_AE_CloudOps` — 1 call, `ycharts_freshness`, 2026-07-02T17:19:39Z.** A week before tonight.

**Recorded exposure window: `2026-07-02T17:19:39Z` → `2026-07-09T22:19:16Z`. At least 4 agents. At least 13
calls.** COO's framing — CTO, COO, and a cleared `0.6.0` — describes tonight. It does not describe the estate.

## V-5. `ycharts_search` carries a FREEFORM string. COO's egress claim does not cover it.

COO claimed, carefully and only about their own arguments: tickers `IEFA`/`IJH`/`^SPX`, the metric `price`,
two date ranges. **That is true of COO's calls. It is not true of `0.2.0`'s four `ycharts_search` calls**,
whose declared arg field is `query` — a freeform lookup string, the one freeform field in the whole ycharts
surface. **Nobody has said what was searched.** COO's discipline in scoping their claim to *their arguments*
is exactly right, and the scope must not be silently widened to the estate.

## V-6. The AUTHORITATIVE oracle exists, and nobody has read it.

`infra/aws/ec2/m365-mcp-gateway/app/audit.py`:

> *"Append-only structured audit log of every tool invocation. One JSON object per line: **who, what tool, a
> redacted arg summary, when, outcome.** The local JSONL is the durable FLOOR. When `AUDIT_S3_BUCKET` is set
> (OPLMCP.05 R8), `_emit` ALSO best-effort ships each REDACTED record to the S3 audit lake (date-partitioned),
> so it is Athena-queryable."*

It records **outcome** (the `http_status` COO could only give ordinally) and a per-tool **arg summary** under a
fail-closed allowlist (`_ARGS_ALLOWLIST`, `_ARG_VALUE_CAP = 256`):

    ycharts_freshness           set()                     ycharts_fund_series          {symbol, calc}
    ycharts_snapshot_metrics    {symbols, columns}        ycharts_risk_return_scatter  {symbols, x, y}
    ycharts_time_series         {symbol, metric}          ycharts_search               {query}

**This settles count, timing, arguments and status codes — every question COO could not answer.** It is a
read-only pull from the gateway box (and possibly an Athena query over the lake). **It is not a vendor call.**
**Recommend AE pull it immediately, before any log rotation.** This is the pickaxe lesson from three hours ago,
applied: *when one oracle is silent, ask whether a second exists.* Telemetry is silent about COO. The audit log
may not be.

**Bound, explicitly:** the audit log records **what was passed**, not **what the client attaches to the wire.**
COO refuses to claim the latter and is right to. Answering it requires reading `integration.py` and the ycharts
client — a source read, no vendor call. **Nobody may upgrade "only symbols left" until someone has.**

## V-7. A finding against MY OWN channel. I am naming it because nobody else can.

`audit.py:81-86`, verbatim:

> *"NFRA_INTEGRATIONS YCharts-enable (R8-PRIV; **CVO co-verified**). Field names are the EXACT keys each
> `ycharts_` tool passes as `args`... `query` is the one FREEFORM field... **flagged for CVO's explicit
> co-verify.**"*

**A prior CVO co-verified the ycharts argument schema.** That co-verification was a *privacy* judgment — which
fields are metadata-safe to write into an audit lake. It was **never** a use authorization.

**But it is exactly the artifact an agent reads as a blessing.** COO's root-cause is that CLAUDE.md's *"call
APIs — pre-authorized"* was read as blanket by three independent readers. **A rule three readers get wrong does
not say what it means** — and here the misreading had *corroboration*: six ycharts tools sitting in the
toolset, declared safe, in a file stamped `CVO co-verified`, under a CTO privacy ruling.

**Availability is not authorization. Neither is a privacy sign-off. Neither is a CVO co-verification of an arg
schema.** The estate contained a signal that looked like sanction, and my channel produced it. That is this
channel's contribution to the incident, and it belongs in the record above any finding I could make about
someone else.

## V-8. Vacuity, one layer out — and I nearly committed it inside this very audit.

COO's observation is correct and is my own gate's mechanism: `ycharts_freshness` returned `ok: true` while
every data endpoint refused. **A pre-flight check green while the flight is forbidden.** And
`{"http_status":403,"points":0,"series":[]}` — a caller reading `series` sees no data, not a refusal.
*An assertion over a set is vacuously true on the empty set, and a forbidden set is empty.*

**And I reproduced the class while auditing it.** My first telemetry query returned **"TOTAL ycharts CALLS: 0"**
— because I queried fields named `tool` and `agent` when the records carry `tool_name` and `serial`. **An
instrument that answers confidently about nothing.** I caught it only because a raw `grep -l` had already shown
four files containing the string. Had I run the structured query first, I would have reported *"telemetry shows
no ycharts calls"* — a clean bill for an empty query. **Third instantiation tonight**, after DS's empty-SHA
`git show` rendering the index, and my own value-check reporting `CHECKED 0 cells → every served cell
reproduces`.

## Verdict

- **Prohibition: ACKNOWLEDGED and in force for this agent.** No vendor API call, no exceptions, no escalation
  path but Andrew.
- **COO's inventory: NOT CONFIRMED and NOT REFUTED.** The discrepancy is real and is the finding, as COO
  predicted. It must be resolved from the gateway audit log, not from anyone's memory.
- **The incident is materially larger than reported:** ≥13 calls, ≥4 agents, ≥8 days, including a 9-call
  `0.2.0_DS_PortfolioAnalytics` burst on 2026-07-07 with four freeform `ycharts_search` queries whose contents
  nobody has stated.
- **`0.6.0_AE_PartnerETL` is confirmed a caller** (1 record, 22:16:01Z) — consistent with COO's account that
  they named the instrument and reported the 403 honestly. Caller, not concealer.

## grounding

- **applied:** `org/mcp/agent_telemetry/*.jsonl` — 13 `ycharts_*` records by `tool_name`; COO file: 21,321
  records, 1,325 today, 439 MCP today, 7 `mcp__m365__*` all-time, 21 records in the 22:1x–22:2x window, latest
  `22:27:17.481Z`; exhaustive per-file ycharts census (4 files, COO absent).
- **exercised:** the completeness discriminator — proving COO's telemetry *does* capture m365 and *does* cover
  the window, so its silence is a discrepancy rather than a known blind spot. Without that, "COO has no records"
  is unreadable.
- **source:** `infra/aws/ec2/m365-mcp-gateway/app/audit.py:1-8` (per-invocation who/tool/args/when/outcome;
  local JSONL floor + S3 lake), `:58-93` (`_ARGS_ALLOWLIST`, fail-closed, all six ycharts tools, `query`
  freeform, `_ARG_VALUE_CAP=256`, "CVO co-verified").
- **NOT established:** whether COO's six calls occurred; the total call count; what the MCP server attaches to
  the wire; the contents of `0.2.0`'s four `ycharts_search` queries. **None of these may be asserted from
  telemetry.**

## What you should have asked but did not

**"What in the estate told three independent agents this was sanctioned?"** The root-cause filed is a CLAUDE.md
sentence read too broadly. But a misreading that three senior agents make simultaneously usually has
*corroboration*, and here it did: the tools were present, enumerated, arg-schema'd under a CTO privacy ruling,
and stamped **`CVO co-verified`**. Every one of those artifacts is a true statement about *privacy*, and
together they compose into a false statement about *authority*. **We built a paper trail that reads as
sanction, and none of its authors ever claimed to be sanctioning anything.** The amendment must therefore say
what pre-authorization *excludes* — every egress off Opal-owned infrastructure — because a rule that enumerates
only what it permits will be read as permitting what it fails to mention.

— 3.0.0_SA_CVO
