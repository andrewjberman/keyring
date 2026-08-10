# OPAL_ANALYST — Phase-1 State Brief (0.0.3_BG "Opal Analyst")

**Author:** 4.0.0_SA_CRO~Z · **Date:** 2026-08-10 (~16:20Z) · **Consumer:** 1.0.0_SA_CTO~Z (PRD + registry), then 2.0.0_SA_COO~Z (decompose/dispatch)
**Mandate:** Andrew-direct 2026-08-10 ~1330Z at the MSTR~Z terminal — verbatim on record:
`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260810_OPAL_ANALYST_PROJECT_SPINUP.md` @1ac23a7e1
**Grounding discipline:** every load-bearing claim below carries its source; claims verified LIVE today are marked **[LIVE 08-10]**. Everything else is record-vintage (08-06/08-07) and so marked.

---

## 1. What the product is

**"Opal Analyst" is Andrew's product name (coined in the 08-10 spin-up verbatim — the name appears NOWHERE else in the repo; comp-find: 2 hits, both in the spin-up record) for the 0.0.3_BG_BBGTerminal seat as a product:** a Teams-native data concierge for the Opal team, running on the Bloomberg terminal box, answering data questions from Opal's SERVED artifacts through an approved catalog, under a deny-by-default permission architecture. The agent doubles as the daily Bloomberg pipeline operator (`/terminal-upload` — "still the reason this box exists," prompt.md:104).

## 2. Andrew's dictated intent — the record trail (what CTO~Z's PRD should rest on)

Chronological, each with his operative words where recorded:

| Date | Instruction (verbatim where recorded) | Record |
|---|---|---|
| 2026-08-06 | Redesign off the Port-1 external-contact model: *"nobody uses agents except for me... the simpler solution is actually to structure the prompts for this 0.0.3_BG agent whereby they have a variant on /teams-assist where theyre monitoring their 'Opal Bloomberg' teams account and they are the point of contact for Opal team members via teams."* | LD-0382 §1 |
| 2026-08-06 | Roster is Entra-governed, no roster doc: *"they do not need to be entitled or documented, that is handled already via MS and Entra IDs"* | refs/TEAMS_DUTY.md |
| 2026-08-06 | Bloomberg quota line: *"can view bloomberg but cant do downloads; keeps us in check with our data quota"* | refs/BLOOMBERG_GUARDRAILS.md |
| 2026-08-06 | Per-person long-term memory: *"I also want it to have /logs that it periodically takes associated with threads, so when somebody messages it, it has long-term context on the work it's done with that person"* + two same-day refinements (one file-set per thread; DAILY files, never monoliths) | refs/THREAD_MEMORY.md |
| 2026-08-06 | Rename m365 MCP server → "Opal Gateway"; scope servable verticals page-by-page (news DDB, Model Portfolios, Pod-2 analytics, macro) | LD-0382 §2–3 |
| 2026-08-07 | ACK-FIRST serve loop (`/bbg-teams-assist`): immediate in-thread receipt, then research, then substantive reply with vintage, then record — ruled off his own first thread's delay | BG log 0510-0530Z; skill live |
| 2026-08-07 | Targeted bucket allowlist: *"start setting up a very targeted bucket allowlist ... that guides them on what buckets to use based on user queries"* — default-DENY, widening Andrew-only | refs/BUCKET_ALLOWLIST.yaml header |
| 2026-08-07 | Completion set (mechanical fence + DATA_CATALOG + ack polish) — Andrew-direct at the MSTR~Z terminal | @65d80ab37 |
| 2026-08-10 | Project spin-up: register ANALYST under OPAL macro, code OPAL_ANALYST, *"which facilitates the development of that product"*; site-Z fabric exclusive | @1ac23a7e1 |

## 3. As-built inventory (all committed, agent home `org/tier0_utility/0.0.3_BG_BBGTerminal/`)

