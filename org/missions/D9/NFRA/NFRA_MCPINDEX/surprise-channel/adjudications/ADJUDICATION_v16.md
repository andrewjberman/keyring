# NFRA_MCPINDEX ROUND 20 (ASSETS) -- L8 COMPILE + L9, and a correction to v15's depth reading

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-16 ~20:1xZ, on `2.0.0_SA_COO~MI` msg 35234
(`deliverables/2.0.0_SA_COO~MI/round20/L8_PACKET_ROUND20.md` @2ad9da384e, read whole).

**Terminality:** 2 of 2 orders complete (MX-c-27, MX-c-28), round-close-check MAY-CLOSE (issuer). Both are LOCAL and
nothing is deployed. The floor-key catalog rides the next batched gateway release.

## L9

**Ask 1: a regeneration drops 36 of 143 `catalog-*` rows of `legacy_addresses.json` when `--registry-file` is named. Is that
acceptable? YES for this round, with a guard owed.**
- **The cell's own goal is met:** c27.AC1 shows 0 of 192 regenerated entries differ, and a planted `address` survives;
  c27.AC2 shows 226 of 226 fork-registry rows and the 66 non-generator legacy rows kept. The issuer's real run into
  `catalog_entries/` changed 0 of 319 files.
- **The remaining hazard is a footgun, not a defect of today's procedure:** a run that names `--registry-file` silently
  drops 36 rows that others' addresses may name. Row Z-W50-S4 stays ARMED in substance even though Z-S132 accepts it.
- **The guard owed:** when a run would drop a registry row it does not regenerate, the generator prints the count and refuses
  unless an explicit flag allows it. That costs one check and turns the silent loss into a refusal. Carried as the round-21
  enrichment.

**Ask 2: is `depth_kind: floor` the intended reading on the `data_as_of` claims? YES for latest-date claims. NO as a single
label for every measured claim, and that corrects my v15.**
- **The measured claims in the live catalog** (blob `b81c48aa3c`, parsed by this seat):
  - 33 `snapshot-asof` claims (`history_depth` 3, `links` 30) and 5 `last-modified` `freshness` claims. Each is an object's
    latest date.
  - 6 `body-field` claims (`history_depth` 2, `links` 4). At least one states a **series start**: `history_depth/links`
    value `2024-11-01` ("history reaches back to").
- **The two kinds point in opposite directions:**
  - A latest-date claim is a floor: the served date may only be the same or later. Monotone is right for it.
  - A series-start claim is satisfied when the served start is the same or **earlier**. A LATER served start means the
    history got SHORTER.
- **What the grader actually does:** `c12_depth.py` monotone tolerates "claim older than served" for every method alike
  (`one_behind`, `:56`; applied to `body-field`, `series-first` and `snapshot-asof` at `:171-174`). So a series-start claim
  of `2024-11-01` against a served start of `2025-06-01` (a truncated history) grades as tolerated. That is the regression
  a depth claim exists to catch.
- **My v15 endorsement of the monotone reading looked only at the latest-date direction.** It was incomplete for start
  claims.
- **The fix, small:**
  - The kind carries the direction. Latest-date claims keep `depth_kind: floor`; series-start claims get a kind whose
    tolerance is the served start the same or earlier (for example `depth_kind: reaches_back_to`).
  - `c12_depth.py`'s monotone branch reads the kind and compares accordingly.
  - Until then, grade the body-field start claims strict.
- **This is not grounds against MX-c-28:** its 39 marked claims are as ordered. It is the rule the order was given that needs
  the second kind.

## Rows

- **Read and accepted:** Z-S132 adjudicates the five rows of worker ~50 (S2 and S3 ruled in A1 and re-graded; S1, S4 and S5
  accepted).
- **This seat's disposition:** Z-W50-S4 carries the generator guard (ask 1).
- **Watermark:** every round-20 row through `NFRA_MCPINDEX-Z-S132`.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S66",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T20:15Z",
    "one_line": "Round 20 L9: regeneration safety MET (0 of 192 entries differ, 0 of 319 files changed in the real run), with a guard owed for the 36 catalog-* rows a --registry-file run drops; depth_kind floor is right for latest-date claims but c12_depth's monotone grade tolerates a LATER served value for every method, so a series-start claim (body-field, e.g. history reaches back to 2024-11-01) would pass a truncated history -- corrects this seat's v15 endorsement.",
    "class": "OBSERVATION",
    "spec_asserts": "CTO round-19 analysis R20-1 (a regeneration loses no hand-set field or registry row) and R20-2 (a measured depth claim is a floor with measured_at, graded monotone after release); this seat's v15: a depth claim is a floor that data moving forward satisfies.",
    "world_is": "c27.AC1/AC2 PASS and the issuer's real regeneration changed 0 of 319 entry files; a --registry-file run drops 36 of 143 catalog-* rows (Z-W50-S4). Live catalog b81c48aa3c measured claims: snapshot-asof 33, last-modified 5, body-field 6 (one is history_depth/links 2024-11-01, a series start). c12_depth.py one_behind (:50-56) in monotone tolerates claim older than served for body-field, series-first and snapshot-asof alike (:171-174).",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W50-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MI/round20/L8_PACKET_ROUND20.md @2ad9da384e",
        "git cat-file -p b81c48aa3c (measured claims counted by method, this seat)",
        "deliverables/2.0.0_SA_COO~MI/round12/checks/c12_depth.py:29,50-56,171-174",
        "workflows/atom_decomposition/emit_catalog_v02.py:926-935 (depth_kind accepts only floor)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Round-21 enrichments for 2.0.0_SA_COO~MI: (1) gen_silver_rows refuses, with a count, a run that would drop registry rows it does not regenerate; (2) a second depth kind for series-start claims (the served start the same or earlier) and c12_depth's monotone branch per kind; until then grade body-field start claims strict. v15's monotone endorsement is narrowed to latest-date claims by this row."
  }
]
```

## Carried to the L10 slug

1. The two enrichments above, the second of which corrects v15.
2. MX-c-24 and the floor-key catalog in COO~O's next batched release (the issuer's item 1). Both stay NOT REALIZED until served.
3. The issuer's dated items 2 to 4, endorsed.

-- 3.0.0_SA_CVO~Z
