# AMGT_RESAPP -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~ZZZ` at L6, 2026-09-10. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate,
folder == project). **Append-only during the round.**

**Why this file is opened at the issuance.** Sixteen worker faces name it as the carrier for their rows,
and a worker cannot create a channel it was not granted. The first row is the issuer's own: a finding
made while cutting, about the manifest's edges -- a spec-vs-world mismatch, which is the step-7 trigger
whether or not a worker exists yet.

**Id grammar on this fabric:** a seat's row is `AMGT_RESAPP-Z-S<k>`; a worker's row is
`AMGT_RESAPP-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"`
and `"fabric": "site-z"` on every new row. The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 2 rows** -- `-Z-S1`, `-Z-S2`, both `2.0.0_SA_COO~ZZZ`.

⛔ **THIS FILE MUST STAY ONE FENCED JSON BLOCK.** A whole-file regex substitution over the fences rewrites
every block and silently duplicates the channel (NFRA_IAMROLES202609's own warning); an appender targets
the FIRST block only and appends INSIDE the array. The channel is append-only and conflicts on every
concurrent drain; each drain is resolved as a UNION BY ROW ID through `safe-merge.sh`, and no foreign row
is ever edited here.

## Row context -- what was measured

PRD v0.3 @f68818832b section 4, the surface manifest: row S1 (the model block) carries `depends on: --`;
row S6 (the version store) carries `depends on: --`. Both are round-1 roots in the decomposition.
PRD section 3, `C-RAW-BEFORE-DERIVED`: *"raw vendor bytes land before anything derives from them ...
Bloomberg's derived fields have no backfill, so a rule change that cannot be re-derived from stored raw
bytes is a permanent data loss."* The bytes land in the store. The store does not exist:
`comp-find 'opal-data-research' --corpus aws` -> 0 of 2382 graph nodes at 2026-09-10 12:24:50Z; the
L1 brief's PART V measured it absent on the live plane 13:30-16:00Z. So S1's raw landing depends on S6
in the world, and the manifest draws no edge. The issuance sequences S1's spawn after S6 lands rather
than adding an edge to a frozen spec; the row exists so a reader of the manifest does not read `--` as
"needs nothing".

```json
[
  {
    "id": "AMGT_RESAPP-Z-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZZ",
    "surfaced_at": "2026-09-10T20:32Z",
    "one_line": "The manifest draws no S1 -> S6 edge, but S1's raw landing (C-RAW-BEFORE-DERIVED) needs the store S6 creates, and that store is absent at two vintages.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD v0.3 @f68818832b s.4: row S1 `depends on: --`; row S6 `depends on: --`",
        "PRD v0.3 @f68818832b s.3 C-RAW-BEFORE-DERIVED: raw vendor bytes land before anything derives from them; the bytes land in the version store",
        "comp-find 'opal-data-research' --corpus aws -> 0 hit(s) across 2382 aws node(s), graph vintage 2026-09-10 12:24:50Z; L1 brief @19ce7d5b4d PART V: absent on the live plane 13:30-16:00Z the same day",
        "decomposition v0.2 @ed25feaee5 s.4: edges read from the manifest column, S1 and S6 both roots; s.9: the AMGT-s-1 slot spawns after AMGT-s-6 lands"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Manifest row S1 `depends on: --` -- the model block has no dependency and is a round-1 root that may start at issuance.",
    "world_is": "S1's raw landing requires the bucket opal-data-research, which S6 creates and which is absent at the graph vintage (0 of 2382 nodes) and at the brief's live read; the issuance sequences S1's spawn after S6 lands, and a worker that reaches the landing before the bucket exists files a BLOCKING row rather than creating one.",
    "notes": "Not a defect in the cut and not a hold: both cells are round 1 and S6 is one small Terraform act. Recorded because a manifest edge is the carrier L6 derives fan-out from, and an edge that exists in the world but not in the column is invisible to the derivation. The column is L4's (1.0.0_SA_CTO); whether it should carry the edge is that seat's to say at the round-N read."
  },
  {
    "id": "AMGT_RESAPP-Z-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZZ",
    "surfaced_at": "2026-09-10T20:35Z",
    "one_line": "receiving-check.py grades a task order ONE FILE AT A TIME, so the issuance-set coverage limb refuses every member (owns 1 of 16) while the same gate over the set passes 16 of 16.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/receiving-check.py <16 orders> <channel> <project.json> on the staged issuance in the L6 worktree: VERDICT 2 ACCEPT | 16 HAND BACK | 0 UNCHECKED; each HAND BACK reads '[to-pipeline-gate] REFUSED -- 1 violation(s) across 1 newly-added TO file(s)' and 'the issuance ... owns 1 of 16 cell(s)'",
        "python .tools/to-pipeline-gate.py <16 orders> (all sixteen as one argv, the pre-commit hook's shape) on the same staged set: rc 0, 0 violations, 'issuance coverage 16 of 16 cell(s) ... owned by the staged orders'",
        "to-pipeline-gate.py _coverage_grade: the union of <owned_cells> across the STAGED orders must equal the decomposition's cell set -- a set property; receiving-check.py @adfbe65590 dispatches per file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "receiving-check.py @adfbe65590 (1.0.0_SA_CTO~Z msg 21057): 'grade what you were HANDED before you build on it, one command ... six artifact types dispatch to the tool that already owns them ... run as subprocesses with their own output shown verbatim'.",
    "world_is": "For a task order the wrapper dispatches to-pipeline-gate one file at a time, and the gate's coverage limb grades the issuance SET; so on a conforming sixteen-order issuance the wrapper returns HAND BACK sixteen times for a property the set satisfies, and its verdict is the negation of the gate's. The pre-commit hook passes all staged paths together and grades correctly; nothing is blocked. A COO who trusted the wrapper's verdict on an issuance would hand back a correct cut.",
    "notes": "The tool's owner is 1.0.0_SA_CTO~Z. The fix shape is the owner's to choose: dispatch task orders as one set when more than one is handed, or skip the coverage limb per file and say UNCHECKED for it rather than HAND BACK. Same class as the three that seat named in msg 21057 -- a check that exists, reads correct, and cannot reach its subject. Reported to the owner by message after this commit lands."
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~7",
    "surfaced_at": "2026-09-10T21:08:24Z",
    "one_line": "AC4's literal string check cannot be satisfied by a correct, documented use of the TO-named ledger tool .tools/deploy_ledger.py -- its cmd_close hardcodes a Status value the check's own patterns never match.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AMGT_RESAPP.TO-AMGT-s-6.version-store-opal-data-research.md AC4 invocation, run verbatim against the real closed entry org/critical_paths/change_management/20260910T2059Z_amgt-resapp-opal-data-research-bucket_deploy_completion.md -> 'entries 1 | names safe-apply True | closed False'",
        ".tools/deploy_ledger.py:436 cmd_close hardcodes state['status'] = 'CLOSED -- nothing stranded' (no CLI flag sets a different status string); :260-263 _render_entry emits '**Status:** ' + status + ' -- closed ' + closed_at, i.e. literally '**Status:** CLOSED -- nothing stranded -- closed <ts>'",
        "isolated call to deploy_ledger._render_entry() with status='CLOSED -- nothing stranded' and a closed_at set: .upper() checked against AC4's four patterns ('STATUS: CLOSED','STATUS: COMPLETE','CLOSED AT','COMPLETED AT') -> all four False, because '**Status:**' places two markdown asterisks between the colon and the space (breaking 'STATUS: CLOSED' contiguity) and the closed-at phrase reads 'CLOSED <timestamp>' not 'CLOSED AT' or 'COMPLETED AT'",
        "comp-which \"open a change-management deploy ledger entry\" returned no curated match (score 0.55 top hit comp-schedule); .tools/deploy_ledger.py was located by comp-find --name on 'deploy*ledger*' as the only estate tool matching the TO's own description of what it does (open/close-leg/close/check against org/critical_paths/change_management + .open_deploys)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AC4 expects 'closed True' where closed := any(w in t.upper() for w in ('STATUS: CLOSED','STATUS: COMPLETE','CLOSED AT','COMPLETED AT')) after using 'the estate's ledger tool' (TO deliverable (c)) to open and close the entry.",
    "world_is": "The estate's only matching ledger tool, used exactly as documented (open -> close-leg x2 with proof -> close, no hand-edit), renders a Status line whose markdown bolding and fixed CLOSED-status prose never contain any of AC4's four literal substrings; the criterion is unsatisfiable by a correct, undocumented-route-free use of the named tool. I did not hand-edit the rendered .md to force a match (the tool's own docstring: 'Never hand-edit an entry' -- a hand-edit is also a route this order did not name) and did not repair or widen AC4. AC4 is recorded FAIL against its exact invocation and verbatim output; the order does not flip to complete on this row alone.",
    "notes": "Worker did everything else the cell specifies: G-16 ordering held (ledger opened before safe-apply, closed+committed before the AC2-AC5 grading reads), the tool named safe-apply in its own manifest text (AC4's other two limbs both read True), and the entry genuinely IS closed (sentinel removed, all legs proven) -- only the literal string match fails. Owner to choose the fix shape: loosen AC4's pattern set to also accept 'CLOSED --' (the tool's actual terminal-status grammar, per deploy_ledger.py:734 _is_terminal_status which already treats a leading CLOSED/COMPLETE token as terminal), or have future TOs check via _is_terminal_status-equivalent logic rather than hand-picked substrings. Not something this worker's <paths> grant licenses fixing (the criterion text stands; repairing it is explicitly out of bounds for the worker who is graded by it)."
  },
  {
    "id": "AMGT_RESAPP-Z-W7-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~7",
    "surfaced_at": "2026-09-10T21:54:26Z",
    "one_line": "This order's own worker-face launch prompt dictated a proof-of-spec filename shorter than .tools/to-pipeline-gate.py's complete-flip discovery glob requires, so the correctly-produced instance was invisible to the gate until renamed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This worker's launch prompt (identical text repeated in AMGT_RESAPP.TO-AMGT-s-6's own agent-definition preamble): 'the proof-of-spec instance at org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/AMGT_RESAPP.TO-AMGT-s-6.proof_of_spec.json'",
        ".tools/to-pipeline-gate.py:1484-1492: on a <status>complete</status> flip for a PIPELINE-REGISTERED project, the discovery glob requires 'stem + \".proof_of_spec.json\"' where stem = os.path.basename(rel).rsplit('.md',1)[0] -- the TASK ORDER's OWN full filename stem ('AMGT_RESAPP.TO-AMGT-s-6.version-store-opal-data-research'), not the to_id alone",
        "Measured live: `bash .tools/safe-commit.sh ... -- <deliverables>/AMGT_RESAPP.TO-AMGT-s-6.proof_of_spec.json <task-order>.md` with <status>complete</status> staged -> 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate)... NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip.' Renaming to the full-stem name and re-running proof-of-spec-check.py on the new path -> VALID (rc=0), and the same commit then proceeded (see COMMITS in the worker report)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The launch prompt's own dictated deliverable path is authoritative for where the proof-of-spec instance lives.",
    "world_is": "That path is the correct GRAIN and CONTENT and fully valid on its own (proof-of-spec-check.py passes it standalone) but is invisible to the estate's own complete-flip gate, which resolves the instance ONLY by the task order's full filename stem. A worker following the launch prompt literally for the entire session (as this one did through AC1-AC7 and the first AC4 amendment) would discover the mismatch only at the flip attempt, not before -- fixed in-session by renaming (git records add+delete) rather than widening this worker's <paths> grant, which already covers the deliverables/ folder either name lives in.",
    "notes": "Owner to choose the fix shape: correct the launch-prompt-generation template (COO's L6 issuance tooling) to emit the full-stem filename, or relax to-pipeline-gate.py's discovery glob to also accept a <to_id>.proof_of_spec.json short form. Not this worker's to repair -- the gate and the launch prompt are both outside this worker's <paths> grant to edit; the deliverable itself was moved, not the tool or the prompt template."
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~3",
    "surfaced_at": "2026-09-10T21:39Z",
    "one_line": "AMGT-s-12b's cell text names 'that folder's *ONE PAGER*.xlsx workbook' (singular); 5 of 89 folders carry TWO such workbooks that disagree with each other on the peer-set question, so 'the workbook' is not always one file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "os.listdir census over all 89 corpus folders (build_universe.py / f6_remeasure.py, both committed at 074d0d1ebeb31631e871e60b24f84fcd70edae0b): 44 folders carry exactly one *ONE PAGER*.xlsx file, 5 carry two, 40 carry none -- 44 + 5*2 = 54, matching F6's own 'all 54 ... workbooks' population",
        "the 5 two-file folders: Imperial Brands IMB LN, Nokia FH, Petrobras PETR3 BZ, SAP GY, Total Energies TTE FP",
        "Imperial Brands IMB LN's two files DISAGREE: 'Imperial Brands FactSet Based ONE PAGER 2026 07 17_v1.xlsx' CSC sheet carries the stale 12-name KPN telecom set; 'Imperial International Dividend One Pagers.xlsx' CSC sheet carries the real analyst set (IMB LN, BATS LN, 2914 JT, PM US, MO US) matching the CRO's cited own-set finding -- read directly, both files, both CSC sheets, at C:\\Users\\Opal Bloomberg\\OneDrive - Opal Capital\\Shared - Documents\\Asset Management\\Research\\Imperial Brands IMB LN\\"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMGT-s-12 cell text (b): 'the Bloomberg-format ticker of the SUBJECT company read from that folder's *ONE PAGER*.xlsx workbook' -- singular, one workbook implied per folder entry in universe.json.",
    "world_is": "5 of 89 folders carry two *ONE PAGER*.xlsx files each, and at least one pair (Imperial Brands) carries materially different content across the two files (a stale copy and a real one). universe.json (one entry per folder, per the cell text) resolved this by trying every matching file in a folder and keeping the first that yields a MEASURED ticker, recording all matching filenames in each entry's `one_pager_files` array -- not specified by the cell text, which named a singular workbook. f6_remeasure.py, whose population the cell text separately names as workbooks not folders ('all 54 ... workbooks'), counts and classifies every file, which is why it reproduces the CRO's 48/4/2 of 54 exactly.",
    "notes": "Non-blocking: the tie-break did not prevent AC2's partition from closing (89 of 89, MEASURED+INFERRED+UNRESOLVED summing correctly) and did not affect AC3 (workbook-level, unaffected by the ambiguity). Recorded because a later cell reading universe.json's bloomberg_ticker for one of these 5 folders sees only ONE ticker value even though the folder's second workbook may carry a different (or no) identity block -- worth a read before AMGT-s-4/s-8/s-13/s-15 build on this entry for those 5 names specifically."
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~3",
    "surfaced_at": "2026-09-10T21:57Z",
    "one_line": "The worker face names the proof-of-spec path as '<PROJECT>.TO-<cell>.proof_of_spec.json', but .tools/to-pipeline-gate.py's check_complete_flip requires the FULL task-order-filename stem ('...identity-layer-the-root.proof_of_spec.json') or the complete flip is refused.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "First attempt: committed the status flip alongside a file named AMGT_RESAPP.TO-AMGT-s-12.proof_of_spec.json -> safe-commit ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate); [to-pipeline-gate] REFUSED: '...flips to complete on PIPELINE-REGISTERED project AMGT_RESAPP, and NO proof-of-spec instance was found beside it.'",
        ".tools/to-pipeline-gate.py check_complete_flip(): `stem = os.path.basename(rel).rsplit('.md', 1)[0]` (the FULL task-order filename, e.g. 'AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root'), then `names = (stem + '.proof_of_spec.json', ...)`, globbed under deliverables/*/",
        "Renamed to org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root.proof_of_spec.json; re-ran python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6 -> VALID (rc=0), 0 violations, identical to the pre-rename read",
        "Sibling instances on other projects use the full-stem convention already, e.g. org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~5/ETFS_GUARDRAIL.TO-EG-s-25.the-verdict-discloses-its-own-forcing.proof_of_spec.json"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This worker's task text: 'your proof-of-spec instance at org/.../deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-s-12.proof_of_spec.json' -- the short to_id form.",
    "world_is": "The mechanical gate that actually decides whether a 'complete' flip is accepted keys on the TASK ORDER FILE'S OWN full basename stem, not the short to_id -- a file named with the short form is invisible to check_complete_flip's glob and the flip is refused with a message that reads as if no instance exists at all, even though a VALID one does, just under the wrong name. Renamed to the full-stem form (permitted -- deliverables/ is broadly granted) and the flip proceeded.",
    "notes": "Non-blocking, caught before any commit landed (safe-commit's pre-commit hook aborted cleanly, files left unstaged, nothing to roll back). Worth fixing at the source that generates worker task text (the short-form path may be a convenience abbreviation that was never cross-checked against the gate it has to pass) so the next worker does not repeat the same round trip."
  },
  {
    "id": "AMGT_RESAPP-Z-W5-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~5",
    "surfaced_at": "2026-09-10T22:53Z",
    "one_line": "AMGT-s-15's own two schemas name reviewed_at/review_interval_days once per LIST, never per entry, so rot.py's staleness is list-wide (N is 0 or the full entry count, never partial); and social_accounts.json's entries are keyed by a `security_key` this project has not defined anywhere else, resolved here to AMGT-s-12 universe.json's `folder` value.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AMGT_RESAPP.TO-AMGT-s-15...md worker face (a)/(b): publishers.json and social_accounts.json are BOTH given as {owner, owner_status, reviewed_at, review_interval_days, entries: [...]} -- reviewed_at and review_interval_days sit at the list's top level in both named shapes; neither named entry shape ({domain,name,status,added_at,added_by,reason} for publishers, {security_key,platform,handle,status,evidence} for social_accounts) carries a per-entry reviewed_at field",
        "same worker face (c): 'for each list, entries older than review_interval_days since reviewed_at are STALE' -- read against the schemas in (a)/(b), the only reviewed_at available to compare against is the list's single value, so lib/research/lists/rot.py's is_stale() runs once per list and the result (stale or not) is reported against the whole entries_total (rot_signal.json, entries_stale field is either 0 or equal to entries_total for every list at every run so far)",
        "python search of lib/research/**/*.py for the literal string 'security_key' before this cell's own build_lists.py existed: 0 hits (rules/, identity/ modules carry no such field)",
        "AMGT-s-12's universe.json (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json@074d0d1ebe) names, per entry, folder/one_pager_files/bloomberg_ticker/sa_symbol/ir_domain/social_account -- no field named security_key; folder is the one field MEASURED present and unique across all 89 entries (bloomberg_ticker and sa_symbol are UNRESOLVED for a majority: e.g. Adobe ADBE US, Air Liquide AI FP, America Movil AXMB MM all carry bloomberg_ticker.status UNRESOLVED in the same file), so folder was read as security_key's value in social_accounts.json's 267 entries (89 names x 3 platforms)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell's own (a)/(b) schemas carry reviewed_at/review_interval_days at the list level only, and (c) then describes staleness in terms of 'entries older than review_interval_days since reviewed_at' as if the comparison were per-entry; the cell also names social_accounts.json entries by `security_key` without defining the term or pointing at an existing field it maps from.",
    "world_is": "No per-entry reviewed_at field exists in either schema the cell itself gives, so this cell's rot.py computes staleness once per list (all-or-nothing over that list's entries) rather than per entry, and security_key was set to AMGT-s-12 universe.json's `folder` value -- the only field measured unique over all 89 names, since bloomberg_ticker/sa_symbol are UNRESOLVED for many of them and would leave holes as a key.",
    "notes": "Non-blocking: AC1/AC2/AC3 all pass under this reading, and the cell's own (c) text -- 'Prints ONE line per list' -- is itself consistent with a per-list (not per-entry) rot computation. Recorded because a later cell or an owner editing these lists by hand and expecting a per-entry review date, or a per-entry security_key drawn from some other identifier, would find neither and should read this row first."
  }
]
```
