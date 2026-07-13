# CVO~B — GATE-2 CLEARED, THEN **RE-OPENED BY ME**, THEN RE-SCOPED. And ten more of my own instruments broke.

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated AoR validation lane, LD-0277)
**window:** 2026-07-13 ~11:35Z -> ~18:10Z (continues `cvo_B_gate2_determination_3_...`)
**commits (8):** `f2ab728b6` · `8e4789fb7` · `191d59d55` · `a2ff8d8ce` · `51da8e035` · `15a1102c1` ·
`7c153343f` · `24ecc9dec` — all pushed to CLOUD.

---

## Summary

Cleared gate-2 (determination #4), then **indicted my own clearance and re-opened it two hours later**,
then **re-scoped it again** when COO proved my arms were fed a basis the run will never read. Nothing
served, switch OFF, chain held twice over, and no gate closed on a green I did not believe.

**The through-line: every substantive finding this window came from a control failing, and roughly half
of them were controls failing on ME.**

---

## 1. GATE-2 DETERMINATION #4 — CLEARED at `59d70b95e` (`8e4789fb7`)

Both withholds discharged against the bar I had **pre-registered before the fixes existed** (3/5 -> **5/5**),
and — the load-bearing half — **the three over-condemnation controls STAYED GREEN.** R2 was confirmed
**independently of me** by base CVO's own falsifier. Battery: 10 live arms, 9 GREEN.

**And I had to correct a scope error of my own to clear it:** determination #3 listed **V4 as a gate-2
withhold**. That was a **category error** — V4 verifies the *first nightly AFTER the switch flips*, so it
cannot be a precondition of a *pre-cutover* gate. **I named it rather than quietly reclassifying it**,
because quietly reclassifying a withhold in order to clear is exactly how a gate stops meaning anything.

## 2. >> THEN I RE-OPENED IT. THE AoR FOLD IS DATE-BLIND. <<

Andrew asked, in passing, why Noel was not in the numbers (he was thinking AUA, and retracted). **The
question was right anyway.** Exercised on the real `apply_resolution_fold`:

```
account 59, servicing=peter_lee, AoR SSOT says noel_soderblom
  2020-03-15  $100,000  ->  noel_soderblom     <- A SIX-YEAR-OLD FLOW, RE-KEYED
  4 of 4 rows re-keyed. $400,000 of HISTORICAL NNA moved to an advisor who never held it.
```
`attach_advisor_key` maps **by `account_id` and has NO DATE COLUMN.** It re-keys the entire history of
every mover. **That is the same defect the time-lock exists to prevent, arriving through the AoR SSOT.**

**I cleared gate-2 on the mechanism, the served-view survival, the DELTA-0, and the movers-only contract —
and I never once asked what the fold does to a 2020 flow.** CLAUDE.md: *"verify findings JOINTLY —
per-finding triage is structurally blind to composition."* **I verified two projects separately while their
policies were opposite.** Gate-2 **RE-OPENED**; CTO~B re-opened gate-1 on identical grounds.

**Andrew ruled:** *"history stays with whoever held it at the time"*, then *"we backfill the first available
AoR."* **My exercise turned out to be CORRECT BEHAVIOUR under the second ruling — a correct call reversed
by a ruling, not a miss.**

**And I saved the redesign:** exercised that **the STAMP *IS* the date-awareness** — `lock AFTER fold`,
stamping the post-fold key, satisfies BACKFILL + NO-REWRITE + FORWARD-ONLY **with the date-blind fold
unchanged.** *"Already stamped" means "already happened."* **The date-aware fold redesign was unnecessary.**

## 3. THE TIME-LOCK BAR — pre-registered, then broken by DS, twice

- **`191d59d55`** — pre-registered the bar **before DS built the fix**, and **rejected 3 of CTO's 4 HARD
  invariants**: every one is a **conservation check, and conservation is invariant under a SWAP**. Proof in
  one line: **8 closed-quarter cells MOVED while `sum(advisors)==firm_total` tied to 0.00.** The
  non-conserved assertion is the property itself — **HISTORY IS IMMUTABLE.** Also rejected the directional
  targets: **a tilde is not an assertion.** COO ratified it as THE bar.
- **DS ran it instead of trusting it and found a blind spot.** The oracle's `as_of` **truncates the quarter
  it was cut in** (`..06-29` vs live `..06-30`) — so my bar gated on **two windows** and never checked
  Q2-2026, **the quarter holding all $709,407.79 of contested money.** It was **fork-BLIND, not
  fork-NEUTRAL**, and I had claimed the latter. **The fix is GRAIN, not a better oracle.**
- **And my own account-grain repair had the conservation trap inside it:** a **named↔named swap nets to
  zero and is invisible to any sum.** I built the fix for the trap and the fix had the trap in it.

**Account-grain v2 reproduced DS's numbers to the cent from a different source** (peter +$1,287,189.93 /
patrick +$818,857.99 / phantom $52,604.80 -> patrick; firm drift **$0.00**). **Two independent derivations,
one answer.**

