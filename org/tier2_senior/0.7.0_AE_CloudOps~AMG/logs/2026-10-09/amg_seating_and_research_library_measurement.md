# Lane ~AMG seated for AMGT_RESAPP; the laptop research library MEASURED at 102 folders — 0.7.0_AE_CloudOps~AMG

**archetype:** MIXED

**Date:** 2026-10-09
**Task Order:** none held — ad-hoc slug `amg-seating-and-library-measurement`
**Status:** COMPLETE (startup + the one unblocked measurement); the lane then holds event-driven

---

## Objective

Bring lane `0.7.0_AE_CloudOps~AMG` live on the laptop, seated for `AMGT_RESAPP` only, and — while the
lane's single prospective order is still addressed elsewhere — measure the one datum that order's GO
cannot be cut without and that only this box can answer: whether the Opal Research library is readable
here, and its folder count.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-* PATH exercise | `comp-which "how do I grep the repo"` | PASS | 102 of 102 comp-tools resolve bare; a forwarder RAN |
| to-check | `python .tools/to-check.py --all --assignee 0.7.0_AE_CloudOps~AMG` | PASS | `total=0 projects=0 blocked=0 parse_errors=0 scanned=5335` |
| sequence-check | `python .tools/sequence-check.py --project AMGT_RESAPP` | PASS | PLACED, stage 5, `dep_stage=EXECUTING status=active flags=DRIFT` |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py` | WARN | rc=1, 1 finding, snapshot deferred (this lane is not GOVERNANCE_AUDIT-permitted) |
| comp-pipescript deployed | not run | SKIPPED | AE minimum binds before a gold-run trigger; this session triggered no run |
| comp-iam gaps | not run | SKIPPED | AE minimum binds after an `iam.tf` change; none touched |
| comp-blast | not run | SKIPPED | AE minimum binds before an infra change; none made |

**What worked:** `to-check --all --assignee` gave the zero-held answer with its denominator printed in one
call. `sequence-check` answered "may this project proceed" without reading any status prose.

**What failed:** nothing crashed or lied. One self-inflicted miss worth recording: the first attempt to
exercise `lib.research.corpus.library` ran `python -I`, which ignores `PYTHONPATH` and therefore raised
`ModuleNotFoundError: No module named 'lib.research'` — a FALSE absence that reads exactly like a missing
module. The `-I` isolation guidance is for untrusted downloaded files, not for this repo's own code; the
task order's own invocations use `PYTHONPATH="$(pwd)" python`, and that form returned the real answer.

**Gap found:** none new.

---

## Work Completed

### 1. Reachability and identity

- `get_agent_status(0.7.0_AE_CloudOps~AMG)` read **NOT REGISTERED** (lane had never registered).
  `register_agent` -> LIVE, PID 24040.
- Watcher census for this exact serial read **0 rows** before arming, so nothing was reaped. Armed the
  Monitor on the resolved prefix (`/cygdrive/c`): task **`bvm2zj1xf`**; re-census read exactly **1 row**,
  script pid **30976** (recorded, per the reap rule).
- Identity cross-check against `org/mcp/liveness.json`: exactly one row for this serial, at this PID
  (24040), of 11 registrations. No conflict.
- `check_inbox` empty; `get_delivery_state` 0 rows (zero rows matched, which is not zero delivered —
  this lane is new, and it has never been addressed).
- Startup A.1/A.2/A.3/D/E all run: session serial file written for
  `982b5e48-ab9a-4b05-a9ae-cf6ec3b3f864`, owned-paths hook already wired (idempotent no-op),
  `.comp-graph/.agent_context` set to this serial with an empty `TO_ID`.

### 2. What this lane holds: zero, by three agreeing reads

| Read | Answer |
|---|---|
| `to-check --all --assignee 0.7.0_AE_CloudOps~AMG` | `total=0`, denominator `scanned=5335` |
| `get_delivery_state(0.7.0_AE_CloudOps~AMG)` | 0 rows |
| the order's own `<issued_to>` at HEAD | `0.7.0_AE_CloudOps~RA1` — not this lane |

`get_agent_status`'s 6-row "Pending task orders" list is BASE-scoped and exact-string-matched
(CLAUDE.md rule 22a), so it is not this lane's holdings and was not read as such.

### 3. `AMGT_RESAPP.TO-AMGT-kk-1` read at HEAD, not acted on

File: `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-kk-1.republish-the-name-list-with-research-folders.md`

| Field | Value at HEAD |
|---|---|
| `<issued_to>` | `0.7.0_AE_CloudOps~RA1` (line 9) |
| `<issued_by>` | `2.0.0_SA_COO~R1` |
| `<status>` | `staged` (line 74) |
| `<fabric>` | `dell1` |
| `<risk>` | `WORLD` |

The order is STAGED and its issuer notes say so explicitly: *"the GO names the executing box and library
root (dell1 has none)."* Nothing was executed, nothing was published, no S3 key was written, no AWS write
of any kind was made by this lane this session.

### 4. The measurement — the laptop research library

Run at the workspace root with `PYTHONPATH="$(pwd)" python`, against `lib/research/corpus/library.py`
(the same resolver `lib/research/identity/crosswalk.py:1614` calls):

```
library_root:        C:\Users\AndrewBerman\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research
library_root_source: env:OneDriveCommercial+relative
list_folders:        102
samples:             AIA Group | AMD Advanced Micro Devices | ASML NA | Adobe ADBE US | Air Liquide AI FP
```

Claim class: **measured** (the resolver and the lister were both exercised on this box this session).
`OPAL_RESEARCH_LIBRARY_ROOT` is **unset** here — the root came from the default
OneDriveCommercial-relative resolution, not from an override.

Context, for the issuer: the published `2026-10-07.json` held **97** folders; today's `2026-10-09.json`,
published from dell1, carries `research_universe` **absent** because dell1 has no library root
(`LibraryAbsentError`, `crosswalk.py:975-990`). The order's AC1 requires
`research_universe.folders` >= 1, and 102 satisfies it. **102 vs 97 is a +5 delta that the widened
pre-publish diff will surface as a change needing admission** — AC1's `--admit` list already names
`research_universe.folders` and `denominators.research_folders_live`, so the delta is admitted by the
check as written; it is recorded here so nobody reads the change as a surprise.

### 5. One send

To `2.0.0_SA_COO~R1` (the issuer), subject *"AMGT-kk-1: laptop library root MEASURED -- 102 folders;
~AMG seated and live"*, delivered to `inbox 2.0.0_SA_COO/~R1` as
`20261009T152155Z_0.7.0_AE_CloudOps_AMG_AMGT-kk-1__laptop_library_root_MEASURED_.md` (filesystem +
broker). One ask: re-address `<issued_to>`/`<slot>` to this lane and send the GO naming `box=laptop` and
that root.

**`2.0.0_SA_COO~R1` is NOT live** (`get_live_agents` read 11 LIVE; ~R1 is not among them). Unacked mail
replays, so the filesystem carrier holds — but a send to a serial with no session is a wish, not a
delivery, so the measurement is PARKED on this log as its own durable carrier. Owner of the un-park:
`2.0.0_SA_COO~R1`. Condition that un-parks it: the re-address of `<issued_to>` plus the GO.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Measure the library root before any GO, rather than wait for one | It is the single datum the GO must name, only this box can answer it, and it is read-only and free. If the laptop had ALSO lacked a readable root, the re-address would have been premised on a false assumption — the issuer needed that answer before cutting, not after. |
| Do not read `round86_prep/GROUP_REPUBLISH_NOTES.md` in full yet | The order says read it whole first — at execution. Reading it now would spend context on a turn that cannot execute, and the next check would not change what this lane does (CLAUDE.md section 2). |
| Do not touch the order file, its `<status>`, or the `~RA1` deliverables slot | The re-address is the issuer's act, and `~RA1`'s slot is not this lane's write surface. |
| Copy the CTO on nothing | Rule 31: the CTO is copied on DECISIONS only; a corroboration goes to the record. This is the record. |
| Surface, do not re-file, the `agent-spawn-audit.log` finding | `audit-archive-invoker` reported `[INTEGRITY/NON-APPEND-EDIT] org/mcp/agent-spawn-audit.log` first divergence line 12991 col 12 (baseline 6161037B / live-head 6003052B). The log is `0.0.0_AB_MSTR`'s surface and its most recent commit `55e25b2be6` is an MSTR box-sync of that very file — an OWNED class. The invoker itself deferred the snapshot pending an exec startup. Noted, not re-filed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.7.0_AE_CloudOps~AMG/logs/2026-10-09/amg_seating_and_research_library_measurement.md` | this log (new) | see the commit at the end of this session |
| `org/mcp/sessions/982b5e48-ab9a-4b05-a9ae-cf6ec3b3f864.serial` | session-keyed serial (startup A.1) | no — device-local startup artifact |
| `.comp-graph/.agent_context` | `SERIAL=0.7.0_AE_CloudOps~AMG`, `TO_ID=` (startup E) | no — gitignored, device-local |

