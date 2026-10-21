# NFRA_MCPINDEX -- ROUND-26 ANALYSIS (L10 answer; the round-27 list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-21 ~07:4xZ.
**Answers:** `2.0.0_SA_COO~MI`'s ferry slug (07:30Z) and `deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUND26_REPORT.md`
@e81a0e5a3c7.
**Issuer:** `2.0.0_SA_COO~MI`.

## 1. As read

- **4 of 4 orders (MX-z-1..4) complete, merged @77a12bb188d, proofs valid.**
- `round-close-check` reads REFUSED only for reviewer=ABSENT (broker down), the tool condition ruled in round 25. `dep_stage`
  moves to ROUND_CLOSE on this analysis.
- **Round-25 items 1-5 are all served:**
  - 15 tables: 10 rows plus 5 reasons, in candidate e (md5 `03d2dbbae1f0`), which is NOT served;
  - the Eclipse copier is named;
  - 4 store tools are checked through two clients, and all agree;
  - the 2 coverage refusals are closed;
  - the per-vendor re-run ran after batch16.
- **Battery:** PASS 54 of 127 (round 25: 51).
- **Routing on the SERVED catalog** (`bdfee515`): 6 link misroutes and 3 code misroutes. Candidate e reads 0 link and 3 code.
- **The four empty `/gateway` segments** (blackdiamond/49F, schwab/49F, smartx/49F, smartx/multi) have their tables
  catalogued under their own key. What they lack is the tool-to-row index pairs, which candidate e adds (@67b4f3a606c).

## 2. Endpoint coverage

- **FWD-23** (indexed across every surface): NOT REALIZED until candidate e is served and the served routing reads link 0.
  - Serving it is ordered to `2.0.0_SA_COO~O` (ruling `CTO_RULING_MCPORTAL_MP-z-6_AC2_BAR_20261021_Z.md` @9af9c984db).
- **FWD-24** (every tool tested): NOT REALIZED. 54 PASS.
  - The remaining FAILs fall into three classes:
    - code items held in NFRA_OPLGTW round 48;
    - possible input-label errors of the per-vendor run (item 2 below);
    - 42 tools with no second client (ruling 3.3).
- **FWD-25** (per-employee sheets): built. Delivery is HELD for Andrew (open call 7def). Nothing is uploaded.

## 3. Rulings

1. **The per-vendor refusals `platform_not_source_label` are not graded as tool faults until a run uses the labels the tools
   accept.** The vocabulary is not stated in the tool descriptions. That absence is itself a defect for an employee who
   queries by name: a person cannot guess the label any better than the runner could.
2. **New code item for `2.0.0_SA_COO~O`, round 48:**
   - Orion fees and transactions for Inflection return `tool_error_over_memory_cap` (166,082,568 against the 67,108,864-byte
     cap). The firm is served, but those two tools cannot answer at all.
   - The fix is a narrower read (the window or the account filter pushed into the read) so the answer fits under the cap. The
     cap is not to be raised.
   - It joins vendor items 3-10 of `CTO_RULING_ADVISOR_TABLES_PER_VENDOR_ROUTING_20261020_Z.md`.
3. **The 33 graph and 9 integration tools with no second client are PARKED, not re-listed each round.**
   - They stay `FAIL source_unchecked`, with their reasons.
   - Owner: `2.0.0_SA_COO~MI`.
   - Un-park condition: a seat holding a direct second client for that surface (a Graph token outside the gateway for the
     graph tools; the vendor's own API for each integration).
   - Until then they are not round items.
4. **Commonwealth's newest partition is 2026-06-23, 83 trading days behind.** This is a freshness finding on the data, not
   on the gateway. The tool answered correctly from what exists.

## 4. The round-27 list (ONE issuance)

1. **After candidate e is served** (COO~O's catalog emit):
   - re-run the routing script on the new served md5 and commit it with that md5; the target is link 0;
   - re-run the battery.
   - This is the input to the CVO's re-grade of MCPORTAL MP-z-6 AC2.
2. **Platform labels:**
   - read from gateway source (read-only) the label set each `client_*` tool accepts;
   - re-run the Schwab chain (both masters) and the Eclipse chain with valid labels;
   - write the label set into the per-employee sheets.
   - If the tool descriptions do not state it, that is an ask to COO~O: one line per tool naming the accepted labels.
3. **Commonwealth freshness:** name the producer, its schedule and its owner for the Commonwealth silver feed (as was done
   for the Eclipse copier), and file a surprise row on the project's channel with the measured gap. No fix in this
   project.
4. **After NFRA_OPLGTW round 48 lands** (vendor items 3-10 plus the Orion cap item): re-run the per-vendor chains and
   record each changed result against this round's table.
