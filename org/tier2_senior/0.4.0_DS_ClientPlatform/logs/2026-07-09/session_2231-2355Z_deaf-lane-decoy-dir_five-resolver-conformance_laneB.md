# Deaf lane -> the decoy dir -> five-resolver conformance (lane ~B)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform~B
**Window:** 2026-07-09T22:31Z (went deaf) -> 2026-07-09T23:55Z
**Commits:** `331eb1a4a` (mine). Authored-uncommitted: `.tools/inbox-resolver-conformance.py`.

---

## Current State

Written for a reader with zero prior context.

### 1. I woke deaf, holding a GO to edit a client-facing producer. I wrote nothing.

At `22:30:44Z` my lane went deaf. My last instruction (COO) was: *after 04:00Z, open a ledger,
land step 1 (`A_00`), then step 2 (`D_00`).* Three messages had piled up unread:

- COO `225453Z` `[SOVEREIGN, STANDING]` -- Andrew closed **49F / Schwab / RPS / bd-custody**.
  *"i do not want to deal with 49 right now ... not something that we should pursue unless i
  explicitly ask for it."* COO carved out an exception: **"`A_00` is NOT 49F work ... that work
  survives the prohibition."**
- COO `223204Z` `[STOP]` -- no `ycharts_*` or ANY external vendor API without Andrew's per-use word.
- CTO `231152Z` `[STOP]` -- **cancels his own `221611Z` authorization.** `data/black_diamond/`
  **IS** 49F's pipeline; therefore `A_00` **and** `D_00` are both cancelled. *"Confirm before you
  touch a file."*

**The two Tier-1 execs disagreed, in writing, about `A_00`, and neither held the other's message.**
I was the only party holding both. I wrote nothing, computed the intersection (write nothing --
safe under either reading, so the divergence never gated me), and escalated the difference to both.

- CTO `231518Z` overruled COO, ordered the carve-out **retracted explicitly to every lane that
  received it**, and adopted the rule as fabric doctrine under my name:
  **latest + most-restrictive binds; act on the intersection, escalate the difference.**
- COO `231641Z` issued the `[EXPLICIT RETRACTION]`.
- MSTR `233155Z` then wrote *"the A_00 guard survives"* -- **the retracted carve-out, restated by
  Tier 0**, 15 minutes after its withdrawal. I **declined a Tier-0 instruction** and escalated with
  receipts. MSTR `233620Z` `[STOP]` retracted it in full.

> **The prohibition is only as good as its weakest copy.** The weakest copy ended up at the top of
> the authority chain.

**Zero files written under `data/black_diamond/`, `schwab/`, or `opal-data-bd` at any point.**
`b5a95c9f5` (BRANCH-A last-good hold) untouched. Status: `BLOCKED-SOVEREIGN`.

### 2. The deafness had a mechanism, and it was not "the enumerator is blind"

`fabric-check --blocks` reported `deaf=2`. The answer was `3`. CTO and COO both diagnosed *"it
cannot enumerate nested `~lane` inboxes."* **Source refutes that:**

```
org/mcp/server.py:1133       inbox = INBOX_DIR / to_folder.name / f"~{to_suffix}"   <- mail DELIVERED here
org/mcp/inbox-watch.sh:98    WATCH_DIR="$INBOX_BASE/$AGENT_DIR/~$SUFFIX"            <- Monitor WATCHES here
.tools/fabric-check.py:132   d = os.path.join(INBOX_DIR, serial)                    <- deaf-check READ here
```

The third path is the **flat** dir `inbox/<base>~<suffix>/`. It **exists for 28 lanes**, receives
nothing from the broker, and answers **`0 unread` forever.** **The watcher and the
watcher-of-watchers read different directories.** Not blindness -- **a decoy that reports health**,
which is strictly worse because a blind instrument at least cannot be quoted.

Startup ground truth (`ps` + `get_agent_status`): **no `inbox-watch.sh` process for
`0.4.0_DS_ClientPlatform~B`**, and `NOT REGISTERED`. **The Monitor was never armed, not dead.**
*"Absent" and "died" are different states and only one of them respawns.*

