# INPUT — CVO~A battlefield enhancements from the ETFS_GUARDRAIL preflight

**Author:** `3.0.0_SA_CVO~A` · **Ferried by:** Andrew, CVO base terminal, 2026-09-02 ~17:2xZ, VERBATIM
("I also want to ferry you a briefing from CVO~A based on battlefield enhancements we encountered on the
ETFS project which may be useful context in terms of refining the key tooling for the canonical workflow")
**Filed by:** `3.0.0_SA_CVO` as an INPUT to `NFRA_COMPEFFICACY`. Not this seat's authorship; not altered.

---

CVO Base — battlefield enhancements from the ETFS_GUARDRAIL preflight

OBJECTIVE

Improve tool truthfulness and diagnostic value without forcing every comp-tool to cover every ETFS
surface. A tool that clearly reports its boundary is working; a tool that turns "subject absent,"
"zero result," and "not decidable" into the same answer is dangerous.

P0 — UNBLOCK THE EXISTING ADMISSION HOLD

1. comp-adversary pytest compatibility

Keep this repair surgical: remove module-scope sys.exit() behavior and make the battery import-safe.

Acceptance:
- pytest --collect-only exits 0 and collects >0 tests.
- pytest execution exits 0 with a printed test denominator.
- Direct execution and pytest report the same substantive 7/7 result.
- A planted mutant makes pytest fail.
- No comp-adversary production behavior changes.

This closes RC5. Please do not combine it with a battery rewrite.

2. Battery ownership gap

The estate has 59 ownership lanes and zero .tools/tests ownership rules. Surface a placement request
to CTO/COO; do not self-create an ownership lane. A load-bearing battery needs a named owner
obligated to notice when collection reaches zero.

CROSS-TOOL HARDENING

3. Standardize disclosure before expanding coverage

Every tool run should expose, in rejectable fields or stable lines:

- exact subject;
- engine/implementation path, not only shim path;
- corpus or backend examined;
- corpus/build vintage;
- denominator scanned;
- resolved and unresolved counts;
- declared blind spots;
- whether the subject was absent, present-with-zero-results, partially resolved, or not decidable.

Do a Rule-24 census before introducing a shared enum. The required semantic distinction is:

SUBJECT_ABSENT_FROM_CORPUS != PRESENT_WITH_ZERO_EDGES != PARTIAL/BLIND != NOT_APPLICABLE.

4. Add a battery-of-batteries check

For every .tools/tests/test_*.py:
- import/collection must not terminate the runner;
- collected test count must be >0;
- collection and execution results must be reported separately;
- module-scope sys.exit()/unbounded subprocess work should be caught;
- each important green needs a red-first mutant or negative control.

TOOL-SPECIFIC ENHANCEMENTS

5. comp-blast

Do not treat NOT-FOUND as a zero blast radius.

First check whether the subject exists in the graph:
- absent subject -> SUBJECT_ABSENT_FROM_CORPUS / no blast answer;
- present subject with zero dependents -> measured zero blast radius;
- planned new surface -> identify the nearest existing parent/caller surfaces instead of pretending
the new file has graph history.

Always carry graph vintage and node denominator. This is more valuable than merely adding ETFS names
to the corpus.

6. comp-dataflow

The tool behaved correctly: 4/4 dynamic reads were found and honestly marked unresolved. Preserve
that honesty.

Enhance the unresolved result to print:
- source line and expression;
- which symbol/env/config value prevented resolution;
- any candidate bucket or prefix values found;
- the exact next instrument required.

Resolve common static constructions where safe—dict lookup, constant propagation, f-string/path
joins—but never guess through deployment-time configuration. For that boundary, emit "DEPLOYED-
BYTES/BUILD-INPUT COMPARISON REQUIRED."

7. comp-trigger

Determine whether the existing graph or comp-events machinery already indexes S3 bucket
notifications before building another extractor.

The tool should either:
- incorporate EventBridge, Scheduler, and S3-notification backends through one shared event graph;
or
- state in its identity/header that it covers EventBridge + Scheduler only.

Acceptance should include:
- EventBridge trigger found;
- Scheduler trigger found;
- S3 notification trigger found or explicitly out of declared scope;
- absent trigger distinguished from unsupported trigger type;
- denominator per backend.

8. comp-iam

This is the highest-value capability gap after RC5. The tool cannot currently answer effective
denial.

Add an effective-deny mode that separately inventories:
- identity inline and managed policies;
- resource policies;
- permissions boundaries;
- SCPs and session policies where observable;
- parsed versus unparsed DENY statements.

Allowed output must be three-state in substance:
- explicit deny found;
- no deny found over a declared complete carrier set;
- NOT DECIDABLE because one or more deny carriers were unavailable/unparsed.

Never translate "no parsed deny" into "allowed." Add a cross-firm bucket fixture exercising the
existing deny belts.

9. comp-pipescript

Do not add ETFS to its registry solely because it was in this preflight. Zero population was
truthful.

Fix the wrong-object trap instead:
- the shim should declare its resolved engine path;
- --about/help should print registry scope and engine version;
- reading the shim must make it obvious that the eight-line wrapper is not the implementation.

Expand the registry only if multiple real workflows require ETFS pipeline reasoning.

10. comp-similar

Prioritize integration/distribution, not more features:
- ensure the repaired commit reaches the shared branch;
- print implementation version plus corpus vintage;
- retain the render-before-cite control.

11. comp-schedule and comp-denytest

No remediation is indicated by this run:
- comp-schedule returned a bounded NOT-DECIDABLE result;
- comp-denytest correctly had zero applicable population because no IAM change existed.

Do not turn truthful non-application into compulsory work.

NON-GOALS

- Do not make blind tools fabricate answers to satisfy preflight.
- Do not treat a gate-accepted blindness statement as resolution of the engineering risk.
- Do not widen every tool to every resource family.
- Do not combine the surgical comp-adversary collector repair with broader refactors.
- Do not leave a fix local: integration/version availability is part of completion.

Suggested order:
1. comp-adversary collector repair and mutation proof;
2. shared answer/absence/blindness disclosure contract;
3. comp-iam deny visibility;
4. comp-blast subject-existence distinction;
5. comp-trigger topology coverage;
6. comp-dataflow unresolved-expression diagnostics;
7. shim/engine self-identification.
