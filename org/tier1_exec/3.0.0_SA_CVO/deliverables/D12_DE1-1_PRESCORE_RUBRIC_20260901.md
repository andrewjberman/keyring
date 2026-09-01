# DE1-1 PRE-SCORE RUBRIC -- registered BEFORE the artifact exists

**Author:** `3.0.0_SA_CVO~Z` · **Registered:** 2026-09-01 ~07:5xZ · **Repo HEAD at registration:** `24da55157d`
**World state at registration (measured, `2.0.0_SA_COO~Z` msg 18404):** deployed `opalinvest-auth-handler`
`CodeSha256` == the Act-A build, `LastModified 03:11:25Z`. **Act B NOT applied.** No terraform apply running.

> **WHY THIS IS WRITTEN NOW.** The evidence DE1-1 will be scored against does not exist yet. A rubric
> written after the artifact lands cannot be distinguished from one written *to fit* it. This file is
> the discriminator: it is committed while the deployed sha is still the Act-A build, so every
> criterion below is falsifiable against an artifact nobody has seen.
> **It grades the ARTIFACT, not the outcome. A PASS here is not a statement that the system is safe.**

---

## 1. THE PROPERTY UNDER TEST

> **No OTP code is MAILED to a user before that user opts in.**

⛔ **This is a SERVER fact.** A browser network capture observes what the client *requested*, never what
the mailer *did* -- `0.4.0_DE_ClientPlatform~Z` withdrew the capture as DE1-1 evidence on exactly this
ground (msg 18330), after it was shown that an Act-A send is emitted from inside `/auth/login` and
produces **no browser-visible request at all**.

---

## 2. VALIDITY CONDITION -- checked FIRST, and it is not a footnote

```
REQUIRED   the deployed auth-handler CodeSha256 == the ACT-B BUILD ARTIFACT hash
           (a POSITIVE match against a pinned value, per CLAUDE.md 22a: diff deployed bytes
            against the BUILD INPUT)
```

⛔ **NOT `!= the Act-A build`.** That negative form is satisfied by *any* redeploy -- an unrelated
hotfix, a dependency bump, a rebuild of identical source, a rollback to a third build -- and the
criterion in §3 **false-passes on every one of them**, exactly as it does on Act A. A negative
validity condition opens the gate on the first change of any kind.

**Acceptable substitute if the artifact hash cannot be pinned:** a **content** probe on the deployed
bundle showing `login()` no longer reaches `sendMfaCodeEmail`. That is the property itself rather
than a proxy, and no unrelated redeploy can satisfy it.

⛔ **IF THE VALIDITY CONDITION IS UNMET, THE VERDICT IS `NOT-SCOREABLE`. NEVER `PASS`, NEVER `FAIL`.**
Under Act-A bytes the oracle in §3 reads ABSENT *while a code is in the user's mailbox*.

---

## 3. THE CRITERION

Oracle: CloudWatch logs, auth-handler log group. `account_hash = sha256(trim(lower(email)))`,
**unsalted** -- measured at `mfa.ts:90` and `throttle.ts:66`, byte-identical expressions, so the value
is computable offline and no address appears in any log.

| # | Observation | Required | Role |
|---|---|---|---|
| T0 | `mfa_challenge_issued` for the subject's `account_hash` | **PRESENT** | **ADDRESS CONTROL** -- proves the hash is right and the subject did log in |
| T1 | `mfa_code_rotated` for that hash, **before** the opt-in click | **ABSENT** | **THE PROPERTY** |
| T2 | `mfa_code_rotated` for that hash, **after** the click | **PRESENT** | **POSITIVE CONTROL** -- the instrument can see a send |

**All three from ONE continuous read window.** A late-attached reader manufactures T1's absence while
T2 still passes.

⛔ **T0 IS A GATE, NOT A DATA POINT.** If T0 is absent the read is `VOID` -- it means the address, the
hash or the window is wrong, and **a hash that appears in no log line returns a flawless absence for
free.** The failure is anti-correlated: the more wrong the hash, the cleaner the apparent PASS.

⚠ **If the subject never clicks**, T2 is unavailable in-trace; the **fixture** positive control
substitutes for it. The fixture is *not* redundant -- it is the control for exactly that branch.

⚠ `mfa_code_rotated` is an **UPPER BOUND** on sends (`getUser` may return null at `auth.ts:218`; the
mailer may throw). Present = *attempted*. **Absence is the sound direction, and absence is what the
claim rests on.**

---

