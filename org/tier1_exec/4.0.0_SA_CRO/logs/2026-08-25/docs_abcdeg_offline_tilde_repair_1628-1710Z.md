# 4.0.0_SA_CRO — docs_abcdeg offline tilde repair, 2026-08-25 16:28–17:10Z

**archetype:** COORDINATE  
**secondary_archetypes:** VALIDATE, SCRIBE

Andrew directly instructed this seat to resume `Downloads\docs_abcdeg`, work largely offline
from the major fabric, oversee a small CRO Tilde team, and pick up from the persisted close.
The exact instruction was recorded at
`deliverables/ANDREW_DIRECT_20260825_DOCS_ABCDEG_OFFLINE_TILDE_TEAM.md` and committed as
`731142ebb2` before planner work began.

## Result

The carried cold-certification defects are closed for the exact final five-instrument baseline.
The prior cold run killed 17/31 mutants and left 14/31 alive. The final independent run, executed
from the immutable certifier, killed **31/31 with 0 survivors**.

| Instrument | Final self-test | Final LF identity |
|---|---:|---|
| `evidence_plane.py` | 26/26 | `4b0c682309bff4d51be579ae0ce45a1f23d190c98fb81b53681d7ce6aa7019a9` |
| `interface_edge.py` | 16/16 | `29d50609c7ccc5b0f237e5bf1d1d87cbb6cdf2407bc07fa0b7692eb5b9360d52` |
| `program_registry.py` | 20/20 | `776ff4f86d20f17ab471313fd299658fc27c53d1e1ddd09c90233a06210f46d8` |
| `propagation.py` | 15/15 | `da80bd0a22890d0149eb6faaaf9ab81192b068c8fc29ab8bcaf9e84a26e8729c` |
| `publish.py` | 19/19 | `e6d7ecd471ef75114c86243960aad5ceefd7d00f87426139a244d13bf118223f` |

`cold_certification.py` passes 5/5 and is frozen at LF/raw
`69407662ff981e071ac6647f21a0bbea5f8b61a96a057615032b30adb1cddfa0`.
The final certification report is frozen at LF/raw
`43d04eab7671fcc2b66a1316ce0a2d512877d61bf5a2e28c23653098868f9e16`.

## Team

Three canonical `ajb2` Codex seats were used under exact full serials:

- `4.0.0_SA_CRO~A`: repaired declaration-derived evidence-axis coverage, singleton claim
  cardinality, and orthogonal interface review state. Focused battery moved 6/10 to 10/10.
- `4.0.0_SA_CRO~B`: repaired registry verification/blocked-edge denominators and propagation
  reachability/state refusal. A first author battery passed, but the independent cold run exposed
  four additional survivors. RAVC rework added guard-specific digest, case, sorting, and error-path
  controls; the second cold run killed all four.
- `4.0.0_SA_CRO~C`: repaired full pointer grammar/digest verification, built the explicit
  31-mutant certifier, fixed a self-triggering certifier assertion caught by Base, made the frozen
  harness relocatable from `_published/`, and atomically published the final report.

The launcher-owned turn bridges timed out before binding loaded CLI threads, so no duplicate
detectors were started. Exact original app-server thread IDs were nudged manually. Three accidental
diagnostic duplicate threads were interrupted immediately and never used for work.

## Independent validation

- All six Python sources compile.
- Self-tests pass: 26/26, 16/16, 20/20, 15/15, 19/19, and certifier 5/5.
- The immutable certifier copy itself runs successfully and reports 31/31 killed, 0/31 survived.
- Seven atomic pointers (five subjects, certifier, final report) each contain two full identities;
  pointer, frozen LF/raw hashes, live bytes, and immutable bytes agree.
- `raws/` contains seven files and zero changed after this session's start; latest raw write remains
  2026-08-24 17:24 EDT.
- Canonical Base inbox is empty after exact-file reads and moves to `read/`.

## Compiler Tools

| Tool/path | Purpose | Result |
|---|---|---|
| `provision-path-shims.sh` + `comp-which` | provision and measure Codex command resolution | PASS, 102/102 resolved after PATH prepend |
| `python .tools/comp-find` | explicit Codex-safe compiler invocation probe | PASS |
| bare `comp-find.cmd` | wrapper execution probe | FAIL, access denied; explicit interpreter form used instead |
| Tilde-seat execution probe | verify shim execution, not merely resolution | one ~B probe timed out at 20s; no planner result relied on it |
| `safe-commit.sh` | isolate the Andrew-direct record from the dirty worktree | PASS, `731142ebb2` |

Compiler tools work for Codex in this workspace when invoked through the documented explicit
interpreter/path form. Command discovery alone is not proof that a wrapper executes.

## Startup/audit surprises held out of scope

The startup audit found `org/to-pos-override-audit.log` absent from `MANIFEST` and a roughly
132-hour-stale baseline with an uncaptured tail; snapshot remained `DEVICE-CHAIN-PENDING`.
`~C` also surfaced a stale-looking C9-RIDE status disagreement. These were recorded and not chased
because Andrew's mandate bounded this round to the external planner.

## Remaining program decisions

This repair round has no blocker. The larger planner still has no priced critical path, no built
seed derivation, no selected demonstration estate, and no product-versus-specification decision.
Those remain the next program-level choices after the instrument baseline is now independently
certified.
