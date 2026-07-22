# /verify -- comp-iam APPLIED plane + live-primary flip (0.8.0_AE_CloudComp)

**Verifier:** `3.0.0_SA_CVO` · **Date:** 2026-07-22 · **archetype:** VALIDATE
**Trigger:** Andrew-direct ~1945Z ("address a /verify on 0.8.0 work"). Discharges the verify-on-land
reserved in my own design brief §9 (`COMP_IAM_APPLIED_PLANE_DESIGN_BRIEF_20260720.md`).
**Range verified:** `c490ee017^..2901f1fc9` (9 commits). **Baseline HEAD fixed BEFORE reading their
artifact:** `2901f1fc9`.

**INDEPENDENCE:** per Andrew's ruling @2901f1fc9 -- *"a verifier handed the builder's evidence is
checking arithmetic, not truth"* -- I generated my OWN census and did not read theirs. All evidence
below is my own run against live AWS (account 313476888478, `arn:aws:iam::313476888478:user/Andrew_Berman`).

---

## VERDICT: BROKEN@MECHANICAL + BROKEN@DECLARATIVE · SEMANTIC PASS

**The §9 reservations themselves PASS.** Four findings, all **P1**, none of which make today's output
wrong. The core -- the §5.1 fail-closed vintage gate on `reconcile` -- is SOUND and independently
proven **including its accept side**, which is the limb the builder reported as nearly shipping unproven.

---

## AXIS 1 -- MECHANICAL: PASS on the reserved items, 2 defects at the edges

**Generator (exercised, live):** `comp-iam refresh-census` -> 205 roles / 1 group / 6 users in 15.1s,
one API call (`iam:GetAccountAuthorizationDetails`). **My independent population = 205, identical to
their reported 205.** Population reproduced, not accepted.

**The discrimination pair, on IDENTICAL CENSUS BYTES with only `_meta.generated_utc` varying** -- a
sharper control than the builder's unit suite, because it removes every other difference:

| mutant of MY census | verdict | exit |
|---|---|---|
| fresh (`2026-07-22T19:44:11Z`) | FRESH | **1** (reconcile performed) |
| `generated_utc` removed | NO_VINTAGE | **3** REFUSED |
| `generated_utc` = `"not-a-date"` | NO_VINTAGE (fail-closed) | **3** REFUSED |
| `generated_utc` = `2026-06-03` (age 1181.0h) | STALE | **3** REFUSED |
| **`generated_utc` = `2026-07-24` (age -48.0h)** | **FRESH** | **1** -- **F1, see below** |

**Exit-code contract CONFIRMED distinct** (0 clean / 1 drift / 2 unreadable / 3 refused). The refusal is
**970 bytes on STDOUT**, not stderr-only -- the comp-constants "REFUSE with empty stdout reads as a pass"
residual is genuinely not re-introduced.

### >> F1 (P1) -- A FUTURE-DATED CENSUS READS FRESH: THE GATE HAS AN UNAUDITED BYPASS EASIER THAN ITS AUDITED ONE. <<
`comp_iam_census.py:100-109 @2901f1fc9`: `return (FRESH if age <= ttl_hours else STALE), age`.
A negative age passes trivially, and **the more the date is pushed forward, the fresher it reads** --
so an arbitrarily old census is made authoritative by editing one field.

The gate refuses a census that *cannot date itself* (NO_VINTAGE) but accepts one whose date is
*impossible*. **Those are the same epistemic state -- the timestamp carries no information -- given
opposite verdicts.** The declared verdict set `FRESH | STALE | NO_VINTAGE` has no cell for "impossible";
the state space is under-enumerated.

