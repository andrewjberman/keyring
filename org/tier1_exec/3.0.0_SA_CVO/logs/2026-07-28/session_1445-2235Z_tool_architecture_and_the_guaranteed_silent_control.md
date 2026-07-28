# 3.0.0_SA_CVO — session 2026-07-28T1445Z..2235Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

Continuation of the 1258-1445Z window (`cecd61d38`). Andrew-direct throughout: the archetypal-pattern
program, then the tool-registry architecture, then the `comp-opalbizcluster` reroute, then a standing
certifier role. **Six deliverables landed. The doctrine instance at §7 is the one CTO asked me to log
and it is the most useful thing in the session.**

## 1 — Archetype / runtime-provenance brief (`d4fee91bc`)

Andrew: hammer down archetypal patterns; the S3 code-import scenario is a dynamic we have not brought
under OPAL_STNDRD/OPAL_TAXONOMY. **Central finding: our scanners model an estate where code lives in
the repo, while Rule 12 REQUIRES that EC2 code does not** — the tooling contradicts the standard it
exists to enforce. Gap measured, not asserted: token census over `NFRA_TOOLARCH_PRD.md` returns
`provenance` 0 / `Rule 12` 0 against positive control `archetype` 12.

Seven dimensions established with live denominators (191 Lambdas, 34 EC2, 131 time-triggers across
two services, 39 buckets). **Sharpest measurement: 5 of 5 data buckets carry runtime `code/` prefixes
while all three dedicated artifact buckets are empty of it.**

## 2 — Coverage-universe requirement + the pattern library (`adc009888`, `a3dac97be`, `bc709b569`)

The type-2 shape: **a tool asked outside its universe does not error, it returns CLEAN** — a false
negative indistinguishable from a true one at the call site. comp-heat's universe enumerated: 24,605
tracked, **21.2% vendored**, four structural exclusion classes including the entire portal.

Four enumeration patterns abstracted from live instances — DERIVE / SIMULATE / CROSS-DERIVE /
ATTRIBUTION. **CROSS-DERIVE is the answer to Andrew's "even if the negative control has no true
oracle": two independent derivations differenced yield a negative signal with no ground truth.**

**Three corrections against myself in ninety minutes**, all understating what COMPUNIFY had built
(exclusions "written nowhere" — false; 36 tools — actually 88; S2 gate "not built" — it runs and
PASSES). Each from reading a document instead of exercising the thing.

## 3 — Enumeration primitives resolved 57 → 0 (`a4a3b1e`, harness committed)

93/93 classified. **The finding was not the count: my classifier had no `SIMULATE` primitive — Pattern
B from the library I had written four hours earlier.** Five tools use it; three came back unresolved
(and so announced themselves) but **`comp-which`, `comp-whoread`, `comp-deadgrant` resolved on other
primitives and read as fully classified while their strongest mechanism was invisible.** An
unresolved tool announces itself; an under-classified one reads as complete.

## 4 — The tool registry architecture (`78336e300` + predecessors)

Andrew's design call: light card for agents, heavy master otherwise. Built C-for-authorship +
B-for-delivery. **Justification measured: `comp-which` re-parses 133KB of YAML per call, ~97% of
runtime (AE~B cProfile). Compiled index: 0.4ms warm import — 7,726x.**

Hand-authored surface reduced to **two fields**; everything else derived or measured.

**CTO ruled the placement neither fold nor peer:** coverage-map is sole POPULATION authority, master
may be an ATTRIBUTE store, generator must FAIL LOUD both directions. **His control fired on first
exercise and caught my own defect: authority 89, master 89, COUNTS IDENTICAL, 12 DIVERGENT MEMBERS.**
Three causes, and the third was a silent `continue` dropping unclassified tools from the master.

## 5 — `comp-opalbizcluster` (ex-`pipescript`) — root cause + solution (`OPALBIZCLUSTER_REROUTE_SOLUTION`)

Andrew renamed it (`estate` is ontologically taken by platform surfaces; this groups business
clusters) and told me to verify the kuzu blocker myself rather than route it.

**I retracted my own finding mid-investigation:** I reported "no S3-key node type exists" — there are
**232 `S3Key` nodes**. My predicate was `CONTAINS 'KEY'`, case-sensitive, against a type named
`S3Key`. **Positive control passed, denominator right, FILTER still wrong — a control on the retrieval
does not catch a defect in the predicate.**

