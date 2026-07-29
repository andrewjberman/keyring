# 1.0.0_SA_CTO~Z -- RV-0057 F-001 mechanism: the audit archive's key has no device in it

**archetype:** MIXED (DIAGNOSE + VALIDATE + SCRIBE)
**Session window:** 2026-07-29 ~2320Z -> ~2345Z. Site Z (second device), cygwin, workspace at
`/cygdrive/c/Users/Opal Bloomberg/Desktop/ajb_workspace`.
**Assignment:** Andrew-direct via MSTR~Z -- RV-0057 F-001, mechanism half. Site-Z scoped.
**Commits:** `e05fad4f3` (design + build TO), `7821a8366` (two record corrections). Both pushed.

## 1. Startup

`/watcher`: serial read NOT REGISTERED; registered PID 5420; persistent Monitor `b7aneay3d` armed
and confirmed `running` via `TaskOutput` -- the only probe that observes a *consumer*. No orphan and
no peer collision: the one pre-existing `inbox-watch.sh` on the box belongs to a live
`0.0.0_AB_MSTR~Z` (pid 129780 under a live wrapper), left untouched per self-scope. Zero crons
(`CronList` empty; LD-0157). Owned-paths hook wired. Session serial file written. `git fetch` +
`merge --ff-only` advanced `01d0fbec4 -> f35e69bd8` (11 commits; merge, never rebase -- NEVER#7).

A.3 PATH probe: **93 of 96** resolve bare, and the mandatory EXERCISE half passed (a forwarder
produced its own banner). I ran the exercise clause deliberately -- my own last session logged a
false `93 of 93` textual-proxy pass, and that is now XXX.md's cautionary example.

**A.2 (`audit-archive-invoker.py`) I ran ONLY as `--self-test` and `--dry-run`, never live.** It is
the subject of this session's finding and it writes to the shared evidence base; running it live at
startup would have appended a twelfth false batch to the record I was sent to fix.

## 2. What I was asked, and the one correction that changed the fix

F-001: *"audit records are device-local, governance reads them git-shared."* Its premise reads
*".gitignore:68 is a blanket `*.log`, so **every** audit log is device-local and untracked."*

**Measured, per file, `git ls-files` + `git check-ignore -v` with a positive and a negative control:
5 of the 13 covered logs are TRACKED.** Four are declared `!` un-ignores at `.gitignore:494-497`;
the fifth, `org/ws-charter-hard-block-audit.log`, is tracked since `7f1d3b29c` with **no `!` rule at
all** -- `check-ignore` still reports it matched by `:68`, and it survives only because tracking
outranks ignoring.

**This changes the fix.** The mechanism for putting an audit log in the shared record already exists
and is already in use for 5 of 13. The task is not *invent a consolidation*; it is *extend the key
the instrument already has*. I would have designed a heavier thing without this measurement.

## 3. The defect, source-confirmed

The archive is keyed on `(timestamp, logical-log)` -- a tuple that stopped being unique the day the
fabric acquired a second device. `audit-archive-invoker.py:99-108` parses each archive child dir as
a bare timestamp; `:185` resolves the baseline as `ARCHIVE / ts`. A grep of the entire file for
`hostname|device|uname|platform|node()` returns **two hits, both comments, both reading
"single-host"** (`:75`, `:417`).

So site Z's audit evidence has no slot in the shared record, and the shared record carries no marker
that a second device exists. A `0` override count from either device is indistinguishable from *"no
overrides happened."* Same class as RV-0047 F-015, arriving through a device boundary instead of a
time boundary.

Design landed: `docs/architecture/NFRA_AUDITDEV_PRD.md`. Add `<DEVICE>` to the key, per-device
`.baseline`, device-stamped findings, global manifest, laptop chain migrated wholesale.

## 4. A hypothesis I refuted against myself -- the negative is the load-bearing part

I expected a site-Z mint to **corrupt the laptop's chain** and make the primary device's healthy
trail read as tampered. I was about to write that as the headline.

**Refuted at source.** `take_snapshot:381-386` pins a dirty log by copying the *prior baseline* copy
forward, and `:488`/`:494` put **both** `NON_APPEND` **and** `ERROR` logs into `dirty_logs` -- so all
8 divergent-or-absent logs carry the laptop's bytes forward byte-for-byte. The `935ca2a7d` per-log
unwedge (landed 13:50Z today, for an entirely unrelated reason) closes the cross-device corruption
vector by construction.

I checked the `ERROR` branch specifically because `pinned` is documented for `NON_APPEND` and the
three device-absent logs land in `ERROR` -- if they had fallen through both copy branches they would
have been **dropped** from the snapshot, and the header at `:339-341` names exactly that state as
the one that re-wedges the tool while disguising a finding as an instrument fault. They do not fall
through. `:494` catches them.

**Residual, sized honestly: a design wart, low likelihood, non-corrupting.** A site-Z mint would
produce a snapshot byte-identical to its predecessor, advance `.baseline`, and satisfy clause 1
having archived nothing -- a freshness clock reset by a device that contributed no data. It is
unlikely to fire at all (`:531` gates on `uncaptured_tail`, computed only over *clean* logs, and
site Z's clean set is the 5 low-churn tracked ones). Measured tonight: `snapshot=not-due, baseline
4.5h < 12.0h`. **Reporting this as an incident would have been the false-outage class**, and I had
the sentence half-written before I read `:381`.

## 5. A defect not in RV-0057: the instrument's positive control cannot fail here

`self_test` CONTROL-A (`:210-215`) compares the S1 known-redacted snapshot (1,305,108B) against the
live `git-author-override-audit.log` (12,055B on site Z) and requires `NON_APPEND`. They share no
bytes, so **it returns `NON_APPEND` for any site-Z state whatsoever.** It cannot distinguish *"the
S1 redaction is still detectable"* from *"wrong device."*

And `SELF-TEST: PASS` is the gate for *"instrument not broken"* -- so **the instrument certifies
itself healthy on a device where it is structurally blind.** Same shape as A.3's `93 of 93`. Each
new device chain needs its **own generated** control; an inherited one measures the author.

## 6. Second correction, against my own line

`.owned-paths.yaml:104` -- my hand, earlier today -- recorded *"site Z has ZERO git hooks... site-Z
commits are currently ungated."* **False.** 7 of 8 installers are wired; only
`install-headmove-guard.sh` is not. Exercised rather than read: `owned-paths-check.sh` run per-path
with its audit log redirected to scratch **BLOCKED** `infra/aws/lambda/data_refresh/**` and
`org/tier0/ledger/**` for this serial while **ALLOWING** `docs/architecture/**` -- a firing negative
control, so the gate is live here, not merely present.

**The error mattered more than the fact.** "Ungated device" makes site Z's audit logs read as an
artifact of absent gates -- safely empty. The opposite is true: the gates run, so site Z's ~23KB of
override records are **real evidence, durable nowhere**. My line was pointing readers away from
F-001. Struck and corrected in `7821a8366`.

## 7. Ordering as a safety property, and what I refused

The build TO shipped **STAGED, not GO.** The reader guard (`/mstr-review` Step 2 prints which device
chains it walked and refuses a fabric-wide count from fewer than all) is MSTR's and lands **first**:
a device-keyed archive shipped first gives governance partial multi-device data that *looks*
complete -- strictly worse than one chain a reader knows is partial.

**Refused at the gate:** F-002's stated remedy, *"suppress or device-scope the INTEGRITY clause."*
Device-scoping is the design. Suppression deletes a real tamper detector to silence a keying bug,
and is under-scoped besides -- 5 of the 11 findings are `COVERAGE`, not `INTEGRITY`, and false-fire
identically. Fix the key; keep every detector.

`FINDINGS.md` got an appended annotation, not a retraction -- the false batches stay. An audit record
that can be rewritten when it embarrasses the instrument is not an audit record. The annotation
deliberately carries **no `sig:` marker** (verified against `emit():256` *before* writing) because a
hand-written block with a matching sig would silently swallow the real finding it resembles; sig
count 17 before and after, and a `--dry-run` immediately after returns the identical verdict.

Its **scope bound** is the load-bearing half: it covers site-Z batches ONLY and must not absorb
RV-0057 Amendment 1b's separate **laptop-side** observation, which stays OPEN and UNOWNED.

## 8. Inbox, mid-session

`[SOVEREIGN-FENCE]` from MSTR~Z (2337Z), relayed from base MSTR. ACKed same turn.
**ADVI_PERFORMANCE + MDPF_GLOBAL are the HELD-OUT TEST SET for NFRA_VELOCITY** -- excluded from rail
shaping; a breached held-out set has no failure channel. Bound as an authoring rule: every P1 rail I
author publishes its **shaping corpus** explicitly, which is Rule 22's print-the-denominator applied
to a training set. NFRA_VELOCITY **CORE @ site Z is mine**; the canonical landing is in flight at
base CTO, so I did not start decomposition off a path I was told is not final.

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-which "where are the audit logs and who reads them"` | routed | Confirmed no rich tool models `.gitignore` precedence, hook wiring, or python control flow -- so the git-metadata and source reads below carry inline `# rail-checked:` markers rather than pretending a comp tool covered them. |
| `comp-surface-check` (auto, safe-commit x2) | OK | 2 files each pass, no critical surface. Workspace-side advisory; read anyway. |
| `comp-pulse diff` (auto, risk-reflex x2) | CLEAN | Printed its denominator both times: 2 files vs 1484 danger nodes, map 23.8h / 23.9h old. A measured result. |
| `owned-paths-check.sh` | **EXERCISED** | Per-path, one invocation each, audit log redirected to scratch so the probe did not pollute the log under review. Firing negative control (`infra/aws/lambda/data_refresh/**`, `org/tier0/ledger/**` -> BLOCK) beside a passing positive (`docs/architecture/**` -> ALLOW). This is what told me RV-0057 corrections route to MSTR instead of being edited by me. |
| `audit-archive-invoker.py --self-test` | PASS 7/7 | **The pass is the finding** (s.5), not the clearance. |
| `audit-archive-invoker.py --dry-run [--json]` | rc=1, 11 findings, `snapshot=not-due` | Dry only, never live. Sized s.4 down from "corruption" to "design wart". Re-run after the FINDINGS.md append as a control: identical verdict. |
| `git ls-files` / `git check-ignore -v` / `git cat-file -s` | the measurement of record | s.2. One command each; their absence would have been the whole error. |
| `comp-iam` / `comp-pipescript` / `comp-blast` | deliberately NOT run | No IAM, no gold script, no served surface, no deletion in this change. `comp-blast audit-archive-invoker` IS mandated in the TO's Phase 1 -- it belongs to the agent who edits the file, not to the one who specs it. Recording the reason because "ran it, GREEN" would be worse than not running it. |

## Open at others

1. **`0.0.0_AB_MSTR`** -- the reader guard (F-001 item 1). **Gates the AE build.** ACK sent 2340Z.
2. **`0.7.0_AE_CloudOps`** -- the build TO, STAGED. Reaches its owner over the **git tier**; MCP does
   not cross devices and per Rule 22b I have **not** recorded it delivered.
3. **`3.0.0_SA_CVO`** -- the RV-0057 laptop re-walk (F-001 item 3).
4. **Unowned:** RV-0057 Amendment 1b's laptop-side `git-author-override` truncation. Not explained by
   this mechanism, not determinable from site Z, still open.
5. **Small, surfaced, not fixed:** `org/ws-charter-hard-block-audit.log` tracked with no `!` rule;
   `install-headmove-guard.sh` unwired on site Z; and `owned-paths-check.sh` **ALLOWS** this serial
   on `data/*/scripts/gold/*.py`, which Rule 13 reserves to DS -- a lane gap, noticed as a negative
   control that did not fire, not chased.
