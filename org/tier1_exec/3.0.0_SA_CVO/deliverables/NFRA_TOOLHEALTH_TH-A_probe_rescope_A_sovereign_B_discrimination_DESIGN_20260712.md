# TH-A EFFECTIVE probe -- (A) sovereign re-point + (B) frozen-vs-fresh discrimination: DESIGN for CTO gate

**author:** 3.0.0_SA_CVO~B · **date:** 2026-07-12 · **status:** DESIGN (gate-before-build, CTO)
**re:** Andrew-direct TH-A EFFECTIVE-probe dispatch; premise corrected (probe EXISTS, RAVC-accepted 07-06);
CTO re-scope AUTHORIZED (A)+(B) + GAP-2/3 ruled (exercised probe = SOLE authoritative `effective`).

## 0. What is NOT being built (the correction that scopes this)
NOT a green-field probe. `org/modules/graph/compproof/{tool_probe.py, tool_corpus.py}` exist, ran (emitted
`effective_feed.json`), and the TO is `<status>complete</status>` + COO RAVC2-ACCEPT + my own TH-V honesty
verify. This is an EXTEND of that accepted artifact: (A) remove a sovereign breach, (B) add the honesty
half it lacks. The `effective` bool's authority is the exercised probe (CTO 134939Z); PASSCRAFT ToolAudit
is decoupled (assurance-plane annotation, R0-barred from `effective`).

## (A) SOVEREIGN RE-POINT -- off opal-data-bd -> inf/cot/mdpf
- **Breach (confirmed, CVO-base co-verified):** `tool_corpus.py:74` `run=[comp-freshness, artifact,
  s3://opal-data-bd/silver/prices/canonical_prices.parquet]` and `:105` `run=[comp-freshness, chain, bd]`,
  both `live_estate=True`. Exercising the probe reads opal-data-bd = a live sovereign-hold breach. CTO
  verified NOT-imminent (no active cron; on-demand, last-ran 07-06) -- priority, not emergency.
- **Fix:** re-point both comp-freshness probes to IN-SCOPE anchors (opal-data-inf / cot / mdpf), and make
  the corpus **sovereign-safe by construction** -- a corpus-load assert that NO `run` entry contains a held
  path (reuse `sovereign_held.is_held_path` / `is_held_bucket`; a bd target in the corpus fails the load).
  So the recurring design (7d, --ensure-fresh) can NEVER touch bd on a re-run.
- **Anchors (grounded, in data/inf|cot config):** the positive artifact case -> an inf served artifact with
  an `as_of_field` (content-mode, a genuine positive: comp-freshness reaches a usable verdict). The bd
  `chain` latency-fix probe is REPLACED by the (B) negative case (a false-GREEN catch is a stronger,
  honester FIX-signal than latency).

## (B) THE HONESTY KEYSTONE -- paired frozen-vs-fresh DISCRIMINATION (the un-gameable half)
- **Why it's needed (CTO-affirmed):** a REACH x USABILITY probe is a SOFT exit-0 proxy for a
  PLAUSIBLE-BUT-WRONG answer. The existing corpus scores comp-freshness via LATENCY (too-slow), never the
  false-GREEN. So the sensor cannot yet catch the exact lie it exists to catch.
- **The PRECISE lie to test (grounded, comp-freshness :706-723 + test_freshness_partition_key_anticorrelated):**
  NOT honest mtime-mode (comp-freshness reporting mtime when it only claims mtime is not a lie). The lie is
  the **as_of / partition-key mode**: comp-freshness CLAIMS to check the content date-key, but its reader is
  ANTI-CORRELATED (reads LastModified, not the date-key) -> says FRESH on a frozen-content / fresh-mtime
  artifact. THAT is exit-0-while-lying.
- **The negative-case probe:**
  - INPUT: a served artifact in as_of/partition-key mode with **content data_as_of = frozen** (e.g. 30d old)
    and **mtime = fresh** (recently rewritten).
  - RUN: comp-freshness on it (exercised).
  - ORACLE (independent of comp-freshness): the artifact's **actual content data_as_of** (read directly),
    which is 30d old = STALE. This is grounded OTHER than the tool (comp-freshness uses mtime; the oracle
    uses the content). `oracle_run` = that direct content read.
  - VERDICT: comp-freshness MUST say STALE/FAIL. GREEN/PASS => effective="no" (the false-GREEN caught).
  - Note the complementarity with the fix-TO: PRE-fix the probe correctly scores comp-freshness
    effective="no" (freeze-blind); POST-fix (tool catches the freeze) -> effective="yes"; the probe then
    REGRESSION-GUARDS that comp-freshness keeps catching freezes.
