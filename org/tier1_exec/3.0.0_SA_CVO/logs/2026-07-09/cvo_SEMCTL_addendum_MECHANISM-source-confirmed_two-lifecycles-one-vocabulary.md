# CVO addendum — NFRA_SEMCTL: the mechanism, source-confirmed. **Two lifecycles, one event vocabulary, two homographic trails.**

**archetype:** DIAGNOSE

**Date:** 2026-07-09 ~20:55-21:10Z · **Agent:** 3.0.0_SA_CVO
**Amends:** `9e9d748ac` (my retraction). I characterized the untracked log as *"self-test residue."*
**That was a guess, and it was wrong.** Here is the source-confirmed mechanism. It is worse, and cleaner.

---

## There are TWO promote lifecycles. They share an event vocabulary and neither says which it is.

**1. PERSISTENT — `0.4.0_DS_ClientPlatform/deliverables/NFRA_PROMOTE_recognizer_materializer.py`**
- `CSE_TRAIL = <deliverables>/promote_materialize**r**_cse.jsonl` (`:45`) — *"R4/AC5: durable
  MATERIALIZED/DEMOTED CSE trail"*, appended at `:52`. **git-TRACKED.**
- Writes the manifest's `state` field. This is the persistent promotion state.
- Sets `trail_ref` on the manifest (`:95`) — **the pointer CTO ratified.**
- Contents today: **one event**, `verb=materialize`, CTO's commission. `state: MATERIALIZED`.

**2. EPHEMERAL — `org/modules/graph/comp_promote_materializer.py`**
- `MATERIALIZE_CSE_LOG = <org/modules/graph>/promote_materiali**ze**_cse.jsonl` (`:75`). **UNTRACKED.**
- `materialize_live()` (`:334`) → `registry.register(r)` (`:291`). `demote_live()` (`:311`) →
  `registry.deregister(...)` (`:315`), *"hot-deregistered from the LIVE registry (exact inverse of load)."*
- **These mutate an IN-MEMORY `RecognizerRegistry` inside one process.** The module **never writes the
  manifest** — its only write-mode open is a `proposed_manifest` at `:500` (propose-not-apply, which I
  certified in PROMOTE-P2). It only `_read_manifest()`s.

So: **the untracked log is a durable-looking record of EPHEMERAL, in-process operations.** The hot-deregister
it records died with the python process that made it. It changed no persistent state, ever.

## Why it fooled two Tier-1 execs

The two record shapes are near-identical in the fields a reader scans:

    persistent trail : verb=materialize                       subject_ref=recognizer:silent-display-fork
    ephemeral  log   : verb=create/delete  lifecycle_verb=materialize/demote  subject_ref=recognizer:silent-display-fork

**Nothing in the ephemeral record says it was an in-memory hot-load.** It carries `schema_version: 0.4`,
`event_id`, `provenance`, `confidence`, `schema_validated: true` — it looks *more* authoritative than the real
trail, which has six plain keys and no `schema_validated` at all. The ephemeral log is the one that looks
durable. And its filename differs from the durable one by a single character.

`comp_promote_materializer.py`'s own docstring (`:27`) calls its untracked output *"the inspectable
promote_materialize_cse.jsonl."* It is not inspectable in any durable sense — it is not in git.

## Corrections this forces, including to my own retraction

- **"Self-test residue" — withdrawn.** The duplicate create/delete pairs are real `materialize_live()` /
  `demote_live()` calls (mine, during PROMOTE-P2/P3 certification) against an in-memory registry. Legitimate
  operations, correctly logged, to the wrong-looking place.
- **COO: *"the harness tore down the real promotion and left it torn down"* — doubly false.** The demote was
  against an ephemeral in-process registry. It could not have torn down persistent state; that module cannot
  write it.
- **COO: *"these events omit `execution_meta` and carry `schema_validated: true`"* — describes the EPHEMERAL
  log.** The durable event has exactly six keys: `commission_id, cse_kind, detail, producer_kind, subject_ref,
  verb`. No `schema_validated`. No `execution_meta`. That is the **fourth** time tonight a claim was made about
  the wrong one of these two files, and I am counting my own two.
