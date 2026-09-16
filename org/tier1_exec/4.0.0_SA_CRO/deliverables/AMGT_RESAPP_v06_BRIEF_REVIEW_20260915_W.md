# AMGT_RESAPP v0.6: brief-half review

Reviewer: `4.0.0_SA_CRO~W`. 2026-09-15 06:11 UTC.
Request: exact inbox messages 23048 and 23050, both from `1.0.0_SA_CTO~W`.
Target: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`
at `2f3b65d8b842847bd31eefc63766593bcc235b42`, brief half `90b966c9b310`.
Brief pin: `docs/briefs/amgt-resapp-security-analysis-20260910.md@19ce7d5b4d`.
Previous signed target: `932d83eb1704f3e9e9364a803a6478d178c23093`,
brief half `7c533738184f`.

## Verdict: REFUSE pending explicit supersession and supplement carriage

This is a scoped delta review, not a regrading of implementation or the CVO's
ratified-text half. The Git diff from the previous signed target establishes
that the new brief-half substance is section 9. Section 9's own declaration
that sections 2-8 remain unchanged creates an actionable ambiguity for the
decomposer; the new requirements need an explicit precedence map.

### R1. The addendum preserves requirements that its new design supersedes

Pinned lines below are in the PRD at `2f3b65d8b8`:

- Lines 969-971 say sections 2-8 and the surface manifest do not change.
- Lines 698-701 retain three tabs and the Model tab cut, while the newly
  introduced C-PAGE-LAYOUT at 355-364 restores Model and specifies five tabs.
- Lines 703-709 retain C-AMGT-ARTICLES-STORE, requiring article content in
  DynamoDB and describing S3 as the model/print home. New C-ONE-STORE at
  367-375 makes S3 the article source and retires DynamoDB as a source after
  reader transition. S16's manifest row still names the older store constraint.
- Lines 724-738 and 903-906 retain mandatory EC2/cloud-lambda acquisition and
  explicitly rule out SiteZ. Andrew's direct instructions in this session
  instead require local auth and local REST pulls while reserving activation
  and collection cadence. Section 9c at 1000-1003 preserves that reservation,
  but does not identify the former EC2 prescription as superseded for the
  current local work.

**Requested repair:** in the brief-half addendum, enumerate the old clauses
and manifest references being superseded, the replacement contract, and the
transition condition. Keep earlier decisions as dated history if useful.
Explicitly preserve the local commissioning boundary and Andrew's cadence
reservation. No new infrastructure deployment is requested by this review.
The reviewer is not editing the CVO-owned CONTRACTS section.

### R2. The new supplement's source and content coverage are not reviewable as written

Section 9a, lines 977-983, uses abbreviated paths containing `...` and short
topic summaries. Section 9d names recommended future work, but does not supply
a section-by-section supplement coverage map. The L4-R brief-half bar requires
content carriage (fields, units, paths, guards and proof gaps), a denominator,
and the consuming surface, not a pointer alone.

**Requested repair:** provide exact source paths and pins for the added
Andrew-direct/substrate material; enumerate the source sections/records in
scope and map their substantive requirements to the new contracts and
existing or proposed engine surfaces. Include the known measurement limits
(one-company filings sample, five uncited outputs, loose Lusha filter/no
tenure, unpopulated peer universe) and the corresponding required checks.
This is an L4 coverage map, not a demand that CTO pre-cut COO's task orders.

## Positive findings and limits

The new section explicitly preserves the portal hold, no push, no outcome
grade, and Andrew's harvest collection reservation. The proposed S3 reader
transition addresses the actual disconnected article-store seam found in the
Chatter audit. The measurement summaries distinguish the loose Lusha filter
and missing tenure field; these are useful limitations to carry into the cut.

The prior brief and retained constraints were inspected for the affected
boundaries; this refusal does not claim a fresh exhaustive certification of
every unchanged v0.5 section. Decisive defects above are sufficient to withhold
this changed half. No outcome was marked unrealized solely because its code
is not yet built; these findings concern conflicting and missing specification
carriage. No POSN work is taken on by this review.

Push state: LOCAL. This seat does not push.
