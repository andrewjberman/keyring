# /self-drive tick 3 -- `MDPF_TAXSMA`, `NFRA_MCPINDEX` -- **four rulings, and every one of them decided a question this seat had been carrying**

**Seat:** `1.0.0_SA_CTO` · laptop · CLOUD · **UTC** 2026-09-21 ~04:0xZ
**Arming record:** `ANDREW_DIRECT_20260921_005xZ_...md` @`07b8a03ec3`, amended §8 @`57751941a0`
**State:** ARMED · cadence 30m · job `e0992603`

---

## 0. HEADER FIGURES -- EACH PRODUCED BY A CALL IN THIS TICK

| figure | value | the call |
|---|---|---|
| projects in scope | 2, both **PLACED stage 0**, flags `-` | `sequence-check --project` x2 |
| live COO lanes / cap | **3 / 3 -- AT CAP, no longer over** | `sequence-check` CAPACITY |
| `MDPF_TAXSMA` orders | **27; 4 complete, 23 non-terminal** | `git ls-files task-orders/` + first-word `<status>` |
| `NFRA_MCPINDEX` orders | **0** (pre-L6) | same |
| positive control | **33** (`NFRA_OPLGTW`), **2 non-terminal** | same -- ⭐ matches the CVO's resolver |
| unread inbox | **0** | `ls` on my inbox slice top level |
| open calls at Andrew | **2** (Schwab tools; rollback-repair owner) | §4 |

## 1. ⭐ BOTH ITEMS THIS SEAT HAS CARRIED FOR THREE TICKS ARE CLOSED

### 1.1 `R-OG-22` CLOSED @`e51d49aa9e` -- the adopted remedy cannot work

`R-OG-22` (09-16) settled that `job_memory_bytes` does not move (a multi-tenant ADMISSION parameter vs a
single-feature contract term) and left one prerequisite: *"before any contract number is LOWERED, is 250,000
rows / 50 MiB a CONSUMER REQUIREMENT or an aspiration."* It also named a third branch **explicitly as an
unconfirmed inference from a 22.6:1 ratio**, calling it *"a cheap thing to falsify."*

**It was falsified fourteen hours later.** Row `NFRA_OPLGTW-S57` (`2.0.0_SA_COO~O`, 09-20T11:05Z), at the
source: the export materialises the whole result set in **up to three concurrent full-size representations**,
and **`LIMIT_EXCEEDED` is raised AFTER the allocation** -- so peak RSS tracks the **requested** size even on
requests that are **refused**.

⛔ **THAT CLAUSE DECIDES IT: lowering `export_rows` does not bound peak RSS.** A 250k request against a 60k cap
still allocates for 250k and is refused afterwards, at the same peak. **The remedy would have changed the
number in the SPEC and not the behaviour on the HOST -- and its criterion could have gone GREEN, because a
conforming test request is small by construction.** Rec **withdrawn as a remedy**; the remedy is the
implementation, in two independent parts: **check before allocate**, and **stream**. Question 2 stops being a
gate **without being widened** -- its own scope was *"before any contract number is LOWERED"* and none is.

### 1.2 `G-C`'s delegation RECORDED @`a35f175a59` -- his answer had no carrier for three hours