Independently corroborated by `ps` with a positive control (assert my own known-live watcher
appears): **38 nested `~lane` inboxes exist; exactly 1 has a live watcher -- mine, armed at
startup. Before this session: zero.** (My first attempt at that count was itself wrong:
`grep -c '~'` matched the tilde in the temp path `ANDREW~1`. Caught by implausibility, not by the
control.)

### 3. `331eb1a4a` -- fabric-check fix (CTO GO `231518Z`, COO review APPROVED `232922Z`)

- `lane_inbox_dir()` -- canonical resolution, mirroring **both** writers, comment-bound to
  `server.py` + `inbox-watch.sh` so the next drift is visible.
- `enumerate_inbox_lanes()` -- walks **both** dir conventions. *A lane must be enumerable before
  it can be judged.*
- `is_deaf()` -- factored out **so the positive control drives it in both directions.**
- `legacy_flat_orphans()` + `deaf_denominator_line()` / `enum_denominator()` -- denominator on
  **both** `--blocks` exits, **including the clean pass, which is the pass that lies.**

```
DEAF-COVERAGE: deaf=0 over 85 enumerated inboxes (43 base serials, 38 nested ~lanes, 28 flat-lane dirs)
WARN: flat_orphans=4 -- message(s) written to an UNWATCHED path (inbox/<base>~<lane>/).
      FIX THE WRITER (.tools/operator.py:539 ... mkdir's it on demand).
      Do NOT delete these files: they are the only evidence the dispatch path is broken.
      Do NOT hand-deliver them into a live agent either -- a queued GO has no expiry.
```

**Design call, ratified by CTO + COO:** flat-dir orphans are **not** folded into `unread`. DEAF's
prescribed remedy is *respawn*, and **a respawn cannot drain a directory no Monitor watches** --
the alarm would demand, forever, an action incapable of fixing the condition that raised it (the
dual of a latched alarm). Different failure, different owner, different remedy. **Louder is not
better.**

**It immediately found 4 stranded messages** -- MSTR `BUILD-CHARTER`s to `1.1.0_SA_CTO~A` and
`3.1.0_SA_CVO~A`, dated **2026-05-29, undelivered 41 days**, one a `PROCEED ... GO`. Reported to
MSTR (their author); **not moved, not deleted** (CTO `232729Z`: *delivering a 41-day-old GO
executes a stale authorization*). MSTR dispositioned **SUPERSEDED**, ledgered **LD-0269**, and is
routing my general form toward a Directive: *an enumerator that finds nothing and an enumerator
that cannot see are the same output.*

### 4. `.tools/inbox-resolver-conformance.py` -- AUTHORED, EXERCISED, **UNCOMMITTED**

CTO handoff: *you author the five-resolver conformance assertion; COO reviews and commits.*

```
resolver                role        method    verdict      note
fabric-check.py         CHECKER     EXECUTED  OK           lane_inbox_dir() -> nested
inbox-watch.sh          MONITOR     EXECUTED  OK           emitted NESTED.md, ignored FLAT.md
halt-gate-check.sh      INTERLOCK   EXECUTED  NONCONFORM   PASSED a nested-dir [STOP] (rc=0; control
                                                           proved rc=2 reachable) -- lane UNHALTABLE
server.py               WRITER      PARSED    OK           :1133
operator.py             DISPATCHER  PARSED    NONCONFORM   :540  inbox_dir = inbox_root / agent
RESOLVER-COVERAGE: nonconformant=2 over 5 resolvers (3 EXECUTED, 2 PARSED)
```

**The INTERLOCK is exercised, not asserted.** `safe-apply` calls `halt-gate-check.sh` at the last
reversible moment before `terraform apply`. Control: a `[STOP]` in the **base** dir -> `rc=2`
(hard block), proving `rc=2` is reachable. Decisive: the identical `[STOP]` in the **canonical
nested** dir -> **`rc=0`, silent pass.** **A `~lane` agent cannot be halted by `[STOP]`** --
unconditionally, not as a race, even with no watcher running. Exposure bounded tonight (both
`~lane` ledgers are sovereign-gated verifies, no pending apply) -- **bounded by luck, not by the
gate.**

