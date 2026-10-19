# IRPT_ANLREQ PRD v0.23 -- ratified-text half review: REFUSED (one contradiction in FWD-1; one-line fix)

**Seat:** `3.0.0_SA_CVO~DELL2`, 2026-10-19 ~20:1xZ. **PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` v0.23 @6500db27df
(half_hash `6adc4982a981...`). Asked by `1.0.0_SA_CTO~DELL2` msgs 10950 and 10953.

## What I read

1. **The whole diff, v0.22 @d5b6ba40a1 to v0.23 @6500db27df** (79 lines added, 9 removed): FWD-1, FWD-2, the new FWD-8, C-FIRM,
   C-PACKAGER, surfaces S8-S10 and ADDENDUM v0.23.
2. **Andrew's words**, in the two records the addendum cites:
   - `ANDREW_DIRECT_20261019_165xZ_TCKT_ANALYSIS_REQUEST_FLOW_BREAKS.md`, lines 9-27: "Opal Users should have 0 blocks or authorization gates
     from being able to submit through the ticket center on behalf of any firm"; "no need really to break out the type of analysis in a
     drop down because it is implicit"; the Opal models "surface immediately", with no wait; "The expected deliverables here are the four
     attachments".
   - `ANDREW_DIRECT_20261019_18xxZ_TCKT_NO_ADVISOR_EMAIL_COMMENTARY_DEFAULT_ON.md`, lines 8-10: no email field; "the Add Commentary box is
     unnecessary; investment commentary should be on by default".

## What holds

- **FWD-1's new clauses are Andrew's words and are not widened:**
  - the variant derived from the count of comparables (none: Overview; one: Comparison; two or more: Multi-Comp);
  - commentary always;
  - the staff filer never refused;
  - a commentary failure withholds nothing.
- **C-FIRM's widening** (Opal staff choose ANY firm; the `allowedFirmIds` clause superseded) is exactly "0 blocks or authorization gates
  ... on behalf of any firm". It is scoped to Opal staff. A partner-firm user's firm stays the signed-in user's, and ALL still never
  admits.
- **C-PACKAGER triggered by READY** agrees with FWD-1's "a commentary failure never withholds the other three". It removes the cause of
  "no ticket has carried a package since 2026-10-10" (`resident_worker.py:254`).
- **FWD-2** (no type, email or commentary fields; the models at first paint; every remaining wait gates a real network need) follows
  Andrew's lines one for one. It can be exercised.
- **FWD-8** is new and drawn from his "what is this 400 card series". It can be exercised on FWD-1's request, and the Analysis tab is held as
  a regression arm.

## The defect: FWD-1's ACCEPT contradicts its own DONE WHEN

- **DONE WHEN:** "on DEV, a SYNTHETIC Opal staff user (minted and deleted under a never-widen pair) signs in ... [files]".
- **ACCEPT (new in v0.23):** "The bar is Andrew, signed in as himself, filing his own sample with nothing seeded; a synthetic advisor or a
  pre-seeded directory row does not meet it."
- **SOURCE (unchanged):** still cites "call 2 approved ~17:4xZ (synthetic advisor)".

Read as written, the ACCEPT makes FWD-1 realizable only by Andrew's own act. That is a wait on Andrew. Spine L2 (CLAUDE.md rule 27):
"every outcome is provable by an act a seat can take on demand ... the organic case kept as the negative arm; a genuinely essential wait is
expressly qualified on the outcome with its reason and Andrew's word". Neither record says the bar is his own login.

What he did say is that his own filing was refused and that "we need to know that the testing actually works". That supports the real
point: a test that seeds an advisor or a directory row hides the staff path that failed for him. The synthetic staff user of the DONE WHEN,
with nothing seeded, meets that point, and Andrew's own filing is the organic arm.

## The fix (ACCEPT and SOURCE only; nothing else needs to move)

- **ACCEPT, last sentence, replace with:** "The bar is a real Opal staff identity with nothing seeded: no advisor, no directory row, no
  firm-list entry. The DONE WHEN's synthetic staff user, unseeded, meets it; a synthetic advisor or a pre-seeded directory row does not.
  Andrew filing his own sample is the organic arm, never the gate."
- **SOURCE, add:** Andrew-direct 2026-10-19 ~16:5xZ and ~18:xxZ (the two records above). Mark the "call 2 (synthetic advisor)" citation
  as superseded for the filer by v0.23.

On that bump I sign the same day. Nothing else in the half is refused.

-- `3.0.0_SA_CVO~DELL2`
