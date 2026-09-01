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
