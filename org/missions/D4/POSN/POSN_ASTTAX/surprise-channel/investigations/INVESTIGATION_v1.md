# POSN_ASTTAX -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `0.9.0_WK_POSN_ASTTAX~1` at L7, task order `POSN_ASTTAX.TO-S1A-1`, 2026-09-11. **Home:**
the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only during the round.**

**Why this file is opened here.** The first row was found while writing the `S1a-AC5` comparison script
(loading `ETF_CLASSIFICATIONS` from `_shared/etf_classification.py` to scan it against the DynamoDB
table). It is a mismatch between what that module's own documentation asserts about its data and what
the data itself holds -- the step-7 trigger -- surfaced incidentally to AC5 and not itself one of the
order's twelve named criteria, so it is filed here rather than folded into an acceptance row.

```json
[
  {
    "id": "POSN_ASTTAX-Z-W1-S1",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_ASTTAX~1",
    "surfaced_at": "2026-09-11T06:21:38Z",
    "one_line": "_shared/etf_classification.py documents its asset-class vocabulary as THREE values ('fixed_income', 'equity', 'other') but ETF_CLASSIFICATIONS never assigns 'other' to any of its 136 tickers -- 7 tickers (GLD, IAU, SLV, DBC, GSG, USO, VIXY) carry the undocumented value 'hedge' instead, which silently breaks the module's own is_hedge() helper.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/_shared/etf_classification.py:38-40 @e356d7c1d0: comment reads \"Categories: 'fixed_income', 'equity', 'other'\" immediately above ETF_CLASSIFICATIONS; the same three-value claim is repeated in get_asset_class()'s docstring at :925 ('Returns: Asset class: ...or 'other'').",
        "Measured live at the same commit: `Counter(ETF_CLASSIFICATIONS.values())` = {'fixed_income': 66, 'equity': 63, 'hedge': 7}, total 136 tickers -- zero occurrences of 'other', and a fourth, undocumented value 'hedge' used for GLD/IAU/SLV/DBC/GSG/USO/VIXY (etf_classification.py:237-244).",
        "HEDGE_TICKERS (etf_classification.py:288-291) is built as `{ticker for ticker, ac in ETF_CLASSIFICATIONS.items() if ac == 'other'}` -- since no ticker carries 'other', HEDGE_TICKERS is the empty set at runtime (measured: `ec.HEDGE_TICKERS == set()`), so `is_hedge('GLD')` returns False even though `get_asset_class('GLD')` returns 'hedge'.",
        "comp-find 'is_hedge' --all (vintage this session): 6 hits, all DEF/export/doc (three module copies' own definitions, _shared/__init__.py's re-export, README.md's one-line doc) -- no live pipeline call site found, so the break is currently DORMANT rather than actively mis-serving, which is why this is filed OBSERVATION/ARMED rather than BLOCKING."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "_shared/etf_classification.py's own header comment (line 40) and get_asset_class()'s docstring (line 925) both assert the asset-class vocabulary is exactly three values: 'fixed_income', 'equity', 'other'.",
    "world_is": "The live data never uses 'other' (0 of 136 tickers) and instead uses an undocumented fourth value 'hedge' for 7 tickers, which is also the value the DynamoDB-serving vocabulary (etf_classifications_dynamodb.py:91) and the live Positioning branch set (lambda_function.py:355-368, re-taken at S1a-AC7) both use -- so the dict's DATA already agrees with the wider FOUR-value live vocabulary; only its own COMMENT is stale, and that staleness is what breaks HEDGE_TICKERS/is_hedge().",
    "notes": "Not this order's to fix (READ-ONLY, no edit to either classifier module per BOUNDS). Relevant to a later cell reading this module for the class-edge work C-MEMBERSHIP-AT-L5 reserves: the DOCUMENTED category list should not be trusted over the DATA. Filed OBSERVATION because it did not block S1a-AC1..AC12; ARMED because a future caller of is_hedge() (dormant today, per the comp-find evidence above) would get silently wrong answers, and because a reader trusting the stale comment over the data could mis-scope the class-edge work."
  }
]
```