## 4. LIFT-GATE ITEM 4 (`a2ff8d8ce`) — and the arm nobody built

Both guards verified by exercise, **and the DISJOINTNESS PROVEN**:
```
assert_no_residual_advisor({inflection_wealth_management: $202,062,830.31}) -> PASSED
   THE ENTIRE FIRM COLLAPSED ONTO ONE **VALID** KEY AND EVERY DOWNSTREAM DETECTOR IS GREEN.
   (control: the guard DOES fire on a real residual -> its silence is a real reading, not a dead instrument)
```
**The collapse class is PREVENTED AT SOURCE and DETECTED BY NOTHING.** The `INF_B_00` selector is **not
defence-in-depth — it IS the only thing.** Filed as an open residual, not a covered box.

## 5. >> DS INDICTED MY BAR AND HE WAS RIGHT (`51da8e035`) <<

**Four consumers RE-FOLD the stamped `canonical_nna` AT SERVE TIME** — including `INF_D_00f`, the served
NNA spine. **So the lock could freeze gold perfectly and the served number would still slide, and my
gold-layer bar would have printed GREEN through all of it.**

> **Could my instrument, on that layer, ever have returned a FAIL? No. Then it measured nothing.**

**I wrote the rule that catches this — after C_07 — and then broke it.** C_07 was the fold being **un-done**
downstream; this is the lock being **re-folded** downstream. Same seam, opposite sign. **I did not look for
it because I had already "handled" that class.**

His stamp-aware fix: **attacked with a working mutant**, not trusted. `S2` reproduces the deployed defect
(strip the stamp -> joe handed **$400,000** he never held).

## 6. THE FINAL RE-SCOPE (`7c153343f`, `24ecc9dec`) — COO: *"was your bar fed the basis the run will read?"*

**No.** Verified myself, positive-controlled:
```
accounts_v2: `advisor_of_record_raw` in 0 of 70 snapshots  (control: rep_id present -> the read works)
INF_AOR_FOLD_ACTIVE=1 -> the resolver RAISES. The switch CANNOT be turned on against live silver.
build_advisor_of_record_fold(LIVE) -> fold=0.   (control, injected: fold=628 -> the fn works)
```
> **THEREFORE EVERY FOLD-ON ARM I HOLD IS *NECESSARILY* HERMETIC — not by choice, by construction.**
> **And "164 movers" = `_AOR_MOVERS_*` frozensets (64+64+22+14), read by ONE TEST and NO PRODUCTION CODE.
> A FACT ABOUT A CODE PATH THE RUN DOES NOT WALK.**

Gate-2 #4 **RE-SCOPED, not voided**: structural arms hold; **fold-ON claims are NOT live-verified** and get
re-fed on the 07-14 partition. **On today's basis they are TRUE but VACUOUS — with zero movers, "does the
fold survive to the served view?" has no content.**

## 7. AND THE NUMBER I HAD TO WITHDRAW

I reported **"21 house-AoR accounts would be dropped"** (`KNOWN_ADVISOR_KEYS` omits the house while Andrew
ruled the house IS a valid AoR). **The DEFECT IS REAL AND LATENT. THE 21 WAS AN ARTIFACT OF MY OWN
INJECTION** — I filled the AoR from `representative_name`, and **21 accounts are SERVICED by the house**, so
my injection **manufactured the very thing it then detected.** Real roster, my own positive control
(named-AoR **837**, matching COO and DS): **HOUSE-AoR = 0.**

> ## **AN INJECTED COLUMN IS A HYPOTHESIS, NOT AN OBSERVATION. THE VALUES ARE NEVER EVIDENCE.**
**Third instance today, three agents:** DS's rigged basis · COO's `732` (reality 164 — *it reached an exec
ruling in 90 minutes*) · my `21` (reality 0). **A structural finding does not need a fake number — and the
fake number is what gets it dismissed.**

---

## >> TEN MORE OF MY OWN INSTRUMENTS BROKE THIS WINDOW (#6–#15). NOT ONE CAUGHT BY BEING CAREFUL. <<

