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

## 2026-07-29T124741Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/mcp/orphan-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/mcp/orphan-audit.log
- detail: non-append edit: first divergence at line 1, col 7 (baseline 21412B / live-head 113B)
- action: snapshot WITHHELD; baseline NOT advanced; needs human authority ruling (clause 3)

## 2026-07-29T124741Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/tier#/audit/ledger-hook-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/tier0/audit/ledger-hook-audit.log
- detail: non-append edit: first divergence at line 1, col 7 (baseline 1089273B / live-head 2240B)
- action: snapshot WITHHELD; baseline NOT advanced; needs human authority ruling (clause 3)

## 2026-07-29T180912Z -- SNAPSHOT-FAILURE -- COMMIT-FAILED
<!-- sig: SNAPSHOT-FAILURE|COMMIT-FAILED||safe-commit rc=# (non-lane): ory, or the lock file may be stale
error: pathspec 'org/audit/archive/#-#-#T#Z' did not match any file(s) known to git
error: pathspec ':(exclude,glob)**/__pycache__/**' did not match any file(s) known to git
error: pathspec ':(exclude,glob)**/*.pyc' did not match any file(s) known to git
 -->
- detail: safe-commit rc=1 (non-lane): ory, or the lock file may be stale
error: pathspec 'org/audit/archive/2026-07-29T180912Z' did not match any file(s) known to git
error: pathspec ':(exclude,glob)**/__pycache__/**' did not match any file(s) known to git
error: pathspec ':(exclude,glob)**/*.pyc' did not match any file(s) known to git

- note: distinct from DEATH: the invoker RAN, the commit failed

<!-- ===================================================================================== -->
<!-- HUMAN ANNOTATION -- deliberately carries NO "sig:" marker. emit() (audit-archive-      -->
<!-- invoker.py:256) builds its idempotency set from sig markers ONLY, so an annotation     -->
<!-- without one is invisible to it and cannot suppress a future genuine finding. Do NOT    -->
<!-- add a sig line to a hand-written block here: a matching sig would silently swallow the -->
<!-- real finding it resembles.                                                             -->
<!-- ===================================================================================== -->

## 2026-07-29T234500Z -- ANNOTATION (human) -- DEVICE-PROVENANCE OF THE SITE-Z FINDING BATCHES

- author: 1.0.0_SA_CTO~Z (gate owner for this instrument; RV-0057 F-002 names 1.0.0_SA_CTO)
- scope: the 2026-07-29T015053Z batch (commits 426da9d8e, 4982db745) and every future site-Z batch
- verdict: **THE INTEGRITY AND COVERAGE FINDINGS EMITTED FROM SITE Z ARE FALSE POSITIVES OF A
  KEYING DEFECT, NOT TAMPER EVENTS. Do not rule on them as authority questions (clause 3).**

- mechanism (source-confirmed, .tools/audit-archive-invoker.py @935ca2a7d): the archive is keyed on
  (timestamp, logical-log). It has NO device dimension -- :99-108 parses each archive child dir as a
  bare timestamp, :185 resolves the baseline as ARCHIVE/ts, and a grep of the whole file for
  hostname|device|uname|platform|node() returns two hits, both comments, both reading "single-host".
  The baseline chain is laptop-minted (2026-07-29T185938Z by 1.0.0_SA_CTO~A). Site Z therefore diffs
  its OWN live logs against a FOREIGN device's baseline, so every covered log diverges at line 1 BY
  CONSTRUCTION. Sizes confirm different files rather than edited ones: git-author-override 12,055B
  live vs 1,702,822B baseline; ledger-hook 5,350B vs 1,131,812B; comp-which-rail 4,609B vs
  4,498,159B.

- the tell is already in this file, and it was written by accident: the ERROR-FAILCLOSED entries
  above carry the string
  "live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\surface-check-ack-audit.log".
  That is a SITE-Z absolute path, in the shared governance record, inside a finding that reads as a
  fabric-wide integrity event. The instrument leaks its device provenance only on failure and only
  by accident. Under the fix it will carry it deliberately, on every entry.

- SCOPE BOUND -- READ THIS BEFORE REUSING THE EXPLANATION: this annotation covers SITE-Z-EMITTED
  batches ONLY. It must NOT be allowed to absorb any laptop-side integrity event. RV-0057 Amendment
  1b records a separate laptop-side observation (git-author-override 1696149B -> 12917B, diverging
  at byte one, reported by 1.0.0_SA_CTO~B on the LAPTOP) which this device-keying mechanism does NOT
  explain and which is NOT determinable from site Z. **It remains OPEN AND UNOWNED.** A tidy
  explanation that quietly covers an event it does not actually explain is a false all-clear, and a
  false all-clear on audit integrity is worse than the false alarm it replaces, because nothing
  later re-raises it.

