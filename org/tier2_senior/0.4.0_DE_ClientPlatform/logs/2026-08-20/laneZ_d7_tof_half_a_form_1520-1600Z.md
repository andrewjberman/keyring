# D7_TICKETING.TO-F-SITEZ half (a) -- the CLIENT-FACING intake form, built + exercised against the applied API (Act 2)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DE_ClientPlatform~Z (lane ~Z, base-folder log per convention)
**window:** 2026-08-20 1520Z -> 1600Z (immediately after the D8 close @00d22532ac)
**TO:** D7_TICKETING.TO-F-SITEZ (pending @562a74f4f7; JOINT @b90722ea89; read at/after @5dc7756ac7 incl. the D7F-11 fold)
**Vintage:** PRD sec.7.3 @a765d66f82 as amended @1d524d06ca/@2cb58ecf22; head_version @91fe6afbca; half (b) @4bede18189 + @1fd9ef2750, applied ticket-center-v1.1.0 -> v1.1.1

## Result: half (a) COMPLETE -- portal DEV @483b896c; ONE proof instance 12/12, validator rc=0 positional D7F-1..12, unpiped

`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/D7_TICKETING.TO-F-SITEZ_PROOF_OF_SPEC.json` --
`python .tools/proof-of-spec-check.py <instance> D7F-1,...,D7F-12` -> `rows=12 | violations=0 | VALID`, rc=0.
(rc history, honest: first run rc=1 -- the validator's artifact-coverage check wanted `artifact_covered_by`
on the (b) lambda artifact row; added, re-run rc=0. The A_03 class doing its job.)

