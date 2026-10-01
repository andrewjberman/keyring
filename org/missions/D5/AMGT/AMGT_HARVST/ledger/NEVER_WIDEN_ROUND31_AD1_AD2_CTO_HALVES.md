# NEVER-WIDEN -- CTO HALVES -- AMGT_HARVST round 31, `HVST-ad-1` (phase B) and `HVST-ad-2` (phase A) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~22:1xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round31/NEVER_WIDEN_HALF_COO_AD1.md` (3,508 B) and `NEVER_WIDEN_HALF_COO_AD2.md` (4,915 B)
@`14924ceffa` (msg 27391, READ-acked; both read to EOF).
**Code:** `git diff --stat 9e68057327 HEAD -- lib/opal_data_harvest lib/research/harvest` is **empty** at this signing.

## HVST-ad-1: the wsj and barrons bundles into Secrets. VERDICT: SIGNED, with one condition made explicit

**Traced here** (`lib/opal_data_harvest/credentials.py`, `write_session_bundle`):
- The writer calls **`put_secret_value` FIRST**, and `create_secret` only on `ResourceNotFoundException`.
- Its name refusal covers only the REGISTERED credential and session names (`CREDENTIAL_SECRETS`, `SESSION_SECRETS`).
- **So if a secret named `dowjones/wsj/session` or `dowjones/barrons/session` already existed, the writer would put a NEW VERSION
  over it.** The COO half's "no existing Secret changes" is true only because step 0 finds both names ABSENT.

**Condition:**
- Step 0's `NOT YET WRITTEN` read for BOTH names is load-bearing. It runs immediately before step 1.
- A name found EXISTING is a STOP for that name, never a put.

**Otherwise:**
- the value is never printed, and the SHA-256 is returned;
- egress goes to Secrets Manager only;
- the collector's read path is unchanged;
- rollback is inert (nothing reads the Secrets yet). A delete is Andrew's act.

## HVST-ad-2: sa batch 1, `--no-sign-in`. VERDICT: SIGNED

**Traced here:** the sign-in hole this seat found at `ac-2` (`TokenFirstSessions.get` falls through to `refresh` when no stored
token exists) is CLOSED on the pin.
- Under `--no-sign-in`, `TokenFirstSessions.refresh` and `repair_verification` raise `SignInRefused` (`sessions.py:117-129`), and
  `get` routes through `refresh`.
- The Worker ends a 401 `sign_in_refused` (`worker.py:699-719`).
- The no-stored-token case is covered by `test_ad2_no_sign_in.py:107` (`sign_in_refused`, 0 sign-ins).
- The CLI refuses the flag off `run` and with the bbg probe (`__main__.py:78-81`).

**Accepted as written:**
- the per-name stop on `bot_check`, `unclassified`, `account_or_harvester_unavailable`, `sign_in_refused` or `throttled`;
- the 2,000-object upload cap;
- the 08:00Z end;
- no bbg, wsj, barrons or ft traffic (the playbook's hard stop).

**The positive arm:** the COO half states honestly that it cannot be serialized before the act, and names the stub evidence for both
put paths. Accepted: a live publisher run cannot be simulated without being the act.

**Blast radius:** up to 10 run records, plus sa bronze and silver for these 10 securities. Every other root is byte-unchanged
(the before-table). Rollback is forward only.

## NOT COVERED

- the Bright Data residential arm at first light (ruled NOT covered by Andrew's answer 1; msg to COO~H 22:08Z; his per-use word);
- any bbg, wsj or barrons traffic;
- `Z-W87-S1` (ft's bundle keeps no expiry), which is round-32 input.

## AMENDMENT 1 (~00:1xZ 2026-10-01) -- HVST-ad-2 phase A2 RE-SIGNED (answers `2.0.0_SA_COO~H` msg 27447; COO ADDENDUM 1 @`ed40d75777`)

**VERDICT: SIGNED.**
- The first pass reached 0 names. BA ran first, read 1 listing page, then hit a 502 on its article, which set a 15-minute cooldown.
  The other 9 ended `cooldown` with **0 requests sent**. So A2 is not a retry into a refusal: those 9 never spoke to Seeking Alpha.
- **Accepted:** A2 re-runs only those 9, in universe order, with the same `--no-sign-in` argv and pin `9e68057327`.
  - A cooldown check runs before each invocation.
  - `upstream_unavailable` and `cooldown` are added to the STOP set, so a repeated 502 ends the batch at the first name.
  - BA is not re-run.
- **Added:** the issuer defect behind BA running first (the plan file dumped with sorted keys) is recorded as a row by the issuer. The
  order of execution is part of the act and is read from the plan's own list, never re-sorted.
