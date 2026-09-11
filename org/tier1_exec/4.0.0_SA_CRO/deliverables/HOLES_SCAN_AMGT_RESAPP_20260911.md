# Holes Scan — AMGT_RESAPP Four-Horsemen + News-Backing End-to-End, 20260911 ~08:1xZ

**Author:** 4.0.0_SA_CRO~Z
**For:** 1.0.0_SA_CTO~Z to fold in
**Scope:** everything this seat has authored or informed this session (chatter-volume mechanism,
full-stack vision, self-healing auth brief, the CRO coverage sign-off) plus what changed in parallel
while this seat was working. Not a re-summary of those docs — this is only the GAPS.

---

## 1. HIGHEST PRIORITY — two documents that will both bind DESIGN_SPEC/PRD already disagree

`1.0.0_SA_CTO~Z`'s own `AMGT_RESAPP_FRONTEND_FRAMEWORK_20260911.md` (`bf00c90d49`, committed
~06:53Z, distilled from the same Andrew transcript this seat also processed) and this seat's
`AMGT_RESAPP_FULLSTACK_VISION_20260911.md` (`3e25edc3e1`, committed ~07:22Z) **describe the same
page and now materially disagree**, because Andrew corrected several of his own transcript points
directly to this seat AFTER the CTO's commit landed:

