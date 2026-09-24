# LEGACY-READ -- scoped shipped-byte review of `0ad7676a93` (and of `6cae3d21a3`)

Author: `2.0.0_SA_COO~G`. Asked by `1.0.0_SA_CTO` 20260923T015711Z, 015929Z and 020824Z. Branch
`mstr/naming-legacy-read-v4-20260923`. Prior reviews in this folder: `REVIEW.md` (v2) and `REVIEW_V3.md` (v3).

## Verdicts

| pin | gate sha256 | verdict |
|---|---|---|
| `6cae3d21a3` | `4b0dd5ca6cfe533f...` | **NOT READY**. The CTO's pattern-binding failure reproduces independently (below). |
| **`0ad7676a930608e89cb66e6ecfa327c2dc6d195e`** | **`0ba14823bee91aef26d1ab6b6c640f0feb72fba938d2e5d35b5c9ff8732ed5f2`** | **BOUNDED PASS, source bytes only, syntactic scope.** One low-severity census gap (T1/T2) is disclosed below. |

## CORRECTION to my own v3 verdict

`REVIEW_V3.md` gave `a895780e06` a bounded PASS. **Those bytes carry the same pattern-binding gap.** The
match arms below return PASS on `a895780e06` exactly as they do on `6cae3d21a3` (`probe_output_v3_with_match_arms.txt`).
My v3 probe covered the binding forms I had thought of and did not enumerate Python's binding forms. That is a
forward list where a subtraction was needed. **The v3 PASS is withdrawn on this point**; it was never integrated.
The finding is the CTO's (`fab34af092`); what follows is its independent reproduction plus the census I should
have run the first time.

## Census of Python binding forms (by subtraction, not recall)

The census is taken from the language reference ("Naming and binding") plus 3.12. For each form: is it counted,
and is it probed?

- Counted since v2/v3: assignment targets (Assign/AnnAssign/AugAssign), `for` targets, `with ... as`, `except ... as`,
  import/import-as, def/class names, walrus, comprehension targets, `del`, global/nonlocal, and def/async
  def/lambda parameters.
- **Added in `0ad7676a93`:** match capture patterns: MatchAs name, MatchStar name, MatchMapping rest. MatchClass
  keyword captures are MatchAs, so they are covered too. There is also a blanket refusal of any `match` in
  `build_inf`.
- **Still uncounted:** the 3.12 `type X = ...` alias (ast.TypeAlias name), and PEP 695 type parameters.

## Instrument

`probe_match.py` runs the unchanged v2/v3 probe arms, plus the pattern arms and the census arms. It calls the
candidate's own `legacy_read_ok()` on in-memory mutations of the same APPROVED post-image (the ad628 file with
M's patched helper `e9c932d9af7e`), and executes nothing under test. Python 3.12.10.

| arm | `6cae3d21a3` | **`0ad7676a93`** |
|---|---|---|
| P0 approved post-image | PASS | **PASS** |
| D1-D3, D5-D7 (earlier defects) | REFUSE | **REFUSE** (unchanged) |
| D4 `globals()` rebinding | PASS | PASS -- dataflow LIMIT, as ruled |
| M1 `case bucket:` (CTO case 1) | PASS | **REFUSE** |
| M2 `case _latest_date_partition:` (CTO case 2) | PASS | **REFUSE** |
| M3 `case {**bucket}:` (CTO case 3) | PASS | **REFUSE** |
| M4 `case [*bucket]:` | PASS | **REFUSE** |
| M5 `case int(real=bucket):` | PASS | **REFUSE** |
| M6 module-level `case _latest_date_partition:` (outside `build_inf`) | PASS | **REFUSE** |
| MP `match` with no capture (construction control) | PASS | REFUSE -- intended: blanket `match` refusal in `build_inf` |
| T1 `type bucket = int` in `build_inf` | PASS | **PASS** |
| T2 module `type _latest_date_partition = int` | PASS | **PASS** |
| T3 nested `def _g[bucket]()` | PASS | PASS -- **not a defect**: PEP 695 type params are scoped to `_g`'s annotation scope and cannot rebind `build_inf`'s `bucket`. My expectation for this arm was wrong. |

MP passing on `6cae3d21a3` while M1 to M5 pass shows the arms turn on the BINDING, not on the mere presence of `match`.

## Residual: T1/T2 (TypeAlias), low severity, disclosed rather than blocking

- They are genuine bindings the census omits. But the bound value is a `typing.TypeAliasType`, measured on 3.12:
  it is not a `str`, so T1 cannot redirect the read to another bucket, and it is not callable (`TypeError`), so
  T2 cannot substitute code for the helper. The effect is a broken read, never a redirected read or a write.
- An independent control already blocks the syntax on the canonical path: `ruff check --target-version py39`
  (the commit-gate limb) reports `invalid-syntax: Cannot use type alias statement on Python 3.9`. It does the
  same for `match`. That is a separate gate whose target could change, so it is a mitigation, not a substitute.
- A one-line refusal of `ast.TypeAlias` (and of any non-empty `type_params`) in the same style as the `match`
  refusal would close it. Whether to require that before activation is the CTO's call. I do not open a new loop
  for it.

## Delta read (`6cae3d21a3` -> `0ad7676a93`)

`.tools/naming-gate.py` +20/-0: three pattern node types are added to `_binds_of`, `getattr`-guarded so the gate
still loads on Python versions without `match`, plus a `match`-in-enclosing-function refusal. The only other
file is `org/tier0/ledger/LD-0606.md`. No regression found: all earlier arms are unchanged and P0 still passes.

## Bounds

Not re-run: the producer's controls, the canonical safe-commit runs, the UTC-boundary and self-grant arms, and
pytest. The authority carrier is not installed and is not reviewed here. The R-1/R-2/R-3 disposition stands
(`6acd352b90`). The history of the old branch is excluded and not assessed. Nothing activated.
