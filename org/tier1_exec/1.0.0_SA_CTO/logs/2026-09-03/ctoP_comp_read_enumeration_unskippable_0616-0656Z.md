# CTO~P — comp-read enumeration claims made unskippable

**archetype:** IMPLEMENT

## Andrew-direct scope

Seat `1.0.0_SA_CTO~P` was loaded through the repository-local Codex startup sequence. Andrew then directed:

> I just want you to make the adjustments listed here and get feedback from 0.0.0_AB_MSTR to validate when complete: org\tier0_exec\0.0.0_AB_MSTR\deliverables\BRIEF_20260903_COMP_READ_ENUMERATION_UNSKIPPABLE.md

Andrew subsequently corrected the review/test-owner routing:

> direct that request to 0.8.0_AE_CloudComp~P, they are coming online now. Base 0.8.0 is busy they are not part of your fabric

The base-seat requests were retracted, and only `0.8.0_AE_CloudComp~P` remained in this task fabric.

## Implementation

Commit `dc944897c5a4c6e5b6f9c74a821adf3fb3694f76` (`tools(comp-read): make enumeration claims unskippable`) changed only:

- `.tools/comp-read`
- `.tools/hooks/comp-tool-hud.sh`
- `.tools/comprail-gate1-fptest.sh`
- `org/standards/COMP_READ_ENUMERATE.schema.json`

Delivered BR-1/BR-2/BR-3 behavior:

- Text rows carry `WHOLE|SUB` and `hit i/N`; zero/error sentinels carry `hit 0/0`.
- `ENUMERATE` header and terminal `ENUMERATE-END` trailer make the denominator visible.
- Source metadata is prefixed `SOURCE:` so the brief's exact positive-numeric filter retains enumeration rows only.
- `--width`, `--band`, and `--json` are implemented; JSON output validates against the new schema.
- Census pipelines through the HUD deny filtered denominator loss as `CENSUS-FILTERED`, allow summary-preserving or rail-checked forms, and emit `CENSUS-PIPE ALLOW|DENY` audit rows.

Owner-gated battery `.tools/tests/test_comp_read_enumeration_unskippable.py` was reviewed and pathspec-committed only by the corrected personal seat in `aa62c46077de3e048b1da070dbc71281be59d493` (`test(comp-read): lock unskippable enumeration contract`).

## Red/green evidence

- Pre-change contract battery: 7 failed, 1 passed.
- Pre-change rail controls: both intended DENY cases were allowed.
- New contract battery: 8/8 passed; requester post-owner rerun: 8 passed in 5.08s.
- Existing direct comp-read battery: 10/10 passed.
- Combined targeted pytest: 9 passed.
- Isolated rail fptest: 53/53 passed.
- Enrolled suite and precommit simulation: 141 passed.
- `py_compile` and `bash -n`: clean.
- JSON sample: schema-valid; terminal trailer ordering inspected.

One concurrent rail run initially reported 50/53 while another test process shared the enforcement marker. After that peer process ended, the authoritative isolated run was 53/53.

## Instruments

| Instrument | Use | Result |
|---|---|---|
| `.tools/comp-find` | Required consumer census | Brief's `--band CODE` rejected by current band vocabulary; uncapped fallback found 84 hits |
| `pytest` | New and enrolled behavioral batteries | 8/8, 9 passed combined, 141 passed enrolled |
| `.tools/comprail-gate1-fptest.sh` | Pipeline rail validation | 53/53 passed in isolation |
| `py_compile` / `bash -n` | Syntax validation | Clean |
| `.tools/safe-commit.sh` | Identity- and pathscope-gated commits | Exact seat authorship preserved |
| `org/mcp/codex-send.ps1` | Canonical peer routing and RAVC | CloudComp~P owner loop and MSTR validator loop closed |

## RAVC and governance closure

- `0.8.0_AE_CloudComp~P` ACKed, reviewed, committed exactly the one battery file, and reported 8 passed.
- The requester verified commit identity/diff-tree and independently reproduced 8 passed, then sent `ACCEPTED`; CloudComp~P ACKed closure.
- `0.0.0_AB_MSTR` independently validated at origin/CLOUD `3bd8d2ef04`, with both new commits as ancestors. Its verdict was `ACCEPTED`: BR-1, BR-2, and BR-3 all passed on its own instruments, including pre-change build/hook negative controls.
- MSTR owned the brief errors: `comp-find --band CODE` is invalid in the current vocabulary, and error row `-1` cannot survive the brief's required `^\s+[0-9]+ ` filter. It accepted line `0` tagged `ERROR` and the `SOURCE:` prefix.
- MSTR explicitly did not exercise whether every consumer-census reference parses the former row grammar; it treated the already-green 141-test enrolled suite as the control and did not issue REWORK.
- Both `dc944897c5` and `aa62c46077` are confirmed ancestors of origin/CLOUD `3bd8d2ef04`.

## Repository findings

- The brief-referenced `org/tier1_exec/1.0.0_SA_CTO/deliverables/architecture_brief.xml` is absent. No replacement path was inferred.
- A direct `git commit` attempt for the routing-correction record was blocked because it would have used the workstation owner's author line. The staged file was safely unstaged and committed through `.tools/safe-commit.sh` as exact seat `1.0.0_SA_CTO~P`.
- Durable Andrew-direct records: `9cffa7e523` (implementation directive) and `a8b5380be2` (CloudComp~P routing correction).
- Unrelated dirty-worktree changes were preserved and not committed.