COO licensed parsing the bash resolvers. **I executed 3 of 5** (both bash resolvers were
sandbox-runnable: `halt-gate-check.sh` exposes `HALT_GATE_INBOX_ROOT`/`HALT_GATE_REPO_ROOT` + a
stable exit contract; `inbox-watch.sh` derives `INBOX_BASE` from `SCRIPT_DIR`). The 2 PARSED rows
are labelled PARSED, counted separately, and carry a printed caveat. **No silent downgrade.**
Exit contract: `0` conform | `1` nonconformance | **`2` harness broken -- never read as `0`.**

`--self-test` **7/7** (positive control on the checker: a NESTED resolver judged conformant, a FLAT
one NONCONFORMANT, a vanished source line must **raise**, never silently pass).

### 5. cot -- IN SCOPE, and its one served window is live-wrong (VALUE class, not EMPTY class)

CVO routed cot's wall-clock anchor to me and recorded *"client impact bounded: only 1Y served."*
**That bounds the EMPTY class. The VALUE class lands on the served window.** bd's harm was never
emptiness -- it was **$3,516,778.16** of dropped flow.

Grounded on cot's own evidence (no bd read):
```
SERVED  s3://opal-data-cot/platinum/firm/leaderboard.json
        windows=['1Y']  1Y.entry_count=1  data_as_of=2026-07-07
        generated_at=2026-07-09T02:04:55Z    window_bounds=ABSENT
SOURCE  gold_utils.py:118-119  _today() = pd.Timestamp.now(tz='UTC').normalize()   <- WALL CLOCK
        D_00c:1253 today=_today()   D_00c:1152 w_start = today - 365d  -> 2025-07-09
        D_00c:787  latest_date = detail['date'].max()                  -> 2026-07-07
        D_00c:392  window = detail[(date >= w_start) & (date <= latest_date)]
ORACLE  comp-freshness cot -> content as_of 2026-07-07, 2td behind 2026-07-09 frontier
```
**The served "1Y" is `[2025-07-09, 2026-07-07]` = 363 days.** It drops `2025-07-07` (Mon) and
`2025-07-08` (Tue) -- two business days of `nna_daily` -- from a window labelled `1Y`. Not empty:
**short, populated, and mislabelled.** cot emits **no `window_bounds`**, so it is unobservable
downstream. **Dollar magnitude UNMEASURED** (needs `gold/canonical/nna/`; will not trigger an
ad-hoc gold run -- CLAUDE.md NEVER rule).

**Not landing tonight, and the reasons are hard gates, not deferral:** `D_00c` writes a **SERVED**
artifact -> **NEVER#2 never-widen sign-off (CTO+COO)**, and `DELTA=0` is unavailable *by
construction*; a cot gold push **AUTO-DEPLOYS** (`safe-deploy.sh` PIPELINE_MAP); the 02:00Z cot run
already carries the snapshot row-count verify; CTO's standing rule requires a **COTTONWOOD-tenant
probe**. Fix will be **cot-native** -- no mirroring bd's diff (Rule 13, both directions).

### 6. Six instances of one grammar, found in the act of measuring each other

*An instrument reporting confidently on something other than what it claims to measure.*

1. `fabric-check` deaf-check read a **decoy dir** -> `0 unread` forever.
2. COO read a **moved file** in `read/` as **a live Monitor** (my startup drain moves files too).
3. COO's `git show origin/CLOUD:<path>` was **MSYS-mangled**; `grep -c` counted **0 matches inside
   a `fatal:` error**.
4. My own `grep -c '~'` matched the tilde in `ANDREW~1` -> "10 lane watchers"; the answer was 1.
5. My conformance harness: `shutil.which("timeout")` -> Windows `TIMEOUT.EXE`; bare `"bash"` ->
   **WSL bash**; Windows paths into bash made `[ -f "$msg_file" ]` fail so `halt_gate_is_stop_class`
   **silently downgraded a real `[STOP]` to "routine"** (rc=1). **The harness would have printed
   the TRUE verdict from a BROKEN instrument.** A right answer for a wrong reason is not evidence.
   Hence exit code `2`.
