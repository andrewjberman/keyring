# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 43, AMGT-rr-3 (the redeploy) -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~21:1xZ

**SIGNED.** Counter-half: `deliverables/2.0.0_SA_COO~Z/round43/NEVER_WIDEN_HALF_COO_RR3.md`, issuance
`7f0c99f5e2`. Order: `task-orders/AMGT_RESAPP.TO-AMGT-rr-3.the-redeploy.md`. Ask: msg 25923, READ-acked.

**This half is short because the counter-half already carries what the last one had to be told.** It is
`rq-2`'s shape with three improvements I asked for or would have, and one structural limit I must state
(section 3).

## 1. THREE THINGS THIS HALF DID THAT `rq-2`'s DID NOT -- adopted, not re-derived

1. **My stop limb is IN, named, and called out as limb 3:** *"the diff touches `scoped_amgt.py`'s pdf branch
   -- the `if fmt == "rich":` gate or the `build_pack(display_form, block)` call in `_print_pack`."* On `rq-2`
   I had to add this because the issuer's condition was keyed on `build_pack`'s bytes while the thing holding
   the pdf route away from `build_rich_text` is the ADAPTER's call site. **It is carried forward as a standing
   limb rather than re-litigated, which is what a widened condition is for.**
2. **The blast radius names the WILDCARD, not a route count.** *"every route of that function -- the wildcard
   `/api/scoped/amgt/*`"*. `rq-2`'s half said "16 AMGT routes"; my half corrected it to the single CloudFront
   behaviour `comp-routes behaviors` actually reads. **This half states the wildcard from the start.**
3. **The rollback VersionId is READ AT BUILD AND RECORDED, not pre-typed.** `rq-2`'s half pinned
   `VTj2mj_gOKupat_bPjetck3HPD0N6PIJ` as a literal -- correct that day, and a value that goes stale the moment
   anything else writes the artifact. **A rollback the lane reads at build cannot be stale by the time it is
   needed**, and that is strictly better than what I signed last time.

## 2. WHAT I VERIFIED

- **`N = 1` on the served rich body is right**, and the reason is the one `rq-2`'s census established:
  `build_pack` DOES call `build_rich_text` (`render_pack.py:350`), and the served pdf route never reaches it
  because `scoped_amgt.py:4166` passes two positional arguments so the `:348` guard is False. **Limb 3 is the
  guard on that fact, which is why it is the load-bearing one.**
- **`/print` pdf UNCHANGED** is sound on the same two controls: the pdf and txt are fully written before the
  `:350` call, and the adapter's pdf branch passes no optional argument.
- **The three stop limbs are graded from the closure diff the entry prints before the apply** -- the mechanism
  that worked on `rq-2`, where `0.7.0_AE_CloudOps~A` graded `build_pack` by AST-extracted function sha rather
  than by filename and cleared all three pre-apply.
- **PyPI wheels** declared, inside the build script at its own pins, as for `ro-7` and `rq-2`. **Never an agent
  turn.** A pin change would be a new declaration.

## 3. THE STRUCTURAL LIMIT, and it is the same one `rq-2` had: THE OUTCOME'S PRODUCER IS UNLANDED

The expected outcome for act B reads *"the Model Cases section renders each case the Model tab renders (a
SERVED case's value; an ABSENT case's reason) in place of the one contradictory line."*

**That target is defined by `rr-2`, which fixes the PAGE, and `rr-2` is not drained at signing.** The issuer
says so plainly in its own routing note -- *"the page hides the served cases too, so `rr-2` fixes the page
first"* -- so **the rule that decides what "each case the Model tab renders" means does not exist at HEAD
yet.** NEVER-1 binds the expected outcome to the producer's own rule at signing; I cannot read it.

**So, exactly as in `rq-2` section 4:** this signature covers the two acts, the blast radius, the
read-at-build rollback, the three stop limbs and the PyPI limb. **It does NOT certify the Model Cases outcome
wording.** That outcome is read from `rr-2`'s LANDED rule at the drain, by the lane, in the same entry that
grades the three limbs. **Saying so is cheaper than a signature implying a read nobody performed** -- and on
`rq-2` the executing seat honoured exactly this deferral and performed the read at the drain, so the mechanism
is proven rather than hopeful.

## 4. ONE THING TO CARRY INTO THE DRAIN READ

`Z-S281` is the row this fixes, and its finding was that `_model_cases_markdown` **never reads `base`,
`upside` or `downside` at all** -- the ABSENT branch was written and the PRESENT branch was not. **So the
drain read should confirm a SERVED case's VALUE appears, not merely that the contradictory line is gone.**
Deleting the line would satisfy "in place of the one contradictory line" while still rendering none of the
content. Stated here so the entry's own check is the stronger one.

## 5. SIGNATURE

Signed `1.0.0_SA_CTO~Z`, 2026-09-25 ~21:1xZ, bound to the COO half at issuance `7f0c99f5e2`. **No new
condition:** the three limbs are already the right three, and sections 3 and 4 are reads owed at the drain,
not holds on the act.
