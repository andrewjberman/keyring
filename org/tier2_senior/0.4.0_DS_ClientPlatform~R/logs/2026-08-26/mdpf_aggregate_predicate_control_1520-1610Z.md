# 0.4.0_DS_ClientPlatform~R -- the :699/:703 + :1124 acceptance control (1520-1610Z)

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT

**seat:** `0.4.0_DS_ClientPlatform~R` · **window:** 2026-08-26T15:20Z -> 16:10Z
**prior log:** `d1_catviews_finding2_repair_1452-1520Z.md` @`099e2ad87c`
**project:** D8 / MDPF (`mdpf_aggregate_aua.py`) · **dispatch:** `2.0.0_SA_COO` 72427 s.4, extended 72469 s.1

---

## SUMMARY

Authored the acceptance control for three defective float comparisons in
`mdpf_aggregate_aua.py`. **Control only** -- `0.4.0_DS_ClientPlatform~S` made the repairs; the roles
were **inverted** from the `:992` pairing (where I repaired and they controlled) so neither seat
grades its own work on either fix.

**Both repairs accepted. 9 arms x 10 magnitudes, and every discriminating arm was proven DEAD against
the unrepaired code before being trusted green against the repaired one.**

---

## THE DEFECT

Three sites compared UNROUNDED floats against `RECON_TOLERANCE`:

| site | shape | consequence |
|---|---|---|
| `:699` / `:703` | `abs(decl - act) > TOL` on two floats | appends a FALSE MISMATCH -- manufactures work |
| `:1124` | `abs(_t - (_m+_s+_n)) > TOL`, **three terms** | **`raise SystemExit`** -- ABORTS THE RUN |

An exactly-one-cent decimal gap is not exactly `0.01` in float. **This module IS in the running lambda
bundle**, so unlike the `:992` repair the "absent from production" safety argument does not cover it.

---

## FINDINGS

### F10 -- The two legs have DIFFERENT defective magnitude sets, and that justified the arm split

```
model leg (:699) flags:  100 | 10K | 1M | 100M | 10B      = 5 of 10
sma   leg (:703) flags:        10K | 100K | 1M |     10B  = 4 of 10
```
The sma fixture carries `mag/2`, so its float error lands elsewhere -- two members swap. **A control
sweeping only the model leg would exercise the sma site precisely where it happens not to fail, and a
half-repair would read as a PASS.** I did not separate A2/A3 for symmetry; the measurement justified it.

### F11 -- `SystemExit` does not derive from `Exception`

The obvious harness -- wrap the `:1124` call in `except Exception` -- **does not catch the FATAL.** It
escapes, kills the control process, and the run reads as **a crashed test rather than a fired arm**,
so the arm gets rewritten instead of believed. *An arm that cannot report is worse than an absent one.*
The probe catches `SystemExit` explicitly **and matches the message**, so an unrelated one scores
`SYSEXIT-OTHER` and is never counted as this arm firing.

### F12 -- A control spanning two commits has NO single pre state (a limit in my own instrument)

The two repairs landed in **different commits**, so there is no commit at which every arm is in its
"pre" state. `--pre` against HEAD reads `ARM IS DEAD` on three arms -- **correctly** -- and a later
reader would call the control broken. Fixed **in the docstring, not the code**: it is a **per-arm
reachability instrument** with per-arm baselines named (A2/A3 vs `c5bce83d1e^`, R2 vs `c5bce83d1e`).

### F13 -- I re-verified my own number because a peer stopped checking it

`0.4.0_DS_ClientPlatform~S` reported 5/10 for a two-leg site as one figure, corrected themselves, then
**deferred to my per-leg 4** after their own reconstruction gave 5. **That deference closes the
question -- nobody else would check the 4.** Re-ran it: 5 and 4, stable across three runs against a
baseline verified unrepaired (`TOL_CENTS` count 0). Then found the discriminator and sent it: **a
reconstruction feeding the same value to both legs instead of `mag/2` measures the model leg twice and
gets 5 both times.** Their reconstruction is now *validated as different with a named cause*, which
beats an open discrepancy between two seats' records.

---

## ACCEPTANCE

|  | `--pre` | default |
|---|---|---|
| vs `c5bce83d1e^` (`:699/:703` unrepaired) | **rc=0** | rc=1 |
| vs `c5bce83d1e` (`:1124` unrepaired) | R2 reachable **5/10** | -- |
| vs HEAD (both repaired) | rc=1 | **rc=0**, all 9 arms |

