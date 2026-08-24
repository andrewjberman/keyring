# ANDREW-DIRECT 2026-08-24 ~13:2xZ (base CTO terminal) — THE MONDAY PUSH ORDER, BY DIRECTIVE

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) · **archetype:** SCRIBE / COORDINATE
**Context:** his notes against the directives list I briefed at his ask ("slow down and brief on all
open subjects so we can organize for a concerted push across the fabrics").

## VERBATIM

> "D0: Yes we should bring on 0.8.0_AE_CloudComp to proceed the work here. D1: This seems to be
> crucial to knock out in the immediate term because it's beginning to get awkward because we need
> to tracking Cottonwood's Opal-Advised Assets and it's causing breaks in tracking (Global Held up
> on Cottonwood because of this by proxy). D2: We are going to need to come up with a more robust
> solution for where this data comes from. What it seems like we effectively may have to do is some
> blend of the 0824 and 0833 schwab accounts, relevant black diamond metatables, and eventually
> maybe fidelity. the issue is that 0833 has very little lookback. Black Diamond itself is the
> master for all assets but i get nervous about them so would rather focus on schwab and not rely
> on a third party solution and just flesh out our hisotircal data blending the schwab accounts
> versus putting dependency back on BD. WE need to think about how to manage this considering.
> D3: This really needs D1 clear to be able to do first and foremost, which we should be able to
> execute this week. D4: This needs to get done today. THe premise should be very simple,
> additional script pulls from bloomberg the relevant shaped ETFs data and
> characteristics/constituents in the "Positioning" page. These pulls should occur at the sametime
> as the daily /terminal-upload on the sitez machine. These files should be sent to a relevant
> folder in opal-data-etfs and published at the same time as the rest of the portal is published
> each morning. D5: HOlding for now. D6: Need to run /comp-state and check into this and see where
> it is and what is still remaining that is not yet covered from the relevant PRDs and prior art.
> D7: Holding on this until further advisory from Opal MGMT. D9: HOlding until further advisory
> from YAng."

## DISPOSITIONS (per directive, unwidened)

- **D0 — SEAT 0.8.0_AE_CloudComp.** MSTR spawns; the brief carries the routed tooling packet
  (comp-which→comp-trigger rule; HUD nudge on raw events/scheduler; comp-estate framed zero +
  warranted list; comp-routes edge-versions false-[OK]) + the pipeline enforcement builds
  (proof-of-spec-check decomp_ref extension; TO commit-lint) + D0-T1 broker primitives — all
  previously build-routed to that lane.
- **D1 — IMMEDIATE TERM.** His diagnosis binds it to the live breaks: Cottonwood's Opal-Advised
  assets are untracked in the taxonomy, and Global is held up on Cottonwood by proxy (the
  15/85-class guard failures ARE that break). `D1_CATVIEWS` stage-3 decomp proceeds NOW at COO,
  concurrent with D4's last mile — no longer queued behind it.
- **D2 — SOURCING ARCHITECTURE, think-first.** His direction: blend the **0824 (MDPF/SmartX)** and
  **0833 (ADVI)** Schwab accounts + relevant Black Diamond metatables, eventually maybe Fidelity;
  0833's short lookback is the named problem; BD stays master-of-record but he does NOT want
  dependency built back on BD — flesh out our own history by blending the Schwab accounts.
  Disposition: CTO drafts the **49F data-sourcing PRD** (purpose-level, pipeline stage 1+2) around
  that constraint set; the earlier "history reconciliation program" framing is SUPERSEDED by this
  direction (BD-gold-port is no longer the default remedy — the Schwab blend is). The 0824/0833
  distinctness law binds throughout (never conflate, full account numbers).
- **D3 — after D1, this week.** D1 clears first; the SmartX↔BD/Schwab exact-join spec is the
  early-startable piece and now doubles as D2-blend groundwork.
- **D4 — DONE TODAY.** His premise matches what is built: the additional Bloomberg pull runs WITH
  the daily /terminal-upload on the site-Z machine (live since Monday's 07:00 fire), lands in
  `opal-data-etfs/bbg/{as-of}/`, and the platinum publish aligns with the portal's morning publish
  cadence — **that cadence is TO-5's schedule anchor (AE)**. Last mile today: TO-5 schedule TF;
  the TrueShares capture deploy (constituents' operative source — Bloomberg constituents are
  entitlement-walled per the hunt; BQL pricing is his optional card); **the held PROD promote needs
  his word** for the page itself to ship. One premise note carried honestly: "constituents from
  Bloomberg" is blocked by the BQL entitlement today — TrueShares fills constituents now; A3 folds
  Bloomberg constituents into the daily pull if he ever buys the entitlement.
- **D5 — HOLDING.** No acts.
- **D6 — STATE ASSESSMENT.** Run comp-state + census the D6 PRDs/prior art → a remaining-work map
  (what is not yet covered). Routed to site Z (their directive; folds into the LD-0444 register
  cleanup), laptop comp-state packet supplied.
- **D7 — HOLDING until Opal MGMT advisory.** In-flight reply-on-thread work: not newly tasked;
  site Z holds at current state.
- **D9 — HOLDING until Yang.**

## BROADCAST

MCP to all live seats + agentbus to site Z, this turn; push state stated; commit rides integration.
