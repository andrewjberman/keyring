# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0849Z – 0901Z

**archetype:** IMPLEMENT
**Projects:** D7_NOTIFY — TO-D (D-PROSE half)

> Timestamps read from `date -u` in a prior tool call.

## Summary

`D7_NOTIFY.TO-D_PROOF_OF_SPEC.json` **VALID rc=0, 4 rows, 0 violations — 3 PASS + 1
UNCOMPUTABLE-BY-CONSTRUCTION.** Three files: a new `teams_format.py`, two lines in `tools.py`, a
14-test property battery. **Built, not deployed.**

## 1 — The standard as properties, not prose advice

Seven properties asserted on the **output for arbitrary input**, not on one fixture looking tidy:
content never lost (order included) · ≤3 sentences per paragraph · exactly one blank line between
paragraphs · a sentence-ending URL alone on its line · the declared bound that a mid-sentence URL
stays inline · idempotent · all of it holding on degenerate input.

Four controls, because a property that cannot fail isn't one: the wall-of-text fixture is asserted to
**actually violate the cap before formatting**, its URL asserted to **start out buried**, a
content-losing formatter shown to fail the conservation law, and raising the cap to 99 shown to leave
the wall intact.

**The conservation law is deliberately ranked above the others.** A formatter that silently drops a
sentence is worse than the wall it replaces — the wall is legible, the loss is invisible.

## 2 — ⛔ My first formatter passed every property and produced worse prose

Hoisting every URL split *"Full detail is at `<url>` if you want the breakdown."* into three
paragraphs. **Content preserved, cap respected, URL alone on its line, idempotent — all green.**

**The properties cannot see fragmented prose.** Only printing the output and reading it can. Andrew's
complaint is a *readability* complaint, so a suite that measures structure and never reads the result
is measuring the wrong thing.

Narrowed the code to hoist only sentence-ending URLs, then **narrowed the property to match** — with
the cost pinned by its own test (`test_BOUND_a_url_genuinely_MID_SENTENCE_is_left_inline`) so the
weakening is explicit rather than a quiet relaxation. The battery correctly went **red** in between:
a suite reporting that the code no longer promises what it asserts is doing its job.

## 3 — Two more defects the tests caught before commit

The degenerate-input property **failed on `"\n\n\n"`** — whitespace-only input was returned unchanged
and violated the blank-line property. Fixed to return `""`.

And a **stale docstring survived my own narrowing by one edit**: after changing the code,
`format_for_teams`'s docstring still read *"hoist every URL onto its own line."* Caught on a re-read
of a function I'd written four minutes earlier — the same supersession class I've been finding in
other people's records all night.

## 4 — D-3 is honestly uncomputable

The criterion asks for clickability **verified against TO-C's measured renderer, not the
documentation**. TO-C measured that both send sites post `contentType: "text"`, under which content
isn't parsed as markup — **so no formatting change can make a hyperlink clickable.** That needs
`contentType: "html"`, which is D-HTML.

What this TO does instead is put a sentence-ending URL alone on its line: the best available form
under `text`, and **not a clickability claim**. Whether Teams auto-linkifies a bare URL is
**unmeasured** — observable only by posting, which TO-C was told not to do and did not.

**This row is the whole justification for the J2 sequencing.** Written before TO-C measured, the
standard would have specified link markup the renderer discards — and it would have passed review,
because it matches the documentation.

## 5 — The gate's WARN was visible to me, for once

`ruff` **BLOCKED** on `E741` (ambiguous variable name `l`, three comprehensions), so I read the whole
gate output instead of skimming to "clean" — **and there was the non-ASCII WARN naming `U+26D4` and
`U+26A0` at three lines, my fourth glyph incident this session.** When the gate passes, that same WARN
prints beneath `All checks passed!` and I have missed it every time. Both fixed; gate rc=0, 0 WARN
lines after.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find -i` (rung-2 check) | 6 hits / 42 files, **all unrelated** (ASGI wrapping, middleware) | no formatter to reuse — a new module is rung 7 correctly reached |
| python `ast` in-test | `{send_chat_message: True, send_channel_message: True}` | AST because "which function calls it" is unanswerable by text |
| `commit-gate.sh` | **rc=1** first (E741 ×3) → fixed → rc=0, 0 WARN | the ruff block is why the glyph WARN got read |
| property battery | caught `"\n\n\n"`; went red on a deliberate narrowing; **14 OK rc=0** final | the instrument earned its place |
| `proof-of-spec-check` positional | rc=0, rows=4, violations=0 | 3 PASS + 1 UBC |
| own-instance mutant | anchors: 4 rows, **3 PASS → rule firable**; then rc=1, violations=2, INVALID | CONTROLLED — the reachability anchor mattered here, since a 1-row UBC-only instance would make the rule unfirable |

## Blockers

**None I hold.** D-PROSE done; **D-HTML is next and is BUILD-ONLY** — `contentType: "html"` is a
gateway code change riding `safe-ec2-deploy`, and that box is the one every seat here reaches MCP
through (last bounce measured ~100s, public IP moved). **Under Rule 26 the apply is now mine**, on
Andrew's separate word, with the cost stated first. **F begins once D and E land.**

One decision still waiting on CTO~Z: **E-2's degradation** (refuse, built) vs a generic substitute.
Zero crons, nothing applied, nothing posted.
