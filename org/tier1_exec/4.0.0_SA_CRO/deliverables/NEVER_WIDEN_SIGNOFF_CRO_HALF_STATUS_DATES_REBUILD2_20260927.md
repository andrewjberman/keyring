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
