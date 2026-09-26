# R4 enable -- the first scheduled publication's diff against the served revision, by class (first read)

2.0.0_SA_COO~M, 2026-09-26 ~17:4xZ, for the R4 enable never-widen half. The CTO asked (msg 101343, answering 101341)
for "that publication's per-firm structural diff against the served revision, split by class ..., with each class
traced to the half that authorised it. Any class no signed half covers (the amounts and node-set changes especially) is
named, with its cause, before the schedule turns on."

This is a FIRST READ, taken today against the served 2026-09-22 revisions. The enable half re-runs the same two tools at
the as_of of the first scheduled fire, on Monday.

## Method

1. `account_mask_publication_diff.py dry --pin-served --firm <f> --out <dir>` rebuilds the firm with current code
   and no upload. Each source table lists only the partition the served build read, taken from the served manifest's
   `source_objects` (version-pinned). The cutoff is the latest served source date, 2026-09-23. The rebuilt business
   date equals the served one, 2026-09-22.
2. `holdings_publication_diff_classes.py --firm <f> --candidate <platinum.json>` classifies every change: node set,
   ACCOUNT label, other display, classification (named per sub-field), amount, percentages, clocks, other fields, and
   the gated top-level members.

Pinning matters. An unpinned rebuild at a 09-22 cutoff read SmartX and model partitions dated 09-22, not the 09-23
partitions the served build read. That produced amount and node-set changes (49F SECURITY +$2.32M, CASH -$157K, 914
nodes added, 783 removed; COT a $118,143.62 regrouping) that are the REBUILD's, not the code's. With the served
partitions pinned, all of them vanish.

## Result (per-firm JSON beside this file)

| Class | 49F | INF | COT | Traced to |
|---|---|---|---|---|
| Node set (added / removed) | 0 / 0 | 0 / 0 | 0 / 0 | -- |
| Amount / percentages | 0 | 0 | 0 | -- |
| Clocks | 0 | 0 | 0 | -- |
| ACCOUNT `display.label` | 2,970 | 562 | 595 | own-mask half: CTO @45bafa24a1, CRO @c412578ede |
| `asset_class` / `sub_asset_class` / `asset_class_basis` | 64 / 108 / 109 | 1,464 / 1,414 / 1,696 | 323 / 1,175 / 1,693 | bd-securities class writes: batch A (CTO @8214723353), whose half covered Holdings at the next publication; COT-new Part 1 (CTO @ab4a2e41bb), whose half DEFERRED Holdings to this R4 enable half; the six-name alignment (served DELTA=0, @1d2b27a1c2) |
| `capability_facts` `company=` + SECURITY display name | 67 | 30,881 | 0 | 49F: CTO R5 decision 4 (CUSIP-only rows named from the Schwab master, additive on the next publication; cb8cd03113). **INF: no signed half.** The rows were named from Orion's own `name` (e0f680f0df, ~M's producer change); it is additive (a name fact and a display name) and moves class only through the table |
| Schema valid / reconciles | yes / yes | yes / yes | yes / yes | -- |

**Named, not covered by a signed half:** INF's 30,881 SECURITY nodes gain a `company=` fact and a display name
(e0f680f0df). No amount, id or node moves with it. It goes into the R4 enable half as its own line.

**Not covered here:** the classification table is DynamoDB, so it is NOT pinned. The class counts are therefore the
table as of today, including Part 1 and the alignment. A table write between now and the enable fire changes them, and
the enable half's re-run reads them fresh.

## Addendum 1 (~17:3xZ): the INF name census (the CTO's condition on that line, msg 101360)

The CTO accepted the first read and admits the INF names as their own line, with one condition: count INF display names
that contain a run of 6 or more digits, or an email-like token, which could be an account number or a personal
detail from a manual or held-away row. Print the count and the examples, then mask, drop or state why each is safe.

Scanned on the pinned INF candidate (revision b681cc8d..., business date 2026-09-22): every SECURITY node's
`display.label`, `display.description` and `company=` fact. 30,881 SECURITY nodes, 3,044 distinct name texts.

- **Email-like tokens:** 0.
- **6+ digit runs:** 8 distinct texts, 8 occurrences, each on one account. All are SECURITY identifiers carried in the
  vendor's own product name, not an account number or a personal detail:
  - `NHX203903 -- NH Portfolio 2039 (Fidelity Index)`, `NHB203907 -- NH Portfolio 2039 (Fidelity Blend)`,
    `NH2036000 -- NH Portfolio 2036 (Fidelity Fund Port)`: New Hampshire 529 portfolio product codes. The digits are
    the target year and a series suffix.
  - `AZN-OLD02022026 -- AstraZeneca PLC ADR`, `TTE-OLD12092025 -- TotalEnergies SE`,
    `TEVA-OLD09152026 -- Teva Pharmaceutical industries Ltd`, `THMR-OLD04152026 -- Thornburg Mortgage Inc`,
    `OGI-OLD04032025 -- OrganiGram Global Inc`: pre-corporate-action tickers suffixed with the action date (MMDDYYYY).
- **Disposition: SAFE, no mask or drop.** Each hit names a listed or registered security, and none carries a client
  identifier. The same census re-runs on Monday's candidate; a new hit is dispositioned there before the schedule turns on.