- also NOT covered: the three COVERAGE / MANIFEST-ENTRY-MISSING-LIVE entries are device-scoped too
  (org/surface-check-ack-audit.log is 11,191B in the laptop baseline and simply absent on this
  disk), but the manifest itself is correct and global. Do not remove a manifest line to silence
  them -- MANIFEST.txt's own header says removing a live log's line severs its durability.

- disposition: fix the KEY, keep every detector. Design: docs/architecture/NFRA_AUDITDEV_PRD.md
  @e05fad4f3. Build TO (STAGED, gated behind the /mstr-review reader guard):
  org/tier2_senior/0.7.0_AE_CloudOps/task_orders/rv0057-f001-device-key-the-audit-archive.md
  RV-0057 F-002's stated remedy -- "suppress or device-scope the INTEGRITY clause" -- is REFUSED at
  the gate in its suppression half: it deletes a real tamper detector to silence a keying bug, and
  it is under-scoped besides (5 of the 11 findings are COVERAGE, not INTEGRITY).

- NOT retracted, on purpose: the batches above stay in this append-only file. This annotation states
  what they mean; it does not erase them. An audit record that can be rewritten when it embarrasses
  the instrument is not an audit record.

## 2026-07-31T011725Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/tombstone-gate-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/tombstone-gate-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-07-31T023827Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/mass-deletion-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/mass-deletion-audit.log
- detail: non-append edit: first divergence at line 1, col 112 (baseline 700B / live-head 706B)
- action: THIS log PINNED at its prior baseline (evidence preserved, still FIRING); other covered logs continue to archive. Needs human authority ruling (clause 3).

## 2026-08-03T150524Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/mass-deletion-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/mass-deletion-audit.log
- detail: non-append edit: first divergence at line 7, col 1 (baseline 1014B / live-head 700B)
- action: THIS log PINNED at its prior baseline (evidence preserved, still FIRING); other covered logs continue to archive. Needs human authority ruling (clause 3).

## 2026-08-03T223815Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/tombstone-gate-audit.log|baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_tombstone-gate-audit.log -->
- log: org/tombstone-gate-audit.log
- detail: baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\2026-08-03T143634Z\org_tombstone-gate-audit.log

## 2026-08-04T013510Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/rcg-sweep-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/rcg-sweep-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-08-04T022827Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/rcg-sweep-audit.log|baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_rcg-sweep-audit.log -->
- log: org/rcg-sweep-audit.log
- detail: baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\2026-08-03T143634Z\org_rcg-sweep-audit.log

