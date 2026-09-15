# MDPF_TAXSMA S02: workbook source registry dependency

Author: `1.0.0_SA_CTO~A`. Updated 2026-09-15 after CTO97131. The initial 14:22:00Z probes at `2fd93a5c3db98b1c412da1333cf1946b682d7e73` are historical guessed-source tests, not tests of the declared contract call.

## Current F1 answer, CTO97131

The source token is **gateway**. Notice97131 (15:01:59Z, sender `1.0.0_SA_CTO`) points to the existing doctrine section 1: source is the vendor or system delivering the bytes, and system explicitly includes the gateway platform subsystem. Both definitions were independently read. The seven-field capability response is the delivered source; mdpf is its consumer, so both new workbook tier calls use gateway.

The row is still owed by **COO~G**. `org/standards/NAMING_SCHEMA.json` already permits PRODUCT, PLATFORM_SUBSYSTEM and VENDOR; the populated registry currently contains only the first and last classes. No fourth class, naming override or guessed vendor identity is needed. Direct `address(gateway,49financial,bronze,taxsma_workbook,...)` and corresponding Silver calls refuse because gateway is not yet a systems.json key. These are now tests of the required source token, distinct from the earlier sharepoint/ms guesses. CTO and COO~G received this exact schema distinction at15:03:46/48Z.

The private v0.3 proposal now uses gateway and records both actual refusals. At15:05:08Z its canonical shape, unchanged endpoint, 19-surface / 49-component, 18-heading coverage and acyclic dependency checks pass. The registry commit reference and two positive source-builder outputs remain pending; the canonical signed files are not replaced with an unfinished amendment. Once COO~G lands the row, this seat can finish those outputs and submit both current halves for review. X7/X2 are already granted under97126; no E1/E2 decision remains with Andrew.

**CORRECTED by CTO97115: the declared v0.2 snapshot address builds.** Its source is `mdpf`, a registered product; the earlier failures used guessed `sharepoint` / `ms` identities. Those failures did not establish that the contract's address could not be built. The actual F1 dependency is semantic source identity under R1: LGIC_NAMING owner COO~G must supply the origin row for the bounded Gateway capability response. F2 adds mandatory Silver; F3 preserves one historical served home. **CTO97126 subsequently records Andrew's E1/E2 approval: L6 now waits only for both current v0.3 signatures.** COO~T remains seated and may continue paper L5. The signed v0.2 files are unchanged while the owner finalizes the prepared amendment with the missing origin row.

## Rule 30 and subsequent L6 hold, CTO97099 / CTO97105

CTO97099, received at 14:33:25Z, broadcasts Andrew's instruction that all future pipelines follow LGIC. The checked-in `CLAUDE.md:269` Rule 30 at `a3d77717df` requires every new pipeline to follow doctrine R1-R21, with each new S3 address produced by `address()` and each resource name by `name()` in `lib/opal_naming.py`. The L4 PRD must cite those outputs. A builder refusal is registry row-add work under `infra/logic/registry/`, never permission to hand-type a path. The notice explicitly assigns this workbook source case to LGIC_NAMING owner `2.0.0_SA_COO~G`, which already has this seat's query. Ordinary row addition is not automatically a new Andrew approval request; a deliberate doctrinal departure requires an R20 register entry Andrew acknowledges. Existing pipelines require their own R19 migration projects. The naming gate remains WARN; a passing commit does not establish full conformance.

CTO97105 at 14:35:08Z relays Andrew's words: "im hesitant on taxsma until i know its in pattern with lgic rulings". Base CTO's read subsequently landed as **97115 at 14:41:01Z**, directing this seat to prepare v0.3 F1-F3. The earlier no-edit-yet instruction is satisfied by that read; the build hold remains with the more specific conditions above. A resolved source row or a passing constructor alone releases neither L6 nor the separate named-person capability activation prerequisite.

This note records the received direction, not a full conformance verdict or a change to either signed PRD half. CTO97115 rules the source boundary; the canonical source identity is still the registry owner's work. The seven-field payload limit remains in force.

## Declared v0.2 calls, independently measured at 14:45:31Z

`LGIC_V02_DECLARED_BUILDER_CHECK.json` records **7/7** exact artifact calls resolving through the unchanged builder at `f589a22a4ee5df81e026c0049c1c4cad22d6297f`, plus `name(mdpf,49financial,taxsma,role)` resolving to `mdpf-49f-taxsma-role`. In particular, the actual workbook call resolves to `s3://opal-data-assets/mdpf/49financial/bronze/taxsma_workbook/date={knowledge_date}/{snapshot_id}.json`. The JSON receipt carries the full declared argument/output denominator and v0.2 contract hash. Symbolic date/ID slots are schema; no cloud operation or implemented-pipeline validation occurred.

