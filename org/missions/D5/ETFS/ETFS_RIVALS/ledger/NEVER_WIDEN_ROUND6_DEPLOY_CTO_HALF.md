# ETFS_RIVALS round 6 -- deploy never-widen pair, CTO half (five Lambdas at CLOUD eb6e9f04ff, the AI secret, one 10-02 republish, one 09-30 AI fire, the vehicle code from 10-05)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~19:4xZ.
**COO half:** `deliverables/2.0.0_SA_COO~RV/round6/NEVER_WIDEN_HALF_COO_ROUND6_DEPLOY.md`, sha256 18da5233...f643, verified by this seat
on the file in the shared tree (msg 28697). The commit is pending because a peer holds the staged index; this half binds to that
sha256.

## What I read

- **The act, in order:**
  1. a NEVER-2 entry `etfs-rivalfunds-round6`;
  2. secret `rivalfunds/openai-api-key`, created by piping the existing `openai-api-key` value, never printed;
  3. ONE `safe-apply` of a saved plan at the pin, probe 0/6/0: five source hashes, the daily Lambda's AI env, and the daily role
     gaining GetSecretValue on that one ARN plus `research_hypotheses` read -> write;
  4. ONE 2026-10-02 republish (AI stage SKIPPED_EXISTS);
  5. ONE deliberate 2026-09-30 AI fire, ap-1's positive arm, under VEW-2 and CALL 5 (one run per page day);
  6. the vehicle's round-6 Bloomberg request from 2026-10-05.
- **The served delta, measured through the handlers over the served inputs:**
  - 18 page features x 13 funds read 0 decreases, and the AI guard keeps 12 of 12 accounts;
  - every lost table row is the Unclassified bucket;
  - INEQ's unclassified share falls from 59.2% to 22.2%;
  - the census states are counted;
  - page bytes 1,833,427 against the 2,097,152 cap (12.6% headroom).
- **37 of 43 round-6 checks pass at the pin.** The 6 others are Andrew's ~17:0xZ layout word superseding those cells' surface
  (record `ANDREW_DIRECT_20261002_17xxZ_RIVALFUNDS_LAYOUT_WALK_AND_BUILD.md`). Their J1 is graded by `3.0.0_SA_CVO~RV` on the new
  layout, and none is a loss against the served page.
- **Writers:** one seat. The vehicle is the only Bloomberg writer.

## Changes to the COO half (binding)

1. **P5 rollback is a RE-PUT, never an S3 delete.** The prior `rv-publish-1002g` A1, G5 and census objects' bytes are re-put as
   newer revisions, which "newest wins" serves, then one publish-page runs. This is the same rule this seat set for RFW-D01
   (@6507370187). No human-confirmed delete sits in the rollback path.
2. **The secret is a COPY, and it is labelled as one.** `create-secret` carries a description naming its source
   (`openai-api-key`, copied 2026-10-02) and the pending act (a dedicated OpenAI project key; Andrew, OpenAI console). A rotation
   of the source does not reach the copy, so the two must never silently diverge into "which key is live?". Gate 4 stays
   length-only.
3. **P7 is reverted at once if P1 fails.** If the apply does not land, the issuer reverts P7's two vehicle files in CLOUD in the same
   session, not "by 2026-10-05 06:00 ET". A deadline that rests on a person remembering is the half-landed state NEVER-2 forbids.

## Conditions

1. The gates as written: nothing in flight, deployed CodeSha256 equal to the 722f0db291 set, the saved plan reading exactly 0/6/0
   with those hunks, and the secret present with non-zero length.
2. **Post-act reads come from the SERVED state:**
   - CodeSha256 equals the plan's hashes;
   - the 10-02 page republished with `research_hypotheses_run` SKIPPED_EXISTS;
   - the AI guard reads 12 of 12;
   - bytes are printed against the cap;
   - the 09-30 fire's run status, per-fund grades and page are read back and handed to `3.0.0_SA_CVO~RV`.
   A FAIL account is shown, never re-rolled (CALL 5).
3. **Page size:** a publish over the cap must REFUSE loudly, recorded in the manifest with the byte count, and the prior page
   stays. The trend-spark growth is routed to `4.0.0_SA_CRO~RV`.
4. **NEVER-2:** the entry opens before step 3 and closes after the 09-30 read-back.

**CTO HALF: SIGNED** for steps 1-6 at pin CLOUD eb6e9f04ff, blast radius P1-P8, with changes 1-3 binding.
