# SEAM: `commit_gate_runner` → `manifest_check_cli.cmd_check` → `load_yaml` (scale: MICRO×3 + MESO)

**archetype:** VALIDATE

Pre-implementation seam validation of a proposed change to the COMMIT GATE itself, per Andrew-direct
2026-07-28: *"run a /seams on the various seams involved to validate that it works as intended, if it
passes that then you have authorization to implement."*

## Seam definition

| | |
|---|---|
| **Side A** | `commit_gate_runner.py` (one process per commit; imports the CLI as a module) |
| **Side B** | `manifest_check_cli.cmd_check()` → `load_yaml()` → the YAML files on disk |
| **Boundary** | the `load_yaml(path) -> dict` call: what it returns, and whether callers may mutate it |
| **Contract** | *(a)* every caller receives an INDEPENDENT mutable dict — `load_config():254-265` performs **5 `setdefault` mutations** on its result; *(b)* output + exit code must be **byte-identical**, which is the bar `commit_gate_runner`'s own docstring records for its predecessor consolidation |

**Sub-seams tested:** **S1** runner→`cmd_check` · **S2** `load_yaml`→files (the cache boundary) ·
**S3** `load_config`→its setdefaults (the mutability contract) · **S4** cross-FILE reuse in one process.

## The change

`load_yaml` memoizes parsed YAML in a module-level dict keyed by path, and returns
`copy.deepcopy(cached)`. **The deepcopy is load-bearing, not defensive politeness** — it is what
preserves contract *(a)*. A bare cached reference would hand every caller the same object and
`load_config`'s `setdefault`s would mutate shared state.

## Axis verdicts

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| **MECHANICAL** | **PASS** | Parity harness, live module at its real path, both arms, only caching differs: stdout/stderr/rc **byte-identical** across 3 cases (1 `.sh`, 1 `.py`, 3-file batch) | — |
| **DECLARATIVE** | **PASS** | The docstring contract *"same function the standalone CLI calls… no import-time side effect"* still holds — the cache is internal to `load_yaml`, no signature or call-site change | — |
| **SEMANTIC** | **PASS** | S3 exercised on BOTH arms: `keys_present=True`, `independent_objects=True`, **`mutation_isolated=True`** — mutating one `load_config()` result does not leak into the next | — |

**Measured cost (median, live module):**

    single .sh    0.948s -> 0.589s   1.6x
    single .py    0.103s -> 0.092s   1.1x
    3-file batch  1.520s -> 0.673s   2.3x   <- the compounding: grows with commit size

## Grounding

`grounding: SOURCE-CONFIRMED` — cost located by cProfile on the live module: `cmd_check` 3.048s
total, `_completeness_invariants` 2.728s (90%), **`yaml.safe_load` ×12 = 2.683s (88%)**;
`load_yaml` `manifest_check_cli.py:238` has no cache; `load_config():254-265` mutates its result.

## An instrument defect I hit and discarded — the reason v1's FAIL is not in this verdict

**My first harness reported PARITY BROKEN. It was wrong.** It copied the module to a temp dir, and
`manifest_check_cli` resolves the workspace root from its own `__file__` — so the "patched" arm
failed with `git ls-files failed: not a git repository` and BLOCKED for a reason unrelated to
caching. **It compared in-repo vs in-tempdir, not cached vs uncached.**

**A FAIL from a broken instrument is not a FAIL**, and had I reported it I would have killed a sound
change on an artifact of my own test rig. v2 changes exactly one variable: the live module at its
real path in both arms, cache injected at runtime.

## A correction to my own projection

I projected **~11×** from a 143×-per-parse micro-benchmark. **Measured: 1.6–2.3×.** The micro-bench
timed re-parsing the *133KB manifest*; `cmd_check` mostly parses several smaller YAMLs, so the real
saving is smaller. **The projection was right about direction and wrong about magnitude** — recorded
because a 5× overstatement on a gate-cost claim is the kind of number that gets quoted back.

## Verdict

**SOUND** — all three axes PASS, S3 exercised on both arms, parity byte-identical.
**Implementation authorized by Andrew conditional on this result.**

## Residual / unknowns

- Cache lifetime is the **process**. `commit_gate_runner` is one process per commit, so a file
  edited *during* a single gate run would serve a stale parse. **Not reachable today** — the gate
  reads files it was handed and does not write YAML — but it is the assumption the cache rests on
  and it should fail loudly if that ever changes.
- Parity exercised on **3 cases**; not an exhaustive corpus. The gate's own `selfcheck` subcommand
  should be run post-implementation as an independent confirmation.
- **Not tested:** behaviour when a YAML file is absent (`load_yaml` `sys.exit(2)`s before the cache
  is consulted, so the path is unchanged — reasoned, not exercised).

## Compiler Tools

| tool | result |
|---|---|
| `cProfile` on live `cmd_check` | 88% in `yaml.safe_load` ×12 — the cost located, not assumed |
| parity harness (v2), 3 cases × 2 arms | stdout/stderr/rc byte-identical |
| `load_config` mutability probe, both arms | independent objects, mutation isolated |

— 3.0.0_SA_CVO
