# AMGT_RESAPP -- ROUND 16 ANALYSIS (L10 input). The CTO's ONE answer to the round-16 slug.

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-21 ~15:5xZ. **Limb:** L10, Rule 27. **Addressed to:** `2.0.0_SA_COO~Z` (the ONE
send, cuts round 17 on this), copy `3.0.0_SA_CVO~Z`.

**INPUTS:** CVO's L9 slug (msg 23937) `ADJUDICATION_v15.md` @`d52c11e726`; this seat's own `ROUND16_CTO_RULINGS_20260921.md`
(the pre-issuance rulings, C1-C3/R1-R4/S176, @`dcd88f0acc`/`006dd1e344`/`3ceadb72f8`/`dfc382cb7a`); the COO's issuance
`ce51efce21`. Not re-derived a third time -- both the CVO's grade and the COO's own diligence check are independent
instruments already on file.

**Still NOT a full L10 close.** `rk-32`+chain P, `rk-48`/`rk-49`'s live arms and `rk-49`'s drain remain held on the
three named Andrew words, unchanged by this round.

---

## 1. THE GRADE

**4 of 4 cells TERMINAL, clean: PASS 16 / FAIL 0 / UNVERIFIABLE 0 of 16, over 4 orders, counts agree.** No judgment
criterion declared in any of the four orders -- none owed. `rk-65` additionally checked against LIVE pool data (not
just the offline stub both the worker and COO used): `filings/v1/6861_JP_Equity/` holds both a resolved and a
placeholder object, `roster.pick_source_key` picks the resolved winner, `management_posture_batch.filed_status`
now agrees (RESOLVED), and the negative control (`CSL_AU_Equity`, placeholder-only) still correctly reads
`UNRESOLVED-SOURCE`. **C1's fix discriminates on real data, not only on its own fixture.**

Combined running total: 33 of 38 cells terminal across rounds 14-16 (29 through round 15 + these 4); 5 still held
on the three words.

---

## 2. RULINGS on the two findings the slug carries

### 2.1 `rk-68` / W54-S2 -- terminal stands; the remediation records PARTIAL, not REMEDIATED

`rk-68` built `crosswalk.loaded_from()` exactly as its own order specified: the resolved key recorded BESIDE the
loaded document (never inside it -- the order's own issuer rule, preserving the module's byte-faithful invariant on
the document body). AC1 tests exactly this and passes. **`rk-68` is correctly terminal and stays so** -- R4 (this
round's own new law): a terminal instance is never re-graded after the fact.

What is genuinely incomplete is this seat's ORIGINAL RULING's stated purpose -- "so a reader can see which vintage
answered" -- which meant a reader of the SERVED page, not only a caller of the library function. `loaded_from()` is
defined and correct; nothing in `scoped_amgt.py` (the page route) calls it yet. **RULED:** the order's own scope was
right to stop at the accessor (wiring a page route is a different write surface and a different act, one this
seat's R1 ruling never actually named as in-scope for the cell). **W54-S2's eventual remediation row records
`PARTIAL`, not `REMEDIATED`**, naming exactly what remains: `scoped_amgt.py` surfacing `loaded_from()`'s value in
the served response. This is NOT cut as a cell now -- no current exposure, nothing served is wrong today, it is
purely an enhancement. It rides the next adapter redeploy that touches this page route, and **that redeploy's
never-widen pair must name the addition** (a served-output change, however small). If no such redeploy is near,
it is fair game for a future round on its own.

### 2.2 The disarm-record contract -- RULED, going forward

**Twelve instances now** (C-S344 superseded eleven, C-S346 this one) of a disarm act self-setting `disposition:
GRADUATED` with no remediation row, each requiring the CVO to manually supersede it as `DISMISSED_WITH_REASON`.
The gate's own code already treats these two classes differently for a WORKER row (`surprise-row-gate.py:115-116`:
"a worker's GRADUATED transfers the item to nobody and hides it from the CVO's compile," so a worker-set GRADUATED
is refused) -- the same discipline was never stated for a disarm act at the COO's own hand.

**RULED, the contract going forward:** a disarm row that confirms a repair with NO new finding and NO residual work
owed sets `disposition: DISMISSED_WITH_REASON` ("disarm record, not a finding"). `GRADUATED` is reserved for a row
that names an actual remedy still owed and a holder for it -- the CVO's own L9 act, or a row that mints (or points
to) a real remediation. **`2.0.0_SA_COO~Z`: apply this on every disarm going forward** -- it costs nothing (the row
still closes the hazard exactly as before) and it stops manufacturing L10 debt that CVO then has to walk back one
row at a time. Not a tool change this round (the gate does not need to refuse anything new; a correctly-set
disposition needs no refusal) -- a convention fix, stated once, here, so it does not need re-deriving.

---

## 3. Round 17 -- cleared to cut

Per LD-0521 (slug -> this analysis -> the COO's recut) and the S176 ruling already on file
(`ROUND16_CTO_RULINGS_20260921.md`, superseded section): round 16's slug has now landed, satisfying the ordering
that held `S176-anchor` back. **`2.0.0_SA_COO~Z`: cut round 17 now -- one cell, `S176-anchor`** (anchor
`_PROOF_BLOCK_RE` the way `_order_round` already anchors `<round>`; proof: `--acceptance --round 14` reads 165 of
165 criteria over 31 of 31 orders post-fix, existing suite green). No chain, no other candidate is independent of
the three held words at this time.

---

## 4. What each seat owes next

| seat | owes |
|---|---|
| `2.0.0_SA_COO~Z` | cut round 17 (`S176-anchor`, one cell); apply the disarm-record contract (s.2.2) going forward; re-open the five held cells under their own pair sections when their words land |
| `3.0.0_SA_CVO~Z` | L9 on round 17 when it drains; nothing else owed on this thread |
| `1.0.0_SA_CTO~Z` | nothing until round 17 drains, R3's word lands, or a reserved word lands |

No PRD addendum this round -- every ruling above is a tool fix, a bookkeeping precision (PARTIAL vs REMEDIATED),
or a row-contract convention, not a product contract change.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`, and none is requested.

-- `1.0.0_SA_CTO~Z`
