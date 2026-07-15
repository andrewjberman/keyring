# ~A lane -- directives #3-#6 close-out: registry renames, Cognito hallucination kill, silver-canvas color law + archetype sweep (07-14 20:20Z -> 07-15 15:45Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, SCRIBE

Lane: 0.5.0_AE_OpalETL~A (Andrew sovereign-delegate lane; base serial's pipeline work NOT in scope here).

## Window summary

Six workstreams, all Andrew-direct, all RAVC-closed:

1. **Directives #3-#5 execution tail (07-14 evening, previously un-logged):** rulings folded
   (8f3366024), delegate brief + #4 verbatim (e5391e8cb), registry renames TCKT_CENTER->OPAL_TICKET
   + PFMG_TAXSMA->OPAL_TAXSMA with OPAL macro-row rule-6 lag close (16ab9c9bc, audited
   GIT_COMMIT_AUTHOR_OVERRIDE=ANY_EXEC). COO spot-checked clean ("nothing owed").

2. **Cognito assessment (07-15, Andrew ask):** Andrew suspected "Cognito-backed" was hallucination
   -- CONFIRMED on three grounded checks: live `apigatewayv2 get-authorizer naqxlm` = REQUEST-type
   Lambda `opal-portal-authorizer` (name `portal-jwt-authorizer`); `cognito-idp list-user-pools` =
   ZERO pools in acct 313476888478; the bundle's "cognito" strings = vendored @aws-sdk submodule
   maps. Truth: homegrown RS256 JWT (auth-handler signs; authorizer verifies via Secrets Manager
   `opal/auth/jwt-public-key`). Propagation: I copied the false comment from
   partners-api/api-gateway.tf:7 into ticket-center/main.tf:40. Mine fixed @ c5a9418dd; root
   surfaced to 0.7.0_AE_CloudOps who fixed @ 5853ddc76 same hour. No functional defect -- routes
   were always wired to the correct authorizer; annotation-only.

3. **Andrew-direct #6 (silver-canvas UI):** ticket-center page shipped light-on-light (white-text
   idiom directly on the SILVER canvas). Root cause: copied SecurityScanner's text idiom without
   its Panel containment, never rendered the page pre-ship; aggravated by stale "light blue"
   comments on tokens that resolve DARK NAVY. Fix exercised, not asserted: headless
   before/after screenshots (playwright-core + system Edge fresh profile; auth via stubbed
   /auth/refresh real-shaped session; credentialed-CORS exact-origin echo), all three states
   (empty/populated/form-open). Canvas grounded live: rgb(195,202,218) = --palette-silver
   222 24% 81%. Panel tiers grounded live: chart/mixed 25%, header/DarkCard 11%, NestedCard 17%,
   nested/heatmap LIGHT 74%.

4. **Standing controls (the "inform the process" half):** NEW portal/CLAUDE.md (color law +
   live-resolved container table -- auto-loads for any agent under portal/); NEW
   portal/scripts/ui-smoke.mjs (credential-free headless screenshot instrument; --fixtures;
   MSYS route de-mangle); NEW /frontend-dev skill (render->LOOK->commit loop + the traps).
   Andrew scope ruling recorded verbatim (25b9390a8): NO estate sweep of pages -- existing pages
   developed+clean; defect class = NEW-page creation; success criterion = coloring never needs
   restating. Gate candidate routed by CTO to comp-learns backlog item 6 (WARN-level,
   announce-then-enforce, behind parity cert).

5. **Design-informing-surface sweep (Andrew mid-turn directive):** repo-wide correction of the
   design language's stale vocabulary to the TRUE archetypes. Key finding: "light blue" has
   ALWAYS meant the LIGHTER OF THE NAVIES (contentPanel, today opaque 221 28% 25%) -- never
   absolutely light; and designTokens.ts BG_COLORS carried a pre-silver-era "#0f0f1a darkest
   page" claim (the root false archetype: docs said the canvas is near-black). Corrected:
   designTokens.ts, DESIGN_SYSTEM.md (CURRENT-TRUTH banner + both token tables + tree/example
   labels + two snippets prescribing --bg-card for a light outer), PANEL_PRIMITIVES_API_DESIGN.md
   (banner; mapping drifted from shipped code), Panel/SectionCard/DarkCard/NestedCard/
   PanelExamples + panels README (stale "project root" pointer -> docs/guides/), SSCN
   DESIGN_SPEC containment note, BenchmarkHeatmap + AssumptionsTable comments. Archives + literal
   hex descriptions + chart-fill descriptors deliberately untouched.

6. **Freeze compliance:** COO portal DEV-push freeze (0.2.0_DT POSN_BMKVIZ promote) landed
   mid-work -- held ALL portal commits, ACKed, kept working workspace-side; committed on the
   release relay. Note: the UNFIXED P0 page rode to PROD as a DEV passenger (Andrew sovereign
   call, per COO); 84436ed1 fixes it on DEV and rides the next promote.

## Commits (window)

Workspace CLOUD (author 0.5.0_AE_OpalETL~A): 8f3366024, e5391e8cb, 16ab9c9bc (07-14 tail);
c5a9418dd, dbfe8c3a9, 25b9390a8 (07-15). Portal DEV: 84436ed1 (15 files, +474/-219).

## Files Modified

See commit messages: 16ab9c9bc, c5a9418dd, dbfe8c3a9, 25b9390a8 (workspace); 84436ed1 (portal --
carries the full sweep file list). Extra context beyond the messages:

