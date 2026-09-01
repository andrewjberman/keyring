# 1.0.0_SA_CTO~Z -- D12 built and accepted, the principal locked out of PROD, and a criterion that moved surface while getting stricter (2355-0147Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE

**Seat:** `1.0.0_SA_CTO~Z` (lane ~Z; base folder, lane named in title)
**Window:** 2026-08-31 23:55Z -> 2026-09-01 01:47Z. Prior log `e91772cfb6` covered 1800-2355Z.
**Device:** site Z. Grew to 5 seats in-window (MSTR~Z, CTO~Z, COO~Z, AE_CloudOps~Z, CVO~Z re-seated).

---

## Summary

D12's backend went from cut to accepted. It then **locked Andrew out of production**, because every
acceptance criterion tested an API and none tested a human. Diagnosed, cleared, and the frontend
series authored and issued. Four instrument defects surfaced; **two of the false readings were mine.**

---

## Andrew-direct in-window (4, all recorded verbatim @`9002122e63` parts D/E + relays)

| ~Time | VERBATIM (first clause) | Effect |
|---|---|---|
| 00:4xZ | "Both the password reset and the otp code ... came to top of inbox no junk" + 4 more | W1-10 CLOSED; 5 calls ruled |
| 00:5xZ | "All of these functions should be noreply ... i want to test it with a few people first" | repoint authorized on a NEW basis; named pilot |
| 01:2xZ | "COO needs to just write a TO series of frontend ui tasks ... and then spawn them" | DE series authorized |
| 01:3xZ | "sure we can do 0.4.0_DE thats fine" | serial ruled |

⭐ **HE VOLUNTEERED THE FACT THAT FALSIFIED MY OWN CALL.** My open-call card asserted the
password-reset mailer was BROKEN. He replied that he had received one. Measured after: the auth role
carries **two** SES grants -- one conditioned on `FromAddress=noreply@`, and a **second, unconditioned**
one. IAM is a union of Allows with no Deny, so `support@` was never blocked.
**The real defect is the inverse:** an intended sender restriction that constrains nothing -- and the
fix I had put to him would have resolved a symptom that did not exist while burying it.

---

## Delivered

| Artifact | Commit |
|---|---|
| D12 cells 2.3 + 2.4 (SES readiness PASS / deliverability FAIL-as-was) | `db29f8a2e5` |
| Andrew-direct record, Parts D + E | `9002122e63` |
| W1 acceptance (10/10) and W2 acceptance | msgs 17271-17273 |

**W2 (`noreply` repoint + the `Limit:1` fix) accepted on evidence spanning TWO RUNGS** -- COO~Z and I
both read source, which is the SAME rung twice; the AE seat censused the RUNNING BYTES. Acceptance
states in itself that **the IAM defect is NOT closed by it.**

---

## ⛔ The production lockout -- the central event

Andrew enabled-and-tested MFA on his own account per his B.3 gate. It worked: challenge issued on his
real account, code delivered. **He could not complete the login.** `mfaRequired`/`mfa/verify` in
`portal/src` = **ZERO** (positive control: 10 auth files in the same tree). **There is no challenge UI.**

⭐ **WHY W1 COULD BE AN HONEST 10 OF 10 AND THE FEATURE UNUSABLE:**
```
PRD WS-2 exercise : "cannot reach the DASHBOARD without a live code"   <- BROWSER outcome
W1-3 as scored    : "no accessToken, /auth/me 401 before, 200 after"   <- API outcome
```
Both true; the second does not establish the first. **The frontend disappeared in that translation.**
⭐ **AND THE CLAUSE THAT MOVED THE SURFACE WAS ADDED TO RAISE RIGOR** -- COO~Z's own diagnosis: it
wrote *"exercised end to end AGAINST THE DEPLOYED HANDLER"* to strengthen the criterion, and that
relocated the test surface while the word "dashboard" stayed in the text.
**Three seats each named a different half and none hid behind another's:** the PRD-to-TO narrowing
(mine to catch), scoring `/auth/me` against "dashboard" without labelling the stand-in plus never
opening `portal/src` (AE), and the rigor clause (COO). Banked:
`a-rigor-clause-can-relocate-the-test-surface`.

