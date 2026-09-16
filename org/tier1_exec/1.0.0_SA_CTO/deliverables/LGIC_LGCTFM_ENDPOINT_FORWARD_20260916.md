# LGIC_LGCTFM -- ENDPOINT (step 2, /endpoint --forward) -- 1.0.0_SA_CTO, 2026-09-16 ~05:4xZ

**Input (F1):** `docs/briefs/d14-legacy-transform-brief-20260916.md` -- 522 lines, 44,635 bytes, committed @d1f867b0ce
by `4.0.0_SA_CRO` (in HEAD; author date 2026-09-16 05:26Z). No `generated` line; the brief carries its own
"MEASURED AT 2026-09-16 04:0xZ-05:4xZ UTC at CLOUD 74385b5fd5" stamp. Read whole.
**Commissioned by:** Andrew-direct 2026-09-16 ~05:1xZ at the `4.0.0_SA_CRO` terminal (two messages, verbatim in the
brief's header) and ~05:2xZ at the `1.0.0_SA_CTO` terminal (the session goal naming LGIC_LGCTFM and this act; record
`ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md` @a6e628fb89).
**Mode:** greenfield. No project on the register, no PRD, no task orders. Phase 0 only.
**Consumer:** the L4 PRD's `ENDPOINT (step 2, /endpoint --forward)` section, at
`org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md`. ⛔ **NOT YET LANDED IN A PRD** -- the PRD does not exist;
this file is the carrier until L4 pastes the block below verbatim as confirmed.

## The one-line premise, his words

*"take a preexisting product/pipeline/bucket setup/etc, all the resources that compose a product, and essentially how to
render it a canonical nomenclature structure from the LGIC art, and how to mark it and transition it, essentially
consolidating the paths and naming and structures"* -- as a WORKFLOW (*"something like /atom-decomp and
/canonical-flow combined"*): subject in; end-to-end walk; forks; proper names and structure; tensions in structured
form; a contract covering every trigger, script, IAM, bucket, VM and Terraform; a flow diagram; current vs desired; a
remediation plan. The instrument classifies and plans; **it moves nothing** (brief, boxed line under the header).

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  A seat names a legacy subject and gets back ONE contract listing every
         resource that composes it, each row saying which instrument found it and
         what that instrument cannot see
         DONE WHEN  EXERCISED -- run on the first real subject and read by the person
                    opening that subject's migration
         ACCEPT     the person opening the 49 Financial migration learns what the
                    pipeline is made of from the run's contract, and never has to go
                    and list the schedules, machines, roles and buckets by hand to
                    fill a gap the contract left blank without saying so
         SOURCE     brief O1; Part III O1 bar; IV.1-IV.3, IV.6, IV.8, IV.9

  FWD-2  Every fork -- two things doing one job -- is named as a fork, with the one
         canonical member marked, found by the engine and not told to it
         DONE WHEN  EXERCISED -- the first run over a subject that carries known forks
         ACCEPT     the duplicate trees the team already knows about show up on their
                    own on the first run, and the one look-alike pair that is NOT a
                    duplicate does not show up as one
         SOURCE     brief O2; Part III O2 bar; IV.5 (positive controls: the Schwab twin,
                    the two MDPF gold trees, the _legacy pairs; negative control: the
                    SmartX platform/account pair)

  FWD-3  Every resource's DESIRED name and address sits beside its CURRENT one, and
         the desired one was computed by the naming rules, never typed by a person
         DONE WHEN  EXERCISED -- a reviewer who is not the author has reproduced desired
                    strings from the rules
         ACCEPT     a reviewer picks any "should be" name or location in the contract
                    and gets the same string back by asking the rules, and where the
                    rules cannot answer, the row says so and names what is missing
         SOURCE     brief O3; Part III O3 bar; IV.4; Rule 30

  FWD-4  The disagreements between current and desired are a typed, ranked list, and
         the rule that ranks them is printed so the order can be disputed
         DONE WHEN  EXERCISED -- Andrew has read the list for one subject
         ACCEPT     Andrew, reading the list for one subject, can ask "why is this
                    above that" and the answer is the row's measured facts, not a
                    seat's opinion
         SOURCE     brief O4; Part III O4 bar; IV.10 (the tension map's rule, his
                    "These work i like it")

  FWD-5  A flow picture of the subject -- what fires what, what writes where, what
         serves it -- exists in two versions, current and desired, and both are
         drawn from the contract by a program
         DONE WHEN  EXERCISED -- the contract has been edited and the picture regenerated
         ACCEPT     change a row in the contract, regenerate, and the picture changes
                    to match; nobody ever edits the picture by hand
         SOURCE     brief O5; Part III O5 bar; Part V.7

  FWD-6  The migration's work plan comes out of the run, in the order the canon
         rules, shaped so a COO lane can decompose from it directly
         DONE WHEN  EXERCISED -- a real migration's decomposition has been cut from it
         ACCEPT     the 49 Financial migration's decomposition starts from the run's
                    plan instead of rebuilding the inventory from scratch
         SOURCE     brief O6; Part III O6 bar; IV.11, IV.15; Part V.8, V.11

  FWD-7  The run MARKS the subject in the records the commit gate already reads, so a
         person who later adds one more use of a marked legacy location is stopped
         DONE WHEN  EXERCISED -- a planted change has been refused
         ACCEPT     a deliberately planted change that adds one more hand-kept use of a
                    marked legacy location is refused, in a practice checkout with
                    enforcement switched on, and the refusal names the migration
                    project that owns it
         SOURCE     brief O7; Part III O7 bar; IV.7; Part V.6, V.12

  FWD-8  Running it again on the same subject after a migration wave shows what
         closed, what opened and what stayed
         DONE WHEN  EXERCISED -- two runs on one subject have been compared
         ACCEPT     two runs on one subject at two points in time give a reader the
                    list of closed, opened and unchanged disagreements without
                    re-reading either run
         SOURCE     brief O8; Part III O8 bar; Part V.10

  FWD-9  Any seat running it on the same subject at the same pinned point gets the
         same files
         DONE WHEN  EXERCISED -- with its own negative control fired
         ACCEPT     two runs at one pinned point produce identical files, and a
                    deliberately broken copy of the engine produces different ones
         SOURCE     brief O9; Part III O9 bar; IV.13(a); Part V.5

  FWD-10 The instrument moves nothing: after a run, nothing in the cloud and nothing
         the portal serves is different
         DONE WHEN  EXERCISED -- measured after the first real run
         ACCEPT     after the first real run, the only things that changed are the
                    run's own folder and the three record files it marks; every
                    change it recommends is carried out later by a separate
                    migration project under its own sign-off
         SOURCE     brief boxed line under the header; Part II "DOES NOT"; Part V.13;
                    R18/NEVER#1
