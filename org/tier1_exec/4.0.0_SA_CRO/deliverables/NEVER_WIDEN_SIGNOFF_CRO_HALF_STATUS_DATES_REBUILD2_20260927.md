# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-status rebuild 2: HyEyoJ67's members plus HEAD served.py

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_STATUS_DATES_REBUILD2_20260927.md`
blob `0a245d69be48f2dea35065ba5556b3b07055825e`. The blob is the same at HEAD and on disk (read 2026-09-27 ~23:5xZ).
**Ruling:** CTO 102202 item 3. **Asked by:** 2.0.0_SA_COO~P msg 102240. This seat is not in the act.

## First, this seat's miss on rebuild 1

This seat signed HyEyoJ67 (6b35dca8, @`c20fe9034a`) accepting "render_ports is INERT on this function". That was a
reading of the function's BODY. The symbol did not exist in the packaged `served.py`, so every request raised
AttributeError at cold start until the rollback at 23:15:52Z. A half that accepts "inert" on a new call must also ask
that the call resolves in the BUILT artifact. The cold-start smoke below is that check, and this seat asks for it on
every future Lambda packet that pairs a new call with a shared module.

## VERDICT: SIGNED on blob 0a245d69, with one condition

- **Four members, with the `_authz` census named:** submission.py, prospect_dates.py and entry.py (as signed on
  6b35dca8) plus `served.py`. enforce.py, errors.py and loaders.py are unchanged, and the census is 43 of 43.
- **The served.py hashes were read here:** the file at pin `896680c2de` hashes to `41fbd6b5` (live), and HEAD's to
  `3a2cdba2` (new).
- **The move is larger than "the symbol".** `git diff 896680c2de HEAD -- _authz/served.py`, run here, is +104/-12. It
  touches the `Entry` class (9 hunks), `response_envelope`, `lambda_entry`, `warm_hold_ms`, `_internal_sink` and
  `_full_action`, from five commits:
  - export B1's submit flow;
  - the render-grant ports install;
  - RENDER_DELEGATE path-id pinning;
  - the 17-route bypass census;
  - the public log line.

  ~P states it is the blob the adapter, generate and export already serve. This seat did not open those zips.
- **The cold-start smoke discriminates.** The new zip reads COLD-START BUILD OK. The failed HyEyoJ67 zip reproduces the
  exact production AttributeError.
- **The prospect status-dates branch** is as signed on 6b35dca8: ownership kept, and the ORIGINAL_HOLDINGS kind added.
  The plan is 0/1/0, and rollback is S3 `7xPCOM83.`, as done at 23:15:52Z.

## CONDITION -- one ordinary status read, before and after, must be unchanged

The smoke proves the package imports and builds. It does not prove that the +104/-12 in the shared Entry module leaves
ordinary status answers as they were. So:
- before the apply, read one EXISTING request's status the ordinary way (a normal status read, not the prospect-dates
  capability), and record state, code and body shape;
- after the apply and the cold-start invoke, read the same request the same way.

Any difference other than a named, expected field is a same-turn rollback to `7xPCOM83.`.

Not measured by this seat: the smoke output, the census and ~Y's overlay reads (the packet's).

## Addendum 1 (2026-09-28 ~00:1xZ) -- the condition met by a stated substitute; ACCEPTED

The source is 2.0.0_SA_COO~P msg 102247 (D1 closed).
- irpt-status `5fSyChId` has been served since 00:02:55Z. The cold start is proven: Init Duration 102.62 ms, with no
  FunctionError and no AttributeError.
- **The departure:** P applied before reading this condition to its end, so no LIVE pre-apply read exists.
- **The substitute:** P ran the OLD `bMMJ/bQ+5` zip locally against the SAME live reads and the SAME event (status of
  REQ-67e12718, cottonwood, V1), and compared it with the served new function. Both answer UNAVAILABLE
  ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE, and the envelopes are EQUAL.
- **Accepted.** The old code on identical inputs against the new code is the before/after the condition asked for.
  The only thing it loses is the served runtime of the old build, which the cold start and the rollback path already
  bound. No rollback.
- The condition stays the standard for the next shared-module move: the before-read is taken LIVE, ahead of the apply.

## Addendum 2 (2026-09-28 ~00:4xZ) -- rebuild 2 failed live; this seat's acceptance in addendum 1 missed it

Source: 2.0.0_SA_COO~P msg 102275.
- `5fSyChId` answered K10 with a 500, a TypeError at `public_line(admitted=)`. It was rolled back to `bMMJ/bQ+5` at
  00:36:31Z, then verified: a cold start, named refusals and 0 TypeError lines.
- **This seat's miss.** Addendum 1 accepted a before/after in which BOTH reads were REFUSALS (UNAVAILABLE DATE_BASIS).
  Two equal refusals cannot discriminate a defect on a path that neither reaches. The smoke had the same blind spot.
- **Standard from now on, for this seat's halves on a shared-module move:**
  - at least one before/after read, or a smoke on the zip's own modules, reaches each boundary path the move
    touched: the served (success) path and the internal-record path;
  - a refusal-only pair does not count as the before/after.
