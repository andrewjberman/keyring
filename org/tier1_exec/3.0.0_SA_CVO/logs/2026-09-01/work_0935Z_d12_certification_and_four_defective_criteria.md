# 3.0.0_SA_CVO~Z — D12 W3 certification, and four of my own criteria that were wrong

**Window:** ~07:10Z–09:35Z, site Z · **Seat:** `3.0.0_SA_CVO~Z` (NFRA verifier, reports MSTR, LD-0325)
**Subject:** D12_PLATFORM_OPS W3 — email-OTP opt-in (Act B), idempotent send (Act C), DE1-1, F-8.

---

## 1. WHAT WAS CERTIFIED

| Row | Verdict | Evidence |
|---|---|---|
| **DE1-1** (no code mailed before opt-in) | **PASS, both halves** | server half twice independently (F-8's run); client half on the PROD build at the PROD origin |
| **W3 Act C** (idempotent send) | **PASS 6/6, exercised** | deployed plane, 3 clicks → one code, cap intact |
| **F-8** (rotation binding) | **NO DEFECT** | superseded code 401, `reason=wrong_code attempts=1` |

**Pre-registered rubrics, both committed BEFORE the code existed** — which is the only reason the
PASS verdicts mean anything:
`ef3ec6f019` (DE1-1) · `57dd460e6c` (Act C) · amendments `f161939dd3` `52cb108bab` `2f09e4b27d`
`adf440f0b6` · findings `0878b4ffc5`. **All 7 ON ORIGIN** (`is-ancestor`, both controls).

---

## 2. ⛔ THE MAIN LESSON, AND IT IS AGAINST THIS SEAT

**FOUR of my criteria were defective, in BOTH directions, and the BUILDER (`0.7.0_AE_CloudOps~Z`)
found every one.**

```
DE1-1 T1/T2 on `mfa_code_rotated`   Act C deletes the event -> would FALSE-PASS with its own
  (an IMPLEMENTATION event)         control unable to fire.                    -> false PASS
Act C C2 "sends == N"               two-sided test, ONE-sided invariant.       -> false FAIL
Act C C4 "total emails == MAX"      no read-timing clause; CloudWatch lags     -> false FAIL
"record explicit start/end UTC"     browser window vs server stamps, 293ms     -> false PASS
```

⭐ **The directions are the finding.** A false-FAIL criterion is challenged by the seat it accuses,
so it surfaces. **A false-PASS criterion is challenged by nobody.** I would never have found #1 or #4.
⛔ **And pre-registration makes this WORSE:** it freezes criteria written by one seat alone, before
anyone has seen the system, and makes every later fix look like cheating. **The discipline that
protects the verdict also protects the defect.**
✅ **REMEDY FOR THE NEXT SEAT: send the rubric to the graded seat FOR REVIEW in the window between
registering it and the artifact existing, and say that finding a hole in it is the point.**

---

## 3. ⭐ THE NIGHT'S RECURRING DISEASE — four instances, one estate

```
mfa_challenge_issued  ISSUING   read as MAILING       CodeSha256 MOVED  CHANGED   read as IS-ACT-B
mfa_code_rotated      ROTATING  read as SENDING       resend:true       UNSEALING read as REPEAT-CLICK
```
**A field named by the writer for what the writer just did, read as the property.** Only the
`CodeSha256` one was caught before use — because the reader wrote the two claims side by side
(*"a sha that moved proves NOT-Act-A; it does not prove IS-Act-B"*) and then read the deployed bytes.
⭐ **The habit: write what the name literally asserts, write what you want to conclude, check they
are the same sentence. They almost never are.**

---

## 4. REUSABLE INSTRUMENT NOTES

- **A push-state claim must be a MONOTONIC PREDICATE, not a snapshot** (`0.7.0_AE_CloudOps~Z`).
  `origin/X = <hash>` is stale on arrival — the head moved twice in ~4 minutes tonight.
  `C is-ancestor of origin/X` survives the trip. **CLAUDE.md's prescribed form quotes the hash,
  which is the perishable half.** ⚠ Monotonic only absent history rewriting.
- **THREE seats got push state wrong, all UNDER-stating.** Relay, relay, and (mine) a true
  measurement repeated in a later report **without re-reading — a measurement wearing the grammar of
  a permanent fact.**
- **An absence needs a bracket, not a window.** F-8's T1 gaps were bounded on BOTH sides by observed
  log lines — a bracketed absence cannot be manufactured by a clock error or a dead reader, and needs
  no window arithmetic. **Prefer it to any start/end-UTC scheme.**
- **A shared fixture whose `account_hash` is a pure function of a WELL-KNOWN address**
  (`success@simulator.amazonses.com`) collides by construction with any other test that ever used it.
  The recorded window is the only separator.
- **`grep -c` on a minified bundle counts LINES.** Every such reading is PRESENCE, not multiplicity.
- **A citation of a measurement is not a second measurement.** Two seats quoting one census are one
  instrument.

---

## 5. OPEN AT HANDOFF

⚠ **LD-0319 parity (mine, non-D12, NO DISPOSITION):** `ont-rulebank-version-current` counts **demo
tenants and its own negative-control fixture** as stale `/system` representation; its desc is frozen
at *"live version 1.2"* while the runtime measures **1.8**; and its detail line emits verbatim the
wording its own desc retracts as false. Reported msgs 18386/18387. **Surfaced, not chased.**
⚠ **F-9** (Act C legacy-mint = dead code, record-for-removal) and the **two build-tooling items** —
`build-nodejs-lambda.sh` cwd-mount failure, and its "Next steps" block that walks an operator into a
`comp-tagauthz` false block whose obvious workaround is `TAGAUTHZ_OVERRIDE`. **All unowned, INERT,
still in the tree** — `findings/2026-09-01_d12-w3-surprise-items_received.md`.
⚠ **F-10** scope corrected to: *a refresh token binds to EMAIL, not the row; deletion makes it inert,
RE-CREATION on that email makes it live again against a NEW identity.* The 7-day figure is
**inherited, not measured by me.**
⚠ **A vite dev server is LISTENING on 5199 (pid 16976).** Started in this window for the RED/GREEN
capture work, which was later withdrawn as DE1-1 evidence. **Ownership not re-confirmed — ~6 seats
share this box, so it was NOT killed.** The `portal-red` worktree is already gone.
