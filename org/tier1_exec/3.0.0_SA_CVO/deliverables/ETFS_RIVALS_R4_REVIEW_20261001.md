# ETFS_RIVALS round 4 -- CVO review and L10 slug basis

**Seat:** 3.0.0_SA_CVO~RV (Andrew's pairing with 2.0.0_SA_COO~RV). 2026-10-01 ~23Z.
**Packet:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/DRAIN_END_READ_ROUND4.md` @550af8d320 (msg
28073, acked). 6 of 6 orders terminal; ledgers `etfs-rivalfunds-round4` and `-round4-a1` CLOSED.
**Carriers:**
- `ADJUDICATION_v4.Z.md`: 3 rows covering 24 items.
- `REMEDIATION_v4.Z.md`: 3 items (W4-S9 ARMED, W4-S7, W4-S14).
- Clock advances in place, all REMEDIATED: v1 W1-S4, v2 W1-S11, v3 W1-S27 (also DISARMED), W4-S5, W4-S2, S6.

**Open after this commit: 14.** All are owned by 1.0.0_SA_CTO~Z:
- Product (5): W3-S11, W3-S12, W5-S21, W3-S15, W4-S9.
- Fabric and instrument (9): W5-S3, W5-S7, W5-S12, W5-S14, W5-S15, S2, S7, W4-S7, W4-S14.

Every round-3 product item the analysis cut is now closed.

## Measured by this seat (code read at HEAD for every code hazard, per the round-3 correction)

| claim | read | result |
|---|---|---|
| W1-S27 (my P0) closed | `gold_trade_schedule.py:766-779` | each fund pairs with its own previous report date; packet AC2: TSEL 101, WCMG 42 windows, 0 mismatched |
| one revision contract | `revision.py` docstring + `newest()` | newest by capture time; an `import:` never outranks live; "a HASH NEVER ORDERS" |
| S9 / W2-S11 | `gold_canonical_shape.py:77`, `:293-297` | issuer silver read per fund; `issuer-site:<token>` |
| S10 | `enrichment_bloomberg.py:579/589/612` | exit_code, main, `__main__` present |
| W4-S13 | `gold_holdings_coverage.py:289` | a sidecar's own `fund`, legacy = BASG |
| deployed | `lambda list-functions` | all 5 Lambdas LastModified 21:54:46Z..21:55:09Z |
| package | pytest | 306 passed, 2 skipped, 0 failed |
| page | manifest, date=2026-10-01 | generated 22:03:35Z, batch d5-publish-a1, 13 funds, 12 updated, GQGU not-updated on freshness only; **top-level status `not-updated`** |

## Recommendations by driver

**For CTO (1.0.0_SA_CTO~Z), the round-4 analysis**
- **P1 -- W4-S9 (ARMED).** It is bounded only by procedure: any marker-driven batch above about 45 dates times out G1 at
  900 s. The next long outage's catch-up is that batch, with no one choosing to run it. A code bound belongs in round 5.
- **P1 -- a per-fund issuer floor.** The packet names it, but no row carries it. The issuer floor is 0.23 because GQGU
  resolves 0.2368, so BASG, which resolves 1.000 via the alias, could fall to 23% before its guardrail notices. A source-level
  floor set by the weakest fund in the source is blind to the strongest one. I recommend the COO file the row so it has a
  carrier.
- **P1 -- W3-S11, W3-S12, W5-S21 are still uncut.** Round-2 analysis ruling 7 placed them in round 4, and round 3's cut list
  did not carry them forward. W5-S21 (quadratic dedup) and W4-S9 share a cause: both bite on the first bulk run.
- **P2 -- W4-S7.** The WORLD device identity is AdministratorAccess, so every half's identity-level negative control is
  vacuous. Choose a scoped identity, or halves that name the stage roles.
- **P2 -- the page headline.** The manifest's top-level status now reads `not-updated` whenever one of 13 funds fails
  freshness. Round 3's page read `published` with the same 12 of 13, because GQGU then had no input to fail. One fund
  lagging two days now flips the whole page's word. Decide whether the headline is "all funds current" or "page published".

**For COO (2.0.0_SA_COO~RV)**
- **P2 -- the check-defect pattern.** Three issuer checks failed only when a worker ran them on real data, never in the
  dry-run at base (packet :71-75). Before issuing, run each criterion once against the live object it will grade.
- **P2 -- W4-S9's disarm is yours.** No bulk silver batch (backfill or catch-up) runs without windowed G1 until the code
  bound ships.

## Close-reads owed (acceptance, not graded here)

- **2026-10-02 07:00 ET issuer fetch:** BASG then GQGU. This is the live test of W4-S13 (G2 attributes each capture to its own
  fund) and of W4-S10 (GQGU's 10-01 report clears freshness).
- **2026-10-02 08:03 ET vehicle run:** the first time the enrichment step actually runs daily (S10 was a silent no-op until
  this round). Under the narrowed gate, a failure there holds only corporate-action funds.
- **GQGU 2026-09-29 and 09-30** are a permanent gap in its history unless backfilled (W4-S10 option a, not taken).
- **FWD-1:** the signed-in /rivalfunds read is still Andrew's.

## What you should have asked but did not

Whether tomorrow's first fully organic morning can be read as one thing. It is three things at once:
- the 07:00 issuer fetch on new G2 code;
- the 08:03 vehicle running an enrichment step that has never run on schedule;
- the 09:00 sweep walking a day whose upstream markers come from code deployed at 21:55Z.

If the page reads wrong at 09:30 ET, nothing today says which of the three to suspect first. Each leg already writes its own
marker and exit code (90-97), so the read costs nothing to set up. It does need someone to read the legs in order: fetch
markers, then the vehicle log's two exit lines, then the sweep's `waiting` and `unresolved`. The page alone is not the
evidence.

-- 3.0.0_SA_CVO
