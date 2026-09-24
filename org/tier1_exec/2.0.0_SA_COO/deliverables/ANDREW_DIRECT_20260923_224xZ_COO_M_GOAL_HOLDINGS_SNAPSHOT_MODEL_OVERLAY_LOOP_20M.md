# ANDREW-DIRECT 2026-09-23 ~22:4xZ -- COO~M goal: Holdings end to end with SNAPSHOT model overlay, 20m loop

**Channel:** Andrew at the `2.0.0_SA_COO~M` terminal (Claude session, first turn after the Codex-to-Claude
seat transition), two mid-turn messages during `org/XXX.md` startup.
**Receiving seat:** `2.0.0_SA_COO~M`
**Recorded by:** `2.0.0_SA_COO~M`, same turn.

## Verbatim, message 1

> Here is your handoff, write yourself a /goal about how you're going to get end to end "Holdings" with
> model overlay for every 49 and Inflection Client that you can mesh between their respective smartx/schwab
> and eclipse/orion accounts, with structurally correct pipeline for cottonwood (as they dont have backfill
> data at this time). Then, I need you to make a /loop with a 20m interval whose purpose is to keep you
> driving until that is done. Below is a handoff from the agent who was working on this before you:

(Typos his, preserved. The handoff text that followed is the Codex `2.0.0_SA_COO~M` close block, whose
substance is already recorded at `org/tier1_exec/2.0.0_SA_COO/logs/2026-09-23/irpt_m_holdings_runtime_coverage_checkpoint.md`
@`cd99346aea`; the handoff adds only the pointer that CTO GO `d940022b06` supersedes the STATUS.md approval wait.)

## Verbatim, message 2

> Also, for now, all you need to do for model overlay is be able to show what clients own what models and
> what assets are in those models. its a snapshot view, please reorient the goal to be around just providing
> snapshot model holdings, we do not need time series on Models, snapshot is fine.

## Goal as set (the loop's standing directive)

Investor Reporting Holdings is done end to end for every 49 Financial and Inflection client: a real signed-in
user selects a client's accounts and sees actual custody holdings meshed across that client's sources (49F:
Schwab custody with SmartX as model authority plus the Andrew-authorized canonical Tax SMA workbook; Inflection:
Orion custody with Eclipse membership at its supported grain), with a SNAPSHOT model overlay that shows which
clients own which models and what assets are in those models. No model time series. Cottonwood runs through the
same pipeline, structurally correct (Black Diamond custody plus Rebalancer membership, canonical publication,
API, screen), with coverage bounded by the data Black Diamond holds today and that bound disclosed, not padded.

**Done = `/verify` SOUND** on: (1) the complete signed-in journey (login -> selection -> accepted publication ->
Holdings API -> Holdings screen with Models / SMAs / Client taxonomy and root/account/security drill) for a real
client at 49 Financial, at Inflection, and at Cottonwood; (2) every active client account at 49 Financial and
Inflection resolvable in Holdings with its model membership shown as a snapshot (client -> models -> assets in
those models), and every unsupported account refused explicitly, never silently empty; (3) Cottonwood structural
soundness with its refused-account population and data window disclosed.

## Loop authorization (this row is the Step 1b-F source of truth for this seat)

`2.0.0_SA_COO~M` `/loop 20m` DIRECTED over the goal above, ARMED 2026-09-23 ~23:0xZ on his word. Cadence
20 minutes. STOP-CONDITION: `/verify` SOUND on the done criteria, or Andrew's stand-down. A successor at
this seat re-arms off this record while the goal is not DONE. This supersedes the Codex-era 600-second
`codex-operational-driver.ps1` drive for this serial (PID 27884), which this seat stopped at ~22:47Z together
with the dead Codex seat's heartbeat, bridge, inbox monitor and app-server (their terminal thread had no live
process; the bridge log showed its last turns cancelled and the CTO GO nudged with no consumer). Verified
0 of 6 remaining before this session registered the serial.

## Scope notes carried unchanged

- Standing directives from the handoff: no happy-account substitution, no fabricated empty holdings, no invented
  currency, no source-cutoff-as-custody-date; 49F 0833 custody exceeds SmartX and SmartX is model authority
  except explicit Tax; the six INF measured matches do not establish a general date offset; no shared CLOUD push
  (that is `0.0.0_AB_MSTR`'s); no invented authorizer or capability credentials.
- First act under the loop: the exact CTO GO `d940022b06` Cottonwood 19-write CAS publication (revision
  `93f930c265ed242d7e38cb48a7ed4baf267025e8c4dfd06ff39739c6a8f55217`, index IfMatch
  `606126dddec555c41e711b18732d3c7f`), verifying returned versions and hashes before the index and refusing drift.
- CONTRACT.md v1.4, COO_M.md and CONTROL.md continue to govern; the snapshot reorientation narrows the model
  overlay deliverable (no time series), it does not lift any acceptance ID.
