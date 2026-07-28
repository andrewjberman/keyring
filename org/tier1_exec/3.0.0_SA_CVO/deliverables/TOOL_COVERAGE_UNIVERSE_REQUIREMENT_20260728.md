# THE COVERAGE-UNIVERSE REQUIREMENT — eliminating type-2 errors on silent recall

    author:      3.0.0_SA_CVO
    status:      FOUNDATIONAL SPEC (assessment + proposed requirement). Not a ratified standard.
    authority:   Andrew-direct 2026-07-28 ~1531Z, CVO terminal, VERBATIM:
                 *"I want the coverage universe for every tool explicitly enumerated so we do not end
                 up with type 2 errors on silent/missing recall. That is a foundational requirement,
                 from there we can expand on the more unique generalized concepts of how to expand the
                 respective tools coverage denominators, i.e. what drives that denominator update."*
                 Placement instinct, same message: *"may actually be better suited for COMPRAIL"* — §6 agrees, with the mechanism.
    companion:   `OPAL_ARCHETYPE_RUNTIME_PROVENANCE_BRIEF_20260728.md` @d4fee91bc (the axis this enforces)
    measured:    2026-07-28T153xZ. Two tools carried through end-to-end as worked instances.

---

## §1 The failure this exists to prevent

**A type-2 error here is not "the tool was wrong." It is "the tool was RIGHT about a set that did not
contain the answer."**

    comp-clobber --live  <served key>   ->  ACTIVE_CLOBBER=False     (key was clobbered 3x)
    comp-clobber (static)               ->  0 mentions of "mdpf"     (110 sinks scanned, correctly)

Neither output is a bug. Both are correct **within the set each mode can see**. The key was clobbered
by a producer whose code lives in `s3://opal-data-mdpf/code/` — **outside the universe**, because the
static scanner walks the repo and Rule 12 requires that EC2 code not be in the repo.

>> **THE DEFINING PROPERTY: a tool asked about something outside its universe does not error. It
>> returns CLEAN. A false negative is therefore INDISTINGUISHABLE from a true negative at the call
>> site — and it is the reading that ENDS inspection.** <<

That is why this is foundational rather than a hygiene item: every other quality control we have
(positive controls, mutation tests, adversarial verify) operates **inside** the universe. None of them
can detect that the universe itself was the wrong shape.

## §2 The requirement

**Every comp-tool MUST declare its coverage universe, and MUST print it with every result.**

A declaration has four fields. Three are commonly written; **the fourth is the one that prevents the
type-2 error and is currently written nowhere.**

| field | question | worked example (comp-heat) |
|---|---|---|
| **SOURCE** | what enumerates the population? | `git ls-files` + untracked mtime |
| **DENOMINATOR** | how many, at run time, not from a doc | 24,605 tracked (+164 untracked = 24,769) |
| **FILTERS** | what is dropped after enumeration? | none applied by default |
| **⚠ STRUCTURAL EXCLUSIONS** | **what can this SOURCE never see, by construction?** | **4 classes — §3** |

**A result without its universe is an assertion, not a measurement.** The estate already enforces the
analogous rule on retrieval (*"print the denominator of every scan you reason from"*, Rule 22). This
extends it from the count to **the shape of the set the count is over**.

## §3 Worked instance 1 — `comp-heat`, universe enumerated (Andrew's explicit ask)

**RUN, fresh, 2026-07-28T153xZ:** `files=24769  half_life=30.0d  hot=1389 warm=4653 cold=18727
(cold_frac=0.76)`. Engine: `org/modules/heatmap/object_freshness.py:46` (`git ls-files`) + `:58`
(untracked mtime). **Source-confirmed, not inferred.**

**IN — and the headline number is 21% not-ours:**

    tracked                  24,605
      of which VENDORED       5,215   (21.2%)   -- 5,185 under infra/ (Lambda layer deps:
                                                    pygments, pyarrow, openai, ...)
      OPAL-AUTHORED           19,390             <-- the set anyone actually means

**OUT — structurally invisible, by construction:**

    1. GITIGNORED            .gitignore:68 `*.log` -> ALL audit logs, incl. the two that are the
                             estate's sole tamper-evidence oracle (my CVO-F1, RV-0056)
    2. SUBMODULE CONTENTS    5 gitlinks -- portal, models/factor_scanner, tools/analytics_dashboard,
                             +2. One line each; contents NEVER walked. THE ENTIRE PORTAL FRONTEND.
    3. S3-RESIDENT CODE      class P2 -- 0 files. Not in git at all.
    4. LIVE/DEPLOYED PLANE   0 -- comp-heat reads git history; it never observes a running artifact.

**Two consequences that would have bitten a real user, and neither announces itself:**
- *"What's cold in the estate?"* — **the whole portal is absent from the answer**, and absent is not
  reported as absent. A frontend surface cannot appear in any heat-based archive or debt decision.
- *"Archive candidates: 1312 cold subtrees"* — includes `infra/aws/lambda/layers/.../pygments/lexers/`
  (260/260 cold). **Vendored third-party code presented as an Opal archive candidate.** Correct within
  the universe; wrong as advice.

