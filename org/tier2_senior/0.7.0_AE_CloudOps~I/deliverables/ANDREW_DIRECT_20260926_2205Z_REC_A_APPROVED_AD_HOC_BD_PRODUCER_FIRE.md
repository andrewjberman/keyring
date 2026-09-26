# ANDREW-DIRECT 2026-09-26 ~22:05Z -- rec (a) approved: fire the Black Diamond producer once, ad hoc

**Channel:** the `0.7.0_AE_CloudOps~I` terminal, site Z. Andrew at the terminal, answering the single
card from `/open-calls` run at this lane.

**VERBATIM, his whole message:**

> rec a approved

---

## What that approves, exactly

The card he answered, reproduced so the word is readable against its question:

> **Fire the Black Diamond producer once, ad hoc, tonight? (a) yes (b) wait for Monday's scheduled
> run (c) stop at the vendor boundary**
> It is the last act in MX-s-4 (now steps 1-2 only). The trigger is weekdays 22:10Z, so (b) costs
> ~48 hours -- today is Saturday.
> **REC -- (a).** CLAUDE.md is explicit that "waiting for the scheduled run" is itself the failure
> unless the ad-hoc would destroy the discriminator the scheduled run exists to produce. It would
> not: Monday still fires and stays the acceptance. One ledgered run, no new credential.

**APPROVED: (a).** ONE ad-hoc run of the EXISTING producer, against the Black Diamond portal, ledgered.

## The scope of this word, stated narrowly because a vendor word must be

COVERED, and only this:
- ONE ad-hoc invocation of the existing SSM document `opal-bd-asset-dim-download`, run as the producer
  already runs it, with its own existing credential from `opal/bd/credentials`.
- Each vendor-facing run ledgered in this lane's deliverables, per MX-s-4's preflight.

NOT COVERED, and unchanged by this word:
- A NEW credential, an MFA device, an account change, or any contract or interaction with the vendor.
  MX-s-4's step 1 carries that carve-out verbatim and it survives: *"If the fix needs a new credential,
  an MFA device, an account change or anything from the vendor: STOP, file a BLOCKING row, and
  report. That is Andrew's word."*
- Repeated or standing ad-hoc runs. The card said ONCE and the approval is of that card.
- Any sibling producer. `fees` and `allocation` fail identically and are NOT in this order.

>> The per-use question this card existed to settle: MX-s-4's preflight already cited an Andrew-direct
of 2026-09-26 that "API egress is permitted this session". CLAUDE.md requires a PER-USE word on top of
availability, and a banked lesson says an existing narrow producer still needs it. He was asked whether
the session-level word already covered repeated runs of an existing producer; he approved the card
rather than answering that broader question, so THE BROADER QUESTION REMAINS OPEN and the narrow
reading stands: one run, this run. <<

## Order of acts, and why the deploy comes first

1. Deploy the honest-exit fix (`4b3a757410`) to the live SSM document, under its own NEVER-2 ledger.
2. THEN fire the producer once.

That order is load-bearing. The run is expected to FAIL at the login, exactly as the last 69 have. Under
the current live document a failure exits 0 and SSM records Success, so firing first would produce no
AC4 evidence at all -- AC4 asks for "a real or planted failure's SSM status", and the failure is already
real. Deploying first turns tonight's expected failure into the evidence AC4 needs.

Monday's scheduled 22:10Z fire is unaffected and remains the acceptance.