```

**No FWD is a wait** (Rule 27): every DONE WHEN is an act a seat can drive on demand -- the first run, the planted
commit, the second run, the de-sorted engine, the reviewer's reproduction, Andrew's read of one list.

## What the outcomes deliberately do NOT include

- **No number** -- not a class count, a run time or a tension score (F3; Part III's last paragraph).
- **A migration itself.** FWD-6 and FWD-10 say it in terms: the run plans; a separate R19 project moves.
- **The receiving checker (Part V.9), the Rule 24 record for the schema (V.1), the two-API trigger read (V.3), the
  run-home convention (V.10)** -- these are CONTRACTS the PRD's ratified-text half carries, not outcomes a person
  experiences. They are preconditions of FWD-1, FWD-6 and FWD-8, and L4 places them.
- **The register word (IV.14, "the LENS" in MACROS.yaml's LGIC text)** -- an L3 act on Andrew's confirmation, not an
  outcome.

## For Andrew -- the DONE WHEN confirmation the spine makes his

Ten outcomes, all EXERCISED bars. Three carry a named first subject (FWD-1, FWD-6: 49 Financial on Black Diamond,
because its migration project ADVI_FIRMBKTS is admitted and waiting at L5; brief IV.15). If a different first subject
is wanted, FWD-1 and FWD-6 change their ACCEPT line and nothing else. Confirm, amend, or strike any line; L3
(register) proceeds now because it is reversible and independent of the confirmation; L4 (PRD) waits on the word.

## Provenance (F5)

```
GROUNDED ON: docs/briefs/d14-legacy-transform-brief-20260916.md @d1f867b0ce (whole file, 522 lines);
             the two Andrew-direct records (4.0.0_SA_CRO's @d1f867b0ce, this seat's @a6e628fb89)
NOT READ:    the TO register (no TOs exist for this project; the 19 D14 TOs in flight belong to the
             three sibling projects and were NOT consulted for this phase); org/projects/*.json;
             the tree index; infra/logic/* (cited by the brief, not re-read); lib/opal_naming.py
```