**Why this matters beyond clock skew:** the honest bypass (`--allow-stale-census`) is audited and prints
*"NOT an APPLIED-plane authority."* The one-field edit is silent, unaudited, and yields a verdict
indistinguishable from a clean run. **A control whose bypass is cheaper than its override channels
behaviour toward the bypass.**
**Fix:** treat `age < -<small skew tolerance>` as a refusal class of its own. Fail-closed, consistent
with the gate's own stated doctrine. `grounding: SOURCE-CONFIRMED comp_iam_census.py:100-109
@2901f1fc9` + exercised (m1_future -> `age -48.0h [FRESH]`, exit 1).

### F2 (P1) -- `comp-iam live --census` APPLIES NO VINTAGE GATE AT ALL
`census_freshness` is called at `iam_cli.py:1043` (`cmd_reconcile`) only. `cmd_live` reads `--census`
at `:784-802` / `:848-852` with a bare `json.loads` and no freshness call. **Exercised:** `live --census
<undated 06-03>` and `live --census <future-dated>` both proceed, exit 1, **no provenance line for the
census, no vintage statement, no refusal.** Two census-overlay surfaces, one gated, one open.

**HONEST FALSIFICATION OF MY OWN HYPOTHESIS -- recorded because it cuts against my finding.** I
predicted the ungated door would SUPPRESS findings. **It did not.** Measured: `live --census <fresh 205>`
-> `!! 12 role(s) live but ABSENT from the graph`; `live --census <stale 111>` -> **the same 12**. The
111-role census is a subset containing the same 12. **No suppression occurred on today's data.**
What IS wrong is the printed denominator: the stale run reports `population cross-check: graph 193 vs
census 111`, inviting the reading that the graph over-enumerates by 82, when against a live population
of 205 the graph **under**-enumerates by 12. **The gate gap is real and confirmed; the specific harm I
expected is not present, and the coincidence that saves it is not a property of the design.**

---

## AXIS 2 -- DECLARATIVE: FAIL (2 drifts)

### F3 (P1) -- THE DOCSTRING CLAIMS A MITIGATION THAT DOES NOT EXIST
`comp_iam_census.py:103-104`: *"A future-dated census is treated as FRESH by age arithmetic but is
**flagged by the caller's provenance line** (negative age prints and is visible) **rather than silently
accepted** as very fresh."*

**Measured, and the claim does not hold:**
- the line prints `(age -48.0h, TTL 24h) **[FRESH]**` with **no `!!` marker** -- contrast the undated
  case, which DOES emit `!! This census cannot date itself`. The loud marker exists; it is not applied here.
- the machine-readable contract (**exit 1**) is byte-identical to a clean reconcile.

**"Visible to a human who reads the line carefully" is not a flag, and it is not a control -- it is
care.** The record describes a safeguard one strength above the implementation. That is the
declarative-drift class this whole build exists to remove, appearing in the build's own docstring.

### F4 (P1) -- TIER-SEPARATION DISCLAIMER PRESENT ON `live`, ABSENT ON `reconcile`
The §9 item I reserved. **Exit-code contract holds; the disclaimer does not.**
- `comp-iam live` prints: *"NOTE: DETECTOR, not an oracle. No Deny/boundary/condition/SCP evaluation.
  For an allow/deny verdict use `comp-iam simulate` (Rule 22a)."*
- `comp-iam reconcile` prints **no such note** -- while using authorization-shaped language:
  `DRIFT-LIVE-ONLY ROLES (47) -- granted live but ABSENT from Terraform`, `over-perm`, `live-only action`.

`reconcile` evaluates **no Deny, boundary, condition or SCP**. So *"granted live"* is a statement about a
census statement, **not** an authorization fact -- a role carrying an Allow behind an explicit Deny or a
permissions boundary is reported as "granted live." **This is precisely the collapse my brief §3 named:
"Never let the census-overlay masquerade as an allow/deny verdict."** The safeguard was written for the
newer surface and not back-fitted to the older, more-quoted one. Cheap fix: print the same NOTE.

### NOTE (P2) -- handoff cites `tests/test_iam_census_vintage.py`; actual path is
`org/modules/graph/tests/test_iam_census_vintage.py`. Does not resolve from workspace root.

---

## AXIS 3 -- SEMANTIC: PASS

- **Census content correct + denominator-honest.** `_meta` carries `generated_utc` / `account` / `api`;
  `scope` self-states *single-account*, `accounts_swept=1`, and that attached-managed policies are
  **recorded UNRESOLVED, never treated as absent**. My §8 assigned multi-account enumeration to
  CTO/CloudOps and **they did not invent it** -- the census says single-account rather than implying
  estate coverage. That was the specific false-clean risk and it is closed.
- **Reconcile magnitudes sane:** live 205 / TF-parsed 162 / matched 158 / 47 live-only (predominantly
  `AWSServiceRoleFor*`) / 5 live-only-action / 0 over-perm.
- **Builder suites reproduce independently:** census self-test all-pass; `pytest` 5/5.

---

## MY PLANE-3 HAZARD: NOT PRESENT -- AND THE GUARD IS STRONGER THAN THE BUILDER CLAIMED

They wrote: *"I built no simulate wrapper. `cmd_simulate` is untouched."*
**VERIFIED:** every hunk in `c490ee017^..2901f1fc9` on `iam_cli.py` is a pure insertion (`-N,0`); none
falls inside the 537-745 simulate body.

**And better than stated** -- the pre-existing `cmd_simulate` already implements the exact discipline I
flagged: `ResourceArns=[arn]` one ARN per call (`:597`), `ContextEntries` passed when present (`:597`),
the positive control run as a **separate invocation** (`:620`, `:656`), and a self-test that asserts
`len(ResourceArns) == 1, "wrapper must never batch ARNs"` (`:698`). **So the hazard is not merely
absent-because-unbuilt; the guard exists and is test-enforced.** My mutant test remains the right gate on
whoever extends it, but it is not owed today.

---

## ROUTING (verify-not-fix)
**F1, F2, F3, F4 -> `0.8.0_AE_CloudComp`** (owner/builder). **F1 + F4 are the two I would land before
`comp-iam reconcile` is quoted as an APPLIED-plane authority** -- F1 because a control with a cheap
unaudited bypass is not yet a control, F4 because the surface most likely to be quoted is the one
missing the not-an-oracle guard. **None is P0: no current output is wrong.**

## RESIDUAL / NOT VERIFIED BY ME
- **Their items 3 and 4 (D4 scope-exclusion suppressing 12 findings; "no cadence (event-driven)" vs
  `_provenance.py:405` "runs hourly")** -- NOT reached this pass. Both are live open questions and I am
  not implying they are clean.
- **`comp-aws derive --classes iam` flag rejection** -- reproduced as reported, not diagnosed.
- **Zero `source=incremental` IAM_ROLE rows** -- unsettled, and I agree with their refusal to mutate
  production IAM for instrumentation.
- **`comp-iam simulate --self-test` invocation** -- the self-test did not run via that flag form
  (argparse demands positional args). `_simulate_self_test` exists at `:685`; I did not locate its
  entry point. **UNVERIFIED, stated rather than assumed.** Out of scope: untouched by this build.

---

# CLOSURE AMENDMENT -- all 4 P1s RE-VERIFIED FIXED @72fda2aa5 (CVO, 2026-07-22 ~2005Z)

Builder reported all four fixed 8 minutes after the verify. **I did not accept the self-report.** I
re-ran **my own original mutant census files** -- the same bytes that produced the findings -- against
the new code, plus a direct probe of the decision function.

| finding | before | after (my re-run, same inputs) | verdict |
|---|---|---|---|
| **F1** future reads FRESH | exit **1**, `[FRESH]` | exit **3**, `[FUTURE]`, `!! IMPOSSIBLE VINTAGE: dated 47.7h in the FUTURE` | **FIXED** |
| **F2** `live` ungated | cross-check computed off any census | limb **DISQUALIFIED**, report survives (exit 1) | **FIXED** |
| **F3** docstring claims absent flag | `[FRESH]`, no marker | loud `!!` marker + refusal reason names FUTURE, not "STALE" | **FIXED** |
| **F4** no detector NOTE on reconcile | absent | `NOTE: DETECTOR, not an authorization oracle ... (Rule 22a)` | **FIXED** |

**Skew-tolerance boundary probed directly** (`census_freshness`, synthetic clock, no CLI): `+14min ->
FRESH`, `+15min -> FRESH`, `+16min -> FUTURE`. The claimed 0.25h tolerance is exactly what is
implemented; no off-by-one. Their choice of a tolerance over a blanket future-refusal is right --
minutes of skew are real, hours are not, and a blanket rule trades my false-accept for a false-refuse.

**F2's fix is BROADER than my finding.** I reported the ungated door via the FUTURE and undated cases.
They gated the whole class: `NO_VINTAGE` **and** `STALE` **and** `FUTURE` each disqualify the limb, each
naming which. **And the accept side still computes** -- fresh census -> `graph 193 vs census 205`,
`!! 12 role(s) live but ABSENT`. So the fix did not buy refusal by breaking the feature.

**Design call I endorse:** `live` **disqualifies the limb rather than refusing the report** -- the graph
is `live`'s primary source and stays trustworthy; only the cross-check is invalidated. Refusing the
whole report would have been the over-correction.

**No regression:** `m3_novintage -> 3`, `m4_old -> 3`, fresh `-> 1`. Suites run by me: pytest **9/9**
(was 5), census self-test pass, simulate self-test pass.

**My UNVERIFIED residual is closed:** the simulate self-test entry point is `comp-iam simulate-self-test`
(its own subcommand, not a flag) -- run by me, all cases pass.

**Two message-accuracy defects they introduced inside the fixes and caught pre-commit** (a FUTURE census
reported as "STALE"; the disqualified path printing "no --census" when one was supplied) -- **both
verified actually correct in the landed code.** They are F3's own class, and committing a misreporting
defect inside the fix for a misreporting defect would have been its own finding.

## STATUS: RAVC CLOSED. Verdict upgraded **BROKEN@MECHANICAL + BROKEN@DECLARATIVE -> SOUND** on all
four routed findings. **STILL OPEN, unchanged and not closed by this:** the D4 scope-exclusion (12
suppressed findings) and the `_provenance.py:405` "hourly" vs event-driven contradiction -- carried as
NOT-REACHED by me, never as clean.

-- `3.0.0_SA_CVO`
