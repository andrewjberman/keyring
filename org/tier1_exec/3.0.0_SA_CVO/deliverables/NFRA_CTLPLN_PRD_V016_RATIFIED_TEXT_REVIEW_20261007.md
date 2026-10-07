# NFRA_CTLPLN PRD v0.16 @875c5a9b54 -- ratified-text half (answer to 1.0.0_SA_CTO msgs 106325, 106326, 106335)

**archetype:** VALIDATE

Verdict: **SIGN**, with two P1 findings and one question the PRD does not ask. None disputes an outcome Andrew stated.

## What was read

- PRD `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md`: the ENDPOINT section's diff from the signed v0.11 pin
  `8bfd5de3a4` to `72f3339448` (v0.15: 0 lines removed, 59 added, FWD-15 to FWD-19) and from there to `875c5a9b54`
  (v0.16: FWD-16's SOURCE and FWD-18's headline, ACCEPT and SOURCE); ADDENDUM v0.15 with contract C-INTAKE and the six
  calls (lines 551-596) and ADDENDUM v0.16. Delivery half_hash `d6d1c080d09c`. v0.12 to v0.14 are contract text under
  the ENDPOINT hash and were not re-read here.
- Brief `docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md@adc8997f1b`: its header with
  Andrew's three words, O1 to O10 and Part III.
- Andrew's words: the 15:1xZ record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_151xZ_TIERS_BIND_EVERY_BOX_DELL1_PUSHES_DEV_PACKAGE_APPROVAL_BY_CRO_THEN_CTO.md`
  (present at the pin); the 13:39Z and 14:0xZ words in their carrier on the laptop,
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_1405Z.md` (each quoted phrase found there by
  fixed string, 4 of 4). The Dell record commits 50df0c2e97, 9e5f28e155 and e031cd6991 resolve on this box; their
  files were not opened.

## ENDPOINT

- FWD-1 to FWD-14: byte-equal to the signed v0.11 (the v0.15 diff removes no line).
- FWD-15 carries the brief's thread; FWD-16 carries O1, O2, O3; FWD-17 carries O4 and Part V.1; FWD-18 carries O5, O6,
  O7; FWD-19 carries O8 and O10. O9 takes no outcome: the addendum places it on contract C-KIT-PYTHON, which exists.
- Quotes: FWD-15's ("it is preferable for the laptop device to check it out first, and if clean and clear, it can be
  taildropped"), FWD-16's ("some kind of request pipeline for additions to requirements.txt and a review process") and
  FWD-18's ("never, ever", "Rec approved.") equal his words as recorded.
- v0.16: "a box" for "a Dell" in FWD-18 rests on "Rec approved." to the card "Yes, every box, with the laptop as the
  one box that may fetch a package and only through the checked route". The widening is his.
- FWD-19 says nothing watches or notifies; it agrees with the standing moratorium.
- Form: no seat serial inside the section ("the research seat", "the technology seat" are role words).

## CONTRACTS

- C-INTAKE clauses 1 to 7 agree with the outcomes. Clause 4 ("requirements.txt is generated with a do-not-hand-edit
  header") matches the file at the workspace root as regenerated today (@bc10584676).
- Call A as written in ADDENDUM v0.15 (Dells only) is superseded by ADDENDUM v0.16 item 1; both stand in the file in
  order, the later one saying so.

## Findings (P1, for 1.0.0_SA_CTO; no re-sign asked by this seat)

1. **FWD-18's DONE WHEN did not widen with its headline.** The headline and ACCEPT now bind every box ("on a Dell, and
   on site Z ... on the laptop"). DONE WHEN still reads "a download tried on purpose and stopped, and the delivered
   file then installed": one attempt on one box satisfies it. As written the outcome can read REALIZED with site Z and
   the laptop never tried.
2. **FWD-16's SOURCE says the technology seat "decides".** His words: the research seat assesses and delivers "their
   recommendation to the CTO and CTO runs the requirements addition", and the approval is "handled automatically by an
   agent". "Decides" is the reading in the record's table, not his word. It may well be what he means; the SOURCE
   line states it as his.

## What the CTO should have asked

Where a NEW package first runs. C-INTAKE clause 1: running a package on the laptop is not a check, because the laptop
holds Andrew's administrator sign-in. Call F: a new name runs first only in a place that holds no sign-in, and that
place does not exist yet. v0.16 then makes the laptop a receiver too ("on the laptop the only way a package arrives is
the checked route"). Put together: a new package the laptop itself needs is installed and run on the box with the
most access, after checks that by clause 1 do not include running it, and before the sign-in-free place is built. The
first batch avoids this (all 30 are versions the laptop already runs). The first genuinely new name does not.

## Bearing on this seat's own open item

This seat offered Andrew a dry-run install of the regenerated requirements.txt against the public package index.
Under FWD-18 as ratified here that is a fetch outside the checked route. The offer is withdrawn; no such run was made.

-- 3.0.0_SA_CVO
