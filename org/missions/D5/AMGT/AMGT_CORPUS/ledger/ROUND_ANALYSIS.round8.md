# AMGT_CORPUS -- ROUND 8 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~01:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26353, READ-acked, subject *"L10 SLUG AMGT_CORPUS round 8
@b685951395"*, citing `surprise-channel/adjudications/ADJUDICATION_v11.md`. Issuer packet
`deliverables/2.0.0_SA_COO~X/ROUND8_DRAIN_END_PACKET.md` @`895a999451`.

**Round 8 is CLOSED. The project is NOT closed.**

---

## 1. MY ROUND-7 RULING WAS WRONG ON ITS PREMISE, AND THE ROUND SHOWED IT

I ruled "prose first": serve the text under each case heading. The round measured all 95 names: **no stored pack carries
prose under a case heading.** The three headings are the ROW LABELS of a 3-case x 5-year scenario table on page 0, so
"text under the heading" reads the table body, and only the last label (Downside) has anything after it. The CVO ran the
as-built rule itself on ADBE and AZN: **Downside receives all three cases' numbers; Upside and Base are served ABSENT.**
`j-1` AC3 is NOT MET, and the rewrite was correctly HELD (`Z-S53`), corroborated on two planes (no change entry; AZN still
serves the heading).

> **I ruled on where the team's cases live without reading one pack.** The heading was a label, not a section. The
> cheaper route was the right instinct; the unread premise made it the wrong cell.

**What the round did find is the answer:** the team's own Upside/Base/Downside numbers ARE present, positional and citable.
ADBE Price 2026 reads `416 / 233 / 143`; AZN carries its unit (the pound sign U+00A3, 30 times, read by codepoint census).

---

## 2. RULINGS

1. **ADOPT THE TABLE-AWARE CASE RULE** (packet s.3). From the case labels, read the year-header group length k; each
   metric row's 3k values split by case, `[ik, (i+1)k)`; serve `{metric: {year: value}}` with the page citation. A row whose
   value count is not 3k reads ABSENT with that reason. **Two additions from the L9:** carry the unit read from the row
   (the pound sign on AZN), and print the Upside >= Base >= Downside ordering per name as a census column, **never a refusal.**
2. **`Z-S51` -- the question the CVO put, answered.** `b56fef3032` IS the fix: it is AMGT_RESAPP's `case_rule.py` on the
   adjusted basis Andrew ruled (record @`c027b4726f`); the trailing P/E is `PX_LAST / IS_COMP_EPS_ADJUSTED`
   (`case_rule.py:13-19`, read at HEAD by this seat for the uu-4 half). The pairing flagged at RESAPP round 45 is gone on
   the P/E side; the EPS side's "adjusted" is still a label (the BEST_EPS basis object never says it -- my uu-4 half s.4).
   **The re-derive runs in round 9, AFTER the combined scoped-API deploy lands**, so the stored blocks and the served
   adapter move to one rule in the same window; it carries a never-widen pair (the derive report reads SERVED 49 -> 69, and
   CAT_US SERVED -> ABSENT, which the pair must name).
3. **The six keys with no adjusted EPS (`Z-W3-S6`: 6861_JP, BZLFY_US, CAT_US, CSL_AU, PBR_US, TSM_US).** No landed stamp
   carries a single `IS_COMP_EPS_ADJUSTED` figure. **No GAAP fallback**: Andrew ruled the adjusted basis, and a fallback would
   silently serve the pairing he ruled out. They stay ABSENT with the rule's own reason. A scripted Bloomberg pull for
   those six is vendor egress and goes to Andrew as a card; nothing is cut for it.

---

## 3. FWD GRADES

- **`FWD-12`: NOT REALIZED.** Limb 3 (the team's cases, cited) is NOT MET; the table-aware rule is the round-9 route.
- **`FWD-9`:** `j-2`'s code census reads unresolved 0, rc 0 (@`db5f64c8f3`), with the plant outside the censused tree per
  the round-7 ruling. The CVO did not grade it at L9 (no judgment criterion), so this seat records the mechanical read and
  does not grade REALIZED on it alone.
- The remaining outcomes stand as `i-5`'s evidence pass recorded them.

---

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 9 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Table-aware case rule + the held dossier rewrite** | s.2 ruling 1; the rewrite under a never-widen pair (`--write --workers N`); `Z-S53` lifts on it. JUDGMENT: *does each served case read as that case, in the team's numbers, with its unit?* -- graded on names from more than one currency |
| 2 | **Re-derive the model blocks under `case_rule.py`** | s.2 ruling 2; gated on the combined scoped-API deploy's close; never-widen pair naming 49 -> 69 and CAT_US |

**NOT cells:** the six keys' pull (Andrew's card); the worker worktrees and `%TEMP%` dirs (recursive deletion, the
operator's word).

## 5. WHAT THIS ANALYSIS DOES NOT DO

It does not close the project and changes no outcome, so no L4-R half re-opens.

## Compiler Tools

The CVO's own run of `dossier._resolve_case_field` on ADBE and AZN taken as the L9 measurement; the packet's 95-name survey
(s.3) read to EOF; `case_rule.py:13-19` as read at HEAD for the uu-4 CTO half (`@f266db8833`) to answer `Z-S51`; rows
`Z-S51` and `Z-W3-S6` read from `INVESTIGATION_v1.md`.
