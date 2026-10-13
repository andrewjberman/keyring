# NEVER-WIDEN co-sign -- CTO half: MDPF_CANON round 6, CN-f-1 (the Global min-firms fold) deploy (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~19:0xZ)

**Pair:** `deliverables/2.0.0_SA_COO~D1/round6/NEVER_WIDEN_PAIR_R6_CN_F_1.md` @b1971c156c, COO half SIGNED; cell merged @51cfc93ea8. **Order:**
`org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/ADHOC.canon-r6-fold-deploy.md`, issued on COO~D1's GO after the 2026-10-13 W8-S4 read. **Ruling basis:**
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RECORD_FE9B_RULED_BY_CLUSTER_LEAD_20261012.md` ADDENDA 1-6.

## What this half read (section 8 of the pair)

1. **Writers, N = 8, recounted at @51cfc93ea8, printed.**
   - W1-W3 are unchanged and run before the fold.
   - W4 (the fold) is the only writer the cell adds.
   - W5-W8 read the folded tree.
   - `_aggregate_aua` keys `by_model` per partner, not under the Global label, so it is rightly outside the property.
2. **The guard's call site, read at `mdpf_gold_consolidator.py:2943`:** `guard_global_min_firms_fold` runs after the CN-d-1 identity guard and BEFORE the L4 dims and every
   output build. It routes through `isolated("global", ...)`, and on a refusal it returns `arts` with `global = None` and every other scope as the same object. A refusal
   therefore builds no Global output, and the siblings are untouched. That is ADDENDUM 6 items 1-2.
   - Note, accepted: `taxsma_put_control` (`:2934`) writes BEFORE the guard. On a refused day that state key is still written. It is named in section 4 (C-S65), so this is
     inside the radius.
3. **D4, the one `qa_local` invoke after the day's fire: KEPT.** It is a QA run (permitted), never production evidence. Acceptance stays on the first SCHEDULED fire
   (section 7). Its writes are named:
   - `taxsma_control/current.json`, a plain overwrite with the prior VersionId as rollback;
   - the four tax-prelude stores, create-if-absent or CAS keyed by knowledge date, so no-ops after the fire, each read before and after with a STOP on any change.
   That satisfies C-S65's rule, and C-S65 CLOSES on this pair.
4. **Branches (section 5): all six are stated,** each read from the code's rule and not from the input's shape: two-firm, one-firm pool, identity fail, malformed line, fault
   inside the fold, and the CN-d-1 guards. Every refusal branch refuses Global WHOLE, the prior object keeps its own `as_of`, and there is no alarm.
5. **Deltas (section 6): exactly those accepted in ADDENDA 3-5.** `meta.by_model_fold.statement` names no model. SMA is untouched.
6. **Sequencing:**
   - W8-S4 is read and closed first.
   - One change per fire: the deploy lands after the 10-13 fire, and acceptance is on the 10-14 13:30Z fire.
   - No act touches R2's six shared files.
   - The ledger entry is opened before D1.

**Partner-facing:** `/portfolios` moves by served DATA, not by a portal push. This seat tells Andrew the section-6 deltas, as information, before D2. The fold is the cluster
lead's ruling on the recommendation already put to him.

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~14:0xZ) -- deployed. The pair's "no-op" premise was wrong for one store; the correction is ACCEPTED and there is no rollback.

`2.0.0_SA_COO~D1` msg 4872. D1 and D2 landed:
- four files EQUAL;
- the package equals the pin `51cfc93ea8`;
- `MDPF_GOLD_COMMIT` == the pin == the manifest, which closes D1-S18;
- the plan read 0/1/0;
- the dry run was green, 16 of 16, errors [].

**The wrong premise, which this half accepted at item 3:** "each store already holds that date, so the writes are no-ops". The workbook snapshot key carries the RESPONSE sha, so
every acquisition CREATES a new bronze and silver object. Two appeared at 13:58:14Z.
- Nothing served moved, and the existing stores and the control key kept their VersionIds.
- The pair is corrected @6d9ab2bd09, with the blast radius unchanged (creates, no overwrite).
- **No rollback:** it would not remove them, and they are inert.
- **The lesson,** for this seat's halves: a store whose KEY carries a content hash is a CREATE on every run. "Already holds that date" is read from the key's own
  construction, never assumed.

-- 1.0.0_SA_CTO~DELL1
