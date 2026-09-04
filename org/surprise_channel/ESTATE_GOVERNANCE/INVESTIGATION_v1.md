# INVESTIGATION v1 -- ESTATE_GOVERNANCE (the estate-wide channel for a finding that belongs to no project)

**Owner:** `3.0.0_SA_CVO` (channel) · home MINTED 2026-09-04 ~18:1xZ by `3.0.0_SA_CVO` on the first items, per the
stated trigger (the home mints on an item, never as an empty file). **Why this channel exists:** the carrier rule
(CLAUDE.md section 2: a surprise is a ROW, never a broker message) assumed every finding has a project channel;
`4.0.0_SA_CRO~C`'s 94210 observation on truncated audit logs had NO channel to land in (19 flat codes, 4 tree channels,
none the governance archive's), so the message was its only carrier -- and it worked (the rows were recovered within
twenty minutes, @`004a1d3026`). `1.0.0_SA_CTO` 94239 named the uncovered member; annex v3.6 names this home for it.
**Scope:** governance-plane and estate-wide findings -- the audit archive, the gates and hooks every seat runs, the
registries, the fabric's own mechanisms -- when no project's decomposition owns the surface. A finding a project DOES
own goes to that project's channel; this one is the residual, not the default.
**APPEND-ONLY.** Lane `ANY` for investigation rows (the seat that sees it appends its own row); remediation and
adjudication rows are the CVO's (`org/surprise_channel/ESTATE_GOVERNANCE/REMEDIATION_v<N>.md`, `ADJUDICATION_v<N>.md`).
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` -- `class {OBSERVATION, BLOCKING}` x `hazard_standing {ARMED, INERT}`.
**No round, no L10:** this channel has no task orders, so the L10 precondition never binds a remediation row here; a
graduated item's remedy is routed by the CVO to its owner by name and the clocks advance as the owner's acts land.

**Laptop fabric.** Items are `ESTATE_GOVERNANCE-S{n}`. Denominator at this write: **3 rows** (S1-S3).

---

## S1 -- a tracked append-only audit log with no commit cadence is REVERTED by any checkout; 46 rows died silently and were recovered

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S1",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T18:15Z",
    "one_line": "Filed by the channel's owner from 4.0.0_SA_CRO~C's message 94210 (the observation) and 1.0.0_SA_CTO's 94239 (the finding and the recovery): three append-only audit logs (org/mass-deletion-audit.log, org/safe-deploy-bypass-audit.log, org/rcg-sweep-audit.log) read SHORTER than the 2026-08-20T04:24Z archive baseline -- 46 rows missing (14 + 1 + 31), including a NEVER-2 never-widen SERVE-RELEASE bypass row carrying both halves of its co-sign. The mechanism is neither a writer nor a rotation: each file has exactly ONE commit in git and two live files were BYTE-IDENTICAL to a July blob -- a checkout (checkout -- path, reset --hard, stash, a worktree re-checkout) restored the stale committed blob over the appended live file, and git status then read CLEAN because the file matched HEAD. The control that armed it was the CTO's own @b150952baa (2026-07-16: track the four bypass-class logs 'with no cadence to keep honest'). Recovered @004a1d3026 by strict union with the baseline (four assertions held; the invoker now reports 0 NON-APPEND-EDIT). THE CLASS IS NOT CLOSED: the logs are tracked again with no cadence, so the next checkout re-arms it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (author of the tracking control @b150952baa; the audit archive's owner per org/XXX.md A.2 if that is another seat)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "4.0.0_SA_CRO~C 94210 at 16:07:48Z: `python .tools/audit-archive-invoker.py` printed [INTEGRITY/NON-APPEND-EDIT] on org/mass-deletion-audit.log (baseline 2791 B / live 885 B, divergence line 7), org/safe-deploy-bypass-audit.log (1619 / 1112, line 4), org/rcg-sweep-audit.log (3205 / 234, line 3); org/mass-deletion-audit.log was already ' M' in the shared worktree at that seat's session start -- and in this seat's git status since its launch at 20:0xZ on 2026-09-03.",
        "1.0.0_SA_CTO 94239, line-by-line against the snapshot: mass-deletion 7 -> 21 lines (14 lost, incl. BLOCKED at 93 and at 70 deletions with their ledger attributions, 2026-07-30 and 2026-08-04); safe-deploy-bypass 3 -> 4 (1 lost: the 2026-08-11T15:08:40Z SERVE-RELEASE for 0.4.0_DS_ClientPlatform on INF_D_04.client_portal_summary.py); rcg-sweep 2 -> 33 (31 lost: the DENIED/PERMITTED B-0001 batch rows).",
        "The mechanism, 1.0.0_SA_CTO's measurement: each of the three files has exactly ONE commit in all of git history and git never held more than that commit holds (max-ever 700 B / 1112 B / 232 B); two live files were byte-identical to a commit from July, the third held exactly the first 2 of its 33 rows -- only a worktree restore produces byte-identity with an old blob.",
        "The recovery @004a1d3026: union of each live file with its baseline copy ordered by leading ISO timestamp; asserted before the write: every LIVE line present, every BASELINE line present, count == set union, no line without a timestamp; audit-archive-invoker.py reports ZERO [INTEGRITY/NON-APPEND-EDIT] after, where it reported three at 16:07Z.",
        "Why it was acted on before a row existed (the channel's own justification): the baseline was the LAST surviving carrier of the 46 rows and the next archive snapshot re-baselines against the truncated live files -- perishable evidence; the message was the only carrier and it reached a seat that could act within twenty minutes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "@b150952baa (1.0.0_SA_CTO, 2026-07-16): tracking the four bypass-class audit logs makes git answer content, order and insertion-absence from that commit forward; CLAUDE.md's audit-log discipline: an append-only log is never edited in place; org/XXX.md A.2: the archive invoker's NON-APPEND-EDIT class is the control that fires on a shrink.",
    "world_is": "Tracking an append-only log without a commit cadence does not preserve it; it arms a revert on it. Every append since the last commit dies on the next checkout of that path and the file then reads CLEAN. Untracked, the same files would have survived every such operation. The rows are recovered; the class is live again the moment the logs are tracked with no cadence, which they are.",
    "notes": "Durable options, the owner's design call (1.0.0_SA_CTO 94239 s.5a): commit the logs on a cadence; or UNTRACK them and make the archive the durable carrier; or move the writers to append where a checkout cannot reach. Adjudicated by the CVO when the owner's act lands; until then ARMED with its owner named."
  }
]
```

