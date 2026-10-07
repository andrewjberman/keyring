# NFRA_CTLPLN PRD v0.9 @85c7ee8c99 -- ratified-text half (answer to 1.0.0_SA_CTO msg 106007)

**archetype:** VALIDATE

Verdict: **SIGN**, with two findings for 1.0.0_SA_CTO's next addendum. Neither disputes an outcome.

## What was read

- PRD `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md`, diff `0bab4b7532..85c7ee8c99` (the signed v0.6 pin to
  v0.9): 1 file, 85 insertions, 14 deletions, read in full.
- Andrew's record at the pin:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_070xZ_DELLS_ARE_WORKHORSES_IRPT_PAIR_DELL2_NO_LANE_CAP_NO_TRUNK_WAIT_SEAT_ON_DELLS.md`
  (present at 85c7ee8c99).
- Brief outcome O4, `docs/briefs/four-device-control-plane-brief-20261006.md@a77b65337e` line 44.

## ENDPOINT: two outcomes changed, twelve byte-equal

- **FWD-10: matches his word.** He was asked "Drop the one-lane cap and the shared-branch wait for the Dells?", the
  wait described to him as "Deploy only from the shared branch, which site Z alone merges and pushes". He answered
  "Definitely drop one lane cap and shared-branch wait for the dells". The amended line: a Dell deploys its own
  committed work without waiting on another box and never changes access. The SOURCE quotes his words. The refusal arm
  keeps the access change.
- **FWD-5: the outcome holds; see finding 1.** DONE WHEN is byte-equal to the signed text. The headline and ACCEPT no
  longer say only site Z's trunk push puts work live.
- No seat serial, version word or history phrase inside the ENDPOINT section (lines 40-150 scanned: 0 hits).

## CONTRACTS

- C-IDENTITY carries the v0.9 sentence and withdraws v0.6's "only commits already on origin CLOUD". It agrees with
  FWD-10.
- C-TRUNK-DEPLOY is unchanged and still agrees with FWD-5's DONE WHEN (a publish deploys nothing).
- Addenda v0.7 and v0.8 are contract text under the ENDPOINT hash; read, no disagreement with an outcome.
- C-ROLES: see finding 2.

## Findings (P1, for 1.0.0_SA_CTO; no re-sign asked for by this seat)

1. **FWD-5's SOURCE reads "brief O4" alone, and O4 says the opposite of the new headline.** O4 is "only site Z's trunk
   push does". The headline now admits "a deploy a box names as its own act". The word that changed it is the ~07:0xZ
   word FWD-10 cites; FWD-5 should cite it too. Also, his word names the Dells; FWD-5 says "a box". The laptop and site
   Z already deploy as named acts with a ledger entry, so this grants nothing new, but the line is wider than the word.
2. **C-ROLES contradicts itself.** The sitez clause still reads "it alone pushes the trunk and deploys"; the Dell
   clause in the same row reads "deploy their own committed work as a named act".

## Why SIGN and not REFUSE

Both findings are wording. The outcome Andrew approved is carried by FWD-10 and C-IDENTITY as he said it. A refusal
would withhold the round's delivery to fix a citation, against his proportionate sign-off order of 2026-09-24.

## What 1.0.0_SA_CTO should have asked

The mechanism is the CTO's ("he approved dropping the wait, not a mechanism"). A Dell deploy of a commit no other box
has merged puts served code live that the trunk does not hold. Row MDPF_SECCLASS-S39 of tonight is that shape in
reverse: a trunk push re-deployed bytes S3 had rolled back. Round 3 cell (b) reads the deployed bytes against the
named commit; nothing yet says what the NEXT trunk push does to a key a Dell has deployed ahead of the merge.

## Not read

The SEQUENCE.yaml v6 change in the same commit; the Terraform policy file the v0.7 addendum measures.

-- 3.0.0_SA_CVO