6. **`.gitignore:183` ignores `.tools/` wholesale** ("Local tooling binaries") while **191 files
   there are tracked.** A **newly authored** fabric tool is ignored and **`git status` says
   nothing.** COO must `git add -f` or the conformance tool never lands.

**MSYS path-mangling produced a false-empty three times tonight, in three tools, to three agents.**
That is an environment-shaped trap, not an agent-discipline failure.

---

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | `D_00c` | **WARN** | Resolved to **bd-gold** `D_00c` with no firm prompt. `D_00c` exists in bd **and** cot; under a live bd prohibition a cot question silently returned bd's manifest. **Gap: `comp-pipescript` has no firm/tree scope arg** (`--help` confirms). |
| `comp-freshness cot` | cot chain | **PASS** | Grounded the 2-trading-day lag independently: `content as_of 2026-07-07, 2td behind 2026-07-09 frontier`. Also surfaced `cot_platinum_employee_leaderboard -> SKIP`. |
| `comp-surface-check` | `.tools/fabric-check.py` | **PASS** | Auto, inside `safe-commit.sh`: *"1 changed file(s) touch no critical surface."* |
| `commit-gate.sh` | `fabric-check.py`, `inbox-resolver-conformance.py` | **PASS** | rc=0 both (py_compile + AST undefined-name + ruff py39). |
| `comp-which` HUD | Bash greps | **PASS** | Nudged `comp-lambdamap parity` and `comp-pipescript io D_00c`; the latter surfaced the firm-ambiguity gap above. |

**What worked:** `comp-freshness cot` was the decisive independent oracle for the cot lag -- I did
not have to take CVO's `data_as_of` on report, and I did not read bd to get it.

**What failed:** `comp-pipescript io D_00c` answered for the **wrong firm, silently.** Rule 13 makes
bd/cot separation law and a sovereign prohibition currently covers bd; a DS asking about cot's
`D_00c` gets bd's I/O manifest with no warning. **Same grammar as the decoy dir.**

**Gaps found (2, both routed):**
1. **`comp-pipescript` needs a firm/tree scope** (`comp-pipescript io --tree cot D_00c`) or must
   fail loud on an ambiguous script id. Filed to CTO/COO.
2. **`comp-freshness cot` registry points at `platinum/firm/employee_leaderboard.json`, which does
   not exist** (`aws s3 ls` confirms; the real served key is `leaderboard.json`). It prints **SKIP**,
   which reads as "not applicable" rather than "I am watching a key that does not exist." **cot's
   served leaderboard therefore has no freshness coverage.** *Note: my first attempt to prove this
   by grepping `.tools/` for `cot_platinum_*` found nothing -- but the positive control
   (`cot_platinum_header_metrics`, which the tool had just printed) also found nothing, so the grep
   was blind, not the registry empty. The IDs are constructed, not literal.* The SKIP + missing-key
   fact stands on `aws s3 ls`; the registry-shape claim is **NOT ESTABLISHED** and is not asserted.

---

## Files Modified

| File | Change |
|---|---|
| `.tools/fabric-check.py` | `331eb1a4a`, +257/-19. See commit message. |
| `.tools/inbox-resolver-conformance.py` | **NEW, UNCOMMITTED** (gitignored -- needs `git add -f`). COO commits. |
| `memory/project_cot_snapshot_zero_row_freeze_20260709.md` | STOP header + `description:` rewritten -- it instructed a respawned me to run cancelled bd work at 02:30Z. |
| `memory/project_pending_trigger_nna_1y_served_verify.md` | Same, for the 10:30Z bd verify. |
| `memory/MEMORY.md` | Sovereign-prohibition banner; 3 triggers marked SUSPENDED; permissive duplicates removed. |
| `memory/{4 new feedback files}` + `MEMORY_FULL.md` | denominator law; alarm-remedy law; latest+most-restrictive; stale-durable-instruction. |

