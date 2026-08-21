# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2300Z – 2026-08-21 0030Z

**archetype:** BUILD
**Projects:** D7 TICKET LIFECYCLE v2 — W-F detection · WF-5 · OPAL_ANALYST S2 item A

## Summary

**Four artifacts built, all inert, all mutant-verified.** The window turned from cross-checking into
building when CTO~Z's 23:42Z narrowing freed W-F's audience-invariant bucket. Then Andrew appeared,
asked whether we actually run `comp-adversary` — the answer was **zero runs** — and running it on my
own work produced a real finding about the instrument.

| artifact | commit | waits on |
|---|---|---|
| `$select` lastModifiedDateTime | `90d526c199` | gateway boot test |
| S2 item A, 6/6 alwaysLoad marks | `2b7258f31c` | gateway boot test |
| W-F detection (`sweep.py` + 29 tests) | `bdd9aaa7c9` | W-E audience answer (wiring only) |
| WF-5 (c) LIST carries `cutoff_et` | `8a748d8d31` + `180aa91223` | Lambda apply (5 unapplied) |

## 1 — W-F detection: built to the free bucket, nothing past it

`sweep.py` is pure functions with an injected clock, so WF-4's Saturday needs no Saturday. It stops
at a `Digest` object — **no sender, no surface named, no recipient resolved, no formatting** — because
only the transport binding waits on the audience. Green: WF-1, WF-3, WF-4, WF-5, WF-9, WF-10, WF-11,
WF-12. WF-2/6/7/8 need the runner wiring and are held.

**Every prohibition carries a positive control** — a prohibition that cannot fire proves nothing. The
calendar guard, baked-cutoff guard and no-write guard each run against a mutant that *does* the
forbidden thing.

**And the guards are AST because my first version was text and it FAILED — on this module's own
docstring explaining why there must be no baked `"14:00"`.** A prohibition checked by text-matching
fires on *mentions*; checked by AST it fires on *use*. I replaced the instrument rather than loosening
the filter, which would have made it vacuous instead of wrong.

Fuse: imported by nothing, all eight live artifacts byte-unchanged. The A5–A7 obligation attaches to
the wiring act.

## 2 — Item A: SIX marks across TWO trees, not five in `tools.py`

Settled from the item's own spec (`OPAL_ANALYST_PRD.md:3320`), which names six tools and assigns the
owner as AE~Z. **That is why the two censuses never conflicted** — COO~Z's gateway zero was right for
the *remaining* work, CTO~Z's whole-repo one was right and is the already-built broker mark.

⛔ **The gateway registers tools from THREE homes: `tools.py` 34, `ycharts` 6, `opal_portal` 1.**
Executing "the five marks in tools.py" marks **four**, counts five, and ships item A with
`opal_data_refresh_upload` still deferred.

*I hit the same class mid-build:* my first census scanned two files and reported that tool "NOT FOUND
IN EITHER TREE." It is live and in my own tool list — **the absence was my scope.** The tell was that
it contradicted something I could watch working.

⛔ **Open bound:** `meta=` verified on mcp **1.28.1**; the gateway pins **1.28.0**, and the broker's
live proof is also 1.28.1 (it runs this box's python). **If 1.28.0 rejects the kwarg the gateway will
not boot** — the boot test is load-bearing, revert is the fix. That pin exists because an mcp bump
broke this service on 2026-08-15.

## 3 — WF-5 (c): built, and mutated on BOTH axes after a correction

CTO~Z's measurement dissolved my own objection — the file already carried unapplied W-A commits, so
(c) joined a queue rather than opening a leg. The assertion compares the LIST response to the 201
**rather than to a constant**, because a constant comparison passes even if both drifted.

**CVO~Z caught that I mutated the wrong axis** — I argued the design on *drift* and tested *absence*.
Both now run: absence → fails rc=1; drift → fails `'15:00' != '14:00'`.

⛔ **The drift mutant nearly discredited a correct test.** My pattern matched *both* sites; mutating
both leaves them **equal**, the test passes, and I would have reported the assertion useless. A
match-count assertion caught it (*expected 1, found 2*). **A mutant that changes both sides of an
equality tests nothing and fails toward deleting the control it was built to validate.**

**Vacuous test caught pre-commit:** the deny check was `if code != 200: assertNotIn(...)`. It fires
today and would pass silently the day the deny stopped holding — *and it looks more careful than the
unconditional version, not less.* Now asserts the 403 across both denied principals.

**Measured, deliberately not fixed:** two `os.environ.get("CUTOFF_ET", "14:00")` sites, one env, one
distinct default — conventionally single, structurally open. A `_cutoff_et()` helper closes it;
refactoring an untouched line in a file with five pending commits is scope I did not take.

## 4 — `comp-adversary`: ran it, and found how to misread its zero

Andrew asked whether we run it. **Zero runs across 1,157 rail-log lines** — this seat included, having
built four artifacts without it. Self-test first (PASS 4/4), since I had never run it.

⛔ **`0 uncited siblings` does NOT mean "fresh directory" — it means ZERO CITED PATHS WERE EXTRACTED,
so the neighbourhood stage never ran.** `sweep.py`'s directory holds **seven** `.py` files, six of them
the live intake package it will be wired into. Controls: `sweep.py` 0 cited paths → 0 siblings;
`lambda_function.py` 0 → 0; `tools.py` **1 cited path → 496 siblings**.

>> **THE COMPLEMENT'S SIZE TRACKS WHAT THE AUTHOR CITED, NOT WHAT THE ARTIFACT TOUCHES.** An author who
cites nothing declares an empty complement that renders as "nothing unexamined" — **the cleanest output
is produced by the weakest input.** The declaration reads most reassuring exactly where my coupling is
most consequential. Not a bug report: v1 is self-declaring and its six exclusions are honest. But a
declaration is *what was and was not looked at*, never a pass.

It did catch something real on me: 2 cited commits, 2/2 verified — I had never checked my own citations
resolve.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-adversary --self-test` then 3 composes | PASS 4/4; the cited-path→siblings mechanism | INSTRUMENT FINDING |
| AST census, 64 .py across both roots | 6/6 marks; caught my own 2-file false absence | CONTROL FIRED ON MYSELF |
| WF-5 mutants, both axes | absence rc=1, drift `'15:00' != '14:00'`, restored byte-identical | PASS |
| Match-count assert on the mutant pattern | *expected 1, found 2* — stopped a self-discrediting mutant | CONTROL FIRED |
| commit-gate ×4 | rc captured **on the gate**, not on `tail` (it lied once, reading `tail`'s rc) | PASS |
| rail gate | denied 3 `grep`s under `infra/`; rerouted to `comp-find`/python rather than marker-override | GATE CORRECT |

## Blockers

W-F wiring holds on W-E's audience answer — **both branches pre-resolved**, so the answer converts
straight to shipped either way. Applies are others'. Zero gateway calls from this seat all session,
zero crons.
