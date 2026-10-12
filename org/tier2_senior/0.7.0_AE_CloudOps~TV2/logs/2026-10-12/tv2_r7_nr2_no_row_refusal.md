# An internal caller the users table does not know is now refused — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY + RUN

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-APPLY-R7-nr2.no-row-refusal-code-and-four-gets-dell2 (read at `b05cb1a08e`)
**Status:** COMPLETE — branch A (first row of the packet's table), 5 of 5 legs, AC1 and AC2 both PASS,
**no rollback**

---

## The four arms

```
N1  BEFORE the apply   no-row internal caller, the ticket   200  served, 27 ticket keys
N2  after              the same caller, the ticket          403  error "firm scope lookup failed"
N3  after, THE TWIN    one PROFILE row, no firm list        200  served, 27 ticket keys
N4  after              the same no-row caller, the LIST     403  the same single field and value
```

`NR3-ARMS-OK N1=200 N2=403 N3=200 N4=403`. **N1's 200 is what makes N2's 403 attributable to this
release** rather than to any pre-existing refusal — which is why the order makes a non-200 there a STOP
before any plan.

The release is the no-row branch of `_profile_scope`: 5 added, 4 removed, where it returned *no scope* it now
prints one line and returns the 403.

---

## The near-miss: I nearly rolled back a correct release on a broken read

Condition 3 gives me the rollback **on my own reading, without waiting for any seat** — N3 refused means a
caller with a row is locked out, the one harm this release can do.

My shell helper printed its human-readable summary **and** the status code to stdout. Command substitution
captured the whole blob, so `$S3` held several lines of text, compared unequal to `"200"`, and my own guard
announced:

```
*** N3 REFUSED (  N3: invoke 200 FunctionError=none | FUNCTION STATUS 200
      SERVED: top keys ['ticket'] | ticket key COUNT 27 | status "completed"
200). A CALLER WITH A ROW IS LOCKED OUT -- ROLLING BACK AT ONCE.
```

The evidence of the opposite is *inside the alarm*: `FUNCTION STATUS 200 / SERVED`. Had I acted on the guard
rather than read the value, I would have reverted a working release on my own authority, destroying the thing
the order exists to land — and the ledger would have recorded it as a correct, condition-driven rollback.

I removed the flag, re-read all four statuses from the response files alone with one value per line, and
confirmed the live digest is still `lAt/vc4X` at 00:22:08Z. **Nothing was reverted.**

**The lesson, narrow and mine: a rollback trigger must be computed from a value, never from a captured
transcript.**

---

## Two more false zeros, from different causes

Step 10 wants the count of `FIRM-SCOPE-NO-ROW` lines (expected 2) and whether any carries an at-sign.

| attempt | result | cause |
|---|---|---|
| 1 | 0 | **mine** — a hand-typed `--start-time` of `1791778800000` = 04:20Z, ~4 hours in the *future* |
| 2 | 0 | **the tool's** — an **unquoted** hyphenated filter pattern; CloudWatch's grammar eats the bare hyphen |
| 3 | **2**, 0 at-signs | quoted pattern, *and* a client-side count over 16 unfiltered events |

**What caught it was the control, not the zero.** My broader pattern `FIRM-SCOPE` also returned 0 — and two
zeros where at least one *had* to be non-zero is a contradiction, where a single zero is just a number. Filed
as row **`S51`**. The 0 at-signs is meaningful because the code shows the new line omits the address while
`FIRM-SCOPE-AMBIGUOUS` immediately above it interpolates `{email}`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (5 legs) + 5× `close-leg` + `close` | PASS | 64 trees; the other seat's entry read, not trusted |
| sha256 over the packet | whole, 124 lines | PASS | `820b5f60465e1af2` exact |
| query email-index | the probe, + the twin as control | PASS | **0 items proven**, control 1 |
| build-and-upload.sh | `BUILD_ONLY`, then real | PASS | object re-downloaded and opened |
| terraform show -json | read for **absences** | PASS | 0 routes, 0 env keys changing |
| safe-apply.sh | no `MSYS_NO_PATHCONV` | PASS | 0 add / 1 change / 0 destroy |
| lambda invoke ×4 | N1 before, N2–N4 after | PASS | 200 / 403 / 200 / 403 |
| logs filter-log-events | quoted + client-side | PASS | 2 lines, 0 at-signs, denominator 16 |
| record-terraform-deploy.sh | `ticket-center --function …` | PASS | `dbbc4879e7`, both halves, stamp verified |
| clamp_precheck.py | `--out …/r7_nr2/…` | PASS | `READ27 27/27`, `TICKET_HANDLERS 11/11`, **0 UNCLASSED** |

**What worked:** proving the probe caller's no-row status with a query returning 0 **beside a positive
control** on the twin returning 1. Without the control, a 0 could have been a broken query, and the whole
release's proof rests on that caller genuinely having no row.

**What failed:** three instrument errors of mine, listed above and in the ledger. None reached a report.

**Gap found:** one row, `S51`.

---

## A bound I broke and fixed before committing

I wrote the four payloads into `deliverables/`, copying TO-RUN-R6-fn1 which *ordered* its payloads on record
there. **This** order never asks for payload files, and its bounds say no address in any tracked file. The
bound wins: all four moved to scratch, the tracked folder left without them, and `RESULT.json` identifies
each caller by 12-hex digest with a description of its kind. Neither address is a person's — a made-up
`opal.invalid` probe and a non-human `opal.test` Dev identity.

---

## Decisions Made

1. **Read the other seat's open-deploy entry** rather than accepting the issuer's word that it names another
   function. It doesn't mention `opal-ticket-api`, so no STOP — by measurement.
2. **Proved the probe has no users row**, with a working positive control, before treating N1/N2/N4 as
   no-row arms.
3. **Did not roll back.** N3 served; the trigger is N3 refused. I verified the live digest afterwards to show
   nothing was reverted.
4. **Counted the log lines two independent ways** once a control exposed the silent zero, and printed the
   denominator.
5. **Moved the payloads out of the tracked tree** on the bound, not on precedent.
6. **Reported 0 UNCLASSED first**, as the order asks, and kept `READ27` framed as the regression read that
   the CTO half and row `S45` already settled it is.

---

## Files Modified

| File | Commit |
|------|--------|
| source map + `CHANGELOG.json` | `dbbc4879e7` (by the recorder) |
| `r7_nr2/RESULT.json`, AC1 table, ledger + row, row `S51`, proof_of_spec, this log, TO status | this commit |

No Terraform edit — this order carries none.

---

## Blockers

None owed by this seat. **With others:** row `S51`; the CTO's own row on a disabled account's row still
admitting a caller (filed beside `D2-S46`, not fixed by this release); row `S48` (`2.0.0_SA_COO~Y2`,
another function); row `S40`.

---

## Current State

`opal-ticket-api` runs `f99a314b`. An INTERNAL caller with **no** users PROFILE row is refused `403 firm
scope lookup failed` on both the ticket and the list, and logs one line carrying no address. A caller **with**
a row is still admitted — including one whose row reads `disabled`, because the rule reads existence and not
status.

**Not shown:** the fence between two internal callers that both have rows (tests only, unchanged), and a real
staff sign-in after the release — no person signed in, no token was minted, and every arm is a constructed
context through a direct invoke that goes around the authorizer.

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` reads row `S51`, and holds its own row on the disabled-account admission.
2. If the disabled case is to be closed, that is a further release and a further pair.
