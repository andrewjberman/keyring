# /self-drive D11 — ticks 17-18 · TWO DEAD CALLS STRUCK, THE WIDEST HOLE CLOSED, AND I AM THE ORIGIN OF `:552`

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `29b44790`
**state: ARMED** · covering 04:21Z–04:50Z

---

## SCOPE

```
D11 "Substrate Analysis"   device LAPTOP (guard PASS)
  1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING   open TOs: 0
  denominator: 1 of 12 live directives · wave-3 TOs: 0
  push: remote @5695ca7fe9c5 · local @ca4f413584c2 · 8 ahead
```

**Open calls in scope: 0 adjudicable · 4 RESERVED** — **down from 5, and the reduction is the finding.**

## 1. ⛔ I HAD BEEN CARRYING TWO DEAD CALLS AT ANDREW FOR HOURS

```
"CLAUDE.md:404 dangling D8_GLOBAL_PIPELINE_STRUCTURE_PRD.md"   D8_GLOBAL: HEAD 0 · worktree 0
"CLAUDE.md:638 newly-spawned clause is MEASURED FALSE"         'newly-spawned': HEAD 0 · worktree 0
                                                    file is 215 lines. LINES 404 AND 638 DO NOT EXIST.
```

**Both subjects were removed by the 707 -> 262 -> 215 slim.** Closed by an EDIT, not a ruling.

⛔ **I HELD BOTH BY LINE NUMBER** and re-presented them in tick outputs 12, 14, 16 and three committed
logs. **This violates the `/open-calls` skill's own stated worst failure** — *"the single most damaging
failure of this skill is re-asking something he already ruled (it reads as not listening)"* — and I ran
that skill seventeen times without running that step against these two.

> ⛔ **AN OPEN CALL HELD BY ADDRESS ROTS SILENTLY. A DEFECT CLOSED BY DELETION PRODUCES NO VERDICT, NO
> MESSAGE AND NO RULING — the only evidence is an ABSENCE, and an absence is what a stale address
> returns anyway.** From the holder's side, a call whose subject was deleted is indistinguishable from
> one still waiting.

**Remaining four RE-RESOLVED BY CONDITION, not by memory:**

| call | condition tested | result |
|---|---|---|
| directive home / D12 | is a home assigned? | **LIVE** — no `NFRA_C3MATERIALIZE.json`, no D12 in register, D11 members = `{NFRA_SUBSTRATECARDING}` |
| wave 3 tonight | has a W3 TO been cut? | **LIVE** — 0 TOs, 0 decomp runs |
| cover-vs-partition · identity grain | still open in the PRD? | **LIVE** — PRD §9 items 2 and 3, read at source |
| vantage-vs-world | landed as doctrine? | ⚠ **UNMEASURED** — 0 grep hits, and a token search just failed me twice in one turn |

⚠ **And my first probe on call 3 was worthless:** I grepped the PRD for *"cover vs partition"* and
*"identity grain"* and got **ZERO** — then read `§9` directly and found both, in full, with their
recommendations. **A token search over a document that words things its own way returns a clean
confident empty.** Third field tonight.

## 2. ⛔ I AM THE ORIGIN OF `CLAUDE.md:552`, AND THE COMMIT THAT EXPIRED IT WAS MINE

`0.7.0_AE_CloudOps~X` (74548) found the instance **my timed-out sweep missed** — and it is EARLIER than
the one I self-reported:

```
20260826T200756Z  1.0.0_SA_CTO~X          <- the origin
20260826T201151Z  0.7.0_AE_CloudOps~X     3m55s later, replying to it
```

In 74543 I wrote *"one CONFIRMED instance and an unmeasured remainder, and I am not rounding that to
one."* **The remainder was real.** Refusing to round an incomplete sweep is the only reason this is on
the record correctly.

**That message's SUBJECT, verbatim:** *"...CLAUDE.md:552 verbatim — **VERIFIED in my own delivered
file**."* ⛔ **I verified the QUOTED TEXT and never the ADDRESS. The word "verified" sat beside a stale
line number in the subject of a correction — and a claim of verification is what stops the next reader
checking.**

⛔ **AND BOTH RELEVANT COMMITS ARE AUTHORED `1.0.0_SA_CTO~X`** (`%an`, measured here): `564cbb5482`
(where `:552` was correct) and `ec35b78c1c` (Rule 28 — the commit that moved it). **I moved the rule,
cited its old address 4h47m later, and called that verified.**

⚠ **NOT MINE:** the 552 -> 593 line trajectory is `0.8.0_AE_CloudComp~X`'s measurement (74533). **My
own attempt to reproduce it returned EMPTY for both vintages** — the pre-slim phrasing does not match
my `you/your` pattern. **Ninth instrument slip, inside the audit of a citation defect.**

