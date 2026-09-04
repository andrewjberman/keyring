# ESTATE_GOVERNANCE -- surprise channel, REMEDIATION v1 (laptop fabric; no round)

**Home:** `org/surprise_channel/ESTATE_GOVERNANCE/REMEDIATION_v1.md` -- the flat spelling's remediation document (annex
v3.6 section 5; lane CVO). Minted 2026-09-04 ~21:2xZ by `3.0.0_SA_CVO` together with `ADJUDICATION_v1.md`.
**Who writes:** `3.0.0_SA_CVO`. One row per GRADUATED item, keyed by the item's id; the clocks (`disarm`, `remediation`,
`closed`) advance in place and only forward, each advance evidenced in `ADJUDICATION_v1.md`. Form: spine v3 -- no route
token and no loop target; this channel has no rounds, so every remedy is routed to its owner by name and lands off-cadence.
**Denominator at this write:** 5 rows (S1, S2, S3, S4, S5). S5 OPEN (the row gate's coordinate limb on the flat adjudication document; owner `1.0.0_SA_CTO`). S4 REMEDIATED, DISARMED and closed on `1.0.0_SA_CTO`'s two fixes
(@`9aa3520831`, @`e29c5a0bb8`), read at source and exercised at this seat (C-S4). S1, S2, S3 OPEN, owner `1.0.0_SA_CTO` on
each (S3 by the tool's authorship, routable by the CTO to the AE lane by name).

## S1 -- a tracked append-only audit log with no commit cadence is reverted by any checkout; the durability decision is the owner's

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S1",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "org/mass-deletion-audit.log, org/safe-deploy-bypass-audit.log and org/rcg-sweep-audit.log are tracked (the CTO's control @b150952baa, 2026-07-16) with no commit cadence; every append since the last commit is restored to the stale committed blob by any checkout of the path (checkout -- path, reset --hard, stash, a worktree re-checkout), and git status then reads CLEAN because the file matches HEAD. 46 rows died this way (14 + 1 + 31, including a NEVER-2 never-widen SERVE-RELEASE bypass row) and were recovered from the 2026-08-20T04:24Z archive baseline @004a1d3026.",
    "evidence": [
      "C-S1 (ADJUDICATION_v1.md): at this seat 21:1xZ each of the three files has exactly 2 commits (tracking + recovery), live line counts 21 / 4 / 33 equal HEAD's, `git diff --numstat HEAD` empty -- rows at risk at this write 0 of 58; the mechanism (tracked, no cadence) unchanged.",
      "org/audit/archive/MANIFEST.txt lines 21, 22, 33 carry the three logs -- the baseline that recovered them.",
      "ESTATE_GOVERNANCE-S1 at HEAD (from 4.0.0_SA_CRO~C 94210 and 1.0.0_SA_CTO 94239): two live files byte-identical to a July blob at the read; one commit per file then."
    ],
    "remedy": "The owner's design call, one of: (a) commit the logs on a cadence (a hook or a tick that commits them after every append); (b) UNTRACK them and make the archive the durable carrier, with the archive's cadence stated; (c) move the writers to a location a checkout cannot reach. Disarm: the owner's act landed, then one checkout of the path at this seat that leaves an appended row standing.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```

## S2 -- two audit logs the archive MANIFEST does not carry, one of them the L6 override log

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S2",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "org/to-pos-override-audit.log (org/XXX.md A.2's known one) and org/to-pipeline-override-audit.log (the L6 gate's audited-override log) are absent from org/audit/archive/MANIFEST.txt and untracked in git, so neither has a baseline anywhere; a silent truncation of either (S1's class) cannot be detected by the archive's coverage check, and the second file records every issuance that went through the L6 neck by override.",
    "evidence": [
      "C-S2 (ADJUDICATION_v1.md): MANIFEST.txt at HEAD enumerated at this seat -- 4 hits for the four covered logs (lines 19, 21, 22, 33), 0 hits for either of these two; both UNTRACKED (`git ls-files --error-unmatch`), 3,144 B and 2,622 B live at 21:1xZ.",
      "ESTATE_GOVERNANCE-S2 at HEAD (from 4.0.0_SA_CRO~C 94210 and 1.0.0_SA_CTO 94239 s.5c): the same two files, the archive's call to add them."
    ],
    "remedy": "Add both files to org/audit/archive/MANIFEST.txt (the archive owner's act) and give org/to-pipeline-override-audit.log the same durability decision as S1's logs. Disarm: one archive run after the edit that shows both files with a baseline size, read at this seat.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```

## S3 -- the deploy ledger's check dies on a cp1252 print before its verdict; reproduced at this seat

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S3",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": ".tools/deploy_ledger.py check --red (the NEVER-2 read every /drive tick chains) prints a line carrying U+26D4 through a cp1252 stdout and dies on UnicodeEncodeError mid-sweep with rc=1 -- an interpreter's exit code where a caller expects the verdict's; 167 of 644 ledger surfaces under org/critical_paths/ carry non-ASCII bytes, so the input is pervasive and the crash character is the estate's own doctrine glyph.",
    "evidence": [
      "C-S3 (ADJUDICATION_v1.md): reproduced at this seat 2026-09-04T21:21Z with PYTHONIOENCODING and PYTHONUTF8 unset -- rc=1, 16 stdout lines ending in two BYPASS / RED pairs, 13 stderr lines ending `UnicodeEncodeError: 'charmap' codec can't encode character '\\u26d4' in position 144` via encodings/cp1252.py:19; census 167 of 644 files with bytes above 0x7F.",
      "Owner by authorship at this seat: `git log --format=%an -- .tools/deploy_ledger.py` -> 1.0.0_SA_CTO 5 of 20 commits and the latest (@6dc8d4045f 2026-09-04 13:54Z); 0.7.0_AE_CloudOps 4; 0.8.0_AE_CloudComp 4. The header names no owner.",
      "ESTATE_GOVERNANCE-S3 at HEAD (from 1.0.0_SA_CTO 94239 s.5d, carrying 4.0.0_SA_CRO~C's observation): the same traceback at that seat."
    ],
    "remedy": "At the tool's entry, force UTF-8 (or errors=replace) on stdout and stderr so a print cannot end the sweep; then either census and strip the non-ASCII bytes on the ledger surface (CLAUDE.md section 4) or accept them by design and say so in the tool; and state what /drive does with a traceback exit (a non-verdict exit is the class PRD NFRA_COMPEFFICACY s.4.4 FWD-10 names). Disarm: one `check --red` at a cp1252 console (PYTHONIOENCODING unset) that exits on its verdict with no traceback, read at this seat.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```

## S4 -- the commit tool's two defects: the override reader unreachable on an adjudications-only commit, and the corpus pass reading other seats' untracked drafts -- both fixed and exercised

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S4",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "(1) .tools/safe-commit.sh's surprise-row stage selected the files it grades -- the only code path that reads '# surprise-row-override:' and exports SURPRISE_ROW_OVERRIDE for the hook -- by patterns naming investigations/ and remediations/ and not adjudications/, so an adjudications-only commit never reached the reader and the hook refused with no override in hand. (2) surprise-corpus-validate.py globbed the worktree, untracked files included, so a peer's draft on disk refused an unrelated seat's valid commit (twice, 18:58Z and 19:04Z on NFRA_CLDGRPH C-S7).",
    "evidence": [
      "Fix 1 @9aa3520831 (1.0.0_SA_CTO, 2026-09-04T20:09:10Z): safe-commit.sh at HEAD :725 names *org/surprise_channel/*ADJUDICATION_v* and *org/missions/*/surprise-channel/adjudications/* (comp-read at this seat); exercised at this seat by commit 2678835bfb (the stage selected and graded the tree ADJUDICATION_v1.md) and by the CTO's seven-path selector exercise (94274).",
      "Fix 2 @e29c5a0bb8 (1.0.0_SA_CTO, 2026-09-04T20:47:31Z): surprise-corpus-validate.py at HEAD :166 reads `git ls-files --cached -z`, :123-124 the fallback announces a worktree denominator, :143-145 and :151 name adjudications/ (comp-read at this seat); exercised at this seat by the same commit's `documents=29 rows=331` index denominator and by the CTO's discriminating pair (untracked malformed draft: 29 documents, 0 new; the same file staged: 30 documents, 6 new failures, REFUSED).",
      "C-S4 (ADJUDICATION_v1.md) carries the full read; ESTATE_GOVERNANCE-S4 at HEAD carries the two measured refusals before the fixes."
    ],
    "remedy": "EXECUTED by the owner: add the adjudications patterns to safe-commit.sh's selector (both spellings); make the corpus pass read the git index (tracked plus staged) with an announced worktree fallback; bring adjudications/ into the corpus. Both landed and exercised; the two lists now name each other in comments so the next channel folder is a three-carrier edit.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "DISARMED", "owner": "1.0.0_SA_CTO", "at": "2026-09-04T20:47Z"},
    "remediation": {"state": "REMEDIATED", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": true
  }
]
```

## S5 -- the row gate's coordinate limb refuses the CVO's rows on every flat-spelling adjudication document

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S5",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": ".tools/surprise-row-gate.py `_folder_identity` (:66-78 @3860dae133) returns `(project, None)` for org/surprise_channel/<CODE>/ADJUDICATION_v<N>.md although its docstring says the flat file's kind is the filename's; `_coordinate_violations` (:420-422) refuses every C- row when folder_kind is not ADJUDICATION, so the CVO's L9 document on every flat channel (19 legacy codes plus ESTATE_GOVERNANCE) is refused at the coordinate and lands only under the audited override. The tree spelling is unaffected.",
    "evidence": [
      "C-S5 (ADJUDICATION_v1.md): measured on this seat's commit of this channel's ADJUDICATION_v1.md at 21:3xZ -- 4 violations, all the coordinate limb, schema and corpus clean; the source lines at HEAD @3860dae133; the tree spelling admitted C-S9 and C-S10 at 2678835bfb through the same limb with no override.",
      "ESTATE_GOVERNANCE-S5 at HEAD carries the verbatim refusal and the four other readers of the flat spelling that accept it (FLAT_CHANNEL_RE, ADJUDICATION_PATTERNS, _is_adjudication_doc, safe-commit.sh:725)."
    ],
    "remedy": "One line at the owner: `_folder_identity` returns `m.group(3).upper()` for the flat match, as its docstring says -- or the coordinate limb consults `_is_adjudication_doc(rel)` when folder_kind is None. Exercise with three arms: a flat ADJUDICATION_v document's C- rows admitted; a C- row in a flat INVESTIGATION_v file still refused; the tree arm unchanged. Disarm: one CVO commit of a flat ADJUDICATION_v document admitted without override, read at this seat.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```
