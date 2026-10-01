# Call 3 (Part D), OG-t-2 PHASE A to signed halves, TRNSPT-DEPS decomposition -- 2.0.0_SA_COO~O

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE
**Date:** 2026-09-30 17:18Z .. 2026-10-01 01:14Z
**Task Order:** NFRA_OPLGTW.TO-OG-t-2 (PHASE A drained; PHASE B ready); workstream TRNSPT-DEPS orders drafted (branch)
**Status:** IN PROGRESS -- OG-t-2 PHASE B waits on Andrew for the K2 read; TRNSPT-DEPS issuance waits on OG-t-2 landing

## Objective

Seated by `0.0.0_AB_MSTR~Z` on `1.0.0_SA_CTO~O` msg 27277 to drive Andrew's call 3 (G-D walkthrough + Part D) for
NFRA_OPLGTW. Then follow what the call released: OG-t-2, and PRD v1.2's TRNSPT-DEPS workstream (step 5).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | `'sender.table\|SENDER_TABLE\|senders\.json\|sender_table' org/missions/D9/NFRA/NFRA_TRNSPT data/transcripts --files` | PASS | 0 hits / 70 files: the sender table is not in the repo (gate G-SENDERS) |
| prd-signoff | `status NFRA_OPLGTW` | PASS | v1.2 ADMITTED (ratified-text current by ENDPOINT hash) |
| safe-merge | `wk-NFRA_OPLGTW-12-t2`, `coo-o-trnspt-deps` | PARTIAL | first drain swept a peer's unstaged project.json (row Z-S23); second clean, 1 file |
| to-pipeline-gate | issuance commit c9912a6581 | FAIL then PASS | comp-iam disposition missing on OG-rl-1; fixed by removing IAM from the order |
| to-decomp-ref-lint (gate2) | same commit | WARN | ANNOUNCE mode; seating parses `0.9.0_WK_NFRA_OPLGTW~15` as base `0.9.0_WK_NFRA` |
| missions-tree-check | R3-T commit in sparse worktree | FAIL then PASS | needs `org/projects` in the sparse set |
| proof-of-spec-check | read (expect semantics) | PASS | `expect` is a regex searched over output; multi-line expects need `(?s).*` |

**What worked:** content checks (md5 13/13, added-line presence 460/490, tier.py principal-read counts with a positive
control) settled every release-order question that git ancestry answered wrongly.
**What failed:** two shared-tree hazards in one evening: a peer's merge swept or lost uncommitted edits (mine and the
CTO's), and safe-merge's staged-set refusal does not cover a peer's unstaged edit.
**Gap found:** gate2's seating lint misreads worker serials whose CODE contains an underscore (announce-only).

## Work Completed

### 1. Startup
- Registered (PID 52352), `/watcher` armed; reaped 2 orphan watchers (53132, 13732); 9 queued messages acked.

### 2. Call 3 = Part D only (CTO~O msg 27304)
- G-D cannot start: the G-C record is absent and OG-g-1 is BLOCKED-EXTERNAL on Opal IT. Alyssa's real grant does not
  substitute.
- Part D as written could not yield `<tid>/<oid>`: the owner header carries `sub` only (E1_G-HDR_READ). Source
  switched to the Entra admin center (row Z-S20).
- Andrew pasted tenant ID + 3 object IDs (20:54Z-20:57Z). They are stored off-repo
  (`%LOCALAPPDATA%\opal\og-principals\part_d_20260930.json`, sha256 5367971...). Alyssa's pair matches her grant key.
  Record PART_D_RECORD_20260930.md @205c2e7f6c.
- /next-calls -> Andrew "Go with your recs": G-C = he chases IT (record @205c2e7f6c).

### 3. OG-t-2 (narrow tier-auth release)
- A1 @ad55c31336: grade by content (row Z-S21). Live 42c52ed4d9 has the 4 build commits in its history but not its
  bytes.
- Worker 0.9.0_WK_NFRA_OPLGTW~12 PHASE A, drained @0a5cc3c093:
  - 13/13 md5;
  - 15 files +774/-42;
  - 50+6 tests passed;
  - 9 identities, 0 tier deltas;
  - 0 of 6 clients expiring;
  - rollback 87/87.
