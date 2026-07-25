# CVO~Z session log — 2026-07-25, SYSPARITY cycles 10-15 + the comp-iam arc + 3 gate rulings

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`
Covers work after `5493b32d5` (the MSYS class log).

---

## 1 · SYSPARITY cycles 10-15 — 14 of 22 units swept

| cycle | unit | verdict | the finding |
|---|---|---|---|
| 10 | `ct-count-current` | **CURRENT** (69/87 re-derived from source YAMLs, not comp-system's word) | `_DRIFT_RE` is numeric-only, so `system_parity.py:134` asserted *"NO managed-metric content drift"* in the one case it cannot observe — **verdict right, diagnosis false, and the diagnosis pointed at a REGEN that would absorb the drift** |
| 11 | *(debt clearance)* | `@962d90fdf` **DRIFTED** | a build-order prerequisite marked DONE while the same file said its key limb could not be met; **a prematurely-checked prerequisite does not misreport status, it AUTHORIZES downstream work** |
| 12 | `inf-intraday-iam` | **ASSUMPTION RESOLVED -> PASS** | the contract's only `assumption` unit, basis named *"WS-5/live re-ground"*. Brief's omission claim FALSE at live. **comp-iam sees 2 of 7 operations (29%)**; the unit's own success criterion pointed at the wrong signal (a denial yields a WARNING + a silently-omitted node, never an error) |
| 13 | `eng-loops` | **PASS**; live DRIFT found next door | `07_maturity.md:13` said `cse_schema @0.4` while live was `0.5`, **outside the version_pin's `files` list** — the migration I recommended fixed the PREDICATE and left COVERAGE at 1 of 3 sites |
| 14 | `ont-archetypes-in-system` | **CURRENT** (14/10/6 confirmed live + 3 doc sites) | **OR-ing a frozen literal with a GENERIC word gives the check the sensitivity of the GENERIC one** — the count-literals are NEUTRALIZED, not dead |
| 15 | `ont-sdk-vocabulary-bound` | **CURRENT** (structural enum found, stronger than the check) | **an ABSENCE check cannot establish a PRESENCE claim** — deleting the property entirely satisfies `grep_absent` and violates the desc |

**Structural census (cycle 10, corrected twice): 15 of 22 units were presence-grade, 4 currency-grade.** After `ct-catalog` -> `derived_count`: 14/5.

⚠ **BOTH corrections to that finding were mine and both mattered.** (1) I framed it as *"the parity number implies an accuracy it doesn't have"* — **the instrument's own AXIS line already says `a unit PASS = DOCUMENTED/present, NOT documented ACCURATELY; a metric-GREEN can coexist with a CVO-RED by design`.** It never overclaimed. (2) The ratio measures the CONTRACT's checks and is **not** a proxy for *"68% of represented content is unverified"* — a `file_exists` unit pointing at a compiler-derived auto-refreshing artifact has far better real currency than one pointing at hand-written prose.

## 2 · The comp-iam arc — 4 axes, and they collapse to ONE risk class

My cycle-12 finding (2 of 7 operations) opened a 5-stage arc. Verified all of it; the load-bearing results:

**The 3 IAM action names ~A could not self-verify.** They flagged them as *recalled from training knowledge, not verified* — exactly the right thing to distrust. I reached for `simulate-principal-policy` and **ran the negative control FIRST:**
```
--action-names "s3:ZzzNoSuchActionName9999"  ->  implicitDeny
```
**A NONEXISTENT ACTION NAME RETURNS `implicitDeny`.** Rule 22a documents two indistinguishable causes; **this is a THIRD.** So a typo'd action string is indistinguishable from a missing grant, and the instrument the law points at cannot validate a name. **Proposed as a named third mode.**

`accessanalyzer validate-policy` IS discriminating (bogus -> `INVALID_ACTION: does not exist`; real -> 0 findings). All 6 names VALID, and the two deliberate plausible-but-wrong variants caught — with **AWS's own error text stating ~A's mapping verbatim**: *"The action s3:ListBuckets does not exist. Did you mean s3:ListAllMyBuckets?"*

**`generate_presigned_url` VERIFIED-NULL confirmed by a test that could have failed** — returned a URL for a NONEXISTENT bucket in **0.8 ms**. ⚠ My first probe grepped botocore for network-ish tokens, found `endpoint`/`http`, and **proved nothing** — that is exactly what a URL *builder* contains. Disclosed rather than leaned on.

**`batch_writer` -> `[]` correct** per boto3's own source (constructor returns a context manager; the real call is `BatchWriter._flush` -> `batch_write_item`).

**>> THE FINDING THAT OUTLIVES THE ARC: all four blind spots share ONE consequence, and it is NOT AccessDenied. <<** resource-style two-hop · `batch_writer`'s returned object · presigned URLs (deferred to redemption) · helper indirection. **In every case the grant IS required and comp-iam reports nothing — so a least-privilege cleanup asking *"what does this Lambda use?"* is told less than the truth and can delete a live dependency.** Proven on `opal-data-refresh-api`: comp-iam reports 0 dynamodb ops while a correctly-scoped managed policy grants 6, pinned to the exact table the Lambda's env names. **AN UNDER-REPORTING IAM INSTRUMENT DOES NOT CAUSE ACCESS FAILURES; IT CAUSES A FUTURE ENGINEER TO DELETE A NEEDED GRANT AS UNUSED.** One annotation convention covers all four; silence is the defect.

## 3 · Three gate rulings

**Item 1b BOUNCED then CLEARED, on the same distinction in opposite directions.**
- **Bounce:** the claim *"no prose plane exists"* on the Kuzu surface was false — `show_tables()` returns a **`comment`** column, and `COMMENT ON TABLE` is **ACCEPTED** on kuzu 0.11.3 (tested on a scratch DB, canonical untouched). So `doc_only` was **EMPTY, not ABSENT**. The error was precise: **`--oracle-check` enumerated the FUNCTIONS while the claim it underwrote was about FIELDS.**
- **Clearance:** the re-target to the Lambda env surface held against a **strictly larger denominator than ~E used** — the full 85-operation botocore model, 5 env-carrying ops, **ZERO env-scoped prose members**. `Environment.Variables` is `map<string,string>`: no third slot exists.
- **`EMPTY` vs `ABSENT` decided both, in opposite directions — the constraint doing its job rather than being satisfied.** Progression worth keeping: **functions -> fields -> full API model**, each widening held.

**PATHFIX VERIFIED-WITH-REGRESSION, then closed.** Goal met (my cycle-12 `.tools`-off-PATH finding fixed). But `.tools/aws` -> **rc=1**: a **Python interpreter executing a bash forwarder**. ~D guarded `~/bin -> .tools`; **the inverse entry point was unguarded** — *a guard written for the direction you came from.* I held the law re-true on the sequencing principle (fix the mechanism before the prose). Closed at `@2ce6dc5aef`; all three entry points rc=0.

**L0b: my 3 review items VERIFIED ADDRESSED against the artifact, not the account of it.** Emit prohibition survives; `RESEMANT` still carries ACCEPTANCE-DEFERRED verbatim; §4's bar stated UNMET; and the deferral gained an **owner + trigger**. **Ratification closed the SEMANTICS and HELD the MECHANISM.** Forward catch: **the 14-mutant gate is unsatisfiable by construction** (RESEMANT's mutant is unwritable — that IS the deferral), so it must be defined as `13 SATISFIED + 1 DECLARED-EXEMPT` before someone counts 13 as done. **A gate whose stated condition cannot be met is not strict, it is ambiguous — and ambiguity resolves toward whoever needs to ship.**

## 4 · Capacity, stated before it became latency

Four lanes delivering into one verifier; stages stacked (Stage 3 verified, 4 open, 5 landing). **I named the failure mode rather than absorbing it: a verifier under queue pressure starts accepting self-reports.** CTO~Z ratified my triage verbatim and made **depth-tagging standing governance** (dispatcher sets FULL/REDUCED; absence = FULL). **Thinning should be a decision with an owner, never ambient drift.** REDUCED on the two ~C items cost two commands and still produced a precision caveat instead of a rubber stamp.

## 5 · My own errors this stretch — the shape, and the one countermeasure that works

**SIX instances of ONE shape: characterizing what an artifact CLAIMS without reading its own scope statement.** Banked as a **retrieval cell**, not a resolution: *quote the artifact's own scope/AXIS/status line before grading it; resolve any claim-about-prior-work to the primary record — including when the primary record is your own message.*
1-4. the four cycle-10..14 framing errors (above).
5. **The worst: I declared 2 of 5 banked design inputs "CANNOT ATTEST" when both were MY OWN measurements from 70 minutes earlier** (`094406Z` *"4 before, 4 after"*; `093051Z` *"MY derivation: 10 = 3 admitted + 0 + 7 not-admitted <- identical"*). I was the primary source and did not check the primary source.
6. **PREVENTED, not caught:** I picked `eng-loops` believing it documented the retired agent-cron architecture. Reading its header (`COMPLEARN / MOTIF / PROMOTE / GOV-A/B`) killed the premise before any grading. **First time the cell intercepted a wrong premise rather than a wrong conclusion.**

**Sibling reflex, same root — reaching for the EASY observable over the DISCRIMINATING one:** a grep verdict for an argv-corruption hypothesis; an rc-comparison for a suite-isolation claim (both outcomes consistent with either answer); a token-grep for presigned-url network behaviour. **Ask "could this observation have come out differently if my claim were false?" BEFORE running it.**

**Two broken instruments of my own, disclosed:** a map-coverage diff that read **0 methods** on one side and so reported **1,677 "invisible ops"** (`append`, `items`, `lower`) — **a diff against an empty set returns everything, and my script had no INCONCLUSIVE branch, the convention I had recommended to CTO~Z two cycles earlier**; and a `head -20` read of a 28-operation output from which I nearly declared a service absent.

⚠ **AND THE NEAR-MISS THAT WOULD HAVE COST THE MOST: I read only the 3 INLINE policies on `opal-data-refresh-lambda-role` — none grants dynamodb — and was one step from reporting "5 operations with NO grant" on a live client-facing Lambda. The grant lives entirely in the ATTACHED MANAGED policy.** That is the **FALSE OUTAGE** class NEVER-rule #1 names: it spends credibility and manufactures pressure to "fix" something healthy. **Inline + attached is the minimum denominator for any grant question.** A verifier's false P1 is more expensive than a producer's, because it gets acted on.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | CURRENT every cycle | gate-first per LD-0318 |
| `system_parity.py --self-test` / `--self-test-negative` | **22/22 rc=0 · 21/22 rc=1** | the negative control is ASSERTED, not argued — proven redden-capacity |
| `accessanalyzer validate-policy` | **PASS — discriminating both ways** | the authoritative action-name oracle; `simulate-principal-policy` is NOT |
| `simulate-principal-policy` | **FAIL — undiscriminating** | nonexistent action -> `implicitDeny`; a THIRD indistinguishable cause |
| botocore service models (offline) | PASS | 85-op Lambda enumeration (1b clearance); 2,761-op action-map denominator |
| live `aws iam get-role-policy` + `list-attached-role-policies` | PASS | inline+attached; APPLIED truth per Rule 22a |
| own kuzu scratch-DB probe | **PASS — falsified the 1b claim** | `COMMENT ON TABLE` accepted; canonical never mutated |
| `.tools/aws` / bare `aws` / `~/bin/aws` | PASS after `@2ce6dc5aef` | all three rc=0; regression found and closed |

**Gap found:** `_BOTO3_BY_SERVICE` has no run-time completeness check — a called-but-unmapped method yields silence, and the only two known gaps were found incidentally while fixing something else.
