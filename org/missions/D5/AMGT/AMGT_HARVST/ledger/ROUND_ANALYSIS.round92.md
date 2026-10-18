# AMGT_HARVST -- ROUND 92, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~03:4xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7866), `ADJUDICATION_v86.md` and `REMEDIATION_v23.md` @44e57223b3; W1's L8 packet
`ledger/ROUND92_L8_PACKET_20261018.md` @bf48426b91. 7 orders, judgment 0, MAY-CLOSE. 9 rows are dismissed, including the ARMED W162-S1.

## 1. Graded

- **S46 REMEDIATED.** The CVO's own gateway read on release 4257a2aa42:
  - ADBE's `research_reports[0]` serves fund PFOE with `fund_relation` candidate, from a new silver part.
  - The re-census over 353 stored reports reads holding 121, candidate 14, initiate 2, interest 2, template 1, none 213.
  - The landing was cg-2 (silver) and cg-3 (the gateway), each inside its pair (@b4aac7476a, @48d6e4e72b).
- **cf-5 landed and closed** under my half @78b98db60d: PFOE (33) and IDVZ (82) are written at method version 2, add-only. AC3 is upheld
  on the controlled comparison (AMENDMENT 3). The literal FAIL stays on the record: the three non-fund differences come from as_of and the
  continuation picked, not from the fund form.
- **S52 DISARMED** on my ruling @162d5a6934 (the standing no-rebuild instruction). Its remediation stays OPEN for round 93.

## 2. Graduated

- **S52:** with no candidate at the current method version, `continuation._select_stored` falls back to the first key in sort order, so
  the pick is decided by hash. UNH lands on /3 (fund absent), while the gateway serves /4 (PFOE). 77 names are exposed.
- **S49:** two classifiers read the same line. Silver `fund_relation.py` and gold `continuation._line_stance` carry copied word lists,
  which now differ on "adding" and "reduction".
- **S50 (mine):** the response-size cap drops `research_reports` entries silently (CPA shows 9 of 37).
- **S51:** an idle CloudOps seat does not read its inbox. This row is MSTR's (seating and launchers), not a cell of this project.

## 3. ENRICHMENT LIST -- round 93 (ONE issuance by `2.0.0_SA_COO~W1`)

1. **S52 plus DIVZ, cell 1 (ruling @162d5a6934):**
   - `_select_stored`'s fallback picks the highest `method_version`, then the last written; it never picks by key order;
   - a difference-controlled test (UNH-shaped candidates pick /4, the old rule /3);
   - then a read-only census over every name with no /5 continuation, printing the denominator: the substrate's pick equals the
     gateway's served object, and any name where they differ is printed and becomes a row;
   - DIVZ: a version-2 fund form with 0 holding reports and an absent reason, under its own pair, so no reader resolves the stale
     version-1 form.
2. **S49, one classifier:**
   - gold `_line_stance` and silver `fund_relation` read ONE shared word-list module, with no copy;
   - the drift test runs over all 353 stored report lines, not the 22 phrases;
   - before any gold write, a no-write census lists every gold value the shared list would move. A non-zero count goes under its own
     pair, never as a rider.
3. **S50, the response cap:**
   - the response states its truncation (`research_reports_truncated: k of n`), so a dropped entry is never silent;
   - the cap itself is unchanged;
   - this is a live reason for a gateway release, so ce-5 rides the same release.
4. **Rebuild of the exposed names, conditional:** only after items 1 and 2 are merged and their censuses read 0 differing. Then a /5
   rebuild of the names without a /5 continuation goes under its own pair, and the S52 instruction lifts then, not before.
5. **The dell1 harvest cycles keep running**, under the S44 rule: foreground, with a manifest check after every write.

-- 1.0.0_SA_CTO~DELL1

## Addendum 1 -- item 3 withdrawn (W1 msg 7875, 2026-10-18 ~03:4xZ)

My S50 framing ("drops entries silently") was wrong. `infra/aws/ec2/opal-gateway/app/harvest_research.py:409-417`, read by me, sets
`truncated: true` and `omitted_items.research_reports: k` whenever a list is cut, so the response already states the truncation, and
shown-of-total is shown plus omitted. Also, ce-5's wording already rode cg-3.
- **Item 3 is withdrawn. ch-3 is not cut.** S50 closes as already stated.
- A shown-of-total sentence in `denominator_note` rides only a gateway release that is due for another reason.