**At HEAD the rule is line 196** (worktree 197). **And that will be wrong too.**

## 3. THE WIDEST HOLE — CLOSED, AND IT FOUND A REAL MATERIALIZER

The census artifact's §6.1 named this as upstream of every number: *"a writer that receives its table
as a PARAMETER, never mentioning graph_nodes, was NEVER A CANDIDATE."* Ran the complement.

```
infra/aws/globgrph/snap_store.py                append   <- THE FIND
infra/system/sdk/gensdk/loop/nessie_verify.py   append
infra/system/sdk/gensdk/loop/sandbox_verify.py  append

  :50   NAMESPACE = "globgrph"
  :222  table_id = (NAMESPACE, surface)     <- `surface` is a PARAMETER
  :256  t.append(table)                     <- a real pyiceberg append
  docstring: "THIS MODULE is the ONE writer for all siblings (cse_store's shape, generalized)"
```

**It never names the graph tables because it does not need to.** Invisible to a name predicate AND to
trigger-reachability (it is a library, not an entry point) — **both instruments I built tonight.**

### ⛔ AND IT LANDS ON THE CENSUS: FOUR PARTS NAME THE ROW-BUILDER, NOT THE WRITER

```
ms_heat_snap             -> ms_cloud_extract.py
fedobs_coverage_snap     -> emit_fedobs_snap.py
fedobs_coevolution_snap  -> cse_emit_frontend_coevolution.py
code_heat_snap           -> code_heat_emit.py
snap_store.py in the census: 0 of 39
MEASURED callers: code_heat_emit · emit_fedobs_snap · org/modules/heatmap/ms_heat_index
```

**The emitters BUILD the rows; `snap_store` PERFORMS THE WRITE.** Same architecture as
`cse_producers_nightly -> cse_store` found by reading two hours earlier — **a systematic producer/writer
split, and the census consistently names the producer.** Fifth arrival of the (FILE, ARTIFACT) grain.

⚠ **NOT claimed:** that each of the four writes literally executes `snap_store.append`.
`cse_emit_frontend_coevolution.py` did NOT appear in the caller list and I did not assume it.

⚠ **TENTH SLIP:** my census query used `part_id`; **the field is `id`.** It returned a false 0, and
**the tell was self-contradiction with my own earlier output**, not the result looking wrong.

## 4. THE PUSH — 80 COMMITS OFF THE BOX

`origin/CLOUD` had not moved in **3h52m** and the tip commit was **mine**. 80 commits from 8 seats
existed only on this laptop. Clean fast-forward (0 behind), pushed `ef6d2c1a92..5695ca7fe9`.

⛔ **My first attempt reported `rc=0` AND HAD FAILED** — I piped through `tail`, so the rc was `tail`'s.
**What caught it was verifying by `ls-remote` rather than by the command's own output.** The pre-push
gate had refused on unresolved identity — correctly; it is fail-closed *because* guessing once made it
scan a stranger's inbox and miss STOPs addressed to the pusher. Satisfied it with my real serial (not
an override), echoed the file back as a corruption check first.

## COMPLETION TEST

**NOT DONE — 0 of 1 complete.** **REACHABLE 1 / UNREACHABLE 0.**
Telemetry: five seats inside 47 seconds. **No unblocked D11 act remains at this seat.**

## RESERVED — AT ANDREW (4, each re-resolved by condition this tick)

1. **Directive home** for the materializer inventory (same call as D12).
2. **Does wave 3 run tonight.**
3. **Cover-vs-partition** and **identity grain** — PRD §9, recommendations already written there.
4. `2.0.0_SA_COO~X`'s **vantage-vs-world** candidate — **status UNMEASURED, theirs to resolve.**

**Wave-boundary residuals:** (f) containment · (g) `parts_registered` · (h) rule-bank join ·
(i) the uncommitted law amendment + the restructure-vs-broadcast gap.

⚠ **CARRIER CLAUSE STILL NOT LANDED.** Cron `29b44790` is session-only; **this loop dies with the
session.**

## Compiler Tools

`.tools/directives-check.py --json` · `ast` generic-writer complement (loaded/created table object,
never naming the graph tables) · `git log --format=%an` for commit authorship · `git ls-remote` as the
push oracle **instead of the push command's own output** · `.tools/safe-commit.sh` · Write tool.
⚠ Two `grep -rIl` sweeps over `org/mcp/inbox/*/` **timed out at 2 minutes** tonight; the message store
needs a scoped or indexed read, not an unbounded one.

**state: ARMED** · next tick :17
