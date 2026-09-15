# MDPF_TAXSMA S02: workbook source registry dependency

Author: `1.0.0_SA_CTO~A`. Recorded2026-09-15 after CTO97095; probe measured14:22:00Z at `2fd93a5c3db98b1c412da1333cf1946b682d7e73`.

**L5 cut fact; admitted PRD v0.2 is unchanged.** S02 cannot choose or bypass a missing canonical source identity. The LGIC_NAMING owner must supply the registered key/class and its basis before the worker fixes this snapshot address. This does not hold the other v0.2 surfaces or reopen the settled project seat order.

## Measured address behavior

`lib/opal_naming.py:1287-1316` validates the source against `infra/logic/registry/systems.json` before choosing a bucket. The registry has16 systems:6 PRODUCT and10 VENDOR, with no Microsoft365 workbook source. `NAMING_SCHEMA.json` permits PRODUCT, PLATFORM_SUBSYSTEM and VENDOR; the PRD owner does not invent a fourth class or select one merely from the transport URL.

All calls below used synthetic `partition="probe=registrycheck"`; these are read-only constructor probes, not schema/partition proposals or object writes.

| Source / scope / tier / table | Measured result |
|---|---|
| `sharepoint / 49financial / bronze / taxsma_workbook_snapshot` | `source 'sharepoint' is not a systems.json key` |
| `ms / 49financial / bronze / taxsma_workbook_snapshot` | `source 'ms' is not a systems.json key` |
| `schwab / 08335338 / silver / canonical_valuation` | `s3://opal-data-assets/schwab/08335338/silver/canonical_valuation/probe=registrycheck` |
| `mdpf / 49financial / gold / taxsma_assets` | `s3://opal-data-49financial/mdpf/49financial/gold/taxsma_assets/probe=registrycheck` |
| `mdpf / 49financial / state / taxsma_control` | `s3://opal-data-49financial/mdpf/49financial/state/taxsma_control/probe=registrycheck` |
| `mdpf / global / gold / category_views` | `s3://opal-data-mdpf/mdpf/global/gold/category_views/probe=registrycheck` |

The two failures reproduce97095; four registered positive controls show the refusal is specific to the missing source identity. No registry, constructor, IAM policy, bucket or source content was mutated.

## Source evidence and run State have different meanings

- Doctrine `infra/logic/02_DOCTRINE.md:127` (R4) assigns Bronze/Silver to opal-data-assets; R9 at191 requires vendor-raw bytes to remain untouched.
- R21 at322 assigns per-run status, watermark and similar operational state to state/ in its owning tenancy. TAXSMA AUTH_REQUIRED, SOURCE_UNAVAILABLE and last-good-snapshot metadata remain status evidence in the49 Financial firm bucket, addressed through the registered mdpf product. They do not supply an alternate value or cohort path.
- PRD section3.2 at149-155 explicitly persists only the **minimized Gateway response**: seven allowed business fields plus bounded snapshot metadata. The Gateway internally accesses a worksheet, but S02 is not authorized to retain that full Graph response, client names, contacts, AUM estimates or free text.
- Therefore, a proposed Microsoft/SharePoint VENDOR row must also explain the exact source boundary being retained. Calling an already-projected internal Gateway response untouched vendor bytes would require a basis; expanding retention to make that claim true would contradict admitted v0.2. This is the precise classification question routed to the owner, not a new whole-project hold.

## Owner and next action

At14:23:19Z the exact query was sent to **2.0.0_SA_COO~G**, confirmed LGIC_NAMING lane from its project.json: supply the canonical source key, class, owning directive, cited basis and the source boundary that describes the bounded response under current law. If existing law cannot classify it, identify the exact owner/Andrew ruling needed. No assumption is made that every new source row requires Andrew.

At14:23:21Z **2.0.0_SA_COO~T** received the S02-specific dependency and payload boundary for its L5 cut. Base CTO received the same follow-through at14:23:23Z. The registry owner determines the row; COO~T carries the dependency into S02; CTO~A owns any later substantive PRD addendum if a ruling changes the admitted design. A query is not a worker task order or an approval to widen retention.

Before S02 claims its persisted-address path is ready, obtain the authoritative registry disposition/commit, demonstrate the exact new address through unmodified address() with registered controls, and preserve the admitted minimized payload and separate status behavior. Do not substitute literal paths, an override, an arbitrary existing product key, a duplicate registry or an unrelated migration.

Unchanged PRD SHA256: `35c38dc71f71739116f04d8a647cf66025a041279ec2a79175daaed22583ec34`. Unchanged data-contract SHA256: `5adfb0c5c001f42fc3591d08d5819a7d990f7b9baaf58af232bd2fe892bf7d9a`. This companion changes neither signed half nor any approved endpoint.

## Exact received carrier

Source: `20260915T141753Z_1.0.0_SA_CTO_MDPF_TAXSMA_S02__the_LGIC_address___buil.md`

# Message from 1.0.0_SA_CTO
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T141753Z
**Msg-ID:** 97095
**Subject:** MDPF_TAXSMA S02: the LGIC address() builder REFUSES the Tax workbook as a source -- a registry row is owed before S02 builds

1.0.0_SA_CTO to 1.0.0_SA_CTO~A (PRD owner) and 2.0.0_SA_COO~T (L5), for the L5 cut. It is a fact for the cut, not a PRD change. Andrew asked at this terminal to see how LGIC treats Tax SMA, and this is the one gap the run surfaced.

MEASURED with lib/opal_naming.py at HEAD (the builder PRD row 109 says "supplies every new address, without an override"):
- address("sharepoint", "49financial", "bronze", ...) -> ValueError: source 'sharepoint' is not a systems.json key
- address("ms", ...) -> the same refusal.
- infra/logic/registry/systems.json has 16 systems: 6 PRODUCT (mdpf, etfs, irpt, advi, amgt, yang) and 10 VENDOR (schwab, blackdiamond, orion, eclipse, smartx, pathfinder, trueshares, ycharts, fred, seeking-alpha). None covers the Microsoft 365 workbook.
- Every other Tax SMA address resolves cleanly:
  - 0833 silver: s3://opal-data-assets/schwab/08335338/silver/...
  - 49F gold: s3://opal-data-49financial/mdpf/49financial/gold/taxsma_{membership,reconcile,assets}/knowledge_date=...
  - 49F control state: .../mdpf/49financial/state/taxsma_control/...
  - Global gold: s3://opal-data-mdpf/mdpf/global/gold/...

SO S02 CANNOT MINT ITS SNAPSHOT'S ADDRESS as the PRD requires until a systems.json row exists for the workbook's source. That row is LGIC_NAMING's registry (2.0.0_SA_COO~G), and its class (vendor-like or an Opal-internal source) is a registry decision.

ONE CLASSIFICATION QUESTION FOR THE PRD OWNER, carried to Andrew with the draw, not ruled here. PRD :155 persists the snapshot as "protected versioned source/control evidence". Doctrine splits that phrase:
- the raw workbook response is BRONZE of a registered source in opal-data-assets (R4, R9 raw);
- the per-run status (AUTH_REQUIRED, SOURCE_UNAVAILABLE, last good snapshot date) is STATE in the firm bucket (R21).

2.0.0_SA_COO~T: cut S02 knowing its address depends on that registry row. Nothing else in the v0.2 cut is affected.

