# /canonical-flow first run on site Z: NFRA_SECURITY202609 -> NFRA_OPSEC202609 into the tree, L3 + L4 landed, L5 handed to the COO -- 1.0.0_SA_CTO~Z

**serial:** 1.0.0_SA_CTO~Z (site-Z lane; base folder, lane named here per XXX.md)
**Date:** 2026-09-03, 06:31Z -> 07:25Z
**Task Order:** ad-hoc -- canonical-flow-nfra-opsec202609-l3-l4 (Andrew-direct, no TO; the CTO holds no task orders)
**Status:** COMPLETE for this seat's limbs (L2 confirmed done, L3 + L4 landed); the project is IN PROGRESS at L5 (2.0.0_SA_COO~Z)
**archetype:** MIXED
**secondary_archetypes:** SCRIBE (tree row, PRD v0.4, manifest), VALIDATE (limb measurement, gate falsifiers), IMPLEMENT (gate fix), COORDINATE (handoff, receipts), RECORD (Andrew-direct x1 verbatim)

This is the HANDOFF. Per Andrew ~06:4xZ (MSTR~Z 19440) this session ends at the project's L10 close and `0.0.0_AB_MSTR~Z` spawns a fresh group for `OPAL_TICKET_VNEXT`; a successor `1.0.0_SA_CTO~Z` reads this file first. Section "Next Steps" carries what the successor must know before its first act.

---

## Objective

Run `/canonical-flow` on the site-Z project Andrew named (NFRA_SECURITY202609, "or whatever that project was"), get it into the proper tree structure, and drive it toward conclusion under `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` at this seat's limbs (L2-L4). First run of the skill on this fabric.

---

## Andrew-direct this window (recorded verbatim; broadcast same turn)

1. ~06:5xZ, typed at THIS terminal mid-turn, verbatim and entire: **"Call it NFRA_OPSEC202609"** -- answering this seat's measurement that his 2026-09-02 code `NFRA_SECURITY202609` is refused by the tree grammar. Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_065xZ_CTOZ_CALL_IT_NFRA_OPSEC202609.md` @32daebf403; broadcast 19443/19444/19445 (MSTR~Z, COO~Z, CVO~Z; 3 DELIVERED of 3).

Relayed to this seat (not typed here): ~06:3xZ "run /canonical-flow on the NFRA_SECURITY202609 ... proper tree structure ... drive it to conclusion ... then D7" (MSTR~Z 19435, record @fc78faf65c); ~06:4xZ the fabric sequence NFRA_OPSEC202609 -> OPAL_TICKET_VNEXT -> ASSETCLASS_TAXONOMY -> D1_CATVIEWS research, every one via /canonical-flow, /govern granted to MSTR~Z, one fabric per project (MSTR~Z 19440).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read --enumerate | `comp-read org/projects/REGISTRY.md --enumerate 'NFRA_SECURITY202609\|D12_PLATFORM_FORTIFY'` | PASS | 0 hits / 417 lines at HEAD vs 1 at @74518cc788 -- the lost-row finding; the denominator made the zero a claim |
| comp-read --enumerate | `.tools/to-pipeline-gate.py` for `FWD_DEF_RE`, `ENDPOINT_HEADING`, `PRD_FENCE_RE`, `MANIFEST_HEADING_RE`, `PROJECT_RE` | PASS | read the regexes at source BEFORE writing the header; found the FWD-10..18 single-space defect that would have refused 9 of 18 outcomes at L6 |
| comp-read --enumerate | `.tools/missions-tree-index.py`, `.tools/prd-header-notify.py`, `.tools/surprise-row-gate.py`, `.tools/deploy_ledger.py` | PASS | regex source, RECIPIENT default (base serial), `_blob` call sites, held qualification |
| comp-find | `comp-find 'HELD-CLAIM REJECTED\|HELD-SOVEREIGN-GATED' .tools org/critical_paths --files --limit 12` | PASS | DENOMINATOR 56 hits / 1210 files; DEF band -> `.tools/deploy_ledger.py` |
| comp-surprise | `comp-surprise --project NFRA_SECURITY202609` | WARN | 0 items across 0 projects from 20 files -- correct empty; no channel yet |
| missions-tree-index | `check` (x4) / `derive --write` (x2) | PASS | tree=3 projects, 3 valid, generated=3, 0 violations at every run |
| to-pipeline-gate limb 5 | `_prd_conformance(prd, schema, row)` by direct import | PASS | `[]` on the tree PRD; NEGATIVE control (old flat PRD) fails "no fenced json"; MUTANT control (fabric flipped) fails "two carriers disagree" |
| surprise-row-gate | `--self-test` after the `_blob` fix | PASS | 0 of 6 arms failed + live census |
| commit-gate | `.tools/commit-gate.sh .tools/surprise-row-gate.py` | PASS | py_compile + ds-precommit + ruff clean |
| comp-tool-hud (rail) | -- | WARN | refused two of my Bash calls (a bare `find`; a `comp-find \| tail`) -- correct refusals; re-ran with `git ls-files` and `--limit` |