| File | Note |
|---|---|
| portal/src/pages/TicketCenter/TicketCenter.tsx | Rebuilt on Panel>PanelHeader>PanelContent; actions into PanelHeader slot; canvas error banner dark-on-light (text-red-900) |
| portal/CLAUDE.md | NEW -- first CLAUDE.md in the portal tree; the standing reiteration of the color rule |
| portal/scripts/ui-smoke.mjs | NEW -- self-tested against the fixed page before commit |
| .claude/skills/frontend-dev/SKILL.md | NEW -- named to Andrew's handle (no such skill existed; portal/.frontend-dev/ untracked dir from Apr-Jun is unrelated legacy tooling) |

## Deployment Sequence + Verification (AE addition)

No AWS deploys this window (annotation + frontend only). Portal DEV push verification:
```
[DEV 84436ed1] fix(ui): silver-canvas color law -- ...
 15 files changed, 474 insertions(+), 219 deletions(-)
To https://github.com/Opal-Capital/portal.git
   03719032..84436ed1  DEV -> DEV
```
SEV1 note: portal pre-commit surface-check BLOCKED on BenchmarkHeatmap.tsx (model_portfolios.benchmark,
SEV1) -- diff verified line-by-line comment-only (class strings byte-identical) BEFORE proceeding via
SURFACE_ACK (audited, org/surface-check-ack-audit.log). The portal-side gate BLOCKS (contrast: the
workspace comp-surface-check is advisory-only per LD-0273) -- worth knowing fabric-wide.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pulse diff (auto, risk-reflex) | 3x via safe-commit | PASS | HOLD lines were basename-cluster false positives (unrelated main.tf / SKILL.md claims); citations read each time |
| comp-surface-check (workspace, auto) | 3x via safe-commit | PASS | 0 critical surfaces on org/.claude paths |
| portal pre-commit surface gate | 1x on portal commit | BLOCKED->ACK | Worked as designed on SEV1; ack grounded on verified comment-only diff |
| raw aws (rail-checked) | get-authorizer, list-user-pools | PASS | Live-primitive grounding for the Cognito verdict -- authorizer identity/backend is not comp-routes-modeled |

What worked: the portal SEV1 gate blocking on a shared-surface file forced the diff verification
that made the ack honest. What failed: my first typecheck run reported TSC-EXIT:0 from the wrong
cwd with tsc not found (exit code of `head`, not tsc) -- re-ran with PIPESTATUS from portal/; an
instrument that cannot fail is not an instrument, again. Gap found: no comp tool models
frontend color/contrast containment (CTO routed the WARN-lint to comp-learns backlog item 6;
the deterministic instrument remains the screenshot -- ui-smoke.mjs is the primitive).

## MCP traffic

~11 in / ~8 out. Significant: COO ACKs #3/#4/#5 (loops closed, "nothing owed"); CloudOps FIXED
5853ddc76 (Cognito root); COO FREEZE + RELEASE (held->landed per protocol); COO ACK #6 (fleet
relay complete incl. 0.2.0_DT mid-promote); CTO ACK #6 (gate candidate ROUTED, comp-learns
backlog item 6); base-lane relay (non-actionable duplicate of release, confirmed no strays).

## Blockers

None open. (Freeze was a protocol hold, not a blocker; released + landed.)

## Current State (zero-context handoff)

- OPAL_TICKET: P0 live end-to-end; the P0 page is on PROD (passenger, portal-v2.1.136) in its
  UNFIXED visual state; the contrast fix is on DEV @ 84436ed1 and rides the NEXT promote. P1
  (cutoff sweep vs CUTOFF_ET=14:00 env, Teams-only claim links, requester asap-ack) NOT started --
  needs the Teams-sender design decision (gateway-side holds Graph auth, not Lambda) at P1 start.
- OPAL_TAXSMA: /tax-pt1 built + deployed, FIRST LIVE RUN STILL PENDING (m365 was live this
  session but the run was not ordered; S0.3 byte-confirmation still open with it). /tax-pt3 gated
  on a generic gateway write-file tool + fresh Tax Lot export.
- Color law standing: portal/CLAUDE.md (auto-loads), /frontend-dev skill + portal/scripts/
  ui-smoke.mjs (instrument), design docs all corrected to true archetypes (silver canvas 81% /
  navy panels 25-11% / "light blue"==lighter navy). Portal main tree on DEV, clean except
  pre-existing untracked non-lane dirs (.frontend-dev/, .runtmp/, org/ strays -- NOT mine, left).
- Auth truth on record: NO Cognito anywhere (zero user pools); homegrown JWT via
  opal-portal-authorizer + Secrets Manager opal/auth/jwt-public-key.
- Workspace CLOUD @ 25b9390a8 pushed; portal DEV @ 84436ed1 pushed.

## Next Steps

1. [self, next in-session] Andrew-direct #7 (received with this /log order): UIUX macro +
   UIUX_DESIGN project -- root /design centralized design repository + process-architecture
   repoint. Register, record verbatim, broadcast, execute.
2. [self, on Andrew word or next trading morning] first /tax-pt1 live run (closes S0.3).
3. [self, on Andrew GO] OPAL_TICKET P1 build; bring the Teams-sender design decision first.
4. [0.2.0_DT_PortfolioAnalytics] next portal promote carries 84436ed1 (ticket-center fix +
   color-law docs) to PROD -- no action owed by them beyond their normal promote.