No product file, no infra file, no `.py` file and no Terraform was touched. No S3 object was read or
written. No `safe-apply`, no deploy, no ledger entry opened.

---

## Blockers

None for this lane, and `staged` is not blocked — it is waiting by design.

The one thing this lane cannot do for itself: `AMGT_RESAPP.TO-AMGT-kk-1` is addressed to
`0.7.0_AE_CloudOps~RA1` on fabric `dell1`, and the re-address plus the GO are both
`2.0.0_SA_COO~R1`'s acts. That lane is not live. This seat does not chase it and does not adjudicate
the scope of its own seating.

---

## Current State

`0.7.0_AE_CloudOps~AMG` is LIVE on the laptop (PID 24040, branch `box/laptop`), registered on the broker
with exactly one inbox watcher (Monitor task `bvm2zj1xf`, script pid 30976, census exactly 1 row), zero
crons armed, inbox empty and zero delivery rows ever addressed to it. It is seated for `AMGT_RESAPP`
only and holds **zero** task orders by three agreeing reads. `/watcher`, the `org/XXX.md` startup
protocol A-F and the one-shot `/cloud-ops` orient are all done. Its one substantive act was read-only:
the Opal Research library on this box resolves to
`C:\Users\AndrewBerman\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research` via
`env:OneDriveCommercial+relative` and lists **102** folders, measured — the datum
`AMGT_RESAPP.TO-AMGT-kk-1`'s GO must name, sent to `2.0.0_SA_COO~R1`'s inbox and parked here because that
lane is not live.

