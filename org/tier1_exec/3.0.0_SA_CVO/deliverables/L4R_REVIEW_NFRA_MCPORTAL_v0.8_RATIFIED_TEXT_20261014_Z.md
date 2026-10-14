# L4-R review, NFRA_MCPORTAL PRD v0.8, ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-14 ~02:5xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 33945 and 33946 (both acked). **Bytes reviewed:**
`org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md` @d0dd3f0964 (the working tree equals the pin). I read
`git diff cdb5ff66b1 d0dd3f0964` whole: the bump from v0.7 (this seat's last signed pin), FWD-21 and FWD-22 in
ENDPOINT, and the v0.8 addendum with C18. Half hash at review: `ce592cd443f6`.

## Sources read

- **FWD-21's quotes:** `DIRECTION_SITEZ_20261013.md:52` ("All that needs to be visible and controlled through MC Portal")
  and `:64` ("this way we have one master control panel"). Both match.
- **FWD-22's quote:** Andrew's ~20:4xZ words as carried verbatim in row Z-S47. The record file
  `ANDREW_DIRECT_20261013_204xZ_CONTROL_PLANE_SHOWS_CLAUDE_ACCOUNT_AND_USAGE_PER_BOX.md` exists under the CTO's
  deliverables.
- **Counterparts:** depth and cadence come from NFRA_MCPINDEX FWD-20 (v0.10, signed by this seat; depth read from the
  served artifact) and NFRA_OPLGTW FWD-20 (v2.8, signed; cadence read live). They agree with this text.

## Verdict: SIGN

- **FWD-21** exercises every control it grants: channel, tool and person stop, each switched off and back on. The read
  is checked back from the grant store and on the person's next call. Writes are Andrew-only (C2) and are recorded with
  before and after (FWD-4).
- **FWD-22** is display-only, reads a login record and never a token, and gives every figure a claim and an age. Its
  first cell is a read: where the limits are exposed is not yet known, so building first would guess.
- **C18** keeps one writer. The deploy-time files remain the floor. It has a per-change rollback and a mechanism
  rollback, and it types no new name.
- Both outcomes are Andrew's words at their width. No seat name appears in the ENDPOINT text.

## Owed elsewhere: the gateway side of C18 has no counterpart contract

C18 makes a per-person tool, channel or tier change a new record kind in the grant store, "honoured on the next call".
Honouring it is the GATEWAY's admission decision: `tier.resolve_tier`, the identity scope, and the tool allowlist
overlay. NFRA_OPLGTW's PRD (v2.8) still admits tools and tiers through the deploy-time files only (`:916`,
`identity_tool_allowlist.txt`; `:937`) and says nothing of a store record kind. This is not grounds against this half,
which is coherent. Before the first FWD-21 write cell, one of two things is owed:
- an NFRA_OPLGTW addendum naming the record kind as an input to its admission decision, or
- a C18 line naming which project's cells write that gateway code.

Without one, the store write lands and the gateway ignores it. FWD-21's DONE WHEN would catch that, but only at the end.

## Carried (not grounds)

1. **The widen-above-floor branch is never exercised.** C18 lets a store record widen beyond the floor for a tool the
   floor lists for some principal. FWD-21's DONE WHEN only switches things off and back on, so every exercised change is
   at or below the floor. Exercise one widening on the test principal, or drop the widening clause until it is wanted.
2. **The Bloomberg account.** NFRA_OPLGTW v2.3 says `opalbloomberg` mirrors Andrew's principal "for now". FWD-21 lists
   it like any person and lets Andrew narrow it from the panel. A per-person edit there departs from the mirror. That is
   Andrew's to make, and the page should say the account is in mirror mode until he edits it.

-- 3.0.0_SA_CVO~Z

## Re-read, 2026-10-14 ~03:0xZ: the C18 line and NFRA_OPLGTW v2.9 C-PERSON (@e5e2ce91ec, CONTRACTS only)

The owed counterpart above is written. C-PERSON has `decide()` read the per-person record. The Opal-only, C2 and tier
gates are evaluated first, and with no record the gateway behaves exactly as today. NFRA_OPLGTW cuts the reader, and
FWD-21's write cell F2 waits on it. This is wording under proportionate sign-off, so neither half re-opens.

One mismatch, between the CTO's summary (msg 33953: "A record never widens past the floor") and the text it summarises
(C-PERSON: "It widens only to a tool the floor already lists for some principal"):
- The TEXT governs. It permits widening one person beyond their own floor, up to tools served to someone.
- The COOs received the summary. The first write cell must cut against the text.
- Carried note 1 above therefore stands: exercise one widening on the test principal, or drop the clause.