Andrew-direct ~00:5xZ: *"(b) with the delegation written into the gate deliverable."* ⛔ **The instruction
NAMED an artifact and the artifact DID NOT EXIST** -- `0.9.0_WK_NFRA_OPLGTW~6` had recorded the same absence
from the other side. Recorded **conditional**, because his sentence is (*"if ... that is great, but
otherwise, we will return to this when I am back at the console"*), and the condition's state is
**UNRESOLVED** -- that lane read STALE, which is neither able nor unable.
⚠ **`G-C` IS NOT CLOSED.** It needs three things; the administrator is one. **Naming an administrator is not
verifying an identity**, and the file's existence must not be read as the gate's satisfaction.

## 2. `NFRA_MCPINDEX` L5 LANDED, AND BOTH ITS OFFERS WERE RULED BEFORE L6 @`4710be2a46`

`2.0.0_SA_COO~M` landed decomposition v1 @`1c99d5f1ac` -- **38 cells, 93 edges, acyclic, 33 OPEN / 5 HELD** --
and offered two choices, noting *"a disagreement is cheapest before L6."* L6 was unblocked, so both were
ruled the same tick.

- **OFFER A -- the repository file is the ONE home; S3 is an ARCHIVE.** ⭐ **A HOME IS DEFINED BY WHAT READS
  IT AT RUNTIME.** `query_v0` loads `CATALOG_PATH`; `catalog_gate` enforces it. Nothing reads S3 on the
  serving path, so S3 is not a home. **The tension was two axes being read as one.** The bound is
  falsifiable, not advisory, which turns `MX-c-3`'s J criterion into an M one.
- **OFFER B -- C2 constrains the TOOL, not the FILE. Composed design ADOPTED.** C2 says *"a tool ships only
  with a catalog entry and a safety classification"* -- a condition on the shipped tool, naming no file.
  ⭐ **Reading it as mandating entries in `registry.py`/`destructive_ops.py` would import today's
  IMPLEMENTATION into the CONTRACT.** The deciding reason is **`FWD-10`'s own proof** (*"catalog entry +
  tool, nothing else"*), which the current four-file path **cannot** satisfy: **the contract's committed
  outcome outranks the incumbent implementation.** C2 gains no slack -- resolvability by name through both
  registries stays the bar, **exercised**, with the denominator printed.

## 3. ⛔⛔ THE ROLLBACK EXPOSURE NOW BLOCKS A SECOND PROJECT

`2.0.0_SA_COO~M`, independently: *"The live Gateway has no valid rollback. `MX-r-1`'s first criterion REFUSES
to deploy until the current release's rollback target is restorable, and **no seat owns making it so**."*

⭐ **The AC10 residual has arrived in a project that never touched `NFRA_OPLGTW`** -- it is no longer a
residual on a closed project but **a live dependency of an entire deploy arm**, measured by a third seat.
⚠ **That raises its REACH, not its NOVELTY, and it does NOT retract tick 2 §2(b)**: it was discovered, ruled
and disclosed on 09-18 and I was still wrong to frame it as unknown.
⭐ **`MX-r-1` REFUSING IS THE SYSTEM WORKING** -- a criterion that declines to deploy onto a release with no
rollback is the guard that should exist, not a blockage to route around.

## 4. OPEN CALLS AT ANDREW -- **2**, both created by measurement, neither adjudicable here

1. **Enabling the five Schwab tools** -- changes what a live Gateway serves on a release the runbook marks as
   having no valid rollback. RESERVED by citation: NEVER-class served-output line.
2. ⭐ **NEW: who owns making the live Gateway's rollback target restorable?** **REC: the FIRST act of
   whatever seat next holds `NFRA_OPLGTW`.** Not decided here: the repair is on a live client-facing surface
   owned by a project whose lane is CLOSED on his word, under the **no-new-seats hold** he set at ~02:4xZ.
   **I will not seat a lane against that hold, nor hand a Gateway repair to a lane that does not own the
   surface.**

## 5. NEWLY OWED AT THIS SEAT, FROM OUTSIDE THE SCOPE

`2.0.0_SA_COO~B` filed the **`IRPT_BCKEND` round-7 COO completion report** (`98947`): round TERMINAL, 4/4
served deploys live and independently verified, 0 genuinely-open TOs proof-based of 79.
⛔ **My L10 round-7 analysis is OWED -- and it waits on the CVO's L9 slug, which has NOT landed** (0 unread,
and no IRPT slug in my read/). **The order slug → analysis → recut is LOAD-BEARING (LD-0521): a round-8
issuance cut before round 7's slug deadlocks round 7's L10 until round 8 fully drains.** That lane has it
right -- it recuts *on* my analysis, not before. ⚠ **This is exactly §0.8's case: the register reads an
honest zero while the seat owes an artifact.**

## 6. ACTS THIS TICK

`e51d49aa9e` (R-OG-22), `a35f175a59` (G-C), `4710be2a46` (offers A/B), this log. Messages `98939`-`98946`.
⛔ **One commit was REFUSED mid-tick -- a peer's merge in the shared tree (`MERGE_HEAD 280374b646`, 6 paths,
not mine).** ⭐ **I sent the RULING to `2.0.0_SA_COO~M` before the commit landed, because the lane needed the
answer and not the hash**, and said so in the message. A ruling held hostage to a peer's merge is a ruling
that arrives after the cut it was meant to inform.
**No TO cut, no seat spawned, no apply.** The ~02:4xZ no-new-seats hold is untouched.

## 7. COMPLETION TEST

**NOT DONE -- 0 of 2 complete.** `MDPF_TAXSMA` active/EXECUTING (L7 rd1); `NFRA_MCPINDEX` active, **DECOMP**
(was PRD -- L5 landed this tick). **Both REACHABLE, 0 UNREACHABLE**, so `HELD-AT-STOP` does not apply.
**Push state:** `e51d49aa9e`, `a35f175a59`, `4710be2a46`, `67c7257132` **LOCAL**; only `0.0.0_AB_MSTR` pushes.

## Compiler Tools

`sequence-check.py` x2 · `git ls-files` over `task-orders/` x3 (one a positive control) · `git show HEAD:` with
first-word `<status>` parsing · `comp-find` x3 (`R-OG-22` 13/231, `G-C` 78/231, PRD C1/C2) · `git show
HEAD:<ruling>` at cited lines · `json` reader over `INVESTIGATION_v1.md` (⚠ crashed on cp1252 stdout encoding
mid-print -- the same fault `2.0.0_SA_COO~M` hit in `comp-adversary` tonight) · `safe-commit` x3, one refused
on a peer's merge and retried.
