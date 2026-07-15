# 0.5.0_AE_OpalETL -- reset-session resume: ANDREW-NOW manual fire + part-2 wave 6/6 (2026-07-15 18:13-19:0xZ)

**archetype:** MIXED (DEPLOY + VALIDATE + IMPLEMENT)

Resume surface: handoff_context_reset_1809Z.md @ d26424e81. Everything below happened in one
~50-minute window; the handoff's three work items all closed or advanced ahead of schedule
because a sovereign re-time landed mid-startup.

## 1. Startup (handoff sequence, executed exactly)

- **Orphan reap:** identity-probe first -- both pairs found at the handoff's exact PIDs and
  command lines; killed 864898/864955 (own inbox watcher) + 876382/876463 (landing watch).
  **The `0.5.0_AE_OpalETL~A` watcher pair (572655/572694) left UNTOUCHED** -- the sovereign
  delegate's serial, not mine (own-serial scope).
- register_agent (PID 26332) + session serial file (9ac90484...) + owned-paths hook (already
  wired) + .agent_context + `comp-to OPAL_ASSETS.C5.smartx-holdings-activity-etl`. Zero crons.
- Inbox Monitor armed (task bj0zujfk6, persistent) -- delivered 2 waiting messages instantly.

## 2. SOVEREIGN RE-TIME (preempted the handoff plan)

**ANDREW-DIRECT via COO terminal, relay 182059Z, verbatim on COO's record:** *"THe second order
is that we are not waiting on a scheduled run for the ETFs, that goes NOW, 0.5.0_AE can do that.
Furthermore we do not use msn, we use the issuer route only."* CTO formal amendment 182228Z:
family 5->3 tables (fact_quotes/fact_funds STRUCK, Q3 MOOT, sparsity law RETIRED, Q1/Q2
unchanged); v1.1.0 untouched pre-scheduled-fire; wave queues behind the manual fire.

## 3. Manual ETF fire (Andrew-NOW) -- all three proof legs banked

- Pre-fire fresh grounding on the live primitive: CodeSha256 == 40KaO/7j... (source-map tie),
  env BRONZE_BUCKET=opal-data-assets / GRAMMAR=monolith / SILVER_ROOT=_cloudprobe/, State Active.
- Invoke 200, no FunctionError: 4 funds, 4 bronze objects, 729,867B; tiers=[filepoint,
  trueshares], degraded=[]; **msn NEVER FIRED -- issuer route carried everything; PFOE
  sole-source guard resolved on actuals** (filepoint-served: 2 dailynav + 23 holdings rows).
- Post-fire harness (staged, old-session scratchpad): C4 AC1 listing = 4 keys @ /20260715/;
  **attestation tie: listing byte-sum 729,867 == producer bronze_bytes**; bytes OPENED -- all
  4 TS_PATTERNS matched both funds (as_of Jul 14 = T-1 correct), both CSV headers == expected,
  Q2 conservation ties in-file (85+23=108==delivered).
- Parity gate UNPIPED: **correctly REFUSED at 2/3** (07-13 + 07-14 GREEN 52 fields 0 mismatches;
  07-15 row pends the laptop leg tonight). Refusal = threshold integrity, pre-framed by COO.
- **CTO 183506Z: C4 AC1 CLOSED at his gate (independent listing tie). COO 183555Z: C4 TO
  FLIPPED COMPLETE @ b9407f7ea; V2-1 GO stays held on tonight's day-3 row.** S1 cert = two
  cells, both riding tonight (day-3 parity; scheduled-trigger leg).

## 4. Landing watcher v2 (wrong-axis self-catch, second in two days)

Tonight's scheduled fire REWRITES the same /20260715/ keys the manual fire wrote -- the v1
key-existence watcher would have CORE-LANDED false-positived at 21:56Z on manual keys. Killed
v1, wrote v2: a key counts only if **LastModified >= 21:55Z**; msn key appearance = FINDING
(post-strike stray). **Instrument exercised before arming: positive control (any_keys finds the
2 manual keys), negative control (fresh_keys excludes them), mutant (backdated cutoff passes
them -- the discriminator is load-bearing), None-row guard.** Armed (task bhzqhjzpl). CTO
approved the fix as the correct instrument.

## 5. Part-2 conversion wave: 6/6, ZERO refusals (CTO batch GO 181013Z, pinned order)

| # | table | partition | objs==pin | rows vs pin | landed read-back |
|---|---|---|---|---|---|
| 1 | fact_account_allocations | 07-14 | 7,066 | 23,213 in [19k-25.5k] | 23,213/21c/1,800,109B |
| 2 | fact_nonzerosleeve | 07-14 | 1 | 511 EXACT | 511/24c/102,017B |
| 3 | fact_account_detail | 07-14 | 91 | 91 EXACT | 91/31c/35,583B |
| 4 | fact_model_holdings | 07-15 | 11 | 164 EXACT | 164/15c/25,227B |
| 5 | fact_model_performance | 07-15 | 11 | 6,456 EXACT + multiset EXACT | 6,456/21c/308,132B |
| 6 | fact_model_changerequests | 07-15 | 11 | 1,058 EXACT, vocab to the count | 1,058/16c/69,945B |

