# ws-charter — 2026-06-03 1428Z — #6 scope ruling

**CLASS:** FIX (scope ruling on active Andrew-directed project; #6 PRD scope I own)
**Trigger:** COO SCOPE RULING request (`20260603T142713Z`) off DS RAVC1 finding (`c42c5e6ed`).

## Finding (DS deep-trace)

`total_aua_fee_paying` (AUM-mode fee-split) was missing on BOTH firms' served timeseries.
- **INF:** DS adding it (F11-C) + flows (F11-B, committed-never-deployed since 5/28) → deploying via AE now → INF AUM-mode + NNA-mode both get real splits, approx dies.
- **49F:** NNA-mode fee-split already works (`nna_canonical_fee_paying` + per-role `aua_fee_paying`); AUM-mode `total_aua_fee_paying` ABSENT → 49F AUM toggle falls back unsplit/inert. To fix, 49F needs a D_02 gold change (deduped total_aua split — modest-non-trivial melt/dedup edit + own gold-cycle + publisher deploy).

## RULING — 49F AUM-mode fee-split IS IN SCOPE for #6, executed as fast-follow W2b

Rationale:
1. **Faithful to Andrew's directive** — "KILL the approx, use REAL fee data" is firm-AND-mode-agnostic. The INF #6 work already includes AUM-mode fee-split; consistency requires 49F match.
2. **My own PRD §6 already scoped "both firms"** ("fee-paying toggle shows real splits, no approx label, for both 49F and Inflection"). This is NOT a scope expansion — it confirms that intent extends to AUM-mode specifically (the AUM-vs-NNA wrinkle is a DS implementation discovery, not a new product decision).
3. **Avoids the INF-vs-49F asymmetry** Andrew's eye catches (INF real AUM split, 49F inert).

NOT bouncing to Andrew — within the directive's spirit (AUM-mode fee-split already decided "yes" by the INF work; matching 49F is consistency, not a new call). Flagging the consistency ruling to Andrew for visibility/override.

## Sequencing (per COO rec + my refinement)

- **INF #6 ships NOW** (primary visible case; unblocks the FE #6 tail; does NOT block the promote bundle).
- **49F AUM-split = ADVI_FEREFI.W2b fast-follow** (COO authors TO; DS does the D_02 gold edit + gold-cycle + deploy). Does NOT block INF ship.
- **W2b targets the SAME held promote bundle if it lands before Andrew GOs the promote** (likely — promote is held on Andrew's INFOTD/INFNNA smoke, so there's runway). This avoids any PROD INF-vs-49F asymmetry in the common case. If W2b isn't ready by promote-GO time, INF ships and 49F AUM-split follows in a later promote — acceptable; the promote is NOT held on a 49F fast-follow.

## Follow-on

- Ruling → COO (authors W2b TO) + DS (unblock; was holding on 49F).
- Manifest unchanged structurally (3 commits + #6 INF tail pending + W2b 49F fast-follow). All HELD for Andrew GO + INFOTD/INFNNA smoke.
- Companion to silver/gold discipline: 49F D_02 total_aua split is a gold-tier dedup/aggregation edit (Rule 17 — business-logic split belongs in gold; comp-pipescript io + comp-validate before signal).
