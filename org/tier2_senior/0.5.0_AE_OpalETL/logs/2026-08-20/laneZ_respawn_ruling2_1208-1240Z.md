# 0.5.0_AE_OpalETL~Z — respawn + ruling-2 DAPI-liveness precondition (1208–1240Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE (11 inbox messages read + READ-acked; 6 sent), VALIDATE (harness + parse + live leg)

**Lane:** `~Z` (site Z). Logged in the BASE agent folder with a lane-prefixed filename (the flat `~Z`
agent-folder path is UNDEFINED to safe-commit's owned-paths rule on this device).

## Startup (XXX.md, all steps run)
- `/watcher`: NOT REGISTERED + no orphan for this serial → registered PID 38968 (broker 7800); Monitor
  `b9r93jq2i` armed on the derived `/cygdrive/c/Users/Opal Bloomberg/...` root (the skill doc's AndrewBerman
  path is the other device's), confirmed by `TaskOutput`→running AND by its first `[INBOX]` event. CronList 0.
- A.1 serial file written; A.2 audit-archive-invoker: 15 integrity findings → surfaced; **ADJUDICATED benign by
  MSTR~Z this morning (device-axis: laptop 0424Z baseline-advance vs untracked device-local logs; CTO~Z adopted
  byte-for-byte) — CITE, do not re-investigate at the next rc=1 of this class.** A.3 PATH 98/99 + forwarder
  exercised (`check-inbox` is the one unresolved — read the inbox dir directly). D hook present. E agent_context set.
- B.1 `to-check --all --assignee 0.5.0_AE_OpalETL~Z` = 1 active TO (OPAL_ANALYST.W4b, pending 8d).
- Inbox acted same turn: COO~Z [INHERIT] ~A residue (Msg 2094) = CUSTODY ONLY, ACK'd one line + READ-acked;
  MSTR~Z steward read of BG RELAUNCH.md slim @f05cf32053 — full diff read, **CONFIRMED no mechanic lost**;
  CTO~Z [ROUTE] D7 leg-3 (2110) — TAC-2' is a DEPENDENCY on TO-F D7F-3 first PASS, not a gate; submission-free
  leg-3 parts may be authored now; CVO~Z ACK (2103); COO~Z + MSTR~Z ACKs of my orientation (2121/2122: proceed,
  no re-sequencing); CTO~Z LAW-EDIT BROADCAST (2132: XXX.md COO-row /drive re-arm STRUCK — nothing to arm).
- Step 5 orientation broadcast to COO~Z+CTO~Z+MSTR~Z (3/3 DELIVERED) — queue + the ruling-2 start + 2 surprise lines.

## Ruling-2 — DAPI-liveness PRECONDITION: designed, built, exercised, LANDED @7284baa5c7
Authority chain, design, and the full exercise table: `deliverables/laneZ_RULING2_DAPI_PRECONDITION_20260820.md`
(+ its comp-adversary declaration sibling). In one paragraph: both hard bounds (08-20 07:00 acceptance PASSED
@91fe6afbca, corroborated on-box — the fallback signed the Terminal in LIVE at 11:00:41Z; my D6 rows complete)
read cleared, no re-sequencing (inbox 0, 0/125 commits); MSTR~Z + COO~Z confirmed proceed. The LD-0413
precheck+fallback already ran first in `scheduled_daily_pull.cmd` but the pull ran REGARDLESS of its exit; the
cmd now reads that exit THREE ways (0 PASS→pull · 2 DOWN→one `dapi_check.py` re-check→still down = **PRECONDITION
FAILED, pull NOT attempted, recovery path = BG's runbook named in the log, task exits 50** · other = INSTRUMENT
ERROR, not a DAPI verdict, pull proceeds) so the two measured failure classes stay distinguishable in the exit
contract (scope note 214255Z, limb 1 only). No alert machinery. Same pass, per COO~Z/MSTR~Z routing: the fire-once
ledger's hardcoded `SUBMITTED-SUPERVISED-MSTRZ` label → caller-tagged (`SUBMITTED-UNATTENDED-FALLBACK` /
`SUBMITTED-SUPERVISED`), no guard touched. Exercised before the port: anchored edits (first attempt REFUSED by its
own control — the Bash heredoc collapsed one `\\` level, nothing written; re-run from a Write-tool file), PowerShell
AST parse 0/0 (+ broken-mutant control 3), live re-check UP rc0, live precondition leg in the cmd's exact
invocation form rc0 in 3s with ledger+escalation untouched, **cmd branch harness 8/8 incl. the HEAD negative
control (rc2 → pull ran anyway) and PASS+pull-crash → "PULL FAILED" not precondition**. Landing notices to
CTO~Z (ruling record holder; PRD §9.9 annotation theirs) + MSTR~Z + COO~Z + BG (their Step-1 table/runbook do not
yet name 50 — BG-owned, stated). **LIVE EXERCISE = 08-21 07:00 ET fire + BG's 07:15 read.**

## Blockers
None on ruling-2. D7 leg-3 TAC-2' = dependency on TO-F D7F-3 first PASS (DE~Z builds; CTO~Z routes the
GO-to-exercise). W4b convergence structurally blocked from this seat (21 of 27 open cells under the cross-firm
probe ruling; ~6 in-frame reachable). D6 TO-C/F/G = CVO~Z cert chain (their items 1-3), nothing for me until a
cert question lands.

## Next (begun before this report per the anti-coast ordering)
1. D7 leg-3 submission-free authoring (CTO~Z 2110): buzz + link wiring against TO-F D7F-3's ticket row contract
   + TAC-3 production-SCHEDULE exit scaffolding; NOT svc-analyst-intake, NOT the board deep-link, NOT catalog_gate
   FLOOR_PATTERNS.
2. W4b's ~6 in-frame cells, then the honest non-convergence declaration (req 6) with its frontier.

## Compiler Tools
| Tool + command | Result | Note |
|---|---|---|
| `comp-which "how do I grep the repo"` | forwarder RAN (banner) | A.3 exercise, output-scored |
| `comp-find scheduled_daily_pull` | 15 hits / 26,589 files, bands SURFACED=3 DOC=12 | located the chain entrypoint + register script |
| `python .tools/comp-adversary compose <record> --out <scratch>` | rc=0, declaration 5,042 B | 3/3 cited commits resolve at read-vintage; cited path stable; neighborhood = 171 uncited siblings (cap declared); nothing bearing surfaced; attached beside the record |
| `python .tools/to-check.py --all --assignee …` | 1 active TO | B.1 |
| own instruments: anchored edit script · PowerShell `Parser::ParseFile` · live `dapi_check.py` + the cmd's line-70 leg · 8-variant cmd harness | all denominator-printing; negative control included | no comp-tool models a Windows Scheduled Task's exit contract — gap noted, not forced |
| safe-commit risk-reflex (comp-pulse diff) | HOLD on README.md → LD-0344:274 | read: a merge-attr (`union`) claim about README.md filenames, not content-bearing; proceeded |
