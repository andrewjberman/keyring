# MDPF_CANRTE.W1: route_bindings.yaml landed 33/33 TIE, mutant-controlled, pure-add proven

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~17:12Z -> ~17:30Z (delta since composition_flip log)

## Arc

- COO GO 171137Z (W1+W2, sequence W1 first) on Andrew's "Proceed" 1706Z — Phase-C seating
  accelerated from the morning wave. ACK'd 171202Z; W1 TO flipped pending; comp-to set.
- **Phase-1 re-cite at CURRENT HEAD (da536d5cd):** constant-bearing files that moved today
  enumerated via git log — the slice's vocabulary moved TWICE (@0fa303f91 mint ->
  @54b15511c revert; net drift = INCOME_NON_MODEL_NAMES grew by 'Opal Moderate Income
  Portfolio') — NAMED in the yaml's drift block and encoded BY REFERENCE, never copied.
  Route constants otherwise unmoved (my floor fix touched the cot plane, not mdpf).
- **Landed @8058f5523:** `data/mdpf/config/route_bindings.yaml` (axis, staging keys,
  per-firm legs — C-1 VERBATIM in the 49f custody row with the ETFS one-row-re-bind note;
  L1 cottonwood-only with 4 declared vendor-grain reasons; model-key sets; seams;
  roster-derived carry window; carry-import declared per plan SS6-4) +
  `route_bindings_tieout.py` (read-only validator: AST constant-folding extraction,
  2 computed imports from the crosswalk leaf module, code-literal substring rows;
  denominator printed per kind; empty-check = FAIL by construction).
- **Validator run at HEAD: 33/33 TIE, bare rc=0.** First run was 32/33 — the FAIL was the
  VALIDATOR'S OWN extractor gap (SLICE_KEY = REVAMP_PREFIX + "literal", not a bare
  literal); fixed with a fold pass (Names resolve against prior top-level literals,
  string-concat folds) rather than downgrading the row to a substring check. The
  instrument surfaced its own gap as a loud FAIL — the wanted behavior.
- **Mutant control EXERCISED before close:** perturbed the 49f cohort row in a scratch
  copy -> FAIL rc=1 naming live vs expected. The control can fail.
- **Zero-consumer PROVEN:** comp-grep denominator 22,095 of 24,062 files scanned;
  12 matches in 7 files = the validator + plan/design/log docs + the TO family. No code
  consumer -> the delete-the-file rollback claim is TRUE.
- Reports: COO 172735Z (acceptance leg) + CTO 172846Z. TO flipped complete this commit.

## Compiler Tools

| run | observed | verdict |
|---|---|---|
| git log --since today on the 6 constant-bearing files | slice vocabulary x2 (net: residual set +1), pair scope-field, metrics fold re-source; route constants unmoved | phase-1 drift named before encoding |
| `.tools/commit-gate.sh route_bindings_tieout.py` (x2, pre- and post-fold-fix) | All checks passed both times | PASS |
| `python route_bindings_tieout.py` (bare rc) | run 1: 32 TIE / 1 FAIL (extractor gap, self-surfaced) -> fold fix -> run 2: 33 TIE / 0 FAIL rc=0, denominator per kind printed | PASS at close; the interim FAIL banked as the honest arc |
| mutant control (scratch copy, perturbed cohort row) | FAIL rc=1, live-vs-expected printed | CONTROL PASS |
| `comp-grep "route_bindings" .` | 12 matches / 7 files / 22,095 scanned — validator + docs + TO family only | zero-consumer PROVEN |

## Do NOT (successors)

- Do NOT copy vocabulary sets into this yaml — CANONICAL_KEY / INCOME_NON_MODEL_NAMES are
  BY REFERENCE (the source module is the single authority; it moved twice today).
- Do NOT read the yaml as consumed — W-2's builder is its FIRST consumer; until then the
  rollback is delete-the-file.
- The 49f custody row is C-1 sovereign text — an ETFS-CANON ruling re-binds THAT ROW ONLY.

## Blockers

None. Next at this seat: W-2 (Model-B shadow builder; Phase-1 = Rule-22a shadow-prefix
IAM verification per the joint rider). Tonight's ~02Z floor read + chain-green tie reads
keep priority.