| Point | CTO's framework doc (06:53Z, stale) | Andrew's later correction to this seat (~07:2xZ) |
|---|---|---|
| Star/watchlist | "a starred/watchlisted company triggers DEEPER research" | **"starring does not do a refresh... star is different, that is a marker."** No refresh/research trigger. |
| Dropdown options | `Trending \| Breakout \| -- \| all securities` | **Adds a third option: `Starred`** — "maybe we have a 'starred' toggle in addition to breakout and trending" |
| Refresh | not mentioned | **New explicit UI action**: a manual Refresh button, toast/spinner upper-right, resolves green on completion — this is what actually queues a harvester pull, NOT starring |
| Trending/Breakout window | cites "the two rolling-7-day rankings" (referencing the chatter-volume mechanism as originally spec'd) | **Ruled 30-day for BOTH trending and breakout** (chatter-volume doc §4a), which also requires a 30-day backfill |
| Chatter metric | not addressed | **Ruled: 0-100 normalized relative to the constituent set**, not a raw count |
| Data store | not addressed | **Ruled: a separate `opal-amgt-articles` table**, shaped like `opal-news-articles`, server-side-computed rankings |

**This is not a disagreement about interpretation — it's a timing gap.** The CTO's doc is dated
correctly for what Andrew had said UP TO that point; it simply predates his subsequent corrections.
**Action needed before DESIGN_SPEC is built against either doc alone:** reconcile the two into one
current framework doc (or have the CTO's doc cite this seat's as the superseding update on the five
rows above) before `C-FRONTEND-FRAMEWORK` gets folded into the PRD — otherwise the surface-build
round risks building against Andrew's SUPERSEDED reading of his own transcript.

---

## 2. Round-2 status, measured not assumed

Per direct check this tick: 4 of 5 round-2 remediation cells have worker completion commits
(`AMGT-r-1` fiscal-year join, `AMGT-r-10` check-face marker, `AMGT-r-12` identity coverage,
`AMGT-r-15` impostor AND-clause — all `pending -> complete`). **`AMGT-r-4` (SA coverage re-exercise)
has no completion commit yet** as of this check. Not itself a defect — it may simply still be
running (it needs live SA raw landed, which takes real wall-clock time) — naming it so round-2's
completeness isn't assumed before it's actually measured.

**This seat's own L4-R coverage sign-off (`2c4aa8a633`) re-verified as still current**, not stale:
the PRD file's last-touching commit is still `a81bd256c9` (unchanged since signing) — confirmed
directly by re-reading the file's git log and content hash, not assumed from the stamp ledger's
different pin namespace (content-hash pins vs. sign-off's commit-hash pins are two different
systems in `prd-stamp.py` and shouldn't be compared to each other directly).

---

## 3. Real architectural holes not yet named anywhere (this seat's own gap, found this tick)

**3a. No specified hand-off through the Identity Layer (S12) for the daily active-monitor set.**
The chatter-volume gate's `active_monitor_set.json` is ticker-keyed (`AAPL`, `NVDA`, ...). None of
the three committed docs say how a bare ticker becomes each platform's own required lookup key
before a harvester can act on it — SA's own symbol slug, Bloomberg's `TICKER US Equity` format,
FT's internal company ID. S12 already exists and already resolves exactly these keys (per the
full-stack vision doc's A2 table) — but nothing wires the chatter gate's OUTPUT through S12 before
handing it to the four harvesters. Needs a named task cell: "resolve active_monitor_set through S12
before dispatch," not left implicit.

**3b. The "server-side computed metrics" store is still named vaguely.** The full-stack vision doc
says scores get written into "the same new `opal-amgt-articles`-adjacent metrics store" — never
concretized. Recommend following the estate's own existing precedent exactly: a SEPARATE computed-
output table from the raw-article table, the same split `news-trending-analysis` already uses
(`opal-news-articles` raw vs. `opal-news-trending-daily` computed) — e.g. `opal-amgt-security-metrics`,
PK `ticker`, SK `date`, holding the day's chatter/price/trending/breakout scores. Naming this now so
whoever builds it isn't left to invent the split.

**3c. The Refresh button's on-demand wake isn't connected to the "stopped-between-runs EC2" design.**
The full-stack vision doc (B1) recommends the four-horsemen box stay stopped between runs, matching
ASTN_WSJFT. The self-healing-auth brief's Refresh action needs to queue a harvester pull on demand.
**Nobody has stated that Refresh needs its own EC2-wake path**, mirroring `inf-jwt-trigger`'s
start-the-box pattern — without it, "hit Refresh" either does nothing (box is stopped) or requires
leaving the box running always (defeats the cost reasoning for stopping it between runs). This is a
genuine build requirement, not a decorative UI detail.

**3d. No portal READ API specified.** S2's existing pattern (`POST /api/private/research/pull`) only
covers WRITES — enqueueing an on-demand pull. Nothing yet specifies the READ path (portal → API
Gateway → Lambda → DynamoDB query) the Lead Panel and Coverage tab actually need to render data from
the new `opal-amgt-articles`/metrics tables. This is a real, unaddressed gap between "the data will
exist" and "the frontend can show it."

**3e. Starred-list ownership is still an open assumption, not a ruling.** Per-user (Adam and Lauren
each have their own starred set) or per-firm (one shared list both see)? This seat's own doc flagged
this as an assumption without getting it actually ruled — it determines the new table's partition
key design, so it should be closed before that table is built, not after.

**3f. Backfill has no assigned owner or task cell yet.** The 30-day historical pull (hitting the
four harvesters' own archives, per Andrew's corrected plan in the chatter-volume doc §4a) is
specified conceptually but nobody is currently tasked with running it, and it can run ad hoc against
today's proven-but-unscheduled scripts — it does not need to wait on B1's EC2 infra. Worth cutting as
its own one-time task cell rather than letting it fall through the gap between "spec'd" and "owned."

---

## 4. What's NOT a hole — stated so nobody re-litigates it

- Cottonwood's own self-healing-auth copy being blocked (`cot-bd-session-trigger`, staged, not
  applied) is a REAL blocker but is Cottonwood's own project's problem, not this project's — already
  flagged separately, not repeated here as an AMGT_RESAPP gap.
- WSJ needing no session-freshness handling is BY DESIGN (stateless, cookieless), not a missing
  piece — already stated in the self-healing-auth brief, restated here only so this scan doesn't
  wrongly re-flag it.
