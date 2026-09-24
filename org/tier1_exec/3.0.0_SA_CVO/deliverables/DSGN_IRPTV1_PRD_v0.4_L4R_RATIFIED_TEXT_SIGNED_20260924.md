# L4-R review -- DSGN_IRPTV1 PRD v0.4, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`c4b9056831` (v0.4). **Half:** ratified-text,
hash `a398ff25a800` (from `4540ecd4e08a` at v0.2/v0.3), re-measured from HEAD's bytes with
`prd_signoff_lib.half_hashes()`. **Delivery:** `1.0.0_SA_CTO` msg 100295, READ-acked. **Prior:** REFUSED at v0.3,
review `DSGN_IRPTV1_PRD_v0.3_L4R_RATIFIED_TEXT_REVIEW_20260924.md` @`e0915c97fe`, stamp @`bdb01ee145`.
**Verdict: SIGN.** The bump touches exactly what the refusal named, and nothing in the pin moved.

## R1 -- `unprojected_grant` is now in CONTRACTS: CLOSED

The new paragraph states the fact's class (PARTIAL-DATA, not entitlement bookkeeping), the visible-indicator rule on
the BODY of every scoped view with the header included, the disclosure's share (kinds, denominator, revision), the
two-shape rule (a refusal carrying `public_reason_code` UNPROJECTED_GRANT renders its reason and no count), and the
`irpt-holdings` structural zero until IB-rtf-8 folds the fork. It cites `IRPT_FNTEND` CONTRACTS v0.7-v0.9, ruling
@`61627f39f9` condition 2 and row `IRPT_BCKEND-W1-S28`, and it states why FWD-2's ACCEPT line does not move. That is
the fix as written, and it closes the conjunction: a C1 cell that hides the indicator now fails this PRD's own text.

## R2 -- the count and the unit: CLOSED

"the ten consumed contracts under `docs/contracts/investor-reporting/v1/` and the operations that serve them" is
the counterpart's unit (ten consumed of an inventory of eleven, `RenderPackage` produced). The three
NO-HANDLER-AT-HEAD routes (`analysis-input-upload`, `analysis-request-read`, `analysis-request-history`,
`routes.json` @`124c0694b7`) sit in the Deferred list as Y's, with FWD-7 / FWD-8 named as standing on them.

## What still holds, re-measured at the new pin

- **ENDPOINT verbatim:** the fenced block at `c4b9056831` and the endpoint record @`5daacc16db` are IDENTICAL, 91 of
  91 lines, 0 diff lines. The ENDPOINT section (heading to next heading) is byte-equal between v0.3 and v0.4.
- **FWD-8's SOURCE now resolves at the PRD's own brief pin.** `brief_ref` moved to @`5cc838e696` (23,785 bytes, 303
  lines); its O6 carries the prospect paragraph -- Prospect identity card in place of "No client selected", upload
  path first when no client is selected, owned-request history, re-open / re-run from retained input -- which is
  every clause of FWD-8's ACCEPT. At the old pin `fb90ad8fe0` the word occurred once; at this pin 8 (case-insensitive
  count; the CTO's header says 7). The ENDPOINT bytes did not change, so this is the pin catching up to the text, not
  the text moving.
- **No seat name inside the ENDPOINT section.** CONTRACTS now names `1.0.0_SA_CTO` twice (the ruling's origin and the
  row's disarm owner) and two commit hashes; the spine's no-seat-name clause is scoped to `_top_section` of ENDPOINT,
  and the counterpart's CONTRACTS carries seat names and pins in the same way. Not a finding.
- **The v0.3 observation is now in the text:** enrichment item 11 says a passing round-1 trace leaves FWD-1
  NOT_REALIZED until `spread` is served. The sequencing line further names the Performance path's two external
  preconditions for hop 6 (X10 enforced + repackage; one installed one-use plan on Andrew's per-use word) and the
  CTO's choice that L6 does not wait on the plan. Both are brief-half text; they contradict nothing in this half, and
  they make the round-1 trace's expected hop-6 outcome explicit before a cell is cut.

## Carried unchanged from the v0.3 review (state, not text)

`display` is in the portal wire (`bf3b971b`, on DEV `7975c3bb`) and not in the docs schema copy; `CUSTODY_UNITS` and
`spread` are in neither copy at HEAD. The text says "ruled", which is true; "lands in both copies" is the order rule.

## Instruments

| question | instrument | result |
|---|---|---|
| ENDPOINT verbatim at the new pin? | `difflib.unified_diff` on the two fenced blocks | 0 diff lines, 91 of 91 |
| ENDPOINT section moved v0.3 -> v0.4? | section-slice equality on `git show` at both pins | equal |
| half hash? | `prd_signoff_lib.half_hashes()` at HEAD | `a398ff25a800`, matches the delivery |
| what changed in my half? | `git diff 118613ddb0 c4b9056831` on the PRD | CONTRACTS: the operations line, the Deferred list, the new paragraph; nothing else in the half |
| FWD-8 sourced at the pin? | O6 section read at `5cc838e696` | prospect paragraph present, every ACCEPT clause sourced |

-- `3.0.0_SA_CVO`, 2026-09-24 ~05:5xZ
