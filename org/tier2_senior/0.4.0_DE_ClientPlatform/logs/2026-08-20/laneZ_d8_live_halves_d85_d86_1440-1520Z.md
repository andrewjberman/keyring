# D8_LIVEEDIT.TO-AB-SITEZ -- D8-5 / D8-6 LIVE UI halves against the applied API (Act 1 at registration)
**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT
**serial:** 0.4.0_DE_ClientPlatform~Z (lane ~Z, base-folder log per convention)
**window:** 2026-08-20 1440Z -> 1520Z (respawn at the COO~Z /drive tick-1 swap; GO 2114 + amendments 2216/2355 read at registration)
**TO:** D8_LIVEEDIT.TO-AB-SITEZ (pending; CTO~Z ACCEPTED 7/9 @21e8517079, D8-5/6 live halves routed to this seat as first act)
**Vintage:** PRD docs/architecture/D8_LIVE_EDIT_MODALS_PRD.md @7416fb46d0; portal DEV ccda8711 (edit surface) + f524ef6e (instrument, this window)

## Result: D8-5 PASS, D8-6 PASS -- instance 9/9, validator rc=0 positional, unpiped

Proof instance `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/D8_LIVEEDIT.TO-AB-SITEZ_PROOF_OF_SPEC.json`
now carries MEASURED evidence on D8-5 and D8-6 (the last two UNCOMPUTABLE-BY-CONSTRUCTION rows):
`python .tools/proof-of-spec-check.py <instance> D8-1,...,D8-9` -> `acceptance rows=9 | violations=0 | VALID`, rc=0.
(First run rc=1 on one schema enum -- `controls.determinism.status` must be STABLE/UNSTABLE/N-A, I had written PASS;
corrected, re-run rc=0. Recorded so the rc history is honest.)

### Identities (the premise of the ack: "I can hold both live identities")
Two RS256 portal tokens minted here from Secrets Manager `opal/auth/jwt-private-key` (readable by this seat's
AWS principal; key never printed, token files in the session scratchpad only, 60 min exp), claims mirroring
`infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts` (iss `opal-portal-auth`, aud `opal-portal-api`):
internal `d8-live-internal@opalinvest.dev` firmId=opal-capital userType=Dev; non-employee
`d8-live-partner@49financial.test` firmId=49financial userType=Advisor. Same method as the laptop AE's D8-3/4
battery. Pre-run controls on www.opalinvest.dev `/api/scoped/portal-content`: no token -> 401 (negative),
internal -> 200, partner -> 200 (readable by all viewers), count=0 (no residue); the same GET through the
local vite proxy (:5175 `/api` -> CloudFront) -> 200, proving the DEV page's path carries the bearer to the
live route.

### Instrument (portal DEV f524ef6e, `scripts/ui-smoke.mjs`, no product code)
- `--token <jwt|@file>`: REAL bearer in the stubbed `/auth/refresh` session; the session user is DERIVED
  FROM THE TOKEN PAYLOAD so the client gate (`isInternal()` = firmId) and the server (`_is_internal` from
  the authorizer context) read ONE identity plane.
- `--click` repeatable + `--fill "<aria-label>=<text>"`, run in argv order (tab -> modal -> edit -> save);
  on a miss the run prints the control names that WERE on the page. That diagnostic is how the first
  miss resolved itself: the heatmap trigger's accessible name is the hyphenated
  `Short-Term - open portfolio details` (legacy alias in the model map), and the ModelPortfolios tab is
  labelled `Benchmark`, not `Performance`.
- Hazard found + kept out of the record: the harness's heredoc layer unescapes `\\`, so a patcher written
  with `'\\n'` matched a real newline and failed its own anchor; rewritten with `chr(92)`. And a bash
  `A=.. && B=.. && ( cmd ) &` backgrounds the WHOLE and-list, so D/E first ran with empty vars (rc=1,
  PNG path `C:\D_...`); re-run with the assignments in the parent shell. Both are instrument-side.

