# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 46, AMGT-uu-4 (the redeploy)

`1.0.0_SA_CTO~Z`, 2026-09-28 ~23:1xZ. **SIGNED.** Pairs with the COO half
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/NEVER_WIDEN_HALF_COO_UU4.md` @`7b7bf280ac`.
Order: `task-orders/AMGT_RESAPP.TO-AMGT-uu-4.the-redeploy.md`. Authority for the change of rule: Andrew-direct
~21:3xZ, Base case ADJUSTED EPS x ADJUSTED P/E (record @`c027b4726f`).

## 1. THE RULE I READ, AT HEAD, ON THE RECORD PLANE

`lib/research/api/case_rule.py` `compute_cases` (`:147-256`), read with `git show HEAD:<path>`; landed @`b56fef3032`.
It is a pure function of the stored block's figures and its two currency codes. **SEVEN branches, MECE and TOTAL, in
evaluation order:**

| # | condition | outcome | line |
|---|---|---|---|
| 1 | no `forecast` BEST_EPS FY1 figure | ABSENT "no consensus EPS" | `:162-163` |
| 2 | no closed year < FY1 with both PX_LAST and IS_COMP_EPS_ADJUSTED > 0 | ABSENT "no adjusted P/E history" | `:168-172` |
| 3 | FY1 EPS not a positive number | ABSENT `forward_eps_not_positive` | `:202-206` |
| 4 | no header PX_LAST | ABSENT `no_price` | `:208-212` |
| 5 | quote != reporting currency and not a minor-unit pair | ABSENT `currency_mismatch` | `:215-220` |
| 6 | base / px_last outside [0.33, 3.0] | ABSENT `outside_band`, ratio and operands carried | `:224-240` |
| 7 | otherwise | SERVED, adjusted formula, both inputs with `basis` | `:241-251` |

Upside and Downside are the ruled ABSENT object on every branch (`:104`, `:256`); the served adapter
`scoped_amgt._model_cases` (`:2972-3008`) re-imposes them regardless of the block.

**Writers of the moved properties: N = 2, the same two the COO half names.** The served Base case has one writer,
`_model_cases` -> `compute_cases`; the rich export's case line has one, `render_pack._model_case_line`. The pdf path
(`build_pack`) calls neither.

## 2. THE EXPECTED OUTCOME -- MEASURED BY THIS SEAT, NOT ADOPTED

I ran the landed adapter AND the pre-uu-3 adapter (`scoped_amgt.py` @`78f11f5a02`, `git show`) over every live-library
name's STORED block (95 folders, read 23:11:16Z, 0 no-identity, 0 no-block):

| transition | count | matches COO half |
|---|---|---|
| SERVED -> SERVED | 48 | yes |
| ABSENT -> SERVED (**the widening**) | 22 -- the same 22 names, byte for byte | yes |
| ABSENT -> ABSENT | 25 (currency_mismatch 17, no adjusted history 3, outside_band 2, EPS not positive 1, no price 1, no consensus EPS 1) | yes |
| SERVED -> ABSENT | **0** | yes |

Samples: AMD 652.73 -> 415.64 (ratio 0.659), GOOGL 537.70 -> 511.61 (1.488), RKT 7386.64 -> 5941.78 GBp (1.207). All
70 after-SERVED cases carry a `consensus_eps.basis` object. **AC3's M = 70 is therefore the expected value.**

**The widening is signed as named.** The 22 are the direct consequence of Andrew's ruling: 19 had no GAAP P/E rows and
now have an adjusted history; 3 (GPN, NFLX, NOW) fall inside the unchanged band on the adjusted basis. Each passes the
same refusals as the 48. No name loses a served value.

## 3. THE BLAST RADIUS I SIGN

Exactly the COO half's acts A and B, its rollbacks (the recorded prior VersionId; a copy, never a delete), and its five
stop limbs, unchanged. Nothing re-lands a stored block; no S3 write beyond the one artifact.

## 4. BOUND, STATED -- the EPS side of "adjusted" is a LABEL, not a measurement

The served `consensus_eps.basis` for BEST_EPS reads `{"mnemonic": "BEST_EPS", "definition": "Bloomberg consensus (BEST)
estimate of earnings per share for the overridden fiscal period."}` (AMD, V). It does not say adjusted. The
`trailing_median_pe.basis` does (`PX_LAST / IS_COMP_EPS_ADJUSTED`). The served `formula` string calls the EPS "adjusted
consensus EPS", which rests on the CVO's round-45 INFERENCE from magnitude (`ADJUDICATION_v55`), not on a vendor field.
**This does not change the blast radius, so it does not withhold the signature.** It is the round's JUDGMENT to see
(round-45 analysis s.2 item 3), and confirming BEST_EPS's basis needs a vendor read that rides the next authorised
Bloomberg use; no new ask here.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-28.

## RE-SIGN ON AMENDMENT 1 (2026-09-29 ~00:5xZ) -- the combined deploy with AMGT_HARVST `TO-HVST-a-2`

**SIGNED AGAIN**, against the COO half's AMENDMENT 1 @`658475977c`, on this seat's decision msg 26319 (one combined act
under both pairs; it fires only when all four halves are committed).

**What I measured for the amendment:** `git diff f3de463222 HEAD` (the DEPLOYED `scoped_amgt.py` baseline the amendment
corrects to) over the five closure members: `case_rule.py` +256 (new), `scoped_amgt.py` +175, `render_pack.py`,
`timeline_api.py` +395 (new), `publication_gold.py`. In `scoped_amgt.py` the hunks sit in exactly four places:
`_model_cases` (the case rule this half already signed), the `HVST-z-0` timeline section after `_body` (loaders reading
through the producer's own newest-snapshot reader, READ-ONLY), one GET branch in `handler`, and `scoped_amgt_route_table`
growing 16 -> 18 by `TIMELINE_ROUTES`. The handler branch fires only when `_timeline_split` matches a path ending
`timeline` or `timeline/day/<date>`, so **none of the 16 existing routes is re-routed**; their outputs move only in the
case fields section 2 names. RESAPP's expected outcome is unchanged: 48 / 22 / 25 / 0, AC3 70 of 70.

**The radius this half now signs:** the COO half's acts A and B for the COMBINED build, its amended limbs 1 and 3 (what
a-2's pair names is admitted; a closure file NEITHER pair names is still a STOP), and nothing a-2's pair does not sign
for its own change set. The HARVST change set's own blast radius is a-2's pair's to sign, not this half's.

Re-signed: `1.0.0_SA_CTO~Z`, 2026-09-29.

**Extension (2026-09-29 ~01:0xZ), same re-sign:** (1) the `scoped_amgt_route_table()` change (16 -> 18, `HVST-a-1`
@`180989c8a8`) measured above is admitted by this half; `2.0.0_SA_COO~Z`'s limb 3 must name it too. (2) The combined act
ROLLS BACK AS ONE: a failure on either project's criteria re-points the function to `0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS` and
reverts HARVST's route and grant edits in the same `safe-apply` (the a-2 CTO half, this commit).

**Re-signed on AMENDMENTS 1 AND 2 together** (COO half @`658475977c` + @`e21c04c433`, 2026-09-29 ~01:0xZ): AMENDMENT 2's limb 3
list is the same set of `scoped_amgt.py` hunks this half measured above. All four halves of the combined act now agree.
