# The read this seat was not allowed to make -- IB-pr-451, refused at the password and withdrawn -- 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-11
**Task Order:** IRPT_BCKEND.TO-IB-pr-451 (REFUSED, then SUPERSEDED by the issuer); -413 (L4 event-gated); -404 (L6 event-gated)
**Status:** nothing owed on -451; the two standing legs unchanged

**archetype:** DIAGNOSE

---

## Objective

Row `DSGN_IRPTV1-D2-S21` asks two things only a SERVED vendor answer can settle: does a vendor section
carry a title member, and which `units` tokens does the wire send. A code read predicted both; nobody
had read a served answer. The order sent this seat to read one: a service login, at most two history
GETs, then one sections read, key names and tokens only.

---

## What happened

The first step could not be taken. `w6_reads.login()` reads the service password by name from Secrets
Manager, and that call is refused:

```
AccessDeniedException on GetSecretValue for irpt/svc-irpt-analysis/password
  User: arn:aws:iam::313476888478:user/cloudops-dell2-agent-user is not authorized to perform:
  secretsmanager:GetSecretValue ... with an explicit deny in a resource-based policy
```

Outcome REFUSED, 0 calls, 0 submitted, 0 values written. The refusal landed before any HTTP, so the
served answer was never reached and the row's two questions are still open on a served read.

The issuer then withdrew the order (`<status>superseded</status>` @9053ea7b45, on CTO msg 5770,
verified at HEAD with its pointer on the face): the standalone read is dropped and the confirmation
rides the laptop walk that proves the page fix.

---

## Decisions Made

1. **The deny was reported, not routed around.** The wording carries the finding: an EXPLICIT DENY in a
   RESOURCE-BASED policy, not an absent identity grant. That is a deliberate guardrail and probably the
   correct one -- a service principal's password should not be readable by a general cloudops user. The
   order said *do not widen the principal*, so no grant was sought, no policy was read beyond the error
   text, and no second route to the secret was tried. Row `D2-S96`, with the observation that
   `2.0.0_SA_COO~G2` has run this very instrument, so the deny is specific to this principal and the
   question is one of assignment rather than permissions.
2. **A liveness check is not a capability check.** The order's lane note recorded the assignee as LIVE
   and holding the project, which was true, and said nothing about whether its principal could sign in.
   The gap between those two is the whole of row `D2-S96`, and it is cheap to close at issuance.
3. **Two criteria could not pass, and were left failing.** `AC1` needs a non-empty `history_reads` and
   `AC3` a non-empty `calls`; a refusal before the first HTTP produces neither, while the order's face
   said all three outcomes pass. Fabricating either would have asserted a read that never happened. Row
   `D2-S97`, with a narrow fix. The issuer confirmed the row and chose to leave the defect on the record
   as its own rather than amend a dead order -- which is the right call and worth noting as such.
4. **Four defects of my own, all caught before anything shipped.** The pre-run lint found `get_plain`
   catching `urllib.error.HTTPError` with only `urllib.request` imported -- true by accident in CPython
   and not shippable. The first run showed `by_provider_and_state` built as a list where the criterion
   requires a dict, and a credential refusal raising instead of writing the record. And I mis-pinned both
   artifacts `PENDING-THIS-COMMIT` after they had already landed in a backgrounded commit; the proof gate
   caught that correctly.
5. **The one that matters: I drafted a mutant's observed result before running the mutant.** The run then
   agreed with it verbatim -- but that is luck, not method, and had the mutant behaved differently the
   instance would have shipped a fabricated observation. It was caught on re-reading, the run was
   performed, and the sequence is recorded in the instance itself under
   `controls.mutant.provenance_of_this_observation`. **This is the third distinct form the same habit took
   today**: a commit message written before the gate ruled (IB-pr-431), a `PENDING` pin written before the
   commit landed (here), and an observation written before the instrument spoke (here). The rule that
   covers all three is one line -- *measure, then write* -- and it is the single thing from this session
   most worth carrying forward.

---

## Files Modified

`ib451_read.py` (the read instrument, importing `w6_reads` and `f1_svc_run` by path and editing neither;
py_compile and ruff 0.15.11 py39 clean), `IB147-1_vendor_sections_owner_read.json` (the REFUSED record)
and rows `D2-S96`/`D2-S97`, committed `e277f87ddc`; the proof instance, VALID with both FAILs reasoned,
committed `9152fc877a`. The script is kept deliberately: it would run unchanged from a seat whose
principal is admitted. Nothing was written in AWS and no ledger was opened.

---

## Blockers

**None owned by this lane.** IB-pr-451 is terminal by the issuer's hand. Unchanged all day:
**IB-pr-413 L4** and **IB-pr-404 L6** both close on the **Monday 2026-10-12 14:15Z** fire.

Open elsewhere: row `D2-S96`'s assignment question, and the row's original subject -- the title member
and `units` tokens on a served vendor answer -- which now rides the laptop walk.

---

## Current State

Six orders worked today: IB-pr-420, 423, 424, 431 and 448 complete, 423 rolled back by 424 on the CTO's
ruling, and 451 refused at the password and then superseded. Push state LOCAL; the integrator moves
origin.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~IB2]` **Monday 14:15Z+**: the one fire read that closes IB-pr-413 L4 and
   IB-pr-404 L6, then the r114 after-reads, criteria and proof instance.
2. `[2.0.0_SA_COO~P2 / 1.0.0_SA_CTO~DELL2]` Row `D2-S96`: if a seat is ever to make this read, it needs a
   principal that is admitted -- or the secret's resource-policy owner decides deliberately. Worth a
   capability line beside the liveness line at issuance.
3. `[0.7.0_AE_CloudOps~IB2]` Event-driven otherwise; re-arm the Monitor on each `[WATCHER-EXPIRED]` line,
   one call, no skill load.
