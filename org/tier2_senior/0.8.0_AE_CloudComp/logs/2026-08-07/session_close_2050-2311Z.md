# Session close — the W2-1 retraction window (2050–2311Z)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, COORDINATE

**Agent:** `0.8.0_AE_CloudComp` (base) · **Window:** since `mdpf_remed_w2-1_consumer_census_1900-2050Z.md`
**Commit this window:** `0699c00b8f`

---

## Current State

**Both task orders issued to this seat today are COMPLETE and landed. Nothing is in flight.
Nothing is blocking me. No GO is open.**

| TO | status (verified in git at HEAD) | commits |
|---|---|---|
| `NFRA_PYFIELD.TO-1.pyfieldrecognizer` | `complete` | `50ff3747bf`, `7128f1a785` |
| `MDPF_REMED.W2-1.shape-contract-consumer-census` | `complete` | `9f1396bc7c`, amended `0699c00b8f` |

Working tree clean of my work (one untracked scratch dir, `.scratch-pyfield/`). Inbox empty.
Watcher `b49yuj1rx` running (child pid 4022496). Zero crons armed.

**Artifacts a successor needs:**
- `org/modules/graph/comp_recognizers_pyfield.py` — `PyFieldRecognizer`, the only new component.
  Runner: `python org/modules/graph/comp_recognizers_pyfield.py <roots> --resolver <v1|v2>
  --marker-set <MINIMAL|STRICT_DERIVED|WIDE>`. `format_coverage()` **raises** without a `Pins`.
- `org/modules/graph/tests/test_comp_recognizers_pyfield.py` — 43/43, six mutant controls.
- `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_PYFIELD_COVERAGE_20260807.md`
- `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/MDPF_R9_R12_CONSUMER_CENSUS_20260807.md`
  — **§4 was AMENDED this window; read §4 before citing anything about R-12.**

### What happened in this window: a peer falsified a committed finding of mine, and they were right

`0.4.0_DS_ClientPlatform` answered a question I had explicitly banked as *not a request* — the
identity of the producer of the 8 unrecognised A4 keys. Their answer overturned my R-12 framing.
**I re-verified all three of their citations at source before amending anything**, then retracted
two claims:

1. **RETRACTED: "the row names the wrong mechanism."** I wrote that R-12's `_`/`-` normalisation was
   not involved, because both invisible SERVED keys are hyphenated and `data/mdpf` carries zero
   `_`→`-` normalisation (57 files). **The narrow measurement stands; the generalisation does not.**
   Verified at source: GOLD is UNDERSCORED (`dim_mdpf_account_distribution.py:328`
   `account_units.json`; `dim_mdpf_non_model_assets.py:86` `non_model_assets.json`), SERVED is
   HYPHENATED. Same logical artifact, two spellings. The publisher's `_KEY_RE`
   (`lambda_function.py:88`) admits `_` in the **scope** group and only `-` in the **artifact-type**
   group. **The row was pointing at something real, one layer above where I searched.**
2. **RETRACTED: "producer unidentified."** `opal-assets-mdpf-portal-publisher/lambda_function.py:84`
   — `R12_EXTRA_PAIRS = (("cottonwood","account-units"), ("global","non-model-assets"))`.
   **The constant is named after the register row.** The publisher knows five artifact types; the
   consolidator knows three. And the asymmetry that hid them is confirmed at source: the
   consolidator **CONSUMES** `account-units` (folds the count into `total.account_units` on all four
   scopes, `:337-339`) while never emitting it.

**My generative-vs-observational finding is UNCHANGED** and rests on its own measurement (14 pairs
served vs 12 generated; `a4_expected` and `emitted` both derived from the same closed tuple). Both
mechanisms are real and different; fixing either alone leaves the other. **R-9, R-10 and R-11 are
untouched — none depended on this. Nothing moved; still evidence only.**

### The diagnosis, because it is not the failure my own discipline was pointed at

**A CORRECT MEASUREMENT OVER THE WRONG DOMAIN.** Not a truncated scan, not a missing denominator,
not an unnamed blind spot — my sweep was exhaustive *within* `data/mdpf` and the producer was never
in `data/mdpf`. **No way of calling `comp-find` differently catches that.** It is the DESIGNED half
of the retrieval-control class (CLAUDE.md § "Put the control on the RETRIEVAL, not the pattern"),
whose only remedy is corroborating OUTSIDE the instrument's domain. **I named that class in my own
§4 and walked into it one section later.** COO's note: the same thing happened to four seats today,
including them twice. *Naming a failure mode does not immunise you against it.*

### The hazard this produced — now the sharpest output of W2-1, and it is DS's

> **A census keyed on the GOLD spelling reads the SERVED keys as orphans; one keyed on the SERVED
> spelling reads the GOLD ones as orphans. BOTH FAIL TOWARD RETIRING A LIVE FIELD.**

My own census is the worked example: I keyed on served, found 8 keys with no emitter, and wrote
*"producer unidentified"* — **one inferential step from "unowned," in a document whose verdicts
authorize retirement.**

