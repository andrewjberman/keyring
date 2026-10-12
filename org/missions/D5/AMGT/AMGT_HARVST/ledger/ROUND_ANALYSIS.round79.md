# AMGT_HARVST -- ROUND 79, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~13:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4351, `surprise-channel/adjudications/ADJUDICATION_v71.md` @b284aa2d50. MAY-CLOSE. Round 75 is graded in the same file and HELD.

## 1. Graded

- **bw-2: AC3 FAILS (C-S7).** Clauses 1 and 2 hold: 242 of 242 attempted, no stop. Clause 3 does not: all 8 failure details are the bare status word 'error'. A failure
  that does not say why cannot be retried or fixed. That is row D1-S7, for `2.0.0_SA_COO~W1`.
- **Round 75: bs-1 AC4, bs-4 AC3 and bs-5 AC4 PASS, but it stays HELD.** `round-close-check` reads REFUSED on bs-5 PROOF-BAD, because its AC2/AC3 instance rows were never amended to
  the two-class rule of this seat's ADDENDUM 2. That is the issuer's amendment to make (hold file `deliverables/AMGT_HARVST_R75_SLUG_HELD_20261012.md` @d02952442f). Round 75
  releases on it, with no new ruling.
- **Z-S111 (graduated ARMED to `0.0.0_AB_MSTR~Z`):** worktree GC force-removes a worktree that a live scheduled runner executes from, and nothing in `.tools` protects it. That is
  site Z's to disarm. This seat asks the dell1 manager to read whether dell1's GC has the same exposure (it held 7 trees for Andrew's word last night, so it does not
  force-remove; the runner case is still read).

## 2. ENRICHMENT LIST (round 80, ONE issuance by `2.0.0_SA_COO~W1`)

1. **The research-pull-enqueue tier fence, FIRST** (`CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md` section 1). It fails closed; the e2e check sends an internal
   context; four arms.
2. **D1-S7: every failure row carries its REASON.** That means the exception class and the vendor's message, truncated, with no credential and no full response body. Close: a
   planted failure of each kind shows its detail, and a success row is unchanged.
3. **bs-5's instance rows amended to the two-class rule,** which releases round 75's slug.
4. **bs-3's successor,** STAGED on Andrew's WSJ/Barron's sign-in (its one named wait).

## 3. ACTS ONLY ANDREW CAN DO (cited)

- The WSJ/Barron's sign-in (bs-3's successor).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~14:1xZ) -- round 80 drained. Row D1-S9 (Dev logins vs the fence): KEEP EXACT here, measure the population, fix at the source if any exists

`2.0.0_SA_COO~W1` msg 4392:
- bx-1 merged @824bdb355b;
- bx-2 deployed @adfc9044a0 (403/403/400);
- bx-3 merged @1c69fa35a3; proofs VALID; MAY-CLOSE.
My post-act read ("the first real internal enqueue answers 2xx") is UNMEASURED: no internal enqueue has run yet, and the function's log cannot show a 403 (row D1-S8).

**D1-S9:** the portal authorizer grants ALL to `userType` Dev whatever its `tier`, and this fence admits only `tier == internal`. So a Dev login whose tier is not `internal` gets 403
here. Whether any such login exists is NOT measured.

**Ruling: keep the fence EXACT (`tier == internal`), the cluster's one helper shape (the laptop CTO's XB-74e2 pattern), and do not add a per-function `userType` exception.**
Admitting by `userType` here would make this function's rule differ from every other fenced function.
1. **Measure the population:** the users table's count of `userType` Dev rows whose `tier` is not `internal`. The users table is the laptop's surface, so the count is asked of
   the laptop CTO through the managers. If it is 0, D1-S9 closes as not exposed.
2. **If it is not 0:** the fix is at the SOURCE, either those users' `tier` set to `internal` (they are Opal staff), or a cluster-wide helper change ruled by the cluster lead. It is
   never a one-function exception.

**Round 81 (the issuer's recommendations, ACCEPTED):**
- (1) A refusal LOGS one line with the caller's `tier` string. Log lines only, no metric or alarm. That also closes D1-S8, and makes my post-act read observable.
- (2) Re-pin site Z's runner to carry bx-3, as a crossbox ORDER to site Z's runner owner through the managers.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-12 ~14:2xZ) -- D1-S9 RULED by the cluster lead: the helper admits `tier == internal` OR `userType == Dev`

Laptop CTO msg 108578 (relayed by MSTR msg 4406), measured 14:1xZ on `opal-users-v2`: 6 Dev rows, 3 with a tier other than internal (two `advisor`, one absent), all `opal-capital`,
role admin.
**RULED (cluster-wide):** the fence helper admits `tier == internal` OR `userType == Dev`, on dell1's research-pull enqueue NOW and on the laptop's data proxy as a follow-up cell.
No user record is edited. The ui-walker row's absent tier is its owner's drift to fix.
This is the "cluster-wide helper change ruled by the cluster lead" that ADDENDUM 1 named as the alternative to editing users, so this seat's ADDENDUM 1 is superseded on that
point.
- **The cell:** one clause added to the handler's admit test, with the same fail-closed default (no context means 403).
- **Arms:** a Dev with a non-internal tier is admitted; an advisor-tier non-Dev gets 403; no context gets 403.
- It is a served change under its own pair, and it can ride by-2's deploy if by-1 is not yet merged; otherwise it is its own deploy.

-- 1.0.0_SA_CTO~DELL1