| # | defect |
|---|---|
| 6 | the fix-bar turned the **A3 guard doing its job** into a "RED over-condemnation" (`importlib.reload` doesn't reload the transitive dep) — **its "fix" would have DISARMED A3** |
| 7 | an evidence line printed `no output` on **success** (`A or B if C else D` precedence) — **a PASS nobody could check** |
| 8 | the Guard-B driver **guessed a signature**, got `None`, and turned `None != snap` into **"WALKED BACK"** — printed for the healthy controls too |
| 9 | compared **total flows** against **contested amounts** and nearly **accused DS of an error that was mine** |
| 10 | pandas scores `None != None` as **True** -> **"I CANNOT EVALUATE" reported as "THE BRANCHES DISAGREE"**, inflating the fork set 2 -> 7 |
| 11 | `groupby` **silently drops NaN keys** -> the firm total came out **$13,853.17 high**. *The drift line is the only reason I found it.* |
| 12 | the roster-silent rule is undefined if an account has **two** existing keys — the LOCK would freeze a **coin-flip forever** |
| 13 | my census of DS's census scored an **UNKNOWN as a PASS** (default branch = "legitimate") — *only caught because his count said 4 and mine said 3* |
| 14 | probed a firebreak with a **guessed function name** -> `hasattr` False -> **nothing called** -> printed **"NO RAISE"** at rc=0 |
| 15 | a positive control printed `fold=0` next to the label **"the fn CAN return non-empty"** — **the label was a hardcoded string.** *Read the number, not the label you typed next to it.* |

**Running total: fifteen. Every single one caught by a control failing, none by care.**

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `.tools/commit-gate.sh` | PASS (8 runs; 4 ruff blocks fixed) | Caught F541s + a non-ASCII middle-dot before push every time. |
| `.tools/safe-commit.sh -F` | PASS (8) | `-F` throughout — every message carried backticks/`$`; `-m` is an execution vector. |
| `comp-surface-check` (auto) | PASS | Deliverables only, no SEV1 surface. |
| `comp-pipescript deployed` | **BLOCKED** | Refused: `SKIP: opal-data-bd deploy-verify HELD under the sovereign prohibition`. **Correct behaviour** — the tool honoured the 49F hold. Used `head-object` + `boto3` import-check instead. |

**What worked:** the commit gate caught every lint before push; `safe-commit -F` handled 2KB messages with
backticks without shell evaluation.
**What failed:** nothing in the toolchain.
**Gap found (carried from last window, now confirmed):** `subprocess.run(['aws', ...])` from a **Windows
Python** process cannot resolve the `.tools/aws` Git-Bash shim. **boto3 is the only correct answer from
Python.** Worth a line in the AWS-shim doc.

## MCP traffic

**~14 significant** (7 in / 7 out). **IN:** COO ×5 (gate-2 clearance challenge, the fork ruling, the
served-layer finding, the roster-basis challenge, the injection correction) · DS ×2 (the bar blind spot;
the serve-time re-fold) · CTO~B ×2 (gate-1 cleared; lift-gate item 4). **OUT:** determination #4 + the
re-open [STOP] + the time-lock bar + the lift-gate verdict + the served-layer + property/provenance arms +
the roster-basis manifest + the withdrawal.

## Blockers

**None mine.** **CHANGE-3 (silver carrying `advisor_of_record_raw`) is a HARD PREREQUISITE** — the one-shot
cannot run before it lands, and the 07-14 partition is the first real basis that will exist.

## Current State

- **GATE-2 = RE-OPENED, then RE-SCOPED.** Structural arms HOLD; **fold-ON claims NOT live-verified.**
- **Nothing served. `AOR_FOLD_ACTIVE=0`. Chain HELD twice over. `apply_time_lock` CALLED ZERO TIMES.**
- **The one-shot is IRREVERSIBLE** (`the first run's derivation is FROZEN`) -> **my verdict must be rendered
  on a DRY-RUN, before the stamping write, on the SERVED artifact, with the executing run asserted
  BYTE-IDENTICAL to the one I clear.**
- **Open, routed, not mine:** the house/`KNOWN_ADVISOR_KEYS` gap (latent) · the 5-file atomic deploy
  (`ImportError` kills all 7 producers) · the catch-up hazard (*the ledger records WHEN WE NOTICED*).

## Next Steps

- **[me]** on CHANGE-3 landing: re-feed every fold-ON arm on the **07-14 live partition**; render gate-2 on
  the **SERVED artifact**, on a dry-run, byte-identical.
- **[0.4.0_DS_ClientPlatform]** wire `fold_then_lock` into `INF_C_01`; re-point `timelock_preview` at the
  fold-ON path.
- **[1.0.0_SA_CTO~B]** the house/`KNOWN_ADVISOR_KEYS` ruling; the atomic-deploy gate.
- **[2.0.0_SA_COO]** CHANGE-3 sequencing; the lift ledger's open residuals.
- **[Andrew]** the GO. **Nothing in this window authorizes anything.**
