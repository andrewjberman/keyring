# CVO Startup Ground-Truth Finding — cot B_01 wipeout guard did NOT land

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-07T19:03Z
**Trigger:** CVO session startup (post Huntress-reboot #3, Tier-1 brought back by Andrew). Ground-truth reconciliation of the COO/CTO session-close handoffs (org/XXX.md Step 2b). One material finding surfaced.

---

## FINDING (P1 — time-sensitive, production-risk): "wipeout guard landing" is FALSE against ground truth

**Claim under review** — COO handoff commit `04e4f16b9` subject + `session_close_handoff_COO_1822Z.md:61`:
> "Tonight's wipeout risk is covered ... DS is landing the 1-line B_01 defensive guard NOW ... so tonight's nightly produces a correct-but-still-missing-allocations result instead of a cube wipeout."

**Ground truth (verified against live state — STATE claim, grounded on the live primitive per Rule 22a):**
- `data/cot/scripts/gold/B_01.holdings_lots.py` last commit = `d892fe500`, **2026-06-11**. No commit since. (`B_01b.classify_new_securities.py` also unchanged.)
- `git status --short data/cot/` = **CLEAN** — the guard is not in the working tree either.
- `git log --oneline -30 | grep -iE "b_01|wipeout|guard"` returns **only** the COO handoff commit describing it as "landing."

**Verdict: the guard did NOT land.** The whole `0.4.0_DS_ClientPlatform` family died to a Huntress/SIGTERM event ~17:48Z (COO handoff:22) and the device reboot followed; the guard COO observed "landing NOW" ~18:37Z was cut off before commit. DS is not in the live-agent roster post-reboot (only Tier-1 is up).

**Impact (relaying DS's already-grounded concern, not re-derived):** `comp-pipescript io B_01` confirms B_01 READS `silver/allocations/{*}.parquet` + `silver/unrealized/{*}.parquet` and WRITES the served `gold/timeseries/holdings_lots/` cube. With allocations empty since 07-01 (DATEMODE-B Custom-stamp side effect) and no guard, tonight's **02:00 UTC** cot nightly (~7h from this finding) risks the cube wipeout the guard was meant to prevent.

**Action taken (CVO = verifier-not-fixer; did NOT write the guard):**
- MCP -> `2.0.0_SA_COO` 190355Z: full finding + ask (respawn DS + re-land guard before 02:00Z; OR have DS confirm B_01 already no-ops safely on empty allocations — but don't assume it).
- MCP -> `1.0.0_SA_CTO` 190408Z: relayed (interacts with the DATEMODE ruling) + the mechanism-grounding below.

---

## SUPPORTING GROUNDING: cot DATEMODE mechanism = SOURCE-CONFIRMED (Rule 22)

The causal chain the pending CTO ruling rests on is documented in the producer's OWN code (not just AE's hypothesis):
- `data/cot/scripts/bronze/cot_bronze_ingest.py:333-336`: "overwriting a CurrentDay snapshot's dates with a single stamped day NULLS the measures on a qt1 Holdings export (and zeroed rows on qt5 allocations); the persisted template's dates are the proven-good ones."
- `:300-301`: "stamping start==end==today onto a CurrentDay allocation query empirically returns 0 rows."
- `:337-339`: dates are re-stamped ONLY when `dateRangeType=="Custom"`.

So: DATEMODE-B flipped `templates/{holdings,allocations}.json` to Custom on 06-22 -> this path stamps a single-day window -> snapshot exports (qt1 holdings, qt5 allocations) return null/zero. The code comment implies the correct per-table direction: snapshot tables want CurrentDay/no-stamp; flow tables (AUA-bearing txn/realized) want Custom. **Mechanism CONFIRMED; the ruling foundation is solid. The ruling itself is CTO's (CVO does not rule).**

## RESIDUAL UNKNOWN
Whether B_01 *already* no-ops safely on an empty-allocations partition (making the guard belt-and-suspenders and tonight already-safe) is unverified — I did not read the 3140-line merge/incremental logic. The owners' decision to land a NEW guard implies they judged the current code unsafe; DS should confirm this FIRST on respawn.

## Compiler Tools
- `comp-pipescript io B_01.holdings_lots` — confirmed reads (silver/allocations, silver/unrealized) + writes (served gold/timeseries/holdings_lots/ cube) = the wipeout blast surface. PASS.
- Operational `git log`/`git status` for the state grounding (commit history + working-tree = not a repo content-search; the STATE-claim grounding primitive per Rule 22a). Native `Read` on the cited source lines (free per rail).

— 3.0.0_SA_CVO
