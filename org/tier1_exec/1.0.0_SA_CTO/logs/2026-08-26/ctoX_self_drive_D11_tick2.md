# /self-drive D11 — ticks 1-2

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · armed 2026-08-26T20:22Z on Andrew-direct `/self-drive D11`

---

## SCOPE (re-resolved each tick)

```
D11 "Substrate Analysis (NEW; qualify the ladder before anything is built on it)"
  device LAPTOP (guard PASS -- register LAPTOP == agentbus-sqs resolver 'laptop')
  1 project: NFRA_SUBSTRATECARDING  status=active  dep_stage=EXECUTING
  denominator: 1 of 12 live directives
  claim scan (0.3, PRD-path form only, both prds[] shapes handled):
      1 claim over 334 project JSONs scanned; already a member -> deduped, not an error
```

## TICK 1 — 2026-08-26T20:22Z

**Open calls in scope: ZERO.** The D12 / cover-vs-partition / identity-grain cards belong to
`NFRA_C3MATERIALIZE`, which is **not a D11 member** — out of scope for this loop, held at Andrew from
`/open-calls`. **No empty pitch sent** (§1) and no in-scope call manufactured to have something to
send.

**Verdicts received: 0** (nothing pitched).

**Driver acts (own lane only — no TO, no dispatch, no apply):**

1. **`dep_stage` REGISTERED → EXECUTING** on `NFRA_SUBSTRATECARDING`, with the residuals named in
   `blocking`. My record, my drift: wave 1 was delivered while the project still declared itself
   REGISTERED.
2. **ROUTED to `2.0.0_SA_COO~X`** (msg 73xxx): `TO-W1-DTX` and `TO-W1-COX` faces read
   `<status>pending</status>` while both were ACCEPTED. **The register's `open_tos: 2` was CORRECT** —
   it reads the faces, and two had not moved. Acceptance travelled by message; the record did not
   follow. Routed rather than edited: the TO faces are the issuer's record.

**Completion test:** NOT DONE — 0 of 1 complete. REACHABLE 1 / UNREACHABLE 0.

## TICK 2 — 2026-08-26T20:51Z

**Tick 1's route CLOSED, measured:** `open_tos` **2 → 0**; all four W1 faces now read `complete` with
their verifier and acceptance citations inline. *A driver act with a measured result rather than a
sent message.*

**Open calls in scope: 1 ADJUDICABLE, 0 RESERVED.** Pitched to `3.0.0_SA_CVO` (msg 73636), cc
`3.0.0_SA_CVO~X` (73637) and `2.0.0_SA_COO~X` (73638).

> **Is wave 2 correctly NARROWED to the 33 `composes`-subjects, scoped to methodology +
> declared_opinions only, with the 10 `projection_of`-only stores DEFERRED into `known_unsearched`?**

**Created by** Andrew at this terminal ~20:3xZ, verbatim: *"I would prefer to do (b), yes, but I dont
like the idea of leaving stones unturned if there is any dependency at all upon them."* **A
preference, not a ruling — and it turned the dependency question from rhetorical into measurable.**

**The measurement, from `SC-m-4_wave2_derivation.json` @`d94e825bf2`:**

```
  33 of 43   via COMPOSES          the layer's METHODOLOGY named it
                                   = the CURRENT materializer for that layer USES it
  10 of 43   via PROJECTION_OF only a store the layer derives FROM

  and the 33 span EVERY layer a canonical materializer is wanted for:
     C3.i 6 · C2 6 · D2 5 · D3 5 · comp-similar 5 · C1 4 · D1 4 · C0 2 (+2 shared)
```

Candidate #1 is `ANCHOR_CATALOG + HUB_TYPES`, named by `C3.i-as-built` via `composes` — **the
seven-type roster that DEFINES C3.i today.** A canonical C3 materializer cannot be written without
knowing what the current one bakes in, and that is exactly where the suspected *"deprecated
opinionation, filtering, questionable definitions"* lives.

**REC: (a) narrow.** Skipping wave 2 leaves 33 load-bearing stones unturned; a FULL wave 2 is also
wrong, because the 33 do not need seven-question cards — **for a materializer exactly one field
matters, `generation.declared_opinions`**, since the semantic-defect axis has no instrument and
declaring the opinions is the only thing that makes them reviewable.

⚠ **STATED WEAKNESS IN MY OWN REC:** the `composes` / `projection_of` split is `2.0.0_SA_COO~X`'s
**field semantics, not a measured property of the subjects.** A lane could have placed a genuine
generator in `projection_of`, and the narrowing would then drop a real dependency. **I have not
audited the 10 for that**, and asked for the guard to be named in the verdict rather than assumed.

**Verdicts received: 0** — pitched this tick, none returned yet. **The loop does not proceed on an
absent verdict.**

**Completion test:** **NOT DONE — 0 of 1 project complete** (`NFRA_SUBSTRATECARDING: active`).
REACHABLE 1 / UNREACHABLE 0 — wave 2 is derivable and the input exists, so nothing is structurally
stuck.

## CARRIED — NOT part of D11 scope, listed so they are not lost

At Andrew from `/open-calls` (all `NFRA_C3MATERIALIZE` or doctrine, none D11 members): mint **D12** ·
**cover vs partition** · **identity grain** · two **CLAUDE.md** precision fixes ·
`2.0.0_SA_COO~X`'s **vantage-vs-world** doctrine candidate.

⚠ **THE CARRIER CLAUSE IS NOT LANDED.** §5 requires an `org/XXX.md` Step 1b-F clause so a successor
re-arms; that is a **law-file edit**, and Andrew's standing instruction to this seat is that
guiding-doc content does not move ahead of his word. **The cron `29b44790` is session-only, so this
loop dies with the session and no successor will re-arm it.** Stated as a known gap, not silently
carried.

## Compiler Tools

`.tools/directives-check.py --json` (scope resolution + `open_tos`, both ticks) ·
`bash .tools/agentbus-sqs.sh device` (0.2 device guard) · `.tools/check-inbox` (verdict sweep) ·
`.tools/safe-commit.sh` (this log). `comp-to` produced no D11 rows and the TO faces were read
directly instead — recorded because a tool returning nothing is not the same as a tool answering zero.

**state: ARMED** · next tick :17
