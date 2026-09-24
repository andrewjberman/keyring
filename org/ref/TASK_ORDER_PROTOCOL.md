# Task Order Protocol

Full XML template, filename convention, instance rules. Referenced from XXX.md.

---

## Location

Task orders go in the **receiving agent's** `task_orders/` folder:
```
{receiving_agent_folder}/task_orders/{MACRO}_{6CHAR}.{task-code}.{description}.md
```
One file per feature. Never overwrite into a monolith.

**Tree projects (spine v3.0).** A project with a tree home issues its task orders at
`org/missions/D<n>/<MACRO>/<CODE>/task-orders/<CODE>.TO-<id>.<slug>.md`, every cell of the decomposition in ONE
issuance commit whose message carries `fanout: N of M chains, cap K, reason: <one line>`; the flat folder above is
the legacy home. A task order has TWO FACES in one file: the WORKER FACE (cell text inlined, surfaces, bounds,
`<paths>` absolute from the root, one clause per criterion) is the worker subagent's prompt and the whole of its
context; the RECORD FACE (`<status>`, seating, preflight narrative, authority chain, provenance) stays in the file
for the gates and never travels to the worker. `<issued_to>` names the worker serial `0.9.0_WK_<CODE>~<n>`. Where
this template and the spine differ, the spine governs.

**Spine v3.19 (reports 2 and 3, Andrew-approved 2026-09-24).**
- **`<risk>`** is required on a new tree order: `LOCAL` (code, tests or records, including a portal change landing
  on DEV only), `SERVED` (a PROD promotion or a served data path) or `WORLD` (a deploy, delete, grant, key, or a
  claim to Andrew). `.tools/to-pipeline-gate.py` GATE (xii) refuses it absent, off the enum, or below the floor its
  `<paths>` and invocations imply (an `infra/` path or a deploy verb is `WORLD`). The class decides which limbs
  engage.
- **`<worker_class>`** names the agent type the spawn uses: `worker`, or `worker-light` (a cell of about 100 product
  lines or fewer, or the batch repair cell).
- **The face never restates the worker rules.** Identity, commit, the bar, surprise, proof, scratch and never live in
  `.claude/agents/worker.md`; the face carries only what is specific to its cells.
- **Every mechanical check is a small test or script file, dry-run at the base before the cut.** A build check
  fails there and a bound or control check passes there; the issuance commit carries one line per check.
- **The direct-act path:** one cell, about 300 product lines or fewer, `<risk>LOCAL</risk>` -> one order carrying
  `<direct_act>true</direct_act>`, no L2, L4-R or L8-L10; its close is the COO's one real run of the outcome.

---

## XML Template