- A2 @4d1f1dc038: my own two check defects (rows S4/S5) fixed; disarm row Z-S22.
- Never-widen ask @0e3760b480. CTO half SIGNED @51df60aa1a. CVO half SIGNED @045f6886d9 (K1-K3: K2 = a post-release
  call as Opal Bloomberg must read write-capable).

### 4. Other
- Laptop mail branches triaged @6d41bd25ec (adopt int, supersede f1-f3).
- project.json blocking refreshed @85a765dbcd.
- MX-r-6 v3 hold released to `2.0.0_SA_COO~MI`; OG-t-2 queued first, ahead of its MX-r-7.

### 5. TRNSPT-DEPS (PRD v1.2 C7 @c9fd271499; CTO msgs 27436/27439/27452)
- Decomposition ADDENDUM R3-T merged @0c16bb66ba: 7 cells, 3 slots, gates G-TEAMS-TX / G-SENDERS / G-MEETINGS.
- 7 orders + 16 check files committed on branch `coo-o-trnspt-deps` @c9912a6581 (NOT on CLOUD; the merge is the
  issuance).
- Check controls: _reg.py reads absent tools False, read_email True, scopes 17/17.

## Decisions Made
- Part D's principal source = Entra admin center read by Andrew (no roster widens: same 3 people as the email rosters).
- OG-rl-1 carries no IAM change; a missing secret read is a BLOCKING row back to the issuer.
- TRNSPT-DEPS orders stay on my branch until OG-t-2 lands (CTO's order), rather than issued staged now.

## Files Modified
See commit messages: 79c4956122, 205c2e7f6c, ad55c31336, 85a765dbcd, 6d41bd25ec, 0a5cc3c093, 4d1f1dc038, 0e3760b480,
5eeca31a92, 7bf0ce5cb0, 0c16bb66ba, c9912a6581.

## Blockers
- OG-t-2 PHASE B: needs Andrew to open the Analyst window (`C:\Users\Opal Bloomberg\.opal_runtime\launch-v2.ps1`) for
  K2's Opal Bloomberg call. Evidence: CVO half @045f6886d9 K2; CTO~O relay 27443 names that session as the only one.
- OG-g-1 / OG-v-7 (G-C, G-D): BLOCKED-EXTERNAL on Opal IT (Andrew chasing, record @205c2e7f6c).
- OG-v-8: held on G-E/G-F.

## Current State
- Gateway `i-07dccb1615503ac99` serves `42c52ed4d9` (MX-r-6 v3, 18:33:41Z).
- OG-t-2 release branch `rel-nfra-oplgtw-tier-auth` @d61fde4693 in `/c/tmp/og-rel2`; rollback tree `/c/tmp/og-rb2`;
  worker worktree `/c/tmp/wk-oplgtw-12` (branch wk-NFRA_OPLGTW-12-t2, drained). Order `<status>pending</status>`.
- PHASE B env (never commit): `OG_MASTER_ADMIN_PRINCIPALS` / `OG_WRITE_CAPABLE_PRINCIPALS` from the off-repo Part D
  file; `DEPLOY_BASE_REF=42c52ed4d9e834b0f1cf4f96eb83f9b0f7a183df`.
- My worktree `/c/tmp/coo-o-wt` (branch coo-o-trnspt-deps @c9912a6581, sparse).
- Push state: origin CLOUD 85a765dbcd (ls-remote read 01:14Z); later commits LOCAL.

## Next Steps
1. On Andrew's "ready": tell [2.0.0_SA_COO~MI] "deploying". Then continue worker ~12 into PHASE B (steps 8-12) with
   the env above. K2 read via the Analyst window; admin read via this seat's gateway session (Andrew). Send the landed
   ref and read-back to [2.0.0_SA_COO~MI].
2. After OG-t-2 lands: safe-merge `coo-o-trnspt-deps` (= issuance, round label 8), then spawn slots ~15/~16/~17.
3. Ask NFRA_TRNSPT (via [1.0.0_SA_CTO~O]) for Yang's addresses (G-SENDERS) before OG-rl-1 PHASE B.
4. At OG-t-2 close: remove `%LOCALAPPDATA%\opal\og-principals\part_d_20260930.json`.