## What landed (portal DEV @483b896c, my author; lane commits, never pushed)
- **`src/api/endpoints/ticket-intake.ts` (NEW)** -- the form's ONE call `submitTicketRequest` (body EXACTLY
  {ticket_type, title, description?}; identity/firm/source server-derived) + `intakeErrorMessage` (surfaces the
  API's own `error` string). D7F-1 split machine-read: `comp-routes trace SubmitRequest` -> Calls =
  intakeErrorMessage, submitTicketRequest ONLY; tickets.ts does not import the submit call.
- **`src/pages/SubmitRequest/` (NEW)** -- composition = TradeSubmission page pattern (PageThemeProvider >
  PageHeaderCleanBadge > Panel); controls = the TicketCenter create-panel idiom; internal-only board link via
  `useAuth().isInternal()` (the D8 cohort predicate -- no fork); ack = received-time (ET) + cutoff from the
  201's `cutoff_et` field, fallback wording without a literal time.
- **`src/App.tsx`** -- /submit-request route + Tools nav item (Send); **/ticket-center route hardened
  `requireInternal`** (the existing firmId==opal-capital ProtectedRoute predicate) on top of the firm
  allowlist that already omits the board for every partner firm.
- **`src/lib/firmAccess.ts`** -- '/submit-request' added to 49financial / cottonwood / demo. **Inflection
  deliberately NOT added** (no Tools section, Andrew-direct 2026-05-28) -- surfaced, not decided.
- **`src/api/endpoints/tickets.ts` + `TicketCenter.tsx`** -- TICKET_TYPE_LABELS consolidated to ONE exported
  copy (the board's local copy dropped) so the two surfaces cannot drift.
- Checks: tsc -b rc=0; eslint rc=0 (7 files); comp-transform schema-check SubmitRequest (no data props;
  types WARN = the recorded pre-existing class); comp-cache collisions none; branch DEV throughout.

## Exercised against the APPLIED API (www.opalinvest.dev via the DEV :5175 proxy; minted identities)
- **D7F-1** both directions: partner renders the form, nav has NO Ticket Center; partner /ticket-center ->
  REDIRECT /market; internal reaches the board (separate positive control); client LIST/METRICS 403 vs
  internal 200. **D7F-2**: form + confirmation frames READ, colour law holds.
- **D7F-3 portal-side**: a real partner-session form submission -> POST 201, ticket TCK-20260820-4a3b2b89;
  row READ BACK: source `dashboard_form:49financial`, requester = the SESSION identity, created_by
  `svc-ticket-form`, events[0] actor svc-ticket-form. (FIRST PASS was the laptop's TCK-20260820-f450ec73.)
- **D7F-4** live: body `requester_firm` -> 400 verbatim, nothing written. **D7F-5** client POST /tickets ->
  403 {CREATE, client-human}. **D7F-6** client GET/metrics 403 + internal 200 (separate); svc-ticket-form
  READ 403 = battery row on the real handler (live pair = TO-D's, stated). **D7F-7** client claim 403;
  internal claim 200 + assignee complete (SoD-strict v1 STATED in the row per CTO~Z 2379/2442).
- **D7F-8 EXERCISED**: catalog_gate imported pure against the live catalog home (v0.2, 48 rows) -- 8/8
  ticket-key x principal cells refuse with the FLOOR reason; floor-removed mutant flips the refusing branch
  to 'off-catalog' (the floor was the refuser); served-row positive control passes.
- **D7F-9 both named mutants in SCRATCH** (repo untouched): (i) LIST += client -> failures=2 (the deny test
  flips); (ii) LIST -= svc-analyst-intake -> failures=1 (403 != 200, the duty's read); restored 13/13.
- **D7F-10**: no new IAM/secret/table in the apply (simulate leg N/A by construction); deployed-bytes =
  ledger L4 byte-match; no service token minted here (TO-D's custody act); non-moving svc LIVE cells NAMED.
- **D7F-11 BOTH branches exercised live**: fallback (v1.1.0, no cutoff_et) -> "after the daily cutoff"
  wording, no literal time (1538Z frame); after the re-pinned @1fd9ef2750 apply (v1.1.1, 0.7.0 confirm
  1546Z) -> a second submission TCK-20260820-e2c828f2 renders "after 2:00 PM ET" FROM THE RESPONSE FIELD
  (1548Z frame). The only 14:00 home stays the Lambda env. Both test tickets claimed + completed by the
  internal identity -- board left clean.
- **D7F-12**: validator rc=0 positional; AE~Z's Rule-24 authz-matrix table @2e7fae20d3 cited into the row.

## MCP traffic (window)
Received + READ-acked: MSTR~Z apply-confirm 1529Z + re-pin-applied 1546Z; CTO~Z 2442 (cutoff_et RIDES +
catalog home); COO~Z 2456 (TO folds @5dc7756ac7) + 2459 (ledger read) + 2469; AE~Z 2465 (@1fd9ef2750 landed).
Sent: 2433/2434/2435 (the cutoff_et one-home proposal -- APPROVED and landed same hour); D8 report 2416/2417;
this half (a) completion report follows the commit.

## Compiler Tools
| Tool + invocation | Result | Note |
|---|---|---|
| comp-routes behaviors / trace TicketCenter / trace SubmitRequest | behaviors 12+13 cover the path; board = 5 board calls; SubmitRequest = 2 intake calls ONLY | the D7F-1 split, machine-read |
| comp-cache map + collisions (pre/post) | no ticket keys, no collision rows | form state stays out of the query cache |
| comp-transform schema-check TicketCenter (baseline) + SubmitRequest (post) | WARN no types.ts both (pre-existing class) | no data props on the form |
| comp-iam service opal-ticket-api | FLOOR 12 DDB calls [UNKNOWN], action set unchanged | no new resource -> no simulate target (D7F-10) |
| timeout 90 comp-blast create_ticket | TIMED OUT (site-Z graph-backend class, as AE~Z/CTO~Z named) | consumers grounded via trace + tickets.ts |
| comp-find (cutoff / catalog_gate / FLOOR_PATTERNS / test defs) | one CUTOFF_ET home main.tf:137; floor :42/:82; 13 tests | denominators printed each run |
| comp-to D7_TICKETING.TO-F-SITEZ.client-facing-intake-form | session TO context set | race-free per-session |
| proof-of-spec-check positional D7F-1..12 | rc=1 (artifact-coverage) -> rc=0 VALID | rc unpiped both runs |

## Surprises (surprise channel, one line each -- no action taken)
1. CUTOFF_ET was a config with ZERO consumers (env set, read by nothing) -- surfaced 2433, CTO~Z ruled the
   response-field shape 2442, AE~Z landed @1fd9ef2750, applied v1.1.1 same hour. Closed within the window.
2. Inflection's /submit-request omission: the 05-28 no-Tools ruling would be reinterpreted by adding it --
   left out, surfaced to COO~Z here and in the instance.
3. comp-blast timed out here too (the named class).
4. portal bun.lock pre-existing modification (not mine, not committed).

## Current state / next
- Portal DEV: ccda8711 (D8) -> f524ef6e (instrument) -> 483b896c (the form), all mine, unpushed; workspace
  gitlink advance rides MSTR~Z's integration. Both halves of TO-F have their rows; the ONE instance is
  VALID rc=0. Acceptance = CTO~Z; validation = COO~Z; TO status flips are COO~Z/MSTR~Z lane acts.
- Test residue: none (2 test tickets completed; D8's store override reset earlier; no portal-content rows).
