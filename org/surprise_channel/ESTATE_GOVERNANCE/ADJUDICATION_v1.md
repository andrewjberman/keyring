# ESTATE_GOVERNANCE -- surprise channel, ADJUDICATION v1 (laptop fabric; no round)

**Home:** `org/surprise_channel/ESTATE_GOVERNANCE/ADJUDICATION_v1.md` -- the flat spelling's adjudication document
(annex v3.6 section 4 names the channel, section 4a the document; lane CVO). Minted 2026-09-04 ~21:2xZ by `3.0.0_SA_CVO`
on the first owner's act (`1.0.0_SA_CTO`'s two fixes for S4, @`9aa3520831` and @`e29c5a0bb8`), never as an empty file.
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure or an observation
of the CVO's about the rows in `INVESTIGATION_v<N>.md`; a seat that contests one surfaces a new investigation row citing
it. A reader resolves an item's state from the newest row that cites it across the three documents; an ARMED item's disarm
state is its remediation row's `disarm.state` (annex, the slug paragraph), never the investigation row's `hazard_standing`,
which is the at-surfacing classification and is append-only.
**Coordinate:** `ESTATE_GOVERNANCE-C-S<k>`, `k` from 1 in this document.
**No round, no L10:** this channel has no task orders and no slug. A graduated item's remedy is routed to its owner by name
in `REMEDIATION_v1.md`, and the clocks there advance as the owner's acts land, each advance evidenced in this document.
**Denominator at this write:** 7 rows (C-S1 .. C-S7; C-S7 appended 2026-09-05 ~16:1xZ: the ruling on repository-scoped provenance's residual, accepted on four terms, beside S6 filed in the same commit and left UNDER_INVESTIGATION; 6 rows (C-S1 .. C-S6; C-S6 appended ~22:4xZ: S5's clocks advance on @`14f26b5eff` and this row's own admission without override is the exercise; the flat-kind ruling) dispositioning S1 .. S5 -- all five GRADUATED (C-S5 on S5, the row gate's coordinate limb refusing this very document, appended ~21:4xZ in the same commit under the audited override that limb forced); S4 REMEDIATED and
DISARMED at this write on the CTO's two fixes, read and exercised at this seat; S1, S2 and S3 OPEN with owners named.
Investigation rows without a disposition after this write: 0 of 5.

---

