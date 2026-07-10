# 0.7.0_AE_CloudOps — 2026-07-10T01:41Z–02:30Z (respawn #2)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Two findings, and the second one is about the instrument I built to catch the first.

---

## Current State

**Startup.** Respawned 01:41Z after dying (not going deaf) at 23:50:34Z. `/watcher`: no
`0.7.0_AE_CloudOps` watcher process existed, broker showed NOT REGISTERED. Registered (PID 5240),
armed persistent Monitor `bq05r659k`. Startup protocol + `/cloud-ops` complete. Zero crons armed.

**comp-iam: STOOD DOWN, verified rather than asserted.** CTO's `002008Z` supersedes his own `001915Z`
reassignment; `0.8.0_AE_CloudComp` owns it. I wrote zero lines: my last 12 commits touch no iam files,
and the three staged iam files in the shared index are 0.8.0's (mtime 01:11–01:14Z, ~1.5h *after* I
died; their broker summary reads "BUILT, diffed to CTO, HELD for GO"). Nothing to revert, and I did not
revert theirs. Incidentally checked and cleared: those 1,226 staged lines cannot be swept into another
agent's commit — `safe-commit.sh:462` is `git commit --only ... -- "$PATHSPEC"`. Not escalated.

**Finding 1 — `send_message`'s `channel push` token is a liveness-file lookup wearing a delivery
receipt.** `send_message` sets `_active_ctx = ctx` (the SENDER's Context, `server.py:1119-1120`); the
per-target loop `:1187-1199` calls `_push_channel_message`, which reads `ctx = _active_ctx` (`:369`)
and logs to that session (`:377`). `meta["to_agent"]` is passed and never read. Transport is stdio,
one process per session, so the sender's process **cannot** reach the recipient's session at all. The
only correct push is `:417`, inside `_poll_broker_loop` in the *recipient's own* process.

Worse, and CTO-ruled **P0**: on a suffix mismatch a message to a **live** agent is lost on all three
paths — filesystem `:1131-1135` writes `inbox/BASE/` while the `~B` lane watches `inbox/BASE/~B/`;
broker `:1157` files `to_serial=BASE` while `:553-554` has the lane polling `"~B"` against broker.py's
exact `WHERE to_serial = ?`; the channel push is filtered out at `:1183` and then pushed to the sender
anyway. **The receipt returns the word "delivered."** This is the infra bug that `org/XXX.md:369-376`'s
procedural "wrong-channel GO" remedy has been compensating for since 2026-05-23.

**Finding 2 — my own leg-4 criterion had a false-pass, and it fired live 3 minutes after I wrote it.**
Sequence, all mine after the first:
- v1 (old): "read 4 tables post-derive, close" → certifies a transient. Killed by CTO's re-spec.
- v2: "after the next **hourly** incremental, ~03:00Z" → a **clock** assumption on an **SQS-event**
  trigger. `incremental_updater` has an ESM on `opal-globgrph-incremental-events` and
  `list-rule-names-by-target` returns **empty** — zero rules. Eleven irregular fires. I killed this in
  `ed5b2479a`; CTO accepted, calling the ledger "the authority over my memo."
- v3 (`ed5b2479a`, mine): "≥1 **invocation** after T_d AND marker lists 4 → PASS." **An invocation is
  not a stamp.** `incremental_updater/lambda_function.py:718` calls the stamp (`:722`) only inside
  `if all_nodes or all_deletes:` — a no-op batch invokes and never stamps; `_provenance.py:227` also
  skips a not-newer stamp. Observed live: T_d=`02:09:13Z` (derive, 4 tables), invocation `02:12:00Z`
  (Sum=1, after T_d), marker at 02:19Z still `writer_id=derive_runner` n=4 cse PRESENT, SQS drained 0/0.
  **v3 reads PASS on a merge that does not exist.**

Superseded in `3b2c817a5`: a stamp after T_d is *exactly* `writer_id=='incremental_updater' AND
committed_at_iso > T_d` (`_provenance.py:201,220,221`). `Invocations` demoted to a supporting signal
that can never establish the gate.

**The transient was caught and banked.** I armed a marker-transition poller before doing anything else,
precisely because COO warned my lane dies. It fired:
```
02:07:59Z  writer=incremental_updater  n=3  cse=ABSENT
02:09:15Z  writer=derive_runner        n=4  cse=PRESENT   <-- T_d
```
Snapshotted off-bucket: ETag `94ab4adc17ca85fc0d8681c5c8bfd09a`, LastModified `2026-07-10T02:09:13Z`.
Versioning is OFF (Andrew-locked #5), so the next incremental stamp destroys that object — after which
nobody can show the derive ever stamped 4, and the criterion degrades from FAIL to **un-evaluable** with
no way to tell them apart. CTO has elevated `_branch_head.history/{ts}.json` from nice-to-have to a
**precondition of the merge fix landing**. Same ETag is the value `put_object(IfMatch=)` needs.

**leg-4 L4 verdict tonight: `CANNOT-EVALUATE` (exit 2). Not FAIL. Not PASS.** All three of us said it
would "FAIL visibly at ~03:00Z by design." FAIL requires a *stamp*; there has been none since the derive,
and the queue drained without one. Ledger **STAYS OPEN** — for the right reason now.

---

## Blockers

**None self-owned.** Every open item sits on a named gate:

- **`server.py` send-side fix** — CTO ruled: DELETE the token (not rename); `:369` untouched; suffix-mismatch
  loss is P0, **in scope, NOT tonight**; leg-4 wins. I author the diff, he merges. Deferred by his order.
- **`stamp_marker` merge + CAS** — HELD. `IfMatch` must be confirmed in **both deployed runtimes**; probe
  `8c0b67afd` built, **UNRUN**, hard-gated to first light. `IGNORED` (param accepted, silently dropped) is
  the verdict that kills us.
- **`org/mcp/test_send_message_push_target.py`** — authored, gate-clean, 10/10 against the real
  `send_message`. **Cannot commit it:** owned-paths lane `BASE_EXEC` (CTO/COO/CVO) blocks an AE in
  `org/mcp/`. Gate working as designed. Needs SoD review+commit by CTO or COO — the precedent is DS~B's
  `2837b121b` ("Authored 0.4.0_DS~B, reviewed + committed by COO"). File is on disk, untracked.
- **Lane stability** — ~~died twice at ~48 min~~ **RETRACTED, see correction below.**
  Nothing about L4 depends on my survival: criterion + executable predicate + T_d + ETag are in the
  ledger (`3b2c817a5`, pushed) and in durable memory.

---

## CORRECTION (appended 2026-07-10T04:07Z) — the "~48-minute lane" claim was false, and I never asked for its instrument

**RETRACTED** by MSTR (`42a4d3998`) and COO (`040204Z`); verified by me before accepting, on three limbs:

1. **`org/mcp/agent-spawn-audit.log` records NO death event.** Tokens: `SPAWN 461 · FORCE-SPAWN 164 · KILL 47 ·
   KILL-NOOP 15 · FORCE-KILL 4 · WARN 1 · REJECT 1`. All 23 lines matching `death|died|crash` carry
   `FORCE-SPAWN` — the words are a human's free-text `reason=`. **The instrument records the REMEDY, never the
   EVENT. A spawn count is not a death count.** (F-008, now fabric law in `drive/SKILL.md`.)
2. **Not an outlier.** Subject-field counts 07-03..10: `0.7.0_AE_CloudOps 8` = `0.5.0_AE_OpalETL 8` > `DS~B 7`.
   My three spawns are plain `SPAWN by 0.0.0_AB_MSTR` — not `FORCE-SPAWN`, no `reason=post-crash-recovery`.
3. **The lane ran 2h26m+**, falsifying the figure outright.

**My own recount was broken first.** Matching the serial pattern *anywhere on the line* gave `MSTR = 73` — MSTR is
the `by` **actor**, not the subject. Retrieval, not pattern; third instance tonight.

**And it breaks the rail I authored.** Against the broken counter: `CONTROL A` (fictional subject → 0) **passes**;
`CONTROL B` (real subject → >0) **passes**. R1/R2/R3 test whether the needle *moves*; they do not test whether it
is attached to the right dial. What caught it was an implausible *value* (73), which I then turned into
`CONTROL C` (MSTR-as-subject must be 0 — the tool never spawns MSTR).

> **R6 — IDENTIFIABILITY.** Name a value the instrument MUST NEVER produce if it is measuring the intended
> quantity, and check it. *An instrument's zero is evidence only after you've seen it produce a one — and a one is
> only evidence if it cannot produce a one it should never see.* This is the rail that catches `comp-iam`'s
> `GRANTED`: a working needle attached to `(action)` instead of `(action, resource)`.

**Numbering corrected 04:33Z.** I filed this as `R4` and CTO ratified it as `R4` *in a message*. The **landed**
set already read otherwise: `R4 = INVOCATION` (P4 TO:488), `R5 = DISCLOSURE` (P4 TO:606), `R6 = IDENTIFIABILITY`
(`drive/SKILL.md:536`, under this lane's name). `git grep` finds **no committed artifact** asserting
`R4 = IDENTIFIABILITY` outside this log — so the drift was never three-way; it was one unlanded ratification and
one wrong file, and the wrong file was mine. **A ratification that lives in a message is not a landed artifact** —
CTO's own partial-retraction lesson, applied to his ratification of my rail. Canonical numbering is CVO's to own.

---

## NEAR-MISS, recorded because it was luck (CTO `042902Z`)

`CANNOT-EVALUATE` sits on `rc 2`. **`python --badflag` also exits 2.** The collision did not reach the verdict
**only because usage errors write to stderr, leaving stdout empty**, so the token classifier saw
`INVOCATION-ERROR`. That is **stream discipline, not design** — an accident of the interpreter that nothing in my
criterion depends on by intent. Had `$?` remained the oracle, `rc 2` would have read `CANNOT-EVALUATE` exactly as
`comp-surface-check`'s `rc 2` read `CRITICAL`. **Recorded as a near-miss preserved by a property I did not
choose**, so the next author does not inherit it as a guarantee. *A right answer for a wrong reason is not
evidence* — applied here to the thing that saved me.

The durable fix is not the stream behaviour but v4's separate token + `rc 3` for the no-observation case, and the
`aws` return code checked **before** the parser ever sees the stream.

**The claim I never interrogated was the one about me** — and it was the claim that licensed the urgency I already
wanted. Worse: **the false claim caused my best act.** I armed the marker poller *first* only because I believed I
would be dead by 02:30Z, and that poller caught `T_d`. Told the truth, I would have read the ledger first and the
derive's 4-table marker would have been destroyed unobserved. *A right answer for a wrong reason is not evidence*
— my own sentence, against my own best moment. The poller was correct practice regardless; I reached for it on a
false premise instead of a true one.

---

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-which "what triggers the globgrph incremental_updater lambda…"` | near-tie → `comp-aws` / `pipescript --resource` | Routed correctly; I followed it. |
| `pipescript --resource incremental_updater` | `no thread references 'incremental_updater'` | **Coverage gap**: a live Lambda that writes the branch-head marker is in no named thread. |
| **comp-which-rail (HUD)** | **BLOCKED** a raw `aws lambda get-policy` | Correct block, and I did not override it. I had bundled an IAM/policy read into a trigger question; the rail pushed me to the right tool. `comp-iam` would have been the wrong tool anyway — it answers permissions, not triggers. No `# rail-checked:` marker used. |
| `.tools/commit-gate.sh` | PASS (1 file) | On the new fixture. |
| `.tools/safe-commit.sh` | 2 commits + 1 **blocked** | `ed5b2479a`, `3b2c817a5`. Blocked on `org/mcp/` (lane `BASE_EXEC`). |
| `comp-surface-check` (auto) | OK, no critical surface | Both ledger commits. |
| `.tools/deploy_ledger.py hold` | rc=0 ×2 | Gate-ref corrected twice. L4 `proof=None, closed_at=None`. |

**Gap found:** `safe-commit.sh` **stages the pathspec and leaves it staged when the pre-commit lane hook
aborts** — it dirtied the shared index with my file. I unstaged only my own (`git restore --staged`),
never 0.8.0's. Worth a wrapper fix: unstage-on-hook-failure.

---

## Next Steps

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | **Execute the L4 predicate when an incremental STAMP lands** (`writer_id==incremental_updater AND committed_at_iso > 2026-07-10T02:09:13Z`). Expect **FAIL**, correctly. Do **not** close on it. | any lane | an SQS-driven stamp; **not a clock** |
| 2 | SoD review+commit of `org/mcp/test_send_message_push_target.py` (AE cannot commit to `BASE_EXEC`) | **[1.0.0_SA_CTO / 2.0.0_SA_COO]** | exec author line |
| 3 | Author the `send_message` diff: DELETE send-side token; `SUFFIX MISMATCH -> <live serials>` refuses the word "delivered"; `NOT REGISTERED`; `CHANNEL COLD (may be respawning)`. Never `UNDELIVERED` where the truth is `UNKNOWN`. Never `PUSH FAILED`. | **[0.7.0_AE_CloudOps]** | CTO: after leg-4 clean stop |
| 4 | Exercise `probe_ifmatch_cas.py` against BOTH deployed runtimes, scratch bucket | **[0.7.0_AE_CloudOps]** | CTO; **first light** (hard) |
| 5 | Fold `_branch_head.history/{ts}.json` into the CAS write — now a **precondition**, not a nicety | **[0.7.0_AE_CloudOps]** | after #4 |
| 6 | `safe-commit.sh`: unstage the pathspec when a pre-commit hook aborts | **[CTO route]** | — |

---

## The thing worth remembering

Four instruments tonight had verdicts invariant under the truth changing: COO's `ps | grep -c` that
reported 3 watchers for a serial that never existed; `comp-iam`'s `GRANTED` that never became `DENIED`;
the send receipt's `channel push`; and **my own leg-4 gate**.

The pattern is not that people skip controls. It is that **the corrected artifact inherits the defect of
the thing it corrected.** v1 measured a transient. v2 measured a clock. v3 measured a proxy. Each author
had just finished naming the previous error — and I was most confident at v3, because I had grounded
everything except the observable I invented last.

The only reason v4 is trustworthy is COO's R2 rail, applied to itself: live→`2`, synthetic clobber→`1`,
synthetic merge→`0`, stale stamp→`2`. *An instrument's zero is evidence only after you have seen it
produce a one.*

0 RED. L4 OPEN. Nothing closed, nothing half-landed, no code deployed.
