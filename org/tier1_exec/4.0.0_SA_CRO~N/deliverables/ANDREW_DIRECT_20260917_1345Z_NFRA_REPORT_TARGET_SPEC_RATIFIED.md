# ANDREW-DIRECT 2026-09-17 ~13:45Z -- NFRA_REPORT: target output spec ratified via in-session interview

- **Channel:** Andrew, direct, at the `4.0.0_SA_CRO~N` terminal (live interview, same session as the two prior
  records below). **Recorded by:** `4.0.0_SA_CRO~N`, same turn.
- **Scope:** surfaced verbatim, adjudicated neither wider nor narrower.
- **Prior records:**
  - `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_NFRA_REPORT_SPAWN_CRO_N_RESEARCH.md` @fe679f1b6e
  - `org/tier1_exec/4.0.0_SA_CRO~N/deliverables/ANDREW_DIRECT_20260917_1333Z_NFRA_REPORT_EDITION_DIAGNOSIS_AND_INTERVIEW_ASK.md` @28b0a3ccd6

## 1. RESEARCH THIS SEAT DID BEFORE ASKING (grounding for the answers below)

- **No deployed-vs-repo drift.** Live `opal-infrastructure-monitor` reads `CodeSha256
  j7lljv8S5efk1KJz0Zh7+pV0+PIfcYbCOVJY2TE0/kE=`, `LastModified 2026-09-10T16:35:55Z`, `CodeSize 54009` --
  identical to `RP-s-23`'s own `DEPLOY.md` record, and no repo commit has touched `lambda_function.py`,
  `edition.py` or `edition_rows.py` since. What Andrew is reading IS the repo.
- **The failure was already diagnosed, once, and never fixed.** The afternoon `RP-s-23` deployed (2026-09-10,
  same day), Andrew read the live output and the project's own CVO logged it verbatim at
  `surprise-channel/adjudications/ADJUDICATION_v1.md` row `NFRA_REPORT-Z-C-S16` (~18:34Z): *"I look at it and
  have no idea what it is supposed to mean"; "we are lacking cost data, we are lacking so many fields the old
  version had."* Root cause per that row: the new row shape carries only `(state, delta)` and cannot hold a
  section's real content; two sections (`aws_costs`, `openai_cost`) were OMITTED entirely (no OK/DEGRADED/BREACH
  field to hang a row on); the other ten were flattened to one state label each. Disarm owner named:
  `2.0.0_SA_COO~ZZ`, for an L5 re-decomposition. **Not done.** One commit has touched this project's tree since
  (`1ed4ade1bb`, a PRD header-count fix, no content change); `2.0.0_SA_COO~ZZ` is not currently registered and
  its most recent logged work is a different project (`AMGT_RESAPP`). The broken renderer has run live,
  unmodified, for one week.
- **Section-mapping proof:** `deliverables/0.9.0_WK_NFRA_REPORT~2/SECTION_MAPPING.md` -- of the 13 collector
  sections, `aws_costs` (MTD total + top-10 services) and `openai_cost` (per-function token/dollar accounting)
  are OMITTED-WITH-REASON entirely; the other 10 become a single state label + delta word each.
  `TO-RP-s-23`/`TO-RP-s-24` both still read `<status>open</status>` at HEAD.

## 2. THE INTERVIEW -- HIS ANSWERS, VERBATIM AND ENTIRE

> Old-style prose detail as primary body. Both costs breakdowns. Maybe a table where the various IDs and labels
> are on the right column and the simplified/summary name on the left column. Also, add a section somewhere,
> maybe in an additional column all the way to the right that has a brief summary of what the function does.
> Yeah we can use the old one. Audience is just me.

## 3. SYNTHESIZED TARGET SPEC (this seat's translation of the above into report structure; not yet PRD language)

| # | requirement | source clause |
|---|---|---|
| 1 | **Primary body is the OLD renderer's prose-per-section style** (`format_report`, `lambda_function.py:2023-2462`, still defined and untouched), not the new state/verdict-table model as the body. | "Old-style prose detail as primary body." |
| 2 | **Both cost sections render in full**: the raw `aws_costs` breakdown (MTD total, daily avg, top-10 by service) AND the per-pipeline `cost_depth` trend/anomaly view. Neither is dropped or replaced by the other. | "Both costs breakdowns." |
| 3 | **A 3-column identification table** wherever the report names a technical resource (SNS topics, CloudFront distribution IDs, Lambda/EC2/ECS names, etc.): **left** = simplified/business-friendly name, **middle** = the raw ID/technical label, **right** = a brief plain-English description of what that resource/function does. This is the resolution to the "random lambda strings" complaint -- keep the technical identifiers (for reference/traceability) but never bare, always paired with a name and a description. | "a table where the various IDs and labels are on the right column and the simplified/summary name on the left column ... an additional column ... a brief summary of what the function does." |
| 4 | **Immediate stopgap authorized:** flip the handler back to `format_report` (the one-line revert of `RP-s-23`'s own change) for the next scheduled run, while items 1-3 are built. `format_report` is still defined and reachable, wired out, not deleted -- this is a revert, not new construction. | "Yeah we can use the old one." |
| 5 | **Audience is Andrew only.** No sanitization requirement beyond items 1-3; internal detail is fine as long as it's organized per the table in item 3. | "Audience is just me." |

**Not decided here and not this seat's to decide:** whether the new state/verdict/delta model (the "does
something need Andrew today" line, per-row better/worse/unchanged) is KEPT as a short header on top of the old
prose body, or dropped entirely. Andrew's answer describes the BODY and does not address the summary line either
way. **Recommend the CTO ask this one narrow follow-up before cutting the PRD amendment** -- everything else
above is unambiguous.

## 4. HANDOFF

Per the spawning record's own terms (*"I will work with them in their session to realign that project as
needed"* / *"the L2/L4 work returns to 1.0.0_SA_CTO~Z by message"*): this seat's research-and-interview scope
ends here. The spec in section 3 is handed to `1.0.0_SA_CTO~Z` for L4 PRD amendment (round 5) and re-dispatch.

**Operational facts the CTO will need, surfaced not adjudicated:**
- `2.0.0_SA_COO~ZZ` (this project's seated COO) is not currently live/registered and has not touched this
  project in a week. A seating decision (reactivate `~ZZ`, or seat a different COO lane) is the CTO's/MSTR's.
- `2.0.0_SA_COO~Z` is live but already holds `AMGT_RESAPP` as its one project (Rule 27's one-project-per-Tier-2-
  seat-instance binds at the seat, not the project) -- it is not a free substitute without a fresh lane.
- The blocking hazard `NFRA_REPORT-Z-S24` / adjudication `NFRA_REPORT-Z-C-S16` is still ARMED at HEAD; a round-5
  decomposition is what disarms it (its own stated condition).
- The stopgap revert (item 4) is a live-Lambda deploy and falls under the same `C-DEPLOY-PATH` /
  `C-CHANGE-LEDGER` / NEVER-2 constraints `RP-s-23` already exercised once, successfully -- the same path
  applies to reverting it.
