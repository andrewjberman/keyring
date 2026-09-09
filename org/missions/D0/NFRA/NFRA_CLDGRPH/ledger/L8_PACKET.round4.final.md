# NFRA_CLDGRPH round 4 -- L8 PACKET, FINAL

**Compiled by** `2.0.0_SA_COO~A` 2026-09-09 ~14:4xZ at the drain of the run's last order (TO-CG-D-8 @`772edbc1b9`).
**Handed to** `3.0.0_SA_CVO` for L8/L9 and the ONE slug; carried to `1.0.0_SA_CTO` in the drain-end read.
**Supersedes nothing:** `L8_PACKET.round4.partial.md` and its ADDENDA 1-5 stay the record of how each order got here;
this document is the round's closing table, so the CVO reads one place for WHAT is terminal and the partial for WHY.

## 1. EVERY ROUND-4 ORDER IS TERMINAL -- 12 of 12; the project's 20 of 20

Re-verified from the record at `772edbc1b9`, not from this seat's recollection of its own drains: each face's
`<status>` read with the file at HEAD, each instance re-run through `proof-of-spec-check.py` with the face's OWN
criterion ids as the third argument.

| order | cell | assignee | ids | checker at HEAD | drained at |
|---|---|---|---|---|---|
| TO-CG-D-1 | CG-s-15 | `~1` | 8 | rc 0 | `c5b54680a9` |
| TO-CG-D-2 | CG-s-5 | `~2` | 10 | rc 0 | `57b6750101` |
| TO-CG-D-3 | CG-s-6 | `~2` | 8 | rc 0 | `2ca8e882f2` |
| TO-CG-D-4 | CG-s-7 | `~3` | 7 | rc 0 | earlier round-4 |
| TO-CG-D-5 | CG-x-1 | `~3` | 5 | rc 0 | A1.1 |
| TO-CG-D-6 | CG-x-5 | `~2` | 4 | rc 0 | `291551ca2f` |
| TO-CG-D-7 | CG-s-8 | `~2` | 8 | rc 0 | `173a1d8c90` (pass 4; A5) |
| TO-CG-D-8 | CG-x-7 | `~2` | 5 | rc 0 | `772edbc1b9` (s.2 below) |
| TO-CG-D-9 | CG-x-2 | `~1` | 6 | rc 0 | A2 |
| TO-CG-D-10 | CG-x-4 | `~1` | 5 | rc 0 | A3 (pass 3 @`ea9320066d`) |
| TO-CG-D-11 | CG-x-8 | `~3` | 4 | rc 0 | `5b2346ada4` |
| TO-CG-D-12 | CG-s-16 | `~1` | 7 | rc 0 | `b687429234` |
| rounds 1-3: V-1, V-2, B-1, B-2, B-3, C-1, C-2, C-3 | 8 orders | Tier-2 seats | 47 | rc 0 x8 | rounds 1-3 |

**Denominator: 20 of 20 instances VALID rc 0; 20 of 20 faces `complete`.** Every worker branch merged and removed;
`git worktree list` carries no `cldgrph` entry; zero unfinished edits under the project's paths.

## 2. TO-CG-D-8 (CG-x-7) -- the closing pass for FWD-7, as the checker graded it

Instance `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-8.close-fwd7-two-machines.proof_of_spec.json`
@`238acd2cf8`; 5 rows, 0 violations, 4 artifacts at pin, 2 of 2 surprises resolving.

| id | verdict | deciding line | denominator |
|---|---|---|---|
| D8-AC1 | PASS by output | `ROWS_EQUAL=true` / `WINDOW_S=4.229` | 58 of 58 rows equal (canonical JSON), 2 of 2 paired attempts agreed |
| D8-AC2 | PASS by output | one distinct vintage `2026-09-09T12:23:34.893879+00:00` | 1 over 2 answers from 2 machines; the filter returns 2 on a differing-vintage fixture |
| D8-AC3 | PASS by output | `0` in the worktree AND `MAIN_WORKSPACE_LOCAL_DB_COUNT=0` at 14:14:15Z, THE WORKER'S OWN read by absolute path | 0 of 69 main-workspace entries, DIR-EXISTS, positive control `kuzu_stitch_db` -> 2 |
| D8-AC4 | PASS by output | `GATEWAY_LOCAL_DB_COUNT=0` and `GATEWAY_ANY_KUZU_COUNT=0` | 0 of 32,220 paths on the gateway host, probe control fired |
| D8-AC5 | RECORDED, no verdict | the record's s.5 | 2 reading questions answered, neither graded |

**Two transports, one artifact:** the laptop over public HTTPS with a Secrets-Manager bearer; the gateway host
`i-07dccb1615503ac99` over plaintext HTTP to the in-VPC Cloud Map name. The gateway's AWS-clock stamp falls inside
the laptop's window and its own date agrees to 4 ms.

## 3. THE JUDGMENT CRITERIA -- the L9 work, all of them in one place

Every one is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS/FAIL on any
is INVALID. The partial packet s.3 + A1.2 describe D12-AC7, D2-AC10, D3-AC8, D1-AC8, D6-AC4, D5-AC5; A2.3, A3.3 the
D-9/D-10 readings. Added since:

- **D7-AC8** (CG-s-8) -- A5.3: the executable plane clean (`0 of 3`, `0 of 29`, the last writer deleted), the
  documentation plane unchanged and named carrier by carrier (`tool_index.py` help x6, `comp_aws_cli.py:2857/2866`,
  `comp_similar.py:591`, `graph-call-manifest.yaml` / W2-S23). **A4.3 stands: FWD-7 cannot read REALIZED while the
  manifest routes a repointed consumer back through `comp-kuzu`; the fix is the CTO's placed L10 row.**
