# DS ClientPlatform — AoR: the stamp-aware fold, the wiring, and the CHANGE-3 blocker (1503–1700Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Prior log: `inf_phantom_rootcause_and_timelock_1034-1503Z.md` (b3bf930ad). This covers the delta since.

---

## THE HEADLINE

**A time-lock in the producer alone was a PLACEBO on every served number.** `apply_resolution_fold` has
**seven** call sites, and **four re-fold the FULL, already-stamped `canonical_nna` history at SERVE time**:

```
INF_D_00f:815   nna = load_canonical_nna()   <- THE SERVED PER-ADVISOR NNA SPINE
INF_D_00d:660   nna = load_canonical_nna()   <- cumulative chart
INF_D_00c:451   canonical_nna partitions     <- leaderboard
INF_09:406      canonical_nna partitions     <- partner analytics
```

`INF_C_01` could freeze gold perfectly and these four would re-key it in memory before their groupby.
**Every verification that measured GOLD would have PASSED.** `INF_D_00f` says it in its own voice —
`"re-keyed (historical unfold repair)"` — a comment that was **correct when written** (it repaired
partitions C_01 hadn't folded) and now argues persuasively for the harm it causes. Same class as C_07.

**FIX: the fold is now STAMP-AWARE, not date-aware.** *"Already stamped" means "already happened."* One
function, seven call sites, no per-script wiring to get wrong.

**MUTANT-VERIFIED** (the mutant *is* today's deployed behaviour — a reproduction, not a hypothesis):
```
wild type    -> n=0 re-keyed;  peter_lee keeps $400,000
stamp-blind  -> n=3 re-keyed;  joe_brandenburg handed $400,000 of history he never held
```

---

## GO-LIVE BLOCKER (stands): CHANGE-3's CONSUMER WAS NEVER DEPLOYED

Verified on the **deployed bytes** (package pulled from `Code.Location`, 41,167 bytes) — not the repo:

```
DEPLOYED inf-accounts-v2-daily:
  convert_orion_api_to_silver.py    974 lines   advisor_of_record_raw x0   udf7ADVISOROF x0
      POSITIVE CONTROL: def build_accounts_v2 x1   (reading the real converter; grep works)
  pull_inflection_new_portfolio.py              accounts_roster refs = 12   <- THE PULL *IS* DEPLOYED

REPO data/inf/scripts/silver/convert_orion_api_to_silver.py  1,124 lines -> the join IS there, :549-597
```

**THE PULL IS LIVE. THE CONSUMER NEVER SHIPPED.** The lambda has fetched the AoR roster every night
(landed 09:22:44 today, 3,118 rows, `udf7ADVISOROF` populated) and the deployed converter has no code to
read it. And the fall-through branch is commented *"fully inert — no noise."*

Consequence: `advisor_of_record_raw` in **0 of 70** accounts_v2 snapshots (positive control: `rep_id` IS
present → the zero is real) → resolver RAISES at its ACTIVE firebreak → **the one-shot backfill of 1,410
partitions / 9,510 rows cannot run.**

**Root cause = THE SILVER LIB FORK.** Two halves of ONE Andrew-direct change went to two files; only the
`infra/` half ships. **Third fork-caused production defect today.** Routed to `0.7.0_AE_CloudOps`, whose
layer-consolidation recommendation this vindicates. **Fix = PROPAGATE + DEPLOY, not author** — I nearly
wrote a second copy of a change that already exists.

---

## MY OWN INSTRUMENTS THAT LIED (five; all caught by me, none by a reviewer)

1. **The native `Grep`/raw ripgrep silently skips `data/inf/scripts/gold/lib/`** — root `.gitignore:47`
   `lib/` compiles to `**/lib`; git honours the `!` whitelist at :51, **ripgrep does not.** The AoR
   chokepoint, coverage guard and time-lock are invisible to any raw grep rooted above them.
   **`comp-grep` sees them — Rule 21 vindicated; the OFF-RAIL tool is the one that lies.** My proposed
   `.gitignore` fix was RETRACTED by CTO~B, correctly: it reaches vendored numpy, **cot** (separate firm,
   NEVER#1) and **black_diamond** (sovereign). I declined to execute it — but I had not measured where it
   landed, which is **luck wearing discipline's clothes.**
2. **RETRACTED: a $5,197,081.79 "_IWM misattribution" blocker that DOES NOT EXIST.** I measured with
   `derive_advisor_key()`; the code calls `canonicalize_advisor_of_record()` — **different functions, and
   they disagree on exactly the values I was hunting.** The mapping was already closed: **0 of 837
   unexpected on live data.** *"Two paths to one fact, and we cited the one the code does not use"* —
   CLAUDE.md, from the CTO's correction eight hours earlier. I reproduced it verbatim, with a dollar
   figure, and sent it toward Andrew. **Caught by EXERCISING the function to prove a different claim.**
3. **I reported "HARD RAISE, the chain stops" — read from a DOCSTRING.** The code prints
   `ALARM ... NOT blocking the auto-update` and returns. **A comment is a claim with no vintage and no
   test.** Docstring corrected (`8fc930f21`), naming me in-source.
4. **Preview prefix bug: `GOLD_NNA_PREFIX` diverged from `INF_C_01`'s.** `list_all_nna_dates` *appends*
   `canonical_nna_`, so mine became `canonical_nna_canonical_nna_` → matched nothing → **ZERO stamped rows
   forever.** It would have reported *"ZERO stamped — THIS IS THE ONE-SHOT"* on every run: **correct today
   by accident** (there really are zero stamps) **and silently wrong the moment anything is frozen.**
5. **`AOR_FOLD_ACTIVE=1` — the var is `INF_AOR_FOLD_ACTIVE`.** My "ON" run was silently OFF. Second inert
   line today after warning others about inert lines. Positive-controlled the switch, re-ran.

**And the F10 census test caught me** rebuilding TWO PATHS TO ONE FACT (calling
`build_advisor_of_record_fold` myself in the preview). **It was right; I did not scope it green.** The
preview now **DECLARES WHAT IT CANNOT DO** rather than faking the capability.

---

## COMMITS

| commit | what |
|---|---|
| `5c33ca56f` | STAMP-AWARE FOLD + `fold_then_lock` one-path + residual guard + `attribution_basis` |
| `4be25c494` | WIRE the lock into `INF_C_01` + re-point `timelock_preview` + the CHANGE-3 blocker |
| `8fc930f21` | correct the docstring that promised a hard-RAISE the code deliberately does not do |

## COMPILER TOOLS

| tool | use | result |
|---|---|---|
| `comp-grep` | fold call-site census; `assert_attribution_policy_settled` callers | **PASS** — and it is the *only* searcher that can see `gold/lib/` |
| raw `rg` / native `Grep` | same query | **FAIL** — false zero on the whole directory (see above) |
| `.tools/deploy-import-lint.py` | INF deployed libs | **PASS 18/18**, exit 0 |
| `safe-commit.sh` | 3 commits | PASS (surface-check clean) |

**Gap found:** `deploy-import-lint.py` — **the gate CTO ruled — is PRESENT BUT NEVER INVOKED** (0 refs in
`safe-deploy.sh` / `safe_deploy_core.py`; positive control: `aws` x12 in the core). **I did NOT wire it**:
I cannot measure its blast radius on cot/bd without crossing a firm boundary. Routed to CTO.

---

## CURRENT STATE

- **CHAIN HELD. NOTHING SERVED. `INF_AOR_FOLD_ACTIVE=0`.** 306/306 gold suite, ruff clean.
- Lock wired at `INF_C_01:823` (**AST-verified at HEAD**, result re-bound, `to_write = _relocked`).
  Runs **BEFORE** the guards — the residual-advisor guard groups by `advisor_key` and must judge the keys
  we actually WRITE, not a draft. COO independently mutant-verified the oracle can say NO.
- **5-FILE ATOMIC DEPLOY:** `aor_resolution` now hard-depends on `advisor_timelock`. Ship one without the
  other and **all seven producers ImportError and the nightly dies.**
- OFF-path preview (live, read-only): **folded 0 / locked 0 / firm total $133,107,667.64 UNCHANGED** — a
  structural no-op, as designed. **1,410 unstamped partitions, 9,510 rows: 0 OBSERVED / 9,510 BACKFILLED.**
  *Every row a presumption — and now it says so.*

## NEXT STEPS

1. **[0.7.0_AE_CloudOps]** Propagate/deploy the silver converter (or collapse the fork to a layer). Bar:
   the column must appear in a **LIVE partition produced by the DEPLOYED lambda** — read the row, not the code.
2. **[3.0.0_SA_CVO~B]** Gate-2 **on the SERVED artifact, not gold** — a gold-only bar could only ever say PASS.
3. **[1.0.0_SA_CTO]** Wire `deploy-import-lint.py` into `safe-deploy` (blast radius spans firms; not mine).
4. **[0.4.0_DS]** After CHANGE-3 lands: run the preview against the real SSOT, verify BEFORE the one-shot stamps.
