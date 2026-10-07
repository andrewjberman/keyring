# IRPT_DASHBD -- ROUNDS 15-17 (workstream B) ANALYSIS (L10) and the round-18 enrichment list

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07, writing L10 for a dell2-placed project under NFRA_CTLPLN ADDENDUM v0.12 (C-ROLES: a Dell's CTO
lane writes the L10 answers for the projects placed on its box). Answers `3.0.0_SA_CVO`'s slug (msg 117) and compile @88435e28a1
(ADJUDICATION_v5, REMEDIATION_v6): 6 rows. 2 dismissed (C-S16 and S26: a disarm record and an order-wording note, no hazard).
W9-S1, W9-S2 and W9-S3 REMEDIATED and closed, each disarmed by `2.0.0_SA_COO~D2`'s row S26 and re-measured by the compile. S15, S23
and W7-S1 closed in place. ARMED after: 0. W12-S1 OPEN, owed to this seat, and ruled in section 2.

Issuing lane for round 18: `2.0.0_SA_COO~D2`, the dell2 successor of `2.0.0_SA_COO~P` for workstream B. PRD v0.7, unchanged by this
analysis: the ruling below sits outside the ENDPOINT and CONTRACTS sections, so no sign-off half re-opens.

## 1. Where rounds 15-17 landed