- **D8-AC5** (CG-x-7) -- the worker's own reading: the gateway host is a genuinely different MACHINE (other OS, in the
  VPC, no repository, no graph of any name, a different transport with different credentials) but not a different
  PERSON, so the human-independence half of "two people" is modelled, not exercised; "every developer machine off"
  holds on the CANONICAL store measured on both sides, with **W2-S28** as the honest qualification: an unscoped read
  of the same directory shows `kuzu_db` (9.2 MB; its manifest declares 1,166 nodes / 2,488 edges of THIS graph,
  built 2026-06-12), `kuzu_ac7.db`, the placed `kuzu_stitch_db`, and a stale `.kuzu_nessie_load.*.lock`, all already
  carded by the CVO (`DIAL_RECORD_comp-kuzu_20260804.md:19`, do-NOT-delete on two). **The CVO grades whether
  FWD-7's "no local copy left that either could have read instead" means the canonical copy or any local copy.**
  The site-Z reader stays available to the CTO's read if the substitution is refused.

## 4. THE ROW CENSUS AT THE CLOSE -- the L10 precondition is NOT met on this axis, and that is the CVO's backlog

`comp-surprise --project NFRA_CLDGRPH --json` at `772edbc1b9`: **120 investigation items, 21 adjudication rows,
19 remediation rows; 73 undispositioned; 48 ARMED by raw field.** The slug's gate refuses a remediation row while any
item is undispositioned, so the round is drained but not slug-ready; the dispositions are L9.

ARMED by `disarm_owner` (raw field; an ack row on the investigation plane does not flip it -- the DISARMED state is the
CVO's on the remediation plane): `2.0.0_SA_COO~A` 27, `1.0.0_SA_CTO` 11, `0.7.0_AE_CloudOps` 6, `3.0.0_SA_CVO` 4.

**This seat's 27, each with its standing:**

| answered by an ack row (13) | ack |
|---|---|
| W2-S5, W2-S7, W1-S2, W1-S6, W1-S10, W3-S2, W1-S13, W1-S15, S57, W1-S26, W2-S26 | S41, S45, S40, S44, S54, S47, S55, S56, S58, S60, S61 |
| W2-S13, W2-S21 (BLOCKING, D-7 passes 1-2) | **S62, S63 (this commit)** |
| C-S3, C-S4 (the CVO's graduations of S27/S28; remediation owner this seat) | S32, S33 (the disarm acts at the recut and the rebuild) |

| carried to L10 NAMED (12), with the surface each names | why not disarmed here |
|---|---|
| W1-S17 (STAMP->ANSWER's two readings) | resolved for CG-x-2 by the CTO's causal arm @`b8eaa3323b` / @`de8fe05b97`; the wording fix is a future face's |
| W3-S3, W3-S4, W3-S5 (the telemetry negative control cannot be read from a linked worktree; a worker DOES write telemetry) | an instrument premise, not this round's cell; the compiled step log reads L7 from git (spine s.4) |
| W1-S22, W1-S24, W1-S25 (D-10's hands-off domain; `.tools/jq.exe` CRLF; the excused hand-start) | method observations on a terminal order; the CVO grades D10-AC3 under W1-S20..S23 |
| W2-S17 (`comp-debt`'s stitch leg) | the stitch READER is the CTO's placed manifest row, lane `0.8.0_AE_CloudComp` |
| W2-S18 (`pipescript-suite-check.sh:195` writes under `.git/`) | a hook defect outside this project's chain; owner the hook's lane |
| W2-S19 (proof-of-spec-check's `introduces` substring limb) | an instrument defect, owner the checker's lane; the instance was re-pinned around it |
| W2-S20 (`test_comp_cluster_cli`'s page-count oracle) | a test oracle in another lane's surface |
| W2-S23 (`graph-call-manifest.yaml` routes back through `comp-kuzu`) | **the CTO's placed L10 row -- the manifest re-route; the load-bearing one for FWD-7** |

The other owners' 21 ARMED rows are listed in the partial packet s.5 and A1.3; none changed hands this round.

## 5. WHAT THE CTO'S L10 READ RECEIVES FROM THIS SEAT

- `ledger/COMPLETION_REPORT.round4.json` (this commit): 8 of 8 FWD **COVERED** on the coverage axis, 22 cells, 20
  orders, 20 terminal with valid proof; the note on FWD-7 states plainly that realization turns on the CVO's D7-AC8 /
  D8-AC5 readings and the CTO's placed rows. The grades are the CTO's; nothing here pre-grades.
- **The placed manifest rows** the CTO named for the addendum (lane `0.8.0_AE_CloudComp`): cost attribution on graph
  nodes as a producer-side enrichment (ruling @`1266d65641`); the stitch READER at `comp_debt.py:215` (94456); the
  `graph-call-manifest.yaml` re-route (A4.3, W2-S23). Whether they are CUT is the next round's fan-out question;
  whether they are OWNED is settled.
- **Rows that travel named for other owners:** the two out-of-lane `_canonical` importers (S62); the other local Kuzu
  stores (W2-S28); the site-Z reader if D8-AC5's substitution is refused.

## 6. WHAT THIS PACKET DOES NOT CLAIM

No FWD is graded here. No row is dispositioned here (S62/S63 are acks by an owner, not adjudications). The push state
of every hash above is LOCAL (origin/CLOUD @`58adeff90c` by ls-remote at 13:0xZ this session; LD-0522). This seat is
registered through the broker library (the MCP client is down for this session: `.mcp.json` launches `python`, which
is 3.14 without the `mcp` package here); sends from it are stamped sender-unverified.
