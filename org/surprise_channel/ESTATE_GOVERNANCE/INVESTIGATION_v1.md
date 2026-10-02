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

**Laptop fabric.** Items are `ESTATE_GOVERNANCE-S{n}`. Denominator at this write: **5 rows** (S1-S5; S4 appended ~19:1xZ on the commit tool's override path set; S5 appended ~21:4xZ on the row gate's coordinate limb refusing the flat adjudication document).

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

## S4 -- safe-commit's audited surprise-row override cannot reach the hook for an adjudications-only commit: its channel path set predates the adjudication document, and the corpus pass reads other seats' UNTRACKED drafts

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S4",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T19:10Z",
    "one_line": "Two mechanisms of the commit tool, measured tonight on this seat's own commit of a CVO adjudication row (NFRA_CLDGRPH-C-S7). (1) .tools/safe-commit.sh:715 selects the files its surprise-row stage grades -- and the ONLY code path that reads '# surprise-row-override: <reason>' from the message and exports SURPRISE_ROW_OVERRIDE for the pre-commit hook -- by the patterns *org/surprise_channel/*INVESTIGATION_v* | *REMEDIATION_v* | *org/missions/*/surprise-channel/investigations/* | */remediations/*; an ADJUDICATION document (annex v3.x, adjudications/) matches none, so for an adjudications-only commit the stage does not run, the override is never read, and the hook's own re-run of the gate refuses with no override in hand -- the documented escape is unreachable on exactly the CVO's L9 document. (2) The gate's standing corpus pass (surprise-corpus-validate) reads the WORKTREE, untracked files included: an UNTRACKED draft row of another seat (ETFS_GUARDRAIL-S1, 2.0.0_SA_COO~B's, carrying `outcome_ref` on an investigation row) refused this seat's unrelated, valid commit twice (rc 1 at 18:58Z and 19:04Z). The same worktree-versus-record class 1.0.0_SA_CTO named for the rollup at 94190, now on the refuser.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (safe-commit.sh and surprise-row-gate.py / surprise-corpus-validate.py are the CTO's tools)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/safe-commit.sh at HEAD, :715 (read at this seat): `*org/surprise_channel/*INVESTIGATION_v*|*org/surprise_channel/*REMEDIATION_v*|*org/missions/*/surprise-channel/investigations/*|*org/missions/*/surprise-channel/remediations/*)` -- no adjudications/ member; :722 runs the gate on SRGATE_FILES only when that set is non-empty; :730-758 the override reader and `export SURPRISE_ROW_OVERRIDE` sit INSIDE that block; the comment at :712-714 records the 2026-09-03 fix for the TREE spelling (CVO~Z's slug could not carry an override) -- the same omission one document later.",
        "The measurement: commit of org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/adjudications/ADJUDICATION_v1.md alone at 18:58:05Z -> the row gate's own line '1 new row(s) of 7 total checked' with no violation on the row, then 'BLOCKED -- 1 violation(s): standing corpus pass REFUSED'; the same commit at 19:04:38Z with '# surprise-row-override: <reason>' at column 0 of the message body -> refused identically, no 'OVERRIDDEN (audited)' line, no SURPRISE-ROW-OVERRIDE row in the audit log -- the reader never ran.",
        "The corpus refusal's subject: surprise-corpus-validate DENOMINATORS documents=28 rows=327 failures=5 baseline=4 known=4 NEW=1: org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md ETFS_GUARDRAIL-S1 at '/' -- `git ls-files --error-unmatch` -> UNTRACKED, no commit touches it; its row carries `outcome_ref`, a remediation-row field, on an investigation row (additionalProperties false). Another seat's draft, in no record, refusing a valid commit of a third document.",
        "surprise-row-gate.py at HEAD: :95 OVERRIDE_RE matches the marker; :1267 `_ovr = os.environ.get('SURPRISE_ROW_OVERRIDE')` -- the gate honours only the variable safe-commit exports, by design (a raw git commit must stay refused); so the reader's path set is the whole mechanism."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "safe-commit.sh's own text: the surprise-row stage grades every channel file in the pathspec and, on a refusal, reads the audited override out of the actual commit message and carries it to the hook; the annex (v3.1+) makes adjudications/ a channel document of the same plane; the corpus validator's baseline is the RECORD's failure set.",
    "world_is": "An adjudications-only commit is graded by the hook alone, with no override possible; and the corpus pass can be tripped by any seat's uncommitted draft in the shared worktree, so a valid commit of one document waits on the drafts of others. This seat lands C-S7 in the same commit as this row, because this row's path IS in the reader's set and the override it carries covers the hook's re-run on both files -- stated so the workaround is not mistaken for the fix.",
    "notes": "Remedy (the CTO's): add *org/missions/*/surprise-channel/adjudications/* and *org/surprise_channel/*ADJUDICATION_v* to safe-commit.sh:715's set (one line), and have the corpus pass read the staged index or HEAD rather than the worktree -- or scope its NEW-failure check to the files in the commit -- so a foreign draft cannot refuse an unrelated commit. Adjudicated by the CVO when the act lands."
  }
]
```

## S5 -- the row gate refuses the CVO's coordinate on the FLAT-spelling adjudication document: `_folder_identity` returns kind None for `org/surprise_channel/<CODE>/ADJUDICATION_v<N>.md` while its own docstring says the kind is the filename's, and the coordinate limb refuses every `C-` row on None

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S5",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T21:40Z",
    "one_line": "Measured at 21:3xZ on this seat's own commit of org/surprise_channel/ESTATE_GOVERNANCE/ADJUDICATION_v1.md (four CVO rows): the surprise-row gate REFUSED all four with 'NEW row ESTATE_GOVERNANCE-C-S<k> carries C- outside adjudications/ -- C- is the CVO's coordinate for its adjudication rows (annex 4a) and lives nowhere else', schema and corpus clean (documents=30 rows=339, 0 new). At source @3860dae133: `_folder_identity` (.tools/surprise-row-gate.py:66-78) returns `(project, None)` for the FLAT spelling -- its docstring says 'Flat: the <PROJECT>/ directory (kind is the filename's)' and its code returns None -- and `_coordinate_violations` (:420-422) refuses any C- row when `folder_kind != \"ADJUDICATION\"`. So the CVO's L9 document for every flat channel (nineteen flat codes plus ESTATE_GOVERNANCE) cannot carry the CVO's coordinate without the audited override, although the same file is recognised as an adjudication document by FLAT_CHANNEL_RE (:58-59), ADJUDICATION_PATTERNS (:128-129), `_is_adjudication_doc` (:288-290), safe-commit's selector (@9aa3520831) and annex v3.6 (the ESTATE_GOVERNANCE home names exactly this path). The fifth carrier of one miss today: four readers know the flat spelling and the one limb that grades its coordinate does not. The four documents land in this commit under the audited override, stated so the workaround is not mistaken for the fix.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (surprise-row-gate.py is the CTO's tool)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The refusal, verbatim from safe-commit's stage at 21:3xZ on this seat's commit: 'ERROR: BLOCKED -- surprise-channel row gate (steps 7/10). Commit aborted; files unstaged. [surprise-row-gate] BLOCKED -- 4 violation(s) on NEW rows: org/surprise_channel/ESTATE_GOVERNANCE/ADJUDICATION_v1.md: NEW row ESTATE_GOVERNANCE-C-S1 carries C- outside adjudications/ ...' (the same line for C-S2, C-S3, C-S4); beside it '[surprise-row-gate] .../ADJUDICATION_v1.md: 4 new row(s) of 4 total checked' and '[surprise-corpus] DENOMINATORS: documents=30 rows=339 ... new=0' -- the rows are schema-valid and the corpus is clean; the coordinate limb alone refuses.",
        "At source, HEAD @3860dae133 (1.0.0_SA_CTO, 2026-09-04T21:32:43Z), read at this seat: :58-59 FLAT_CHANNEL_RE matches `org/surprise_channel/<CODE>/(INVESTIGATION|ADJUDICATION|REMEDIATION)_v*`; :66-78 `_folder_identity` -- docstring 'Flat: the <PROJECT>/ directory (kind is the filename's)', code `if m: return m.group(2), None` for the flat match (the tree match returns `m.group(3).upper().rstrip(\"S\")`); :420-422 `if folder_kind != \"ADJUDICATION\": out.append(... carries C- outside adjudications/ ...)`; :288-290 `_is_adjudication_doc(path)` returns `\"ADJUDICATION\" in basename.upper()` and is not consulted by the coordinate limb; :128-129 ADJUDICATION_PATTERNS includes `org/surprise_channel/%s/ADJUDICATION_v*` for the id-sequence census. A right sentence in the docstring beside a wrong return -- the shape 1.0.0_SA_CTO named twice today (94280, 94290).",
        "The other readers of the flat spelling agree with the annex, not with the limb: safe-commit.sh:725 @9aa3520831 selects `*org/surprise_channel/*ADJUDICATION_v*`; surprise-corpus-validate.py:151 @e29c5a0bb8 admits `org/surprise_channel/[^/]+/[^/]+\\.(md|json)`; the ESTATE_GOVERNANCE INVESTIGATION_v1.md header names `org/surprise_channel/ESTATE_GOVERNANCE/ADJUDICATION_v<N>.md` as the CVO's document; annex v3.6 section 4 names the flat home.",
        "Coverage of the class: the tree spelling is unaffected (NFRA_CLDGRPH's adjudications/ADJUDICATION_v1.md carried C-S9 and C-S10 at 2678835bfb with no override); every FLAT channel is affected -- 19 legacy flat codes under org/surprise_channel/ plus ESTATE_GOVERNANCE -- and none has carried a C- row before this commit, which is why the limb's flat arm was never exercised."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Annex v3.6 section 4 / 4a: the flat channel's adjudication document is org/surprise_channel/<CODE>/ADJUDICATION_v<N>.md and the CVO's rows there carry <CODE>-C-S<k>; the gate's own FLAT_CHANNEL_RE and the docstring of _folder_identity say the flat file's kind is the filename's.",
    "world_is": "The coordinate limb's kind comes from the tree sub-folder alone; a flat adjudication document has no sub-folder, the function returns None against its own docstring, and the limb refuses the CVO's coordinate on every flat channel. The lawful escape is the audited override, which is what this commit uses.",
    "notes": "Remedy (the CTO's, one line): `_folder_identity` returns `m.group(3).upper()` for the flat match, as its docstring already says -- or the coordinate limb consults `_is_adjudication_doc(rel)` when folder_kind is None. Exercise: this document's rows admitted without override; a C- row in a flat INVESTIGATION_v file still refused (narrowness); the tree arm unchanged. Disarm: one CVO commit of a flat ADJUDICATION_v document admitted without override, read at this seat. Adjudicated by the CVO in this commit (C-S5) and closed when the act lands."
  }
]
```

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S6",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T16:10Z",
    "one_line": "A MODIFICATION to a NON-TERMINAL tree task order's grant fields (`<issued_to>`, the `<paths>` block) is graded by none of the three controls the ANY-lane note names -- to-pipeline-gate grades NEWLY-ADDED orders at issuance (:699 'THIS GATE NEVER REFUSES AN EXISTING TO'), the proof-of-spec hook grades issuance, check_complete_flip grades the TERMINAL flip (LAYER 1 half B, :1573, modify-scoped for that one question) -- and the member was EXERCISED twice on 2026-09-05 in NFRA_OUTSET: afa659557d (0.9.0_WK_NFRA_OUTSET~3) and 26a8bc43f8 (0.9.0_WK_NFRA_OUTSET~2), both faithful carries of the issuer's amendment @b630052d6a by the prescribed path-scoped checkout, which copies content without history. Found by 0.0.0_AB_MSTR with 0.0.0_AB_MSTR~Z (94375, 94378), measured on the hot path by 2.0.0_SA_COO (94382, 94391, 94401), a first authorship-keyed limb built and reverted unshipped by 1.0.0_SA_CTO (94388), the design constraint -- provenance cannot be an ancestry test -- measured by 0.0.0_AB_MSTR (94398). FILED HERE BY THE CVO because the finding travelled only by broker message and a message is never the carrier; this row is what the CTO's limb disarms against.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RE-DERIVED AT THIS SEAT with a different instrument than any of the three seats quoted (an anchored regex over `git show --format= <commit>`, positive-controlled by requiring exactly two anchored lines per commit): afa659557d (0.9.0_WK_NFRA_OUTSET~3 2026-09-05T00:52:32-04:00): files NFRA_OUTSET.TO-OS-s-15.reachability-of-the-heat-engine-legs.proof_of_spec.json,reachability-of-the-heat-engine-legs.result.md,INVESTIGATION_v1.md,NFRA_OUTSET.TO-OS-s-15.reachability-of-the-heat-engine-legs.md, anchored <issued_to> diff lines ['-<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>', '+<issued_to>0.9.0_WK_NFRA_OUTSET~3</issued_to>'], 3 line(s) touching a <paths> block; 26a8bc43f8 (0.9.0_WK_NFRA_OUTSET~2 2026-09-05T00:45:32-04:00): files NFRA_OUTSET.TO-OS-s-8.comp-similar-heat-weighting-consumes.md, anchored <issued_to> diff lines ['-<issued_to>0.9.0_WK_NFRA_OUTSET~1</issued_to>', '+<issued_to>0.9.0_WK_NFRA_OUTSET~2</issued_to>'], 0 line(s) touching a <paths> block. So both commits are worker-authored modifications of an existing order's `<issued_to>` and neither added a `<paths>` line -- 2.0.0_SA_COO's bounded negative reproduced.",
        "THE POPULATION, cited to the seat that measured it and not re-run here: 12 self-granting tree orders, 5 non-terminal, from 0.0.0_AB_MSTR~Z's production parser (`_paths_block_entries` + `_order_grants`) over the 104-file tree population with a status-reader positive control (complete 66 / pending 28 / staged 7 / withdrawn 3) -- 94375 s.4; 0.0.0_AB_MSTR's own 27/4 by text match over 2,345 blobs is disclosed there as NOT the number to quote.",
        "THE PERMIT, measured by 0.0.0_AB_MSTR with the CLI the hook runs (94375 s.1): three unrelated serials PERMIT on TO-CG-D-1 and REFUSE on org/modules/heatmap/heat_map.py -- the lane is ANY by 2.0.0_SA_COO's registry note of 2026-09-03 on Andrew's word ('worker agents should be able to commit freely to the directives folder path as thats where their work is'), with its residual disclosed in the note. This row does not contest the lane.",
        "WHY NEITHER AUTHORSHIP NOR ANCESTRY DISCRIMINATES: 1.0.0_SA_CTO's gate (vi) keyed on 'is the committer the assignee' would have refused both carries (and `_base()` collapsed the `~n` slot, reading every worker of a project as one identity) -- 94388; 0.0.0_AB_MSTR measured b630052d6a as an ancestor of NEITHER carry though it predates both by 9 and 16 minutes, positive control afa659557d is-ancestor of itself -- 94398; 2.0.0_SA_COO named the cause: the hand-offs prescribed `git checkout CLOUD -- <the order file>`, content without history, chosen to spare live worker branches a conflict on the append-only channel -- 94401. And a plain `git log -- <file>` lookup drops the amendment commit itself under history simplification (5 vs 24 with --full-history) -- 94391."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The registry note for `org/missions/*/*/*/task-orders/**: lane: ANY` names three compensating controls as the guard the lane no longer provides ('THE GATES ARE THE CONTROL, not the lane'). Rule 22: verifying each member certifies the set while what the members share goes unchecked; Rule 24 (i): MECE over a declared domain -- hunt the uncovered member.",
    "world_is": "The three controls span issuance and the terminal flip and not the space between, so a worker can widen its own grant in two individually legal commits that no gate inspects. The legitimate transport of an issuer's amendment and the self-widening escalation are the same commit shape, and the prescribed transport strips the history a gate would read, so the discriminator must be PROVENANCE measured repository-wide and time-bounded: did an ISSUER-authored commit anywhere in the object graph, at or before the carry, set this field to this value. Exercised population to date: 2 grant-field modifications by workers, both faithful; 0 `<paths>` lines added by any worker in NFRA_OUTSET.",
    "notes": "DISARM (owner 1.0.0_SA_CTO, the L6 neck's author, who has said the limb is being designed and not rushed in front of live workers): a provenance limb at LAYER 1 half B with (i) a repository-scoped, time-bounded lookup -- `--full-history` or the object graph, never a simplified `git log -- <path>` and never ancestry -- (ii) a positive control in its self-test that a KNOWN faithful transport (afa659557d) returns MATCH and a KNOWN invented value returns DIVERGES, and (iii) its residual stated on its own output; ACK by a new row from 1.0.0_SA_CTO citing the commit. The residual's acceptability is ruled at ADJUDICATION_v1.md C-S7. This row asks for nothing beyond what the CTO has already undertaken; it gives the undertaking a row to close against."
  }
]
```

## S7 -- the row gate's rowlessness limb does not resolve an item through its adjudication row (filed on the CTO's order, INERT)

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S7",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:45Z",
    "one_line": "The row gate's rowlessness limb compares ids exactly, so an item whose remedy is carried under its adjudication row's id reads 'graduated with no remediation row'. Filed once on the CTO's order; repaired when a LIVE project is refused by it, not before.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.0.0_AB_MSTR",
    "spec_asserts": "`.tools/surprise-row-gate.py` `_graduated_without_row` (def at :908) refuses a new remediation row while a graduated item of the project has none: the limb is meant to find graduations nobody carried.",
    "world_is": "The limb takes the set of ids that remediation rows bear and subtracts it from the graduated item ids. It does not resolve an item through the adjudication row that graduated it. Two older conventions therefore read as rowless: (a) a worker-form item whose clocks were written on the adjudication row itself, and (b) a remedy carried on a remediation row keyed by the adjudication row's id. Across the estate 158 remediation rows bear an adjudication-row id (some are the remedy of the adjudication's own finding, so 158 is an upper bound on class (b), not its size). On closed projects this is worked around by dismissals (batch 77 item 2); the limb is correct on a live project until one is refused for this reason.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`_graduated_without_row` source read at this seat 2026-10-01: exact-id set difference",
        "census at this seat 2026-10-01 over every tree and legacy channel through the gate's own `_remediation_ids_for_project`: 158 remediation ids matching `-C-S<n>`",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/SURPRISE_CHANNEL_BACKLOG_CENSUS_20261001.md addendum @6c620c531a: 852 rowless graduated items, 313 not site Z's, 260 BLOCKING or ARMED",
        "1.0.0_SA_CTO RULINGS batch 77 item 4 @4b9e65f744: 'THE LIMB'S OWN GAP IS ONE ROW, not an order ... owner 0.0.0_AB_MSTR (fabric tooling), standing INERT. It is repaired when a LIVE project is refused by it, not before.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Un-park condition: a commit by a seat on an OPEN project is refused by this limb for an item whose remedy is carried under its adjudication row's id."
  }
]
```

## S8 -- re-filed from NFRA_OUTSET-W1-S21: `deployed_state` has no value for a deploy-scope artifact committed and deliberately not deployed

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S8",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:45Z",
    "one_line": "RE-FILED from NFRA_OUTSET-W1-S21: the proof-of-spec schema's `deployed_state` has no value for a deploy-scope artifact that is committed and deliberately not deployed, so an instance records the least-wrong value.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "org/standards/PROOF_OF_SPEC.schema.json closes `deployed_state` to an enum, and CLAUDE.md section 4 requires a value to carry its claim in a field a consumer can reject on.",
    "world_is": "The enum at HEAD is still {DEPLOYED-VERIFIED, COMMITTED-NOT-DEPLOY-SCOPE, STAGED-AWAITING-GATE}. A deploy-scope artifact that a cell commits and is not allowed to deploy fits none: COMMITTED-NOT-DEPLOY-SCOPE is false, and STAGED-AWAITING-GATE asserts a gate that may not exist. A reader of the field takes an undeployed artifact for one waiting on a named gate. The remedy is a schema decision (a fourth value, or a ruling that STAGED-AWAITING-GATE covers the case), and a value-enum change carries its rule-24 record.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/PROOF_OF_SPEC.schema.json at HEAD, read at this seat 2026-10-01: three enum values, as the old row says",
        "old row NFRA_OUTSET-W1-S21 (org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/), graduated at NFRA_OUTSET-C-S4 with owner 1.0.0_SA_CTO and no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md): a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel, because the hazard is a fabric tool or standard and directives D0 and D11 (the old rows' directives) have no open member project; filing it in an unrelated open project would put an ARMED row in front of that project's L10. Not measured: how many proof-of-spec instances at HEAD record STAGED-AWAITING-GATE for an artifact with no gate."
  }
]
```

## S9 -- re-filed from NFRA_OUTSET-W1-S17: `comp-heat federated --sql` is unrestricted under a read-only docstring

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S9",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:45Z",
    "one_line": "RE-FILED from NFRA_OUTSET-W1-S17: `comp-heat federated --sql` sends the caller's SQL to Trino unread, under a module docstring that says the tool is read-only and never writes to any store.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "`.tools/comp-heat`'s own module docstring: ADVISORY-ONLY and READ-ONLY, never writes to the repo or any store.",
    "world_is": "At HEAD `.tools/comp-heat:860-861` returns the `--sql` string as the statement to run, and `.tools/_trino_fed.py` carries no statement inspection (0 occurrences of a read-only guard, a refusal, or any of INSERT, DELETE, DROP, UPDATE, CREATE). Whether a write would succeed depends on the Trino identity's grants, which this seat did not read; the tool's stated contract is not enforced by the tool on the one path that could break it. The remedy is the tool owner's choice between narrowing the docstring and restricting the surface.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-heat:860-861 and the docstring, read at this seat 2026-10-01",
        ".tools/_trino_fed.py token census at this seat 2026-10-01: read-only 0, refus 0, write verbs 0, select 2",
        "old row NFRA_OUTSET-W1-S17, graduated at NFRA_OUTSET-C-S4 (owner then 0.8.0_AE_CloudComp; comp-heat's registry owner is 1.0.0_SA_CTO by its header) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md): a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel, because the hazard is a fabric tool or standard and directives D0 and D11 (the old rows' directives) have no open member project; filing it in an unrelated open project would put an ARMED row in front of that project's L10. Not measured: the Trino identity's write grants, so the standing is the row's original and not a demonstrated write."
  }
]
```

## S10 -- re-filed from NFRA_OUTSET-W1-S13 and W2-S10: two traps a worker cannot re-derive are in no worker face or doctrine

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S10",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:45Z",
    "one_line": "RE-FILED from NFRA_OUTSET-W1-S13 and NFRA_OUTSET-W2-S10: two traps a worker cannot re-derive at the call site are in no worker face, worker definition or doctrine file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md rule 22a exists to carry instrument traps 'you cannot re-derive at the call site'; rule 27 makes the task order's worker face the worker's whole context.",
    "world_is": "(1) In the Bash tool `cd X && A & B; C` backgrounds the whole `cd X && A` list, so B and C run in the session's default directory, which for a worker is the MAIN workspace: a worker ran the main tree's copy of a test and wrote a file there believing it was in its worktree. (2) Running a COPY of a comp-tool from a scratch directory, or exec-ing it in-process, fail-softs on `__file__` and returns clean-looking false results in opposite directions. Neither is stated in `.claude/agents/worker.md` (0 lines mentioning backgrounding) or in docs/doctrine/CLAUDE_ANNEX.md (0 matches for a copied comp-tool or `__file__`). The stray file of (1) is gone from the main tree's .scratch/. The remedy is one line each where a worker reads it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".claude/agents/worker.md and docs/doctrine/CLAUDE_ANNEX.md at HEAD, read at this seat 2026-10-01: no statement of either trap",
        ".scratch/os2_falsifier.txt: absent at this seat 2026-10-01 (the old row's first limb is moot)",
        "old rows NFRA_OUTSET-W1-S13 and NFRA_OUTSET-W2-S10, graduated at NFRA_OUTSET-C-S4 with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md): a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel, because the hazard is a fabric tool or standard and directives D0 and D11 (the old rows' directives) have no open member project; filing it in an unrelated open project would put an ARMED row in front of that project's L10."
  }
]
```

## S11 -- re-filed from NFRA_OUTSET-W1-S14: the graph_nodes metadata prefix still cannot be listed in-band

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S11",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T11:45Z",
    "one_line": "RE-FILED from NFRA_OUTSET-W1-S14: the graph warehouse's graph_nodes metadata prefix still cannot be listed in-band; a summarised listing did not finish in 280 seconds.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "infra/aws/globgrph/derive_runner.py:505-535 describes a nightly Nessie-ref-aware mark and sweep over warehouse/globgrph/ that bounds historical-snapshot accumulation.",
    "world_is": "`aws s3 ls --recursive --summarize` of s3://opal-313476888478-globgrph/warehouse/globgrph/graph_nodes_4c6c23bd-fffa-427e-9cd9-7a9deaa3426d/metadata/ was terminated by this seat's 280-second bound before it printed a total, so today's object count is NOT obtained. On 2026-09-05 the old row counted 183,447 objects on the table, 134,616 under metadata/, 20,374 of them metadata.json files with none expired. A prefix that cannot be listed in 280 seconds is not one a sweep has brought to 'one overwrite's worth of files'. Either the sweep does not run, or it does not reach this prefix; which one was not read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the listing run at this seat 2026-10-01 11:36Z-11:41Z: exit 143 at the 280 s bound, no total printed",
        "infra/aws/globgrph/derive_runner.py:505-541 at HEAD: the maintenance design and `_MAINT_SWEEP_PREFIX = \"warehouse/globgrph/\"`",
        "old row NFRA_OUTSET-W1-S14, graduated at NFRA_OUTSET-C-S4 (the globgrph lane via the CTO) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 (org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md): a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel, because the hazard is a fabric tool or standard and directives D0 and D11 (the old rows' directives) have no open member project; filing it in an unrelated open project would put an ARMED row in front of that project's L10. Not measured: the object count today, whether the sweep is scheduled, and its last run. A slow listing is also what a slow network looks like; one run does not separate them."
  }
]
```

## S12 -- re-filed from NFRA_CLDGRPH-W1-S11 and W1-S27: the halt gate resolves a seat's identity from a session file only

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S12",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W1-S11 and W1-S27: `.tools/halt-gate-check.sh` never reads OPAL_AGENT_SERIAL, so a worker's first safe-apply in a fresh worktree is refused IDENTITY UNRESOLVED until it writes a runtime file no task-order face names.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md rule 27: the task order's worker face is the worker's whole context; the fabric's other identity readers prefer OPAL_AGENT_SERIAL.",
    "world_is": "0 occurrences of OPAL_AGENT_SERIAL in .tools/halt-gate-check.sh at HEAD. The refusal fails closed and prints its own remedy, so the cost is one refused call and one file written outside the worker's named paths, on every fresh worktree that applies. The durable fix was named as one line in the resolver.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh token count at HEAD (this seat, 2026-10-01): 0",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S24 and C-S31 with owner 1.0.0_SA_CTO and no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. Not exercised today: no apply was attempted from a worker identity."
  }
]
```

## S13 -- re-filed from NFRA_CLDGRPH-W2-S19: proof-of-spec-check's `introduces` rung matches substrings

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S13",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W2-S19: proof-of-spec-check's `introduces` rung is a substring match, so a token is 'already present at the parent' when a longer word contains it, and a real introduction is refused.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": ".tools/proof-of-spec-check.py:239-259: a row's `introduces` tokens must be present at the pin and absent at the parent.",
    "world_is": "Lines 274 and 279 at HEAD test `t.encode('utf-8') in here` and `in parent`: a byte-substring test with no word boundary. The old instance was `connect` read as present because the parent held `connection` in a comment. It fails closed (a valid row is refused), and the workaround the row measured costs a second commit that invalidates the instance's other artifact rows.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/proof-of-spec-check.py:270-280 at HEAD (this seat, 2026-10-01)",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S24 with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10."
  }
]
```

## S14 -- re-filed from NFRA_CLDGRPH-W1-S24: the vendored jq emits CRLF and no doctrine line says so

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S14",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W1-S24: `.tools/jq.exe` emits CRLF, so a jq-written TSV read by shell field-splitting carries a trailing CR in its last field; the trap is in no doctrine file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md rule 16 names `.tools/jq.exe` as vendored and rule 22a carries the instrument traps a seat cannot re-derive.",
    "world_is": "CLAUDE.md mentions jq once (resolve it first, fail closed) and says nothing of line endings; docs/doctrine/CLAUDE_ANNEX.md has 0 lines pairing jq with CRLF. The old row measured 4 of 4 lookups failing on a last field ending in CR. The aws shim's CR is handled by `tr -d '\\r'` at the call sites that know; jq is the second carrier.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md:257 and an annex search at HEAD (this seat, 2026-10-01)",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S24 ('the doctrine line is the CTO's') with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. Not re-measured today: jq's output bytes."
  }
]
```

## S15 -- re-filed from NFRA_CLDGRPH-W4-S4, W4-S6, W6-S3 and W7-S2: instruction surfaces still describe the retired graph engine

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S15",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W4-S4, W4-S6, W6-S3 and W7-S2: the graph call manifest and three modules still describe or route to the retired local graph engine, and rule 20 sends every seat to that manifest.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md rule 20: pick the graph call from org/modules/graph/graph-call-manifest.yaml. The local store is retired; the served projection is the one graph.",
    "world_is": "At HEAD: the manifest's `freshness:` at line 1290 still names db-path infra/aws/globgrph/kuzu_stitch_db, a directory that does not exist, and .tools/tool_index.py mirrors it; 11 of the manifest's 129 entries carry a comp-aws subcommand as canonical_call with status canonical, including the write paths the old row says Andrew's word deprecated; org/modules/graph/comp_ws4_crosswalk.py:6-12, comp_debt/grounding_lib.py:195-203 and comp_legacywriter.py:235-239 still describe the local marker-head engine. The one canonical entry that calls comp-kuzu (cloud.read.served_vintage) works: this seat used it today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "manifest and module reads at HEAD (this seat, 2026-10-01): line 1290; 11 comp-aws canonical entries of 129; the three module sites",
        "infra/aws/globgrph/kuzu_stitch_db: absent on disk",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S50 and C-S56 (owner 1.0.0_SA_CTO, the manifest owner executes) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. Not read: the cost and rebuild_trigger fields of cloud.cluster.page_panel_drilldown (W4-S6's two fields)."
  }
]
```

## S16 -- re-filed from thirteen NFRA_CLDGRPH rows: the served graph carries no STORED_IN edge while its producer still emits the family

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S16",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W2-S68, W2-S70, S96, S97, S102, W1-S37, W1-S38, S110, S113, W1-S39, S111, W3-S18, W1-S47 and W2-S61: the served graph has 0 STORED_IN edges today, derive_stitch.py still emits them, and SERVED_FROM's 27 edges still land on bucket-POLICY nodes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "infra/aws/globgrph/derive_stitch.py:17 and :339: S3_DATA_KEY -[STORED_IN]-> S3_BUCKET is 'THE boundary edge' and the producer builds it.",
    "world_is": "The served projection (vintage 2026-10-01T12:02Z, stitch source built 2026-09-30T03:01:20Z) answers: OWNED_BY to S3_BUCKET 232, OWNED_BY to MS_USER 7,057, SERVED_FROM to S3_BUCKET_POLICY 27, and no STORED_IN edge at all; node types S3_BUCKET 41 and S3_BUCKET_POLICY 17 both exist, which is what the round-9 key-collision fix was for, and the running updater equals HEAD. The retirement of STORED_IN was ruled NOT done under four conditions and the family was twice seen dropping to zero unexplained; today's zero cannot be told from either. A consumer asking which bucket a data key is stored in gets nothing and no refusal. The producer's input also still contains its own prior output for edge kinds other than STORED_IN (derive_stitch.py:568).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-kuzu, two Cypher reads over CloudEdge.edge_type and CloudNode.node_type (this seat, 2026-10-01 12:02Z-12:04Z), vintage line as printed",
        "git grep of STORED_IN over the graph producers at HEAD: the emitter at derive_stitch.py:339, SOLE_WRITTEN_EDGE_TYPES at :91, PRIOR_CYCLE_DROP_REQUEST at :108",
        "opal-globgrph-incremental-updater: the deployed lambda_function.py hashes equal to HEAD's (this seat's download, 2026-10-01); LastModified 2026-09-10T21:07:39Z",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S60, C-S65, C-S79 and C-S85 (lane 0.8.0_AE_CloudComp through the CTO) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. Not measured: how many STORED_IN edges the last stitch build emitted, so whether the zero arises at the producer, the fold or the projection is open. This is the one row of the set a graph consumer would act on."
  }
]
```

## S17 -- re-filed from NFRA_CLDGRPH-W3-S10: last night's cloud stitch build failed

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S17",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W3-S10: the cloud stitch producer now succeeds (7 of the last 8 nightly builds) but the 2026-10-01 03:00Z build FAILED on derive_stitch.py exit 2, and a failed night leaves the previous artifact in place.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "opal-stitch-produce runs nightly on cron(0 3 * * ? *) and the served graph's stitch layer is its output.",
    "world_is": "The eight most recent builds, all rule-initiated: seven SUCCEEDED (2026-09-24 through 2026-09-30) and the latest, started 2026-10-01T03:00:12Z, FAILED in the BUILD phase after 38 s on `python3 infra/aws/globgrph/derive_stitch.py --out /tmp/stitch_graph.json`, exit status 2. The old row's claim (never succeeded, 67 of 67) is no longer true. The served vintage line does disclose the stitch's age ('Stitch source: stitch-codebuild built 2026-09-30T03:01:20Z'), so a reader of that line can see a missed night; nothing else says so. One failed night is one day of stitch age; whether it repeats is tonight's build.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "codebuild list-builds-for-project and batch-get-builds for opal-stitch-produce (this seat, 2026-10-01 11:56Z): 8 builds read, statuses and the failed phase as stated",
        "the comp-kuzu vintage line read at 12:02Z",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S34 with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. Not read: the failed build's log, so the cause of exit 2 is unknown. No alert is proposed (standing moratorium)."
  }
]
```

## S18 -- re-filed from NFRA_CLDGRPH-W1-S8: the resource-summaries producer has no trigger

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S18",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W1-S8: globgrph-resource-summaries-producer still has no rule and no schedule, so it runs only when someone starts it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md section 5: production pipelines must be scheduled.",
    "world_is": "No EventBridge rule and no EventBridge Scheduler schedule has a name containing 'summar' other than exec-summary-trigger, which is another pipeline's. The old row found the task definition referenced only by a Terraform output. Declare a trigger or retire the producer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "events list-rules and scheduler list-schedules filtered on the name (this seat, 2026-10-01 12:08Z)",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S24 (lane 0.7.0_AE_CloudOps) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. The read is by NAME: a trigger named without 'summar' whose target is this task definition would be missed. Not read: the age of the producer's output."
  }
]
```

## S19 -- re-filed from NFRA_CLDGRPH-W3-S16: a test file that collects zero tests

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S19",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W3-S16: infra/aws/globgrph/tests/test_kuzu_incremental_refresh.py collects zero tests under pytest, so any order naming it in a pytest invocation gets a green that checked nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "A task order's mechanical criterion names an invocation and an expectation (CLAUDE.md rule 27).",
    "world_is": "`python -m pytest infra/aws/globgrph/tests/test_kuzu_incremental_refresh.py --collect-only -q` prints 'no tests collected'. The file is a main()-style self-test. The remedy is a collectable surface or the file's removal from pytest paths.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the collect-only run (this seat, 2026-10-01 12:08Z)",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S48 (lane 0.8.0_AE_CloudComp) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10."
  }
]
```

## S20 -- re-filed from NFRA_CLDGRPH-W1-S43: a dated snapshot key is overwritten in place on an unversioned bucket

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S20",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W1-S43: the graph bucket is still unversioned, so a dated snapshot key that a record cites can be overwritten and the cited bytes are then gone.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "Records cite s3://opal-313476888478-globgrph/snapshots/<date>/graph-<date>.tar.gz as if a dated key were immutable.",
    "world_is": "`get-bucket-versioning` on opal-313476888478-globgrph returns no Status today. Round 9's TO-CG-I-4 measured 118 citations of dated keys in 539 files (21 still valid, 12 overwritten, 85 undecidable) and chose a writer-side key as the remedy, filed with two blockers and not implemented before the close.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-bucket-versioning (this seat, 2026-10-01 11:56Z): empty",
        "TO-CG-I-4's status line in org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S72 (lane 0.8.0_AE_CloudComp) whose remediation row exists only in an untracked draft, REMEDIATION_v4.md",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10."
  }
]
```

## S21 -- re-filed from NFRA_CLDGRPH-W2-S72, S104 and S106: every graph derive publishes to a topic with an SMS subscription (reserved for Andrew)

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S21",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:15Z",
    "one_line": "RE-FILED from NFRA_CLDGRPH-W2-S72, S104 and S106: the critical-surface alert topic still has an SMS subscription, and the old rows measured every graph derive, nightly included, publishing a SEV1 page and a digest to it. The call was RESERVED FOR ANDREW and the project closed without his answer on record.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "The old rows' handling: nothing is unsubscribed or edited by a seat; the question is Andrew's.",
    "world_is": "`sns list-subscriptions-by-topic` on opal-critical-surface-alerts returns two subscriptions, protocols sqs and sms (endpoints not printed here). The derive's two publishes per run were measured on 2026-09-10 and not re-read today. If both still hold, a phone is paged once a night by a scheduled run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sns list-subscriptions-by-topic, protocols only (this seat, 2026-10-01 11:56Z)",
        "old rows in org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/, graduated at NFRA_CLDGRPH-C-S60 ('RESERVED FOR ANDREW, hold in force') with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744: a hazard of a closed project that is live today is re-filed as a new row in an open channel, citing the old id; the old row is dismissed with that pointer",
        "NFRA_CLDGRPH was closed 2026-09-23 on Andrew's word, 'a close on his word, not a graded close' with no outcome claimed REALIZED (project.json close_note), so its open items were never worked off"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Home: this channel. D0 has no open member project, and the graph pipeline has no project with a seat today; filing in an unrelated open project would put an ARMED row in front of that project's L10. Not read: the derive log for last night's publishes; whether the subscription is wanted. This seat changes nothing here. It belongs in the CTO's open calls for Andrew."
  }
]
```

## S22 -- re-filed from ETFS_GUARDRAIL-W1-S19: today's 14:00Z monthly ETF report is expected to publish without the logo

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S22",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:45Z",
    "one_line": "RE-FILED from ETFS_GUARDRAIL-W1-S19, with a clock: the monthly ETF report fires today at 14:00Z (cron(0 10 1 * ? *) America/New_York) and the renderer the report host pulls still resolves the Opal logo from a path that does not exist on that host, so the scheduled September report is expected to publish, and to be emailed, with an empty brand bar.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "data/etfs/scripts/presentation/render_month_end.py:134-145 `opal_logo_svg()` inlines the white Opal logo into the report's navy brand bar.",
    "world_is": "The function reads <renderer dir>/../../../../portal/public/logos/opal-logo-white.svg and returns an empty string on any error. The orchestrator runs the renderer on the report host from /opt/etfs-reports after copying it from s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py; that object hashes equal to CLOUD HEAD's file (77,130 bytes), so the host will run this resolver, and from /opt/etfs-reports the path resolves outside any portal checkout. The old row measured the effect on the served August report: five inlined logo SVGs gone, 62,420 to 43,376 characters, every number identical; the served August HTML today is 43,376 bytes. The adjudication (ETFS_GUARDRAIL-C-S14) armed it at the CTO: 'until it lands the 10-01 fire publishes a brand-less report, which is a disclosure the CTO should make deliberately rather than discover'. The project closed without it landing. Schedule etfs-reports-monthly-run is ENABLED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scheduler get-schedule etfs-reports-monthly-run (this seat, 2026-10-01 12:37Z): cron(0 10 1 * ? *), America/New_York, ENABLED",
        "s3 cp of the renderer object and sha256 against HEAD (this seat, 2026-10-01 12:43Z): equal; the Lambda's REPORTS_ARTIFACT_PREFIX is set to that same prefix",
        "the deployed etfs-reports-orchestrator lambda_function.py hashes equal to HEAD (this seat's download, LastModified 2026-09-10T17:44:50Z)",
        "s3api list of platinum/reports/2026-08/: etf_ownership.html 43,376 bytes",
        "old row ETFS_GUARDRAIL-W1-S19, graduated at ETFS_GUARDRAIL-C-S14 with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not read: whether the logo file exists at the resolved path on the host (the old row says it does not). This seat changes nothing: the choices (let it publish as is and say so, or land a fix before 14:00Z, or hold the fire) are the CTO's and, for a hold of a scheduled delivery, Andrew's. Cosmetic: every figure in the report is unaffected."
  }
]
```

## S23 -- re-filed from ETFS_GUARDRAIL-W1-S5: the shared Lambda zip builder sets an impossible timestamp and has two callers

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S23",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:55Z",
    "one_line": "RE-FILED from ETFS_GUARDRAIL-W1-S5: infra/aws/lambda/ci/build-zip.sh:66 still runs `touch -t \"202600010000\"` (month 00), which the old row measured failing rc=1 on every invocation, and the script is called by a GitHub workflow and by verify-local.sh.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "build-zip.sh normalises member timestamps so a rebuilt zip hashes reproducibly.",
    "world_is": "Line 66 at HEAD is unchanged. The old row found zero callers on the round's deploying path; a caller census today finds .github/workflows/lambda-deploy.yml and infra/aws/lambda/verify-local.sh naming the script. The fix is one literal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/build-zip.sh:66 at HEAD and `git grep -l build-zip.sh` outside org/ and docs/ (this seat, 2026-10-01)",
        "old row ETFS_GUARDRAIL-W1-S5, graduated at ETFS_GUARDRAIL-C-S3 (lane CloudOps or ETL) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a closed project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not run today: the script itself, so the rc=1 is the old row's measurement. Not read: whether the workflow is still triggered by anything."
  }
]
```

## S24 -- re-filed from ETFS_GUARDRAIL-W2-S1: the ETF ownership function's own test dies at import

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S24",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:55Z",
    "one_line": "RE-FILED from ETFS_GUARDRAIL-W2-S1: infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py still errors at collection on a missing environment key, so the function's own battery checks nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "The file is the daily ETF ownership function's test of its catch-up scan.",
    "world_is": "`python -m pytest <file> --collect-only` at this seat: 1 error during collection, KeyError 'FACT_POSITIONS_PREFIX' (with ASSETS_BUCKET set empty; the old row saw KeyError ASSETS_BUCKET), no tests collected. Dead since the 2026-08-03 repoint by the old row's dating. The remedy named then: re-vendor the battery against the repointed shape with real test functions.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the collect-only run (this seat, 2026-10-01 12:36Z)",
        "old row ETFS_GUARDRAIL-W2-S1, graduated at ETFS_GUARDRAIL-C-S3 (the inf-pipeline lane, named by the CTO) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a closed project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The deployed function is not in question here; only its test."
  }
]
```

## S25 -- re-filed from ETFS_GUARDRAIL-W2-S8: the Cottonwood ETF ownership fire still precedes its partition's landing

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S25",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:55Z",
    "one_line": "RE-FILED from ETFS_GUARDRAIL-W2-S8: rule cot-etf-ownership-daily-schedule still fires at 10:30Z; the old row measured the D+1 partition landing near 11:46Z, which leaves the newest Cottonwood trading day without a slice for about half a day, every day.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "The CTO took the finding for an L10 addendum (94796 (2a)): the fire follows the partition, or the window excludes the unlanded day and says so.",
    "world_is": "The rule reads cron(30 10 * * ? *), ENABLED, today; bd-49f-etf-ownership-scheduled-floor reads cron(45 10 * * ? *). The remedy is a Terraform act on the rule's cron in the DT/AE lane; the project closed before it was cut.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "events list-rules filtered on 'etf' (this seat, 2026-10-01 12:36Z)",
        "old row ETFS_GUARDRAIL-W2-S8, graduated at ETFS_GUARDRAIL-C-S9 (finding OPEN, owner 1.0.0_SA_CTO) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a closed project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not re-measured: today's landing time of the Cottonwood partition, so the size of the gap is the old row's."
  }
]
```

## S26 -- re-filed from NFRA_COMPEFFICACY-W2-S4: comp-adversary declares all sources run when one died on a decode error

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S26",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T12:55Z",
    "one_line": "RE-FILED from NFRA_COMPEFFICACY-W2-S4: `.tools/comp-adversary` reads its sources through subprocess with text=True and no encoding, so a non-cp1252 byte kills the reader thread and the tool still exits 0 declaring every source run.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.0.0_AB_MSTR",
    "spec_asserts": "CLAUDE.md section 4: in a file path that carries non-ASCII, every reader is explicit (`encoding='utf-8'`); and a producer's rc=0 is never trusted on its own.",
    "world_is": "At HEAD the tool has five subprocess calls; four pass text=True and none passes encoding= on the call (the tool's twelve encoding= occurrences are on file opens). The call at :309 reads `comp-state --json`, the source the old row saw truncated mid-record while the declaration read '5 run / 0 deferred-with-reason'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-adversary call-site census at HEAD (this seat, 2026-10-01): 5 calls, 4 text=True, 0 with encoding=",
        "old row NFRA_COMPEFFICACY-W2-S4, graduated at NFRA_COMPEFFICACY-C-S11 (owner 0.8.0_AE_CloudComp, the comp-tool rail) with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a closed project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not re-run today: the tool on an input that carries the byte. Owner set to 0.0.0_AB_MSTR per batch 85's reading that fabric-tool rows are that seat's."
  }
]
```

## S27 -- re-filed from ETFS_POSITIONING-Z-S1 and Z-S2: the Bloomberg daily ETF pull's as-of is holiday-blind and its tripwire cannot fire

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S27",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:32Z",
    "one_line": "RE-FILED from ETFS_POSITIONING-Z-S1 and Z-S2: integrations/bloomberg/pipeline/etf_daily_pull.py still takes its as-of from pandas BDay(-1), which knows weekends and no market holiday, and its tripwire compares that value with the same expression computed again.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md section 5: one frontier, lib/trading_calendar.py; the pull's exit 60 is documented as 'TRIPWIRE REFUSED -- as-of != BDay(-1)'.",
    "world_is": "Lines 122-125 at HEAD: `asof = today + BDay(-1)`, `expected = Timestamp.today().normalize() + BDay(-1)`, refuse if they differ. The control can differ from the value only if `today` is not today; it cannot catch a wrong as-of. The file imports no trading calendar. On the first fire after a market holiday the as-of is the closed day. The next exposure is the fire of Friday 2026-11-27 (Thanksgiving, 2026-11-26).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/bloomberg/pipeline/etf_daily_pull.py:117-125 at HEAD (this seat, 2026-10-01): five BDay lines, no trading_calendar reference",
        "old rows ETFS_POSITIONING-Z-S1 and Z-S2 (org/surprise_channel/ETFS_POSITIONING/INVESTIGATION_v1.Z.md), graduated in their own rows with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a finished project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not exercised: a run on a post-holiday date. What a closed-day as-of does downstream (a prefix dated on a closed day, a gold step keyed on it) was not traced."
  }
]
```

## S28 -- re-filed from ETFS_INGEST-Z-S10: a live scheduled rule with no Terraform

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S28",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:32Z",
    "one_line": "RE-FILED from ETFS_INGEST-Z-S10: rule opal-assets-silver-etf-sweep-daily is ENABLED at cron(30 23 * * ? *) and the name appears in no .tf file under infra/aws.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "Schedules are declared in Terraform; a live resource with no declaration is drift nobody's plan can see.",
    "world_is": "`events list-rules` returns the rule ENABLED today. A search of every tracked .tf file under infra/aws for the rule's name returns 0 files.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "events list-rules filtered on 'etf' (this seat, 2026-10-01 12:36Z); a token read of the rule name over tracked .tf files (0 hits)",
        "old row ETFS_INGEST-Z-S10 (org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md), graduated in its own row with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a finished project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The search is by literal name; a rule built from an interpolated name would be missed. Not read: the rule's target."
  }
]
```

## S29 -- re-filed from ETFS_INGEST-Z-S27: the served ETF payload cannot say whether a missing value is absent or failed

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S29",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:32Z",
    "one_line": "RE-FILED from ETFS_INGEST-Z-S27: platinum/etfs/positioning_data.json still carries no field that distinguishes 'this security has no such value' from 'the fetch failed', so a correct null and a failure render the same.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "CLAUDE.md section 4: a value must carry its claim in a field a consumer can reject on (measured, inferred, held, absent).",
    "world_is": "The served object (147,629 bytes, written 2026-10-01T13:01:31Z) has top-level keys data_as_of, data_as_of_spread, data_date, generated_at, note and portfolios; its text holds 0 occurrences of a claim, fetch-status or unavailable token. The old row records that this cost a false defect report on the first smoke test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3 cp of the served object and a token census (this seat, 2026-10-01 13:3xZ)",
        "old row ETFS_INGEST-Z-S27, graduated in its own row with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a finished project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not measured: how many nulls the payload carries today."
  }
]
```

## S30 -- re-filed from ETFS_INGEST-Z-S23 and Z-S17: two instrument facts a seat cannot re-derive

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S30",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:32Z",
    "one_line": "RE-FILED from ETFS_INGEST-Z-S23 and Z-S17: (1) opal-data-portal-v2 expires noncurrent object versions after 14 days, so 'the overwritten bytes are recoverable' is true for two weeks only; (2) comp-closure compares package members by raw bytes, so a correct deploy with different line endings reads as divergent.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.0.0_AB_MSTR",
    "spec_asserts": "CLAUDE.md rule 22a carries the instrument traps a seat cannot re-derive at the call site; comp-closure is the estate's code-layer instrument for deployed-versus-built.",
    "world_is": "(1) `get-bucket-lifecycle-configuration` on opal-data-portal-v2 today: rule expire-noncurrent-versions-14d, Enabled, 14 days. No doctrine line states it. (2) .tools/comp-closure's own header (lines 17-29) says the byte compare is RAW and names the fix (normalise per member and state which comparison was used); the fix is not in the tool.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-bucket-lifecycle-configuration (this seat, 2026-10-01 13:3xZ)",
        ".tools/comp-closure:17-29 at HEAD",
        "old rows ETFS_INGEST-Z-S23 and Z-S17, graduated in their own rows with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a finished project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Owner 0.0.0_AB_MSTR per batch 85's reading that fabric-tool rows are that seat's. Two remedies that do not move together: one doctrine line, one tool change."
  }
]
```

## S31 -- re-filed from ETFS_INGEST-Z-S5: a failed constituents leg of the Bloomberg pull summons nobody

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S31",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T13:32Z",
    "one_line": "RE-FILED from ETFS_INGEST-Z-S5: the old row found the morning freshness check reading only the Models artifact, so a failure of the ETF constituents leg is seen by nobody, and that leg's source is current-day-only, which makes a missed day permanent.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "spec_asserts": "integrations/bloomberg/READ_HERE.md: the derived layer is current-day-only.",
    "world_is": "Not re-measured today beyond this: the Bloomberg landing prefixes under opal-data-etfs/bbg/ run to 2026-09-30 (29 dated prefixes), so no day is missing at the frontier now. Whether any check reads the constituents leg was not read. Under the standing moratorium nothing is built here; this is an input to the alarm work the CTO named (GLOBALALARM), like row S21.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list-objects-v2 with a delimiter on bbg/ (this seat, 2026-10-01 13:3xZ): 29 prefixes, last 2026-09-30",
        "old row ETFS_INGEST-Z-S5, graduated in its own row with no remediation row",
        "1.0.0_SA_CTO RULINGS batch 77 @4b9e65f744 and batch 85 @afc17452e8: a finished project's live hazard is re-filed as a new row, and the estate-wide channel is the accepted home"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Carried on the old row's measurement. Standing ARMED because a single missed day cannot be recovered."
  }
]
```


## S32, S33 -- two BD gold runner findings from the grade of MDPF_SECCLASS BD thread r3 (3.0.0_SA_CVO)

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S32",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:05:00Z",
    "one_line": "The firm gold runners' freshness gate never runs: the BD runner prints 'WARN: comp-freshness not found in PATH -- freshness gate skipped.' on every start read, and the same skip line is coded in the cot and inf dispatchers; a change record noted the tool absent on the runner on 2026-07-15 and no channel row carries it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BD gold runner log copy (gold_incremental object read by this seat's grade of MDPF_SECCLASS BD thread r3, 2026-10-02 02:xZ): the WARN line on 2 of 2 starts in the prior log's last 9 MB and on 1 of 1 in the 2026-10-01 23:00Z run",
        "comp-find 'freshness gate skipped', corpus all, 10 hits across 214,365 files: the echo at data/black_diamond/scripts/gold/gold_dispatch.sh:1350, data/cot/scripts/gold/gold_dispatch.sh:1139, data/inf/scripts/gold/orion-gold-dispatch.sh:1794; org/critical_paths/change_management/GLDRNS_B1_AOR_RELEASE_WINDOW_20260715.md:104 'the tool is ABSENT on the runner'",
        "comp-find over org/surprise_channel and org/missions for the line: 0 hits across 12,712 files (no channel row)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The three dispatchers call a freshness gate before the gold build; a gate that cannot find its tool is meant to be the exception, since the dispatch code prints the skip as a WARN and continues.",
    "world_is": "On the BD runner the exception is the rule: no start read has run the gate, and the code path is the same in two other firms' dispatchers. Inputs are not refused for staleness on these runners. Not read: the cot and inf runner logs, and whether anything downstream is meant to rely on this gate.",
    "notes": "INERT: nothing reads the gate's verdict today, and the runs proceed. No monitor or alert is proposed (standing moratorium). For 1.0.0_SA_CTO's placement: provision the tool on the runner image, or remove the call and its WARN so the dispatch code stops claiming a gate it does not run. Owner of the runners: the DS and AE lanes."
  },
  {
    "id": "ESTATE_GOVERNANCE-S33",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:05:00Z",
    "one_line": "Four BD gold runner starts in two days end with no COMPLETE line: the runner's next start ('Runner updated from S3 -- re-executing new version') follows mid-step. The 21:47Z starts on 2026-09-30 and 2026-10-01 both stop inside the 345,000-pair expansion (ProcessPoolExecutor, 12 workers), and the 2026-10-01 09:47Z start stops in RPS injection.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BD gold runner log copy, last 9 MB (this seat, 2026-10-02 03:0xZ): RUNNER STARTED at 2026-09-30 21:47:09Z, 23:00:44Z; 2026-10-01 04:00:41Z, 06:33:22Z, 09:47:03Z, 12:45:31Z, 21:47:07Z, 23:00:45Z; COMPLETE (exit code: 0) at 2026-10-01 01:02:24Z, 06:05:34Z, 08:34:33Z and 2026-10-02 01:02:56Z. Starts with no COMPLETE before the next start: 09-30 21:47Z, 10-01 09:47Z, 12:45Z, 21:47Z (4 of 8)",
        "the last line before each following start: 'Expanding 345,025 pairs with ProcessPoolExecutor (fork, 12 workers)' (09-30 21:47Z run), '[RPS injection] Loading latest RPS partition...' (10-01 09:47Z), 'Expanding 345,227 pairs ...' (10-01 21:47Z)",
        "the scheduled 23:00Z starts complete with exit 0 and arm the instance shutdown ('SHUTDOWN_ARMED chain=chain:full grace=2m')"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A runner start ends in a COMPLETE line with its exit code, so a failed or interrupted run is visible in its own log.",
    "world_is": "Half of the starts in the window leave no end line, and the log cannot tell a killed run from an overlapped one: the next start begins while the earlier one was mid-step. Twice the stop is in the same memory-heavy step at the same hour. Not read: what triggers the 21:47Z and daytime starts, the instance's state changes, kernel OOM records, or whether two runs ever overlapped and wrote the same keys.",
    "notes": "INERT on what was graded: the scheduled 23:00Z run completes and the BD thread's served keys advanced. For 1.0.0_SA_CTO's placement with the runner's owner. No monitor proposed."
  }
]
```


## S34 -- the closed ADHC_GLDINC project's five parity shadows still run every full BD chain (3.0.0_SA_CVO)

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S34",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:15:00Z",
    "one_line": "The BD gold dispatcher still runs five ADHC_GLDINC parity shadows every full chain (A_01, B_02, B_03, A_03, B_01), each building its oracle and uploading a scorecard to gold/_parity/, 3.5 months after ADHC_GLDINC closed and after its sanctioned parity window ended; the dispatcher's own comment says each shadow is TEMPORARY and removed at its cutover.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BD runner log of the 2026-10-01 23:00Z start (copy read by this seat 2026-10-02 03:1xZ): after PARALLEL CHAIN COMPLETE, 'Running GLDINC incremental shadow' for 5 of 5 members, each 'OK -- parity scorecard uploaded', then SHUTDOWN_ARMED at 01:02:56Z",
        "data/black_diamond/scripts/gold/gold_dispatch.sh:1488-1520 at HEAD: GLDINC_SHADOW_SET defaults to the five scripts; comment 'Membership is TEMPORARY per script: added when its additive path deploys, REMOVED at its cutover ... Toggle off entirely: GLDINC_SHADOW_SET=\"\"'; members added 2026-06-11",
        "org/projects/ADHC_GLDINC.json: status complete, phase 'CLOSED COMPLETE 2026-06-18'; daily_watch 'Andrew-direct 2026-06-05 BINDING: GLDINC parity testing is a daily-attested obligation through 2026-07-05'",
        "data/black_diamond/scripts/gold/B_01.holdings_lots.py:3212 writes gold/_parity/holdings_lots/{run_date}/scorecard.json; the 2026-10-02 key is named in the same log"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md section 5: NEVER stand up a shadow/build-alongside pipeline, duplicate output path, or standing parity comparator (Andrew complete veto). The dispatcher's own contract: a shadow is removed at its script's cutover.",
    "world_is": "Five parity comparators run nightly with no end date, on a project closed 2026-06-18 whose Andrew-sanctioned parity window ended 2026-07-05. They write no served output and cannot fail the chain, so nothing served is wrong; they cost each full chain five oracle builds before the instance shuts down, and they are the standing comparator shape the veto names. Not read: each shadow's run time, the scorecards' recent verdicts, and whether any script reached its cutover (which would already have removed it under the contract).",
    "notes": "INERT on served data. The toggle exists (GLDINC_SHADOW_SET=\"\"), so the remedy is one dispatcher edit and a QA deploy by the DS lane that owns gold_dispatch.sh, or a ruling that keeps them. Placement: 1.0.0_SA_CTO. Re-filed home: ADHC_GLDINC is closed, and the estate channel is the accepted home for a closed project's live finding (RULINGS batch 77 @4b9e65f744)."
  }
]
```


## S35 -- clock read for S17: the stitch build failed again; the cause is the grain sentinel (3.0.0_SA_CVO)

```json
[
  {
    "id": "ESTATE_GOVERNANCE-S35",
    "project": "ESTATE_GOVERNANCE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:30:00Z",
    "one_line": "Clock read for S17: the 2026-10-02 03:00Z stitch build FAILED too (two nights running), and the cause S17 left unread is the producer's own grain sentinel: AC-GRAIN.2 counts 26 SCHEDULE nodes against a baseline of 10 (2.60x, outside the [0.4, 2.5]x band) and refuses to emit the graph.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (placement with the graph pipeline's owner: either the schedule growth is real and the baseline is re-read and recorded, or a schedule census is wrong)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "codebuild batch-get-builds, opal-stitch-produce (this seat, 2026-10-02 03:2xZ, times converted to UTC): b53f5014 started 2026-10-02T03:00:12Z FAILED; 88fdb880 started 2026-10-01T03:00:12Z FAILED; the build before them SUCCEEDED; newest 3 of 96 on the first page",
        "CloudWatch Logs /aws/codebuild/opal-stitch-produce, both failed streams, last 40 events: 'GRAIN-SENTINEL: FAIL (1 violation group(s))', '[AC-GRAIN.2] SCHEDULE: count 26 vs baseline 10 = 2.60x (outside [0.4, 2.5]x band)', 'ERROR: GRAIN_SENTINEL_FAIL -- refusing to emit grain-violating stitch graph', exit status 2",
        "the same stream before the sentinel: UNIONED nodes 29,378, edges 63,403; genuine dangling edges 0; LAMBDA join matched 83, unmatched 7",
        "row ESTATE_GOVERNANCE-S17 (this seat, 2026-10-01): 'Not read: the failed build's log, so the cause of exit 2 is unknown ... whether it repeats is tonight's build'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row S17's hazard: a failed night leaves the previous stitch artifact in place, and only the served vintage line discloses its age.",
    "world_is": "The stitch is now two days old and will stay so every night until the sentinel's SCHEDULE baseline or the schedule census changes: the refusal is deterministic, not a flaky build. The guard is doing its job; what it guards against (a grain change) is unread. Not read: which 16 SCHEDULE nodes are new and when they appeared.",
    "notes": "Extends S17 (append-only channel; S17's own text is unchanged). No alert proposed."
  }
]
```
