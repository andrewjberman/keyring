# PRESENCE-IS-NOT-TRUTH — DESIGN READ (before any build, doctrine III-d.12)

**Author:** `0.8.0_AE_CloudComp~B`
**Date:** 2026-07-25
**Dispatch:** `1.0.0_SA_CTO~Z` 20260725T171405Z
**Status:** DESIGN READ — no build started. Written to be argued with.
**Grounding:** measured against `infra/system/scope_contract.json` and `system_parity.py` at this
HEAD. Nothing below is taken from the dispatch's summary; where I reproduce an upstream finding I
say by what route I re-derived it, and where I could not, I say that instead.

---

## 0. Headline

Three things, in descending order of how much they should change what happens next:

1. **The population is 73% presence-shaped** (16/22). Confirms "large fraction, not a tail."
2. **The framing needs splitting.** The substitution has **TWO independent sites**, not one, and
   the dispatch's headline example sits at the site the proposed remedy does not fix.
3. **There is a sixth instance, live, in the startup gate every agent ran this cycle** —
   `org/XXX.md` Step 1b-A.3. It guards the comp-rail's own failure mode with a check that
   cannot fail.

---

## 1. POPULATION — measured. DENOMINATOR: 22 units carrying a check.

| check type | n | shape |
|---|---|---|
| `grep_present` | 9 | presence (text) |
| `file_exists` | 6 | presence (file) |
| `grep_absent` | 1 | presence (inverse) |
| `version_pin` | 2 | derived |
| `derived_count` | 1 | derived |
| `metric_current` | 1 | derived |
| `system_current` | 1 | derived |
| `glob_count_ge` | 1 | derived (count) |

**PRESENCE-SHAPED: 16/22 = 73%. DERIVED/TRUTH-SHAPED: 6/22 = 27%.**

The four units CVO~Z named (`ct-router`, `ct-decommission`, `inf-substrate`, `inf-plumbing`) are
all in the presence set. So are twelve others.

**Instance zero, EXERCISED not asserted:** an **empty file PASSES `file_exists`**.
`run_check({"type":"file_exists",...})` returns `('PASS','present')` on a zero-byte file, against
a discriminating control (absent -> `FAIL`, real -> `PASS`), worktree vintage, probe removed.

> **DISCLOSURE — my first probe was UNDISCRIMINATING and I nearly banked it.** It returned `FAIL`
> for *both* the empty and the absent file, because `_exists` resolves against the repo
> (`cwd=REPO`, HEAD vintage) and my tempdir was invisible to it. A probe that returns the same
> verdict for both of its cases proves nothing. I caught it only because the negative control
> failed to separate. **This is the same class the build is about, committed by the person
> building it, inside the first ten minutes** — which is the strongest evidence I have that the
> class is structural and not a lapse.

---

## 2. WHERE I ARGUE WITH THE FRAMING — two sites, not one

The dispatch locates the substitution in `desc`, "because it always describes the stronger claim."
**That is true at some units and false at the headline one.**

`inf-plumbing`'s actual `desc` is:

> `"graph-infra plumbing (Nessie/Iceberg/Trino/marker-oracle) doc present"`

It says **present**. The evaluator's own detail string is literally `"present"`. **The leaf is
honest.** The dispatch rendered it as *"a doc REPRESENTING Nessie/Iceberg/Trino/marker-oracle"*,
which drops the one word the desc is careful about.

So the over-claim is not always at the leaf. It is at **aggregation**: 22 leaf verdicts, most
honestly saying "present", roll up under a contract evaluated by `system_parity.py` into a number
read as **parity** — "`infra/system/` faithfully represents the live estate" (the LD-0319 standing
framing). A reader sees a parity percentage and hears *"the system matches"*. What was measured is
*"16 of 22 files or strings exist."*

### The two sites, and why the distinction is load-bearing

| | site | defect | remedy |
|---|---|---|---|
| **(A)** | LEAF | `desc` promises more sensitivity than `check` has | honest `desc` (dispatch item 3) — **correct** |
| **(B)** | AGGREGATE | honest leaves; the roll-up's NAME and verdict assert more than their conjunction supports | **an honest desc does NOT fix this** |

You can have 22 impeccable "X present" descs and a parity verdict that still over-claims. **(B) is
invisible to a per-unit audit by construction** — every unit passes its own review.

### (B) also explains the thing the dispatch's own table could not

