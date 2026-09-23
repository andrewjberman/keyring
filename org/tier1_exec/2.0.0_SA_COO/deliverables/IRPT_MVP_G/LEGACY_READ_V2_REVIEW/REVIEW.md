# LEGACY-READ v2 -- naming-owner review of `ad628ba502`

Author: `2.0.0_SA_COO~G`. Asked by `1.0.0_SA_CTO` 20260923T010913Z under LEGACY-READ-01/02/03
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`). Candidate:
`ad628ba502f6627bb277d9ed7e9afb48b9271eef`, branch `mstr/naming-legacy-read-20260922`, implementer `0.0.0_AB_MSTR`.

## Verdict: NOT READY -- four residual recognizer defects, one of them the LR-01 class again

The recognizer refuses LR-01's three defeats and LR-02's malformed duplicate, as MSTR reports (not re-run
here; see the bounds below). It still accepts five of seven new mutations built from the approved post-image.
Four of those five are syntactic and inside what the ruling requires; the fifth is dataflow, which the ruling
explicitly does not require.

## Instrument (different from the producer's)

`probe.py` in this folder imports the candidate's own `.tools/naming-gate.py` (blob at `ad628ba502`) and calls
`legacy_read_ok(entry, text)` and `authority_ok(...)` on in-memory mutations. It executes no source under test.

- Carrier entry: `org/standards/NAMING_LEGACY_READS.json` at `ad628ba502`, `helper_body_sha256` `e9c932d9af7e...`.
- ⚠ At `ad628ba502` the file still carries the OLD helper: its hash is `7225ec2df653...`, and the
  unmutated file REFUSES. The pinned hash is M's cutoff-patched helper, reconstructed from the CTO-captured
  `candidate.diff` (sha256 `00805e11892da975...`, equal to the CTO's recorded hash), which hashes to
  `e9c932d9af7e...`. **So every arm runs on the APPROVED post-image**: the ad628 file with M's patched helper
  spliced in and the call given `as_of=as_of`. On that image P0 PASSES; without it, every arm would refuse on the
  hash and the probe would be vacuous. My first run was vacuous exactly that way.
- Input sha256 prefixes: gate `a86ba0073470523c`, holdings `d896ffeb8d959595`, carrier `bc11f6d87471bc6e`.

| arm | mutation (inside the approved post-image) | expect | got |
|---|---|---|---|
| P0 | none | PASS | PASS |
| **D1** | a decorator `@_writes_too` on `_latest_date_partition` | REFUSE | **PASS** |
| **D2** | inside `build_inf`: `def _probe(bucket): return <approved call>`; `acc_date = _probe("any-other-bucket")` | REFUSE | **PASS** |
| **D3** | inside `build_inf`: `def _probe(_latest_date_partition): return <approved call>`; called with a lambda | REFUSE | **PASS** |
| D4 | module tail `globals()['_latest_date_partition'] = lambda ...` | REFUSE | PASS (dataflow; LIMIT, not a defect) |
| **D5** | a decorator on `build_inf` | REFUSE | **PASS** |
| D6 | `(lambda bucket="x": <approved call>)()` | REFUSE | REFUSE |
| D7 | class body inside `build_inf` assigning `bucket` | REFUSE | REFUSE |

## Defects

**G-1 (D2, D3): `_binds_of` does not count a nested `def`'s PARAMETERS as bindings. It is the LR-01 class
again.** It enumerates Lambda arguments (`:107-112` of the diff) but for `FunctionDef`/`AsyncFunctionDef`
records only the NAME. `_params_of(fn)` is applied to the enclosing function alone. So a nested function inside
`build_inf` can take `bucket` or the helper name as a parameter. D2 then reads ANY bucket through the one
approved literal, which defeats LEGACY-READ-01's bucket bound. D3 calls an arbitrary callable in the helper's
place. The call-site scan `for n in ast.walk(fn)` descends into the nested function, so the site still counts
as `hits == 1`.
Remedy direction: treat every `ast.arguments` under the scope (FunctionDef, AsyncFunctionDef and Lambda: posonly,
args, kwonly, vararg, kwarg) as a binding of that name. Or, simpler and stricter, require that the approved call
is a DIRECT statement-level descendant of `build_inf` and that no nested FunctionDef, Lambda or ClassDef
encloses it.

**G-2 (D1): the helper hash does not cover decorators.** `ast.get_source_segment(text, FunctionDef)` starts at
`def`, so `decorator_list` is outside the hashed bytes. A decorator that wraps the helper to write, or that
replaces it, leaves the hash equal. That is the ruling's "changed read helper that now writes" case.
Remedy direction: refuse any non-empty `decorator_list` on the helper, or hash from the first decorator's line.

**G-3 (D5): decorators on the ENCLOSING function are unchecked.** A decorator on `build_inf` can replace the
function whose body the site recognizer approved. It is a lesser case than G-2, and the same one-line refusal
covers it.

**G-4: `authority_ok` checks the ruling id as an unanchored substring** (`entry_id not in text_of(out)`).
Measured on the real pin `ec80b01ca4`: the ids `"LEGACY"` and `"IRPT-M-LEGACY-READ-0"` both return `True`.
The shipped entry's id is exact, so this does not open the approved case. It weakens the "authority must name
this ruling" control for any future entry. Remedy direction: match a whole id (a heading or a word-bounded token).
Also consider requiring `git merge-base --is-ancestor <pin> HEAD`, so that the authority lives on the shared
history rather than on any local commit.

**LIMIT (D4, not a defect under the ruling):** a runtime rebinding through `globals()`, `setattr` on the
module, or `exec` is dataflow. The ruling declines to require dataflow soundness. It is recorded so that nobody
reads P0 as proving more than site syntax plus helper text.

## Bounds of this review

- NOT re-run: MSTR's 22-arm harness (`deliverables/LEGACY_READ_CANDIDATE/controls.py`), the LR-01/LR-02
  repairs, the UTC boundary arms, the HEAD-only self-grant arms, the absent/empty-carrier arms and any
  canonical safe-commit invocation. My arms test the one function that decides the waiver.
- The CTO-only exact-file lane for the carrier is not in this candidate (`.owned-paths.yaml` is unchanged
  against CLOUD `c462d8b4df`). Until it lands, the HEAD-read rule stops a same-commit self-grant, but not a
  two-commit one by any ANY_EXEC member. This is known and pending the CTO's landing, and it is not scored here.
- To reproduce: place `naming_gate_v2.py` (`git show ad628ba502:.tools/naming-gate.py`), `holdings_v2.py`
  (`git show ad628ba502:data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`), `carrier.json` and
  the CTO's `candidate.diff` beside `probe.py`, then run `WS_REPO=<workspace> python probe.py`. The output is
  in `probe_output.txt` in this folder.
