# audit-archive-invoker -- FINDINGS (append-only)

Durable, human-readable record of every finding the audit-archive-invoker emits: non-append edits
(clause 2), stale baselines (clause 1), invoker death (clause 4), coverage gaps, and snapshot
failures. It states the EDIT, never an opinion on authority (clause 3) -- a human rules on whether an
edit was authorized. Owner: 0.7.0_AE_CloudOps. Gate: 1.0.0_SA_CTO.

This file is itself append-only, mirroring the logs it guards.

Format per entry:

    ## <UTC timestamp> -- <CLAUSE> -- <VERDICT>
    - log: <path>          (when log-scoped)
    - detail: <what was detected>
    - action: <what the invoker did>

<!-- entries append below this line -->

## 2026-07-19T191123Z -- LIVENESS -- STALE-BASELINE
<!-- sig: LIVENESS|STALE-BASELINE||baseline #-#-#T#Z is #.#h old (>#.#h) AND uncaptured tail exists -->
- detail: baseline 2026-07-16T175907Z is 73.2h old (>24.0h) AND uncaptured tail exists
- action: minting fresh snapshot below

## 2026-07-29T015053Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/surface-check-ack-audit.log|listed in manifest but no live file -->
- log: org/surface-check-ack-audit.log
- detail: listed in manifest but no live file

## 2026-07-29T015053Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/mcp/comp-detect-gate-override.log|listed in manifest but no live file -->
- log: org/mcp/comp-detect-gate-override.log
- detail: listed in manifest but no live file

## 2026-07-29T015053Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/mcp/log-open-ok-override.log|listed in manifest but no live file -->
- log: org/mcp/log-open-ok-override.log
- detail: listed in manifest but no live file

## 2026-07-29T015053Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/mcp/orphan-audit.log|listed in manifest but no live file -->
- log: org/mcp/orphan-audit.log
- detail: listed in manifest but no live file

## 2026-07-29T015053Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/tier#/audit/ledger-hook-audit.log|listed in manifest but no live file -->
- log: org/tier0/audit/ledger-hook-audit.log
- detail: listed in manifest but no live file

## 2026-07-29T015053Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/git-author-override-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/git-author-override-audit.log
- detail: non-append edit: first divergence at line 1, col 1 (baseline 1682776B / live-head 67B)
- action: snapshot WITHHELD; baseline NOT advanced; needs human authority ruling (clause 3)

## 2026-07-29T015053Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/surface-check-ack-audit.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\surface-check-ack-audit.log -->
- log: org/surface-check-ack-audit.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\surface-check-ack-audit.log

## 2026-07-29T015053Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/mcp/agent-spawn-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/mcp/agent-spawn-audit.log
- detail: non-append edit: first divergence at line 1, col 7 (baseline 156089B / live-head 217B)
- action: snapshot WITHHELD; baseline NOT advanced; needs human authority ruling (clause 3)

## 2026-07-29T015053Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/mcp/comp-detect-gate-override.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\mcp\comp-detect-gate-override.log -->
- log: org/mcp/comp-detect-gate-override.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\mcp\comp-detect-gate-override.log

## 2026-07-29T015053Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/mcp/comp-which-rail.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/mcp/comp-which-rail.log
- detail: non-append edit: first divergence at line 1, col 7 (baseline 4133122B / live-head 563B)
- action: snapshot WITHHELD; baseline NOT advanced; needs human authority ruling (clause 3)

## 2026-07-29T015053Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/mcp/log-open-ok-override.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\mcp\log-open-ok-override.log -->
- log: org/mcp/log-open-ok-override.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\mcp\log-open-ok-override.log

## 2026-07-29T015053Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/mcp/orphan-audit.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\mcp\orphan-audit.log -->
- log: org/mcp/orphan-audit.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\mcp\orphan-audit.log

## 2026-07-29T015053Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/tier#/audit/ledger-hook-audit.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\tier#\audit\ledger-hook-audit.log -->
- log: org/tier0/audit/ledger-hook-audit.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\tier0\audit\ledger-hook-audit.log
