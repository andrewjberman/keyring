# NFRA_COMPEFFICACY — comp-tool efficacy: every named comp-tool validated per-tool, remediated, and CLEARED

**Directive:** D11 Substrate/Tooling Enhancements (Andrew-direct 2026-09-02, VERBATIM: *"This would go in D11
Substrate/Tooling."*) · **Fabric:** laptop (D11 placement row; membership and fabric agree, per the ETFS_GUARDRAIL
D8 precedent) · **dep_stage:** PRD
**Author:** `3.0.0_SA_CVO` (driver, Andrew-designated comp-tool lane @`98b1a59907`) · **Executor:** `0.8.0_AE_CloudComp`
(Andrew-direct @`1bb6769055`) · **Sequencer:** `2.0.0_SA_COO` · **PRD gate:** `1.0.0_SA_CTO` · **Register owner:** `0.0.0_AB_MSTR`
**Version:** v0.1, 2026-09-02 · **Vintage of every measurement below:** repo HEAD `f90ab3936b` unless a cell pins otherwise
**archetype:** IMPLEMENT (spec) / VALIDATE (rows)

```json
{
 "project": "NFRA_COMPEFFICACY",
 "directive": "D11",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md@f90ab3936b",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```
*PRD_HEADER block (`org/standards/PRD_HEADER.schema.json`; limb 5 of `to-pipeline-gate.py` @`689960ce16`). `brief_ref` is
the Andrew-direct RECORD, not a `docs/briefs` file — admitted by the pattern widened @`75ead40079` on this seat's Rule 24
finding. `status` flips to `RATIFIED` when `1.0.0_SA_CTO` lands this at `docs/architecture/NFRA_COMPEFFICACY_PRD.md`.*

---

## 0. AUTHORITY — his words, verbatim

Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md`
@`f90ab3936b`. The operative clauses:

> "...draft a spec that covers end to end how to validate and streamline their purpose, how they are called, their
> timeout and pagination mechanics, any disclosures on denominator/coverage/risk factors. I need you to drive this
> project with 0.8.0_AE_CloudComp to completion where the desired final output is complete efficacy with all of
> these functions, this is why I had CRO send you the passcraft analysis, to assist in your validation and
> remediation process for these tools. I think you need to start by listing/enumerating the tool list we described
> and then we methodically go through all of them, whereby you hand off the list to 0.8.0_AE, they go through each
> tool and return results in a specified schema deliverable that covers everything we need, you review those and
> mark the tool cleared. This is one project I need you to proceed, i think while you are on the subject we can also
> have you and 0.8.0_AE address the globgraph-cloud-compile-and-gateway-traversal-20260901.md brief that CRO did
> yesterday since it is directly related to the efficacy of these tools."

> "This would go in D11 Substrate/Tooling."

Prior word, same thread (CloudComp terminal ~16:53Z, @`1bb6769055`): *"...team up with CVO Base ... comprehensive
audit and fix of the tools of interest, and I want them to parallelize that work through a delegation process with you."*

**Two rulings he has separately given that bind rows below:** *"comp-kuzu/kuzu-inc should be consolidated as
described"* (held on the KUZUSPLIT reconciliation now at him — §6 R-3) and *"comp-trace ... if so it should be
retired"* (condition met — §7 row T-19).

---

## ENDPOINT (step 2, /endpoint --forward)

Emitted from his words alone, before any task order exists. `FWD-n` ids are **permanent and never reused**; a retired
outcome leaves its number vacant.

> ⛔ **"Frozen" is a CONTRACT here, not a CONTROL** — measured by this seat 2026-09-02 against its own gate:
> `.tools/surprise-row-gate.py:53` @`c6c3627269` validates `outcome_ref` by SHAPE (`^FWD-[0-9]+$`), never by
> existence. A row citing a FWD-n that was never cut passes. Named so the word is not read as a mechanism.

```
  FWD-1  Every comp-tool on his list has been examined against ONE schema, and the
         result for each is on the record in that schema
         DONE WHEN  EXERCISED -- N per-tool deliverables exist, one per enumerated tool,
                    each conforming to s.4's schema, each graded by CVO
         ACCEPT     the enumerated list (s.7) has no row without a graded deliverable;
                    the two tools that do not exist are recorded as such, not skipped
         SOURCE     "start by listing/enumerating ... hand off the list ... return results
                    in a specified schema deliverable ... you review those and mark the
                    tool cleared"

  FWD-2  A tool that cannot answer says so in a way a machine can reject, instead of
         returning a zero that reads like an answer
         DONE WHEN  EXERCISED -- for every CLEARED tool, a known-absent subject, a
                    present-with-zero-result subject, and a not-decidable case each
                    produce a DIFFERENT, rejectable answer-state
         ACCEPT     the four-state distinction of s.4.3 holds on every CLEARED tool,
                    tested with a planted case per state, not asserted
         SOURCE     "any disclosures on denominator/coverage/risk factors"; CVO~A brief s.3

  FWD-3  Every CLEARED tool prints where it looked, how much, and how old
         DONE WHEN  EXERCISED -- engine path (not shim), corpus/backend, vintage,
                    denominator, resolved/unresolved counts appear on a live run
         ACCEPT     s.4.2's disclosure fields present on every CLEARED tool's default
                    output, verified by a reader who did not write the tool
         SOURCE     "their timeout and pagination mechanics, any disclosures on
                    denominator/coverage"; comp-similar D1-D3 (2026-09-02) is the
                    exemplar of the defect and its repair

  FWD-4  A long or wide scan tells the operator what it did NOT finish, instead of
         stopping silently
         DONE WHEN  EXERCISED -- a CLEARED tool driven past its ceiling (time or size)
                    emits a truncation/timeout disclosure carrying the reached
                    denominator, and that disclosure is distinguishable from a clean
                    empty result
         ACCEPT     s.4.4 holds: no CLEARED tool has an unbounded subprocess; every
                    bound is disclosed at the ceiling; pagination, where present, prints
                    PAGE i of N and the true total
         SOURCE     "when we issue a timeout or if there's a default timeout ... we need
                    to know what's being truncated" (transcript 1056); MEASURED 76 of 94
                    implementations set no explicit timeout, 5 of 106 paginate

  FWD-5  Redundant tools are named as redundant with evidence, and the ones he
         separately ruled on are consolidated
         DONE WHEN  EXERCISED -- comp-trace retired into comp-blast (his conditional
                    ruling, condition met); comp-kuzu/-inc/-full resolved per his
                    KUZUSPLIT reconciliation; comp-dups disposed by its owner; every
                    other candidate carries a finding with an owner, not an act
         ACCEPT     no tool is retired on this project's judgment alone; every
                    retirement cites his word or the owner's disposition
         SOURCE     "retire/archive groups of comp-tools and elevate a few to the
                    marquis list" -- a direction of inquiry; "if so it should be retired"
                    -- a ruling

  FWD-6  A tool cleared here stays cleared: the fix reaches the shared branch and the
         tool has a battery that can go red
         DONE WHEN  EXERCISED -- every CLEARED tool's remediation commit is ON origin
                    (measured by is-ancestor, not claimed), and its battery collects >0
                    tests under the runner the gates use, with a planted mutant that
                    reddens it
         ACCEPT     no CLEARED status is granted on a LOCAL commit; comp-find, which has
                    3,722 invocations/30d and NO battery, gains one
         SOURCE     CVO~A brief NON-GOALS: "Do not leave a fix local: integration/
                    version availability is part of completion"; 92625 s.5(b)

  FWD-7  The agent-facing graph tools answer from a graph whose age is bounded and
         disclosed, and the freshness surface points at the artifact agents actually
         read
         DONE WHEN  EXERCISED -- comp-graph status reports kuzu_nessie_db (not the two
                    legacy artifacts); every graph-derived answer from comp-kuzu /
                    comp-similar / comp-estate carries the DB's built: vintage; the
                    stale-served path (F5) is either bounded by a schedule or the
                    bound is stated on the answer
         ACCEPT     globgrph brief O3/O3b/O7 on the agent surface; F6 corrected; F4's
                    QUALIFIED verdict carried or fixed, never silently ported
         SOURCE     "address the globgraph-cloud-compile-and-gateway-traversal brief
                    ... directly related to the efficacy of these tools"; brief F4-F6
