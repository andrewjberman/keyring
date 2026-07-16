# A4 L4 flip EXECUTED on CTO GO -- DEFAULT_FLOW_SOURCE=monolith serving; tonight's nightly is the exercised read

**archetype:** DEPLOY
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-16 18:48Z -> 18:57Z

Chain, in order: 0.7.0's grant message 184839Z (87f5940a7 / bd-v2.52.0, 22a-verified: APPLIED
get-role-policy + simulate w/ isolated positive control + conditioned ListBucket w/ context;
cross-firm deny cot-scoped-only) -> my flip-plan proposal 185017Z (scheduled-nightly-as-the-
exercised-read; failure mode pre-stated) -> CTO GO 185225Z (grounded on his OWN live
get-role-policy read, not the relay; plan approved in full) -> EXECUTED:

- lib/schwab_flows.py DEFAULT_FLOW_SOURCE 'legacy'->'monolith', GO + grant cited in code
  comment + commit body (-F authored). commit-gate clean; bd suite 5/5.
- **Commit 0b0eb7f0f** (lane author), pushed 40d400330..0b0eb7f0f.
- Deploy: safe-deploy pre-push gate carried the S3 upload atomically (Rule 13); I then
  verified the SERVED artifact independently of the hook's self-report:
  **head-object ETag 851eaf6a8630ca5d1502c7500ab8a0a8 == md5(git show 0b0eb7f0f:...) EXACT.**
- Execution report to CTO 185651Z.

STANDING INTO TONIGHT: rollback lever live (SCHWAB_FLOW_SOURCE=legacy env, no deploy needed;
legacy path in code until the clock runs out); 0.5.0 bridge holding; retirement clock HELD.
MORNING EVIDENCE at CTO's gate (~09:46Z seam, now a QUADRUPLE w/ daily runs + WP7 cycle-1 +
~B's bd49f first-fire): (a) nightly loader line `[monolith]` + partition count; (b)
canonical_nna present for the new date, overlay totals consistent w/ bridge-era pattern;
(c) legacy trn_nna path idle -- reading FOR the degrade-WARN, never assuming its absence.
On CTO acceptance: bridge stands down, /49-schwab-conv retires whole, clock runs out.

Lesson banked (CTO): cite NEVER rules by NAME (the ad-hoc-gold-runs NEVER), not ordinal --
ordinals shift.

## Compiler Tools

commit-gate (1 file, clean); no comp-* search tools this delta -- the window was a
pre-scoped single-file deploy motion off a standing GO, every path already grounded in the
1655-1815Z window's censuses. Deploy verify = live primitives (head-object ETag vs committed
md5), per the L4 pattern.
