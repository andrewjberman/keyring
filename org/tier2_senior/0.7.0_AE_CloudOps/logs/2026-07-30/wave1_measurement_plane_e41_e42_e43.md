# The measurement plane was built a week ago and never exercised -- E4.1/E4.2/E4.3 — 0.7.0_AE_CloudOps

**archetype:** MIXED (VALIDATE + IMPLEMENT + DIAGNOSE)

**Date:** 2026-07-30
**Task Order:** NFRA_VELOCITY_ESTATE Wave-1 (COO dispatch 20260730T053344Z + refinement 053709Z; no TO file -- dispatched by MCP)
**Status:** COMPLETE (E4.1 3/3 conditions, E4.2, E4.3) with 3 holds at other lanes

---

## Objective

Land the Wave-1 measurement plane so "are we improving?" becomes answerable in either
direction: E4.1 (verdict-derivation fix, three binding gate-approved conditions incl. a
REQUIRED MUTANT), E4.2 (separate the FAIL column's three meanings in the machine record),
E4.3 (re-derive C5 independently, make per-series decomposition the standing form). Do not
start E6.R8, and do not foreclose it.

The load-bearing discovery came first: **two thirds of E4.1 was already built (2026-07-23,
NFRA_MSBEFF.R1R3/M3) and had never been run against a mutation.** It read healthy on
inspection for a week. So this session was verify-then-close-the-gaps, not greenfield --
and it is the reason I measured before building.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `"where is the comp-tool telemetry verdict derived PASS FAIL"` | WARN | Honest NO-MATCH: printed "NO CURATED RULE MATCHED... these are FUZZY GUESSES, not a routing decision" and refused to pretend. Correct behaviour -- the tool has a channel for "I don't know". Routed me to its on-rails fallback. |
| comp-grep | `comp-tool-runs`, `12\.14`, `per_result`, `exit 120\|...` | PASS (and caught MY error) | Located the appender, the C5 source table, and the miner. On the rc=120 hunt it WARNED my escaped-pipe pattern would be read literally by Python re, so the 0-match was not evidence of absence -- I had written a broken predicate and the tool said so. Also prints its own denominator (24,407 of 26,404 in scope). |
| comp-manifest-check | `check --file .../comp-output-contracts.yaml` | PASS | The registration invariant. Used as both control and mutation target: PASS 70/70 un-mutated, `rc=1 BLOCKED` naming `comp-aws` when mutated, PASS again restored. Re-verified PASS after my `kind:` edit. |
| comp_output_contract.py | `--self-test` | PASS | The true census (70/22/51/50) -- replaced my own bad `grep -cE` count of 3, which had matched only top-level yaml keys. A tool's own self-test beat my hand-rolled predicate. |
| comp_msbeff_rebaseline.py | bare, then `--dual-basis`, `--corpus-profile`, `--write` | PASS | Existing tool surfaced 517 re-verdicting rows; my extension added the dual-basis exercise. |
| comp-pipescript | `io` (no arg), `io <bogus>` under COMP_SYNTHETIC_FIXTURE=1 | PASS | Used as the LIVE end-to-end exercise of the new typed field through a real shim into the real sink. |
| comp-surface-check | auto in safe-commit (x4) | PASS | No critical surface touched; 6 surfaces / 3 SEV1 screened each time. |
| comp-pulse | risk-reflex, auto in safe-commit (x4) | PASS | REFLEX CLEAN with denominator printed (N files vs 1,484 danger nodes). |
| comp-system gate | auto in safe-commit | FAIL-CLOSED, correctly | BLOCKED my yaml on `BLOCKED-ON-PEER-LANDING`. Working as designed -- see Blockers. |
| comp-kuzu | `MATCH (n) RETURN count(n)` | FAIL (hung) | My own error: ran it unbounded as a probe and it hung past the 2-min harness timeout, killing the batch (exit 143). Its row landed as rc=1 -> `kind_undeclared`, which usefully populated my own taxonomy. Bound your probes. |
| comp-iam / comp-blast | not run | SKIPPED | No IAM change, no boto3 call, no infra change this session -- E4.x is repo-side python + a declaration yaml. Rule-22a grounding not applicable. |

**What worked:** comp-which's honest NO-MATCH and comp-grep's self-warning about my own bad
regex were both worth more than a confident answer would have been. `comp_output_contract
--self-test` corrected a census I had gotten wrong by hand. And the comp-system gate blocked
me for exactly the right reason.

**What failed:** nothing in the tools. Three failures were MINE and all three were caught by
a control rather than by care: (1) I grepped the `comp-manifest-check` shim instead of its
implementation and nearly reported the registration invariant as ABSENT -- it lives in
`manifest_check_cli.py:943`; (2) I counted declared tools with `grep -cE '^[a-z...]'` and got
3 instead of 22, because the entries are indented; (3) I wrote an escaped-pipe comp-grep
pattern and would have read its 0 matches as absence if the tool had not warned me.

**Gap found:** `org/ref/SESSION_LOG_STANDARD.md:34` instructs every agent to *"Append one
line to org/compiler-tools-log.md after writing this section."* That append was RETIRED
Andrew-direct 2026-07-29 (*"just constant commit nonsense"*), killed at source in
`comp_log_auto.py:_append_log`, and `org/XXX.md:391` now says **"Do NOT append to or commit
org/compiler-tools-log.md."** The standard therefore tells every agent to do a prohibited
thing -- the same class as the CLAUDE.md:71 defect (law instructing a retired tool). I did
NOT obey it. Routed to COO/CVO as a record fix, not edited across lanes.

---

## Work Completed

*(AE's Deployment Sequence table does not apply -- this session shipped no artifact to AWS
and ran no Terraform. Verification section below carries the actual output instead.)*

### 1. E4.1 conditions 1 + 2 -- EXERCISED, not inspected (`39dffb3af7`)

Both conditions were already coded and never mutated. I exercised both, then made the
exercise permanent as 12 mutant traps.

MUTANT A (condition 2, the REQUIRED one) -- victim `comp-blast`, declaration removed from the
in-memory contract surface, disk untouched:
- positive control, run FIRST and separately: rc0 PASS / rc2 VERDICT / rc3 REFUSE / rc99 FAIL
- MUTATED: rc2/rc3/rc99 all -> UNKNOWN; both header lines went LOUD ("coverage NOT asserted")
- RESTORED: rc2 VERDICT / rc3 REFUSE
- bonus: a never-registered ghost renders UNKNOWN with a *distinct* reason ("not registered
  in tools_index" vs "registered but awaiting a contract") -- the instrument separates the
  two kinds of not-knowing, which is more than the condition asked for.

MUTANT B (condition 1's enforcement -- the gate had never been fired):
- control: `output-contract invariant PASS: 70 tools_index tool(s)`
- mutation: deleted `- comp-aws` from `pending_declaration:` (line 417)
- result: `BLOCKED ... comp-aws in NEITHER contracts: NOR pending_declaration:`, rc=1
- restored: sha16 `f09dab0e757496ea` byte-identical, gate PASS again

### 2. E4.1 condition 3 -- dual-basis preservation + the read-back query (`631e71f4b9`, +324)

The 07-23 shape preserved the VALUE (`result_prior`) but not the LOGIC. Built rows-alongside-
rows: each source row emits two rows, one per basis, each carrying its verdict in the SAME
`result` field, so a consumer filters one column and gets a complete clean series and never
needs per-basis field-selection logic. Basis id = version AND content hash
(`derived@v1+f09dab0e757496ea`), because a hand edit that does not bump `version:` still
changes every derived verdict.

### 3. E4.2 -- typed `fail_kind` on the machine record (`a580011c3d`, +146)

Derived from the tool's own declared exit contract via an optional `kind:` on a fail-class
exit; no frozen map. Legacy `(SYNTHETIC TEST FIXTURE)` suffix PRESERVED (additive). Two
honest-unknown buckets, `undeclared_rc` and `kind_undeclared`, neither ever defaulted into
one of the three meanings.

### 4. E4.3 -- answered as a REFUSAL, and per-series decomposition made structural

See Verification. The per-series form is now enforced by shape, not convention: `series()`
always returns `by_tool`, `dual_basis_compare()` always returns `per_tool_disagreements`, and
a test goes RED if the decomposition collapses. No aggregate can ship unaccompanied because
the function does not offer that shape.

---

## Decisions Made

1. **Measured before building.** The dispatch read as a build order; the estate said two
   thirds existed. Reporting that scope correction beat delivering a duplicate.
2. **Meta-mutated every suite before trusting it.** All three suites passed on first write,
   which is exactly when a suite is least trustworthy. I broke the source each guards and
   confirmed RED (5 separate meta-mutants), restoring byte-identical every time.
3. **Refused to attach a cause to rc=120.** Two hypotheses tested, BOTH REFUTED. Left it as
   `undeclared_rc` and an owned item rather than picking a plausible bucket.
4. **Declared `kind: usage` for comp-pipescript rc1/rc2 ONLY** -- transcribing the owner's
   own meaning text, not authoring semantics. Deliberately left `comp-keys:rc1` /
   `comp-kuzu:rc1` / `comp-routes:rc1` unkinded: "tool/input error" is genuinely ambiguous
   and picking a side would be me deciding a semantic I do not own.
5. **Did NOT override the comp-system gate.** The drift included an untracked PEER file;
   regenerating 06 would fold their uncommitted work into my commit. Split the commit and
   held the yaml, as the gate itself instructed.
6. **Did NOT use `--force` on the owned-paths block.** Routed the lane grant to COO (SoD: the
   grantee does not commit its own grant).
7. **Disclosed that my first commit landed inside the lane-enforcement-off window** rather
   than quietly benefiting from a gate that was failing open.

---

## Files Modified

| File | Change | Commit |
|---|---|---|
| `org/modules/graph/tests/test_e41_verdict_derivation_mutants.py` | NEW, 12 traps | `39dffb3af7` |
| `org/modules/graph/comp_msbeff_rebaseline.py` | +324: basis ids, dual-basis emit, series(), dual_basis_compare(), corpus_profile() | `631e71f4b9` |
| `org/modules/graph/comp_output_contract.py` | +116: fail-kind vocabulary, `classify_fail_kind()`, `fail_kind_coverage()` | `a580011c3d` |
| `org/modules/graph/comp_log_auto.py` | +31/-1: typed `fail_kind` + `synthetic` on the run row, additive optional keys | `a580011c3d` |
| `org/modules/graph/comp-output-contracts.yaml` | `kind: usage` x2 + header vocabulary | **HELD** (comp-system peer-landing) |
| `org/modules/graph/tests/test_e413_dual_basis_preservation.py` | NEW, 10 traps | **BLOCKED** (lane) |
| `org/modules/graph/tests/test_e42_fail_kind_separation.py` | NEW, 11 traps | **BLOCKED** (lane) |
| `.gitignore` | ignore the derived dual-basis sidecar + meta | **BLOCKED** (lane BASE_EXEC) |

---

## Verification

```
=== E4.1.3 DUAL-BASIS EXERCISE -- both queries RUN on the live corpus ===
corpus : org/mcp/comp-tool-runs.jsonl
rows   : 10259   span: 2026-07-14T02:37:44Z -> 2026-07-30T05:53:07Z (16.14 days)
months : 2026-07(n=10259)
basis A: as-written                     n=10261  FAIL=592  rate=5.77%
basis B: derived@v1+f09dab0e757496ea    n=10261  FAIL= 87  rate=0.85%   DIFFERS: YES
VERDICT: EXERCISED -- the two bases return DIFFERENT series, so the basis switch is wired

-- PER-SERIES DECOMPOSITION (this is the finding, not the aggregate) --
  comp-pulse      n=3418  FAIL 358 -> 0   (10.47% -> 0.00%)
  comp-system     n=625   FAIL  59 -> 0   ( 9.44% -> 0.00%)
  comp-blast      n=99    FAIL  45 -> 5   (45.45% -> 5.05%)
  comp-constants  n=36    FAIL  17 -> 0   (47.22% -> 0.00%)
  + 12 more tools each moving to 0
```

**So the headline improvement is the verdict LOGIC being corrected, not the estate getting
better.** comp-pulse alone is 358 of the 505 corrected rows.

```
=== E4.2 -- the 87-row post-M3 FAIL population, TYPED ===
  usage_error       33   comp-pipescript rc2 (22) + rc1 (11)   [declared]
  kind_undeclared   32   comp-kuzu rc1 (30) + comp-keys rc1 (2)
  undeclared_rc     22   rc=120 x 5 tools (18) + comp-dataflow rc2 (3) + comp-routes rc2 (1)
  negative_control   6
fail_kind coverage: 7 declared fail-exits, 2 kinded, 5 NOT --
  comp-keys:rc1, comp-kuzu:rc1, comp-legacywriter:rc2, comp-routes:rc1, comp-semantic-estates:rc2

=== LIVE end-to-end through the REAL shim into the REAL sink ===
comp-pipescript io                    -> rc2  result=FAIL                        fail_kind=usage_error
COMP_SYNTHETIC_FIXTURE=1 ... io <arg> -> rc2  result=FAIL (SYNTHETIC TEST FIXTURE) fail_kind=negative_control synthetic=True
comp-kuzu rc1                         -> rc1  result=FAIL                        fail_kind=kind_undeclared
PASS rows                             -> key OMITTED (not null)
```

**E4.3 -- C5 is NOT re-derivable, and that is the result.** The markdown corpus (26,248 rows,
2026-04..07) reproduces C5 exactly (12.30 / 12.74 / 9.37 / **6.14**) but has NO rc column and
a free-text result cell (`PASS`, `FAIL`, `PARTIAL`, `WARN`, `1162 nodes/940 edges`), so it
cannot be re-verdicted at any price. The rc-bearing sink spans 16.15 days / ONE month. The
corpus that carries the trend cannot be corrected; the corpus that can be corrected cannot
carry the trend. A defensible multi-month trend must be REBUILT FORWARD.

C5's April reconciled to the row: C5 said 221/12.14%, `startswith("FAIL")` gives 224/12.30%,
delta = **exactly the 3 `FAIL->FIXED` rows.** Two honest predicates sharing one word. The
predicate now ships with every series.

**Denominator disclosures:** an undeclared tool cannot contribute a FAIL by construction, so
declared-only is 9,789 rows / 0.89% while 106 nonzero rows are structurally invisible to
FAIL. The 50 undeclared tools are **71% of the roster but only 4.5% of the traffic.**

**rc=120 -- cause UNDETERMINED, two hypotheses REFUTED:** H1 harness-rc corruption (LD-0340
class) refuted -- the rate ROSE across MSTR's 07-28 mount fix (0.120% -> 0.727%); a fix
cannot raise the rate of what it fixes. H2 CPython exit-120 stdout-flush-on-closed-pipe
refuted by exercise -- piped python exits 1, and `comp-opalbizsem --list` exits 2 both piped
and unpiped. 19 rows, 6 tools, no contract declares it.

**Tests:** 33/33 green. 5 meta-mutants each proven RED, each restored byte-identical (oc
`28fe851dee45dc82`, mcc `06a9c1bd8d6f16fe`, rb `934e2d3b5946419c`), `git diff` clean of
residue.

---

## Blockers

**None are mine to clear; all three are correctly-functioning gates or another lane's work.**

1. **[2.0.0_SA_COO] LANE GRANT** -- `org/modules/graph/tests/**` is lane NFRA_TOOLCHECK_P4
   (0.8.0_AE_CloudComp + DS~B), not 0.7.0. **21 of my 33 mutant traps are untracked and
   uncommittable by me.** Both files are gate-clean and meta-mutant-verified. The lane's own
   note carries the precedent and quotes 0.7.0_AE_CloudOps by name for the R2 principle. Not
   using `--force`; SoD says the grantor lands it.
2. **[2.0.0_SA_COO] `.gitignore` one line** -- lane BASE_EXEC. Without it the derived
   dual-basis sidecar dirties every agent's tree on every run.
3. **[peer / self, on landing] comp-system BLOCKED-ON-PEER-LANDING** on
   `comp-output-contracts.yaml`. Source drift includes untracked
   `org/modules/graph/types-index/MdpfAggregateAUATimeSeries.yaml` (not mine). Did not
   override, did not regenerate. **Consequence stated plainly: the E4.2 CODE is committed but
   the `kind: usage` DECLARATIONS are not, so on a fresh checkout comp-pipescript rc1/rc2
   render `kind_undeclared` rather than `usage_error`. My measured "usage_error 33" currently
   depends on an uncommitted file and is not reproducible from the tree until that yaml
   lands.** Degraded-but-honest, not wrong. I land it the moment the peer's file does.

**Disclosure, not a blocker:** `1b0cad9305` reports lane enforcement was silently OFF for ~6h
while the audit log recorded "PASS (all paths in-lane)". My commit `39dffb3af7` landed BEFORE
that fix, writing to the same lane that now blocks me -- so
`test_e41_verdict_derivation_mutants.py` is in the tree having passed a gate that was failing
open, not one that cleared it. Verified genuinely at HEAD (positive control: 2 matches for a
line I know is in the file) and `39dffb3af7` is an ancestor of HEAD. COO's call: grant the
lane, or I relocate both files.

---

## Current State

Wave-1 measurement plane is COMPLETE and exercised. 3 commits landed; 1 yaml + 2 test files
held behind gates at other lanes. 33/33 tests green against current HEAD. Zero crons armed.
Broker summary set to BLOCKED-ON-PEER with the three holds named.

**R8: NOT started, NOT foreclosed.** Both new keys are additive and OPTIONAL, omitted when
inapplicable; the re-baseline reads `rc`, not any field I added. A later `route_id` needs no
schema migration and no telemetry re-baseline. No appender decision pre-empted R8 in either
direction, so there was nothing to bring COO before landing.

**No Terraform run**, so no HALTGT race with `~A`'s hard Aug-1 10:00 ET ETFS clock. Coordinated
with `~A` directly per COO (20260730T062538Z), including three comp-pipescript cautions
relevant to its deploy-verify path.

---

## Next Steps

1. **[2.0.0_SA_COO]** Land the two lane grants (tests/** + `.gitignore`), or rule that I
   relocate. 21 traps are outside the tree until then.
2. **[0.7.0_AE_CloudOps]** Land the held `kind: usage` yaml the moment
   `types-index/MdpfAggregateAUATimeSeries.yaml` lands and comp-system 06 is regenerable
   without sweeping a peer.
3. **[2.0.0_SA_COO]** Pick between (a) spec the forward-rebuild for a defensible multi-month
   trend, or (b) chase the 5 outstanding `kind:` declarations + rc=120 with the tool owners.
   Both touch other lanes so I am not choosing unilaterally.
4. **[tool owners, via 2.0.0_SA_COO]** Declare `comp-kuzu:rc1` (30 rows, highest-value single
   declaration open) and explain rc=120 across comp-kuzu / comp-blast / comp-pipescript /
   comp-iam / comp-drift / comp-opalbizsem.
5. **[2.0.0_SA_COO / 3.0.0_SA_CVO]** Fix `org/ref/SESSION_LOG_STANDARD.md:34` -- it instructs
   every agent to append to the retired `org/compiler-tools-log.md`.
