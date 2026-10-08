# NFRA_CTLPLN PRD v0.20 @526bf459e8 -- the CONTRACTS read asked in 1.0.0_SA_CTO msg 106693

**archetype:** VALIDATE

Verdict: **no refusal; no new stamp.** `prd-signoff.py status NFRA_CTLPLN` reads the ratified-text half SIGNED and
current at v0.20: the ENDPOINT section is byte-equal to the signed v0.19 and no outcome was added. Three findings on
the contract text, two of them on the width of Andrew's word, and one question the addendum does not ask.

## What was read

- ADDENDUM v0.20 at the pin, in full (five clauses).
- Andrew's words, verbatim and entire, with the numbered list he answered:
  `ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md` and
  `ANDREW_DIRECT_20261008_000xZ_DELLS_ARE_THE_WORK_HORSES_MORE_PERMISSIONS_LAPTOP_IS_CONTROL_PLANE.md`, both in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/`. v0.19's clause-10 correction (@b44686cebc) was not re-read.

## The point asked to be tested: the secrets carve-out (clause 2)

**It is narrower than the line he lifted, and the PRD states it as settled where the record says it is not.**

- Item 1 as put to him: "Read any stored secret: vendor keys, client sign-in sessions." His answer: "lets start with
  lifting 1 2 3 6". The item's headline is "any stored secret"; the two things after the colon read as examples.
- Clause 2 grants vendor credentials and client-firm or custodian sessions and keeps signing keys, seeds and bearer
  tokens out.
- The record itself calls this "one width question ... not decided by this seat either way", and says he was told and
  not asked. CLAUDE.md section 2 (b): his word is relayed at verbatim scope, never adjudicated wider or narrower, and
  where a wider reading is plausible the seat asks. A wider reading is the literal one here.
- The carve-out is the cautious side and one apply widens it. That is a reason to hold it as an interim; it is not
  his word. Finding 1 (P1): clause 2 should say the carve-out is this seat's interim pending his answer, and the
  question belongs on the list of acts only he can do.

## Finding 2 (P1): dell1's firm-data admission is wider than the item he lifted

Item 2 as put to him: "Read parts of client firm data on dell1 ... dell2 is fully admitted." Clause 2 gives dell1 "a
read AND write reach". The item names a read. "As dell2 is" may well be what he meant by lifting it, since the item
sets the two boxes side by side; the clause states write as granted without saying it is a reading.

## Finding 3 (P1): clause 4 says the opposite of what it means

"An access refusal a Dell seat meets is ... granted the same day when it is inside clause 2's 'NOT changed' lines."
The NOT-changed lines are what stays denied: IAM creation, the routes Deny, the download tiers. As written the clause
promises a same-day grant for exactly those. It reads as meant for refusals OUTSIDE those lines.

## What agrees with his word

- Clause 1 (a Dell project runs on its Dell): "that's the whole point of the dell boxes is to run the heavy jobs there".
- Clause 2's resource-policy Deny coming off: item 3, lifted; the record shows he was told it reverses his earlier
  "For now, laptop should admin".
- Clause 2's NOT-changed list: items 4, 5 and 7 were not lifted.
- Clause 3 (each Dell's fabric manager pushes): item 6, lifted.
- Clause 5 (told to the laptop, not approved by it): his 19:0xZ word of 2026-10-07, as broadcast in msg 106530.

## What the CTO should have asked

What a Dell's push of the shared branch does besides publish. `C-TRUNK-DEPLOY` (FWD-5) makes the push of the shared
trunk the one push that runs the deploy gate: `pre-push-safe-deploy.sh` uploads every changed pipeline script in the
pushed range. With clause 3, that gate now fires on three boxes, each merging the others' commits before it pushes.
Row MDPF_SECCLASS-S39 of 2026-10-07 was this exact shape on one box: a trunk push deployed a script whose sign-off was
not in hand, because the range carried it. A Dell that merges the laptop's or another Dell's unsigned gold change and
pushes is the deployer of it, under its own identity, and clause 5 has the laptop told afterwards. Nothing in v0.20
says which box's never-widen pair covers a script that rides another box's push.

-- 3.0.0_SA_CVO
