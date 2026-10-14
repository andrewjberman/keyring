# MDPF_SECCLASS -- ROUND 24, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~12:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 5505, `surprise-channel/adjudications/ADJUDICATION_v23.md` @22af7de1a4 with REMEDIATION_v14.
- MAY-CLOSE: 18 orders, 14 complete with proofs. `TO-DEPLOY-e57e61` is held outside the verdict, and its hold is now stated (packet @d4286aab30 section e57e61).
- 22 of 22 rows are dispositioned. D1-W83-S5's clock is closed: XA-20261014T113939Z-a304 reads DELTA=0 as canonical-JSON equality.

## 1. The reading the CVO asked for: FWD-1's "never consulted at any step" = THE CLASS PATH

**Ruling: "at any step" binds the steps of the trace FWD-1 describes, from the shared list to the page the advisor reads.** It does not bind every step of the
Black Diamond chain run. **The CVO's grade stands as stated.** B_01b (it writes new securities into `bd-securities`) and E_18 (it reads them) put no class on any page,
so they are not on the traced path.

**Why (TAXONOMY LAW, intent coherence: one axis, one intent):**
- The chain-wide claim "nothing uses the old copy" is FWD-5's own ACCEPT, verbatim: "the FWD-4 check and the list of who is allowed to read the old copy both show no
  remaining user".
- Reading FWD-1 chain-wide would put two cards on one axis. FWD-1 could then never realize before FWD-5's deletion, although its DONE WHEN is one live run traced
  to a page.
- B_01b and E_18 remain FWD-4/FWD-5's open work, as the slug says.

## 2. Graded

| FWD | Verdict | Read |
|---|---|---|
| **FWD-1, the Black Diamond page half** | **REALIZED** (the class-path reading, section 1) | The 10-13 23:00Z and 10-14 04:00Z fires wrote the served client pages 05:47Z-05:48Z, `data_as_of` 2026-10-09 (D1-C-S21). On the largest real holder of each: GLD commodities/Metals, PHYS commodities/Metals, VXX structured/Hedge, each with `class_source etf-classifications` equal to the list's own row. Every top holding on the three pages comes from the list (16, 15 and 22 of 16, 15 and 22), 0 unclassified. The served classifier bytes equal the repo by content. |
| **FWD-1, the "same as Positioning" limb** | **NOT_EVALUATED** | The CVO did not render Positioning. Its evidence is PRD line 236 (both Positioning surfaces read `etf-classifications`), which is a design statement, not an exercised artifact. The grader's bar takes no limb on prose. **One read closes it (section 4, item 2).** |
| FWD-2 to FWD-17 | not re-graded | This round moves none of them. |

**Round 19's defect is closed:** the 23 placeable securities ($966,285) are placed. The residue is 4 tickers (HPI, CUBE, GLPI, PCEF; $63,967.82) with no ticker,
`NAME::` or CUSIP row in the list, so they are unclassified by right. Adding rows for them is list maintenance (section 4, item 5), not a classifier defect.

## 3. This seat's rows

- **D1-S36 (ARMED): the e97 bars and advisors clauses against the Oct-12 baselines.** XA-20261014T014758Z-01a0 rules the re-base: the bars are re-based to
  post-restatement baselines as a class in the round-25 recut, never mid-round. Round 25, item 1. It disarms on the re-based read.
- **D1-S27 (C_06's firm `total` minus the sum of its class values: -4.71, +128.06, -128.57 on 10-06..10-08), cause named as share rounding: ACCEPTED as
  rounding, with a stated bound.**
  - The bound: |total minus the sum of the classes| <= $1,000 per firm-date. That is about 8x the largest gap seen.
  - Any date over the bound re-opens the row as a defect.
  - D_04's `Unclassified` line (total minus six classes) therefore differs from C_06's `unclassified` class by the same cents. That is disclosed, not corrected.
  - **Owner of the bound's check:** `2.0.0_SA_COO~M1`, folded into round 25's re-base read (the same objects), with no new cell.

## 4. ENRICHMENT LIST (round 25, ONE issuance by `2.0.0_SA_COO~M1`)

1. **The e97 re-base as a class** (D1-S36, XA-01a0): the bars and advisors clauses re-based to post-restatement baselines, read on the first scheduled fire after the
   recut. The D1-S27 bound is read on the same objects.
2. **FWD-1's Positioning limb, ONE read:** render both Positioning surfaces for GLD, PHYS and VXX and compare class and sub-class with the Black Diamond page values in
   D1-C-S21. Equal on all three -> FWD-1 REALIZED whole. Any difference is named, with the surface that differs.
3. **C_06 writes JSON with sorted keys** (D1-S37; XA-a304's follow-up), under its own never-widen pair. The pair names the served objects whose bytes move with no
   content change. Until it lands, every DELTA read on this writer uses canonical-JSON equality and says so.
4. **Conditions carried, not cells:**
   - D1-S39: any pair that ships `code/gold/lib/` names DB-b-181's classifier radius, or the deploy pins the served classifier (owner `~M1`);
   - e57e61's L3 waits on a SCHEDULED new-security run that plans US stocks. **The issuer names that run's date in the packet.** If none is scheduled within
     5 trading days, it states the trigger that will plan one.
5. **The 4-ticker residue:** `~M1` files one request with the list's owner to add rows for HPI, CUBE, GLPI and PCEF (the evidence: names and CUSIPs from the
   10-09 lots). It is not a SECCLASS cell.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- **The client-facing BD Mix PROD push** (CLAUDE.md Agent Autonomy: a portal PROD push that changes a client-facing page waits on his word). Its card names the
  AUA restatement and its size (+249..+263; -30,914.72 on 10-09), per XA-01a0.

-- 1.0.0_SA_CTO~DELL1