Root cause source-confirmed: `extract_gold_compute.py` **constructs** the bucket as `opal-data-<firm>`
from a hardcoded firm map, so `opal-data-assets` and `opal-data-portal-v2` **can never appear.** And
extending the map would not help — the new key's writer is the Rule-12 S3-resident dispatch script,
invisible to a repo scanner. **The graph inherits comp-clobber's exact blindness via the same
primitive over the same source.**

## 6 — Step 1 landed: the served-prefix registry (`.tools/served_prefix_registry.yaml`)

Demand-anchored denominator: **46 keys in scope, not 957.** The dump rule caught `json/sentiment/`
(722 keys / 5 endpoints) automatically. **The registry never derives a key from a URL** — measured,
because `/api/general/mdpf/aggregate-aua-timeseries.json` coexists with both the bare and the
`global/` key, and a naive transform picks the wrong one.

**Two defects in my own generator:** the documented bare-`bash`-from-Python trap (failed SILENTLY,
demand side returned zero), **and the worse half — it wrote the registry anyway**, declaring zero
coverage at rc=0. Both sides now raise `EmptyDenominator` and refuse to write.

## 7 — THE DOCTRINE INSTANCE (CTO: "yours to log")

Assigned standing certifier of Andrew's MDPF DONE definition D1-D4. I pinned four criteria **before
any evidence existed** — including my own D2 standard: *"CloudTrail showing NO manual invoke."*

CTO corrected the general point (Lambda data events are often disabled). **I then measured these two
specific trails:**

    opal-organization-trail       Lambda data events = 0
    opal-served-key-write-trail   Lambda data events = 0

> **I HAD PROPOSED A GUARANTEED-SILENT CONTROL AS MY OWN CERTIFICATION STANDARD, ON THE CONDITION
> ANDREW CARES MOST ABOUT. It could not have fired. Its silence would have read as "no manual
> invoke" — a PASS.**

**This is the failure I spent the entire session cataloguing in other people's instruments**, applied
to my own, one message after writing *"a control that cannot fail is not a control."*

**The generalisable rule, which is not the same as the one I already knew:** I have been demanding
that instruments carry positive controls. This adds a prior step — **measure whether the instrument
EXISTS AND CAN FIRE, before adopting it as a standard.** A positive control validates an instrument
you have; it says nothing about one that is switched off. **The check must run before the evidence
window, because afterwards the distinction is unrecoverable** — which is exactly why the follow-on
(no MDPF stage logs its triggering event; `inf-portal-publisher:919` has the one-line pattern to
copy) was time-critical rather than merely open.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-kuzu` | 6+ queries, PASS | provenance header read each call; 20,431 nodes / 40,856 edges, built 2.9h |
| `comp-coverage-check` | PASS, exercised | 88 homed tools, 12 gate rules — the run that corrected my "not built" claim |
| `comp-heat freshness` | PASS | 24,769 files; the worked coverage-universe instance |
| `comp-clobber` (both modes) | blind, as found | static + `--live`, neither surfaces the MDPF clobber |
| `comp-which` / `comp-grep` / `comp-glob` | PASS | timing corpus for the cost bands |
| `safe-commit.sh` | 12 commits | two gate BLOCKS honoured (ruff on a generated file; comp-system) |

**Rail note:** raw `aws`/`git`/`grep` used throughout with inline `# rail-checked:` markers — the
session's subject WAS the comp-tool layer, and routing its own inspection through a comp-tool makes
the instrument its own auditor. Stated, not assumed.

## Carried forward

- **Certifier role is STANDING and attaches to the SERIAL** (PIN-5), not this session. **D2 cannot
  close before tomorrow's unattended fires; stage-1 evidence NEVER closes it.** A successor inherits
  this in writing via `MDPF_RESET_DIRECTIVE_20260728T2220Z.md`, not by recollection.
- **AE has a time-critical build item**: the triggering-event log line on `mdpf-daily-trigger` +
  publisher, before the fires. Routed by CTO, priority-inverted.
- `comp-opalbizcluster` steps 2-3 (producer + `ServedURL→S3Key` edge) belong to an AE lane —
  deliberately not mine, because a producer feeding the canonical graph must not have its author as
  its verifier.
- Two audited `system-current-override`s ride today's commits, **neither carrying the conventional
  regen promise** — ~17 uncommitted peer files would have been swept. 06 currency not claimed.

— 3.0.0_SA_CVO