```

**Not cut, deliberately:** an outcome for "the marquis list." He said *"we may want to"* — the enumeration and
evidence in s.7 make that decision possible; making it is his.

> ⛔ **BINDING ON FWD-7 AND THE G-ROWS — Andrew-direct 2026-09-02 ~18:12Z, VERBATIM:** *"right now i think the
> estate pipeline is probably junk for the most part, until the tools at the front of that pipeline are properly
> rectified and generating real outputs/data, i dont think that pipeline makes sense to analyze analyses from."*
> **So the daily Semantic Evolution Pipeline is DOWNSTREAM of this project, not beside it.** Its outputs are not
> adjudicated until the tools it consumes are CLEARED here (the 24 PENDING manifest days stay PENDING by his word).
> This matches the measurement in §7 rows G-1..G-3 and the review §5b: the runner's propagation stratum returns
> `INSTRUMENT_UNAVAILABLE` daily and invokes zero comp-tools. **Not read into it:** stopping or changing the
> runner; it keeps running, nobody acts on its output. Record:
> `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1812Z_OPEN_CALLS_RULINGS_KUZU_ESTATE_NOTIFIER.md`.

---

## 1. The arc

The estate has **106 `comp-*` entrypoints over 94 distinct implementations**, and **61 of the 106 are wrappers**
that forward to an engine elsewhere. Measured 2026-09-02 across both usage instruments (because each is blind to
tools the other logs — the first defect this project found was in its own census): the top 20 tools carry
**99.6% of 30-day invocations**, so his instinct that ~20 tools matter is right. What is wrong is the coverage
underneath them: **5 of 106 paginate; 34 of 106 print a denominator; 18 of 94 set any timeout, with 14 different
constants nobody chose; 76 of 94 have no ceiling at all.** The most-run tool (comp-pulse, 8,364/30d) is a commit
hook that agents invoke by hand 5 times a month. The two most doctrinally central (comp-find, comp-read) were
invisible to the estate's own traffic feed until unit 1 landed today.

The same day produced the pattern this project exists to end, three times: **a tool that turns "subject absent",
"zero result" and "not decidable" into one answer.** comp-similar reported no vintage and its self-test scored the
missing half PASS (fixed @`b8a73cc064`). comp-pulse's traffic reads clean over a feed that omits comp-find. A
comp-kuzu build inside a call read as a laptop-local defect. Each was a correct number over the wrong denominator,
and each was caught by a second instrument, not by the tool.

**So the arc is not "make every tool cover everything."** It is: **every tool on his list tells the truth about its
own boundary, in fields a machine can reject on**, and the ones that are redundant are said to be — with evidence
and an owner — rather than quietly kept. CVO~A's brief states the bar exactly: *"A tool that clearly reports its
boundary is working; a tool that turns 'subject absent,' 'zero result,' and 'not decidable' into the same answer is
dangerous."*

**The method is his and it is prescribed** (s.0): enumerate (s.7) → one schema (s.4) → CloudComp fills it per tool →
CVO grades → CLEARED. The schema is the deliverable that makes the rest mechanical; it is authored here under
Rule 24 with its record and census (s.4.5).

---

## 2. Purpose — what DONE means

**DONE = "complete efficacy with all of these functions"** (his words), operationalised as: **every row in s.7 carries
a CVO-graded deliverable in the s.4 schema, and every row's disposition is one of:**

```
  CLEARED        the tool meets s.4.1-4.4 on a live run, its fix (if any) is ON origin,
                 and it has a battery that can go red
  RETIRED        on his word or the owner's disposition, with the replacement named and
                 callers redirected -- never on this project's judgment alone
  DOES-NOT-EXIST comp-hud, comp-legacy -- recorded, not dropped
  CARRIED        blocked on a named decision outside this project (e.g. R-3), with the
                 blocker's owner stated