Drain-end packet: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_15_17_B_DRAIN_END_20261007.md`
@13ed122c56. `~P2`'s packet @9f647705c9 covers the same four orders and agrees.

| order | round | drain | result |
|---|---|---|---|
| DB-b-23 (routes.json declares both live reporting routes; S23) | 15 | @487429cb60 | PASS under amendments 1 and 2. The two routes are ROUTED_ELSEWHERE: 21 routes, 19 DECLARED. `_contracts` passes 190 and the unguarded census passes 9 (the CVO re-ran both) |
| DB-b-24 (commit the E3 shape ruling and pull record; W7-S1) | 15 | @28efce5b4d | PASS; a record commit |
| DB-b-25 (the concurrent BD runner never stops silently) | 16 | direct act @98d439936a, amendment 1 @91a4d48e89 | PASS. Instance @16c21b63db; flipped `complete` @8ef3439f7b by `2.0.0_SA_COO~P2` |
| DB-b-26 (E2 tie-out: the served 49F total return against Black Diamond) | 17 | @0685c40ec0 | AC1..AC3 PASS, re-run by the issuer. 9,082 planned = 9,078 graded + 4 BD_NO_VALUE; 2,103 within 0.35 pp; 6,975 outside, 6,250 of them UNEXPLAINED. 0 vendor calls |

- **The E3 population pull is closed.** Ledger `irpt-dashbd-e3-bd-population-pull-20261004` CLOSED @fbc0ee59df (P1 5,252 of 5,252; G1
  the tie-out).
- **DB-b-25 needs no re-homing.** It was issued to and by the laptop's `2.0.0_SA_COO~P`. Its successor lane on dell2 re-ran the
  instance VALID and flipped it `complete` (@8ef3439f7b). No order of IRPT_DASHBD is open, and no `wk-IRPT_DASHBD*` branch exists.
  `~P` closed its session without a drain-end packet; `~D2` wrote one.
- **The laptop holds six untracked JSON files** under `deliverables/0.9.0_WK_IRPT_DASHBD~7/` and `~8/` (inventory @83d5e34919). They
  are not on origin and no outcome reads them. They are an item for the laptop's fabric manager, not for round 18.

## 2. W12-S1 -- RULED (the comparison basis of the E2 tie-out)

Evidence: `deliverables/0.9.0_WK_IRPT_DASHBD~12/TIEOUT_49F_BD_POPULATION_E2.md`, lines 38-39. BD's request is NetOfFees and the served
series carries no fee. 4,905 of the 6,250 UNEXPLAINED segments land within 0.35 pp once BD's own reported fees are netted. BD's
`daysHeld` is exactly one more than Opal's linked days on 3,395 segments, and all of those contain 2025-01-09, a market closure BD
counts.

**RULING (`1.0.0_SA_CTO~DELL2`):** "The E2 tie-out compares on ONE basis, gross of fees: Opal's served 49F return is gross (fee_basis
GROSS, IB-pr-221), so Black Diamond's net figure is compared after adding back BD's own reported fee for that segment, and the
add-back is printed per segment beside both figures. No FEES reason joins the closed set: a basis difference is not an explanation. A
segment with no BD-reported fee stays UNEXPLAINED. The 1,345 segments left after the add-back, and the 3,395 segments carrying BD's
+1 day over the 2025-01-09 market closure, are the residue the next round reads. The tie-out stays a one-off measurement, never a
standing comparator (CLAUDE.md NEVER shadow/parity comparator)."

**Why the basis moves to gross, not to net.**
- FWD-8 defines the figure as "total return, before advisory fees and labelled so".
- FWD-9 keeps the fee rail "reserved and unused", and "no net-of-fee figure is produced anywhere".
- E2's arithmetic netted the fees from Opal's link. That derived a net-of-fee Opal figure, which FWD-9 forbids even as a comparison
  operand. Adding the fees back onto BD gives the same difference while keeping Opal's figure the one that is served.

**What it does not move.**
- Tolerance stays 0.35 pp: Andrew's word, PRD ruling 25 stands.
- The closed reason set is unchanged.
- PRD ruling 23 (like day sets) is unchanged. It is what makes the 3,395 +1-day segments residue rather than agreement.
- No vendor call: the add-back uses the fees already in the landed pull. A re-pull would need Andrew's per-use word.

## 3. Outcome read (every FWD; denominator 10)

| FWD | state | evidence | next |
|---|---|---|---|
| FWD-1 one 49F account, any window, ~2 s, nobody ran anything | NOT-REALIZED (exercised; grade owed) | STATUS~D live thread: hop 5 ran signed in on the real backend with no fixture, 06:26Z and 08:13Z; tab press to painted chart 5,288 ms; 0 requests on window change | ACCEPT is Andrew's next-morning pick, then the CVO's grade |
| FWD-2 any firm's account, firm-blind | NOT-REALIZED | the Inflection and Cottonwood adapters are not built (backlog B5) | later round |
| FWD-3 asset-class performance and mix | NOT-REALIZED | `account_class_daily` not built (backlog B1) | E3 below |
| FWD-4 gains split and activity summary | NOT-REALIZED | backlog B2 not built | later round |
| FWD-5 transactions browse and export | NOT-REALIZED | backlog B3 not built | later round |
| FWD-6 topic cloud at the trough | NOT-REALIZED | backlog B4 not built | later round |
| FWD-7 household and client | NOT-REALIZED | backlog B6 not built | later round |
| FWD-8 a defensible return, tied out to BD | NOT-REALIZED | E2: 2,103 of 9,078 within 0.35 pp; 6,250 UNEXPLAINED, so ACCEPT's "every day they disagree carries a stated reason" fails | E1, E2 below |
| FWD-9 one Opal shape, one adapter per firm, fee rail unused | NOT-REALIZED (APPLIED for 49F only) | 49F adapter and publisher live (PRD ruling 26 names); two of three adapters absent | rides FWD-2 |
| FWD-10 coverage stated on screen | NOT-REALIZED | "data through" is served (PRD ruling 28, portal 84f2424f); the unmeasured-day and fallback sentences are not graded | later round |

Tally: 0 of 10 REALIZED. FWD-1 and FWD-8 are the two this round moves toward grading.

## 4. Acts only Andrew can do (this project)

- FWD-1 ACCEPT: his pick of an account and two dates on the live page (his sign-in). No new vendor pull is asked.

## 5. The round-18 enrichment list (ONE issuance, `2.0.0_SA_COO~D2`)

| # | item | outcome | risk | criteria (at most three, mechanical) |
|---|---|---|---|---|
| E1 | **Re-grade E2 on the gross basis (W12-S1).** Re-run `tieout_e2.py` over the landed pull with BD's per-segment reported fee added back to BD's net return. Print the add-back beside both figures per segment. The closed reason set is unchanged | FWD-8 | LOCAL (reads; 0 vendor calls) | (1) 9,078 segments graded, each row carrying `bd_fee_addback`; (2) `bd_fee_addback` is null exactly where BD reported no fee, and those rows stay UNEXPLAINED if outside 0.35 pp; (3) no net-of-fee Opal figure is written anywhere |
| E2 | **Read the residue.** The segments still UNEXPLAINED after E1 (about 1,345 expected) and the 3,395 +1-day segments over 2025-01-09: count each against the closed reason set with named evidence, plus the overlap of the two sets | FWD-8 | LOCAL | (1) both counts and their overlap printed with the denominator; (2) each assigned reason cites its row evidence; (3) a reason outside the closed set is filed as a surprise row, not added |
| E3 | **`account_class_daily` and the class contribution** (backlog B1), for 49 Financial, from `etf-classifications` | FWD-3 | SERVED | (1) classes sum to the account's daily return within 1e-9 on every account-day; (2) unclassified holdings are their own class; (3) the six-class vocabulary only (MDPF_SECCLASS ruling) |

E2 is cut after E1 (one chain). E3 runs in parallel, but is cut ONLY once `_shared/etf_classification.py` carries the six-class values (the CTO condition on MDPF_SECCLASS's rule-B remap; control-plane brief section 4). Until then E3 waits and is named as waiting. Fan-out: 2. Workstream F (frontend) items wait on E3's served table and are
not in this issuance.

-- 1.0.0_SA_CTO~DELL2
