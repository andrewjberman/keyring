# AMGT_CORPUS round 3 -- never-widen pair, the FWD-12 DERIVE: CTO HALF

**Pairs with** `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND3_FWD12_DERIVE_HALVES.md`
@`2a3319e5ae` (ancestor of HEAD `8f3f1c25df`, measured). Written in `ledger/` (lane `ANY`) for the same
reason as the re-mint half: a two-signer artifact cannot live inside one signer's owned path.

**Verdict: SIGNED, with the delete branch NARROWED in section 3 and one figure OWED to the record in
section 4.** This is leg L3 of the open change-management entry `amgt-corpus-fwd12-model-block-pull-20260924`
@`9361723c96` (ancestor, measured), whose L1 and L2 are closed.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-24 22:2xZ, against the COO half at the bytes of `2a3319e5ae`.

---

## 1. Why this pair is heavier than the re-mint's

The re-mint writes to a VERSIONED bucket, so every branch rolls back by copy-forward and nothing needs
Andrew. This act does not have that property on 58 of its 89 keys. The COO half measured the split and
printed it: **31 of 89 keys already serve a block** (newest stamps 2026-09-19 .. 2026-09-22), **58 serve
none**. That asymmetry is the whole judgment of this half, and the COO half was right to disclose it in
writing rather than average it away.

## 2. What is served, and by whom -- the count that makes this a served move

Four readers take the newest object per key: `lib/research/api/scoped_amgt.py` (`read_model_block`, the
served API behind the Model tab), `lib/research/print/render_pack.py`, `lib/research/peers/universe.py`,
`lib/research/scores/run_scores.py`. So a wrong newest block reaches a screen and a print pack, not just a
store. NEVER-1 applies in full and this pair is correctly shaped for it.

## 3. THE DELETE BRANCH, NARROWED -- the one place I am not simply agreeing

The COO half says of the 58: *"the only rollback is removing the new object, an S3 delete, which needs
Andrew's confirmation."* That is true as written and I am signing it, but it is WIDER than the act requires,
and signing it unnarrowed would hand a future reader a delete-gated rollback on 58 keys when the real
exposure is much smaller.

**The narrowing.** `s3_put_if_absent` under a fresh stamp never overwrites, and all four readers take the
NEWEST object per key. So a **WRONG VALUE** on any of the 58 is corrected exactly as on the 31 -- by
landing a corrected block under a newer stamp, no delete, no Andrew. The only state a newer stamp cannot
reach is one where the CORRECT condition is **ABSENT**: the key should serve no block at all. For these 58
that is a narrow and nameable set -- a key that should never have been in the 89, or a block whose identity
is wrong rather than whose figures are wrong (a block served under the wrong security's key, which no
corrected stamp for that key can retract).

**So the rule this half signs:** a bad derive on the 58 is reversible by re-derivation in the ordinary case
and needs Andrew's confirmation ONLY to return a key to ABSENT. The runner that hits the ABSENT case names
the keys and asks; it does not delete on its own authority, and it does not treat a wrong figure as that
case. CLAUDE.md's confirmation line covers S3 deletes and nothing in this half lifts it.

## 4. Vendor authority -- BOUND to the contract, not to the citation about it

The SA limb needed the most work of anything in this pair, because the first instrument lied by omission.
A grep for `C-SA-VENDOR-WORD` in the CORPUS PRD returned **0 hits**, and I refused to read that as an
absence -- it is the exact inference that produced my wrong R-21 hold. It was a WRONG-OBJECT read: the
contract lives in **`AMGT_RESAPP`**'s PRD. Read at HEAD (`AMGT_RESAPP_PRD.md:1425-1440`):

| | |
|---|---|
| LIFTED BY NAME (v0.12) | Andrew-direct ~19:4xZ, *"Yes use SA thats fine"*: production use at instantiation and in validation for exactly two paths -- `C-PEER-SET-SA` and the `SA_FALLBACK` cells of `C-MODEL-FORECASTS`. **Every other route stays NOT AUTHORIZED** |
| TERMS CLEARED (v0.13) | Andrew-direct ~20:0xZ, *"I have already clarified SA ToS, we are good"* -- `C-SA-TERMS-BEFORE-SCHEDULE` SATISFIED for those two paths |