**Freshness: CONFIRMED.** Derived on demand from git at call time — no persisted snapshot, so no stale
vintage. That is a genuine strength and it is why the fix here is declaration, not re-plumbing.

## §4 Worked instance 2 — `comp-clobber`, for contrast

    SOURCE        os.walk over roots ["data","infra"], ext {.py,.sh,.tf,.json}   (clobber_scan.py:49,318)
    DENOMINATOR   110 write-sinks, 11 multi-writer
    FILTERS       _WRITE_VERB regex :52-54; _S3_KEY literal-prefix regex :58; sovereign_held (now 0)
    EXCLUSIONS    (a) S3-resident producers -- the code is not in the repo
                  (b) variable-interpolated destinations -- `s3://${VAR}/...` cannot match :62
                  (c) --live mode: only ETag-REPETITION clobbers (:101-109)

**Same disease, different organ.** Both tools are correct instruments pointed at a set that excludes
the P2 provenance class. **That co-extensiveness is the point: the exclusions are not random per-tool
quirks — they cluster on the same missing dimension**, which is why enumerating them per tool exposes
a systemic gap rather than a list of bugs.

## §5 What DRIVES a denominator update (Andrew's second question)

A universe is not static. **Four events invalidate one, and each is detectable:**

| driver | example | detector |
|---|---|---|
| **D1 NEW PROVENANCE CLASS** | EC2 code moved to S3 (Rule 12) | a new class in the provenance axis ⇒ **every repo-scanning tool's universe is now wrong** |
| **D2 NEW PLANE / STORE** | a bucket, table, or account added | estate census delta (39 buckets today) |
| **D3 GRAMMAR CHANGE** | S3 key grammar or naming law amended | TOOLARCH §3 CHURN axis; the extractor must cite its law so it fails loudly |
| **D4 EXCLUSION DRIFT** | `.gitignore` gains a pattern; a submodule is added | diff of the exclusion set itself |

**D1 is the dangerous one and it is the one we just lived through.** It does not change any tool's
code, output, or self-test — **it changes what the tool's silence MEANS**, retroactively, across every
tool at once. Nothing in the current suite watches for it.

**Therefore the proposed mechanism is comparative, not absolute:** a tool's declared universe is
checked against the **estate census** (provenance classes × planes × stores), and the delta is the
tool's blind spot, computed rather than remembered. *"comp-heat covers 0 of 4 provenance classes
beyond P1"* is a machine-derivable sentence. **This also makes the requirement testable: a universe
declaration that cannot be diffed against a census is not a declaration.**

## §6 Where this belongs — agreeing with Andrew's instinct, with the mechanism

He suggested **COMPRAIL** over TOOLUNIFY/TOOLARCH. **Concur, and the reason is structural rather than
organisational:**

- **TOOLARCH** answers *"what patterns exist"* — its §3 stability grader already grades a pattern's
  POPULATION and VIOLATION. **The universe requirement supplies the denominator those axes need.** It
  feeds TOOLARCH; it does not live there.
- **TOOLSEM** is *"resolve a query to its required (rail, grain, plane, scope) denominator"* — the
  closest fit conceptually, **but it has 4 commits and ZERO code files. Nothing is built.** Putting a
  foundational requirement behind an unstarted project is how it becomes a note.
- **COMPRAIL is the RAIL — it is what ROUTES a question to a tool, and it is LIVE and ENFORCING
  today** (Gate-1 armed, ~3 weeks of live DENY log). **The routing layer is the only place that sees
  the QUESTION and the TOOL together**, which is exactly where a universe mismatch is detectable:

      comp-which "what writes this S3 key?"
        -> routes to comp-clobber
        -> comp-clobber's universe EXCLUDES S3-resident producers
        -> the rail can say so BEFORE the tool returns a clean answer

  **That is the type-2 error caught at routing time rather than discovered three hours into an
  incident.** No other layer holds both halves.

**Recommended shape (not a ruling — CTO + 0.7.0_AE_CloudOps~Z own it):** universe declaration as a
required field in the tool registry that `comp-manifest-check` already gates on registration, with the
rail reading it at route time. That reuses a LIVE gate instead of inventing enforcement.

## §7 Scope and limits, stated

- **Two tools carried end-to-end; the suite is ~92.** This is the requirement plus two worked
  instances, **not** a completed census. The remaining tools' universes are unenumerated and I am not
  implying otherwise.
- **§6 is a recommendation.** Ratification is CTO's and `0.7.0_AE_CloudOps~Z`'s; per my prompt §8 I
  qualify and recommend, I do not set the standard.
- **Trino/Nessie deferred by Andrew** (~1531Z, *"Trino we will deal with later"*). The `_trino_fed`
  module has **no CLI surface** pending a CTO tool-home ruling, and queries cost ~3-4 min via an in-VPC
  Fargate one-shot. Not blocking this spec.
- **git co-change not yet run** — still the open item from the companion brief's §6. It is cheap and
  next.

— 3.0.0_SA_CVO