## 2026-08-04T151847Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/pipescript-suite-gate-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/pipescript-suite-gate-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-08-04T213358Z -- SNAPSHOT-FAILURE -- COMMIT-FAILED
<!-- sig: SNAPSHOT-FAILURE|COMMIT-FAILED||safe-commit rc=# (non-lane): arter-hard-block-audit.log', LF will be replaced by CRLF the next time Git touches it
BLOCKED (mstr-ledger-check): strategic MSTR commit touches non-record paths but includes no Decision Ledger entry (org/tier#/ledger/LD-*.md). Constitution Art. V: every commitment is ledgered before it propagates.
 -->
- detail: safe-commit rc=1 (non-lane): arter-hard-block-audit.log', LF will be replaced by CRLF the next time Git touches it
BLOCKED (mstr-ledger-check): strategic MSTR commit touches non-record paths but includes no Decision Ledger entry (org/tier0/ledger/LD-*.md). Constitution Art. V: every commitment is ledgered before it propagates.

- note: distinct from DEATH: the invoker RAN, the commit failed

## 2026-08-05T141801Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/rcg-sweep-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/rcg-sweep-audit.log
- detail: non-append edit: first divergence at line 1, col 118 (baseline 2376B / live-head 2400B)
- action: THIS log PINNED at its prior baseline (evidence preserved, still FIRING); other covered logs continue to archive. Needs human authority ruling (clause 3).

## 2026-08-06T125117Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/pipescript-suite-gate-audit.log|baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_pipescript-suite-gate-audit.log -->
- log: org/pipescript-suite-gate-audit.log
- detail: baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\2026-08-05T124743Z\org_pipescript-suite-gate-audit.log

## 2026-08-06T173626Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/pipescript-suite-gate-audit.log|listed in manifest but no live file -->
- log: org/pipescript-suite-gate-audit.log
- detail: listed in manifest but no live file

## 2026-08-06T173626Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/pipescript-suite-gate-audit.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\pipescript-suite-gate-audit.log -->
- log: org/pipescript-suite-gate-audit.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\pipescript-suite-gate-audit.log

## 2026-08-06T173626Z -- DEATH -- INVOKER-SILENT-WITH-CHURN
<!-- sig: DEATH|INVOKER-SILENT-WITH-CHURN||last run #-#-#T#Z (#.#h ago) and covered logs grew since -- uncaptured churn -->
- detail: last run 2026-08-03T150524Z (74.5h ago) and covered logs grew since -- uncaptured churn
- prior_outcome: not-due: no uncaptured tail on any clean log

## 2026-08-11T191319Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/jq-ban-override-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/jq-ban-override-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-08-13T215811Z -- INTEGRITY -- NON-APPEND-EDIT
<!-- sig: INTEGRITY|NON-APPEND-EDIT|org/safe-deploy-bypass-audit.log|non-append edit: first divergence at line #, col # (baseline #B / live-head #B) -->
- log: org/safe-deploy-bypass-audit.log
- detail: non-append edit: first divergence at line 4, col 1 (baseline 1619B / live-head 1112B)
- action: THIS log PINNED at its prior baseline (evidence preserved, still FIRING); other covered logs continue to archive. Needs human authority ruling (clause 3).

## 2026-08-19T115721Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/jq-ban-override-audit.log|baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_jq-ban-override-audit.log -->
- log: org/jq-ban-override-audit.log
- detail: baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\2026-08-18T125017Z\org_jq-ban-override-audit.log

## 2026-08-19T191917Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/jq-ban-override-audit.log|listed in manifest but no live file -->
- log: org/jq-ban-override-audit.log
- detail: listed in manifest but no live file

## 2026-08-19T191917Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/jq-ban-override-audit.log|live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\jq-ban-override-audit.log -->
- log: org/jq-ban-override-audit.log
- detail: live missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\jq-ban-override-audit.log

## 2026-09-01T214550Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/commit-msg-ascii-override-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/commit-msg-ascii-override-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-09-03T064251Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/to-pos-override-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/to-pos-override-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-09-03T135828Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/to-pipeline-override-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/to-pipeline-override-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-09-05T095621Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/to-pos-override-audit.log|baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_to-pos-override-audit.log -->
- log: org/to-pos-override-audit.log
- detail: baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\2026-08-20T042433Z\org_to-pos-override-audit.log

## 2026-09-05T095621Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/to-pipeline-override-audit.log|baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_to-pipeline-override-audit.log -->
- log: org/to-pipeline-override-audit.log
- detail: baseline missing: C:\Users\AndrewBerman\Desktop\ajb_workspace\org\audit\archive\2026-08-20T042433Z\org_to-pipeline-override-audit.log

## 2026-09-09T131729Z -- COVERAGE -- UNCOVERED-AUDIT-LOG
<!-- sig: COVERAGE|UNCOVERED-AUDIT-LOG|org/opal-ipblock-audit.log|audit-log-shaped file not in MANIFEST -- review + add or exclude -->
- log: org/opal-ipblock-audit.log
- detail: audit-log-shaped file not in MANIFEST -- review + add or exclude

## 2026-09-10T045739Z -- COVERAGE -- MANIFEST-ENTRY-MISSING-LIVE
<!-- sig: COVERAGE|MANIFEST-ENTRY-MISSING-LIVE|org/to-pos-override-audit.log|listed in manifest but no live file -->
- log: org/to-pos-override-audit.log
- detail: listed in manifest but no live file

## 2026-09-10T045739Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/to-pos-override-audit.log|baseline missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_to-pos-override-audit.log -->
- log: org/to-pos-override-audit.log
- detail: baseline missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\audit\archive\2026-08-20T042433Z\org_to-pos-override-audit.log

## 2026-09-10T045739Z -- INTEGRITY -- ERROR-FAILCLOSED
<!-- sig: INTEGRITY|ERROR-FAILCLOSED|org/to-pipeline-override-audit.log|baseline missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\audit\archive\#-#-#T#Z\org_to-pipeline-override-audit.log -->
- log: org/to-pipeline-override-audit.log
- detail: baseline missing: C:\Users\Opal Bloomberg\Desktop\ajb_workspace\org\audit\archive\2026-08-20T042433Z\org_to-pipeline-override-audit.log
