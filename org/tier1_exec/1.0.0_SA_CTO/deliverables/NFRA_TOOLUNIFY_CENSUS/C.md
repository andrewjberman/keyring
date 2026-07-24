# NFRA_TOOLUNIFY Estate Census — Lane §2.C: M365 / Microsoft surface

**Author:** `0.8.0_AE_CloudComp~C` · **Date:** 2026-07-24 · **Vintage:** all live measurements below taken
this session @ commit `9da59d7ced` on `CLOUD`, 2026-07-24T22:14:50Z, live/source, not quoted from a prior
report unless explicitly marked historical. **Report to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` only.
**Discipline honored:** read-only census throughout; the gateway was read as SOURCE CODE + CONFIG only —
no `mcp__m365__*` tool was invoked, no Graph call was made (vendor-egress discipline held per BINDING §2).

---

## VERDICT

**M365 is a POPULATED PLANE — real, live, deliberately narrow, with a built-but-DORMANT heat analytic and
a never-shipped consumer.** It is not a stub and not "a single heat table." Four things are simultaneously
true and none of them is the whole picture alone:

1. **The graph-ingestion substrate is live and growing.** 5,669 `layer='ms'` nodes in the canonical
   kuzu/Nessie graph today (07-24), up from 5,520 on 07-15 — the nightly derive is still running and still
   picking up real SharePoint activity. This is genuinely populated, not decorative.
2. **The scope is intentionally narrow, by a recorded Andrew decision, not an accident or a stall.** One
   SharePoint site (`/sites/Shared`), one library. OneDrive and the other 5 SharePoint sites are explicitly
   NOT ingested (`org/projects/NFRA_MSGRAPH.json`: *"COVERAGE deliberately narrow BY DECISION #1... widen
   only after S4's tools prove out on the slice"*).
3. **The heat analytic (`ms_heat` / `ms_heat_snap`) is real but DORMANT, not scheduled, and currently
   unguarded.** Last computed 2026-07-17 (7 days stale as of this census); no code path anywhere invokes it
   automatically; the CloudWatch alarm that was "born healthy" on 07-16 no longer exists in live AWS.
4. **The project's own headline deliverable never shipped.** NFRA_MSGRAPH's stated Component-3 — agent
   findability over the MS estate (`comp-ms-find`, a `comp-which` MS route) — is `S4`, and S4 was never
   built. Live-checked this session: `comp-which` has zero curated route for MS/SharePoint questions and
   scores it a "no curated rule matched" fuzzy guess. **The heat data that does exist has no tool-level
   consumer.** That is very plausibly *why* it went dormant on 07-17: its build-and-prove window ended and
   nothing downstream depended on a fresh answer.

**Is there an M365 plane in the GLOBGRPH 7-layer taxonomy? No.** The canonical taxonomy
(`docs/architecture/NFRA_GLOBGRPH_PRD.md` §1, live-read this session) declares exactly seven layers —
L1 Portal frontend, L2 Network/API, L3 AWS compute, L4 Data storage, L5 Data pipeline, L6 IAM/security,
L7 External boundary — and M365 is not one of them, not as an eighth layer, not folded into L7. M365 enters
the graph as a **property value** (`layer='ms'` on the same single `CloudNode` label everything else uses),
the same extensibility mechanism as every other layer value, but it was never retrofitted into the PRD's own
canonical layer table. A reader of the authoritative taxonomy doc would not learn M365 exists in the graph
at all — a real (if narrow) documentation/taxonomy gap.

---

## §1 — The `m365-mcp-gateway` EC2: what it actually exposes

**Grounded:** `EC2_MANIFEST.json:444`, `infra/aws/ec2/m365-mcp-gateway/` (source), live file-checksum
manifest, `README.md`, `app/tools.py`, `app/graph.py`.

**Deployed, live, persistent EC2** — `i-07dccb1615503ac99`, `deployed_commit c390d1c6a`,
`deployed_at 2026-07-15T18:49:23Z`, deployed by `0.2.0_DT_PortfolioAnalytics`. This is current infra, not a
stale record — the checksummed file manifest in `EC2_MANIFEST.json` is 9 days old at census time, well
inside normal churn.

**Architecture (source-grounded):** AWS ALB (internet-facing, `authenticate-oidc` against Entra ID) →
nano EC2 (bound to 127.0.0.1, inbound only from the ALB SG) → per-user delegated MSAL token (cached,
Fernet-encrypted) → Microsoft Graph. Delegated-only — the gateway can never exceed what the signed-in user
could do themselves; there is no app-only path. Kill switch (`touch KILL_SWITCH`), per-user blocklist
(hot-reloaded), and a JSONL audit log (`audit.jsonl`, one line per call) are all live mechanisms, not design
intent — the file inventory carries `app/blocklist.py`, `app/revocation.py`, `app/audit.py`,
`app/token_broker.py`, `app/oauth_as.py`, plus tests (`test_jwt_cve_lock.py`, `test_min_tier_gate.py`,
`test_ratelimit.py`, `test_ssavail_contract.py`, `test_attachment_tools.py`).

**Two structurally distinct consumers of this one box — this is the crux of "modeled vs merely queryable":**

| Path | What it is | What it touches | Grounded in |
|---|---|---|---|
| **A — graph ingestion** | `derive_runner.py` → `ms_cloud_extract.py`, nightly, machine-to-machine | 4 allowlisted, structure-only HTTP GETs on `/ms/*` (`ms_sites`/`ms_site_children`/`ms_onedrive_children`/`ms_search`) + `/ms/health`. Content/comms fields are stripped at the gateway AND cert-checked again at the derive (`assert_no_content_comms`, a gate-impossible fail-closed leg). | `infra/aws/ec2/m365-mcp-gateway` server + `infra/aws/globgrph/` derive; `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-06-26/*` |
| **B — interactive MCP tool surface** | Live `@mcp.tool()` functions callable by any connected Claude session (Code/Desktop) over `https://mcp.opalinvest.dev/mcp` | **~30 tools**, content-bearing, both read AND write: `whoami`; email (`list_recent_email`, `search_email`, `read_email`, attachments, `create_draft`, `send_email`, `reply_email`); `list_calendar`; OneDrive (`list_onedrive`, `search_files`, `read_file`); SharePoint (`find_sharepoint_site`, `list_site_files`, `read_site_file`, `profile_site_file`, `search_site_files`, `list_site_drives`, `get_item`/`get_site_item`, `read_document`); Excel (`read_site_workbook`, `read_workbook`); Teams (`list_chats`, `read_chat_messages`, `send_chat_message`, `list_teams`, `list_channels`, `read_channel_messages`, `send_channel_message`, `poll_addressed_teams_messages`); plus SSAVAIL-specific tools (`validate_ssavail_attachment`, `upload_text_to_site`) built for the **PFMG_TAXSMA** project's file-drop workflow. Writes are `confirm`-gated. | `app/tools.py` (live-read, line-numbered `@mcp.tool()` inventory this session) |

**This session's own environment is a live instance of Path B**: the system prompt's MCP-server list names
an `m365` server "still connecting" — that is this gateway. I did not call it (census discipline, BINDING
§2) but its presence in this very session is first-hand, not inferred, evidence that Path B is a real, used,
current consumption channel, separate from and much richer than Path A's four read-only structural GETs.

**Path B is NOT graphed at all.** Email bodies, chat messages, calendar entries, workbook contents returned
by Path B tools are ephemeral per-call responses — nothing about them lands in `graph_nodes`/`graph_edges`.
Only Path A's structural metadata (site/library/folder/file/user existence, containment, `lastModified`)
becomes a graph node. This is the precise answer to the MUST-CLOSE question "modeled as graph nodes vs
merely queryable via the gateway": **structure is modeled; content is merely (and only interactively)
queryable, by design (the catastrophic-floor guardrail), and unrelated to the graph.**

**Scope note (why the box isn't M365-exclusive):** `app/integrations/` also carries `ycharts/` and
`opal_portal/` integration modules — this EC2 is a general-purpose MCP gateway that happens to host M365
as one (the largest, oldest) of several integrations, not an M365-dedicated box. I did not characterize the
other integrations (out of my M365-only boundary); flagging their existence because it bears on "how much
of this infra investment is M365-specific" — the honest answer is: the box, not all of its code, is shared.

**Declarative drift finding:** the gateway's own `README.md` states *"Current state (verified 2026-06-16):
... AWS deploy: NOT STARTED ... zero ALBs and no gateway EC2 of any kind."* That was true on 06-16. It has
been false since the 06-23 GO-LIVE cutover (`i-01d75141` → `i-07dccb161`) and every day since — including
the 07-15 deploy that is the box's own current `deployed_at`. The README is stale by five weeks against the
box it documents. Not my call to fix (out of scope for a read-only census) — recorded as a finding.

---

## §2 — `ms_heat`: producer, content, cadence (the MUST-CLOSE item)

**Two distinct artifacts share the "ms_heat" name — the census plan's own §1 pass conflates them; worth
correcting precisely:**

| Artifact | Kind | Location | Written by |
|---|---|---|---|
| `ms_heat` (index) | Plain S3 JSON, NOT Iceberg | `s3://opal-313476888478-globgrph/warehouse/ms_heat/ms_heat_index.json` (latest) + `.../snapshots/*.json` (dated) | `org/modules/heatmap/ms_heat_index.py`, run directly |
| `ms_heat_snap` | Iceberg table (append-only delta sibling) | `globgrph.ms_heat_snap` in the Nessie catalog | same script's `--emit-sibling` path, staged to S3 then appended by `snap_store.py --ingest-pending --surface ms_heat_snap` (must run **in-VPC** — the Nessie REST endpoint is `http://nessie.opal-globgrph.local:19120`, a private-DNS name unreachable from this session; noted as a could-not-reach-directly item below) |

**Producer, fully grounded (source-read, `org/modules/heatmap/ms_heat_index.py`):** reads `MS_FILE` +
`MS_FOLDER` nodes from the canonical kuzu graph at `pin==HEAD` (via the house `ensure_fresh` pattern),
scores each by write-recency using the shared `heat_map.HeatParams`/`score_item` engine (reused, not
rebuilt, from the DS-owned pure lib — same engine `code_heat` uses), rolls scores up the folder tree via
`object_locality.aggregate_tree`, and emits one JSON index: `nodes[]` (score-desc, hot/warm/cold banded) +
`clusters{}` (per-directory rollups). **Signal, verbatim from its own params block:**
`"write_heat: props.last_modified_dt (S2 metadata; content/comms NEVER read)"` — i.e., it measures
**write recency of SharePoint documents in the one ingested library**, nothing else; there is no read-heat
or access dimension yet (`read_heat: null`, `access: null` — explicitly reserved, S5-gated, additive).

**Cadence: NONE. This is the load-bearing finding.** The script's own docstring states cadence is
*"cadence-agnostic... the standing schedule... is a sizing RAVC to COO/CTO"* — i.e. undecided at build
time. I checked whether that RAVC was ever resolved into an actual trigger:
- `grep -r ms_heat infra/aws/globgrph/derive_runner.py` → **zero matches.** The nightly full-derive that
  feeds the GRAPH does not touch the heat index at all.
- No EventBridge rule, Lambda, or scheduled ECS task anywhere in the repo invokes `ms_heat_index.py` or
  `snap_store.py --surface ms_heat_snap`.
- `code_heat_emit.py` (the sibling analytic over git, not MS) is **also** a bare manually-invoked CLI
  script with no wiring into `derive_runner.py` — so this is not an M365-specific gap, it is a property of
  the whole "heat analytic" family as currently built. Noted for completeness, not chased further (base's
  Iceberg-core lane, not mine).

**Content freshness, live-measured this session (`aws s3api list-objects-v2`, UTC timestamps, not the
CLI's local-time-rendering `ls` — Verification Law 11):**

```
warehouse/ms_heat/ms_heat_index.json          2026-07-17T18:09:45Z   2,626,103 bytes
warehouse/ms_heat/snapshots/20260717T180941Z  2026-07-17T18:09:45Z
warehouse/ms_heat/snapshots/20260716T132023Z  2026-07-16T13:20:27Z
warehouse/ms_heat/snapshots/20260715T213817Z  2026-07-15T21:38:19Z
```
Three runs, 07-15/16/17 — exactly the S3 (heat-map) build-and-prove TO window
(`ms_heat_index.py` header: *"TO: NFRA_MSGRAPH.S3 ... 2026-07-15"*) — then **nothing for 7 days**. No
pending un-ingested batch sits in `warehouse/snap_ingest/pending/ms_heat_snap/` either (checked live,
empty) — so this is not "computing but failing to land," it is simply not being run.

**This is NOT the trading-calendar T-1 pattern (CLAUDE.md NEVER-rule) — checked and ruled out.** That rule
governs client-data pipelines with a known trading-day cadence where an old timestamp is expected on
weekends/holidays. This artifact has **no cadence at all** to be T-1 *of* — there is no schedule to compare
the age against. A dormant script with zero triggers is a different, plainer fact than a healthy pipeline
between trading days, and I am not conflating the two.

**No live freshness guard exists today.** The 2026-07-16 deploy-completion ledger
(`org/critical_paths/change_management/20260716T1533Z_batch-codeheat-msheat-17a_deploy_completion.md`)
proved a CloudWatch alarm `opal-globgrph-freshness-stale-ms_heat_snap_last_append` born healthy
(State=OK) that same day. Live-checked this session, twice (exact name, then a bare `freshness` prefix
sweep): **zero matching CloudWatch alarms exist.** Live-checked further: **zero Lambda functions with
"freshness" in the name exist in the account at all.** I did not chase why (the FRESHGUARD mechanism in
general is base's Iceberg-core lane, and the workspace's own git status at session start shows
`freshguard-leg4`/`freshguard-leg5` open-deploy files mid-flight, which may be the proximate cause) — but
the bounded, M365-specific fact stands: **whatever currently exists to detect `ms_heat_snap` going stale,
it is not live in AWS today.**

**Branch-head marker cross-check (`warehouse/_branch_head.main.json`, live-pulled this session,
`committed_at 2026-07-24T15:04:10Z`, writer `incremental_updater`):** its `table_metadata` tracks exactly
four tables — `cse`, `graph_contracts`, `graph_edges`, `graph_nodes`. `ms_heat_snap` is not among them.
Read in context (this is the same field `ms_heat_index.py` itself reads, and it only ever reads
`graph_nodes` from it), this marker is scoped to the core substrate, not every obs-layer sibling — its
silence on `ms_heat_snap` is not evidence the Iceberg table is missing, just that this particular marker
was never the place its vintage would be recorded. **Could-not-verify, disclosed rather than papered over:**
I could not read `ms_heat_snap`'s own Iceberg metadata (snapshot count / last commit) directly — the
Nessie REST catalog (`nessie.opal-globgrph.local:19120`) is a VPC-internal hostname, unreachable from this
session's vantage. The S3 JSON mirror (same producer, same run) is the best available proxy and is fully
consistent with dormancy since 07-17.

---

## §3 — What's modeled as graph nodes (live counts, current vintage)

**`comp-kuzu` live query, this session** (provenance header: `kuzu_nessie_db`, 20,403 nodes / 40,827 edges
total, **built 2026-07-24T18:01:18Z, age 4.0h, Nessie HEAD current — pin==marker HEAD**):

```
n.node_type   count
-----------   -----
MS_FILE       4,618
MS_FOLDER     1,034
MS_USER          15
MS_SITE           1
MS_LIBRARY         1
                ─────
TOTAL layer='ms'  5,669   (27.8% of the entire 20,403-node graph)
```

**Denominator + comparison:** the project's own record (`org/projects/NFRA_MSGRAPH.json`, phase note dated
2026-07-15) states 5,520 MS nodes then (4,498 MS_FILE + 1,021 MS_FOLDER + others). Today's 5,669 is **+149
nodes in 9 days** — small, real, monotonic growth consistent with an actively-running nightly derive over
one live document library, not a frozen snapshot.

**7 node_types are declared in the schema** (`S1_MS_GRAPH_SCHEMA.md`): `MS_SITE`, `MS_LIBRARY`, `MS_FOLDER`,
`MS_FILE`, `MS_DRIVE_ONEDRIVE`, `MS_USER`, `MS_GROUP`. **Only 5 have live instances today; 2 read zero, and
both are explained, not mysterious:**
- `MS_DRIVE_ONEDRIVE` (0 live) — this type exists only for personal-OneDrive ingestion, which was
  **deliberately dropped** when the extraction target moved from Andrew's personal `/me/drive` to the
  shared `/sites/Shared` (see §4, the RESCOPE). Zero is the *expected* count post-re-target, not a gap.
- `MS_GROUP` (0 live) — this type is created only from `/permissions` data (S5 scope). S5 was never built
  (confirmed live: no `/permissions`, `/delta`, or `/insights` endpoint on the gateway per the S1 recon,
  never revisited since). Zero is the correct state of an unbuilt phase, not a defect in what shipped.

**Edges:** `CONTAINS` (containment hierarchy) and `OWNED_BY` (creator/last-modifier, partial — needs a
`$select` addition per the schema doc) are day-one and live. `HAS_ACCESS`/`SHARED_WITH`/`MEMBER_OF` are
schema-defined but **zero live edges** — all three are gated on the same never-built `/permissions` (S5).
Access-topology over the MS estate is entirely unmodeled today; this is a known, named, S5-gated gap, not
an unexplained hole.

**Source-verified site narrowing (not merely inferred):** `ms_cloud_extract.py` defines
`TARGET_SHAREPOINT_SITE_ID = os.environ.get("GLOBGRPH_MS_TARGET_SITE_ID", ...)` — a single-site env-var
target, confirming at source (not just by count-matching) that the extractor targets exactly one site by
design. The live MS_SITE=1 / MS_LIBRARY=1 counts are the direct, intended consequence of this code, not a
symptom of something broken.

---

## §4 — Trajectory: a rescope was proposed, partly landed, and explains today's state

On 2026-06-26 (the same day as GO-LIVE), Andrew directed a re-scope, recorded in
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_MSGRAPH/RESCOPE_estate_wide_heat_analytics_layer.md`
and routed to CVO review → CTO arch-gate. Three proposed changes, checked against live state this session:

| Proposed change | Landed? | Evidence |
|---|---|---|
| Re-target ingestion: personal `/me/drive` → shared `/sites/Shared` | **YES** | Live MS_FILE count (4,618) matches the RESCOPE's own predicted `/sites/Shared` corpus size (~4,560) almost exactly; `MS_DRIVE_ONEDRIVE` now reads 0 (personal-drive crawl dropped); `TARGET_SHAREPOINT_SITE_ID` in source confirms single-site targeting. |
| Cadence: nightly-full+delta-hourly → hourly full poll, drop `/delta` | **Not confirmed either way** — the derive still runs on the nightly cadence per the project record; I found no evidence of an hourly poll. Not chased further (would require checking the ECS schedule directly, arguably base's territory). |
| **Generalize heat from MS-only to an estate-wide, domain-agnostic `heat_index` over ALL `graph_nodes`** (AWS + MS in one table) | **NO** | The tables in live use today are still MS-specific (`ms_heat` / `ms_heat_snap`), not a generalized `heat_index`. No `heat_index` Iceberg table was found anywhere in this session's greps. The 2026-07-17 decommission-tooling assessment (same lane, `0.8.0_AE_CloudComp`) independently re-derives this exact gap three weeks later ("Heat exists for code and documents... does NOT exist for the rest of the AWS-resource plane") — i.e. the RESCOPE's core ask was still unmet three weeks after it was proposed, and is still unmet today. |

**The project's own phase record is unambiguous about what's actually left:** `org/projects/NFRA_MSGRAPH.json`
(`status: "active"`, last phase update 2026-07-15) sequences the work S1→S6 and states plainly that **S4 —
"THE deliverable" (comp-ms-find / doc-cloud comp-which findability)** — was still awaiting "CTO+COO
decomposition" as of that update. **Live-checked this session:** `comp-which "find documents in the shared
sharepoint site by heat or recency"` returns **zero curated matches** — the tool's own output: *"NO CURATED
RULE MATCHED THIS QUESTION... these are FUZZY GUESSES, not a routing decision."* No `.tools/comp-ms-*`
executable exists. **S4 has not shipped, as of 2026-07-24.** This is the most load-bearing single fact in
this census: the graph substrate and the heat analytic were both built to feed a findability layer that
was never built, which is the most parsimonious explanation for why the heat analytic (whose only reason
to exist is to feed S4) stopped being run the moment its own proving window (S3) closed.

---

## §5 — Denominators + vintage (summary)

| Measurement | Value | Denominator / scope | Vintage |
|---|---|---|---|
| `layer='ms'` graph nodes | 5,669 | of 20,403 total graph nodes (comp-kuzu, canonical, pin==HEAD) | built 2026-07-24T18:01:18Z (4.0h old at query time) |
| `ms_heat` JSON index last write | 2026-07-17T18:09:45Z | S3 object listing, `warehouse/ms_heat/`, UTC via `s3api` (not CLI `ls`) | live-pulled 2026-07-24T22:1xZ |
| `ms_heat_snap` pending-ingest backlog | 0 objects | `warehouse/snap_ingest/pending/ms_heat_snap/` | live-pulled 2026-07-24T22:1xZ |
| CloudWatch alarms matching `opal-globgrph-freshness*` | 0 | account-wide `describe-alarms --alarm-name-prefix` | live 2026-07-24T22:1xZ |
| Lambda functions matching `freshness` | 0 | account-wide `list-functions` | live 2026-07-24T22:1xZ |
| MCP tools exposed by the gateway | ~30 (`@mcp.tool()` count) | `app/tools.py`, this file at `deployed_commit c390d1c6a` | source-read 2026-07-24 |
| Declared MS node_types | 7 | `S1_MS_GRAPH_SCHEMA.md` §1 | authored 2026-06-26, unchanged since (no S5/S6 schema revision found) |
| Populated MS node_types | 5 of 7 | live comp-kuzu GROUP BY | 2026-07-24T18:01:18Z |
| GLOBGRPH declared layers | 7 (L1–L7), M365 not among them | `docs/architecture/NFRA_GLOBGRPH_PRD.md` §1 | PRD v0.4.4, 2026-06-12, unchanged since (no later layer-table revision found) |

---

## §6 — Could-not-determine (disclosed, not papered over)

1. **`ms_heat_snap`'s own Iceberg snapshot count / exact last-commit timestamp** — the Nessie REST catalog
   endpoint is VPC-internal (`nessie.opal-globgrph.local`); unreachable from this session. The S3 JSON
   mirror (same producer script, `--emit-sibling` runs both together) is the best available proxy and is
   consistent with the same 07-17 dormancy; I am not asserting the Iceberg table's exact state as directly
   observed, only as strongly implied by its sibling artifact from the same producer run.
2. **Whether the ingestion cadence is actually hourly (per the RESCOPE) or still nightly** — would require
   reading the ECS schedule/EventBridge rule for the derive-runner task directly; not chased (borders on
   base's Iceberg-core-derive territory, and doesn't change the M365-specific verdict either way).
3. **Why the FRESHGUARD alarm/Lambda are currently absent from live AWS** (torn down, mid-migration, or
   renamed) — the workspace's own open-deploys ledger shows `freshguard-leg4`/`leg5` in flight at session
   start, which may be the proximate cause, but I did not verify a causal link. This is base's Iceberg-core
   mechanism to characterize; I report only the bounded, M365-specific consequence (no live guard on
   `ms_heat_snap` today).

---

## §6a — ADDENDUM (post-CVO~Z verification): the dormancy claim, upgraded to independently proven

`3.0.0_SA_CVO~Z` PASSed this lane after independently re-deriving 3 of 4 claims exact-to-source, and
correctly declined to certify the 4th ("zero scheduled trigger") as independently negative-proved — their
own check (source-read of `ms_heat_index.py`/`snap_store.py`'s manual-only invocation forms) was
*consistent* with my claim but did not itself *enumerate the space* the absence is claimed over. Their
standard, verbatim: *"proving an absence requires enumerating the space, not failing to find an instance."*
Fair, and cheap to close, so I closed it:

- **`aws events list-event-buses`** → exactly **one** bus (`default`) exists in the account — no
  custom-bus blind spot to worry about.
- **`aws events list-rules`** against it, properly paginated (a naive `--query length(Rules)` silently
  applies per-page under CLI auto-pagination and would have reported a floor of 100 — caught and corrected
  by collecting full page-merged name lists instead; **141 total rules, 0 duplicates**, confirmed exhaustive
  for the account's one bus).
- **Zero of the 141 rule names contain "heat" in any case.** The only globgrph-prefixed rules are
  `opal-globgrph-cloudtrail-mgmt` (event-pattern, not schedule), `opal-globgrph-comp-learns-producer-nightly`
  (cron 04:00, a different named producer), `opal-globgrph-derive-runner-nightly` (cron 02:00 — the one
  whose source I already read line-by-line and confirmed contains zero `ms_heat` references), and
  `opal-globgrph-fedobs-producer-nightly` (cron 04:30, a different named producer).

**Residual, disclosed rather than papered over:** this rules out any rule *named* for heat, and directly
confirms the one plausible *un-named* host (the nightly derive rule) by reading its actual code rather than
its name — but it does not certify that literally no rule on the bus targets a Lambda/task whose body
happens to invoke the MS heat producer under a name that reveals nothing about what it does. I consider
that residual vanishingly thin given the source-level confirmation on the one real candidate, and record it
for completeness rather than silence.

**Claim #4 status, restated at its now-correct grade:** zero scheduled trigger for `ms_heat_index.py` /
`snap_store.py --surface ms_heat_snap` is now **independently enumerated + proven** (141/141 rule names,
one event bus, cross-checked against a direct source read of the only rule that could plausibly hide it),
not merely corroborated-by-absence-of-contrary-evidence. Thank you to CVO~Z for holding the line on the
distinction — it is the correct standard and the gap was worth closing rather than leaving at "probably."

---

## §7 — Boundary discipline note

Stayed inside M365/Microsoft only. Did not characterize: the `ycharts`/`opal_portal` integrations riding
the same EC2 (noted as existing, not examined); the general FRESHGUARD alarm mechanism (base's Iceberg-core
lane); live-AWS-vs-graph count parity for non-MS resources (~A's lane); the tool→source mapping for
`comp-which`/`comp-heat` themselves as tools (~D's lane, though this report's live `comp-which` and
`comp-heat --help` calls are cited as primary evidence for the M365 verdict specifically, not as a
tool-census contribution).