## 4. VERDICT LATTICE (MECE over the declared domain; Rule 24)

Domain: *the outcome of one DE1-1 scoring attempt against one submitted artifact.*

| Verdict | Meaning | Moved by |
|---|---|---|
| `PASS` | validity condition met; T0 PRESENT, T1 ABSENT, T2 (or fixture) PRESENT | -- |
| `FAIL` | validity condition met; T1 **PRESENT** -- a send preceded consent | a code fix |
| `NOT-SCOREABLE` | validity condition **unmet** (wrong/unknown deployed vintage) | a deploy |
| `VOID` | validity condition met, but T0 absent or the window is not continuous | a re-run with a corrected hash/window |
| `WITHHELD` | artifact submitted but missing a stated element (no denominator, no vintage, control absent) | the submitting seat amending the artifact |

⛔ **`NOT-SCOREABLE`, `VOID` and `WITHHELD` are three different remedies with three different owners**
(deploy / re-run / amend). Collapsing them into one "inconclusive" bucket loses the routing, which is
the whole point of separating them.

---

## 5. WHAT WOULD MAKE ME SCORE `FAIL` -- stated now so it cannot be negotiated later

A single `mfa_code_rotated` line carrying the subject's `account_hash` with a timestamp **at or before**
the opt-in click, under a met validity condition. **One line is sufficient. There is no threshold and
no tolerance**, because the property is universally quantified: *no* code before consent.

## 6. WHAT I WILL NOT ACCEPT AS EVIDENCE

- A browser network capture, alone -- **structurally blind** to a server-side send (§1).
- A source read of `auth.ts` -- **source != deployed.** `1.0.0_SA_CTO~Z` recorded this trap firing three
  times in one night on this very row (msg 18381): source already had Act B while deployed was Act A.
- An absence with no positive control in the same window.
- `rc=0` from any producer, or a self-report of success.

## 7. BOUNDS

⚠ CloudWatch **retention on the auth-handler log group is UNMEASURED by me** -- it bounds how late the
read may happen and I have not established it.
⚠ The pilot addresses (`andrew@opalinvest.com`, `aj@opalinvest.com`) and their hashes were computed by
`0.4.0_DE_ClientPlatform~Z` and **independently reproduced by me, 2 of 2, both controls passing**. That
confirms the arithmetic. **It does not confirm those are the cohort's actual portal login addresses** --
that lives in `opal-users-v2` and is `0.7.0_AE_CloudOps~Z`'s plane. T0 is what closes it at scoring time.
⚠ **NON-APPLICATION:** this rubric governs DE1-1 only. It says nothing about whether MFA is correctly
enforced (a different row), nor about Andrew's own experience, which is his to judge and not a scored row.

---

# AMENDMENT 1 -- 2026-09-01 ~08:3xZ, BEFORE ANY DE1-1 ARTIFACT EXISTS AND BEFORE ACT C LANDS

⛔ **NOTHING ABOVE IS EDITED. §3 STANDS AS ORIGINALLY REGISTERED** and remains the criterion for any
run against an **Act-B** deployed handler. This section ADDS a form for the post-Act-C world.

## A1.1 Why this amendment is legitimate, stated so the line is auditable

⛔ **The line I am not crossing:** editing criteria to fit an artifact that has ARRIVED is worthless.
**This is the other thing** — the SYSTEM UNDER TEST is being changed out from under the instrument,
and the amendment is written **before** the artifact exists and **before** the change lands.
**If a DE1-1 artifact already existed, I would leave this file alone and score it as written.**

## A1.2 The defect in §3, found by `0.7.0_AE_CloudOps~Z` mid-build (msg 18580), not by me

`resendMfaCode` is the **only** caller of `rotateChallengeCode` (denominator 3 hits / 12 files). Act C
rewrites that path so nothing rotates. Therefore, on an Act-C handler:

```
T1  mfa_code_rotated ABSENT before the click   TRIVIALLY, PERMANENTLY TRUE -- the event is gone.
T2  mfa_code_rotated PRESENT after the click   STRUCTURALLY IMPOSSIBLE.
=> DE1-1 FALSE-PASSES BY CONSTRUCTION, with the positive control unable to fire.
```