## C-S1 -- adjudicates S1: a tracked append-only audit log with no commit cadence arms a revert on itself, GRADUATED; the rows are recovered, the mechanism is unchanged, and the durability decision is the owner's

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S1",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T21:20Z",
    "one_line": "ADJUDICATES S1 -- GRADUATED. The mechanism is real and is unchanged at this write: the three append-only audit logs (org/mass-deletion-audit.log, org/safe-deploy-bypass-audit.log, org/rcg-sweep-audit.log) are tracked with no commit cadence, so every append since the last commit dies on the next checkout of that path and git then reads the file CLEAN. The 46 rows are recovered (@004a1d3026, 1.0.0_SA_CTO); at this seat's read the live files equal HEAD line for line (21 / 4 / 33), so the class is ARMED and UNLOADED -- nothing is at risk this minute, and the next append loads it again. The remedy is a design call among three named options and belongs to the control's author, 1.0.0_SA_CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "At this seat, 21:1xZ, the record plane: `git log --format=%h -- <log>` returns exactly 2 commits for each of the three files (the original tracking commit @b150952baa and the recovery @004a1d3026); `git diff --numstat HEAD -- <the three>` is empty; live line counts 21 / 4 / 33 equal `git show HEAD:<log>` line counts 21 / 4 / 33. Rows at risk at this write: 0 of 58. The condition that armed S1 (tracked, no cadence) is unchanged.",
        "org/audit/archive/MANIFEST.txt at HEAD, enumerated at this seat: lines 21, 22 and 33 name the three logs -- the archive baseline that made the truncation visible and the recovery possible exists and covers them (the positive control for C-S2's finding).",
        "S1 at HEAD (3.0.0_SA_CVO, 18:15Z, filed from 4.0.0_SA_CRO~C 94210 and 1.0.0_SA_CTO 94239): the two live files byte-identical to a July blob; one commit per file at that read; the recovery within twenty minutes -- read as written, and the recovery commit is in HEAD at this seat (`merge-base --is-ancestor` YES)."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ESTATE_GOVERNANCE-S1"
    ],
    "spec_asserts": "The CTO's control @b150952baa (2026-07-16) tracks the bypass-class logs so the record carries them; the archive (org/XXX.md A.2) is the durability baseline; an append-only log is expected to be preserved by being tracked.",
    "world_is": "Tracking without a cadence preserves nothing past the last commit and arms a revert on every later append; the archive, not git, is what recovered the rows. The item is graduated with its remedy as the owner's design call: commit the logs on a cadence, or untrack them and make the archive the durable carrier, or move the writers to where a checkout cannot reach. The remediation row names 1.0.0_SA_CTO and stays OPEN until the act lands.",
    "notes": "Evidence law for the grade: GRAIN (the three files by path at HEAD and live), COVERAGE (3 of 3 logs, both planes), STATE (APPLIED: tracked with no cadence, measured; the revert itself was EXERCISED by the incident and is not re-exercised here). The disarm is the owner's act plus one checkout that leaves an appended row standing."
  }
]
```

## C-S2 -- adjudicates S2: two audit logs the archive MANIFEST does not carry, GRADUATED; one of them is the L6 override log, and a truncation of either is undetectable by the one control built to detect it

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S2",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T21:20Z",
    "one_line": "ADJUDICATES S2 -- GRADUATED. Measured at this seat against the manifest itself: org/audit/archive/MANIFEST.txt names four audit logs (git-author-override, mass-deletion, safe-deploy-bypass, rcg-sweep; lines 19, 21, 22, 33) and names neither org/to-pos-override-audit.log nor org/to-pipeline-override-audit.log (0 hits each, beside the 4 hits of the positive control). Both files are UNTRACKED in git at this seat (3,144 B and 2,622 B live), so they have no baseline in the archive and none in the record: S1's class cannot be DETECTED on them, and the second file is the log the L6 gate writes on every issuance that goes through by override. The remedy -- add both to the MANIFEST and give them S1's durability decision -- is the archive owner's, 1.0.0_SA_CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`comp-read org/audit/archive/MANIFEST.txt --enumerate '<six log names>'` at this seat, 21:2xZ: 4 hits across 39 lines -- line 19 org/git-author-override-audit.log, line 21 org/mass-deletion-audit.log, line 22 org/safe-deploy-bypass-audit.log, line 33 org/rcg-sweep-audit.log; 0 hits for to-pos-override-audit and to-pipeline-override-audit. The four are the positive control: the instrument finds a covered log, so the two zeros are absences in the manifest, not out-of-corpus.",
        "`git ls-files --error-unmatch` at this seat: org/to-pos-override-audit.log UNTRACKED, org/to-pipeline-override-audit.log UNTRACKED; `wc -c` 3,144 and 2,622 bytes live. No baseline in the record either.",
        "S2 at HEAD (filed from 4.0.0_SA_CRO~C 94210 and 1.0.0_SA_CTO 94239 s.5c): the same two files and the same finding -- read as written; the CTO's 94239 names adding a file to the MANIFEST as the archive's call."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ESTATE_GOVERNANCE-S2"
    ],
    "spec_asserts": "org/XXX.md A.2 and the archive MANIFEST: every audit log the fabric writes has an archive baseline against which a truncation is measurable; the L6 gate's override log is an audit log of that class.",
    "world_is": "Two audit logs have no baseline anywhere; a silent truncation of either is invisible to the archive's coverage check and to git alike. Graduated; the remediation row names 1.0.0_SA_CTO and stays OPEN until both files are in the MANIFEST and carry S1's durability decision.",
    "notes": "The disarm is one archive run after the manifest edit that shows both files with a baseline size, read at this seat."
  }
]
```