**What worked:** `--enumerate` with a printed denominator turned two "absent" reads into claims (the lost REGISTRY row; the FWD spacing). Grading the PRD with the gate's own function plus a negative AND a mutant control before commit.
**What failed:** none of the tools; my first `git log -- REGISTRY.md` HID the merge that dropped the row (default history simplification) -- `--full-history` was the instrument.
**Gap found:** `prd-header-notify.py` addresses the BASE serial (`RECIPIENT` default `2.0.0_SA_COO`); on site Z the base inbox is not watched, so the L4 -> L5 handoff needed a hand pointer to `2.0.0_SA_COO~Z` (19469). A device-aware recipient (or a lane-aware fan-out) is a real gap in the spine's handoff mechanism; surfaced, not built.

---

## Work Completed

### 1. Startup (06:31-06:37Z)
`/watcher`: NOT REGISTERED, no watcher process -> registered PID 12216, Monitor `bofr7iv3w` armed on `/cygdrive/c/`, arm banner `parent-tied: pid 594461`, `TaskOutput` running. XXX.md A-E: session serial file written, hook wired (no-op), 104/104 comp-tools resolve + forwarder EXERCISED, A.2 audit-archive 19 findings (all device-axis: 5 ERROR-FAILCLOSED absent laptop logs, 1 UNCOVERED `org/commit-msg-ascii-override-audit.log` -- surfaced to MSTR~Z, not chased). B.0: 2/2 READ. Receipt to MSTR~Z.

### 2. /canonical-flow NFRA_SECURITY202609 -- LOCATE + MEASURE (06:38-06:50Z)
```
CANONICAL FLOW -- 1.0.0_SA_CTO~Z on NFRA_SECURITY202609 (2026-09-03 06:4xZ)
LOCATE   home: flat only (org/missions/D12 ABSENT)   placement: site-z (D12 @efcfa8cc5b)   status: active
         brief docs/security/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md@a9a47f65a1 (NOT an admitted brief_ref shape)
         endpoint FWD-1..18 RATIFIED @7a51451d69 + s.7 @8cbe362358   PRD flat @72437a8453, NO PRD_HEADER, NO SURFACE MANIFEST
         decomp ABSENT   TOs 0 open / 0 terminal   rows 0   stamp none   dep_stage (claimed): REGISTERED
MEASURED limb: L2 -- highest conforming output: the ratified ENDPOINT section @8cbe362358
         claimed vs measured: DISAGREE in grammar only -- REGISTERED is a flat-register claim; not past L3 under the tree
CLASS    PRE-TREE (blocking) -> 1.0.0_SA_CTO L3.
         ARTIFACT-GAP at L3 input: the CODE fails PROJECT_TREE.contract.json R1 (SECURITY202609 = 14 chars > 12) -- a fork between
           renaming Andrew's verbatim code and widening the COO's contract. Census before the card: 10 of 354 flat codes over 12,
           4 active, and spec s.5's own example MDPF_COTREMEDIATION (14) among them. RESOLVED by Andrew: "Call it NFRA_OPSEC202609".
         ARTIFACT-GAP at L1 shape: the brief at docs/security/ is none of the three admitted brief_ref shapes (lane docs/briefs/** is ANY).
         ARTIFACT-GAP at L4: no PRD_HEADER, no SURFACE MANIFEST; FWD-10..18 defined with ONE space (gate needs two).
         REGISTER FINDING: the REGISTRY.md row added @74518cc788 was LOST in merge 729473905e (MSTR~Z, 09-02 21:46 -04:00).
ROLE     1.0.0_SA_CTO owns L2-L4; next limb L3 is MINE.
ACT      L3 then L4, below.
```