⛔ **I named an IMPLEMENTATION EVENT (`rotated`) where the property is AN EMAIL WENT OUT** — the same
class of error I had corrected on this row ninety minutes earlier (`mfa_challenge_issued`, an event
named for the writer's act rather than the property), **and had banked as a lesson in between.**

## A1.3 The amended criterion -- property-level, implementation-independent

Define **SEND-EVENT** := *any log event emitted because an OTP email was actually sent.* On an Act-B
handler that is `mfa_code_rotated`; on an Act-C handler it is whatever Act C emits per email
(`mfa_code_resent` or equivalent), **which the Act C rubric already requires as C5**
(`57dd460e6c` §3 — every email emits a line; an email with no log line is a FAIL there).

| # | Observation | Required | Role |
|---|---|---|---|
| T0 | `mfa_challenge_issued` for the subject's `account_hash` | **PRESENT** | address control (gate) |
| T1 | **any SEND-EVENT** for that hash, **before** the opt-in click | **ABSENT** | the property |
| T2 | **any SEND-EVENT** for that hash, **after** the click | **PRESENT** | positive control |

⛔ **T2 REMAINS A HARD GATE AND ITS MEANING IS UNCHANGED:** if no SEND-EVENT can be observed after a
click that demonstrably sent mail, the instrument is dead and the verdict is `VOID`, never `PASS`.
⚠ **AND THE AMENDMENT INHERITS A DEPENDENCY:** it is only sound if Act C honours C5. **If Act C ships
emails with no log line, DE1-1 becomes UNSCOREABLE on the log plane entirely** — not a `FAIL`, a
`VOID`, and the fix would be C5, not this rubric.

## A1.4 Preferred resolution, and it does not need this amendment

⭐ **Run DE1-1 in the Act-B window, under §3 exactly as first registered.** The deployed handler still
rotates on every send, so T0/T1/T2 are all satisfiable now. **A real run against the untouched
original is worth more than any amendment**, and this section is the fallback if that window closes
first.

---

# AMENDMENT 2 -- 2026-09-01 ~08:5xZ, BEFORE THE CLIENT-HALF ARTIFACT EXISTS

⛔ **NOTHING ABOVE IS EDITED.** This tightens **the window requirement**, which was under-specified in
a way that fails toward PASS. Forced by a measurement in `0.7.0_AE_CloudOps~Z`'s F-8 run (msg 18683
§4) — **found by accident while running a different experiment.**

## A2.1 The measured skew

```
client recorded  end = 2026-09-01T08:51:48.767Z   (after the verify response returned)
Lambda stamped   that same request  08:51:49.060Z
```
**A response cannot precede its own log line, so these are two clocks: server stamps run ≥293 ms
AHEAD of that client's.**

## A2.2 Why the original requirement was unsound

My artifact requirement (msg 18632 item 2) said only *"record explicit start/end UTC."*

> ⛔ **A window taken from the BROWSER and applied as a filter to SERVER log stamps has edges wrong by
> roughly a third of a second, IN THE DIRECTION THAT EXCLUDES A REAL TRAILING LINE.** T1 is an
> **absence** claim, so a wrongly-excluded send line reads as **PASS**. The under-specification fails
> toward the verdict nobody would question.

## A2.3 Amended requirement -- binding on any DE1-1 run

✅ **Take the window bounds FROM THE LOG STREAM ITSELF**, or widen browser-derived bounds by a
measured skew margin. ⛔ **Never filter one clock's stamps with another clock's bounds.**
⭐ **Stronger still, and already demonstrated achievable:** bracket the absence **between two OBSERVED
log lines in the same slice** (F-8's run did exactly this — T0 and T2 bound each gap). **A bracketed
absence needs no window arithmetic at all and cannot be manufactured by a clock error.** Prefer it.

## A2.4 Scoring record for the SERVER half (this rubric's §3, original text)

```
CONTROL  challenge 2   T0 08:51:45.280 PRESENT · T1 897 ms EMPTY · T2 08:51:46.177 PRESENT
SUBJECT  challenge 1   T0 08:51:48.257 PRESENT · T1 380 ms EMPTY · T2 08:51:48.637 PRESENT
account_hash  f9a9cc07…  -- matches this seat's independent offline computation exactly
```
✅ **SERVER HALF: PASS, twice independently** (`0.7.0_AE_CloudOps~Z` msg 18683, scored in msg 18696).
⚠ **BOUNDS ON THAT PASS:** (i) T1 is an absence and rests on the log query's completeness, which is
internally corroborated but not independently established; (ii) ⛔ **the run called the API directly —
NO UI, NO CLICK.** The server property is identical, but **the UI path is UNTESTED and DE1-1 is NOT
closed.** The client half remains `0.4.0_DE_ClientPlatform~Z`'s and unrun.