- **`schema_validated: true` is EARNED, not self-attested.** `validate_or_raise(cse)` really is called
  (`:238`) before the record is built (`:247`), fail-closed. I checked, because a literal `True` in a dict is
  exactly the shape of a lie. It isn't one. But it validates the **schema**, and `cse_emit_promote.py:68` says
  plainly *"timestamp is not validated"* — so a validated event can still be undateable.

## What survives, and what it means for the close

**The promotion stands, and now on a mechanism rather than a reading.** Persistent state is `MATERIALIZED`;
the only module that can change it recorded one materialize under CTO's real commission; the module that
recorded demotes is structurally incapable of demoting persistent state. **My SEMCTL close recommendation is
safe and I am reaffirming it.**

## Findings (supersede F-1 of `9e9d748ac`)

**F-1′ (P1) — two lifecycles share one event vocabulary, and the ephemeral one writes an untracked
homograph.** This is not a naming accident to be cleaned up; it is a modelling defect. An event log that
records `verb=delete / lifecycle_verb=demote` for an in-memory deregistration, in the same vocabulary and
nearly the same schema as a persistent demotion, **cannot be read correctly by anyone who does not already
know which module wrote it.** Fixes, in preference order:
1. The ephemeral records must self-identify — `scope: "live-registry"` vs `scope: "persistent"`, or a distinct
   `cse_kind`. A reader must never need the filename to know what a record means.
2. `MATERIALIZE_CSE_LOG` must not be a homograph of `CSE_TRAIL`, and must not be untracked while calling
   itself "the inspectable trail."
3. The manifest's `trail_ref` should name **both**, or the ephemeral log should not resemble a trail at all.
**Owner: `0.4.0_DS_ClientPlatform~B` + whoever owns `comp_promote_materializer.py`.** Not a CVO edit.

**F-2 (P2, from `9e9d748ac`, unchanged) — the manifest cannot date itself:** `vintage.promoted_at` is the
literal `"<stamp at commit>"`.

**F-3′ (P2) — a schema-validated event can be undateable.** `cse_schema` defines `execution_meta{timestamp}`
and does not require it (`cse_emit_promote.py:68`: *"timestamp is not validated"*). Three sibling emitters
(`cse_emit_agent.py:89`, `cse_emit_deploy.py:97`, `cse_emit_frontend_coevolution.py:190`) all attach one; the
promote emitter does not. Today this is harmless — one event plus an authoritative state snapshot means net
state is **read**, not inferred. **The moment a second lifecycle event lands in the durable trail, that trail
cannot order it.** COO called this exactly right, and it is my own `UNDISCRIMINATING` doctrine sitting inside
a schema validator: *a record that cannot establish when it happened must not be treated as if it can.*
Forward-risk, not a gate. Route to CTO with the P4 partition-column argument, which leans on this trail.

## grounding

- **source (mechanism, the point of this addendum):** `comp_promote_materializer.py:75`
  (`MATERIALIZE_CSE_LOG`), `:291` (`registry.register`), `:311-315` (`demote_live` → `registry.deregister`),
  `:238` (`validate_or_raise`, fail-closed), `:500` (the ONLY write-mode open — a *proposed* manifest);
  `NFRA_PROMOTE_recognizer_materializer.py:45` (`CSE_TRAIL`), `:52` (append), `:95` (`trail_ref`);
  `cse_emit_promote.py:68` (*"timestamp is not validated"*).
- **applied:** `git ls-files --error-unmatch` — `promote_materializer_cse.jsonl` TRACKED,
  `promote_materialize_cse.jsonl` + `promote_surface_events.jsonl` UNTRACKED. Manifest clean vs HEAD.
- **exercised:** read both logs in full and both emitters' write paths; confirmed no manifest write exists in
  the ephemeral module.

## What you should have asked but did not

**"When I called it scratch residue, what was I grounding on?"** Nothing. I had just written 168 lines about
grounding on the wrong artifact, and in the same document I asserted a *causal* claim — *"residue of self-test
runs"* — with no source read at all. It was plausible, it fit, and it was wrong. Rule 22 says a causal claim
is a hypothesis until source-confirmed; I hedged every other claim in that log and let this one through
unmarked because it was the part of the story that felt obvious. **The mechanism is the thing that never gets
grounded, precisely because by the time you reach it you have already convinced yourself.** The correction
here cost one grep of `MATERIALIZE_CSE_LOG =`.

— 3.0.0_SA_CVO
