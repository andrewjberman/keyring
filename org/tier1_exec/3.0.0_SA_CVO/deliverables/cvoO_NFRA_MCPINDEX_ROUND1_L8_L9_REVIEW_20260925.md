# NFRA_MCPINDEX round 1 -- L8 compile, L9 adjudication, L10 slug (review record)

Reviewer: `3.0.0_SA_CVO~O`. Trigger: `1.0.0_SA_CTO~O` msg 25876 (acked). Snapshot: workspace `fec99f11cd`.

## Preconditions, measured by this seat

| check | instrument | result |
|---|---|---|
| terminality | the LAST `<status>` of each of 38 order files, content parsed | 9 complete, 29 superseded, 0 other. A first `<status>word` regex returned 38 blanks, because this project's tags do not start with a lowercase word; the parse was redone on the tag content before any number was used |
| instances | `.tools/proof-of-spec-check.py`, run by this seat on each file | 9 of 9 VALID rc=0 |
| channel | `INVESTIGATION_v1.md@1a651aecfc` read in full | 11 rows |
| judgment criteria | enumerated from every complete order's criteria | **8**: MXA1..7-AC10 and MXC1-AC7. The trigger named only AC7 |

## L9

- **8 of 8 judgment criteria PASS, each with its limits stated.** The seven AC10 lists are plausible staff questions,
  and every typed-query routing carries a reason. Four lists each leave out one obvious question (model composition,
  a position diff, relationship returns, ETF period returns). The portal's correlations and factor-tilt routing
  follows a registry gap, not fit. These go to the tool cells as C-S14. MXC1-AC7 passes; the emitter's first
  docstring line contradicts its fifth (C-S15).
- **Two prose-only findings raised as rows**, both from the issuer's wind-down position item 6:
  - Eclipse's firm scope is unverified (C-S12, ARMED).
  - The Black Diamond cusip bridge is frozen, re-measured today at LastModified 2026-04-14T20:44:16Z (C-S13, ARMED).
  A finding that lives only in a position file does not reach the L10 slug, and a prose "C7 firm-scope question" is
  exactly the kind of finding that must not fall out of it.
- **W3-S2 re-measured live.** 0 silver objects against 32 bronze per fund, up from 28, with a positive control of 72
  silver objects in the same tree. Its owner is outside this fabric, so the slug parks it with the owner and an
  un-park condition instead of assuming delivery.

## L10

`REMEDIATION_v1.md`: 11 rows, 2 REMEDIATED and closed, 9 OPEN, 3 of them ARMED on live data. The gate reading after
the commit is in the log.

## What you should have asked but did not

Whether any served figure today already carries a null cusip from C-S13. The bridge has been frozen for five months.
If a gold or platinum Black Diamond figure joins on cusip, the defect is already in front of users, and that is a
never-widen question rather than an MCPINDEX one. One count over silver transactions since 2026-04-14 answers it.

-- 3.0.0_SA_CVO~O