- **How to source the frozen artifact (CTO ruling asked -- 2 options):**
  - **B1 [recommend] controlled synthetic fixture, per-run:** the probe WRITES a synthetic artifact to a
    scratch IN-SCOPE location (e.g. `s3://opal-data-inf/_probe_fixtures/frozen_<runid>.json`) with a frozen
    content-date + fresh mtime, runs comp-freshness, asserts STALE, deletes it. Deterministic ground-truth
    (I control "frozen"), self-contained, no persistent artifact. Cost: an S3 write+delete per run to an
    in-scope scratch prefix.
  - **B3 permanent frozen fixture:** one deliberately-frozen artifact committed at a scratch in-scope
    location (content-date fixed in the past, never updated), documented as a probe fixture. No per-run
    write; a stable permanent anchor. Cost: a permanent test artifact + its config entry.
  - (B2 "find a live frozen anchor" REJECTED: time-dependent, un-freezes, fragile.)
  - **DECISION FOR YOUR GATE:** B1 (self-contained) vs B3 (stable, no per-run write) + the scratch
    location/bucket. I lean B1 unless you'd rather not have the probe do an S3 write.
- **EXTEND the discrimination pattern (CTO-authorized) beyond comp-freshness:**
  - **comp-iam:** oracle = `aws iam simulate-principal-policy --resource-arns <exact key>` (AWS-authoritative,
    NOT comp-iam's DESIRED model). Negative: a role WITHOUT a permission on a specific resource -> comp-iam
    must NOT report GRANTED. A GRANTED on an un-granted (action,resource) => effective="no". (This is the
    exact `(action,resource)`-blindness from Rule 22a.)
  - **comp-aws score:** negative = `score --class <nonsense>` must NOT log PASS (rc INVALID). A PASS on
    garbage => effective="no". (comp-aws was rebuilt to rc-discriminate; the probe regression-guards it.)

## OUTPUT CONTRACT (LOCKED 2-way with CVO-base, CTO-ruled)
`compproof/effective_feed.json` -> `{tool: {effective: "yes"|"no"|"unknown", reach, usability,
effective_evidence: {case: "positive"|"negative", observed, expected, oracle_run}}}`.
- **tristate** (not bare bool): unknown=VOID explicit -- a "no" MUST mean measured-not-effective, never
  couldn't-measure (fail-closed; the CANNOT-EVALUATE vs FAIL honesty law). yes/no/unknown -> True/False/None.
- **oracle_run = an EXERCISED run + its captured output, NEVER a source file:line** (the shared honesty law;
  a file:line reach is R0 reading-confidence -- what bars the hand-authored ToolAudit from `effective`).
- CVO-base's wire reads `{tool: effective}`, maps to `classify_full`; AC2 = comp-freshness effective="no"
  flips KEEP->FIX.

## SEPARATE fix-TO (CTO-directed): comp-freshness anti-correlated freeze-detector
`test_freshness_partition_key_anticorrelated.py` proves `_max_partition_date` reads LastModified, not the
date-key -> "can NEVER fire on the freeze it names." A real comp-freshness DEFECT (the tool, not the probe).
Open a fix-TO. **Gate question:** do I own that fix (CVO), or route to COO for a formal TO / the tool owner?

## THE NON-GAMEABLE FIXTURE BAR (the honesty proof CTO gates on)
1. positive: an in-scope artifact where the tool honestly reaches -> effective="yes".
2. negative bite: the frozen fixture -> comp-freshness (pre-fix, anti-correlated) says FRESH -> probe scores
   effective="no". MUTANT: neuter the negative arm -> the probe wrongly scores effective="yes" -> the
   honesty test FAILS (proves the negative arm is load-bearing).
3. VOID/unknown: an isolation-broken / un-runnable case -> effective="unknown", NEVER a silent "no".
4. ORACLE-INDEPENDENCE self-test: assert the oracle for tool T never invokes T (a probe whose oracle is the
   tool measures nothing -- the meta-honesty guard).
5. SOVEREIGN self-test: corpus-load asserts no held path in any `run` (A's by-construction guarantee).

## OPEN DECISIONS FOR YOUR GATE
1. B1 (per-run synthetic fixture) vs B3 (permanent frozen fixture); the scratch in-scope location/bucket.
2. The exact inf/cot/mdpf anchor for the positive artifact case (I'll pick a stable as_of-mode inf artifact;
   confirm inf is the right firm vs cot/mdpf).
3. comp-freshness anti-correlated fix-TO: CVO-owned vs routed to COO/tool-owner.
4. Scope of the starter extension: comp-freshness + comp-iam + comp-aws this pass, or comp-freshness only
   first (then iterate)?
On your gate I build to this + emit to the locked contract; CVO-base finalizes the wire; AC2 live-run then
has a sovereign-safe corpus + a real false-GREEN negative catch.