```
No row may end in any other state. **A row that is "mostly fine" is not CLEARED.**

---

## 3. Territory — what this owns, and what it only relies on

| | |
|---|---|
| **OWNS** | the per-tool result **schema** (s.4); the **enumeration** (s.7) and each row's disposition; the **grading** of every CloudComp deliverable; the **disclosure contract** every CLEARED tool must meet; the **timeout/pagination policy** as a spec (s.4.4); the **globgrph brief workstream** at the agent-facing surface (FWD-7): `comp-graph status` correctness, vintage on graph-derived answers, the stale-served bound |
| **RELIES ON, does not own** | every tool's **code** (owner lanes; `0.8.0_AE_CloudComp` executes fixes in its lane, other lanes via placement); `.tools/tests` batteries (ownership at Andrew, CTO 92581); `comp-tool-hud.sh` and the rail (CloudComp by CTO ruling; the intermittency diagnosis is released there and this project CONSUMES it); `org/mcp/comp-tool-runs.jsonl` + `comp-which-rail.log` (the two usage instruments); `NFRA_PASSCRAFT`'s 8 moves + 12 shapes (`docs/architecture/NFRA_PASSCRAFT_PRD.md` @`362272cce2` §3a/3b — cited, never re-derived); the `boundary_report` type (`org/modules/graph/boundary_report.py`, dict-native — the disclosure contract is a sibling, not a rival) |
| **TOUCHES BUT MUST NOT CHANGE** | **`NFRA_KUZUSPLIT`'s full/inc semantics** — the NEVER-full property must survive any consolidation (§6 R-3); **`NFRA_GLOBGRPH`'s derive / Nessie / stitch** (CLOSED-COMPLETE; globgrph brief Part II puts them OUT); **CTO arch-gate ruling 3** separating comp-dups from comp-similar (the disposition is CTO's); **truthful non-application** — comp-schedule's NOT-DECIDABLE and comp-denytest's zero population are correct results and are not converted into work (CVO~A s.11) |

---

## 4. THE PER-TOOL RESULT SCHEMA — what `0.8.0_AE_CloudComp` returns for each tool, and what CVO grades

One file per tool: `org/projects/NFRA_COMPEFFICACY/results/<tool>.result.md`, one fenced JSON block + prose. Every
field is REQUIRED; a missing field is a non-conforming deliverable and is returned, not graded.

### 4.1 IDENTITY — the wrong-object trap, closed at the schema
```
  tool            the entrypoint name as typed                          e.g. comp-similar
  shim_path       .tools/<name>, with its line count                    e.g. .tools/comp-similar (38)
  engine_path     the RESOLVED implementation, read from the shim body  e.g. org/modules/graph/debtscan/comp_similar.py (538)
  engine_vintage  git log -1 --format=%h -- <engine_path>
  aliases         other entrypoints resolving to the same engine        e.g. comp-kuzu-inc -> kuzu_cli.py --mode inc
  purpose_1line   from the ENGINE's header, not the shim's
  self_identifies whether --help/--about prints engine_path + version    (CVO~A s.9; passcraft MOVE 1)
```
> Both of this seat's wrong-object errors today (comp-dups, comp-trace) were shim-header reads. The schema makes
> the engine the object; the shim is a pointer.

### 4.2 DISCLOSURE — what every default run must print (CVO~A s.3, adopted)
```
  subject               the exact subject the run examined
  corpus_or_backend     what was examined (repo corpus / kuzu DB / AWS plane / portal src / ...)
  vintage               corpus or build vintage, as the tool prints it     ABSENT is a finding
  denominator           N scanned, as printed                              ABSENT is a finding
  resolved_unresolved   counts, as printed
  blind_spots           declared blind spots, as printed                   (e.g. comp-iam "cannot answer deny")
  pagination            {none | PAGE i of N with true total | truncates silently}
  timeout               {none | explicit N s | inherited from caller}, and what is printed AT the ceiling
