---
name: comp-adversary
description: Compose the VALIDATOR-CONTEXT DECLARATION for a returned artifact -- what the author's evidence context WAS, and explicitly what it was NOT. Run it before validating someone's work (Andrew-direct 2026-08-19, a mandatory element of the atom_decomp validation piece), and on your own artifact before handing it over. `comp-adversary compose <artifact-path>` profiles the author's pins, verifies cited commits, flags cited paths that MOVED since authoring, lists the UNCITED directory siblings of everything cited, adds comp-state drift, and -- since stage 4 landed 2026-08-31 -- hands the validator actual `comp-read` DIGESTS of a declared-salience selection of that complement, not just its paths; `--open` emits the empty-context declaration for model-prior review with estate grounding DECLARED ABSENT; `--self-test` runs 5 controls including a planted bogus commit that must flag UNVERIFIABLE. Read-only over repo + git -- no AWS, no model calls, deterministic. ⛔ EVERY FIGURE IT PRINTS IS SCOPED TO WHAT THE AUTHOR CITED, NEVER TO WHAT EXISTS, and its output is phrased as though it describes the world -- a declaration is a statement of what was and was not looked at, never a clean bill of health. Engine `.tools/comp-adversary`.
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
| `/comp-adversary compose <path> --digest-budget N` | How many complement files to DIGEST (default 12). |
| `/comp-adversary compose <path> --digest-bytes N` | Per-file digest cap (default 2400; truncation is printed, never silent). |
| `/comp-adversary compose <path> --no-packet` | Pointers only — skips stage 4. The skip is DECLARED in the output. |
| `/comp-adversary --open` | Empty-context declaration: model priors only, estate grounding DECLARED ABSENT. |
| `/comp-adversary --self-test` | 5 controls. **Run this first.** |

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
>
> **STILL UNFIXED as of 2026-08-31, and deliberately not fixed by the stage-4 build.** `COMMIT_RE`
> at `.tools/comp-adversary:49` is owned by `0.8.0_AE_CloudComp` (design note s.4 routes it there;
> findings 90276–90279 are queued in that inbox). `3.0.0_SA_CVO~C` built stage 4 without touching
> `:49` so the two lanes do not collide in one file. Recommended predicate when that seat picks it
> up: warn when `commits_found == 0 AND raw_hex_runs_present > 0` — the current ZERO-PIN banner
> keys on profile-emptiness, so it stays silent on the 0-commit/1-path case, which is the half that
> looks well-evidenced.

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

## Stage 4 — THE PACKET (landed 2026-08-31, `3.0.0_SA_CVO~C`)

Source 3 tells the validator *which* files the author never opened. **Source 5 lets them actually
read some of them** — real `comp-read` digests, inline, in the declaration.

**It is a SELECTION, not a survey, and that is the whole design problem.** Measured on the D2
proof-of-spec: the complement is **542 files**, and a digest runs 2.4–10.4 KB / 0.3–0.6 s each.
Digesting all of them is ~3 MB and ~240 s — a context bomb *and* a breach of the design note's own
71.5 s constraint. So the packet spends a **budget** against a declared salience ranking:

| class | meaning | why it ranks here |
|---|---|---|
| **S1 POSTDATES** | changed *after* the artifact's vintage | the author could not have read what it says now |
| **S2 KIN** | shares a filename stem with a CITED path | the sibling-member / wrong-version class |
| **S3 DENSE** | in a directory the author cited 2+ times | demonstrably their working area — an omission there is a choice |
| **S4 PERIPHERAL** | sibling of a directory cited once | distance, not choice |

First-match-wins, so the classes **partition** the complement (MECE, Rule 24) — the output's
`class census:` line sums to the domain, and the acceptance battery asserts that it does.

⛔ **READ `selected: N of M` AS THE WHOLE CLAIM.** A typical run digests **12 of 542**. A file's
absence from the packet is a **BUDGET fact, never an assessment that it did not matter** — the tool
prints that sentence itself so it cannot be dropped in the retelling. Raise `--digest-budget` when
the question warrants it; the runtime scales linearly and the 71.5 s order is the bar.

**What one remedy does NOT move** (state coherence): re-running at a later vintage moves S1 only;
the author citing more paths moves S2/S3 only; raising the budget moves what is *selected* and no
file's *class*.

## Scope is self-declaring, and that is the contract

**5 complement sources run; 5 are DECLARED EXCLUSIONS** printed in every output — toolgraph
independence, comp-axes snapshot rows, comp-blast/comp-trace graph expansion, comp-pulse/comp-cochange,
and the T11 admissibility slot. (The sixth, "comp-read digests — the packet lists POINTERS", was
**retired** when stage 4 landed.) Partial coverage is honest **by contract**, never silent. Quote the
tool's own bound alongside any result you carry.

## How to use it

1. `--self-test` first. 5/5 — a planted-bogus-commit control that must flag UNVERIFIABLE, a real pin
   that must VERIFY, and control 5, which asserts the packet carries comp-read's own panels. Control
   5 was **run RED against the pre-stage-4 binary** (0 panels) before it was written green, so a pass
   discriminates rather than merely runs.
2. `compose` the artifact under review.
3. Read source 3 as your **assignment list**, not as a finding — and source 5 as the part of that
   list someone already pulled for you.
4. Carry the declaration WITH its bound when you report. Never as a pass.

## Acceptance battery

`python .tools/tests/test_comp_adversary_stage4_packet.py` — 7 legs (digest content, denominator,
exclusions 6→5, `--open` unchanged, a planted no-digest **mutant**, a zero-cited-path **negative
control**, and the MECE partition). The mutant is built from the *shipped* bytes at run time rather
than a pinned commit, so it cannot go stale into measuring a ghost.
`python .tools/tests/test_comp_adversary_path_truncation.py` — the 4-leg PATH_RE census, unchanged.

⚠ The mandate names `atom_decomp`'s validation piece, but **`atom_decomp` is not an executable in
this tree** — it is the method (`/atom-decomp` skill). Do not go looking for a binary.
