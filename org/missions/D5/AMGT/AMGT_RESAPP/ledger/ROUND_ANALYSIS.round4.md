# AMGT_RESAPP -- ROUND 4 ANALYSIS (L10, `1.0.0_SA_CTO~Z`) -- the round that closed round 3's one FAIL

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**

**Slug graded:** `surprise-channel/remediations/REMEDIATION_v4.md`@`b97837e7fe`, the single round-4 L10
slug from `3.0.0_SA_CVO~Z`. Source/review pin `79ec889666`. Adjudications at the same pin; independent
CVO measurements in `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND4_CVO_EVIDENCE_20260911_Z.json`;
closure clocks @`6bae1cc480`.

---

## 1. THE VERDICT: 2 PASS / 0 FAIL -- and round 3's single FAIL is now CLOSED

Both judgment criteria pass, graded at L9 by the CVO and never self-graded by the executing seat:

| criterion | verdict | what it actually establishes |
|---|---|---|
| `rc-19` AC4 | **PASS** | the shared unresolved-row refusal contract holds THROUGH THE ACTUAL CONSUMER and the scratch PDF -- not at the rule in isolation |
| `rc-20` AC4 | **PASS** | observation date, original vintage and derivation identity are DISTINCT, with a control varying only the key |

⭐ **THE ROUND'S REAL RESULT IS `C-S16`.** Round 3's one FAIL was the consumer-wiring: the corrected
fiscal price did not flow end-to-end to the served consumer, and round 3 recorded that it "FAILED for
the right reason" -- the generalization working rather than a regression. **Round 4 closes it.**
`C-S16`, with its children `C-S19` and `C-S20`, now carries DISARMED / REMEDIATED / closed clocks, and
the original mechanisms and historical grade evidence remain intact rather than being overwritten.

⛔ **WHAT CLOSING `C-S16` DOES NOT CLAIM, quoted from the slug rather than softened:** it does not claim
historical PDFs were regenerated, that an analyst has exercised a deployed UI, or that any FWD outcome
is REALIZED. It claims the named fiscal consumer was exercised with corrected persisted data, with full
join-to-consumer unresolved propagation and distinct derivation identity. **That is a correctness
closure, not a surface one.**

**Row `W1-S6` is dismissed by `C-S21`:** the worker corrected a stale test inside its granted path
without changing the issued acceptance bar. That is the correct disposition -- a worker repairing its
own fixture is not a spec change, and dismissing it is not waving it through: `C-S22` records the two
judgments beside it.

**Coverage, with denominators printed:** 28 of 28 orders terminal, 0 open. 28 proof instances
structurally VALID under the checker's DECLARED coverage limits. 39 of 39 regression tests pass. The L8
census found 30 investigations across both roots; the final census is 31 with `S5`.

---

## 2. NO FWD IS NEWLY REALIZED, AND THAT IS THE CORRECT OUTCOME

**0 of 15 FWD outcomes newly REALIZED. Unchanged from round 3.** Rounds 1-4 have all been pre-surface
correctness work and **no surface is built**, so there is nothing for an analyst or a PM to exercise.

This is the bar the PRD's own ENDPOINT section states and it is worth restating at every L10 because it
is the easiest thing in this project to get wrong: **14 of 15 outcomes carry `EXERCISED`** and only
`FWD-9` carries `APPLIED`. Fourteen outcomes CANNOT be closed by any build. **No cell may claim an
`EXERCISED` outcome REALIZED on the strength of its own artifact** -- the sibling project on this fabric
graded eight outcomes REALIZED against an artifact that had never run once. **Grade the `DONE WHEN`
state line, never the `ACCEPT` paragraph beside it.**

The completion test is therefore nowhere near met, and the round does not pretend otherwise.

---

## 3. TWO ROWS SURFACED THIS ROUND, BOTH STILL OPEN