This measurement agrees with CTO97115 and supersedes the earlier inference from guessed-source refusals. It does not prove R1 source semantics, the missing R10/R14 Silver stage, or the R18/R19 served-home boundary conformant; those are the three required amendment changes.

## Historical guessed-source probes at 14:22Z

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

The two failures reproduce the guessed inputs in97095; four registered positive controls show those guesses were unregistered. **Neither failing input was the v0.2 contract's declared source.** No registry, constructor, IAM policy, bucket or source content was mutated.

## Source evidence and run State have different meanings

- Doctrine `infra/logic/02_DOCTRINE.md:127` (R4) assigns Bronze/Silver to opal-data-assets; R9 at191 requires vendor-raw bytes to remain untouched.
- R21 at322 assigns per-run status, watermark and similar operational state to state/ in its owning tenancy. TAXSMA AUTH_REQUIRED, SOURCE_UNAVAILABLE and last-good-snapshot metadata remain status evidence in the49 Financial firm bucket, addressed through the registered mdpf product. They do not supply an alternate value or cohort path.
- PRD section3.2 at149-155 explicitly persists only the **minimized Gateway response**: seven allowed business fields plus bounded snapshot metadata. The Gateway internally accesses a worksheet, but S02 is not authorized to retain that full Graph response, client names, contacts, AUM estimates or free text.
- The earlier query asked whether the projected response could count as raw source. **CTO97115 F1 answers it:** the capability response is what the registered source ships; its upstream seven-field projection is at the source boundary. Store that successful response body byte-for-byte in Bronze, then retain every shipped row and column in typed Silver. No full Graph worksheet retention is authorized. The remaining row-add work is source identity, not a request to reopen that ruled boundary.

## Owner and next action

At14:23:19Z the exact query was sent to **2.0.0_SA_COO~G**, confirmed LGIC_NAMING lane from its project.json: supply the canonical source key, class, owning directive, cited basis and the source boundary that describes the bounded response under current law. If existing law cannot classify it, identify the exact owner/Andrew ruling needed. No assumption is made that every new source row requires Andrew.

At14:23:21Z **2.0.0_SA_COO~T** received the S02-specific dependency and payload boundary for its L5 cut. Base CTO received the same follow-through at14:23:23Z. The registry owner determines the row; COO~T carries the dependency into S02; CTO~A owns any later substantive PRD addendum if a ruling changes the admitted design. A query is not a worker task order or an approval to widen retention.

Before S02 claims its persisted-address path is ready, obtain the authoritative registry disposition/commit, demonstrate the exact new address through unmodified address() with registered controls, and preserve the admitted minimized payload and separate status behavior. Do not substitute literal paths, an override, an arbitrary existing product key, a duplicate registry or an unrelated migration.

**Current follow-through after97115:** at 14:42:44Z COO~G received the correction and request for its exact key/class/basis/commit; COO~T received the F2/F3 paper-cut update at 14:42:46Z. A private v0.3 PRD/contract/manifest proposal is prepared with S19 Silver and nine declared artifacts. The 14:52:25Z authoring check reports zero canonical shape violations, unchanged approved endpoint bytes, 19 owned surfaces / 49 components, all 18 brief headings, and acyclic dependencies. Five unchanged address calls resolve; the two proposed source calls remain explicitly pending the registry owner. This is preparation evidence, not a landed v0.3 or a signature. Once the row lands, this seat will replace the private placeholder with the owner's exact key, run both source builders, land the concrete amendment, and let the canonical notifier request both current-half reviews. E1/E2 are on base CTO's Andrew decision path, not assumed approved by this note.

Unchanged PRD SHA256: `35c38dc71f71739116f04d8a647cf66025a041279ec2a79175daaed22583ec34`. Unchanged data-contract SHA256: `5adfb0c5c001f42fc3591d08d5819a7d990f7b9baaf58af232bd2fe892bf7d9a`. This companion changes neither signed half nor any approved endpoint.

## Exact received carrier

**Update after97126:** Andrew has granted E1/E2 as R20 X7 CONDITIONAL / X2 PERMANENT at `9cf4a274db`, independently verified in both canonical register carriers. Earlier pending-Andrew statements describe the prior state only. The private proposal now cites those granted entries and passed its authoring checks at15:00:04Z; only the owner source row is missing before this seat can finalize F1, land v0.3 and request both signatures. The registry still contained the same16 rows at the subsequent follow-up artifact read, with no committed origin addition. The source token was later identified as gateway by97131, as recorded at the top of this note. `LGIC_EXCEPTIONS_97126.md` preserves the exact exception direction. `L5_ROUTING.md` records current release conditions.

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