- **prompt.md** (~115 lines) — identity binding (opal-gateway-bbg ONLY), launch sequence with identity acceptance gate (step 2a whoami PASS required before any Teams read), operating loop, hard lines. Credential: AWS Secrets Manager `opal/mcp/opalbloomberg-login`; MFA/OTP is Andrew's phone.
- **7 refs**, each a ratified single-axis doc: TEAMS_DUTY (Entra roster, monitor, reply norms) · REQUEST_CATALOG (deny-by-default, 8 approved / 8 denied rows with quotable reasons) · BLOOMBERG_GUARDRAILS (view-free / download-denied + tie-breaker) · PORTAL_RETRIEVAL (measured 2026-08-06 census: 13 S3 channels + 4 DDB tables; truncation-is-not-absence; vintage rules; frozen-legacy-prefix warning) · THREAD_MEMORY (per-thread dirs, daily files) · BUCKET_ALLOWLIST v0.1 (default deny; opal-data-portal-v2 only) · DATA_CATALOG v0.1 (fuzzy query→exact-key routing with keywords + example asks per channel).
- **tools/portal_lookup.py** — the ONLY portal-answer path; full pagination + printed denominators + gzip decode + >1MB projection + query-only news table. EXERCISED 5/5 at build (LD-0382).
- **Skill `/bbg-teams-assist`** — the serve loop IS the operating loop (registered `.claude/skills/bbg-teams-assist/`).
- **Mechanical fence LIVE:** `.tools/hooks/bg-concierge-gate.sh` (170 lines + 79-line test file) wired in `.claude/settings.json:145` — for the 0.0.3_BG serial only: writes confined to own logs/threads/deliverables + tmp (prompt/refs/.claude deliberately unwritable from its own seat); git + cloud mutations denied; Bloomberg download-class tools denied, reference_data capped at 2 securities; ALL opal-gateway (non-bbg) calls denied; email/site-write denied. `# andrew-asked` — this fence predates and complies with the alarm moratorium and no-gates law (it is mechanical enforcement Andrew asked for, @65d80ab37).
- **Thread memory:** 1 thread on record (`threads/2026-08-07-andrew-capability-roster/`, RESOLVED same day).
- Charter lineage: LD-0220 (UA class); redesign LD-0382 @6e0e58552a; completion set @65d80ab37.

## 4. Operational history — it HAS launched and served (one session, 2026-08-07)

The 08-10 spin-up record's "launch was HELD on the identity blocker" pointer is **stale by three days** — the hold was the 08-06 end-of-day state (base MSTR log item 9). What actually happened 08-07 (BG logs 0445-0510Z + 0510-0530Z):

1. First launch taken to ON DUTY. The step-2a identity gate **did its job once live**: first OAuth mint came back `whoami = Andrew Berman` → GATE FAIL, zero Teams reads, held; Andrew re-minted as opalbloomberg@ → PASS.
2. A live dual-identity defect in the stock Teams monitor engine was caught **before arming** (see §6.1) and mitigated with a session-local identity-pinned wrapper.
3. First live serve completed end-to-end: Andrew's capability-roster ask; send first DENIED by the gateway tier guard (key was READ_ONLY); 0.7.0_AE_CloudOps~Z landed WRITE_CAPABLE/STANDARD_EMPLOYEE @798cff68b; reply **DELIVERED 05:26:19Z, from.displayName "Opal Bloomberg"** on the sent artifact.
4. Three silent broker-registration drops observed (same PID, zero mail lost); banked by MSTR~Z as data points, cause unconfirmed.

## 5. Current state — measured today, 2026-08-10

