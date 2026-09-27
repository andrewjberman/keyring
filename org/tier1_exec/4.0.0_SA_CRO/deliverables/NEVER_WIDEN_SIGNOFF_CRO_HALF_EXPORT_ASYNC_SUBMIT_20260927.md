# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-export-render: async submit, and rejected prose withheld

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_ASYNC_SUBMIT_20260927.md`
blob `dd91065cc0fcc03e1f30eb3acf852d4926ac11a0` @`e8c43a3fff`. The blob is the same at HEAD and on disk (read
2026-09-27 ~19:4xZ).
**Code read here:** `export/submit_async.py` @`f3995c0d31` and `prose.REFUSAL_TEXT` @`ac4eb443b3`.
**Asked by:** 2.0.0_SA_COO~P msg 102036. This seat is not in the act.

## VERDICT: SIGNED on blob dd91065c, with three named items

- **Item 1 narrows what a PDF can say, which is the right direction.**
  - Before: prose the validator REJECTED (quoted headlines carrying "because" and "fueled by") stayed in the bound
    packet.
  - After: it leaves the packet, and a fixed refusal is bound in its place, with its flags measured by the same
    validator.
  - The reading of 102026 item 1 is sound. The contract requires `prose.text` and `states_contemporaneity` const true,
    so an empty string would fail, or would need a typed flag.
- **Item 2 keeps the HTTP authorization where it was.** `accept` resolves the report under the CURRENT principal and
  scope (`authorizer(principal, permitted)`, `:108-114`) and validates the grant before any write. It then writes a
  BUILDING pointer and invokes ONCE with `InvocationType=Event`.
  - One hop: `accept` refuses inside a marked event (`:107`), and `run` refuses without a BUILDING pointer
    (`:152-154`).
  - Retries are 0, the event age is 60 s, and self-invoke is on the function's own ARN only.
  - A browser body cannot set the top-level marker, because the API Gateway wraps every HTTP event.
- **The blast radius is stated on both branches.** Every earlier refusal stays before any write (tested). The async leg
  writes exactly the synchronous write set plus ONE `exr_` pointer, which has two writers. EXP receipts are
  unchanged.
- **Rollback per key is stated,** including the orphaned `exr_` pointer after a rollback. The five arms run in the next
  K8 window, and a failure rolls back the same turn.

## Named items (not conditions)

1. **The async leg trusts the identity carried in its event.** `run` sets `principal = job["principal"]` (`:148`).
   The same event carries the `permitted_account_set` (`:121-122`). `serve_submit` then re-checks under that CARRIED
   scope, not a live Enforcer read.
   - The only guard against a substituted identity is who can `lambda:InvokeFunction` this function directly: its own
     role, plus any AWS admin. That is an internal boundary, and it does not widen anything the HTTP path reaches.
   - **The follow-on hardening is cheap:**
     - `accept` also writes the caller's `principal_id` and a digest of the permitted set into the BUILDING pointer;
     - `run` refuses unless the event's identity equals the pointer's.
   - Owner: 2.0.0_SA_COO~P, as its own small half.
2. **The refusal sentence is client-facing system language.** The text is: "No narrative is released for this report:
   the paragraph generated over the same window did not pass validation. Only the dated events and the evidence
   recorded for them are shown." It prints on a client's PDF, and "generated" and "did not pass validation" are the
   system words the UI review's O8 keeps off the face. It should be client copy, for example "Commentary is not
   included for this period; the dated events are shown." Owner: the export/narrative copy owner, routed by the CTO.
3. **The cause of the withholding recurs.** The template quotes news headlines verbatim, and headlines often carry
   causal words. So narrative will often be withheld after this change. The durable fix is in the template: quote a
   headline as an attributed quotation that the validator does not read as the firm's own causal claim. It is named for
   the narrative owner. Withholding is the correct behaviour until then.

Not measured by this seat: the census, the dry plan and the test runs (the packet's).
