# L4-R review -- NFRA_OPLGTW PRD v2.7 (v2.6 + v2.7), BRIEF half (2.0.0_SA_COO~ZB in 4.0.0_SA_CRO's stead)

**Delivery:** CTO~Z msg 33735 (v2.6) and msg 33763 (v2.7, @27ba6b6191, half_hash c4c3da5d6f6f -- the bytes this review signs); asked again by `2.0.0_SA_COO~O` msg 33752 (round 37 waits on it).
**PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` read at @713305ee56 (v2.6) and re-read at @27ba6b6191 (v2.7). **Reviewer:** a live COO
that does not hold this round (no live CRO session; prd-signoff status names this seat).
**Verdict: SIGN**, with one finding carried to the CTO by pinned line (below). It is not a refusal, because the PRD's own C2
clause and round 37's orders already hold the boundary, and the gap is a missing PROOF arm, not a missing rule.

## What changed under the brief half

`prd-signoff status` read the brief half STALE: it was signed by `4.0.0_SA_CRO~Z` against ENDPOINT hash 3b655164f451, and v2.6 adds
FWD-20 and FWD-21 to the ENDPOINT (:237-268). The v2.6 addendum (:991-1016) names its brief: the CRO's site Z and AMGT alignment
reports on Andrew's 2026-10-13 memos, via `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_SITEZ_20261013.md`
@4e963d4a12 (section 7 lists both reports). The earlier BRIEF COVERAGE table (:446-466) is for the 09-14 commission and is
unchanged; this review covers the two new outcomes against their brief.

## FWD-20 (cadence and depth read) against direction Z3 (:213-238) and the site Z alignment report (:43-44, :93, :139)

| brief content | carried into FWD-20? |
|---|---|
| Andrew's words, "the depth and breadth of the polls available ... what backfill or scope out those tools work" (memo :51, :63) | YES, SOURCE line |
| per family: schedule, and history depth, each with the date read | YES, DONE WHEN |
| schedule read from the live AWS schedule; depth from `backfill-status` plus the served data's earliest date | YES, ACCEPT |
| proof: one family's cadence against its live schedule; one family's depth against `backfill-status` and the earliest date | YES, PROOF, the same two arms |
| OPLGTW produces the read; MCPORTAL displays it; no alert or monitor | YES, ACCEPT + v2.6 item 1 |
| every value carries its claim | ADDED by the PRD (the value-claim law); a tightening, not a drift |

Covered whole.

## FWD-21 (harvest for Opal asset managers) against direction Z5 (:269-289), the AMGT alignment report (:50, :92-93) and call 8

| brief content | carried into FWD-21? |
|---|---|
| Andrew's words, "open gateway mechanics ... open dash data dash harvest folders ... so that the asset managers can use that with their cloud" (memo :101-102) | YES, SOURCE line |
| done when: a real asset-manager principal's driven call returns one covered name's pack and chatter from `opal-data-harvest` | YES, DONE WHEN |
| V1 derived-only ruling, then widened by Andrew's call 8 (all 24 prefixes, raw included, Opal users only, "managed via opalgateway entitlements") | YES, ACCEPT, cites the servable list v4 @7e0da2dfee |
| principals named from the grant store; no work Claude account = Andrew's act | YES, ACCEPT |
| non-Opal principal refused | YES, DONE WHEN + PROOF (`packs/` and `wsj/harvest/`) |
| **"scoped to research data only"** (AMGT alignment :93); Z5 proof arm **"the same principal's call for a Schwab or BD tool is refused"** (direction :279-280) | **NOT CARRIED.** See the finding |
| Z5 proof arm "a principal without the research grant is refused the pack" | Superseded by call 8: the grant is now Opal-wide, so "without the research grant" reduces to the non-Opal arm, which IS carried |

## Finding (to `1.0.0_SA_CTO~Z`, for the next addendum; not a refusal)

**F1.** FWD-21 drops the brief's scope boundary, that an asset manager's access is research data only, and its proof arm, that
the same principal is refused a Schwab or Black Diamond tool. The boundary still holds in the text: v2.6 item 2 (:1004-1007) keeps
the C2 owner gate unchanged, and round 37's OG-hv-1 / OG-hv-2 orders grant only `s3:GetObject`/`s3:ListBucket` on the harvest
bucket. But the v2.2 addendum (:879) opens "any account, any source, for the connected users", so whether an asset-manager
principal reaches Schwab depends on whether it joins v2.2's connected set. Nothing in FWD-21 would catch that. **Correction:**
add to FWD-21 PROOF one arm, "the same asset-manager principal's call to a Schwab or Black Diamond tool is refused", or state
that asset managers are members of v2.2's connected set on Andrew's word. Either is one line; it changes the ENDPOINT, so it
re-opens the ratified-text half, not this one.

## v2.7 re-read (@27ba6b6191)

v2.7 changes FWD-21's ACCEPT only: V1 admits by IDENTITY (OG-tg-1's Opal-user predicate, opalinvest domain, no `#ext#` guest), the
grant writer writes nothing for V1, and a per-person harvest grant arrives with MCPORTAL's control outcome (Z2). This is call 8's
wording ("available for opal users only for now, which will be managed via opalgateway entitlements"), so the brief is carried
more exactly than in v2.6. F1 is unchanged by it: identity admission to the harvest tools says nothing about the same principal's
reach to Schwab or Black Diamond tools under v2.2.

## Heading denominator

The v2.6 brief is two memo items (Z3, Z5) out of seven direction outcomes. Z1/Z2 are NFRA_MCPORTAL's, Z4 NFRA_MCPINDEX's, Z6
OPAL_BBGTML's and Z7 MCPORTAL's (direction section 4). 2 of 2 OPLGTW-owned outcomes are enumerated as FWD-20/21. None is dropped.

-- `2.0.0_SA_COO~ZB`, 2026-10-13

## v2.8 re-read (@ecdab3c7d0, half_hash 2059e86212c5) -- F1 CLOSED

v2.8 changes FWD-21's PROOF only. It adds, verbatim in substance, the arm F1 asked for: "The same asset-manager principal refused
on one Schwab and one Black Diamond tool unless Andrew has admitted it to v2.2's connected set (research data only by default,
AMGT brief boundary)". The brief's boundary is now carried as a proof arm. The CVO's note moves the census to the identity
store that admission reads; that is a ratified-text matter and does not touch brief coverage. Nothing else moved
(`git diff 27ba6b6191 ecdab3c7d0`: the version line, the FWD-21 PROOF paragraph and the v2.8 addendum). **SIGN at these bytes.**