## C-S3 -- adjudicates S3: the deploy ledger's own check dies on a cp1252 print before its verdict, GRADUATED and REPRODUCED at this seat; the input side is pervasive (167 of 644 ledger surfaces carry non-ASCII bytes)

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S3",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T21:25Z",
    "one_line": "ADJUDICATES S3 -- GRADUATED, and the crash is REPRODUCED at this seat rather than carried from 4.0.0_SA_CRO~C's report: `.tools/deploy_ledger.py check --red` run at 21:21Z with PYTHONIOENCODING and PYTHONUTF8 unset exits rc=1 with a Python traceback ending `UnicodeEncodeError: 'charmap' codec can't encode character '\\u26d4' in position 144` (the U+26D4 no-entry sign) out of cp1252.py:19 -- after printing 16 stdout lines that include two BYPASS / RED verdict lines. So the exit code a caller reads is the traceback's, indistinguishable from a verdict's, which is the class S3 names (a verdict-bearing tool returning a non-verdict exit). The input side is not one stray byte: 167 of 644 files under org/critical_paths/change_management/ and .open_deploys/ carry non-ASCII bytes. Owner by the record's authorship: 1.0.0_SA_CTO (5 of 20 commits, the latest @6dc8d4045f 2026-09-04 13:54Z), the AE lanes next (0.7.0_AE_CloudOps 4, 0.8.0_AE_CloudComp 4).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The exercise at this seat, 2026-09-04T21:21Z, a Windows console, PYTHONIOENCODING and PYTHONUTF8 removed from the environment: `python .tools/deploy_ledger.py check --red` -> rc=1; stdout 16 lines, the last four 'BYPASS: UNINDEXED OPEN LEDGER org/critical_paths/change_management/20260901T0645Z_d12-portal-dev-to-prod-promote-v2.1.174_deploy.md age=71.7h ...', 'RED: unindexed-ledger alert delivered to COO inbox: ...', the same pair for 20260901T0817Z_d12-w3-actb-issue-not-send_deploy.md; stderr 13 lines, a traceback through encodings/cp1252.py line 19 `codecs.charmap_encode` ending `UnicodeEncodeError: 'charmap' codec can't encode character '\\u26d4' in position 144: character maps to <undefined>`. The verdict was interrupted mid-sweep; rc=1 is the interpreter's.",
        "The census, same run: 644 ledger surfaces scanned (org/critical_paths/change_management/*.md plus org/critical_paths/.open_deploys/*.json); 167 carry at least one byte above 0x7F (first twenty listed in the probe's output, 2 to 43 bytes each, dating from 2026-06-12 onward). CLAUDE.md section 4's no-non-ASCII rule is not applied on this surface, and U+26D4 is the estate's own doctrine glyph -- the crash character is one the fabric writes on purpose.",
        "DISCLOSURE of the probe's side effect: the `--red` run delivered two RED alert files into 2.0.0_SA_COO's inbox (20260904T212139Z_deploy-ledger_RED__UNINDEXED_open_deploy_ledger__gate_bypass__<entry>.md for the two entries above). Those are the tool's ordinary deliveries, the same ones every /drive tick makes; they are named here so they are not read as a new incident. The two UNINDEXED OPEN entries themselves are the COO's NEVER-2 reads and are not this channel's item.",
        "Owner resolution at this seat: `git log --format=%an -- .tools/deploy_ledger.py` -> 20 commits by 8 seats; 1.0.0_SA_CTO 5 (the most, and the latest at @6dc8d4045f 2026-09-04 13:54Z), 0.7.0_AE_CloudOps 4, 0.8.0_AE_CloudComp 4, 0.4.0_DS_ClientPlatform~B 2, 0.4.0_DT_ClientPlatform~C 2, three singletons. The tool's header names no owner. The CTO's 94239 description ('not this seat's tool') is not supported by the record's authorship; the row names the CTO, who may route it to the AE lane by name."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ESTATE_GOVERNANCE-S3"
    ],
    "spec_asserts": "deploy_ledger.py's own docstring: `check --red` is the NEVER-2 read every /drive tick chains, and a half-finished deploy cannot slip past a tick; PRD NFRA_COMPEFFICACY s.4.4 (FWD-10): a verdict-bearing tool returns its verdict's exit, never an interpreter's.",
    "world_is": "The check dies on a print of a doctrine glyph under cp1252 before its sweep completes, exits 1 on the traceback, and a caller reading the exit code cannot tell that from RED. Graduated; the remediation row names 1.0.0_SA_CTO and stays OPEN. Remedy: force UTF-8 (or errors=replace) on the tool's stdout and stderr at entry so the verdict survives the print; then either census and strip the non-ASCII bytes on the ledger surface or accept them by design; and state what /drive does with a traceback exit.",
    "notes": "Not filed as a separate item, stated for the reader: the probe surfaced two UNINDEXED OPEN ledger entries aged 71.7 h (the 09-01 d12 promote and the d12 w3 actb issuance); they are delivered RED to the COO on every tick already and belong to that seat's NEVER-2 read. The disarm is one `check --red` at a cp1252 console that exits on its verdict with the traceback gone, read at this seat."
  }
]
```

## C-S4 -- adjudicates S4: the commit tool's two defects, GRADUATED and CLOSED at this write -- both halves fixed by 1.0.0_SA_CTO, read at source and exercised on this seat's own commit

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S4",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T21:25Z",
    "one_line": "ADJUDICATES S4 -- GRADUATED, and its remediation row is REMEDIATED, DISARMED and closed in this commit. Half 1 (the override reader unreachable on an adjudications-only commit): fixed @9aa3520831 -- safe-commit.sh's selector at HEAD :725 now names *org/surprise_channel/*ADJUDICATION_v* and *org/missions/*/surprise-channel/adjudications/*, read at this seat; exercised at this seat by commit 2678835bfb, where the surprise-row stage selected and graded the tree ADJUDICATION_v1.md inside safe-commit's own stage (the block that carries the override reader ran), and by the CTO's seven-path selector exercise (94274). Half 2 (the corpus pass reading other seats' untracked drafts): fixed @e29c5a0bb8 -- surprise-corpus-validate.py at HEAD :166 reads `git ls-files --cached` (the index), :123-124 the worktree fallback announces itself with its own denominator; exercised at this seat by the same commit's corpus line (documents=29 rows=331, the index denominator) and by the CTO's discriminating pair (an untracked malformed draft on disk: 29 documents, 0 new; the same file staged: 30 documents, 6 new failures, REFUSED). The same commit also brought adjudications/ into the corpus for the first time (26/317 to 29/331, 0 new failures) -- the CTO's own finding, noted here and not filed on its behalf.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Half 1 at source, this seat: `comp-read .tools/safe-commit.sh --enumerate adjudications` at HEAD -> 2 hits, :717 the comment recording the 2026-09-04 addition on S4 and :725 the case pattern `*org/surprise_channel/*INVESTIGATION_v*|*org/surprise_channel/*REMEDIATION_v*|*org/surprise_channel/*ADJUDICATION_v*|*org/missions/*/surprise-channel/investigations/*|...adjudications/*`; `merge-base --is-ancestor 9aa3520831 HEAD` YES (commit 2026-09-04T20:09:10Z, 1.0.0_SA_CTO).",
        "Half 1 exercised, this seat: commit 2678835bfb (adjudications/ADJUDICATION_v1.md with two remediation documents) -- safe-commit's stage printed `[surprise-row-gate] .../adjudications/ADJUDICATION_v1.md: 2 new row(s) of 10 total checked` BEFORE the hook's own re-run printed the same, i.e. the selector chose the adjudication document and the block holding the override reader ran. No override was needed (the corpus read clean), so the read-through of a marker to the hook is cited from the CTO's exercise (94274: seven real paths, five channel files selected including flat ADJUDICATION_v and tree adjudications/, two controls skipped), not re-run here.",
        "Half 2 at source, this seat: `comp-read .tools/surprise-corpus-validate.py --enumerate 'ls-files|adjudications|worktree'` at HEAD -> :166 `subprocess.run([\"git\", \"ls-files\", \"--cached\", \"-z\"]` in `_index_paths` (docstring: 'THE INDEX, NOT THE WORKTREE (3.0.0_SA_CVO ESTATE_GOVERNANCE-S4 half 2)'), :123-124 the fallback prints 'Denominator below is a worktree denominator' and sets source = worktree, :139-145 the STOP comment and the tree globs now naming adjudications/, :151 the relative-path regex naming all three folders; `merge-base --is-ancestor e29c5a0bb8 HEAD` YES (commit 2026-09-04T20:47:31Z, 1.0.0_SA_CTO).",
        "Half 2 exercised: at commit 2678835bfb the pass printed `DENOMINATORS: documents=29 rows=331 malformed_blocks=0 failures=4 baseline=4 known=4 new=0` -- the index population with the three tree adjudication documents counted; the discriminating pair is the CTO's @e29c5a0bb8 (94280): ARM A an UNTRACKED malformed channel draft on disk -> documents 29, 0 new, OK; ARM B `git add` of the same file -> documents 30, 6 NEW failures, REFUSED, the row named. Without ARM B the fix would be indistinguishable from a broken pass; with it the untracked-versus-staged discrimination is measured.",
        "S4 at HEAD (this seat, 19:10Z): the two measured refusals at 18:58Z and 19:04Z on C-S7 and the :715 path set lacking adjudications/ -- the state before both fixes; the CTO's 94277 corrected its own relay (the foreign draft had already been repaired and landed @5376ecaa8b at 19:2xZ; the refusals were real inside the 25-minute window)."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ESTATE_GOVERNANCE-S4"
    ],
    "spec_asserts": "safe-commit.sh's own text: the surprise-row stage grades every channel file in the pathspec and carries the audited override to the hook; surprise-corpus-validate's baseline is the RECORD's failure set; the annex makes adjudications/ a channel document of the same plane as the other two.",
    "world_is": "Both mechanisms now match their text: an adjudications-only commit reaches the override reader, and the corpus graded at commit time is the index (tracked plus staged), so a peer's draft on disk cannot refuse it. Read at source at HEAD and exercised on a real commit at this seat, with the CTO's discriminating arms cited. The remediation row is REMEDIATED (round v1), DISARMED at 2026-09-04T20:47Z (the later fix's commit, the exercise vintage) and closed.",
    "notes": "The transferable finding is the CTO's and is recorded in both tools' comments: a pattern list is a declared domain whose uncovered member must be hunted -- three carriers missed the same folder in two days (safe-commit's selector twice, the corpus validator once), and the two lists now name each other. The CTO's sibling finding (adjudications/ absent from the corpus, so 3 documents and 14 rows read clean by never being read) is the CTO's to file as its own row on this channel if it judges the record needs one beyond its message and its commit; this seat does not file another seat's finding."
  }
]
```

## C-S5 -- adjudicates S5: the row gate's coordinate limb refuses the CVO's rows on every flat-spelling adjudication document, GRADUATED; this document lands under the audited override the limb forced, and the fix is one line at the owner

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S5",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T21:45Z",
    "one_line": "ADJUDICATES S5 -- GRADUATED. The refusal is measured on this seat's own commit (four lawful CVO rows on the document annex v3.6 names, refused by one limb while the schema, the corpus, safe-commit's selector and the gate's own id census all recognise the file); the mechanism is read at source @3860dae133 (`_folder_identity` :66-78 returns kind None for the flat spelling against its own docstring; `_coordinate_violations` :420-422 refuses C- on None); the class covers every flat channel and no tree channel. The remedy is the CTO's and is one line; the remediation row is OPEN with the disarm named. This document and its siblings land in the same commit under the audited '# surprise-row-override:' -- the documented escape, used for the case it exists for, and recorded here so the override is not mistaken for the fix.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S5 at this write (this seat, 21:40Z): the verbatim refusal on ADJUDICATION_v1.md (4 violations, all the coordinate limb; schema and corpus clean at documents=30 rows=339), the source lines at HEAD @3860dae133, and the four other readers that accept the flat spelling -- read as filed, by the seat that filed it, on its own commit.",
        "Discrimination: the tree spelling carried C-S9 and C-S10 into NFRA_CLDGRPH's adjudications/ADJUDICATION_v1.md at 2678835bfb (17:01:30 -0400) with no override and no coordinate violation, through the same gate at the same vintage's limb -- so the limb's tree arm works and its flat arm is the defect, not the C- coordinate itself.",
        "Coverage: 19 flat codes under org/surprise_channel/ plus ESTATE_GOVERNANCE; no flat channel has carried a CVO C- row before this commit (the coordinate is one day old, annex v3.3), which is why the flat arm was never exercised until the first flat adjudication document was written."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "ESTATE_GOVERNANCE-S5"
    ],
    "spec_asserts": "Annex v3.6 section 4 / 4a and the gate's own FLAT_CHANNEL_RE and docstring: the flat adjudication document is org/surprise_channel/<CODE>/ADJUDICATION_v<N>.md, its kind is the filename's, and the CVO's rows there carry <CODE>-C-S<k>.",
    "world_is": "One limb reads the kind from the tree sub-folder alone and refuses every CVO row on a flat adjudication document. Graduated; the remediation row names 1.0.0_SA_CTO and stays OPEN until a flat ADJUDICATION_v commit is admitted without override at this seat.",
    "notes": "The override used for this commit is the audited path safe-commit.sh carries (read from the message body, exported to the hook, one SURPRISE-ROW-OVERRIDE row in the audit log); it is reachable on this document only because of @9aa3520831 (S4 half 1) -- the two defects are siblings: S4 made the escape reachable on the tree spelling's document, S5 is the flat spelling's limb refusing what the escape now lets through."
  }
]
```

## C-S6 -- S5's clocks advance on 1.0.0_SA_CTO's fix @14f26b5eff; this row is the exercise (a new C- row on the flat adjudication document, committed without override), and the ruling on whether a flat path declares its kind

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S6",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T22:45Z",
    "one_line": "S5's remediation row advances REMEDIATED and DISARMED on 1.0.0_SA_CTO's fix @14f26b5eff (2026-09-04T22:35:50Z): the coordinate limb now consults `_is_adjudication_doc(rel)` when folder_kind is None (remedy ii), the docstring of `_folder_identity` corrected to say what the code does and why, self-test 71 of 71 with the three arms this seat named (flat ADJUDICATION_v C- row admitted; a C- row in a flat INVESTIGATION_v still refused; the tree arm unchanged). The disarm condition S5 set -- one CVO commit of a flat ADJUDICATION_v document admitted WITHOUT override, read at this seat -- is exercised by the commit that carries this row: this is a NEW C- row on org/surprise_channel/ESTATE_GOVERNANCE/ADJUDICATION_v1.md and the commit message carries no override marker; if the reader can see this row at a commit of 3.0.0_SA_CVO's, the limb admitted it. RULING on the question the fix leaves to this seat (whether a flat path declares its kind at all): the flat spelling's kind IS the filename's for schema, coordinate and census purposes (annex v3.6, the gate's own FLAT_CHANNEL_RE), and the L10 precondition limbs do NOT bind on a flat channel, because a flat channel has no task orders to be terminal -- ESTATE_GOVERNANCE's own header says 'no round, no L10' and the 19 legacy codes predate the tree. Remedy (ii) is therefore the durable form, not a stopgap: it gives the flat document its kind where kind matters and keeps the order-bound limbs where orders exist. The open question the docstring now names is closed by this row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "At source, HEAD @14f26b5eff (1.0.0_SA_CTO, 2026-09-04T22:35:50Z), read at this seat: `_folder_identity` :66-84 -- docstring now 'FLAT RETURNS kind=None, DELIBERATELY, and this docstring used to claim otherwise ... The limb now asks _is_adjudication_doc(rel) instead when folder_kind is None' with the four-consumer reason for keeping None and the question named for this seat; `merge-base --is-ancestor 14f26b5eff HEAD` YES.",
        "The CTO's exercise (94300), cited not re-run: self-test 71 of 71 (was 68) -- flat ADJUDICATION_v C- row ADMITTED; narrowness, a C- row in a flat INVESTIGATION_v STILL REFUSED; the tree arm unchanged; remedy (i) measured and declined because folder_kind feeds four consumers and a returned kind would switch the L10 precondition limbs on for the two flat REMEDIATION documents (ESTATE_GOVERNANCE, NFRA_PIPELINE).",
        "This seat's exercise: the commit carrying this row and the S5 clock flip is a commit of the flat ADJUDICATION_v1.md with a NEW C- row (C-S6) and no '# surprise-row-override:' in its message -- the first attempt at 21:3xZ was refused on exactly this limb with the override absent (S5's evidence), so admission here is the discriminating arm at this seat, on the document the defect was found on, by the seat that found it.",
        "The ruling's grounding: the flat spelling's documents carry no task orders (org/surprise_channel/<CODE>/ has no task-orders folder; the tree contract's surprise_channel_glob is where orders live), so an L10 precondition evaluated on a flat channel would read zero orders and pass vacuously -- a gate on an empty input set, the shape the estate already names; keeping the flat kind out of the order-bound limbs is the correct boundary, and remedy (ii) draws it."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A clock-advance record and a ruling: this row adjudicates no new item and opens nothing; S5's state moves on the remediation plane in this commit and the flat-kind question the fix left open is answered above.",
    "spec_asserts": "Annex v3.6 section 4 / 4a: the flat channel's adjudication document carries the CVO's C- rows; the row gate's coordinate limb admits them there. S5's remediation row: disarm on one CVO commit of a flat ADJUDICATION_v document admitted without override.",
    "world_is": "The limb admits the flat document's C- rows on the filename's kind while the order-bound limbs stay keyed to the tree spelling. S5 is REMEDIATED (round v1), DISARMED at 2026-09-04T22:45Z and closed; the exercise is this commit. Sequencing of the boundary's (b) and (c) after the push, as the CTO proposes, is accepted -- nothing of this seat's waits on them, and the exemptions @69603c1807 coming out in the same commit as their replacement is the right shape.",
    "notes": "The clock-advance table convention of the tree channels is carried here in prose: the S5 advance's evidence is this row. ESTATE_GOVERNANCE at this write: S4 and S5 closed; S1, S2, S3 OPEN at 1.0.0_SA_CTO, who has taken S3 by name (94300 s.3). Three docstrings stated a behaviour their code did not have today (safe-merge's abort claim, the gate's merge principle, this one) -- a docstring is a carrier nothing compares to the code; noted for the annex's next revision as a reading rule, not a new gate."
  }
]
```

```json
[
  {
    "id": "ESTATE_GOVERNANCE-C-S7",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T16:12Z",
    "one_line": "RULING on the question 0.0.0_AB_MSTR 94398 s.4 put to this seat: is repository-scoped provenance's residual acceptable -- a value the worker could have read from the shared tree and committed without being told? YES, on four terms, and it is the same shape as boundary (b)'s residual bounded at @2eabc5197e. (1) The limb grades against an artifact the acting seat did not author -- an ISSUER-authored commit anywhere in the object graph at or before the carry that set the field to that value -- and states on its own output WHICH commit blessed the value and that ancestry was not required. (2) Time-bounded: a later issuer commit blesses nothing retroactively. (3) The residual is named in the gate's own note as what the limb does not guard, exactly as the ANY-lane note names what the lane no longer guards -- a permit you can explain. (4) The residual stays OBSERVED, not trusted: at L9 this seat censuses, per project, the worker commits that modify a grant field (anchored diff lines, `--full-history`, denominator printed) and the count rides the slug -- today 2 of 2 faithful in NFRA_OUTSET -- so a value read-and-committed-untold would appear as a MATCH with no instruction in the issuer's hand-off, which the COO can see at its drain. NOT done by this ruling: narrowing the lane (Andrew's word), designing the limb (the CTO's neck), or asking for a merge-based transport (the COO's reasons for the path-scoped checkout stand; a transport chosen to avoid a merge conflict discards the merge's evidence, and the estate takes that trade with its eyes open).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A ruling record, not a hazard: it answers the one call the thread assigned to the CVO and dispositions nothing -- S6 stays UNDER_INVESTIGATION and ARMED to 1.0.0_SA_CTO until the limb lands and its ACK row cites it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE PRECEDENT THIS RULING EXTENDS: boundary (b) @2eabc5197e grades a C- row on a merge against the merge's PARENTS -- an artifact the committer did not author -- and its residual (a parent a seat could have arranged) was bounded and disclosed rather than closed. The provenance limb's residual has the same structure: the blessing artifact (the issuer's commit) is one the worker did not write; what the worker could still do is copy it unbidden, and that act leaves a MATCH with no hand-off behind it, which term (4) makes visible.",
        "WHY THE THREE REFUSED KEYS ARE NOT REVIVED BY THIS RULING: authorship refuses the instructed carry because the slot IS the identity and the carrier is the assignee by design (94388); ancestry refuses it because the prescribed transport is a path-scoped checkout (94398, 94401); a simplified log refuses it because history simplification drops the amendment commit (94391). Each was caught before shipping by a positive control on a KNOWN faithful transport -- which is why term (ii) of S6's disarm requires that control in the self-test, permanently.",
        "TERM (4) IS A READ THIS SEAT ALREADY OWNS, NOT A NEW GATE: the L9 reads a round's task orders from git (spine v3 s.4, the step log's L7 read); adding `git log --full-history --format=%h --author=<worker> -- <project>/task-orders/` with the anchored `^[+-]<issued_to>[^<]*</issued_to>$` and `<paths>`-block diff lines is one command per project with its denominator printed. It was run for this ruling on NFRA_OUTSET: 2 commits, 2 faithful. No approval gate is implemented or proposed (CLAUDE.md s.2, do not manufacture friction)."
      ]
    },
    "spec_asserts": "Boundary (b)'s property (@2eabc5197e): grade against an artifact the acting seat did not author, with the residual disclosed on the limb's own output. Rule 22: a permit you cannot explain is worth less than a refusal you can; DISCRIMINATION -- could the evidence differ if the claim were false.",
    "world_is": "Three keys were tried in one day and all three refused the instructed path; the fourth -- repository-scoped issuer authorship, time-bounded -- admits both real carries and refuses an invented value, and its price is the residual above. Accepted on the four terms; the annex's next revision carries them as section 5's provenance clause.",
    "notes": "The CVO's one call in this thread, recorded as a file because that is the carrier the spine names for rulings the CTO reads; no message rides it beyond the CTO's next slug, where S6 and C-S7 are cited by path and vintage."
  }
]
```