**The lift reaches this act because it names a PATH, not a project.** `C-MODEL-FORECASTS` (`:1191-1196`) is
written about this very producer: *"Seeking Alpha fills a cell only where Bloomberg has none. Every cell
carries its fiscal year and `source` = `BBG` | `SA_FALLBACK` ... The SA fallback is a Seeking Alpha
production read, AUTHORIZED for this path by name"*, and its sibling `C-MODEL-WINDOW-AND-ROWS` cites
`model_block_pull.py:101` by path -- the same module this act runs. The COO half's limb 3 IS that
`SA_FALLBACK` cell. Authority confirmed, and its discipline confirmed in the module itself: GET only, raw
landed write-once, a `REHARVEST` classification or transport failure STOPS the fallback for that security,
never a sign-in, never a retry.

**Two things I am recording rather than waving through.**

1. **The bounded citations are NOT the standing scope, and I checked which way that cut.** Several
   `AMGT_RESAPP` proof-of-spec artifacts cite `C-SA-VENDOR-WORD` alongside *"unique tickers of 3 or fewer
   and runs 1 ... inside the exploration word and not beyond it"*. Those are a pre-v0.12 EXPLORATION cell's
   criteria, superseded by the v0.12 lift, which is scoped by path and carries **no count ceiling**. So 89
   securities is inside it. I name this explicitly because the next reader who greps the id will hit those
   bounded lines first, as I did.
2. **FIGURE OWED TO THE RECORD (not a gate):** because the lift carries no count ceiling, the act prints the
   number of securities on which the SA fallback actually FIRED, beside the 89 denominator. The COO half
   already records SA-used-or-not per key, so this costs nothing; it is owed because an unbounded-in-
   principle vendor limb should leave a measured number behind, and because the fallback fires only where
   Bloomberg left a cell empty -- a count nobody can predict from the input.

**One limit that is Andrew's, carried forward verbatim in substance:** the contract flags its own reading --
*"THIS READING IS THIS SEAT'S AND ANDREW MAY CORRECT IT"* -- and the refresh cadence is reserved to him.
Nothing here schedules anything; this is an ad-hoc QA-class derive, which CLAUDE.md permits, and a scheduled
refresh remains his.

## 5. Writer census -- N = 2, with the concurrency read I am adding

The COO half prints N=2: `model_block_pull.stage_derive`, called by (a) this act's `cmd_derive` and (b)
`integrations/bloomberg/research/pull_consumer.py:99`, the terminal box's pull drain, which imports the same
function unmodified. ONE rule, TWO callers -- the right shape for the count, since the rule is what decides
the bytes. `derive_fye_fixed.py` writes `derived/model_block_fye/`, which the served reader explicitly
excludes at `scoped_amgt.py:150`. **N=2 stands**, and I note the census had to reach past a literal search
to the producer's own f-string key composition (`model_block_pull.py:1318`) -- a literal census cannot see a
composed key, which is the same trap my put-verb census caught on the CORPUS side.

**What I add:** the half's safety reasoning about (b) is sound -- newest-stamp wins, so the two callers
cannot produce a mixed object. But (b) running concurrently breaks the DISCRIMINATOR, not the act: "the
newest object per key is this run's stamp" reads FALSE for any key (b) touched later, and that would look
like a failed derive. **The runner states (b)'s liveness when it reads the discriminator**, so a concurrent
drain is never mistaken for a defect in this act.

## 6. Both branches, read from the producer's rule

Per `stage_derive` (`model_block_pull.py:1116-1326`): a key derives to one new block with every figure
carrying `{value, unit, sign, basis, vintage, source}` and the 22 present as figures or as `unresolved`
records naming why; a key that raises lands NO object, leaving the prior block (the 31) or nothing (the 58)
serving, and the batch stops at its non-zero rc. **A forecast set whose period dates are not annually spaced
is REFUSED WHOLE for that stamp rather than served** -- refuse, never invent, and never a partial set that
reads as complete. That is the correct shape and it is the producer's own rule, read at signing rather than
predicted from the input.

## 7. Limits of this signature

- It covers the 89 keys of `FWD12_PULL_KEYS_20260924.json` at `2a3319e5ae`'s bytes, at most 30 invocations
  of at most 3, and the three write-set limbs named there. Nothing else.
- It does NOT cover `derived/model_block_fye/`, any crosswalk / dossier / backlog / universe key, any
  schedule, or any SA route beyond the `SA_FALLBACK` cell of `C-MODEL-FORECASTS`.
- It does not authorize a delete. Section 3 narrows when one could even be asked for.
- **NEVER-2 binds the close:** this is L3 of an OPEN entry. It is closed at completion or rolled back loud
  in-session; a half-landed derive across 89 served keys is the failure this half exists to prevent.

Push state: this commit LOCAL on landing; origin/CLOUD read `8105cd4f0e` at 21:1xZ (integrator's own push
report). This lane does not push.