Highlights: presence laws 0 violations fleet-wide on 23,213 rows (assert-later ladder earns both
frame RAISEs next library touch); nine-bool law silent on all 91; two-multiplier 164/164;
fractional transactions 1,280 == DS's independent count to the row; event-grain 0-collapse.
Drivers 2-6 authored this session off the staged run-1 template (citation typo a289cfe2 ->
a289cc2fe self-caught PRE-RUN -- a wrong-vintage cite in an immutable manifest is worse than
none). Manifests at smartx/platform/meta/pulls/{20260714,20260715}/. **smartx silver = 12
tables LIVE. CTO 185322Z: wave CLOSED-ACCEPTED whole; cert build-execution residual CLOSED.**

Findings (both loud, neither a refusal):
- **THE ENUMERATION GAP (the day's real finding):** wave-1's 9 model-open-outside-map ids
  resolve to **3 living models NOT in the 11-model resolver set** (Vanguard S&P 100/0 ETF
  Model Portfolio 4ea784d7... x7 allocs; Martin U.S. Investing 0a1cd776... x1; Suncoast
  Dividend Growth 1115d688... x1). Hypothesis (a) vintage-skew REFUTED directly on open_ts
  (opens 2023-09-25 -> 2025-11-07). Model tier pulls 11 of >=14 living models; every model-tier
  feed inherits the gap; will NOT self-heal. **CTO: cert's replacing named residual; THE FIX IS
  MY LANE (feed-9 producer), sequenced TOMORROW** -- find where the enumeration gets its 11
  (endpoint vs static config vs roster; grant scope / pagination / enterprise filter).
- 1/511 nonzerosleeve custody carrier is 9-DIGIT numeric (DS sheet said 8-digit; 510/511 true
  on full read) -- preserved byte-faithfully, DS notified for a sheet footnote.

## 6. ETF design record AMENDED (supersede-in-place, yaliu form)

ETF_SILVER_FAMILY_DESIGN_20260715.md: amendment banner (sovereign ruling verbatim-cited +
CTO 182228Z); tables 4/5 struck in-place; Q3 preserved-verbatim-marked-MOOT; sparsity law
retired; measured landed-bytes evidence folded into section 2 (TS values, 13/14-col header
ties, conservation denominators); msn line re-scoped to deployed-artifact-only with
landed-msn-key=FINDING. DS owns pyarrow pins + skeletons off the same bytes (their 182428Z
plan; contract rules 6-8 fill confirmed against landed keys verbatim, rule 9 struck).

## Compiler Tools

| tool | use | result |
|---|---|---|
| comp-to | session TO context (OPAL_ASSETS.C5) | OK, race-free per-session file |
| comp-grep | "ligament" definition hunt (docs/org/infra) | 7 matches / 3 files; found PRD sec 4b P-3 four-verdict definition |

Raw-aws calls this window were all OPERATIONAL (lambda invoke, get-function-configuration
pre-fire verify, s3api listing inside the watcher/controls) -- no comp-tool inspection gap.
Standing gap unchanged: no comp-tool covers monolith smartx/ETF families yet (noted in the
last three logs).

## MCP traffic (this window)

In: COO ANDREW-DIRECT relay 182059Z; CTO amendment 182228Z; DS coordination 182428Z; CTO
accepts 183506Z / 184005Z (no-halt) / 185322Z (wave closed); COO accept + C4 flip 183555Z.
Out: 2 RAVC ACKs; manual-fire triple verdict (COO+CTO); DS landing announcement + rule-6/7/8
confirmation; wave-1 evidence; wave-complete evidence (CTO) + pins-performance note (DS) +
board note (COO). All loops closed; nothing pending on me except tonight's clock.

## Next Steps

1. **[TONIGHT 21:56Z-] watcher v2 fires; at SCHEDULED-CORE-LANDED: harness on refreshed bytes ->
   unpiped parity gate (day-3 read; laptop leg must have landed) -> report to COO + CTO.**
   V2-1 GO auto-rides a GREEN 07-15 row. A DEADLINE-MISS hits only the scheduled-trigger leg
   (manual-fire legs banked). NO ad-hoc re-fire (CTO 230335Z stands).
2. [TOMORROW] feed-9 enumeration fix (my lane): where does the model tier get its 11; why are
   3 living models outside; then the 3 models' feeds land -> the 9 ids map -> DS pins update.
3. Cutover order untouched: 3d parity -> SILVER_ROOT="" -> verify live write -> disable legacy.
   msn code-strike rides CTO's artifact-swap gate AFTER tonight.
4. [0.4.0_DS] event-driven: ETF pyarrow pins + skeletons off landed bytes; model-tier pin
   updates when feed-9 fix lands.