```xml
<task_order>
  <metadata>
    <id>{issuing_serial}-{YYYY-MM-DD}-{short_slug}</id>
    <issued_by>{issuing_serial}</issued_by>
    <issued_to>{receiving_serial}</issued_to>
    <date>{YYYY-MM-DD}</date>
    <status>staged | pending | complete</status>
    <project_code>{MACRO}_{6CHAR}</project_code>
  </metadata>
<risk>LOCAL | SERVED | WORLD</risk>
<worker_class>worker | worker-light</worker_class>

  <objective>
    <!-- 1-3 sentences: what needs to be accomplished and why -->
  </objective>

  <context>
    <!-- Background, PRD references, architecture decisions the agent needs -->
  </context>

  <compiler_tools_mandate>
    <!--
    MANDATORY. THREE-PHASE structure (all TOs, no exceptions).
    For each <run>, fill in the specific command and an <expect> block.
    <expect> encodes what "normal" looks like — agents verify output against it.
    <if_mismatch> tells the agent what to DO if output is unexpected (not just that something is wrong).

    SPECIAL CASE — TO adds a new value to a TypeScript union type (new cohort, metric, mode, role):
    Phase 1 MUST include both before writing any code:
      <run>comp-transform schema-check {Component} --feature {token}</run>
      <expect>0 feature-relevant WARN entries -- all {token}-prefixed fields in RENDERED set, not UNUSED</expect>
      <if_mismatch>UNUSED field with {token} in name = routing ternary missing the branch. Run ternary-audit to get the complete fix list.</if_mismatch>

      <run>comp-transform ternary-audit {Component}</run>
      <expect>0 gaps, or note which gaps are intentional with reason</expect>
      <if_mismatch>Each gap = routing ternary where {token} silently falls to wrong else. Fix all gaps before Phase 2.</if_mismatch>

    Why: W3 OFC (2026-04-14) — nna_ofc typed but never rendered because L1956 routing ternary
    had no ofc branch. ternary-audit at Phase 1 generates the complete fix list automatically.

    SPECIAL CASE — TO is an ATOMIC-BUNDLE ship (a multi-commit refactor touching a producer
    + one or more of its consumers — a helper signature change, a shared-shape change, a
    co-landed producer+consumer rename):
    Phase 1 MUST capture the pre-bundle snapshot BEFORE the bundle ships:
      <run>comp-chainrun snapshot --label pre --out {to_id}-pre.json</run>
      <expect>snapshot writes; present == sentinel count, errors=0</expect>
      <if_mismatch>errors>0 = a stage sentinel is unreadable; resolve before capturing the reference</if_mismatch>
    Phase 3 MUST capture the post-bundle snapshot and diff it:
      <run>comp-chainrun snapshot --label post --out {to_id}-post.json</run>
      <run>comp-chainrun diff {to_id}-pre.json {to_id}-post.json</run>
      <expect>overall=PASS, leaks=0 — no sentinel flipped green→absent, lost a column, or went row-count>0→0</expect>
      <if_mismatch>Each LEAK row is a partial-refactor leak — a consumer the bundle did not update, or a dropped sibling. Fix every leak before marking the TO complete.</if_mismatch>

    Why: DWSPLT chain #26 — a consumer signature mismatch survived an atomic-bundle ship past
    every code-level + shape-sentinel check. PRD: docs/architecture/ADHC_VALGATE.md section 4.B.

    Example (filled):
    Phase 1 — before writing:
      <run>comp-blast DistributionTab</run>
      <expect>8 downstream nodes; all via opal-partners-data Lambda; OFC is additive so count unchanged</expect>
      <if_mismatch>Flag to COO — unexpected blast radius may mean shared S3 artifact with another active TO</if_mismatch>

      <run>comp-pipescript io D_01</run>
      <expect>COLUMN GAPS: 0 gaps. S3-DYNAMIC: dim_advisor_office.csv present. PORTAL CONSUMERS: partner_analytics → DistributionTab</expect>
      <if_mismatch>If COLUMN GAPS shows any gap, fix before proceeding — silent column omissions have caused zero-valued output in prod</if_mismatch>

    Phase 2 — before committing:
      <run>comp-transform schema-check DistributionTab</run>
      <expect>0 MISSING fields; ofc types in rendered set; NOTE fields are expected aliases</expect>

    Phase 3 — after committing:
      <run>comp-blast [changed function]</run>
      <expect>Blast radius identical to Phase 1 — no new downstream nodes</expect>
      <if_mismatch>Flag to COO — new downstream consumers appeared unexpectedly</if_mismatch>

    WHEN <expect> is required: whenever the tool output gates a decision (blast radius before cross-domain TO,
    column gaps before modifying load logic, validate before signaling AE). If the run is purely orientation,
    a short note is acceptable.

    Results must appear in session log Compiler Tools table.
    A TO with no compiler check logged is NOT accepted as complete.
    See: org/standards/TO_COMPILER_GATE.md
    -->
  </compiler_tools_mandate>

  <cross_domain_coordination>
    <!-- Fill this section ONLY when this TO touches a file, S3 key, or data contract
    that is also touched by another active TO in the same wave.
    COO/CTO must identify cross-domain resources during PRD decomposition using comp-blast.

    If applicable:
    - shared_resource: {file or S3 key}
    - also_in_to: {other TO IDs}
    - last_write_owner: {serial that commits last}
    - required_action: "Message {serial} via MCP before committing to {file}. Pull latest before writing."

    If not applicable: <none/>
    -->
  </cross_domain_coordination>

  <acceptance_criteria>
    <!-- MANDATORY. Specific, machine-checkable. Not "code runs" or "build clean."

    ================================================================================
    APPLY THESE TWO TESTS TO EVERY CRITERION BEFORE YOU ISSUE THE TO.
    Binding per docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md @d3681d1d0 (CTO, 2026-07-24).
    ================================================================================

    (A) THE EASIEST-PASS TEST (corollary 3 — a control satisfiable by breaking what it
        guards is not a control):
          "What is the EASIEST way to make this criterion pass?"
        If that route RE-COMMITS THE DEFECT, the criterion is wrong. Rewrite it, and
        NAME THE FORBIDDEN SHORTCUT INSIDE THE CRITERION so the assignee cannot take it
        by accident.
        Worked example (CTO's own, named as his): an absolute aua_pct gate condition
        could be satisfied by re-basing the very quantity it guarded.
        >> PREFER DIFFERENTIAL INVARIANTS TO ABSOLUTE ONES. "sum(rows)/denominator
           IDENTICAL pre/post (90.03% -> 90.03%)" fails if anything re-bases, and does
           not require asserting a number that was never true.

    (B) THE MISSING-THIRD-STATE TEST (corollary 1):
        If the criterion models a TWO-STATE outcome, ask WHERE "WE DO NOT KNOW" GOES.
          UNKNOWN != COMPLETE · HELD != CERTIFIED · UNREADABLE != UNCLOSED ·
          INFERRED-PRESENT != MEASURED · UNEXERCISED != PASSED
        The fix is ADDING THE STATE, never widening the predicate. On 2026-07-24 that
        single question was the fix in four separate places.

    AND ESCALATE THE ASSERTION LEVEL (2026-07-24, one observable revised three times in
    one hour, each level invisible from the one above):
          EXISTENCE ("a version appeared")        -> passes on the WORST outcome
          CONTENT   ("the block survived")        -> passes on a wrong-axis value
          CORRECTNESS ("the value == 294 exactly") -> the first one that can FAIL
    A criterion that cannot fail is not a criterion. Pin the expected VALUE, not the shape.

    ================================================================================
    THE VERIFICATION DIET -- canonical tree orders (spine v3.16, L6). A TO IS MOSTLY THE BUILD.
    ================================================================================
      AT MOST THREE mechanical criteria on a build order:
        (a) the built behaviour;
        (b) the hop's seam probe against its REAL neighbour where reachable (a fixture only
            where it is not);
        (c) at most one further criterion the cell genuinely needs.
      A fourth carries a one-line reason on the face. A difference-control arm is part of
      the criterion it controls, never counted as a separate check (spine v3.17).
      REPO-WIDE HYGIENE IS NOT A CRITERION: typecheck, lint, the full suite, py_compile, and
      the "bun run build" / "bunx tsc -b" line below run ONCE PER MERGE at the COO's drain,
      and the live thread trace once per round there. On a canonical tree order, the portal
      and gold STANDARD CRITERIA below are drain checks, not lines on the face.
      JUDGMENT criteria only where the outcome needs judgment (a user-facing reading, a
      design-conformance grade) -- never a default slot.
      KEPT UNCHANGED: the refusal clause, the difference control on a criterion that
      asserts a control, and the proof-of-spec instance.
      No gate counts criteria; this is how the issuer cuts.

    STANDARD CRITERIA (include for every gold-touching DS TO):
    N.   comp-validate {script} --artifact /tmp/{artifact}.json exits 0
         (all ERROR checks pass; WARN count documented in session log)
    N+1. comp-pipescript deployed {script} shows MATCH after S3 upload

    STANDARD CRITERIA (include for every portal-touching DE TO):
    N.   comp-transform schema-check {Component}: 0 MISSING fields
    N+1. bun run build (or bunx tsc -b): zero TypeScript errors

    Role-specific examples:
    - DS: fee_earning_aua > 0 for at least one advisor with aua > $1M (Travis Penfield spot-check)
    - DS: geo_drill present in timeseries_chart.json with >= 5 state keys
    - DS: comp-validate {script} --artifact /tmp/{artifact}.json exits 0
    - DE: comp-transform fields shows all rendered fields present in TypeScript type
    - DE: state legend items are <button> elements (clickable), not <div> (static)
    - AE: comp-pipescript deployed {script} shows MATCH before triggering gold run
    - AE: comp-iam gaps shows no new permission gaps after iam.tf change

    Agent confirms each criterion explicitly in session log before marking complete.
    -->
  </acceptance_criteria>

  <proof_of_spec>
    <!--
    MANDATORY -- ANDREW-DIRECT 2026-08-11 ~0821Z at the CVO terminal, VERBATIM: "I do not want
    TOs being issued that do not have machine-readable data contracts, where the agent
    responsible must fill out the contract based on their efforts."
    (Record: org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260811_PROOF_OF_SPEC_CANONIZED.md)

    TWO HALVES, one per party:

    ISSUANCE (the issuer, at PRD decomposition): the machine-readable criterion-id set --
    every <acceptance_criteria> criterion gets a stable id, listed here. A TO WITHOUT THIS
    SET IS NON-CONFORMING AND IS NOT ISSUED.
      <expected_criteria>C1,C2,C3,...</expected_criteria>

    COMPLETION (the assignee, from THEIR OWN efforts): a PROOF_OF_SPEC instance --
    org/standards/PROOF_OF_SPEC.schema.json -- one row per criterion id carrying the
    criterion VERBATIM + the exact re-runnable invocation + output evidence + denominator,
    validated BEFORE the status flip:
      python .tools/proof-of-spec-check.py {instance}.json C1,C2,C3
    THE ID SET IS POSITIONAL (`sys.argv[2]`) -- comma-separated ids OR a path to a file with one
    id per line. There is NO argparse and NO `--expected-criteria` flag: the flagged form makes
    argv length 4, trips the `len(sys.argv) not in (2,3)` usage guard, and EXITS rc=2.
    ⛔ **CORRECTED 2026-08-11 -- this line prescribed `--expected-criteria` and every TO minted
    from it inherited a broken invocation.** Caught by 0.7.0_AE_CloudOps on first use and
    exercised both ways before the fix (flagged -> rc=2 usage; positional -> rc=0 VALID).
    CORRECTED 2026-08-11 ~1710Z (1.0.0_SA_CTO~Z, on 0.5.0_AE_OpalETL~Z's first live use of
    this contract). This line previously documented `--expected-criteria C1,C2,C3`, which the
    tool does not accept -- `proof-of-spec-check.py:65` takes `len(sys.argv) in (2,3)` with
    the criteria string at `sys.argv[2]`.
    **The harm is NOT the loud rc=2 -- it is the FALLBACK it invites:** an assignee who hits the
    usage error drops the id argument, re-runs the 2-arg form, and gets a clean `rc=0 VALID`
    that says **COVERAGE UNCHECKED**. So a wrong flag in the template steers people off the ONE
    layer that catches a silently-omitted criterion, and it does so while printing success.
    ⛔ CHECK THE RC, NEVER THE OUTPUT STRING -- THE USAGE BANNER CONTAINS THE VOCABULARY OF
    BOTH VERDICTS. The flag form is a usage error: rc=2, 19 lines of help, and line 13 reads
    "Exit 0 = VALID. Exit 1 = INVALID (every violation printed). Exit 2 = usage/read error."
    So a string-matching caller reads back whichever word it went looking for:
      - checks rc          -> SAFE. rc=2 is loud and correct.
      - greps "INVALID"    -> effectively safe; it MATCHES the legend and refuses. Noisy, not wrong.
      - greps a SUCCESS string ("VALID") -> ⛔ SILENT PASS. It matches "Exit 0 = VALID" in the
        banner of a call that validated NOTHING.
    Exercised: flag form rc=2 (rc taken WITHOUT a pipe) + 19 help lines; positional form `VALID`,
    rc=0, 6 rows, 0 violations.
    *(MECHANISM CORRECTED 2026-08-11 ~1727Z. This block first said the help text "contains no
    INVALID string" -- FALSE, and it is the reversed reading of the same hazard. Caught and
    ground-measured by 2.0.0_SA_COO~Z, who took the rc without a pipe after catching their own
    first attempt reading `head`'s rc=0. The CONCLUSION -- use the positional form -- was right
    both times; the MECHANISM was backwards, and Rule 22 exists because a wrong mechanism is
    copied forward into the next rule where it becomes load-bearing. The general form worth
    carrying past this tool: WHEN A FAILURE PRINTS THE VOCABULARY OF SUCCESS, ONLY THE EXIT CODE
    DISCRIMINATES.)*
    The validator runs the COVERAGE diff first (a criterion with no row refuses the instance
    before any quality check; frames printed) then the quality rules (FAIL-requires-reason,
    thin-evidence-PASS invalid, dead mutant/determinism controls invalidate). The diff is
    BIDIRECTIONAL: expected-without-row AND row-without-expected both violate.
      <instance_path>{assignee_folder}/deliverables/{to_id}_PROOF_OF_SPEC.json</instance_path>
    ⚠ **ONE instance_path IS THE SINGLE-DELIVERABLE CASE ONLY. A MULTI-GROUP / MULTI-PIECE TO
    DELIVERS ONE INSTANCE PER GROUP AND MUST DECLARE A GRAMMAR, NOT A PATH:**
      <instance_path_grammar>{assignee_folder}/deliverables/PROOF_OF_SPEC_{phase}_{firm}_{group}_{YYYYMMDD}.json</instance_path_grammar>
      <group id="..." status="NOT_YET_MINTED|MINTED|DELIVERED|HOLD_FOR_RULING" instance_path="..."/>
    plus firm-tokened criterion ids `{firm}-{group}-{artifact}-{check}` declared BEFORE the first
    mint (untokened ids collide across parallel firm lanes, and the cert step-zero reads ACROSS
    instances). Adopted fabric-wide, CTO 2026-08-11 092331Z.
    ⛔ **WHY THIS WARNING EXISTS: MDPF_49F_BUILD.P1 declared a single `instance_path` here and
    three per-group instances landed under different names -- the declared path matched NONE of
    them, so a completion flip acting on it would have read absence as work-not-done.** The
    issuer believed that was their own defect; it was inherited from THIS TEMPLATE.
    >> **BOTH corrections on this page came from one TO, in one hour, from one template. A
    template defect is not one defect -- it is one per TO ever minted from it, and fixing the
    copies while the source keeps minting is the single-homing failure: declare it ONCE, at the
    convergence point.** <<
    NOTE the issuance lint (`.tools/git-hooks/to-proof-of-spec-check.sh:29`) greps for the
    PRESENCE of a `<proof_of_spec` element on NEW task-order files. It binds issuance PRESENCE,
    never issuance CORRECTNESS -- it cannot resolve an `instance_path`, cannot check an id set,
    and does not re-run on MODIFIED files. **Neither defect above was caught by any gate.**

    THE TWO-LAYER DIVISION (on the record 2026-08-11 082045Z): the validator catches the
    ASSIGNEE omitting against the TO's id list; CVO's cert-of-built step-zero catches the TO's
    id list omitting against the governing SPEC. The instance is the assignee's self-report
    made maximally checkable -- it never substitutes for independent re-derivation; it makes
    the re-derivation mechanical and its refusals precise.
    -->
    <expected_criteria><!-- comma-separated ids, minted by the ISSUER --></expected_criteria>
    <!-- spine v3.0, ONE CLAUSE PER CRITERION (CRO spec s.13 L-2): each id above is declared once below, mechanical
         or judgment, never compound. A MECHANICAL criterion carries the exact invocation and the EXPECTATION the
         observed output must match, so its pass is decided by the match and not by the worker. A JUDGMENT criterion
         carries judgment="true", is NOT self-graded, and is graded only by 3.0.0_SA_CVO at L9 against the spec. A
         criterion that conjoins clauses is refused at the cut. The instance schema (PROOF_OF_SPEC.schema.json) and
         proof-of-spec-check.py learn `expect` and `judgment` as BUILD ACTS (spine s.4); until they land, the worker
         records the output as today and the CVO's L9 read of the instance against the spec is the only grade. -->
    <criterion id="C1" cell_refs="CE-x-1" judgment="false">
      <invocation><!-- the exact re-runnable command --></invocation>
      <expect><!-- the pattern the deciding output must match --></expect>
    </criterion>
    <criterion id="C2" cell_refs="CE-x-1" judgment="true"><!-- CVO-graded at L9; the worker records output, no verdict --></criterion>
    <instance_path><!-- where the assignee's filled instance lands --></instance_path>
  </proof_of_spec>

  <scope>
    <files>
      <file action="create | modify | reference">path/to/file</file>
    </files>
  </scope>

  <requirements>
    <requirement id="1"><!-- specific, testable --></requirement>
  </requirements>

  <deliverables>
    <deliverable type="commit | document | spec"><!-- description --></deliverable>
    <deliverable type="document">Session log with Compiler Tools section</deliverable>
  </deliverables>

  <do_not>
    <rule><!-- specific anti-pattern to avoid --></rule>
  </do_not>
</task_order>
```