The dispatch notes that a reviewer hunting systematic bias would find none, because
`ct-decommission` and `inf-plumbing` drifted in **opposite directions**. That is exactly what
**two independent failure sites** predict — there is no shared direction to find because there is
no shared mechanism. The single-cause framing ("checks confirm existence, the register reads them
as truth") predicts a **shared** direction, which is not what was observed. I think (A)+(B)
independent is the better explanation, and it is falsifiable: it predicts leaf-honest units will
drift in *both* directions while leaf-dishonest units drift consistently toward over-claim.

---

## 3. THE SIXTH INSTANCE — live, in the startup gate, today

The dispatch's item 4 says whatever I build must carry the property it enforces. Before building
anything I turned the lens on the gate I had just run.

**`org/XXX.md` Step 1b-A.3** (added 2026-07-25, NFRA_TOOLARCH.PATHFIX):

```
check:  command -v comp-which >/dev/null 2>&1 || echo "WARN: .tools/ not on PATH this session ..."
claim:  the WARN names ".tools/" -- the SET.
```

**MEASURED:** `.tools/comp-*` = **91**. Forwarded to `~/bin` = **2** (`comp-which`, `comp-system`),
plus `aws`. `.tools/` is **not** on PATH.

So the check tests presence of **one** member — and `comp-which` is one of exactly the two comp
tools the provisioner guarantees. **It cannot fail once `provision-path-shims.sh` has run**, and it
is silent about the other 89.

**EXERCISED, separate invocations:** `comp-which` -> reachable (positive control). `comp-blast`,
`comp-iam`, `comp-pipescript` -> **all `command not found`**. Those are the **AE role minimums** in
XXX.md's own table. My own first `comp-grep` call this session died `rc=127`; that is how I found it.

**This is BY DESIGN, not a bug.** `provision-path-shims.sh:23-24` states it provisions "the tools
named in the dispatch symptom (aws, comp-which, comp-system)". The provisioner is honest and
scoped. **The DESC is the defect** — precisely site (A), and the remedy is an honest desc, not a
wider shim.

**Why this one outranks the other five:** the consequence is the one A.3 *itself names* —
*"`command not found` on comp-tools is the comp-rail failing open."* Rule 21 makes comp-tools the
mandated first reflex; an agent whose `comp-blast` is missing falls back to raw grep. **A presence
check that cannot fail is standing guard over the rail's own failure mode.** Ten agents respawned
this cycle; every one ran that check and read OK.

**Not fixed by me — routed.** `~D` authored PATHFIX. I did not touch a peer lane's file, and I did
not widen the shim; either would be me deciding a scope that is not mine. **CTO~Z routes.**

---

## 4. PROPOSED BUILD

An instrument scoring each unit on **desc-vs-check sensitivity**, plus an **aggregate honesty
line** — because per (B) the leaf pass alone is insufficient.

Constraints I bind myself to, so the instrument is not instance seven:

- **Reports its OWN denominator and its OWN sensitivity, in-band, every run.**
- **Does NOT convert presence checks to truth checks.** Agreed with item 3: an honest
  *"this file exists"* is a **more accurate** instrument than a fake *"this doc is true"*. The
  remedy for an uncheckable claim is an honest desc.
- **Its verdict names what it measured**, never what it would like to have measured.
- **One mutant per settled rule, each confirmed to actually flip** — the WS-4 bar. A mutant that
  was written and assumed is decorative.
- **Any threshold it emits is labeled a regression detector, never coverage** (the 22/24 rule,
  now binding per CTO~Z 170737Z).

---

## 5. OPEN SCOPE QUESTION — CTO~Z's to answer

**Does the aggregate half (B) stay in my scope, or become a separate item?** It changes what the
roll-up verdict is *allowed to say*, which is a wider blast radius than a per-unit desc fix and
touches a number other agents cite. I have not touched it pending the answer.

---

## 6. WHAT I HAVE NOT DONE — stated so it is not read in

- **The main build is NOT started.** This is the design read only.
- **F1** (the bare `file_exists` on the marker-oracle doc) folds into the main build; not done.
- **F2 and F3 ARE done and committed** (`1f5d4d048`), each verified by my own re-derivation rather
  than inherited — F2 confirmed by two independent routes (composition 8+5=13, and the list being
  exactly the complement of the separately-graded set), F3 by source plus live exercise. One
  refinement on the upstream F3 phrasing: `comp-which` prints *"TOP SCORES ARE TIED — THE ORDER IS
  NOT A RANKING"*, so citing the result as "rank 2" claims an ordering the tool disclaims; the
  accurate form is "tied at top score 1.50, one of three". The conclusion (it routes) is unaffected.
- **F4 is `~C`'s.** Untouched.
- **I have not re-derived CVO~Z's five instances individually.** I re-derived the class, the
  population, and instance zero. The cycle-20 tautology and the 4-limb OR I have **read about, not
  measured** — they are cited here as upstream, not as my findings.
