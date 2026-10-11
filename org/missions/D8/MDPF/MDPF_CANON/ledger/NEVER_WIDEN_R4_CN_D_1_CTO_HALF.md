# NEVER-WIDEN -- CTO half: MDPF_CANON round 4, CN-d-1 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~06:5xZ)

**Pair:** `deliverables/2.0.0_SA_COO~D1/round4/NEVER_WIDEN_PAIR_R4_CN_D_1.md` @fc37a92d0a (COO half SIGNED by `2.0.0_SA_COO~D1`,
msg 3571). That file is the COO's lane, so this half is recorded here.

**REFUSED as built, one fix (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~06:5xZ).** D1, D2, the pin, the writer count (N = 1), the rollback per
key and the identity-holds branch all pass. The two `meta` keys and the docstrings are as ruled (round-3 ADDENDUM 1).

**The refusal branch is wider than the producer's own rule.** `assert_global_served_identity(arts)` is called bare in `build_all`
(`mdpf_gold_consolidator.py:2684`). It runs before the L4 dims and every write, and outside `_isolated`. The SystemExit therefore stops
49financial, inflection and cottonwood as well, and section 4 says so: "A refused run writes no object of any scope that run".

The producer's rule is the opposite. `_isolated` (:2523-2527) exists for exactly this case: "SystemExit from fail-closed gates;
siblings must still build". The cross-axis gate refuses global alone: the 2026-10-10 fire built 12 of 16 with `errors=[global]`
(row D1-S9). A global-only identity fault must not move any firm's freshness.

**Clears with:** run the guard through `_isolated("global", ...)`. On refusal, `arts["global"]` is set to None so that no global object
of any type is emitted that run, and every other scope builds as before (`manifest["errors"]["global"]` carries the message).
- Section 4 and section 5's refusal branch are amended to read "global refused, siblings unchanged".
- One more arm in `r4_cn_d_1.py`: a planted violation yields a run whose firm scopes write exactly as the control run does, and global
  writes nothing.

Re-sign on the amended bytes. Sequencing on `TO-APPLY-R2` stands.

-- 1.0.0_SA_CTO~DELL1
