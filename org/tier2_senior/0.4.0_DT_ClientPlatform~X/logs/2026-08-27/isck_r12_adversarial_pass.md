# The instruments were the subject: two ISCK rounds, five findings, three self-retractions — 0.4.0_DT_ClientPlatform~X

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, DIAGNOSE

**Date:** 2026-08-27
**Task Order:** D11 ISCK v0 adversarial pass (Andrew release @8ba18439dd, ruling item 2) — ad-hoc, scoped
**Status:** COMPLETE (both rounds delivered; standing units armed for the next cited landing)

---

## Objective

Attack `org/standards/isck/` per `1.0.0_SA_CTO~X`'s charter as one of three released seats, dividing by
METHOD so overlap is corroboration. Nothing else was released; the pass was the whole scope. Round 2
extended to per-batch re-differencing, a probe-swap against `2.0.0_SA_COO~X`'s modules, and landing two
authorized battery additions.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | A.3 exercise half — a forwarder RAN, not merely resolved |
| PATH denominator probe | XXX.md A.3 loop over `.tools/comp-*` | PASS | 105 of 105 resolve bare |
| commit-gate.sh | `commit-gate.sh org/standards/isck/isck_coverage_probes.py` | PASS | clean both landings (py_compile + ds-precommit + ruff py39) |
| safe-commit.sh | `-F <msgfile>` + `GIT_COMMIT_AUTHOR_OVERRIDE=ANY_EXEC` | PASS | lane refusal surfaced correctly first; msg-verify MATCH both times |
| to-check.py | `--all --assignee 0.4.0_DT_ClientPlatform~X` | WARN | 0 for the tilde lane (known-broken per XXX.md); base positive control returned 1 |
| run_gates.sh | `run_gates.sh c3be1721d9` | PASS | atomic-extract runner — produced my only CITABLE gate numbers |
| git show / git archive | `git show <commit>:<path>` into a clean dir | PASS | the decisive instrument for DT-R2-3; positive control run before each ABSENT verdict |

**What worked:** `run_gates.sh` (landed mid-session as the remedy to my own DT-R2-3) turned every number
I quote into a statement about a nameable commit. `git show`-into-a-clean-directory settled a
three-instrument disagreement in one command.
**What failed:** `to-check.py --assignee` returns 0 for tilde lanes — already documented in XXX.md, so
I ran the base-serial positive control rather than reading the zero as "I hold nothing."
**Gap found:** No comp-tool answers "what does this schema NOT constrain?" — that gap is what the two
commits below fill, and it is why the arms exist separately from `validate_isck.py`.

---

## Work Completed

### 1. Startup + reachability
Registered `0.4.0_DT_ClientPlatform~X` (PID 24504). No orphan watcher existed for this serial — verified
by `ps` before arming, per the ORPHAN HAZARD discriminator (liveness PID vs my PID). Persistent Monitor
armed (task `b5ul6cbhj`) and confirmed by a consumer-only oracle: it delivered every message this session.
Zero crons. Session serial file written.

### 2. Round 1 — six findings, all upheld
Instrument: driving `jsonschema` directly, validating against the SINGLE `$defs` branch a record's
`record_type` claims (bypassing the root `oneOf`, which collapses every failure into one undifferentiated
error) and scoring the KEYWORD + `absolute_path` of each leaf error. Distinct from the other two seats,
which attacked the prose.

| ID | Finding | Severity |
|----|---------|----------|
| DT-1 | `failure_state=partial` reached by NEITHER conditional — a fingerprint travels with no method/normalization, breaking LAW 2, the law the contract calls "now mechanical". 1 of 5; other 4 reject the identical shape | HIGH |
| DT-2 | sec-6 limits not MECE — 1 of 5 entries is a real expressibility limit; 4 structurally inexpressible classes undeclared (referential resolution, field-pair comparison, vocabulary membership, serial uniqueness) | HIGH |
| DT-3 | registered vocabularies have NO consuming half — schema cannot distinguish an ADDITION from a TYPO (`fiel`, `gti` both validate) | HIGH |
| DT-4 | `status=closed` with `valid_to=null` — LAW 3's interval closes without a close | MEDIUM |
| DT-5 | a failed instrument keeps `fingerprint_method` + `normalization_version` — LAW 2's mirror | MEDIUM |
| DT-6 | `bundle_completeness=complete` had ZERO positive fixture coverage; only a negative mutant touched the arm | MEDIUM |

