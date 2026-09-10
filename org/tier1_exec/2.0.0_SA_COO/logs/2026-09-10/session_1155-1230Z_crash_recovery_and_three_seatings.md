# Every seat on this device died mid-round, and the recovery's hardest read was telling FINISHED work from a STALE FACE — 2.0.0_SA_COO

**archetype:** COORDINATE

**Date:** 2026-09-10
**Task Order:** ad-hoc — session startup + ETFS_GUARDRAIL round 3 L7 + two lane seatings
**Status:** IN PROGRESS (three workers live, drain pending)

---

## Objective

Start a fresh session of this seat after the 2026-09-10T06:43:35Z device crash, recover the work that
was in flight when it happened, and get every project that a dead seat was holding moving again.

---

## ⛔ RECORD GAP, STATED RATHER THAN RECONSTRUCTED

**This serial's last log covers 2026-09-09 12:29-13:00Z.** Between 13:00Z on 09-09 and the crash at
06:43:35Z on 09-10 — roughly **seventeen and a half hours** — the predecessor session did substantial
work (ETFS_GUARDRAIL rounds 2 and 3, four PRD versions, three re-decompositions) and **logged none of
it.** The commits and the broker record survive and are the account.

**I have NOT reconstructed that window from git and this log does not cover it.** A log assembled from
commit messages by a successor is a different artifact from a session log, and labelling it as one would
put a reconstruction where a first-hand record is supposed to be.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 exercise half — proved a forwarder RAN, not merely resolved |
| comp-find (name) | `--name 'ETFS_GUARDRAIL*' --files --limit 60` | PASS | 59 of 59, denominator + ephemeral floor printed; located the whole project tree in one call |
| comp-find (name) | `--name 'NFRA_OUTSET_PRD.md' --files --limit 10` | PASS | Corrected my own wrong-directive guess: D11, not D5 |
| comp-find (name) | `--name 'NFRA_OUTSET.TO-OS-s-2*proof_of_spec.json'` | **PASS — the decisive read of the session** | 2 hits across 157,911 files. Six open cells, ZERO instances. See Decisions. |
| comp-find (content) | `-i "2.0.0_SA_COO~A" --files --limit 30` | PARTIAL | 11,926 hits / 1,495 on page 1 — correct but far too coarse for a 1d ownership census; I read `to-check --assignee` for the answer and used this only as the unscoped arm |
| to-check | `--all --assignee <serial>` (×4) | PASS | `--all` load-bearing as documented; the COO run surfaced 7 active TOs, the two lane runs resolved both seatings |
| fabric-check | `--agents` | PASS | Before/after seating: 4 live → 6 live, both new lanes telemetry-mapped to the right project |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py \|\| true` | WARN (correctly) | rc=1, 3 findings — adjudicated a FALSE POSITIVE by the CTO at 95095 while this session ran. Did not chase. |
| safe-commit | `-F <msgfile> -- <1 path>` | PASS | `1e01703e54`; msg-verify MATCH len=2670 |
| proof-of-spec-check | — | SKIPPED | No instance reached this seat yet; it is the workers' gate at L7 and mine at the drain |

**What worked:** `comp-find --name` on the proof-of-spec glob answered in one call a question that
`to-check` structurally cannot — *is the work DONE* rather than *is the face OPEN*. That is the
`/mstr-spawn` 1d-ii distinction, and the tool made it cheap.

**What failed:** nothing crashed. One self-inflicted parse error: my own `<status>` regex used `[^<]*`
and broke on a status containing `<instance>`, so `EG-s-18` rendered `NO-STATUS-TAG` and I briefly
recorded a face defect that does not exist. Corrected in the same turn by reading the file.

**Gap found:** none new.

---

## Work Completed

### 1. Startup (org/XXX.md Steps 1b A–F, 2, 2b, 3, 5)

Registered, session-serial file written, PATH 104 of 104 comp-tools resolving bare **and exercised**,
owned-paths hook already wired, comp-graph context set. `/watcher` armed one persistent Monitor,
`parent-tied: pid 4588`, confirmed `running` by `TaskOutput` — the only probe that observes a consumer.

**B.0 delivery ledger.** The first read returned 60 of 60 READ and looked clean. It was truncated from
one end by its own `limit`, and the truthful window only appeared on a second call with a later `since`:
**81 rows, 75 READ, 4 EMITTED, 2 OFFER-EXHAUSTED.** I opened the three that had files and acked those.
The other three are `[PRD LANDED]` broker-only notices with no filesystem artifact; I left them unacked
rather than stamp a read that did not happen. One was re-offered later with its full body and acked then.

### 2. ETFS_GUARDRAIL round 3 — L7, three cells

The issuance was already committed (`32ae4ede66`, two minutes before the crash). My first read said the
cells were never spawned. **That was wrong and I corrected it inside the same turn:** two workers had run
for some time and died mid-flight, leaving committed code plus uncommitted deliverables.

| slot | cell | state found | seated |
|---|---|---|---|
| `~5` | EG-s-26 | branch +2 (code committed), ledger + completion doc STAGED, deploy **world-done** in S3 | re-seat |
| `~4` | EG-s-27 | branch +3 (code committed), 4 deliverables untracked incl. a proof_of_spec.json | re-seat |
| `~1` | EG-s-28 | never spawned; branch tip IS the issuance commit | cold |

**The finding neither the CTO's crash assessment nor the faces carried:** *neither surviving worker
branch contains `d3a33a1189`*, the spine-v3.13 correction that relabelled a DIFFERENCE control on both
faces — and on EG-s-27 that is arm (d), the arm carrying the outcome. Both worktrees held the
pre-correction text. Each re-seat is therefore instructed to merge CLOUD **before** it reads its face,
and the corrected text travels in the prompt.

### 3. Two lane seatings

- **`2.0.0_SA_COO~A` → NFRA_CLDGRPH round 8.** The CTO's round-7 analysis (95091) assigns a five-cell
  recut and was addressed to this live base *to hold and hand over*, because mailing a lane with no
  session reads as delivered and is not. Pre-flight clean on 1pt/1a/1b/1d. Seated 12:15:15Z; registered
  and cutting within two minutes.
- **`0.7.0_AE_CloudOps~W` → NFRA_OUTSET round 3.** Six pending cells, dead executor. See Decisions.

### 4. The 94929 pass, assigned to this seat by the CTO

*"a read of whether any DONE WHEN names a calendar where a history read would do."* **Null result, and
the null is the finding.** ETFS_GUARDRAIL 8 of 8 clear, NFRA_OUTSET 8 of 8 clear. The four that did name
one were already fixed: ETFS FWD-2→FWD-9 and FWD-7→FWD-10 superseded, OUTSET FWD-4 and FWD-5 re-pointed
in v0.10. Domain falsified per the amended Rule 24(i): 12 DONE-WHEN lines in the ETFS PRD minus 2
superseded minus 2 duplicated = 8, matching `endpoint_outcomes` id-for-id.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Drain `wk-etfs_guardrail-3-5` FIRST, ahead of the other two | The served renderer is AHEAD OF THE RECORD: the deploy landed 06:40:10Z and the only commit explaining it lives on a branch in a dead worker's worktree. The box pulls that key fresh on every fire. |
| Tell `~5` the deploy is WORLD-DONE and must not be re-copied | NEVER-2: world-done closes SUPERSEDED; a re-execute of an overtaken promote is a REWIND. |
| **Do NOT seat NFRA_OUTSET on the face count alone** | `/mstr-spawn` 1d-ii: an `[ACTIVE]` TO is not evidence of unfinished work, and several broker reports claimed the acts had landed. A stale face over finished work makes seating pointless — and re-execution harmful. |
| **Seat it after measuring the ARTIFACT** | 2 proof-of-spec instances exist across the whole project; **zero** belong to the six open cells. The criteria were never proven. Genuinely mid-L7, so the seating is right — and the `--say` says *measure before re-executing*, asserting no work-state I had not measured. |
| Do NOT arm `/drive` | The launch order puts it off by default and admits only a live scoped authorization from the XXX.md Step 1b-F row. None is live. Zero crons armed. |
| Do NOT spawn `3.0.0_SA_CVO` yet | Its L9 is its first engagement and fires at L8. Seating it now buys an idle seat that drifts stale; seating it at the compile costs 40 seconds. |
| Park the audit-invoker vintage test rather than cut or hand it | The owning seat's live scope is NFRA_OUTSET round 3; pulling it off a live round for a non-urgent tooling item would be manufactured churn. Parked with OWNER + UN-PARK CONDITION. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/2.0.0_SA_COO/deliverables/PARKED_20260910_AUDIT_INVOKER_VINTAGE_TEST.md` | New — parked placement, owner + un-park condition | Yes — `1e01703e54` |
| `org/mcp/sessions/<session>.serial`, `.comp-graph/.agent_context` | Startup mechanics | No — local, by design |

