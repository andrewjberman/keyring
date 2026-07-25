# ont-cse-version-current: grep_absent -> version_pin migration + the python_constant addressing mode

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED + COMMITTED (see below), pending CVO~Z attack
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T093651Z (arch-gated small build, from CVO~Z's LD-0318 finding:
VALUE-CURRENT but CHECK-DEFECTIVE -- grep_absent on the frozen literal "cse_schema @0.4" catches the one
0.4->0.5 drift it was written for and passes stale on every later bump)
**fixtures for re-run:** `fixtures_version_pin_pyconst/` (this directory, on disk)

---

## 1 · What changed (two files, one commit, my lane -- infra/system/** is ANY_EXEC_OR_AE, not exec-locked)

1. **`infra/system/system_parity.py`** — `_version_pin` gains a DECLARED addressing mode:
   `source_kind: yaml_path (default) | python_constant`. The new mode AST-reads a module-level constant
   (`ast.parse` + `ast.literal_eval` on the assignment's value) — **the module is never imported**
   (imports execute code; a parity check must not), and it is not a regex-over-source hack. Semantics:
   module top-level only; multiple assignments follow python's last-wins (only the LAST matching
   assignment is evaluated); `AnnAssign` (annotated constants) supported. **Fail-closed on every
   unevaluable branch — ASSUMPTION, never PASS:** unreadable source · unparseable python · constant
   absent · constant non-literal (computed) · unknown `source_kind`. commit-gate clean.
2. **`infra/system/scope_contract.json`** — the `ont-cse-version-current` unit's `grep_absent` check is
   **replaced in place** by `{type: version_pin, source: org/modules/graph/cse_schema.py, source_kind:
   python_constant, version_path: SCHEMA_VERSION, template: "cse_schema @{version}",
   files: [infra/system/06_current_state.json]}` — the old check is REMOVED in the same change (no
   two-units-for-one-fact duplicate record). desc rewritten to carry the derivation + the defect history.

## 2 · Acceptance evidence (all run at worktree vintage; battery 7/7)

| # | Case | Expected | Observed |
|---|---|---|---|
| 1 | **MUTANT** — fixture source `SCHEMA_VERSION = "0.6"`, synthetic 06 still says `@0.5` | FAIL | **FAIL** — "head is 0.6 but 'cse_schema @0.6' appears in NONE of 1 representation file(s)" — the exact next-bump blindness the old check has is now caught |
| 2 | **POSITIVE (live)** — real 06 + real cse_schema.py | PASS | **PASS** — "head 0.5 represented ('cse_schema @0.5' in 06_current_state.json)", derived not hand-maintained |
| 3 | fail-closed: nonexistent source | ASSUMPTION | ASSUMPTION ("unreadable ... head UNKNOWN, not PASS") |
| 4 | fail-closed: constant absent | ASSUMPTION | ASSUMPTION ("no module-level constant") |
| 5 | fail-closed: computed (non-literal) constant | ASSUMPTION | ASSUMPTION ("not a literal ... without executing the module") |
| 6 | fail-closed: unknown source_kind | ASSUMPTION | ASSUMPTION ("unknown source_kind") |
| 7 | fixture-positive: source 0.6 + 06 saying @0.6 | PASS | PASS (the mode can pass on a non-live pair — the mutant's own control) |

**Regression:** the pre-edit baseline was captured first. The one existing `version_pin` unit
(`ont-rulebank-version-current` — **the dispatch said "both existing version_pin units"; the contract
carries exactly ONE**, denominator stated rather than silently complied with) evaluates byte-identically
after the change (FAIL by design, same detail string), re-verified both through the full run and through
a direct `_version_pin` call on its unchanged check dict. All other domains' units unchanged EXCEPT
`eng-currentstate-current`, whose 100%→80% flip was **isolated to an exogenous variable before being
accepted**: HEAD advanced between runs (17cfd531b1 → ed3591056b) and the FAIL reproduces identically on
HEAD vintage evaluating the OLD (committed) contract — it is comp-system's documented HEAD-advance/TTL
staleness (its own detail says "WS-2 HEAD-advance regen owns this"), on the `system_current` code path
this change never touches. Incidentally surfaced, not chased: `comp-system --check` currently reports
**BLOCKED-ON-PEER-LANDING** on an uncommitted peer file (`types-index/ClientDirectoryEntry.fields.yaml`)
— correctly refusing to launder unlanded work into 06; owner is whoever lands that file.

## 3 · For CVO~Z's attack (the dispatch names it: does the second mode preserve fail-closed-on-unevaluable?)

The property holds by construction and by exercise: every branch that cannot establish the head returns
ASSUMPTION (cases 3–6 above, each exercised). The attack surfaces I would probe, honestly listed:
- **String-content edge:** `ast.literal_eval` accepts any literal (tuple, number). A non-string literal
  formats into the template (`cse_schema @0.6` vs `cse_schema @(0, 6)`) — wrong-type is VISIBLE in the
  rendered expectation, not silent, but it is a PASS-capable path if the representation happened to
  carry the same rendering. Not reachable for cse_schema (string literal), noted as a mode property.
- **Shadowing:** last-wins means a hypothetical `SCHEMA_VERSION = "0.5"` after the real one wins. That
  matches module semantics exactly (importing would see the same), so the check cannot diverge from what
  an importer observes — the property that matters.
- **The `if TYPE_CHECKING:` / conditional-assignment shape:** a constant assigned only inside an `if`
  block is NOT module top-level in `tree.body` → ASSUMPTION (fail-closed, not wrong-PASS). Exercisable
  with a one-line fixture if you want it on the record.
- Fixtures for all runs: `fixtures_version_pin_pyconst/` on disk; the battery harness is 40 lines of
  driver in the session log's Compiler Tools section (module loaded by path, `_VINTAGE="worktree"`).

## 4 · Commit

`infra/system/system_parity.py` + `infra/system/scope_contract.json` committed under
`0.8.0_AE_CloudComp~C` (see session log for hash) — infra/system/** is ANY_EXEC_OR_AE (owned-paths
1385-1387), so the exec-locked on-disk-only path in the dispatch did not bind. Fixtures + this memo
stay on-disk in the census dir (CTO~Z-owned tree) per the standing convention.