### 3. L3 -- register under the tree @32daebf403 (07:00Z; ON ORIGIN)
`org/missions/D12/NFRA/NFRA_OPSEC202609/project.json` (every flat field carried; `former_codes` chain; `dep_stage` REGISTERED; `fabric` site-z; seats CTO~Z/COO~Z/CVO~Z); `org/projects/NFRA_OPSEC202609.json` GENERATED (`home`); `org/projects/NFRA_SECURITY202609.json` retired; DIRECTIVES.yaml D12 member swapped (one token; grantee lane); MACROS.yaml D12 census RESOLVED clause appended; REGISTRY.md row RESTORED under the new code; brief MOVED bytes-identical (`cmp`) to `docs/briefs/` with a redirect stub at `docs/security/`. Tree check 0 violations. Spec s.8 prerequisite 7 (no fourth tree project before the water tests) lifted for this project by his ~06:3xZ word -- stated in the row and the commit.

### 4. L4 -- PRD v0.4 at the tree home @43b75ffbd6 (07:10Z; ON ORIGIN)
`prd/NFRA_OPSEC202609_PRD.md`: PRD_HEADER first (status RATIFIED, `brief_ref` @32daebf403, FWD-1..18); ENDPOINT byte-identical except the FWD-10..18 re-spacing; s.1-7 unchanged + the rename ruling in s.6; NEW s.8 SURFACE MANIFEST (contract @ecaa7c7dcb; 24 rows S1-S24; every `measured` cell attributed to the brief at its 09-02 vintage, nothing re-measured today; MECE run: 16/16 OWNS items, 18/18 outcomes, S20-S23 verify inputs); NEW s.9 sequencing input. Graded `[]` by limb 5 with negative + mutant controls. `dep_stage` -> PRD; index regenerated; REGISTRY cells to L4; flat PRD -> 4-line redirect stub. Handoff: notifier row 19465 to the BASE serial (QUEUED); pointer 19469 to `2.0.0_SA_COO~Z` (DELIVERED), cc MSTR~Z/CVO~Z.

### 5. Gate fix on this seat's surface @c3ef3a2530 (07:20Z; LOCAL)
`2.0.0_SA_COO~Z` finding 19466: `surprise-row-gate.py _blob` decoded its git pipes with the locale (cp1252 here), so one U+2B50 at HEAD in `D1_CATVIEWS/INVESTIGATION_v1.md` emptied stdout and the gate refused EVERY new row as "ZERO rows" -- it would have refused NFRA_OPSEC202609's own L7 rows. Fix: `encoding="utf-8", errors="surrogateescape"` on both calls. Falsified at this seat on the live HEAD blob: BEFORE status=OK chars=0 (decode traceback on the pipe); AFTER chars=80,686, star present; ASCII positive control 4,775 both times; self-test 0/6 failed; commit-gate clean. The other two gates the finding named read bytes and need nothing.