DT-1's generalization was adopted into ISCK doctrine: **MECE over a VALUE DOMAIN does not imply MECE over
the CONDITIONAL COVERAGE of those values**; Rule 24 postulate (iv) binds conditionals, not only value lists.

### 3. DT-7 / DT-8 — found BY the tool, not by hand
Staging the authorized module, the generalized ARM 1 emitted `entity_binding.fabric_scope` as a coverage
gap on its first run, unprompted. Adjudicated: `fabric_invariant` + `fabric_id: laptop` VALIDATES — a
binding claiming to hold on every fabric while pinning one. DT-8 followed: LAW 4's "where device-local" was
inexpressible in the two record types LAW 4 names first, because neither carried a scope discriminant.
Remedy adopted my postulate-(ii) framing — one model of device-locality across three records.

### 4. Round 2 — per-batch ARM-1 re-differencing (ratified standing unit)
Measured the mint-rate across four cited commits:

| tip | value-keyed discriminants | candidate gaps | unconditioned record types |
|-----|---------------------------|----------------|-----------------------------|
| `14e6bcc50d` | 11 | 6 | 4 |
| `b2d01ac6ae` (batch 1) | 13 | 8 | 3 |
| `5ffb98936c` (batch 2) | 14 | 9 | 2 |
| `9fa5a91af5` (R2-1) | 13 | 9 | 2 |

**CONDITIONING A RECORD MINTS UNCOVERED VALUES** — every conditional binds one value and leaves its
siblings unreached by construction. Established as a mechanism, not an inference, with the cause identified
at each step. Operational consequence adopted: the differencing runs after EVERY batch, not once at a
boundary.

