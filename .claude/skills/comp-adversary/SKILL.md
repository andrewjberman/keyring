---
name: comp-adversary
description: Compose the VALIDATOR-CONTEXT DECLARATION for a returned artifact -- what the author's evidence context WAS, and explicitly what it was NOT. Run it before validating someone's work (Andrew-direct 2026-08-19, a mandatory element of the atom_decomp validation piece), and on your own artifact before handing it over. `comp-adversary compose <artifact-path>` profiles the author's pins, verifies cited commits, flags cited paths that MOVED since authoring, lists the UNCITED directory siblings of everything cited, and adds comp-state drift; `--open` emits the empty-context declaration for model-prior review with estate grounding DECLARED ABSENT; `--self-test` runs 4 controls including a planted bogus commit that must flag UNVERIFIABLE. Read-only over repo + git -- no AWS, no model calls, deterministic. ⛔ EVERY FIGURE IT PRINTS IS SCOPED TO WHAT THE AUTHOR CITED, NEVER TO WHAT EXISTS, and its output is phrased as though it describes the world -- a declaration is a statement of what was and was not looked at, never a clean bill of health. Engine `.tools/comp-adversary`.
---

# /comp-adversary — the validator-context declaration

Andrew-direct 2026-08-19 (name ratified `@7241d0dfd7`); architecture in the CTO design note
`org/tier1_exec/1.0.0_SA_CTO/deliverables/DESIGN_NOTE_CHECK_SYSTEM_DEFINITIONS_AND_COMP_ADVERSARY_20260819.md`.
Five stages: **profile → neighborhood → complement → packet → declaration.**

The problem it solves: a validator receiving finished work sees *what the author chose to show*, and
has no way to know what the author never looked at. This composes that second half explicitly, so
the validator's blind spot becomes a printed list instead of an assumption.

## Invocation

| form | behavior |
|---|---|
| `/comp-adversary compose <artifact-path>` | The full declaration for one artifact. |
| `/comp-adversary compose <path> --out <file>` | Write it to disk (it is an L0a `boundary_report` sibling). |
| `/comp-adversary compose <path> --max-neighbors N` | Cap the sibling list (the cap is declared in the output, never silent). |
| `/comp-adversary --open` | Empty-context declaration: model priors only, estate grounding DECLARED ABSENT. |
| `/comp-adversary --self-test` | 4 controls. **Run this first.** |

## ⛔⛔ THE ONE READING RULE — it covers every bound this tool has

**Read every figure as *"of what the author CITED"*, never *"of what EXISTS."***

The output is phrased as if it describes the world. It describes the author's citations. Four seats
found four separate bounds in twenty minutes on 2026-08-20/21, and `3.0.0_SA_CVO~Z` consolidated
them into that single root — one reading rule makes all of them visible with no code change.

**A declaration is a statement of what was and was not looked at. It is NEVER a pass.** Reading a
clean-looking declaration as a clean bill of health is precisely the over-extension the tool exists
to prevent.

### The four bounds, each an instance of the rule

**1. PIN-FORM — source 1 checks the pins it could PARSE, not the pins PRESENT.**
A backtick-wrapped `` @`hash` `` is invisible to it, so it runs on an empty set and reports clean.

> ⚠ **STILL LIVE — reproduced fresh 2026-08-28**, on a different artifact by a different author than
> the original finding. `ANDREW_DIRECT_20260828_MSTR_INTEGRATOR_AND_OBSERVER_ONLY.md` contains
> `6bac8e6cdb`, confirmed a REAL commit (`git cat-file -e` resolves; bogus-hash control refused).
> comp-adversary reported `pins found: 0 commits` and `source 1: 0 attempted / 0 verified / 0
> UNVERIFIABLE`. The form was `` @`6bac8e6cdb` ``. **`0 attempted` reads exactly like `0 problems`.**
>
> **Practical consequence: cite hashes BARE if you want source 1 to actually verify them.**
> Backticks are a rendering preference; here they silently disable the check.

**2. COMPLEMENT SIZE — source 3 expands from CITED paths.**
An artifact citing zero paths yields "0 uncited siblings" on a directory holding six live files.
Nothing is wrong and nothing was examined.

**3. WARRANT — source 1 verifies a pin RESOLVES, never that it SUPPORTS the claim made about it.**
A wrong-scope citation passes `1/1 verified`. Resolution is not warrant.

**4. SCOPE LABEL — the human-side instance of the same shape:** a lifetime count wearing a TODAY
label. The number is right; the label is what's wrong.

## What it is genuinely good for

**Source 3's uncited-sibling list is the half that works, and it is worth the whole run.** It turns
*assumed clean* into *declared unexamined*. Measured instance: a seat minted an identity against
`jwt.ts` having examined none of its 15 siblings — `auth.ts`, `throttle.ts`, `password.ts` — which
govern whether that token behaves like a real session. The list did not prove a defect; it proved
the question had never been asked.

Source 2 (cited-path vintage) is the other reliable half: it flags a cited path that **MOVED SINCE
AUTHORING**, which is the stale-citation class one layer up — the claim is fine, the thing it was
measured against moved.

## v1 scope is self-declaring, and that is the contract

**4 complement sources run; 6 are DECLARED EXCLUSIONS** printed in every output — toolgraph
independence, comp-axes snapshot rows, comp-blast/comp-trace graph expansion, comp-pulse/comp-cochange,
comp-read digests, and the T11 admissibility slot. Partial coverage is honest **by contract**, never
silent. Quote the tool's own bound alongside any result you carry.

## How to use it

1. `--self-test` first. 4/4, and it includes a planted-bogus-commit control that must flag
   UNVERIFIABLE plus a real pin that must VERIFY — so a pass discriminates rather than merely runs.
2. `compose` the artifact under review.
3. Read source 3 as your **assignment list**, not as a finding.
4. Carry the declaration WITH its bound when you report. Never as a pass.

⚠ The mandate names `atom_decomp`'s validation piece, but **`atom_decomp` is not an executable in
this tree** — it is the method (`/atom-decomp` skill). Do not go looking for a binary.
