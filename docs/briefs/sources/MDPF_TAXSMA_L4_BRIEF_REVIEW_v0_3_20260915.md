# MDPF_TAXSMA v0.3 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-15 ~16:48Z · request: `1.0.0_SA_CTO~A` messages 97156 and 97158 (a duplicate).

**VERDICT: SIGNED, brief half.** v0.3 is an LGIC conformance addendum. In this half it:
- adds S19, a complete workbook Silver stage;
- makes the Bronze copy the exact capability response under the `gateway` source;
- routes membership (S03) through Silver only;
- confines the publisher (S08) to the two existing served homes, under the granted exceptions X7 and X2.

Each change keeps the brief's content: privacy, completeness, replay and the served boundary. One non-blocking fix is
named for the next version: three coverage rows do not yet list S19.

## Exact inputs and scope

- PRD: `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@61748ba2e0e31276a6ac84237924508f5df1ac28`, v0.3,
  359 lines, 73,562 bytes. The file's latest commit is the pin, and the worktree matched HEAD at review.
- Brief: `…/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454` (18 headings).
- Reviewed brief-half SHA-256: `4874c5a321c4b14d5482e1773243c8144e041aea6f0819b6570b25b69b0b30ab`, computed by
  `prd_signoff_lib.half_hashes`. It matches the notifier's `4874c5a321c4`.
- Ratified-text half: `fb75838bf3acbd49c93627f3e9a033defcd11872e5fbd96a00b4803200c92b46`, STALE for `3.0.0_SA_CVO`.
  It includes the new "LGIC conformance addendum" (v0.3:116–125), which the library places under
  `## CONTRACTS`. This review does not grade that half.
- Data contract: `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` v0.3.0, compared as parsed JSON against v0.2 at
  `60c722fe64`. It was read only where this half relies on it.
- Prior review: `docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_2_20260915.md@f5a6d57e4a`, which SIGNED v0.2
  (stamp `905d2df375`; admitted and finalized at `60c722fe64`).

## What changed in this half, v0.2 (`60c722fe64`) to v0.3

| Where | Change | Check against the brief and canon |
|---|---|---|
| §1 arc (v0.3:128) | Bronze raw response, then Silver typed rows, then status explained from Silver | A pipeline ordering of the brief's §IV/§VII acquisition closure. Nothing removed. |
| §3.1 (v0.3:155) | Owns S01–S19; adds "complete workbook Silver normalization" | Consistent with the manifest. |
| §3.2 (v0.3:165) | S02 persists the capability response byte-for-byte as immutable Bronze with compact `YYYYMMDD` partitions; provenance is kept outside the body; failures and last-good pointers live in firm `state/`; membership reads only complete Silver | R9 (raw, compact date), R21 (`state/`). The brief's O5 rule survives verbatim: "never manufactures an empty workbook" and "first-run failure yields unknown denominator, not zero". |
| §3.2a S19 (v0.3:167–171) | Typed Silver in `opal-data-assets` under the registered origin: hive `date=` partitions, every shipped row and all seven business columns, replay deduplication only, no filtering by Traded, no business activation. Triggered by Bronze completion, not a new clock. A missing Silver output keeps the prior cohort as unavailable. | R4 and R10 (typed, complete, deduplicate only, event-triggered). Brief O1 and O3 are kept, because Silver does not activate or filter. Brief O5 is kept, because a missing Silver cannot complete a cohort. Brief O7 is kept, because excluded workbook fields never enter storage and the projection happens at the source boundary (contract `workbook.source_boundary`). |
| §3.3 (v0.3:175) | Membership reads the complete Silver snapshot; no shortcut from Bronze to membership | Consistent with S03's dependency on S19. |
| §3.5 (v0.3:197) | Makes explicit that the `date=` label is the knowledge date | A clarification that matches contract `valuation.gold_partition_label`. |
| §3.7 (v0.3:215) | S08 writes only the existing 49financial and Global served keys; no firm-bucket twin; X7 (CONDITIONAL) and X2 (PERMANENT) at `9cf4a274db`; no migration authorized | R18 (no dual write). The exceptions are the R20 entries this seat validated as lane owner (reply 97143 context; cross-reference `c9048873d1`). The consumer route, authorization and privacy rules are unchanged. |
| §3.8 (v0.3:225) | S19 packaged in the existing bundle | The same package discipline. |
| A01 (v0.3:245) | Adds Bronze byte equality, Silver completeness and lineage, replay deduplication, and failed or missing Silver blocking a complete cohort | Deliberate, observable arms under brief O8 ("deliberately missing ... inputs demonstrate the corresponding refusal"). |
| Manifest (v0.3:308–328) | S02 bound adds the registry prerequisite; S03 depends on S19; S08 bound names the historical destinations; S12 adds S19; **S19 row added**; the cross-check reads 19/19 and 17/17 | Recounted: 17 = S01–S13 (13) + S15 + S17–S19 (3). Correct. |
| Coverage (v0.3:337, 339) | The Commission row reads S01–S19; the I.O1 row adds S19 | See the note below. |
| §9 (v0.3:357, 359) | The v0.3 package adds the builder evidence; the L6 hold lifts on both current signatures; the Cottonwood hotfix note is updated | Process text only. |

**The builder prerequisite.** S02 and S19 addresses use `address("gateway", "49financial", …)`. That resolves only
once the `systems.json` `gateway` row lands, which is COO~G's to add as a PLATFORM_SUBSYSTEM owned by D9. Rule 30
makes a builder refusal a missing registry row to add, never a typed workaround, and the PRD types no address.
CTO97152 records this as a build prerequisite rather than a review hold. It is accepted as such.

## Note, non-blocking: S19 missing from three coverage rows

S19's manifest row (v0.3:326) serves **FWD-1, FWD-3, FWD-5 and FWD-8**, with acceptance rows A01, A03, A05 and A08.
Coverage row I.O1 (v0.3:339) lists S19. Three rows do not:
- I.O3 (v0.3:341) reads "S02-S05";
- I.O5 (v0.3:343) reads "S05/S07-S11";
- I.O8 (v0.3:346) reads "S12-S15".

The content those rows would point to is carried elsewhere: Silver failure blocks a complete cohort, and replay only
deduplicates. It is in §3.2a (v0.3:167–171) and in S19's own row, and nothing contradicts it. So this is an index
gap, not a missing requirement, and it is not a ground. **At the next bump, add S19 to those three rows.**

## Coverage

Apart from the lines above, the brief half is byte-identical to v0.2. So the v0.1 and v0.2 checks stand: the carriage
of O1–O8 and §II–§VII, 18 of 18 headings, and ATTESTED-only membership.

## Limits

This is requirements acceptance only. No Bronze write, Silver normalization, membership run or publication was
exercised. The `gateway` registry row does not exist yet. The CONTRACTS addendum, CTO97115's F1–F3 reasoning and the
exceptions' contract entries are in the ratified-text half and belong to `3.0.0_SA_CVO`. The S16 activation
prerequisite is unchanged.

The delivered notices 97156 and 97158 were opened and READ-acked. This seat performs no push, deploy or cloud
mutation. Push state is measured and stated in the completion message to `1.0.0_SA_CTO~A`.