R2's 5/10 matches `~S`'s independent pre-edit measurement **by a different method, neither derived from
the other** -- corroboration rather than repetition.

**All baselines taken with `git show <sha>:<path>` into a scratch tree. No stash, no checkout, and
`~S`'s in-flight working tree was never touched** -- this fabric lost a seat to a claim race today.

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `aggregate_input_predicate_control.py` | 4 baselines x 2 modes + 3 determinism runs | **PASS** | The instrument I authored. ~90 sweeping invocations per run. |
| `safe-commit.sh` | 2 commits, `-F` message files | **PASS** | commit-gate `All checks passed` both; risk-reflex CLEAN; msg-verify MATCH. |
| `py_compile` | after each edit | **PASS** | |
| ad-hoc float probe | 10 magnitudes, both shapes | **PASS** | Reproduced 5/10 before authoring anything -- I do not write a control around an assumed defect. |
| `git show <sha>:<path>` | 3 pre-repair extractions | **PASS** | The only way to baseline without disturbing a peer's uncommitted work. |

**What worked:** running the standalone float probe FIRST. It established the defect was real and
**non-uniform** before a line of control existed -- which is what made the asymmetric PRE/POST matrix a
design decision rather than an accident.

**What failed:** my first fixture reached the predicate but the arms read dead -- because `~S`'s repair
was already in the working tree, then committed between two of my own reads. Diagnosed by checking git
state rather than by assuming my fixture was wrong. **Second time today the world moved under a
measurement mid-read.**

**Gap found:** none new. F11 (`SystemExit`/`BaseException`) is a language property, not an estate one,
but it is not re-derivable at a call site -- `~S` has banked it durably beside the existing bare-except
entry, which is the right home.

---

## MCP TRAFFIC

**11 messages** (6 in, 5 out). IN: 72427 (dispatch, roles inverted), 72463 (`~S` repair + BLOCKING on
`:1124`), 72469 (`:1124` authorized onto my control), 72491 (`~S`'s coverage-gap report), 72515 (close),
plus the Leg A acceptance. OUT: control delivery, gap-closure with their own probe re-run, the per-leg
re-verification. ACKs recorded for all.

---

## BLOCKERS

**None.**

---

## CURRENT STATE

- **Control committed:** `data/mdpf/scripts/gold/tests/aggregate_input_predicate_control.py`
  @`bfb4edd7f8` (`:699/:703` arms) + @`f21c5a2663` (roll-forward arms). 9 arms, 10 magnitudes.
- **Both repairs independently accepted.** `~S`'s coverage-gap report was true of the commit they
  measured and is closed -- their own probe returns **0** at `@bfb4edd7f8`, **13** now.
- **Reaching `:1124` stubs three seams** (`detect_stale_partners`, `load_prior_partner_block` -- its
  real body does S3 IO -- and `log` as a past-the-predicate sentinel). **The predicate itself is never
  stubbed and never re-implemented**; only the block's SOURCE is faked, and every stub is restored in a
  `finally`.
- **Scope held:** does NOT ride tomorrow's build. Leg A pin stays `530ba66971` + 3 files.
- **12 commits this session, all LOCAL** under the integrator-only gate.

---

## NEXT STEPS

1. **[`0.4.0_DS_ClientPlatform~S`]** Nothing owed. If the per-leg members are ever wanted, run
   `--pre` from a scratch extraction of `c5bce83d1e^` rather than reconstructing the fixture.
2. **[`3.0.0_SA_CVO`]** The `:1124` control is available as the acceptance instrument if the
   deploy of that repair is ever cut.
3. **[`0.4.0_DS_ClientPlatform~R`]** Idle. Still holding the ADVI_INSURE AC3 re-take, gated on AC4
   emission which is another lane's build.

---

## DO NOT

- **Do NOT read `ARM IS DEAD` under `--pre` at HEAD as a broken control** -- both repairs are in;
  that is the arm reporting there is nothing left to be reachable against.
- **Do NOT wrap the `:1124` probe in `except Exception`** -- `SystemExit` is `BaseException` and will
  escape.
- **Do NOT cite a single figure for the `_aua_input` pair** -- it is two sites with different
  defective magnitude sets.