---

## Status Values

| Status | Meaning | Who sets it |
|--------|---------|-------------|
| `staged` | Assigned but no GO received — do NOT start | COO |
| `pending` | GO received — active or queued | Agent (on receiving GO) |
| `complete` | Work done, deliverables confirmed | Agent (self-marks) |
| `superseded` | **The NEED WAS MET ANOTHER WAY** — done elsewhere, replaced by a newer TO, or the artifact now exists by another route. **MUST name what superseded it** (commit-ish / TO id). | COO or the ISSUER — never the assignee alone |
| `cancelled` | **The NEED WENT AWAY** — a later ruling killed the work. **MUST cite the ruling** (verbatim + date, or commit-ish). | COO or the ISSUER — never the assignee alone |

`staged` → `pending` happens when the agent receives a GO message from COO, or -- for a worker subagent under spine v3.0 -- when the COO's spawn hands it the task order's worker face: the spawn IS the GO and no broker message carries it. Flip it immediately and begin. The GO IS the authorization -- do not ask Andrew.

**`superseded` and `cancelled` added 2026-08-07, ANDREW-DIRECT, VERBATIM: *"yeah you need to be able to 'supersede' or 'cancel' outstanding task orders in status to clean that up when these situations arise."*** ⚠ **THE MECHANISM ALREADY EXISTED AND ONLY THE LAW WAS MISSING** — `.tools/to-check.py:47` has accepted `superseded`/`cancelled`/`dropped`/`decommissioned`/`archived` as DONE-class the whole time, and the parseable-status paragraph below lists them. **This TABLE is what an agent reads to learn what is legal, and it carried three values.** So a TO whose work a ruling had killed had nowhere honest to go: `complete` is a lie, and `pending` is the rot. *A record NARROWER than its mechanism leaves agents unable to reach a capability that exists — the mirror of the CLAUDE.md 14a `--force` correction, where the record was BROADER than its mechanism.*