⛔ **AND IT COMPOUNDS WITH A CVO FINDING COO RELAYED:** several of these objects are **REGENERATED**,
so **deleting the gold twin is a NO-OP that returns next run while deleting the served one is real.
Same filename family, opposite consequences per layer.** This defeats the obvious safety check — the
no-op reads as reassurance and is actually a **false positive control**, strongest exactly when it is
least informative.
**GUARDED SET (travels together):** `account-units`/`account_units`,
`non-model-assets`/`non_model_assets`, and the hyphenated `account-distribution.json`, a known
**LIVE SERVED PORTAL BELL** that must never read as deprecated.

### Process ruling banked (COO, this window) — I will not re-ask

```
MID-FLIGHT, TO OPEN             -> surprise channel, ONE line, banked. Do not re-open, do not thread.
AFTER CLOSE, RECORD COMMITTED   -> that is REVIEW. Corrections land IMMEDIATELY.
```
*"The flow rule protects WORK IN PROGRESS from churn. It does not protect a COMMITTED FALSEHOOD from
correction."* Complements the Andrew-direct flow rule already saved at
`memory/feedback_make_a_plan_complete_the_plan_then_review.md`.

---

## Blockers

**None.** Evidence-cited: both TOs read `complete` in git at HEAD, inbox empty, no open RAVC of mine.

**NOT winding down** — standing rule is that a session winds down only when Andrew says so. COO's
*"not stacking another TO on you tonight"* is a routing decision, not a stand-down. Status is
accurate on the broker and capacity is free.

---

## MCP traffic

**8 messages this session** (5 sent, 3 received). Significant only:

| dir | peer | substance |
|---|---|---|
| in | `2.0.0_SA_COO` | GO — MDPF_REMED.W2-1 |
| out | `2.0.0_SA_COO` | ACK + plan; then RAVC close; then the CORRECTION; then availability |
| in / out | `0.4.0_DS_ClientPlatform` | collision query on `route_bindings.yaml` → their diff-grounded answer (settled vintage `f999fb25f6`, **UNPUSHED**) → their unsolicited producer answer that falsified my R-12 framing → my retraction |
| out | `1.0.0_SA_CTO~D` | NFRA_PYFIELD PRD §2.1 `layer=portal` finding (now banked in the register as **R-29**) |
| in | `2.0.0_SA_COO` | correction ACCEPTED, verified at their seat, corrected upward to CTO |

⚠ **Broker channel replayed already-actioned messages on three consecutive heartbeats** — reading
from the watcher's `read/` dir does not drain the channel (only `check_inbox(mark_read=True)` does).
Harmless if recognised; it is the shape that gets closed work re-done. Banked, not escalated.

---

## Next Steps

1. **[Andrew]** R-9 `last_updated` → `_provenance`. Evidence in census §1. **Fix the
   `DataSourceContext.tsx:106` fallback chain to fail loud BEFORE the move** — it currently falls
   through to the client's own clock, rendering a stale as-of as *now*.
2. **[Andrew]** R-10 canonical-or-not. Client surface clear (0 portal source consumers,
   positive-controlled); cost is three internal instruments, ordered in census §2.
3. **[`1.0.0_SA_CTO`]** R-12: make the completeness check OBSERVATIONAL and the universe a PREDICATE
   over the real listing. ⛔ Must NOT become "delete the two unrecognised types" — owned and live.
4. **[`2.0.0_SA_COO`]** R-11: close as resolved-by-convergence (register edit only, cost zero).
5. **[`2.0.0_SA_COO`]** Next GO for this seat. Seven base TOs held, all `staged`/`pending`.
   **Recommended: `NFRA_TOOLHEALTH.TH-C`** — only `staged` one, own lane, no cross-seat dependency.
   Flagged that PASSCRAFT TO-1/-2/-3 look like one sequenced body whose TO-1 gates the other two.
6. **[`1.0.0_SA_CTO~D`]** NFRA_PYFIELD PRD §2.1 records fix (already banked as register R-29).

---

## Compiler Tools

Verification-only window — **no tool was re-run for this table** (speed contract). The runs below
are the ones that carried the retraction; the full per-TO tables are in the two prior logs.

| Tool + command | Result | Disposition |
|---|---|---|
| `git show HEAD:<TO path>` × 2 | both `<status>complete</status>` | PASS — TO states verified **in git at HEAD**, not from the working tree or recollection. |
| source reads × 3 (`lambda_function.py:82-88`, `mdpf_gold_consolidator.py:337-344`, `dim_mdpf_*:328/:86`) | all three DS citations CONFIRMED | PASS — **the gate on amending.** I did not amend a committed record on a relayed claim; Rule 22 grounding before retraction. |
| `git log --author=... --since` | window scoped | WARN — `--since` takes LOCAL time, so a UTC-framed window silently under-returns (it dropped both PYFIELD commits on first run). Caught by cross-checking against the TO statuses. Same class as the rest of today: a retrieval whose narrowed domain is invisible in its output. |
| `TaskOutput(b49yuj1rx)` | `running` | PASS — the only probe that observes a *consumer*; watcher liveness confirmed, not inferred from `ps`. |

**What worked:** grounding DS's relay at source before amending. Their answer was correct in every
particular, and I would have amended on it either way — but a retraction that rests on a relay is the
same defect one hop over.
**What failed:** nothing this window. The failure was in the *prior* window and is retracted above.
**Gap found:** none new. The banked one stands — `comp-transform schema-check` cannot see a React
**context** file, though `DataSourceContext` performs a live served-field read.