**Why the memory edits are load-bearing:** COO suspended the shared `PENDING` trigger doc so a
respawn could not execute it. **My auto-recall memory said the same thing and no exec could reach
it.** The `description:` field is what surfaces on recall -- a STOP in the body arrives too late.

---

## Blockers

**BLOCKED-SOVEREIGN (evidence-cited; nothing assumption-blocked, nothing idling):**

- **[Andrew]** 49F / Schwab / RPS / `data/black_diamond/` / `opal-data-bd` -- **CANCELLED, not
  parked.** `A_00`, `D_00`, both `bd-49f` ledgers, the 02:30Z bd row-count verify, and the 10:30Z
  NNA served-verify all stop. Only Andrew reopens.
- **[Andrew, via COO]** The one question COO is putting up: does the cancellation reach an **open
  ledger on a frozen client-facing AUA** (`$1,837,159,865.68`)? **I do not pick a reading.**
- **[1.0.0_SA_CTO + 2.0.0_SA_COO]** never-widen sign-off (NEVER#2) for the cot `D_00c` anchor fix --
  it moves a **served** number by construction, and a cot gold push auto-deploys.
- **[2.0.0_SA_COO]** review + `git add -f` commit of `.tools/inbox-resolver-conformance.py`.

**Not blocked, deliberately not done:** the `server.py:1208` LOUD-warn patch (routed to
`0.7.0_AE_CloudOps`; `server.py` runs in every agent's process and CTO's *"touch nothing else"* is
the more restrictive instruction -- **latest + most-restrictive, applied to me**).

---

## Next Steps

1. **[2.0.0_SA_COO]** Review + commit `.tools/inbox-resolver-conformance.py` (**`git add -f`** --
   `.gitignore:183` swallows it). Then the **retraction-completeness sweep**: *who else still holds
   COO's withdrawn `225453Z` carve-out?* Population = every lane live at `22:54Z`. **Nobody has
   enumerated it, and 37 of 38 lane inboxes have no watcher**, so a broadcast retraction cannot be
   assumed delivered. MSTR adopted this as an LD-0269 leg.
2. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** Fix the two nonconformant resolvers -- **`operator.py:539`**
   (dispatcher writes every lane GO to an unwatched dir **and `mkdir`s it**) and
   **`halt-gate-check.sh:148`** (a `~lane` is **unhaltable**). The conformance tool is the detector;
   these are the bug. Wire it into CI so the gate is RED until both land.
3. **[0.7.0_AE_CloudOps]** `server.py:1208` -- print LOUD when a receipt lacks `channel push`.
   **Do NOT `return non-OK`**: absent push means *"no LIVE registered instance,"* not
   *"undelivered."* CTO accepted this correction.
4. **[1.0.0_SA_CTO + 2.0.0_SA_COO]** Rule on the cot `D_00c` anchor fix: never-widen sign-off, a
   COTTONWOOD-tenant probe, and a quiet run (**not** tonight's 02:00Z, which carries the snapshot
   verify). Then **[0.4.0_DS_ClientPlatform~B -- me]** authors it cot-native, holds it uncommitted.
5. **[3.0.0_SA_CVO]** Amend the cot contract row: **VALUE-class exposure, LIVE and SERVED (363-day
   "1Y")** -- *"does not currently reach a Cottonwood client"* is true of the EMPTY class and
   **false of the served one**, and it is the sentence someone quotes in six weeks.
6. **[1.0.0_SA_CTO / 2.0.0_SA_COO]** Two comp-tool gaps: `comp-pipescript` firm-ambiguity on
   `D_00c` (silently answered bd under a bd prohibition), and `comp-freshness cot` watching a
   nonexistent `employee_leaderboard.json` key while the served `leaderboard.json` goes unwatched.
7. **[0.0.0_AB_MSTR]** LD-0269 Directive: *every gate that reports a count must state the universe
   it counted over.* Add the **MSYS false-empty** class -- three tools, three agents, one night.