**KEEP THE TWO DISTINCT — they differ on RE-OPEN, which is the only time it matters.** `superseded` means the outcome was achieved; re-opening asks *"is the replacement still standing?"* `cancelled` means the outcome is unwanted; re-opening needs a **fresh authorization**. Collapsing them loses which question to ask.

⛔ **A TERMINAL STATUS WITHOUT ITS POINTER IS THE ROT WITH A TIDIER LABEL.** The pointer is what makes "we knew about that" checkable. **Why the assignee does not set these alone:** an assignee who can self-cancel can bury inconvenient work under a status the board reads as closed — the authority is whoever can CITE the killing ruling, not whoever holds the task.

**MEASURED INSTANCES THAT EARNED THIS (2026-08-07):** `0.5.0_AE_OpalETL` held 9 TOs of which **3 ordered work Andrew deprecated 8 days earlier** (DC1/DC2 crawls, ETFS W2 step 1) — invisible because the seat was dark and nothing was executing them to trip over the contradiction. And `MDPF_REMEDIATION_REGISTER` R-13 read *"not yet moved"* for work executed at `@46d3bf3f32`. **A ruling that kills the work does not retract the instruction; they live on different surfaces and only a deliberate sweep joins them.**

**Parseable-status convention (MSTR-adopted 2026-06-29, encouraged not gated).** The board tools (to-check, registry-check) classify a TO/project by the FIRST TOKEN of its status. Lead with a clean state word — `<status>complete — <detail>...</status>`, not `<status>active — ... DONE+ACCEPTED</status>` (first-word `active` reads OPEN even though done). DONE-class first-words: complete|completed|closed|cancelled|superseded|done|merged|shipped|decommissioned|archived|dropped. Both an XML `<status>` tag and a markdown `**Status:**` line are read (markdown now backtick-robust); a TO with NEITHER renders [??]. The parsers deliberately do NOT scan for a DONE token mid-string (would false-close an active phase status like build-complete), so a stale open first-word will NOT auto-flip — keep the first word truthful.