---

## ⛔ One process error of my own, recorded because it was mine

I called `ack_messages("95094")` on the `1.0.0_SA_CTO~Y` ferry message. **That id was a guess** — the
message carries no `Msg-ID:` line, being an unregistered sender-unverified send. The call returned
**0 acked** (the id was already acked by its true reader), so nothing false landed on the READ clock. It
was still wrong: the law is *never ack a row you did not open*, and an id inferred from a numbering
pattern is not a row I opened. A ferry message with no Msg-ID cannot be acked from its file, and the
correct act is to leave it unacked.

---

## Blockers

**None at this seat.** The next act — the drain — is gated on three worker reports, which is the spine's
own sequencing and not a stall. Workers write no telemetry, so silence is not evidence of a stall either;
the report and the proof-of-spec instance are the whole oracle.

**Not blocking, at Andrew:** publication. Local CLOUD and `origin/CLOUD` have diverged because the site-Z
fabric worked through this device's reboot.

---

## Next Steps

1. Drain each terminal order through `.tools/safe-merge.sh` so the row gate grades the MERGED index —
   `wk-etfs_guardrail-3-5` first, on the served-ahead-of-record hazard.
2. Seat `3.0.0_SA_CVO` at L8 compile, not before.
3. L10: ONE message to `1.0.0_SA_CTO` carrying the CVO watermark against the channel row count, every
   armed row whose owner I could not seat, and the 94929 null result.
4. Hand `2.0.0_SA_COO~A` nothing further — it holds NFRA_CLDGRPH round 8 and is cutting.
