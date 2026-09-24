# AMGT_RESAPP round 20: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T22:1xZ at HEAD `3863a8200d`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND20_L8_PACKET_20260921.md` @`3863a8200d`; rk-79's never-widen pair
(`NEVER_WIDEN_ROUND20_RK79_{COO,CTO}_HALF.md`); the channel census (35 carriers, 5 open before this document); three
read-only instruments from this seat over the live store, the registry and the builder.

## Round state

**2 of 2 terminal** (`rk-79` @`a13b0fc140`; `rk-80` workspace @`b06e3f7097`, portal branch `wk-amgt-20-80-portal`
@`f22e369c` UNPUSHED). Acceptance **PASS 17 / FAIL 0 / UNVERIFIABLE 0 of 17 over 2 orders**; the order files carry 17
criterion ids (10 + 7); **judgment census 0 of 2.**

## rk-79 -- the one live act, measured against its own pair on this seat's instruments

The pair carries the census ruling (b) asked for: over the newest management object of all 15 names, 1 of 15 RESOLVED
roster had no chief executive (CAT), so the literal key list is 6861 + CSL + CAT, with the ACT's write set censused one
call deeper. Its post-act bar: 0 of 15 RESOLVED-with-no-CEO, no served literal None. Measured here, window from the CTO
half's signature (@`a294e8d83c`, 2026-09-21T20:34:26Z):

| check | result |
|---|---|
| management keys (denominator) | 15 |
| keys with a new version in the window | exactly 3 -- 6861, CAT, CSL, one version each |
| `management/v1/_pool/` versions in the window | 0 |
| `raw/bloomberg/` objects in the window, over those 15 keys | 0 |
| a literal `None` in any `roster_reason`/`reason`/`basis`, all 15 | 0 |
| RESOLVED rosters with no CEO-roled officer, all 15 | **0** (7 RESOLVED, 7 UNRESOLVED-SOURCE, 1 INCOMPLETE-NO-CEO = CAT) |

Spend per the packet: 1 SERP request of a cap of 3, USD 0.0467 of 1.00. **The act stayed inside its signed radius; the
`S192` census lesson held for a live vendor act.**

**A probe error of this seat's, caught before it was reported.** The first no-CEO census read 7 of 7 RESOLVED rosters
as having no CEO: it matched officers on a `title` field, and the objects carry `role`. So it returned "no CEO" for
every input -- the silent-constant class graduated at C-S336. The tell was that the 7 it flagged were exactly the 7 the
pair says each carry one. Re-run on `role` (with v0.16's JP-President rule): 0 of 15.

## The storage home is now MET in this fabric

`infra/logic/registry/scopes.json` at HEAD carries ONE `harvest` row, tenancy GENERAL (the PRODUCT duplicate removed
@`10bace8916`). The builder now prints `opal-data-harvest` for **all six tiers**, including
`address('sec','harvest','bronze','company_tickers',...)` -> `s3://opal-data-harvest/sec/harvest/bronze/company_tickers/...`
-- the exact address `W37-S1` recorded the registry gate refusing in round 14. **C-HARVEST-HOME is MET; `S203` and
`W37-S1` are remedied, and `rk-32` + chain P are no longer held by the registry.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S364",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T22:15Z",
    "one_line": "L9 GRADE RECORD for round 20: 2 of 2 terminal, acceptance 17/0/0 of 17, no judgment criterion; rk-79's live act measured inside its signed radius -- 3 keys written of 15, no pool or raw write, 0 literal None, 0 of 15 RESOLVED with no CEO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 3863a8200d: rk-79 10, rk-80 7 criterion ids; parser reads the same; judgment=\"true\" in 0 of 2; --acceptance --round 20: PASS 17 / FAIL 0 / UNVERIFIABLE 0 of 17 over 2 order(s).",
        "S3 list_object_versions over management/v1/<key>/ for all 15 keys from 2026-09-21T20:34:26Z: new versions on 6861_JP_Equity, CAT_US_Equity, CSL_AU_Equity only (1 each); management/v1/_pool/ 0; raw/bloomberg/ 0 over the 15 keys.",
        "Latest object of all 15: 0 literal None in a reason field; roster_status 7 RESOLVED (each with a CEO-roled officer), 7 UNRESOLVED-SOURCE, 1 INCOMPLETE-NO-CEO (CAT)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "rk-79's pair: write set 6861 + CSL + CAT; post-act 0 of 15 RESOLVED-with-no-CEO; no served literal None.",
    "world_is": "Measured exactly so on this seat's own read of the store.",
    "notes": "Grade carrier only. This seat's first no-CEO census used a wrong field (title for role) and read 7; caught by the tell that it flagged exactly the rosters the pair says carry a CEO; re-run reads 0.",
    "dismissal_reason": "Grade record: this row carries the round-20 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S365",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T22:15Z",
    "one_line": "DISMISSED, remedied: the registry now carries ONE harvest scope row (GENERAL) and the builder prints opal-data-harvest for all six tiers, including the SEC bronze address W37-S1's gate refused in round 14 -- C-HARVEST-HOME is met.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/scopes.json at 3863a8200d: 1 row with key harvest, tenancy GENERAL, bucket opal-data-harvest (duplicate removed @10bace8916, 4.0.0_SA_CRO).",
        "lib/opal_naming.py address() at 3863a8200d: bronze and silver (source sec) and gold, platinum, state, code (source amgt) all resolve to s3://opal-data-harvest/...; bronze company_tickers -> s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=2026-09-21."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W37-S1: the registry gate homes SEC bronze to opal-data-assets; S203: two harvest rows make the builder take the PRODUCT one.",
    "world_is": "One row remains and every tier prints opal-data-harvest.",
    "notes": "rk-32 and chain P were held on this since round 14; they are now held by nothing in the registry.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S203",
      "AMGT_RESAPP-Z-W37-S1"
    ],
    "dismissal_reason": "Remedied: one GENERAL harvest row; the builder prints the harvest bucket for every tier."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S366",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T22:15Z",
    "one_line": "DISMISSED: three round-20 worker rows, each remedied or ruled -- two WALL tests pinning a retired phrase (paths widened, 95/0), a self-contradicting RULED item (accepted by the CTO), and the fabric-wide naming-gate stop (validator fixed).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W79-S1: rk-79 AC2 first pass 5 failed / 90 passed on two out-of-paths tests pinning 'EMPTY officer section'; the CTO widened <paths> by exactly those two files (msg 24100), order amended @34fa89b46c; re-run 95/0; disarmed by W79-S3.",
        "W79-S2: RULED item 4b states --rederive-roster-reason two ways; accepted by the CTO for dismissal at L9 (packet s.3).",
        "W80-S1: the naming gate refused every .py/.json commit fabric-wide; validator fixed @55c24a8b8a; proof committed @d0ae517a67; disarmed by W80-S2."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row's named defect.",
    "world_is": "Each is remedied or ruled at HEAD.",
    "notes": "W79-S1 is an issuer defect: the order never censused the tests pinning a phrase it retires. The CTO made that census standing for the COO's orders.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W79-S1",
      "AMGT_RESAPP-Z-W79-S2",
      "AMGT_RESAPP-Z-W80-S1"
    ],
    "dismissal_reason": "Remedied or ruled; no standing hazard."
  }
]
```