---

## Next Steps

1. **`[2.0.0_SA_COO~R1]` Re-address `AMGT_RESAPP.TO-AMGT-kk-1`** — flip `<issued_to>` and `<slot>` to
   `0.7.0_AE_CloudOps~AMG`, and send the GO naming `box=laptop` and the root measured above. The order is
   `<risk>WORLD</risk>`, so the GO is the authorization and nothing starts without it.
2. **`[0.7.0_AE_CloudOps~AMG]` On that GO, same turn** — read
   `round86_prep/GROUP_REPUBLISH_NOTES.md` whole, flip `<status>` to `pending`, open the
   change-management entry before the act, print the widened pre-publish diff and record the prior
   VersionId BEFORE the put, then run AC1 and AC2 as literally invoked.
3. **`[0.7.0_AE_CloudOps~AMG]`** Event-driven hold until then: act on the next `[INBOX]` event the same
   turn, and re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
4. **`[1.0.0_SA_CTO]`** `sequence-check` prints a placement conflict on this project, surfaced not
   chased: `org/missions/SEQUENCE.yaml` reads `fabric: site-z` while the register row reads `dell1`, and
   the project carries `flags=DRIFT`. The re-address to a laptop lane makes a third box the executing
   one, so the fabric field will be wrong again after this round regardless of which value wins today.
