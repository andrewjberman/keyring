# Cross-adjudication submission -- sitez-20261016T031855Z-f643 (NFRA_MCPORTAL): integration channels on /gateway

By `1.0.0_SA_CTO~Z`, 2026-10-16 ~03:3xZ. Source: `org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md`, PE.6 item 3.

## Context

The /gateway page groups tools by bucket, and for opal-data-assets and opal-data-bd by (vendor, firm) (PRD v0.9 C-GROUP).
Integration channels (Schwab, Black Diamond, YCharts and others) are currently their own groups (rule 1). The question
is whether to fold them into bucket groups. It gates nothing today: the live page segments only after MX-r-15 and
OG-ap-23.

## Position

**KEEP integration channels as their own groups.** Each carries per-integration auth and tier facts (its OAuth or
key state, its access tier) that a bucket group has no field for. Folding them in would either drop those facts or
put them on a group whose other members do not have them. Revisit after Andrew's sitting on the live page (call 21d9).

## Why it gave pause

### Ambiguity
The scope reads CROSS-BOX from NFRA_MCPORTAL's whole write roots and its shared buckets, not from this display choice,
which writes only the mcportal view.

### Out of pattern
None: the page already ships rule 1 and the fixture grade (MP-pf-2 AC2) passed with it.

### Other solutions
Fold into bucket groups, with an auth/tier sub-row. That costs a schema field on every bucket group and a new
test; it buys one fewer top-level group.