Findings: **DT-R2-1** (a materializer ACTIVE and SUPERSEDED simultaneously), **DT-R2-2** (a five-value
shared enum bound at one value against the contract's own doctrine — later self-retracted, see §7),
**DT-R2-5** (the paired-arm idiom broke in the batch that adopted it: `entity` active + `adjudicated_by`
validates, and the same shape one record over). All upheld and landed by the integrator.

### 5. DT-R2-3 — the process finding, and the largest of the session
Running peer gates against the live working tree returned `ERROR: 2 mutants ACCEPT` — which reads exactly
like F5's warrant remedy having been silently lost. It had not been. Three instruments settled it:
`git show 27f97ac4fd:<path>` showed mutants AND their arms in the SAME commit; a clean extract of that
commit ran GREEN; and the mutant COUNT gave the mechanism away — **43 at the commit, 47 in the tree.**
The tree was four mutants ahead of its own schema.

**A COMMIT IS ATOMIC; A WORKING TREE IS NOT.** No self-control in any suite can see this, because the
instrument and its control read the same torn bytes. The direction that decided it: I hit a FALSE RED,
which is loud and self-correcting; reverse the save order and the same window yields a FALSE GREEN, over
which nobody investigates. UPHELD and remedied by `1.0.0_SA_CTO~X` as `run_gates.sh <commit>` (atomic
extract, provenance-stamped, absent-gate-counts-as-FAIL). It later bit its own author's integrator
mid-batch, which is the only kind of discipline that holds.

### 6. Probe-swap, both halves
Mine against `2.0.0_SA_COO~X`'s four modules: DT-R2-3 above (a package property, mine included) and
**DT-R2-4** — isolation is a PROXY for "every rule has a detecting mutant"; ablation measures that
DIRECTLY and reported GREEN on the same extract, so where they disagree the direct measurement wins.
Their half against mine returned "I found nothing wrong with the module; the finding is at the SEAM" —
COO-R2-1, that `run_gates.sh` declares a failing-class/reporting-class model its loop does not implement,
so a reporting gate's findings scroll past inside a line reading `exit 0`. I corroborated it and accepted
the underlying criticism of my own design: exit-0-on-findings is right for a reporting instrument only if
the findings reach the summary; I built the first half and relied on a reader for the second.

### 7. Two landings + ARM 4
`c7fb383f50` — ARMs 1-3, the last outstanding landing, which opened round 2.
`c3be1721d9` — ARM 4 (paired-arm coverage) + the census debt discharged to **73 of 73 inhabitable, 0
unreachable, 0 open**, with a negative control proving an irrelevant repair does NOT close a value.
ARM 4 found its own false-positive class before shipping: v1 read only top-level `then`, so R2-1's NESTED
forbid (`then:{allOf:[...,{not:{required:[G]}}]}`) made it score FOUR correctly-paired arms as
REQUIRE-ONLY. v2 walks nested combinators, recognises three pairing effects, reports unparsed then-keywords
rather than scoring them unpaired, and ships a REGRESSION SELF-CONTROL for that exact bug.

### 8. R2-1 verification — the one landing that survived
Five probes each on two records at a clean extract of `9fa5a91af5`: all PROTECTED, including the headline
contradiction both external reviews named. **I did not stop at the uniform pass** — ten-of-ten is an
instrument signature as readily as a defect signature — so I ran the discriminating control: coherent forms
VALIDATE, incoherent REJECT. The arms discriminate; R2-1's two-directional claim is MEASURED, not assumed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Kept sec-6 detail from `3.0.0_SA_CVO~X` deliberately | Charter buys corroboration only while the second instrument is independent; a seat reading my findings then confirming them is Rule 22 repetition wearing a second serial. Integrator re-ruled in favour of the blind. |
| Did NOT clear the `.git/index.lock` myself | Live PID, another seat's in-flight commit, that seat under an active disposition at Andrew. Named the exact remedy and the owner instead. It later completed on its own — Andrew was driving that terminal. |
| Did NOT self-grant `GIT_COMMIT_AUTHOR_OVERRIDE` on the lane refusal | An agent-side self-grant against a standing gate is what the audit line exists to make visible, not to enable. Asked; both overrides were then explicitly authorized and singular. |
| Treated neither override as standing | Each landing asked separately; the integrator confirmed the reading was correct and is why both grants are clean. |
| Shipped ARM 1 / ARM 4 as CANDIDATE GENERATORS with stated precision | ARM 1 fell from 2-of-2 real at v0 to 1-of-6 at v0.1 — it gets LESS precise as the schema improves, because good fixes use mechanisms it cannot count. Stating that beats it being discovered as a false-red machine two batches on. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/standards/isck/isck_coverage_probes.py` | New — ARMs 1-3 + self-controls (502 lines) | Yes — `c7fb383f50` (ON ORIGIN, ls-remote read) |
| `org/standards/isck/isck_coverage_probes.py` | ARM 4, 7+4 census repairs, 3 non-ASCII removed (+211/-4) | Yes — `c3be1721d9` (ON ORIGIN, ls-remote read) |
| `~/.claude/.../memory/*.md` | 2 memory entries + MEMORY.md pointers (conditional-coverage MECE; working-tree atomicity) | No — memory dir, not repo |

---

## Blockers

**NONE.** Two blockers arose and both cleared: the fabric-wide `index.lock` outage (~10 min, surfaced at
`76529`-`76532`, resolved when the holding commit completed) and the `ANY_EXEC` lane refusal on
`org/standards/` (resolved by explicit authorization at `76583` / `76661`). Neither is open.

---

## Current State

The D11 ISCK adversarial pass is through two rounds with all four gates plus both probe suites GREEN at
`3c37267b91` (`RUN_GATES` overall exit 0 — the package's first all-green atomic verification). My two
commits `c7fb383f50` and `c3be1721d9` are ON ORIGIN and carry `org/standards/isck/isck_coverage_probes.py`,
a four-arm suite complementary to `validate_isck.py`: ARM 1 conditional-coverage differencing, ARM 2
branch-scoped rejection attribution (2a keyword / 2b coupled-field), ARM 3 enum inhabitability (73/73, no
dead values), ARM 4 paired-arm coverage. Eight self-controls, all two-directional. ARM 1 and ARM 4 emit
CANDIDATES requiring adjudication — never findings — and both print their own blind spots: ARM 1 cannot see
a record with no discriminant (currently `source_frontier`, `surface_version`), and its precision degrades
as the schema improves. Cite any number from this suite via `run_gates.sh <commit>`, never from a working
tree. Round-2 open work is DESIGN, not repair: R2-5 absence cell, R2-8 BRIDGE_ASSERTION, R2-2 doc, R2-7
mint receipt, and ARM 4's 16 require-only candidates awaiting semantic adjudication.

---

## Next Steps

1. **Fire ARM-1 + ARM-4 on the next cited landing** — ratified standing per-batch units; the mint-rate
   series only stays measurable if it runs every batch rather than at a boundary.
2. **Adjudicate ARM 4's 16 require-only candidates** — the discriminator is semantic (harmless
   over-supply vs presence-contradicts-value) and roughly 4 are expected real. Splits between this seat and
   [`3.0.0_SA_CVO~X`]'s rubric, which already holds `delta_summary`-on-verified and `human_adjudicated`.
3. **Add a machine-readable finding count to the module IF [`1.0.0_SA_CTO~X`] takes remedy (b) on
   COO-R2-1** — four lines; I am not treating either prior override as standing, so it needs a word.
4. **[`1.0.0_SA_CTO~X`]** — my registered prediction's clustering half remains UNSETTLED and ARM 1 is
   structurally recused from adjudicating it; the instruments that can see discriminant-free records are
   [`4.0.0_SA_CRO~X`]'s review and [`2.0.0_SA_COO~X`]'s four-unconditioned-types attack.

---

## MCP Traffic

~30 messages handled, all ACKed via `ack_messages` (the READ clock). Significant: the release charter
(`76361`), six round-1 dispositions (all findings upheld), the blind-protocol re-ruling (`76457`), the
Edge-1 independence downgrade (`76472`) and its acceptance at my stated width (`76480`), both override
authorizations (`76583`, `76661`), and the probe-swap exchange with [`2.0.0_SA_COO~X`] (`76687` in,
`76648` out). Outbound: 9 substantive reports including one fabric-wide BLOCKING escalation to four seats.

---

## Self-Corrections (recorded because they are the load-bearing half)

1. **Retracted my own "REFUTED" verdict** on the registered prediction — I read ARM 1's zero over the
   unconditioned types as absence THREE PARAGRAPHS after documenting, in the same commit message, that the
   zero means blindness. Documentation of a limit is not immunity to it. Retracted at `76620`; the honest
   three-state (RETRACTED / SUPPORTED / UNSETTLED) is in the boundary record verbatim.
2. **Retracted DT-R2-2's weight** — true when filed against `b2d01ac6ae`, closed by the tip before
   disposition. Second time the fabric outran a finding between writing and disposition.
3. **Killed my own census "DEAD" row** before reporting it — `fabric_scope=device_local` read UNREACHABLE
   because my probe substituted one field and the conditional demanded a companion. Probe artifact, not a
   schema defect; the repair-before-verdict logic that caught it now ships in ARM 3.
4. **Caught a pipe artifact** — an early `rc=$?` read `tail`'s status, not python's, and nearly became a
   filed finding that four gates exit 0 on failure. They exit 1. Measured properly before reporting.
