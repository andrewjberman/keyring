# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-21 0830Z – 0900Z

**archetype:** IMPLEMENT
**Projects:** D7_NOTIFY — TO-A (the W-E re-cut)

## Summary

`D7_NOTIFY.TO-A_PROOF_OF_SPEC.json` **VALID rc=0, 8 rows, 0 violations, 8/8 PASS.** Three files:
the handler, a 27-test battery, the Terraform. **Built, not applied** — no plan, no apply, no send.

**A/B/C are now all in.** C landed `81e135c92e`, B landed `38518ed924`, A lands here.

## 1 — The seam, which is what made this more than a field release

`resolve_recipients(firm) -> [addresses]`, and `notify_dl` takes the item's firm and calls it. The
config is a firm-keyed map holding one `"*"` row today, so **a per-firm split is adding rows, not
touching the send path**. Andrew declared that ahead of need; the shape I shipped at `4d5a92f4d7` —
`TICKET_DL` read at module scope, consumed inline at the send site — is exactly what the TO forbids
by name, and I surfaced it against my own accepted stage before this TO existed.

A-2 is asserted **by AST**, not by reading: `TICKET_DL` absent from `notify_dl`'s Name nodes,
`resolve_recipients` present as both Name and Call, with a positive control on a synthetic mutant
module that *does* read a module-scope address. And the seam is exercised **as a seam** — same code
path, two maps, two different recipient sets.

## 2 — The three refusal cells, and the reachability control underneath them

Unconfigured → refuse. Unknown firm with a `"*"` row → the default (today every firm — the normal
path, not an edge). Rows present, no match, no default → refuse. Empty resolved set → refuse rather
than send to nobody.

**A-3b is the load-bearing half**, and it exists because COO~Z found the gap in criteria the gate had
authored fifteen minutes earlier: with membership deferred, **a refusal *is* the acceptance surface**,
and a refusal test passes identically whether the pipe ran and found nothing or was never reached.
A spy proves `resolve_recipients` was **entered** with the item's firm in the refusing case, a
positive control on the **same call site** shows the identical path sends when configured, and a
third test models the never-reached pipe to show what the spy discriminates that `assertRaises`
cannot.

## 3 — ⛔ I deleted the two lines the criterion protects, and my own assertion caught it

A-5 names `L132`/`L135` byte-unchanged — WE-4's content-scope limb, preserved by the ruling that
released `description`. **My module-region rewrite replaced the whole comment block and took both
with it.**

I had not done a blanket keyword pass. I replaced a block and wrote new prose, and **the effect was
identical to the thing forbidden.** Recovered byte-for-byte from HEAD; re-verified `IDENTICAL=True`.

**A rewrite deletes as surely as a sweep** — which is why A-5 asserts on the bytes and not on the
intent, and why the assertion written *before* the edit is what found it.

## 4 — Third glyph of the session

Another `U+26D4` into a file that runs on AWS, caught by the byte-level scan. The commit-gate's
non-ASCII lint would have named the codepoint and the line — it is scoped to `infra/**` — but it is
WARN-only and returns 0, so its warning prints beneath `All checks passed!`. Stripped before the gate
ran. Recorded in-band and not chased, per the standing instruction.

## 5 — Subject and CTA, resolved by measurement rather than choice

Subject `[<FIRM>] <requester subject>`, firm first so it sorts. CTA: a **bare URL alone on its own
line**, asserted as a whole line of the body rather than as a substring, with the line above it
ending in `:`.

The target is the **list page**, and the test asserts the body does **not** carry a per-ticket URL —
because TO-B measured that no per-ticket route exists. The conditional ruling resolved to its second
branch by fact.

⚠ The two surfaces stay unharmonised deliberately: a bare URL autolinks in mail and does **not**
necessarily in Teams. Andrew's *"properly linked to be clickable"* was said about Teams.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| python `ast` in-test (A-2) | `TICKET_DL` absent, `resolve_recipients` present, + positive control | AST because the forbidden thing is a **read at a call site**, which text cannot tell from a mention |
| `terraform fmt` / `validate` | rc=0 / rc=0, no plan, no apply | v1.15.8 on PATH; `.tools/terraform.exe` still absent on this box |
| `commit-gate.sh` | rc=0 clean, 2 files | run **after** the strip; its non-ASCII lint is WARN-only under a clean summary |
| `test_we_dl_notice.py` | **27 OK rc=0**, 4 mutants firing inside it | each mutant restored in a `finally` |
| `test_authz_matrix.py` | 15 OK rc=0 | A-4 no-regression |
| `pytest integrations/ticketing/intake/` | 42 passed + 25 subtests rc=0 | runner untouched |
| A-5 byte diff vs `git show HEAD:` | `IDENTICAL=True` ×2 | **caught my own deletion** |
| `proof-of-spec-check` positional, 8 ids | rc=0, rows=8, violations=0 | eight, not seven |
| own-instance mutant, anchor-asserted | rc=1, violations=2, INVALID naming A-1 | CONTROLLED |

## Blockers

**None I hold.** A/B/C complete. What remains is others': the DL membership (deferred by Andrew), the
**laptop apply** — which must be requested as carrying W-A's queue plus `4d5a92f4d7` plus this, not
as a single change — and D/E/F on their activation conditions. **WE-2/WE-3 stay
UNCOMPUTABLE-BY-CONSTRUCTION**: deferring the list defers the proof, never the build, and pipe
completion must not be read as their discharge. The W-F import edge remains unwritten. Zero crons,
zero gateway calls, nothing applied.
