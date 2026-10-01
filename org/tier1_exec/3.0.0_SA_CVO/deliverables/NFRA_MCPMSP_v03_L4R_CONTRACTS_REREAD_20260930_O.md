# NFRA_MCPMSP PRD v0.3 -- re-read of the changed CONTRACTS (3.0.0_SA_CVO~O, 2026-09-30 ~06:3xZ)

**Subject:** `org/missions/D6/NFRA/NFRA_MCPMSP/prd/NFRA_MCPMSP_PRD.md` @c2f5d5a071 (v0.3), against this seat's signed
bytes @b90b97652f (v0.1, review @8d6851f97c). Also read: the NFRA_MCPORTAL v0.4 C4 addendum and the
`org/standards/NFRA_OPLGTW_CONTRACT.json` change in the same commit. Asked by 1.0.0_SA_CTO~O, msg 26957.
The ENDPOINT is unchanged (prd-signoff reads "current by ENDPOINT hash"), so under proportionate sign-off nothing is
withheld. The v0.1 stamp STANDS. This record does NOT re-sign at c2f5d5a071; see F1 and F2.

## Closed

- **N1 (tenant-registry writer): CLOSED.** `tenant_firm` sits at `POLICY#TENANT#<tid>`, inside the existing `POLICY#`
  LeadingKeys guard, following the `POLICY#EMAILDENY#` precedent (`access_state.py:62`). It has one writer, MCPORTAL's
  grant writer op `register_tenant`, which is owner-verified, refused for a firm not brought live, and audited. The
  gateway only reads it. The OPLGTW contract gains the record type. The three documents agree.
- **C5 v0.2 (option (a), portal-v2 prefixes): agrees.** Record s.10 card 5 chose "current buckets" over the successor
  buckets. `opal-data-portal-v2` is a current bucket (`app/query_v0.py:58`), and it is where the served figures A1
  names actually live. The prefix-plus-Deny shape is CLAUDE.md's shared-bucket form. Options (b) and (c) are correctly
  rejected.

## Findings on C5 v0.3

- **F1 -- C5 now contradicts itself.** Two sentences still state the guarantee unconditionally: the first bullet ("The
  gateway's own identity carries no read on any firm's data (record s.8)") and the closing line ("A scoping bug
  therefore surfaces as an AWS refusal, not as a leak"). The v0.3 bullet makes both false in round 1 for
  `opal-data-portal-v2`: the gateway identity keeps a read of every firm's served figures, so a router scoping bug on a
  partner request would leak rather than be refused. A decomposition that cuts from either sentence builds an arm (A1n)
  on a promise the same section withdraws. **Fix (text only):** scope both sentences to what round 1 enforces (the
  firm buckets), and point to the named residual.
- **F2 -- the staging narrows Andrew's word, and the ruling is this project's CTO's alone.** The question Andrew
  answered "yes to per-firm role" to (record s.8) was: "the one server's own AWS identity holds no read on any firm's
  data ... so a scoping bug is refused by AWS rather than leaking data". v0.3 keeps that read on the served figures
  while real partner traffic runs (FWD-1's live conversation, round 1). The reason is sound: a Deny would move internal
  served answers, which is a never-widen act. But the residual is a departure from his stated design during partner
  traffic, and it is his to accept, in the same way an R20 departure is. **Recommendation, not a new gate:** put the
  named residual to Andrew in words, for example with G-FIRM for Inflection, which is already his word and already
  precedes the first partner answer. Record his answer beside s.8.

Neither finding touches the ENDPOINT, and round 1's cells 0-4 do not depend on either. This seat re-signs once C5
carries F1's text fix and F2's answer is recorded (or C5 records that Andrew was asked).

## Re-read at @a227ad9ada (2026-09-30 ~06:3xZ, 1.0.0_SA_CTO~O msg 26970) -- VERDICT: RE-SIGN

- **F1: CLOSED** (@64b086e529). The first C5 bullet now states the zero-read as the target, holding for the firm
  buckets and not for `opal-data-portal-v2` until the staging closes. The AWS-refusal line is scoped to a firm-role
  bug, and it names the router-bug residual as NOT caught by AWS.
- **F2: CLOSED.** Andrew, verbatim, "Yes, rec approved" (record
  `ANDREW_DIRECT_20260930_06xxZ_NFRA_MCPMSP_PORTAL_V2_RESIDUAL_ACCEPTED_FOR_INFLECTION_PILOT.md` @a227ad9ada). The card
  put to him named the residual in plain words ("only the tenant lookup, not AWS, would stop a bug"). C5 carries his
  answer and its condition: the portal-v2 zero-read lands before any second partner firm; FWD-2 is not graded and no
  second G-FIRM is taken until then.
- **Note for L5 (non-blocking):** the Canonical handoff lists "Cottonwood and isolation (FWD-2)" as the first
  enrichment round, but does not list the portal-v2 zero-read round. C5's condition makes that round precede FWD-2's
  grading, so the decomposition should cut it first (or into the same round, ahead of the Cottonwood G-FIRM).
- Re-signed at half_hash `3244b10a028d516f37e4be4304be20cf636a9bb7c5286a16b269fe44c9983798`, recomputed here.

-- 3.0.0_SA_CVO~O
