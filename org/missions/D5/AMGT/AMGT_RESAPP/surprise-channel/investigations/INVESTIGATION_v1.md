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
    "id": "AMGT_RESAPP-Z-W7-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~7",
    "surfaced_at": "2026-09-10T22:40:36Z",
    "one_line": "16 of the 48 MEASURED bloomberg_ticker values in AMGT-s-12's universe.json are the SAME value, 'AAPL US' -- every one resolved from a 'FactSet Based ONE PAGER' workbook's sheet 'Model', label 'Ticker:', row 2, for a company that is not Apple.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZZZ",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json read whole: of 89 folders, 48 carry a MEASURED bloomberg_ticker; grouping those 48 values, exactly one value repeats, 'AAPL US', across 16 distinct folders: AstraZeneca AZN, Canadian National Railway CNR, Clorox CLX, Copa CPA, Imperial Brands IMB LN, JD.com 9618 HK, Michelin ML FP, Mitsubishi UFJ Financial Group 8306 JP, Nestle NESN SW, Nokia FH, Orange ORA FP, SAP GY, Sanofi SAN FP, Shopify SHOP CA, Tokyo Marine 8766 JP, Total Energies TTE FP -- none of them Apple",
        "every one of the 16 entries' bloomberg_ticker.evidence field reads identically in shape: \"...:: sheet 'Model', label 'Ticker:' found, value read from the adjacent cell in the same row (row 2)\", and every one of the 16 entries' one_pager_files names a workbook whose filename contains 'FactSet Based ONE PAGER' (e.g. 'AZN FactSet Based ONE PAGER 2026 06 22_v2.xlsx', 'CNR CA FactSet Based ONE PAGER 2026 06 30_v1.xlsx', 'Nestle FactSet Based ONE PAGER TEMPLATE 2026 05 11_v2.xlsx') -- a single template family, not 16 independent coincidences",
        "a control case from the SAME universe.json: 'ASML NA' resolves to 'ASML NA' (correct, its own ticker) from a workbook named 'ASML One Pager 2025 07 17_v1.xlsx' -- a DIFFERENT, non-FactSet-based template naming -- so the defect tracks the template family, not the resolver rule in general",
        "lib/research/identity/build_universe.py's own docstring already names this exact CLASS of hazard for a sibling sheet: \"the 'Model NEW VERSION' sheet ... was found to carry unrelated template residue (Alibaba's copy names Apple's ticker on that sheet) ... EXCLUDED from the scan\" -- the exclusion list covers 'Model NEW VERSION' but not plain 'Model', and these 16 hits are all on sheet 'Model'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMGT-s-12's cell text: each name's bloomberg_ticker is read from that folder's own one-pager workbook and is MEASURED with cited evidence -- a status of MEASURED asserts the value is the SUBJECT company's own ticker, read from that company's own workbook.",
    "world_is": "16 of 89 covered names (18%) carry status=MEASURED with value='AAPL US' -- Apple's ticker, not their own -- all sourced from the 'Model' sheet of a 'FactSet Based ONE PAGER' template workbook at row 2 beside 'Ticker:'. This reads exactly like the ALREADY-KNOWN template-residue class the resolver's own docstring names and partially guards against (the 'Model NEW VERSION' sheet exclusion), except this instance is on the plain 'Model' sheet, which is not excluded. Every downstream consumer of security_key (this cell's own coverage_freshness.json included) will silently carry 'AAPL_US' as the identity for 16 companies that are not Apple -- and if AMGT-s-1 (raw landing) or any later cell pulls Bloomberg data keyed on these 16 security_keys, it will pull APPLE's model block and attribute it to AstraZeneca, Nestle, SAP, etc. This worker's own coverage_freshness.json rows for these 16 names carry security_key='AAPL_US' as a faithful pass-through of the input -- not corrected here (out of this cell's <paths> and out of its mandate; AMGT-s-12's deliverable is READ, not owned).",
    "notes": "ARMED because the failure mode is SILENT and COMPOUNDING: nothing in this cell's own battery, nor a naive read of universe.json's per-entry MEASURED/evidence fields, flags it -- it only shows up as a CROSS-ENTRY census (grouping all 48 measured values and counting repeats), which no criterion in either AMGT-s-7 or (as far as this worker can see) AMGT-s-12's own battery runs. Disarm: re-run AMGT-s-12's build_universe.py with the 'Model' sheet's row-2 Ticker cell EXCLUDED (or cross-checked against the folder's own company name) wherever the source workbook filename matches 'FactSet Based ONE PAGER', mirroring the existing 'Model NEW VERSION' exclusion; then re-generate coverage_freshness.json from the corrected universe.json (no code change needed in this cell -- build_view.py already treats security_key as untrusted input past AMGT-s-12's boundary)."
  },
  {
    "id": "AMGT_RESAPP-Z-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZZZ",
    "surfaced_at": "2026-09-10T23:17:30Z",
    "one_line": "Issuer's read of AMGT_RESAPP-Z-W7-S3 (ARMED, disarm_owner this seat): the 16-of-48 AAPL US collapse in universe.json is REAL (re-measured 48 MEASURED / 33 distinct / one value on 16 folders), the ISSUANCE cut no unscoped pass over the identity layer's members, and the order is REOPENED with AC7 rather than left to round 2 -- four consumers hang off the root inside this round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json @fcfec6f1c0, read by a Counter over the MEASURED bloomberg_ticker values (a different instrument from the surfacing row's group-by): 48 MEASURED, 33 distinct, [('AAPL US', 16)] -- the surfacing row's count reproduced",
        "the sixteen folders' evidence fields each name a 'FactSet Based ONE PAGER' workbook and the Model sheet's row 2 beside 'Ticker:' -- SAP GY is among them, so the CRO's own control security reads as Apple in the identity layer while AMGT-s-1 pulls it correctly by its own selection rule",
        "AMGT_RESAPP.TO-AMGT-s-12 as issued @908880f6d1 carried AC2 (a partition that closes) and AC5 (per-key negatives) and no criterion over what the 89 members share; AMGT-s-8 and AMGT-s-4, cut by the same issuer in the same issuance, each carry an explicit unscoped pass (C-SHARED-DEFECT) -- the root was the one place it was left out",
        "blast radius read before the reopen: AMGT-s-1 pull_log.json names BA US Equity, BABA US Equity, SAP GY Equity (chosen by its own rule, none contaminated); AMGT-s-13's MEASUREMENT_PLAN.md names Home Depot HD (not contaminated); AMGT-s-7's coverage_freshness.json carries the 16 keys and is held off the drain until it regenerates; AMGT-s-15 and AMGT-s-b4 executing, read on their reports",
        "the reopen: commit 0d2cfbfc11 on wk-AMGT_RESAPP-1-3 (author 2.0.0_SA_COO~ZZZ) adds AC7 -- NEGATIVE, UNSCOPED: no MEASURED ticker value shared by two or more folders, MEASURED equals distinct -- and flips <status> complete -> pending; AC7 exercised against the contaminated file before the commit printed 'values shared by two or more folders 1 [(AAPL US, 16)]', the failure it exists to catch"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 22: 'A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE ... Ask what the members have in COMMON, and check THAT on its own; then re-read the population UNSCOPED once.' PRD v0.3 C-SHARED-DEFECT: the unscoped pass over the population is the pass that would have caught a telecom set on 48 non-telecoms. FWD-13's bar: everything on one page is about the same company.",
    "world_is": "The identity layer -- the root four surfaces hang from, cut to remedy F6 -- shipped with the F6 shape inside it: one template's example ticker keyed 16 of 89 covered names to Apple, every per-member criterion passed, and the defect was found by a CONSUMER building on the artifact, not by the issuer or the gate. Remedy taken by the disarm owner the same turn: the order reopened on its own branch with the unscoped criterion the issuance lacked, the worker resumed to regenerate with a placeholder read as UNRESOLVED, and the consumers that already read the keys held off the drain until they regenerate. What this row does NOT claim: that the corrected universe has landed (it lands with the next drain of wk-AMGT_RESAPP-1-3), or that the CVO's disposition of W7-S3 is anything but its own.",
    "notes": "Owner of the remedy: 2.0.0_SA_COO~ZZZ (issuer). The CVO's L9 disposition of AMGT_RESAPP-Z-W7-S3 is not pre-empted by this row; this row records the issuer's act and its evidence so the disposition can be graded against the artifact rather than the message."
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
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~1",
    "surfaced_at": "2026-09-10T22:35Z",
    "one_line": "AMGT-s-12's universe.json carries a measurement defect: 16 of its 48 MEASURED bloomberg_ticker values -- unrelated folders from AstraZeneca to Total Energies, including the CRO's own control folder 'SAP GY' -- all read the identical string 'AAPL US'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json, read via select_securities.py: 48 of 89 entries carry bloomberg_ticker.status=='MEASURED'; grouping those 48 by bloomberg_ticker.value shows the single value 'AAPL US' shared by 16 distinct folders (AstraZeneca AZN, Canadian National Railway CNR, Clorox CLX, Copa CPA, Imperial Brands IMB LN, JD.com 9618 HK, Michelin ML FP, Mitsubishi UFJ Financial Group 8306 JP, Nestle NESN SW, Nokia FH, Orange ORA FP, Sanofi SAN FP, Shopify SHOP CA, Tokyo Marine 8766 JP, Total Energies TTE FP, and SAP GY) while every one of the remaining 32 MEASURED entries carries a value unique to its own folder",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/select_securities.py run (this worker's own build), dup_report={'AAPL US': 16}, clean_unique_entries=32",
        "The SAP GY folder's own universe.json entry -- the CRO's control security -- carries bloomberg_ticker.value=='AAPL US', which does not match the CRO's own field-map deliverable's control ticker 'SAP GY Equity' (org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_BLOOMBERG_FIELD_MAP_20260910.md, throughout): the folder's own resolver output disagrees with the CRO's independently-measured value for the identical company"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This cell's bound (d): 'a US name and an ADR, both chosen from the coverage universe by a rule you state ... AMGT-s-12's universe.json enumerates them if it has landed' -- implying universe.json's bloomberg_ticker.value entries are each an independent, per-folder MEASURED read this worker could select from directly.",
    "world_is": "16 of the 48 MEASURED entries are not independent per-folder reads -- they share one identical string that is correct for at most one folder (at most one company is genuinely 'AAPL US Equity') and wrong for the other 15, including the control company SAP GY itself. This worker's selection rule (select_securities.py) drops every duplicate-valued entry before picking a US-domiciled name and an ADR, so the defect did not propagate into AMGT-s-1's own security choices (Boeing BA US Equity, Alibaba BABA US Equity) or into the SAP GY Equity control (taken directly from the task order text/CRO brief, never from this universe.json row). Not fixed here: AMGT-s-12's resolver.py and build_universe.py are outside this worker's <paths> grant, and repairing another cell's deliverable is out of bounds regardless.",
    "notes": "Worth the identity-layer owner's attention before AMGT-s-2/-3/-5/-9 (this cell's downstream dependents per the DEPENDENCIES section) build on universe.json for a folder OTHER than the 3 this worker touched -- any of the 16 affected folders would silently resolve to Apple's ticker if consumed without the uniqueness check this worker applied. The shape (one recurring constant value across unrelated keys) looks like a resolver bug that returns a previous/cached result on a failure path rather than a per-folder read; not diagnosed further here (outside this cell's write surface)."
  },
  {
    "id": "AMGT_RESAPP-Z-W1-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~1",
    "surfaced_at": "2026-09-10T23:05Z",
    "one_line": "For the ADR (BABA US Equity, fiscal year end 31 March), Bloomberg's raw HistoricalDataRequest response never carries a single row with BOTH a price field and a fundamentals field -- 100% of its rows split fiscal-period-end (March) fundamentals from calendar-year-end (December) price/ratios, so the fiscal-year join (grouping by the calendar year of `date`) merges each fiscal year's fundamentals with a price observation roughly nine months later, not one from the fiscal period end itself.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "raw/bloomberg/BABA_US_Equity/20260910T224407Z/histdata.json (S3, opal-data-research): all 20 raw rows for BABA US Equity split cleanly into 10 fundamentals-only rows dated '<year>-03-31' and 10 price/ratio-only rows dated '<year>-12-31' -- zero rows carry both a fundamentals field and PX_LAST/PE_RATIO together. SAP GY Equity and BA US Equity (both December-FYE issuers), by contrast, merge most years into one row (SAP: 6 of 10 years single-row, matching the CRO's own 'F5' 14-rows-for-10-years finding).",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/build_field_map.py detect_reporting_currency_mismatch(), run against the fiscal-year-merged groups: fiscal-year-2025-merged naive PE (PX_LAST/IS_EPS = 2.6593) vs Bloomberg's own PE_RATIO (15.7545) for the same fiscal-year label on BABA US Equity, ratio 0.1688 -- outside the 0.8-1.25 plausible-reconciliation band. The identical check on SAP GY Equity's FY2025 (both December-FYE, same-year rows) reconciles to 1.0000007 (positive control: the method is sound and the SAP case shows no such gap).",
        "field_map.json cross_security_findings[0] (this worker's own committed artifact): the finding is recorded as consistent with a currency difference AND/OR the ~9-month fiscal-vs-calendar timing gap AND/OR an ADR share-ratio effect -- explicitly NOT isolated to one cause"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This cell's bound (e)/C-FISCAL-YEAR-JOIN: 'Fiscal year is the join key ... Join on fiscal year, never the date string' and AC4's bar: 'JOIN: 3 of 3 securities at 10 FY rows; orphan price rows 0'.",
    "world_is": "Grouping by the calendar year of `date` (date[:4]) satisfies AC4's MECHANICAL bar exactly -- 10 distinct fiscal-year labels, 0 raw rows left un-merged, for all three securities including BABA -- but for a non-December-FYE issuer this calendar-year grouping is not the same thing as grouping by the ISSUER'S OWN FISCAL PERIOD: it pairs each fiscal year's fundamentals (reported as of the true period end, 31 March) with a price/ratio observation from nine months later in the same calendar-year label (31 December), rather than one from at or near the fiscal period end. AC4's row-count-and-orphan-count bar cannot detect this, because it counts rows, not temporal alignment. This worker did not attempt a deeper fix (e.g. sourcing a price observation nearer the fiscal period end would need an additional Bloomberg field/call this order's F2/G-24 three-security cap does not budget for) -- the finding is disclosed in field_map.json, in every affected figure's `currency_caveat` (model_block_pull.py), and in README.md, per AC8's own question about what the deliverable could not resolve and said so.",
    "notes": "Downstream cells building fiscal-year-keyed ratios for a non-December-FYE covered name (this universe includes several: KDDI, Hon Hai 2317 TT, Mitsubishi UFJ 8306 JP among the ~89, though this order touched none of them besides BABA) should re-derive rather than assume the calendar-year grouping is fiscal-period-aligned. A more precise fix (e.g. reading a Bloomberg fiscal-period-end price via an override, or accepting the March-dated sub-row's own trailing PX_LAST if one exists) is a candidate for whichever cell next builds ratio-bearing figures on a non-calendar-FYE name; not attempted here to stay inside the three-security cost cap and because it was not established which route Bloomberg actually supports without a further, uncosted call."
  },
  {
   "id": "AMGT_RESAPP-Z-W9-S1",
   "project": "AMGT_RESAPP",
   "fabric": "site-z",
   "surfaced_by": "0.9.0_WK_AMGT_RESAPP~9",
   "surfaced_at": "2026-09-10T23:15:24Z",
   "one_line": "16 of 89 folders in AMGT-s-12's universe.json carry bloomberg_ticker.value == 'AAPL US' with status MEASURED even though their folder names name distinct companies -- an identity-layer data-quality anomaly this cell's ticker selection had to route around.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "python census over org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json's 'names' array (89 entries): collections.Counter over bloomberg_ticker.value where status=='MEASURED' -> 33 unique values, one of which ('AAPL US') accounts for 16 of the 48 MEASURED entries; the 16 folders include AstraZeneca AZN, Canadian National Railway CNR, Clorox CLX, Copa CPA, Imperial Brands IMB LN, JD.com 9618 HK, Michelin ML FP, Mitsubishi UFJ Financial Group 8306 JP, Nestle NESN SW, Nokia FH, Orange ORA FP, SAP GY, Sanofi SAN FP, Shopify SHOP CA, Tokyo Marine 8766 JP, Total Energies TTE FP",
     "AMGT_RESAPP-Z-W3-S1 (this same investigation file) already recorded a related identity-layer defect (5 of 89 folders carrying two disagreeing *ONE PAGER*.xlsx workbooks) found by the same worker who produced universe.json -- this is a second, distinct anomaly in the same artifact, not yet recorded",
     "This worker's stated ticker-selection rule for AMGT-s-b4's AC1/AC4 (run_manifest.json in this worker's deliverables) explicitly excludes the 'AAPL US' value and picks the first three array-order MEASURED, ' US'-suffixed, non-anomalous entries (BABA, BA, COST) precisely to avoid resting the test on a non-discriminating identity"
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "AMGT-s-12's universe.json entry per folder carries a MEASURED bloomberg_ticker.value that uniquely identifies that folder's subject company (the identity layer's whole purpose, per AMGT-s-12's cell text and STORE_CONTRACT.md section 2: 'there is exactly one identity axis in this bucket').",
   "world_is": "16 of 89 folders' bloomberg_ticker.value is the identical literal 'AAPL US' at status MEASURED, which cannot be true for 16 distinct companies (AstraZeneca, Boeing peers, etc. are not Apple); the resolver measured SOMETHING at those folders but not each folder's own identity. This worker did not fix or re-run AMGT-s-12's resolver (out of this cell's <paths> and BOUNDS) and instead selected its 3 test tickers by a rule that provably avoids the anomalous value.",
   "notes": "Non-blocking for AMGT-s-b4: the stated selection rule (run_manifest.json) sidesteps the anomaly entirely and BABA/BA/COST are independently confirmed real, distinct, US-listed tickers. Worth AMGT-s-12's owner re-reading build_universe.py/resolver.py for whichever code path defaults to 'AAPL US' (possibly a template/placeholder cell read from a workbook whose real ticker cell was blank or unreadable, silently falling back to a literal in the script rather than refusing) before any other cell trusts universe.json's bloomberg_ticker column at face value for one of these 16 folders."
  },
  {
   "id": "AMGT_RESAPP-Z-W9-S2",
   "project": "AMGT_RESAPP",
   "fabric": "site-z",
   "surfaced_by": "0.9.0_WK_AMGT_RESAPP~9",
   "surfaced_at": "2026-09-10T23:15:24Z",
   "one_line": "astn/brightdata/residential-proxy currently TLS-intercepts every HTTPS GET with an untrusted 'Bright Data Proxy Root CA' leaf that no standard client can verify, so this run's 9 attempted GETs (3 tickers) all failed at the TLS handshake before reaching Seeking Alpha, and AC1 reads 0 of 3 landed -- not a defect in this order's fetcher, detectors, or logging (AC2-AC6 all pass).",
   "class": "BLOCKING",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "curl_cffi.requests.Session(impersonate='chrome', proxies={http/https: the astn/brightdata/residential-proxy secret's host:port with a fresh per-request random sticky-session username, as sa_rest_fetch.py's own build_session() constructs it}).get('https://example.com') -> curl_cffi.requests.exceptions.CertificateVerifyError 'SSL certificate problem: unable to get local issuer certificate'; the identical Session with no proxy set against the same URL succeeded 200/559 bytes, and the identical Session with verify=False against the proxy also succeeded 200/559 bytes (diagnostic only, not used in the shipped fetcher, which never sets verify=False)",
     "openssl s_client -connect example.com:443 -proxy <secret host>:<secret port> -proxy_user <sticky-session id> -proxy_pass env:<var> -servername example.com -showcerts: exactly 1 certificate returned in the chain -- '0 s:CN=*.example.com' / 'i:C=IL, ST=IL, O=Bright Data, CN=Bright Data Proxy Root CA' -- no intermediate or root sent, verify return code 21 (unable to verify the first certificate)",
     "A second, independent TLS stack (native Windows Schannel via curl.exe 8.21.0, which trusts the OS root store, distinct from curl_cffi's bundled certifi store) reproduces the same rejection through the same proxy: 'curl: (60) schannel: SEC_E_UNTRUSTED_ROOT -- The certificate chain was issued by an authority that is not trusted'",
     "Reproduced on 3 independent per-invocation sticky-session identifiers, one per ticker (BABA, BA, COST), each generating its own fresh random suffix per sa_rest_fetch.py's username convention -- all 9 GET attempts (symbol/analysis/news x3 tickers) failed identically, logged in this worker's deliverables/request_log.json with classification TRANSPORT_ERROR and the curl error text (no secret value in any entry)",
     "The reference (@b1656bbebc section 2b) measured 'the proxy is GET-capable today ... never challenged once the PX cookies were present' at 19:4x-19:5xZ 2026-09-10 through the same secret, same default verify=True code path; this run (23:0x-23:1xZ, same day, same secret, same session-building code) reproduces the interception on every attempt with no code difference in how the session or proxy is built"
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "The cell's mechanism for AC1 (carried from the reference, section 2b): 'the fetch MUST egress through the residential proxy ... The proxy is GET-capable today,' i.e. that egressing through astn/brightdata/residential-proxy with the parked jar produces vendor HTTP responses this ETL can classify and land.",
   "world_is": "The proxy zone is currently terminating and re-signing HTTPS with its own 'Bright Data Proxy Root CA' rather than passing the origin's real certificate through, and does not include that root/intermediate in the handshake -- so no standard TLS client (tested: curl_cffi/certifi AND native Windows Schannel) can complete verification without either disabling certificate verification (a security-posture change this cell's BOUNDS do not authorize) or being supplied that specific root CA out of band, which this worker does not have and did not seek from Bright Data (no vendor API/dashboard call made). verify stayed at its safe default for every real attempt in this run, so no part of the parked session's 65-cookie jar was ever transmitted to the intercepting party -- the TLS handshake aborted before any HTTP request left the client. AC1 reads 'raw objects 0 across 3 keys; symbol+report present for 0 of 3; sa_ids MEASURED 0' -- a genuine, reproduced, non-rescued finding, recorded rather than routed around.",
   "notes": "Not this worker's <paths>/BOUNDS to fix: resolving it means either obtaining Bright Data's specific proxy root CA (an out-of-band vendor artifact, e.g. from their account dashboard or support) and pinning it as a scoped trust anchor for this proxy only, or toggling off whatever zone-level SSL-interception feature is enabled, or an explicit Andrew-authorized decision to disable verification for this specific proxy -- all security-posture calls outside this cell's granted authority. The rest of the module is built and exercised as far as the transport layer allows: AC2 (4 fixture tests), AC3 (referer/proxy/method/pacing census), AC4 (3 tickers, 1 run), AC5 and AC6 (structural bans) all pass against this exact run's real output; only AC1 (the live landing) is blocked by this transport-layer finding."
  },
  {
    "id": "AMGT_RESAPP-Z-W3-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_AMGT_RESAPP~3",
    "surfaced_at": "2026-09-11T00:19Z",
    "one_line": "AMGT-s-4's cell text names which securities the reader should key items by only implicitly (via AMGT-s-12's identity layer); this worker reused AMGT-s-b4's own run_manifest.json ticker selection (BABA_US, BA_US, COST_US) rather than deriving an independent set.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AMGT-s-4 cell text (a): 'read(security_key, sources) -> coverage_items.json' -- takes a security_key as a parameter but the order does not name which security_key(s) to run the reader over for AC2's 'at least 1 security'",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~9/run_manifest.json's own selection_rule: 'the first three entries whose bloomberg_ticker.status == MEASURED, whose bloomberg_ticker.value ends with \" US\", and whose value is not \"AAPL US\"' -- read directly and reused verbatim (BABA_US, BA_US, COST_US) by lib/research/coverage/run_reader.py",
        "python -m lib.research.coverage.run_reader -> 'COVERAGE RUN: 3 securities; 4 items attached; sa_raw_keys_found 0; identity_dropped {BABA_US: 1, BA_US: 1, COST_US: 1}'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AMGT-s-4 (a): the reader is a function of security_key and sources; the order does not name which securities AC2's run must cover.",
    "world_is": "This worker reused a SIBLING cell's (AMGT-s-b4) selection artifact instead of deriving one independently from universe.json -- a reasonable, grounded, non-arbitrary choice (identity-resolved, non-placeholder, consistent with the store keys AMGT-s-b4 would land SA raw JSON under) but a choice this order left open, not one it named. Non-blocking: AC2/AC3/AC7 all close cleanly on this selection; a different, equally valid selection would also have closed them.",
    "notes": "Recorded for the CVO/next reader: if AMGT-s-b4's run_manifest.json selection ever changes (a re-run with different tickers), this cell's run_reader.py silently follows it (it is read live, not pinned) -- worth a read before assuming these three names are stable across rounds."
  }
]
```
