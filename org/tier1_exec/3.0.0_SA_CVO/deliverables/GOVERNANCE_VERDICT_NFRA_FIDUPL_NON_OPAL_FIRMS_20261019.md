# Governance verdict -- NFRA_FIDUPL: other firms' accounts in the full Alongside pull

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1, 2026-10-19 ~19:0xZ. Answers 1.0.0_SA_CTO~DELL1 msg 8480 (self-drive box tick 153; acked).
**Read:** the CRO's G-number measurement, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_G_NUMBERS.md` @14f422aa7d
(whole); Andrew's relayed words, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_RELAY_DELL1.md`;
CLAUDE.md section 2 (relay verbatim; if wider seems plausible, ASK); `infra/logic/02_DOCTRINE.md` R7.

## Verdict: the REC is REFUSED as a ruling; the class goes to Andrew as an ask

The REC reads Andrew's staging word as already covering the landing of 17 non-Opal G numbers' accounts. The words do not carry that
reading:

- **His staging word is conditional.** He said: "THe issue becomes whether or not we have a clear mechanism by which to do that. If we do
  not, and need to use alongside as a staging bucket for the full pull, ... then so be it." The CRO measured the condition's other branch:
  "each G number's label names exactly one firm", so these are "clear differentiated masters that tie to different firms" (research s.1).
  The fallback is the branch his own test did not select. Staging is still a fair interim reading while the per-firm mechanism is
  unmeasured (research s.3), but only for Opal's firms.
- **His words name only Opal's firms.** He said "pulling them to the relevant bronze buckets per client" and "fidelity-bronze-49financial
  and fidelity-bronze-inflection and so on". The brief (:149-151) records his umbrella as Inflection, Cottonwood and 49 Financial. Nothing
  he said shows he knew the login sees Keil, Abiding, Lighthouse, VM and one advisor-named G number (17 of 31).
- **The REC widens his word.** It would land and keep, in Opal's bucket, the client-confidential account data of four firms that are not
  Opal's clients. That is wider than he spoke, and wider is plausible. Under CLAUDE.md section 2 the move is to ASK, not to infer. The CRO
  reached the same point independently: "it is Andrew's to say" (research s.3).

## What may proceed now (it widens nothing)

- **The settling read.** The CRO's read (a) is the Export Custom wizard's step 3 "Choose Filter": is "G Number" a filter? The automated
  sign-in is now authorized (C-TOU met), so the sign-in cell can read the wizard's options without starting an export. If the filter
  exists, one profile per Opal firm pulls only Opal's G numbers, the class empties, and Andrew's question disappears.
- **Every cell that does not land the full pull:** the sign-in, the registry rows, and the Terraform authoring.

## The ask for Andrew (one decision)

> The Alongside login also sees 17 G numbers belonging to Keil, Abiding, Lighthouse, VM and one advisor. A full-book pull brings their
> clients' accounts too. May Opal land them raw under `fidelity/alongside` and list them unplaced, or must the pull exclude them (one export
> per Opal firm, filtered by G number)?

**REC beneath it:** exclude them. Pull per firm on the G-number filter if the wizard offers it. If it does not, stage the full pull, then
split it, and delete the non-Opal remainder after the split, with the deletion named in the run record. Either way, no data Opal has no
purpose for is kept.

## Surfaced, not ruled

- The research names five export files already on dell1 (2026-10-16: `.naa`, `.ipn`, `.trn` and `prices.txt`). They hold the full book
  (5,007 accounts), so the non-Opal firms' accounts are already on a box. Andrew's answer to the ask decides their disposition too.

## What this verdict does NOT move

- FIRM tenancy, never COMPOSITE (@bc07810172), and the opal-data-assets home (Andrew ~19:0xZ) are unchanged.
- Open call `5d43` (the nine DONE WHEN lines) is unchanged. FWD-9's "accounts no firm claims listed" holds under either answer.

-- 3.0.0_SA_CVO~DELL1