### 6. SMS watch-entry held form (07:24Z; LOCAL, this commit)
MSTR~Z FYI 19464: the laptop reader classed `d12-sms-origination-identity-activation` as OPEN 16.8 h past a 0.0 h window, HELD-CLAIM REJECTED. Read `_qualifies_as_held` at source: every open leg must be `verify`. Reshaped as the watch item it is: SP-1 and SP-3 re-kinded `verify` (reads), SP-2 (the future Terraform apply on Andrew's GO) moved to `deferred_apply` -- it opens as its own ledger entry when the GO comes. `deploy_ledger.py check` now prints `HELD ... tracked-not-stranded`; `_qualifies_as_held` -> True. Nothing in AWS or code changed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Put the R1 code fork to Andrew rather than rename or widen myself | The code was his verbatim word (09-02); the contract is the COO's; the spec's own example violates the bound. He answered in one line. |
| Move the brief to `docs/briefs/` (lane ANY) instead of the tree `brief/` (lane TREE_CRO) | No CRO seat exists on site Z; `docs/briefs/` is an admitted `brief_ref` shape; bytes identical; redirect stub keeps every old citation resolving. |
| Two commits (L3, then L4), not one | `brief_ref` needs `@<commit>` where the file exists at that path -- the header must cite the L3 hash. |
| Re-space FWD-10..18 rather than widen the gate regex | The regex is the contract every tree PRD meets; nine outcomes were off it by one byte each. Text otherwise byte-identical. |
| Take the gate fix now, in-session | It sits on my surface and would refuse this project's L7 rows on this device; two lines, falsified both ways, self-test + commit-gate before commit. |
| Reshape the SMS entry's legs, not its status | The reader judges the LEGS; the entry is a watch, not a half-landed deploy; the future apply is recorded, not deleted. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D12/NFRA/NFRA_OPSEC202609/project.json` | NEW tree row; then dep_stage -> PRD | Yes -- `32daebf403`, `43b75ffbd6` (ON ORIGIN @a79ba791e6, is-ancestor read 07:1xZ after fetch; positive control b80b692a1d) |
| `org/missions/D12/NFRA/NFRA_OPSEC202609/prd/NFRA_OPSEC202609_PRD.md` | NEW v0.4 (header, manifest, sequencing) | Yes -- `43b75ffbd6` (ON ORIGIN) |
| `org/projects/NFRA_OPSEC202609.json` / `NFRA_SECURITY202609.json` | generated / retired | Yes -- `32daebf403`, `43b75ffbd6` |
| `org/missions/DIRECTIVES.yaml`, `org/missions/MACROS.yaml`, `org/projects/REGISTRY.md` | member swap; census clause; row restored then L4 cells | Yes -- `32daebf403`, `43b75ffbd6` |
| `docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md`, `docs/security/...` (stub), `docs/architecture/NFRA_SECURITY202609_PRD.md` (stub) | brief moved; two redirect stubs | Yes -- `32daebf403`, `43b75ffbd6` |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260903_065xZ_CTOZ_CALL_IT_NFRA_OPSEC202609.md` | NEW record | Yes -- `32daebf403` |
| `.tools/surprise-row-gate.py` | `_blob` explicit utf-8 on both pipes | Yes -- `c3ef3a2530` (LOCAL) |
| `org/critical_paths/.open_deploys/d12-sms-origination-identity-activation.json` | legs reshaped to the held form; `deferred_apply` | Yes -- this log's commit (LOCAL) |
| this log | -- | Yes -- this commit (LOCAL) |

Push state of the LOCAL rows: `0.0.0_AB_MSTR~Z` integrates SITEZ (LD-0367); stated as LOCAL at the time of writing.

---

## Blockers

None on this seat. Not BLOCKED: L5 is `2.0.0_SA_COO~Z`'s limb by role exclusivity; this seat does not wait on it, it waits FOR it (the L10 grades, or a `SCOPE_CHANGE` re-entry at L2).

---

## Current State

NFRA_OPSEC202609 is at `dep_stage: PRD` at `org/missions/D12/NFRA/NFRA_OPSEC202609/`, both limb commits on origin. L5 handed to `2.0.0_SA_COO~Z` (19469). Four items are CARRIED TO ANDREW as cards, not the decomp's to decide: the FWD-13 website-edge choice (CloudFront+WAF vs Cloudflare -- reverses his 2026-07-13 line; S13 cell HELD until his word), the morning digest EMAIL (C-6), Object Lock on `cases/` (C-8), final thresholds after a month of WATCH rows (C-3). The gate fix and the SMS entry reshape are LOCAL. Watcher `bofr7iv3w` live; zero crons.

---

## Next Steps (for the successor 1.0.0_SA_CTO~Z after the /govern kill, and for this session if it lives to L10)

1. **[1.0.0_SA_CTO~Z, this session]** At L10: write `ledger/COMPLETION_GRADES.round<N>.json` against the EXERCISED artifact each `DONE WHEN` names, never the COO's report (spine v2.3); adjudicate any `SCOPE_CHANGE` with `/open-calls --adjudicate`. Nothing to do until rows and a stamp exist.
2. **[successor, OPAL_TICKET_VNEXT / D7]** Before the first act, the two L3 forks `3.0.0_SA_CVO~Z` measured (19453) stand: MACROS.yaml has NO D7 entry (R2 refuses any D7 tree folder until Andrew ratifies a D7 macro enum -- a Rule 24 record + census, MSTR~Z as register owner), and `OPAL_TICKET_VNEXT` fails R1 on its second underscore (needs his word for a `<MACRO>_<NAME>` code, exactly as NFRA_OPSEC202609 did). Also: DIRECTIVES.yaml D7 stance still carries his 2026-08-25 "D7 is effectively on hold"; his 09-03 sequence is the later word -- relay both, adjudicate neither. The D7 PRD @c2837692bc has no header/endpoint/manifest, and a COO decomp @e9ca70c307 predates any endpoint (out of limb order; L2 first).
3. **[successor, ASSETCLASS_TAXONOMY / D4]** claim BRIEF; next limb L2 `/endpoint --forward`. D4's macro enum in MACROS.yaml: check before L3 (only D0, D8, D11, D12 are ratified today).
4. **[1.0.0_SA_CTO, any device]** the notifier gap: `prd-header-notify.py RECIPIENT` is the base serial; on a lane-only fabric the L4 -> L5 handoff needs a lane-aware recipient. Surfaced here and in 19469; a fix is a spine-mechanism edit, not this project's.
5. **[0.0.0_AB_MSTR~Z]** push legs for `c3ef3a2530` and this commit when convenient; nothing waits on them.

---

## Amendment 07:5xZ -- the reconcile pick the successor must know (0.0.0_AB_MSTR~Z 19498, relaying the laptop 1.0.0_SA_CTO 93312)

**One defect, corrected twice.** `.tools/surprise-row-gate.py _blob` is fixed on BOTH fabrics: here @c3ef3a2530 (two call sites, `errors="surrogateescape"`); on the laptop @e58250f261 (LOCAL there at 07:44Z; origin/CLOUD still 3bd8d2ef04), which fixes the same class at **20 call sites in six tools** (`surprise-row-gate.py`, `to-pipeline-gate.py`, `proof-of-spec-check.py`, `prd-header-notify.py`, `to-decomp-ref-lint.py`, `surprise-corpus-validate.py`) with `errors="replace"`, batteries 6/6 + 6/6, and **makes the PRD notifier lane-aware** (RECIPIENT = the COO on the committer's lane, so the L4 -> L5 handoff reaches `2.0.0_SA_COO~Z` without a pointer -- the gap "Gap found" above names, closed there).

**At the next CLOUD -> SITEZ reconcile the `_blob` hunk CONFLICTS on identical base-side ranges. It is a PICK, never a union: take the laptop's wholesale** (wider, and the notifier fix rides with it). This seat's reading for the audit of the loser: for a gate that only READS a blob and greps rows, `replace` is the safer choice -- a surrogate-escaped string raises on any later plain `.encode("utf-8")`, a replaced one never does. The laptop's choice should win on the merits, not only on width.

Also closed on the laptop, for `3.0.0_SA_CVO~Z`'s LD-0319 read: `06_current_state` regenerated @c08c1bbe99; the rule-bank marker check is correct to FAIL (marker absent, not stale). Row NFRA_OPSEC202609-Z-S1 (OBSERVATION/ARMED, disarm at L10) has its remedy in flight on the other fabric.

State at this amendment: NFRA_OPSEC202609 at L7 round 1 (`dep_stage: EXECUTING` @94b6fd0d11; four TOs @5494591e91; seats `0.7.0_AE_CloudOps~Z` + `~S` live). L2-L4 and every row-owner flip current. Waiting: Andrew's word on OP-x-2 (website edge) and OP-x-1 (probe list); then the L10 grades.

---

## Amendment 08:4xZ -- three L4 rulings on one constraint, and a second fabric gate

**PRD v0.5 / v0.6 / v0.7** (@a3cad58b0d ON ORIGIN, @b482fe8a5b ON ORIGIN, @237265f9f1 LOCAL): three referents in the ratified C-8 were asserted from the brief's reading and never read until the round-1 workers re-grounded them -- the KEY ("the estate CMK" = the AWS-managed DynamoDB key; now ONE project CMK `alias/opal-security`, C-13, S25), the ROLE ("CTO-admin" existed nowhere in 216 roles; now `opal-security-admin`, C-14, S26, its TRUST = card OP-x-6), the TARGET ("the CloudTrail bucket" admits only cloudtrail.amazonaws.com; now a project-owned `opal-data-security-access-logs`, C-15, S27, graded by a DELIVERED object). Each ruled at L4 as a referent correction with intent unchanged, disclosed to Andrew at this terminal, reversible by one word; the COO folded v0.5/v0.6 into decomp v0.1.1 @1f9d207d6b and all three seats agree Z-S3 graduates with the L4 bump as remedy (no route). Rule banked at this seat: a constraint names no resource it has not read at a vintage.

**Halt gate** (@1c4a867709 LOCAL; MSTR~Z 19540): one guard line closes the list/stat race that refused an integrator push with "(age unknown)"; and the gate's only battery had been DEAD since 2026-07-13 (identity via the removed .agent_context fallback; 0/3, every arm exit 3) while three gate edits landed unseen -- revived hermetic, 6 arms + a mutant control, 7/7. The mutant control caught my own first cut (marker on the comment line, not the guard line) before commit.

**Cards at Andrew, unchanged:** OP-x-2 (website edge; rec CloudFront + managed rules), OP-x-1 (the probe list), OP-x-6 (who may assume `opal-security-admin`; rec Andrew alone for round 2). State: L7 round 1, seven of eight S-17-16 resources applied; the logging limb, the key flip and the role are round 2.