---

## Filename Convention

**Project work:**
```
{MACRO}_{6CHAR}.{task-code}.{description-words}.md
```
- Dots separate segments. Dashes separate words within a segment.
- Project codes: `org/projects/REGISTRY.md` | Macro codes: `org/projects/MACRO_CODES.md`

```
ADVI_49PUSH.012.de-wire-books-tab.md
ADVI_V1VERS.004.adv-drill-cla.md
ADHC_DESIGN.027.de-tooltip-migration-pod-0.2.md
```

**Ad-hoc (no registered project):**
```
{description-with-dashes}.md
```

---

## Parallel Instances (~B, ~C)

When Andrew runs multiple workers for the same role:
- `register_agent("0.4.0_DS_ClientPlatform~B")` — instance B
- All instances share the same org folder, logs, task_orders
- Commits: use BASE serial as `--author` (no `~` suffix in git)
- Log filenames: include suffix — `nna_fix~B.md`
- Task orders: append suffix when issuing to a specific instance — `ADVI.012.de-books~B.md`
- MCP: sending to base serial delivers to ALL live instances; `~B` delivers to only that instance

---

## Completion Protocol

- Receiving agent edits `<status>` from `pending` to `complete` when done
- This is the done signal — no separate notification required
- **PROOF-OF-SPEC GATE (Andrew-direct 2026-08-11, canonized): the status flip to `complete` is
  legal ONLY with a VALID proof-of-spec instance at the TO's `<instance_path>` — filled by the
  assignee from their own efforts, validated by `.tools/proof-of-spec-check.py` against the TO's
  `<expected_criteria>` set. A completion without it is the sibling of the compiler-gate rule:
  NOT accepted as complete.** Issuers: a TO missing `<proof_of_spec>` is non-conforming — do not
  issue it; assignees receiving one: request the criterion-id set from the issuer before starting
  (the contract is the issuer's to mint, the instance is yours to fill).
- Tier 1/2 agents verify completion against logs and commits, not just the status field