**`AMGT_RESAPP-Z-S5`** (surfaced `2.0.0_SA_COO~ZZZ`, graduated by `C-S23`) -- the PRD carried an
obsolete bucket-absence premise. `opal-data-research` EXISTS. Measured twice on two instruments with a
negative control: CVO at 15:44Z and this seat independently at 15:55Z, both `head-bucket` rc=0,
`arn:aws:s3:::opal-data-research`, `us-east-1`, against a 404 for a nonexistent name.
- **CTO half DISCHARGED @`3e35a50e74`:** s.5 now records the bucket as MEASURED PRESENT with its
  vintage; the S6 manifest row's measured-by no longer cites ABSENT. The brief's PART V measurement is
  preserved as SUPERSEDED, **not rewritten** -- a historical measurement edited to match today destroys
  the evidence that the world moved. The bullet is struck and marked RESOLVED rather than deleted, so
  the record that it was ever a blocker survives.
- **COO half OPEN, `2.0.0_SA_COO~ZZZ`:** re-read live identity AND CONFIGURATION at the next S6 cut and
  state existing-resource integration. ⛔ **EXISTENCE IS NOT ACCESS.** `head-bucket` proves the name
  resolves -- not permission, policy, versioning, encryption or lifecycle.

**`AMGT_RESAPP-Z-S6`** (surfaced `1.0.0_SA_CTO~Z` @`65ab345826`, OBSERVATION, hazard ARMED,
`disarm_owner` `4.0.0_SA_CRO~Z`) -- **the L4-R gate reports a half SIGNED/current when its sign-off
record carries no `half_hash`**, because currency then falls back to `prd_version` equality. Measured
live: this project's brief half moved `a5517057d99f` -> `1cb017c3e490` and
`prd-signoff.py status` kept printing "brief SIGNED current". The discriminator is in the same command
run -- the CVO's new-format record carries a `half_hash` and correctly reads STALE. A false green on a
gate, in the exact direction spine v3.15 exists to prevent. Disarms when `4.0.0_SA_CRO~Z` re-signs
through the current tool, which writes a hash-bearing record. The general fix is routed to the spine
owner and deliberately NOT started: changing that predicate retroactively invalidates every old-format
signature in the estate, and nobody has counted that denominator.

---

## 4. ROUTING -- round 5 IS THE SURFACE ROUND, AND IT IS GATED

**Round 5 (`2.0.0_SA_COO~ZZZ`, ONE issuance, via `/atom-decomp` on the v0.4 surface manifest):** the
two tables (`opal-amgt-articles`, `opal-amgt-security-metrics`) FIRST, then the harvester EC2 box with
its own IAM role, then the `.tsx` shell. `infra/aws/terraform/amgt-resapp` not existing yet is CORRECT
SEQUENCING, not a gap.

⛔ **THE ROUND MAY NOT BE CUT UNTIL BOTH L4-R HALVES ARE SIGNED AT CURRENT BYTES.** State at write:
- `ratified-text` -- REFUSED @`079e7d0a3b`, corrected bytes returned @`421489a8d5`
  (half `4eb997ed71ee`), delta review open at `3.0.0_SA_CVO~Z`.
- `brief` -- genuinely OWED by `4.0.0_SA_CRO~Z` at half `1cb017c3e490`, **notwithstanding what the gate
  prints** (row `S6`).
`.tools/to-pipeline-gate.py` LIMB 6 is the mechanical neck, and `S6` is precisely the reason it cannot
be the only check on the brief half this round.

**Carried forward unchanged:** the vendor word stays NARROW (Seeking Alpha / FT / Bloomberg / WSJ, this
project's harvesters only, effective when the harvester box is stood up -- not before);
`C-NO-CONTACT` stands, NO SEAT CONTACTS ADAM MULLER; Andrew's approved design and harvester scope are
carried by the v0.4 ratification and are **not enlarged** by this round.

**Round 4 CVO stamps:** L8/L9/L10.r4. **Round 4 is CLOSED at L10.** The project is NOT closed -- it
closes when every FWD grades REALIZED, which requires a surface that does not yet exist.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes origin/SITEZ; this seat does not push.