```
Each is graded PRESENT / ABSENT / PRESENT-BUT-WRONG with the run's own output quoted.

### 4.3 ANSWER-STATE — the four-way distinction, tested not asserted
For each tool, CloudComp plants one case per state and records what the tool printed:
```
  SUBJECT_ABSENT_FROM_CORPUS   the subject does not exist where the tool looks
  PRESENT_WITH_ZERO_RESULTS    the subject exists; the measured answer is genuinely zero
  PARTIAL_OR_BLIND             the tool examined part of the space and says which part
  NOT_APPLICABLE               the question does not apply to this subject/tool
```
**PASS** = four cases, four distinguishable outputs. **FAIL** = any two states print alike. This is FWD-2 and it is
the load-bearing test of the project. ⛔ **Rule 24 census on this enum is in s.4.5; it is NOT yet a shared enum**
in code — it is the GRADING vocabulary of this PRD until the census is adjudicated.

### 4.4 BOUNDS — timeout and pagination mechanics
```
  subprocess_timeouts   every timeout= in the engine, with value and what it wraps
  ceiling_behaviour     what the tool prints when it hits one (exercised, not read)
  page_contract         --page/--limit present? true total printed? "PAGE i of N"?
  size_invariance       does the ceiling scale with corpus width, or is it a constant?
```
**POSTURE — Andrew-approved 2026-09-02 ~18:38Z, VERBATIM: *"I agree with this posturing, incorporate it into the
document."*** Two rules, both size-invariant by construction; measured baseline in §4.4.1.

**RULE P (output): comp-find's page contract is the SHARED OUTPUT CONTRACT, not a shared library.** Every marquis
tool that can emit more than one page of rows carries `--limit` / `--page` / `--all`, prints `PAGE i of N` and the
**TRUE TOTAL on every page**, and treats a bare `--top N` that does not print what it dropped as **non-conforming**.
The consumer half already exists in law (CLAUDE.md Rule 21: never `head` a census; a page is not an answer).
Size-invariance comes from the page, never from making output smaller.

**RULE T (work): a tool never exceeds a ceiling it was not told.** Every marquis tool **accepts a budget** (flag or
env; default = the harness's 120s Bash ceiling), **spends it against the WORK, not the call**, and at expiry
**prints the reached denominator with a resume cursor** — *"scanned 12,400 of 144,933 when the 120s budget hit;
re-run `--page 2` / `--budget 600`."* A timeout thereby becomes a page boundary, not a kill. **P and T are one
solution:** a time budget that ends on a resumable cursor IS pagination over work. Internal `timeout=` constants
stay but must be **≤ the declared budget** or they are dead code.

**Non-application:** tools whose output is bounded by nature (`comp-which`, `comp-denytest`, `comp-schedule`'s five
carriers) carry Rule P's disclosure line and nothing else. **Reference implementations:** T-1 (`comp-find`) and
T-2 (`comp-read`) — the only two that already satisfy P; T binds them first. **Cost, stated:** T is a code change on
~18 marquis implementations; P on ~10.

#### 4.4.1 Measured baseline (2026-09-02, 20 marquis tools; help-text census + source grep)
```
  --page          2 of 20  (comp-find, comp-read)       --limit  3 of 20   --top  3 of 20   --all  4 of 20
  prints a true total when capped        8 of 20  (help-text heuristic -- weak; graded per tool in 4.2)
  knows / accepts the OUTER harness budget   0 of 19 implementations  (no BASH_*_TIMEOUT, --budget, deadline,
                                                                       SIGTERM handler, or alarm anywhere)
  outer ceiling the tools cannot see     120,000 ms default / 600,000 ms max (harness contract)
  inner ceilings                         18 of 94 set one; 14 distinct constants; comp-find's 600s EXCEEDS the outer
```
Live specimens the same day: comp-find killed silent at 120s twice (its 600s never reached); comp-similar imposing
180s on comp-kuzu from outside; the rail hook straddling its own 5s harness deadline and writing DENY rows for
searches that ran (fixed @`d2eb720bde` by raising the ceiling, confirmed at 4 of 4 Claude seats) — **every one is a
tool that did not know its budget.**

### 4.5 PASSCRAFT LEG — the 8 moves, run, and the shapes hunted
```
  moves_1_to_8    each: DONE / SLOT (hand-run) / N-A, with the falsifier's answer
  archetype       from the 12-shape taxonomy (comp-passcraft taxonomy), with lead probes hunted
  findings        each finding -> one of the 12 shapes, with file:line @ vintage
```
Cite `NFRA_PASSCRAFT_PRD.md` §3a/3b; do not restate the taxonomy in the deliverable.

### 4.6 USAGE + DISPOSITION PROPOSAL
```
  runs_30d        from BOTH instruments (runs.jsonl AND rail log), stated separately
  hook_driven     fraction of runs from a hook vs by hand
  battery         path, collects >0 under pytest?, has a red-first mutant?
  overlap         tools it duplicates or subsumes, with the EXECUTABLE-BODY evidence
  proposed        CLEARED-candidate | RETIRE-candidate (owner named) | CARRIED (blocker named)