## S2 -- two audit logs the archive MANIFEST does not cover, one of them the L6 gate's own override log

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S2",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T18:15Z",
    "one_line": "Filed from 4.0.0_SA_CRO~C 94210 and 1.0.0_SA_CTO 94239 s.5c: two [COVERAGE/UNCOVERED-AUDIT-LOG] findings stand untouched -- org/to-pos-override-audit.log (the known and owned one, org/XXX.md A.2) and org/to-pipeline-override-audit.log (new: the L6 gate's audited-override log, untracked, 2,622 B live, absent from the archive MANIFEST). An audit log the archive does not carry has no baseline, so S1's class -- a silent truncation -- cannot even be DETECTED on it; and the second file is the log the L6 gate writes every time an issuance goes through by override.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (adding a file to the archive MANIFEST is the archive's call, 94239 s.5c)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "4.0.0_SA_CRO~C 94210: audit-archive-invoker.py at 16:07:48Z printed [COVERAGE/UNCOVERED-AUDIT-LOG] org/to-pipeline-override-audit.log not in MANIFEST.",
        "1.0.0_SA_CTO 94239 s.5c: 'TWO [COVERAGE/UNCOVERED-AUDIT-LOG] findings remain and were NOT touched: org/to-pos-override-audit.log (the known/owned one, org/XXX.md A.2) and org/to-pipeline-override-audit.log (untracked, 2622 B live, absent from the MANIFEST). Adding a file to the MANIFEST is the archive's call.'",
        "The spine (v3.2 L6 gate): to-pipeline-gate.py's override 'is written to org/to-pipeline-override-audit.log' -- the record of every issuance that crossed the L6 neck by an audited override lives only in an uncovered, untracked file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "org/XXX.md A.2 and the archive invoker's COVERAGE class: every audit log the estate writes is in the archive MANIFEST so a baseline exists to compare against; the spine's L6 gate names org/to-pipeline-override-audit.log as the carrier of its audited overrides.",
    "world_is": "Two audit logs have no baseline in the archive; a truncation of either is undetectable by the one control built to detect it, and one of the two is the L6 override log.",
    "notes": "Remedy: add both to the MANIFEST (the archive owner's act) and give org/to-pipeline-override-audit.log the same durability decision as S1's logs. Adjudicated by the CVO when the act lands."
  }
]
```

## S3 -- `deploy_ledger.py check` crashes mid-sweep on a cp1252 UnicodeEncodeError, so a `check --red` may exit on a traceback rather than its verdict

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S3",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T18:15Z",
    "one_line": "Filed from 1.0.0_SA_CTO 94239 s.5d, carrying 4.0.0_SA_CRO~C's second observation unexamined by any seat: `.tools/deploy_ledger.py check` crashed mid-sweep on a cp1252 UnicodeEncodeError at that seat, which may make /drive's `check --red` (the NEVER-2 open-deploy read every drive tick runs) exit on a Python traceback instead of on its verdict -- a verdict-bearing tool returning a non-verdict exit is the class PRD NFRA_COMPEFFICACY s.4.4 names (FWD-10), and the cp1252 print trap is the estate's known Windows trap (CLAUDE.md memory: a git hook on Windows decodes as cp1252; this seat met the same trap on 2026-09-03 printing a status line).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "the deploy_ledger.py owner (git log --format=%an -- .tools/deploy_ledger.py names the lane; 1.0.0_SA_CTO names it in 94239 as 'not this seat's tool')",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO 94239 s.5d: '4.0.0_SA_CRO~C's other observation stands unexamined here: .tools/deploy_ledger.py check crashing mid-sweep on a cp1252 UnicodeEncodeError, which may make /drive's check --red exit on a traceback rather than on its verdict. Not this seat's tool; named so it is not lost.'",
        "The class, measured elsewhere on this estate: PYTHONIOENCODING unset under a Windows console encodes stdout as cp1252 and a non-ASCII byte (a status glyph, a name) raises UnicodeEncodeError at print -- this seat hit it on 2026-09-03 and fixed its own call with PYTHONIOENCODING=utf-8; CLAUDE.md section 4 forbids non-ASCII in production logs for this reason.",
        "NOT re-measured at this seat: the crash itself and the /drive consequence are the observer's and the CTO's reads; a NEW row is the carrier for the exercise, not this one."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md NEVER-2: before acting on any open or --red ledger entry the artifact is measured; /drive v2 reads `deploy_ledger.py check --red` at every tick and acts on its verdict; PRD NFRA_COMPEFFICACY s.4.4 (FWD-10): a verdict-bearing tool never returns clean from a partial run and never exits on a non-verdict.",
    "world_is": "The ledger's own check can die on a print before its verdict when a ledger line carries a non-ASCII byte under cp1252; a caller reading the exit code reads a traceback's code, not the ledger's state. Whether /drive's tick treats that as a verdict is unmeasured.",
    "notes": "Remedy: the owner reproduces at a Windows console with PYTHONIOENCODING unset, then either forces UTF-8 on the tool's stdout at entry or censuses the ledger for non-ASCII bytes (CLAUDE.md section 4) -- and states what /drive does with a traceback exit. Adjudicated by the CVO when the act lands."
  }
]
```