**Cleared at 01:19Z** by the AE seat reverting its own write -- **against a live ruling of mine.**
I had ruled the remedy was "his word to give". **I withdrew that and ruled the revert correct:** a NEW
change to the principal's account needs his word; **REVERTING YOUR OWN change that removed his access
is restoration, not a new act.** The asymmetry settles it -- wrong that way costs a line in a thread,
wrong my way costs the principal production access while agents discuss authority.

---

## Compiler Tools

| tool | why | result |
|---|---|---|
| `.tools/aws` sesv2 / iam / dynamodb / logs | cells 2.3/2.4, the IAM two-grant finding, the reset trace | PASS |
| `mcp opal-gateway` mail read | traced the 00:19Z reset email on Andrew's explicit authorization | PASS -- decisive |
| native `Grep` over `portal/src` | the missing MFA UI | PASS with control |
| `comp-find` | serial verification | PASS (0 vs 1,036) |
| directory `ls` on `task_orders` | pre-flight second instrument | **FAIL -- wrong container, see Errors** |

**What worked:** reading Andrew's mailbox once he authorized it. The emails were addressed *"Hi D12
MFA Test"* -- a **deleted test account carrying his live email address** -- which explained the whole
false bug report in one line and no log query could have.

**Gap found:** `--assignee` **UNDER-matches** when `issued_to` carries prose rather than a bare serial
(banked 08-25, surfaced by MSTR~Z). The earlier defect was an OVER-match, which cannot produce a false
zero; **this one can**, so every "lane is clean" pre-flight tonight is weaker than reported. Unowned;
NOT patched mid-round.

---

## Errors -- two mine, both corrected in-window

1. ⛔ **"No `forgot-password` call at all"** -- from a log filter of `"reset"`, which **cannot match
   `"forgot-password"`.** The probe was structurally incapable of finding what I declared absent.
   There was one, at 00:18:50Z.
2. ⛔ **"The `~Z` lane is clean by construction"** -- FALSIFIED. Lane TOs live FLAT in the base folder;
   11 base files reference `~Z`, 22 occurrences. **I applied a sound prescription to the wrong
   CONTAINER.** Right where the base folder is empty (CVO); worthless where it is populated (DE).
   Retracted to four seats before anyone acted on it.
⭐ CVO~Z found the deeper form independently: **a positive control proves the ENGINE, not that your
SUBJECT'S PATH resolves.** Two controls fired against valid paths while the subject's path
(`tier2_senior/3.0.0_SA_CVO` -- CVO is tier 1) did not exist. *"The controls firing is precisely what
made the zero look earned."* Banked into `positive-control-proves-the-engine-not-your-pattern`.

---

## Blockers

**None.** Two items are EVENT-GATED, not awaiting anyone: the pilot cohort and re-enabling MFA both
wait on the DE frontend, and enabling any account before it would lock that user out.

---

## Current State

- **D12 EXECUTING.** W1 + W2 accepted. Backend MFA built, deployed, exercised; **no login UI.**
- **DE series** `12421cc00d` -- DE1 opt-in prompt (no code sent before the click), DE2 challenge
  screen, **DE3 the browser end-to-end as its OWN TO with its own proof row** so it cannot be
  satisfied by a passing proxy. Issued to `0.4.0_DE_ClientPlatform~Z` on his ruling.
- **MFA OFF fabric-wide** -- 0 of 48 accounts gated, verified on my own read at 01:20:10Z.
- **OPEN, no owner:** the unconditioned `ses-send-email` Allow defeating the `FromAddress` condition.
  I ruled it should be scoped/removed, as its own AE cell when the frontend is moving -- NOT tonight,
  NOT inside the DE series, and W2's acceptance already records that it is unclosed.

---

## Next Steps

- **[`1.0.0_SA_CTO~Z`]** score **AC4** on `gold/holding/date=2026-08-31` after the
  **2026-09-01T13:00Z** fire (~11h). Laptop MSTR holds named fallback. Needs no peer.
- **[`0.4.0_DE_ClientPlatform~Z`]** DE1-DE3. **DE3's acceptance is a human in a browser** -- an API
  response is explicitly not acceptance for it.
- **[`2.0.0_SA_COO~Z`]** size the DE seat's Sec-9 bar from a ROW READ, not `--assignee` -- the AE
  seat's own bar proved wrong in BOTH directions (16 open, not 10; 2 of the named 10 no longer open).
- **[ANDREW, event-gated]** the pilot cohort names, and re-enabling MFA -- both after DE3 passes.
- **[open, unowned]** the `--assignee` under-match; the IAM two-grant defect.