```

### 4.7 Rule 24 four-postulate record for this schema (authored here; CVO does not self-certify — `1.0.0_SA_CTO` gates)
- **(i) MECE over a DECLARED domain.** Domain = the tools in s.7. Every row has exactly one deliverable; every
  deliverable maps to one row. The two nonexistent tools get a DOES-NOT-EXIST deliverable, not silence.
- **(ii) SAME GRAIN.** One deliverable = one ENGINE. Aliases (comp-kuzu-inc, comp-trace) are fields on their
  engine's deliverable, not separate deliverables — which is what makes the overlap visible.
- **(iii) INTENT COHERENCE.** One axis: *does this tool tell the truth about its boundary.* The schema is not a
  status tracker and must not grow a `done` column; disposition lives in s.7, not in the deliverable.
- **(iv) STATE COHERENCE.** The answer-state enum (4.3) classifies a RUN, never a tool. A tool is not "ABSENT"; a
  run's subject is. No remedy moves NOT_APPLICABLE — it is a correct result (CVO~A s.11).
- **Census — RUN 2026-09-02 ~17:5xZ (word-boundary, 8-token alternation, `corpus=all`): 653 hits across
  144,933 files; DEF=4 SURFACED=44 CONFIG=307 TEST=3 DOC=288.** Per-token in CODE/DEF bands of first-party
  source (comp-read `--enumerate`, whole-value):
  ```
    DECLARED-NOT-APPLICABLE   x5   .tools/to-pipeline-gate.py:46 DISPOSITION_RE       (this seat's gate)
    NOT-DECIDABLE             x3   .tools/comp-schedule (the decidability schema)        (this seat's tool)
    NOT_APPLICABLE            x2   org/modules/graph/nerves_resolve.py
    INSTRUMENT_UNAVAILABLE    x1   infra/aws/ec2/estate-report-runner/estate_report_runner.py
    SUBJECT_ABSENT            0    (the single estate-wide hit was THIS draft)
    PRESENT_WITH_ZERO         0
    OUT-OF-CORPUS             0 in CODE/DEF -- lives in comp-find's PROSE output + CLAUDE.md Rule 21
  ```
  **WHAT THE CENSUS SETTLES:** two of 4.3's four states already have LIVE carriers and must ADOPT, not mint —
  `NOT_DECIDABLE` → **`NOT-DECIDABLE`** (comp-schedule's spelling; hyphen), and `NOT_APPLICABLE` already exists
  in TWO spellings (`NOT_APPLICABLE` underscore in nerves_resolve; `DECLARED-NOT-APPLICABLE` hyphen in my own
  gate) — **that split is a finding this project inherits, not one it may paper over.** The other two states
  (`SUBJECT_ABSENT_FROM_CORPUS`, `PRESENT_WITH_ZERO_RESULTS`) have **no carrier anywhere in code** and are
  genuinely new; comp-find's `OUT-OF-CORPUS` prose is the nearest kin to the first and should be reconciled
  with it rather than duplicated. **Until the spellings are ratified (CTO gate), 4.3 binds deliverables by
  reading, not code by enforcement.** Cost of the census on this box: the 8-way alternation exceeded a 120s
  foreground ceiling twice and completed only in the background — itself a FWD-4 specimen on comp-find
  (its own 600s internal timeout exceeds the caller's ceiling, and nothing at the ceiling says so).

---

## 5. Out of scope — and truthful non-application is not work
- **Making blind tools fabricate** to satisfy a preflight (CVO~A NON-GOALS). A tool that prints NOT-DECIDABLE
  with a denominator has PASSED 4.3.
- **Widening every tool to every resource family.** ETFS is not added to comp-pipescript's registry because it
  appeared in one preflight (CVO~A s.9).
- **comp-schedule and comp-denytest remediation** on this run's evidence — both returned correct bounded results
  (CVO~A s.11). They are graded, not repaired.
- **The KUZUSPLIT semantics, the GLOBGRPH derive, D6 GraphQL, gateway auth** (globgrph brief Part II).
- **A cloud Kuzu coexisting indefinitely with a local Kuzu** — that is a duplicate output path and a NEVER (CLAUDE.md
  §5); any cloud port under FWD-7 is a port with a retirement or it is out of scope.
- **The marquis list decision.** Evidence yes; decision his.
- **Any gate.** Nothing here refuses anything. Andrew has not asked for one.

---

## 6. Rulings that BIND
- **R-1 (Andrew, 16:53Z):** team with CVO base; delegation-parallelised. Lane ownership unchanged (three seats
  concurred: 92605/92607/92611).
- **R-2 (Andrew, 17:15Z):** the method — enumerate → schema deliverable → CVO grades → CLEARED. This PRD is that method.
- **R-3 (Andrew, 2026-07-17, KUZUSPLIT O-3) vs (Andrew, 2026-09-02, "consolidate"):** same engine, two words on
  the CLI surface. **HELD at Andrew** — reconciliation options put to him via `/open-calls` CALL 1. No kuzu wrapper
  moves until his word.
- **R-4 (Andrew, 2026-09-02):** *"comp-trace ... if so it should be retired."* Condition MET (trace ⊂ blast at
  `cli.py:1478-1530`). Executable as row T-19 on the s.7 evidence.
- **R-5 (CTO arch-gate ruling 3, 2026-07-19):** comp-dups is its own tool, not a comp-similar mode. Disposition of
  comp-dups (0 runs ever) is CTO's.
- **R-6 (CLAUDE.md Rule 21, Andrew-direct 2026-08-28):** comp-find/comp-read are the rail. Their batteries and
  disclosure are P0 by traffic (3,722 + 2,401 / 30d).
- **R-7 (CVO adjudication 92566/92598, corroborated CTO 92568):** the rail log is a record of rows it managed to
  write, not a census of searches; no seat-coverage claim may be derived from it. Binds every usage figure here.

---

## 7. SURFACE MANIFEST (step 4 → step 5) — the enumeration, one row per ENGINE

Contract: the step-4 manifest as adopted @`ecaa7c7dcb` (amended: `claim: measured` requires a dated pin;
`BASIS_RANK` governs transitions). `outcome` = FWD-n. `claim` is about the SURFACE ADDRESS. `verb` ∈ {audit, fix,
retire, verify, record}. **Every row's lane is `0.8.0_AE_CloudComp` for `audit` unless stated; `fix` rows re-home to
the engine's owner if not CloudComp.** Usage = 30d, both instruments, at `f90ab3936b`.

| id | outcome | surface (engine) | claim | evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| T-1 | FWD-1,2,3,6 | `comp-find` → `.tools/comp-find` (Python, self-contained) | measured | 3,722 runs (rail); **unit 1 @`f34122edfb` ON origin — now also writes runs.jsonl (0→2 `comp_log_auto` calls), CLEARED by exercise at this seat**; paginates (Rule P reference); 600s internal timeout **exceeds the 120s outer ceiling — Rule T's first target** | CloudComp | audit+fix | — | 4.1-4.6 | **NO battery** (92625 s.5b) — FWD-6 gate; Rule T budget + reached-denominator at expiry |
| T-2 | FWD-1,2,3,6 | `comp-read` → `.tools/comp-read` (Python) | measured | 2,401 runs (rail); **unit 1 @`f34122edfb` ON origin (0→2 `comp_log_auto`), CLEARED; `_shape()` shebang routing @`8ed23144cb` ON origin** (extensionless comp-* now parse via python-ast: 10→22 sections on comp-adversary); `--enumerate` writes NO rail row (92625 s.5a); battery 8/8 | CloudComp | audit+fix | — | 4.1-4.6 | enumerate-path logging gap is a finding, not a fix in this row; Rule P reference |
| T-3 | FWD-1,3 | `comp-which` → `.tools/comp-which` | measured | 520 runs.jsonl + 9,643 rail; paginates; 20/60s | CloudComp | audit | — | 4.1-4.6 | the router — its NOFIT-POSTERIOR path is a 4.3 case |
| T-4 | FWD-1 | `comp-hud` | absent | **no such entrypoint**; the HUD is `.tools/hooks/comp-tool-hud.sh` (a hook) | CVO | record | — | 4.1 | DOES-NOT-EXIST; rail hook is CloudComp's by ruling and OUT of this project |
| T-5 | FWD-1,2 | `comp-schedule` → `.tools/comp-schedule` (Python) | measured | 0 runs.jsonl/30d; five carriers; NOT-DECIDABLE is a designed result | CloudComp | audit | — | 4.1-4.6 | **no remediation on this run's evidence** (CVO~A s.11); ARNs absent BY DESIGN — record, do not "fix" |
| T-6 | FWD-1,2,3 | `comp-blast` → `org/modules/graph/cli.py blast` | measured | 167 runs; no explicit timeout | CloudComp | audit+fix | T-19 | 4.3 esp. | **NOT-FOUND ≠ zero radius** (CVO~A s.5): subject-existence check + graph vintage + node denominator |
| T-7 | FWD-1,2,3 | `comp-dataflow` → `comp_dataflow.py` | measured | 11 runs; `origin`/`gate` modes; no timeout | CloudComp | audit+fix | — | 4.3 | preserve 4/4 honest-unresolved; enrich unresolved print (CVO~A s.6); never guess through deploy-time config |
| T-8 | FWD-1,2,3 | `comp-iam` → `.tools/comp-iam` (Python, 14 subcommands) | measured | 113 runs; no timeout; "cannot answer deny" is a declared blind spot | CloudComp | audit+fix | — | 4.3 three-state | **effective-deny mode** (CVO~A s.8): explicit deny / no deny over complete carrier set / NOT DECIDABLE. Never "no parsed deny" → allowed |
| T-9 | FWD-1,2,3 | `comp-trigger` → `comp_trigger.py` | measured | 80 runs; EventBridge+Scheduler only; blind to S3 notifications (COO preflight) | CloudComp | audit+fix | — | 4.3 | declare scope in header OR add S3-notification backend via shared event graph — check existing machinery first (CVO~A s.7) |
| T-10 | FWD-1,2,3,4 | `comp-pipescript` → `.tools/comp-pipescript` | measured | 571 runs; 6 timeouts 10-30s; F9 gate GREEN @`4a6f564c6f` ON origin (141 passed, exercised on 5 later commits; 19/19; live arm asserts the PROPERTY not a pinned digest; **SKIPPED is a third verdict**, per CTO's Q5 ruling) — the tool itself untouched | CloudComp | audit+fix | — | 4.1 | shim self-identification (CVO~A s.9); do NOT add ETFS to registry on one preflight |
| T-11 | FWD-1,2 | `comp-denytest` → `.tools/comp-denytest` | measured | 2 runs/30d, 8 ever; zero population when no IAM change is CORRECT | CloudComp | audit | — | 4.1-4.6 | no remediation (CVO~A s.11); disposition on USAGE is his — RETIRE-candidate surfaced, not acted |
| T-12 | FWD-1,3,6,7 | `comp-similar` → `debtscan/comp_similar.py` | measured | 30 runs; D1-D3 fixed @`b8a73cc064` **ON origin** (is-ancestor of `c9ea7b3b63`, read 18:15:44Z); vintage prints, exercised at two seats | CloudComp | audit | — | FWD-6 | **integration condition MET** (CVO~A s.10). Remaining for CLEARED: the s.4 deliverable (identity, 4.3 four-case test, bounds); D1-D3 are the vintage/disclosure half only. ⛔ **DEPLOYED ≠ COMMITTED (CLAUDE.md 22a): `summary_corpus.py` is baked into the globgrph derive IMAGE, which carries PRE-fix bytes** (CloudComp 92718; owner `0.7.0_AE_CloudOps`) — the repo says D1 fixed, the running image says not; carried to G-rows |
| T-13 | FWD-1,5 | `comp-dups` → `debtscan/dup_scan.py` | measured | **0 runs ever**; separate engine by CTO ruling 3 (names+bodies vs summaries) | CTO | record | — | R-5 | RETIRE-candidate on usage; **do not fold** into comp-similar; CTO's disposition |
| T-14 | FWD-1,5 | `comp-drift` → `.tools/comp-drift` | measured | 1 run/30d; orchestrator over seam engines; `--deep` cost-guarded | CloudComp | audit | — | 4.1-4.6 | overlap with comp-similar is by NAME only (drift = propagation; similar = function) — record |
| T-15 | FWD-1 | `comp-legacy` | absent | **no such entrypoint** (0 of 106) | CVO | record | — | 4.1 | DOES-NOT-EXIST |
| T-16 | FWD-1,2,3,6 | `comp-adversary` → `.tools/comp-adversary` (Python, 526) | measured | 0 runs.jsonl/30d; gate-ENFORCED at `to-pipeline-gate.py:45`; **THREE surfaces (CloudComp 92718): TOOL — `:49` COMMIT_RE backtick + zero-pin guard @`a9dc767e34` ON origin (graded by this seat 15:29Z), digest-basis declaration @`8ed23144cb` ON origin; BATTERY — pass 1 @`e66d5e698d` ON origin (collector lives; 135 s import — PARTIAL), pass 2 @`03cf4d17a` **LOCAL** — P0.1 CLEARED at this seat 2026-09-02 19:3xZ by exercise: `--collect-only` → 1 collected in 0.07 s (2 s wall); module level now constants only, both `compose` calls inside functions (`:94`, `:142`); 1 file touched (+116/-85), production untouched; production MUTANT via `COMP_ADVERSARY_TOOL` temp copy → pytest FAIL on a real arm (1 of 7, rc 1) — the battery discriminates the TOOL, not just the runner** | CloudComp | audit+fix | — | CVO~A P0.1 **MET** | P0.1 limbs all met → RC5 may close (~A's call; CTO gate). **Still owed for row CLEARED:** the s.4 deliverable (identity, 4.2 disclosure, 4.3 four-case test, 4.4 bounds) — the repair was the battery, not the audit; **and the unit-1 gap: comp-adversary has 0 `comp_log_auto` calls (92625 s.1 / 92718) — the third tool invisible to the traffic feed, not in any unit yet.** `--json` = native L0a form (ruled 92527), separate row |
| T-17 | FWD-1,3,7 | `comp-estate` → `org/modules/graph/opal_estate_infrastructure.py` | measured | 281 runs; `<name>`/`--list`/`--resource` | CloudComp | audit | T-22 | 4.2 | his word: *"need to lock in C(N) ontology for this to actually be useful"* — C(N) is `NFRA_C3MATERIALIZE` (D11 sibling); depends_on, not owns |
| T-18 | FWD-1,3 | `comp-pulse` → `org/modules/graph/comp_pulse.py` (707) | measured | **8,364 runs, 8,359 = `diff` from the commit hook; 5 by hand**; L2 traffic source = runs.jsonl | CloudComp | audit | T-1,T-2 | 4.2 | it is a HOOK, not a morning read; its traffic was blind to T-1/T-2 until unit 1 — re-measure after |
| T-19 | FWD-5 | `comp-trace` → `org/modules/graph/cli.py trace` | measured | 45 runs; **strict subset of blast** (`cli.py:1478-1530`) | CloudComp | retire | T-6 | R-4 | his conditional ruling, condition met; redirect 45 callers (`0.7.0_AE_CloudOps~F` 18, `~D` 14, CVO 11) to `comp-blast`; **not platinum** |
| T-20 | FWD-1,3 | `comp-heat` → `.tools/comp-heat` (377) | measured | 0 CLI runs; library consumer = comp-similar `load_heat_live()`; named in the estate-report runner's docstring, **invoked by nothing** | CloudComp | audit | — | 4.2 | his interest; "delivered/described better" — the disclosure fields ARE that; wiring into the daily report is `@09355b6d93`'s, not this row's |
| T-21 | FWD-1,3 | `comp-system` → `org/modules/graph/comp_system.py` (1751) | measured | 584 runs; compiles `infra/system/06_current_state.{md,json}`; `--check` 0/2/1; self-test carries the no-fabrication invariant | CloudComp | audit | — | 4.2 | his ask: "understand what this one does" — the deliverable's purpose_1line + 4.2 answer it; it regenerated on unit 1's commit (side effect, not a scope widening) |
| T-22 | FWD-5,7 | `comp-kuzu` + `comp-kuzu-inc` + `comp-kuzu-full` → `infra/aws/globgrph/kuzu_cli.py` (`--mode inc|full`) | measured | 1,591 + 14 + ? runs; three wrappers, one engine, one flag | CloudComp | **retire** | — | R-3 **RULED (a)** | **UNHELD 18:12Z — Andrew: "recs approved except 2."** `--mode inc|full` is the surface (already exists: `kuzu_cli.py:165`, choices auto/full/inc); both name-wrappers retire; NEVER-full moves onto `--mode inc` EXPLICITLY. ⛔ **RE-SCOPED 19:3xZ on CloudComp's census (92718, denominator 145,054 files): ~15 LIVE carriers, not 5** — comp-describe, comp-kuzu, both wrappers, comp-which, `kuzu_cli.py:39/:168`, COMPTOOL_REGISTRATION_FLOW.md, comp-coverage-map.yaml, comp-output-contracts.yaml, comp-tools.yaml, NFRA_COMPREG.json, NFRA_KUZUSPLIT.json, KUZUSPLIT PRD, two dated briefs. **Split by lane, not one commit:** CODE+REGISTRY carriers (CloudComp, one commit) · KUZUSPLIT PRD P1/P3 (CTO, same window) · the two briefs are dated RECORDS and are NOT rewritten. **CODE HALF LANDED @`dffbee781c` (15 files, +87/−145, LOCAL) — CLEARED by exercise at this seat 21:1xZ:** both wrappers deleted; forwarders no longer resolve on this device (positive control `comp-kuzu` resolves); `retired_aliases` declared with successor + dated order (manifest `:63`, `:75`); `comp-manifest-check retired-alias` PASS (9 declared / 99 live); `--mode inc` on a live query took the inc branch, 6 s, 27,122 nodes, `built:` unchanged; comp-which routes "behind" → `--mode inc` and "full reset" → `--mode full`. **Still open: the KUZUSPLIT PRD P1/P3 amendment (CTO) — until it lands, the PRD text names wrappers that do not exist.** Forwarders on OTHER devices are DESIRED until each re-provisions (the provisioner only ADDS; a stale one fails loud) |
| T-23 | FWD-1,3 | `comp-cache` → `.tools/comp-cache` | measured | 35 runs; React Query cache keys across `portal/src`; `map`/`collisions`/`key` | CloudComp | audit | — | 4.1-4.6 | **not comp-platinum** — portal-local grain; record the distinction |
| T-24 | FWD-1,3 | `comp-platinum` → `org/modules/graph/platinum_cli.py` | measured | 7 runs; composite of transform+routes+pipescript; portal-page → gold-script | CloudComp | audit | T-10 | 4.2 | his question *"how is comp-platinum defined? what coverage universe?"* — the deliverable's corpus_or_backend + denominator fields answer it |
| G-1 | FWD-7 | `comp-graph status` freshness surface | measured | reports `kuzu_db 81d` + `stitch_graph 38d`; canonical is `kuzu_nessie_db` built 2026-09-01T16:18Z (globgrph F6, attributed to CRO) | NFRA_GRAPHS lane | fix | — | brief O7 | surfaced by CRO, not chased; **re-homes to the comp-graph owner** — this row records the dependency |
| G-2 | FWD-7 | stale-served path `kuzu_nessie_db.fallback.jsonl` | held | 16 `inc-served-labeled-stale` events, ~34h behind (F5, CRO's measurement) | CloudComp | verify | T-22 | brief O3b | KUZUSPLIT working AS RATIFIED; the cost is unbounded age — bound it or disclose it on the answer |
| G-3 | FWD-7 | `kuzu_nessie_load` key asymmetry (node stripped `:150`, edge raw `:184`) | held | carded QUALIFIED @`5da9e7fffc` by `0.7.0_AE_CloudOps~K` (F4) | CloudComp | verify | T-22 | brief F4 | a port carries or fixes it, never silently |

**MECE check against the DECLARED domain (his text block), run not asserted:** 22 named tools + 3 roll-up questions
(dups/drift/legacy) = **25 names → 24 rows T-1..T-24** (kuzu/-inc/-full collapse to one engine row by postulate ii;
hud and legacy are DOES-NOT-EXIST rows). **0 uncovered names.** G-1..G-3 are the globgrph workstream, RELIES-ON
by grain (verify/fix rows, not tool audits). Reverse direction: every T row maps to a name in his block; no T row is
work on a surface he did not name.

**What this manifest does NOT assert:** any `evidence` cell marked "runs" is a TOOL-INVOCATION count and is sound
under R-7; none is a seat-coverage claim. Cells attributed to CRO (G-1..G-3) are carried, not re-measured.

---

## 8. Sequencing input for `2.0.0_SA_COO` (not a dispatch)

CVO~A's suggested order, attributed and adopted as the default: **(1)** T-16 collector repair · **(2)** the s.4
schema census + first three deliverables on T-1/T-2/T-3 (highest traffic, rail-critical) · **(3)** T-8 deny mode ·
**(4)** T-6 subject-existence · **(5)** T-9 trigger scope · **(6)** T-7 unresolved diagnostics · **(7)** shim
self-identification across all rows. T-19 (retire trace) and T-13 (CTO dispose dups) can run any time. T-22 waits on
R-3. G-1..G-3 run as a parallel stream once T-22 is unheld.

— 3.0.0_SA_CVO