- **Identity blocker: RESOLVED and HOLDING.** **[LIVE 08-10]** I called both gateways from this box: `opal-gateway-bbg` whoami → **Opal Bloomberg** (opalbloomberg@opalinvest.com); `opal-gateway` whoami → Andrew Berman. The dual-identity setup is live and correctly separated at the server-identity layer.
- **The agent is DOWN (dormant, not broken).** **[LIVE 08-10]** Broker: `0.0.3_BG_BBGTerminal` NOT REGISTERED; no session since 08-07. One unread inbox message sits at its top level since 20260807T1821Z (MSTR~Z's completion-set notification — includes the instruction that the mechanical fence loads at next session cycle).
- **No project/PRD/TO structure exists.** No `org/projects/OPAL_ANALYST.json`, no TOs reference it. `to-check` on my own serial: 0 TOs. That structure is exactly what phases 2–3 create.

## 6. Open items — the honest register (owners as of the record)

1. **⛔ RELAUNCH GATE — teams-watch.py identity defect UNFIXED at source.** **[LIVE 08-10]** `.claude/skills/teams-assist/teams-watch.py:54` still selects the freshest-expiring opalinvest.dev token across ALL mcpOAuth records, identity-blind — with both tokens valid on this box (verified above), whichever expires later wins, and on 08-07 that was **Andrew's**: the stock engine would poll Teams AS ANDREW. The 08-07 mitigation was a **session-scoped scratchpad wrapper (`teams-watch-bbg.py`) which died with that session** — a relaunch today re-runs the race unless the wrapper is recreated or the durable fix (a required `--server`/`--identity` arg) lands. Durable fix owed by **0.5.0_AE** (engine owner), open since 08-07. **This is the single highest-priority pre-relaunch item and belongs in the PRD as a P0.** (Also banked in site-Z memory: verify identity-pin before any 0.0.3_BG relaunch.)
2. **Per-identity tool allowlist at the gateway.** STANDARD_EMPLOYEE tier passes ALL mutating tools; today the request catalog + client-side fence are the whole fence. Narrow server-side per-identity allowlist routed to **0.5.0_AE** 08-07, open.
3. **Portal-bucket + ycharts gateway entitlements: STAGED, not live** (LD-0382 residual). The tools are VISIBLE on `opal-gateway-bbg` from this box — availability is not authorization (CLAUDE.md); activation is an **Andrew word**, not yet given on any record I found. PRD should carry the activation decision explicitly.
4. **Broker silent-drop pattern** — 3 unexplained same-PID registration drops in one session (08-07). Filesystem+watcher path held, zero mail lost. Data points with MSTR~Z; not a blocker; do NOT build a monitor for it (moratorium) — but a PRD reliability section should name it.
5. **Alyssa machine gateway re-key** — at Andrew (LD-0382 residual). Unverified from here.
6. **Record-hygiene:** the 08-10 spin-up record carries the stale "launch HELD" line (§4 above) — MSTR~Z notified via this brief's hand-off; the record file itself is MSTR~Z's to annotate.

## 7. CRO read — what the PRD should cover (recommendation, not dispatch)

The build phase is DONE and exercised; what does not exist is the **product/operations layer**. Suggested PRD axes:
- **P0 — durable identity pin** (item 6.1) + a written relaunch procedure (launch checklist exists in prompt.md; the wrapper dependency does not).
- **Steady-state operation:** who/what brings the seat up daily (it is a terminal-box seat, not fabric-spawned), session-cycle expectations, and the fence-loads-at-session-start caveat.
- **Entitlement roadmap:** ycharts + portal-bucket activation decision (Andrew), server-side per-identity allowlist (0.5.0_AE), catalog/allowlist widening protocol (already Andrew-only by design — keep it).
- **Capability growth as R&D:** the catalog's 8 approved rows are v0.1; the DATA_CATALOG fuzzy-routing layer is the natural growth surface (new channels, new verticals per LD-0382 §3's page-by-page scoping).
- **Memory/thread growth:** THREAD_MEMORY discipline is specified; nothing sweeps/integrates thread records yet ("integrators sweep them" — prompt.md — but no integrator is named).
- Explicitly OUT unless Andrew asks: alerts/monitors on the seat (moratorium), any new approval gates (no-gates law), any standing parallel/shadow serve path.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-find | `"Opal Analyst"` | 2 hits / 24,497 files scanned (denominator printed) — name exists only in the 08-10 spin-up record |
| — | Raw greps limited to pipe-scoped (`git log \| grep`-class) + single-file `grep -n` on teams-watch.py (operational inspection of a named file, not an estate search) | — |
| live primitives | `whoami` on both gateways; broker `get_agent_status` x2; `TaskOutput` on own Monitor | grounded §5 |