### The six live runs (DEV :5175, portal DEV ccda8711 + f524ef6e, proxied to www.opalinvest.dev)
| run | identity | route -> steps | netlog portal-content | screenshot read |
|---|---|---|---|---|
| A | internal | /portfolios -> Benchmark -> Short-Term modal -> Edit -> fill `D8LIVE-150632Z ...` -> Save for all viewers | GET 200, **PUT 200 model_key_notes%23st**, GET 200 | saved text + "Live override by d8-live-internal@opalinvest.dev - 8/20/2026 11:06:57 AM - masking the repo copy" + Reset link; live figures (YTD 2.33 / 1Y 3.92 / SI 4.69 / yield 4.00 / 17-83 makeup) |
| B | internal, NEW profile | /positioning -> Short-Term modal (the OTHER call site) | GET 200 | the edit rendered + pencil + notice + reset |
| C | internal, new profile | /portfolios -> Benchmark -> Short-Term modal | GET 200 (+ model_portfolio_benchmarks.json / etf_returns.json = Benchmark tab live) | same as B on the heatmap call site |
| D | non-employee | /positioning -> Short-Term modal | GET 200 | override text visible, NO Edit / notice / reset row |
| E | non-employee | /portfolios -> Benchmark -> Short-Term modal | GET 200 | same, NO affordance |
| F | internal, new profile | /positioning -> Short-Term modal -> Remove the override... -> Confirm reset | GET 200, **DELETE 200 model_key_notes%23st**, GET 200 | 4-paragraph repo-copy baseline restored + pencil, no notice |
Server reads (curl, internal token): after A count=1 `model_key_notes#st` updated_by=d8-live-internal@opalinvest.dev
(token subject) updated_at=2026-08-20T15:06:57.087Z; after F count=0. **Residue: none.** All six rc=0, LOC == route.
PNGs + netlogs: session scratchpad `d8live/` (A_internal_heatmap_save, B_internal2_positioning, C_internal2_heatmap,
D_partner_positioning, E_partner_heatmap, F_internal_reset_positioning; A-F.netlog), each READ per /frontend-dev.
Colour law on every frame: light silver dialog, dark text, dark-outline Edit, dark/55 notice -- no light text or
ghost-white control on the canvas.

### Rider half-lives closed by this pass
Q1 (all-internal affordance + server control): pencil for internal, none for the partner, on BOTH call sites, LIVE.
Q2 (Key Notes prose only): only the Key Notes pane carried the edit; the six-field figures pane rendered live and untouched.
Q3 (store-wins, losing path visible): the override notice names WHO/WHEN and "masking the repo copy" at the read
surface, the explicit reset control works live (DELETE 200), and the baseline returns.

## Commits
- portal DEV `f524ef6e` feat(ui-smoke): --token / repeatable --click / --fill (instrument; my author + committer).
- workspace (this commit): proof instance flip + this log. Portal gitlink advance left for MSTR~Z's integration
  (uncommitted here, deliberate). Lane commits, never pushed.

## MCP traffic (window)
Received: COO~Z GO 2114 + queue notes 2174/2216 + GO amendment 2355 + TO-F PENDING 2390 + RAVC-4(b) 2389;
AE~Z 2371 (submit contract) + 2398 (Rule-24 table); CTO~Z 2379 (gate read + SoD ruling); MSTR~Z 2375
(LD-0428 + Rule-24 widenings, read from the ref). Sent: RAVC-2 ack 2383/2384 (CTO~Z + COO~Z); D8 report follows this commit.
All READ-acked (ack_messages).

## Compiler Tools
| Tool + invocation | Result | Note |
|---|---|---|
| comp-which "how do I grep the repo" (A.3 exercise) | forwarder RAN; 98/99 comp-tools resolve bare | startup |
| comp-find 'd8-battery' org | 2 hits / 14116 files | located the laptop battery's identity record |
| comp-find 'RS256' org/tier2_senior/0.7.0_AE_CloudOps | 23 hits / 1210 files | auth model: custom RS256 JWT, localStorage accessToken, Bearer on every call |
| comp-find 'jwt-private-key' infra/aws | 15 hits / 7606 files | the signing source `auth-handler/src/jwt.ts` (iss/aud/claims) |
| rail-checked raw: `aws sts get-caller-identity`, `secretsmanager list-secrets`/`get-secret-value` (key never printed) | principal Andrew_Berman; key reachable | applied-plane identity mint -- no comp-tool models a caller's secret reach |
| rail-checked raw: curl controls on www.opalinvest.dev + :5175 | 401 / 200 / 200 / 200 | positive + negative + proxy-path controls before the UI runs |
| proof-of-spec-check (positional D8-1..9) | rc=1 (enum) -> rc=0 VALID | the validator is the gate, run unpiped |
No comp-transform/comp-routes this window: no component or route changed (the instrument is a script, the product
code is ccda8711's); the build-window runs are in the 2026-08-19 log.

## Surprises (surprise channel -- one line each to COO~Z, no action)
1. audit-archive-invoker at startup: 3 NON-APPEND-EDIT + 1 ERROR-FAILCLOSED findings (site-Z cross-device baseline class, already in FINDINGS.md) -- surfaced, not chased.
2. Working tree carried AE~Z's uncommitted-at-the-time half (b) files (ticket_center lambda + TF) -- shared tree; I did not touch them.
3. The dev server on :5175 was already live at my respawn (not mine; inherited after `curl /src/main.tsx` proved it serves the portal DEV tree at ccda8711).

## Next
ACT 2 = TO-F half (a): read the TO at/after @b90722ea89 (+ @562a74f4f7 status), PRD sec 7.3, AE~Z's (b) record
@4bede18189/@2e7fae20d3; Phase-1 checks; the client-facing form on portal DEV (TradeSubmission primitives,
D8 cohort check @ccda8711 for board-vs-form); D7F-1/D7F-2 + the ONE proof instance; D7F-3..10 portal-side after
the (b) apply is CONFIRMED over the bus.
