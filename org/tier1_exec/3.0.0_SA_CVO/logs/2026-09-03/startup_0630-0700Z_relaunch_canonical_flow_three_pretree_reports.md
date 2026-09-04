# 3.0.0_SA_CVO~Z startup, 2026-09-03 0630-0700Z -- relaunch on LD-0522 A2; three /canonical-flow reports, all PRE-TREE

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

Seat: `3.0.0_SA_CVO~Z` (NFRA verifier, ~Z lane; L8-L10 owner under the spine). Site Z.
Spawned 06:30Z by `0.0.0_AB_MSTR~Z` after the CLOUD -> SITEZ law leg landed @55da5aa2c1.
Measured at HEAD fc78faf65c = origin/SITEZ (ls-remote 06:50Z).

---

## SUMMARY

Startup ran clean: watcher armed, 31 of 31 ackable delivery rows READ by this serial, zero crons,
LD-0319 read DRIFTED and surfaced. Andrew typed `D7` at this terminal; the routing message (19434)
assigned `--report-only` on the two D12 projects. All three were measured under `/canonical-flow`
and all three read PRE-TREE with a shared L3 bar: none of the three codes matches the tree
contract's code regex, and D7 has no ratified macro at all. No CVO limb is reachable on any of them
until a tree home and rows exist. Reported to the three owners in one message (19453/19454/19455).

---

## WORK DONE

### Startup (org/XXX.md Step 1b A-F)
```
A    register_agent 3.0.0_SA_CVO~Z -> PID 17748, broker port 7800
A.1  org/mcp/sessions/4a8d6b66-a375-4a1d-a626-29866a4a0e70.serial written
A.2  audit-archive-invoker: 19 findings. 18 device-axis (every NON-APPEND-EDIT a shrink,
     every ERROR-FAILCLOSED a laptop-only log). ONE NEW CLASS surfaced, not chased:
     [COVERAGE/UNCOVERED-AUDIT-LOG] org/commit-msg-ascii-override-audit.log (the LD-0500 gate's log).
A.3  104 of 104 comp-tools resolve bare; EXERCISE: a forwarder RAN.
B.0  get_delivery_state since 2026-09-01T21:00Z: 30 rows -> READ 30/30 (then 19442, 19445, 19448
     as they arrived: 33 total, every one opened before its ack).
B    check-inbox top-level empty (the stream Monitor had mv'd all 28 to read/); broker probe agreed.
B.1  to-check --all --assignee: total=0, scanned=2241, unresolved_serials=0 (an honest zero).
C    /watcher: Monitor bx3jzj8dj, arm banner parent-tied pid 594124. No orphan found (ps rc=1,
     serial NOT REGISTERED before the arm -> genuine fresh session, no kill needed).
D    owned-paths hook already wired.   E   .comp-graph/.agent_context SERIAL=3.0.0_SA_CVO~Z.
F    CronList: none. LD-0318 fork: NFRA_SYSPARITY.json reads status active AGAIN (it read closed
     with closed: 2026-08-25 on 09-01) -- the fork is live; default-if-silent stands: armed NOTHING,
     row left unstruck and unannotated.
L8   surprise-watch.sh stream armed as Monitor bhhfpxz1u (read-only watermark; no banner in its
     output file at 06:50Z; TaskOutput reads running).
```

### LD-0319 first responsibility: DRIFTED
PRIMARY instrument `python infra/system/system_parity.py` (the fallback `comp-system --check` was
run FIRST by mistake -- rc=2 STALE -- then the primary; the instrument order error is recorded below).
```
eng-currentstate-current      FAIL  06 STALE: ledger_union_count 101->99 (4 spans), tools_index_count 80->78 (2 spans)
ont-rulebank-version-current  FAIL  head 1.8; 'rule-bank v1.8' in NONE of 4 required files; 7 of 7 assertion sites stale
                                    (the 09-01 finding that this check counts SDK fixtures + its own negative
                                    control as representation sites -- msgs 18386/18387 -- still has no disposition)
20 of 22 checks PASS; the pass rate is a check-pass rate, not parity.
```
06 is NEVER regenerated from this device (comp-kuzu queries time out here; a site-Z regen writes
unknown-vintage rows into the laptop-maintained 06). Surfaced to `0.0.0_AB_MSTR~Z` in 19455.

### /canonical-flow -- three reports (Step 5 form in msg 19453/19454/19455; condensed here)
```
CODE                     home       placement  TOs open/term  proof instances        surprises   rows  dep_stage  MEASURED limb (tree grammar)
OPAL_TICKET_VNEXT (D7)   flat only  SITEZ      0 / 0          n/a                    0           0     REGISTERED none conforming: brief shape not admitted,
                                                                                                                  no endpoint, PRD @c2837692bc lacks header/
                                                                                                                  endpoint/manifest; decomp @e9ca70c307 exists
                                                                                                                  AHEAD of L2
PLATFORM_OPS_USERMGMT    flat only  SITEZ      0 / 6          6 of 6 VALID (announce) 25 (0 ids) 0     EXECUTING  legacy L7 DONE, L8 input ABSENT; tree: not past L3
D12_PHONE_OTP_ALL_AWS    flat only  SITEZ      1 / 1          SB INVALID rc=1 (5 viol) 7 (0 ids)  0     EXECUTING  legacy L7 in flight; tree: not past L3
```
Classes:
- OPAL_TICKET_VNEXT: PRE-TREE (blocking) + ARTIFACT-GAP at L2 + SEQUENCED-BEHIND with TWO carriers
  pointing different ways (DIRECTIVES.yaml D7 stance: Andrew-direct 2026-08-25 "effectively on hold";
  Andrew-direct 2026-09-03 06:3xZ/06:4xZ names it second in the fabric sequence). Not adjudicated.
- PLATFORM_OPS_USERMGMT: PRE-TREE + OPEN-ROUND + ARTIFACT-GAP at L7 (25 surprises announced inside
  proof instances DE1 7 / DE2 2 / DE3 3 / W1 5 / W2 4 / W3 4, none a row; the six TOs and instances
  are keyed to the token D12_PLATFORM_OPS, which is NOT a register code). Claimed EXECUTING with
  zero open TOs -> stale row.
- D12_PHONE_OTP_ALL_AWS: PRE-TREE + DEAD-SEAT (SF-SITEZ open, 0.4.0_DE_ClientPlatform~Z ABSENT) +
  ARTIFACT-GAP at L7 (SB instance @636d1b5119 INVALID at HEAD: no decomp_ref object; auth.ts +
  mfa.ts at pin 8fd0ae2810 and db.ts at pin 775dc28917 LACK the tokens their rows say they
  introduce; deployed CodeSha256 in commit_or_etag) + SEQUENCED-BEHIND on SF-1 only (SP-1 at Andrew).
  This seat's predecessor certified E1-E8 on 09-01; the validator's content rung may postdate that.
  Measured now: INVALID. Not re-certified from here.
- CROSS-CUTTING L3 bar: PROJECT_TREE.contract.json 0.1.1 level[2] regex ^[A-Z]{4}_[A-Z0-9]{4,12}$
  refuses ALL THREE codes (re.match measured); MACROS.yaml carries NO D7 entry (R2 refuses any D7
  tree entry until Andrew ratifies a macro); D12's ratified enum is [NFRA] only.
Role: next limb L2/L3 on every one -> 1.0.0_SA_CTO~Z. No CVO act. D12 is not in Andrew's 06:4xZ
sequence (NFRA_OPSEC202609 -> OPAL_TICKET_VNEXT -> ASSETCLASS_TAXONOMY -> D1_CATVIEWS research).

### Classing owed from 19347
The 2 residual never-rules-gate arms (`git -c pull.rebase=true pull origin CLOUD` and its
`--no-pager` form pass GATE 1 on every device): {OBSERVATION, ARMED}, disarm_owner `1.0.0_SA_CTO`
(gate surface; F-XXX option-consumer work). A fabric gate, not a project -- no channel home; this log
is the carrier. The SITEZ pair from 19296/19306 is DISARMED by CALL 2 on origin @98fd4ca0d4 (19353).

CORRECTION 07:0xZ (msg 19461 from `0.0.0_AB_MSTR~Z`, relaying the laptop `0.0.0_AB_MSTR` bus frame
1347cb9e): the count "2" above is NOT this seat's measurement. It is the 2026-09-02 SITEZ reading
(`1.0.0_SA_CTO~Z` 19347 and `0.0.0_AB_MSTR~Z` 19353, 94 PASS / 2 FAIL), relayed here and in 19455
WITHOUT its qualifier -- who ran it, on which device. The laptop reads 92 PASS / 4 FAIL on the SAME
hook bytes (origin/CLOUD 3bd8d2ef04 = SITEZ after the 06:5xZ merge): `git -C portal rebase`, the
`-c pull.rebase` one-shot, `-C and -c combined`, `generic flag before -c`, all PASS where DENY is
wanted. The suite's totals were already measured to depend on RUNNER IDENTITY (26221d9c2e), so the
runner is the first candidate for 2-vs-4 before a device difference is inferred. This seat did not
run the suite and does not now: the classing {OBSERVATION, ARMED, disarm_owner `1.0.0_SA_CTO`} is
unchanged by either count, and resolving the count is the disarm owner's. Self-correction: a relayed
measurement lost its qualifier on the way into a CVO record, the banked class, third instance.

### Channel denominators at intake (bare comp-surprise, 06:44Z)
200 items / 17 projects / 20 files; OPEN 66, ARMED 87, GRADUATED 121, DISMISSED 11; 1 remediation
row. Zero items under any D7 or D12 code.

### L8 intake, first notifier event (07:03Z): D1_CATVIEWS +1 row (17)
`D1_CATVIEWS-Z-S4`, surfaced_by `2.0.0_SA_COO~Z` 07:03Z, OBSERVATION / INERT / UNDER_INVESTIGATION,
no `adjudicates`: the DISARM RECORD for `D1_CATVIEWS-S11` (TO-I1-DS's committed proof instance
re-measures INVALID rc=1 at HEAD b80b692a1d). Read here as intake. The row was UNCOMMITTED in the
shared worktree at the read (file ` M`, last commit 9437945112 2026-08-29). CORRECTION 07:0xZ: the
draft I first read said the TO face was annotated "in the same commit"; the notifier then reported
the row MUTATED in place (c5ae1571f267 -> 8b36bcd7777f) and the re-read row says that face edit was
REFUSED at commit by `.tools/to-pipeline-gate.py` layer 2 (the gate keys on a staged `<status>` line
reading `complete` and cannot tell an issuer annotation from a flip -- COO~Z's own observation, in
its row). An edit to an UNCOMMITTED draft is not an append-only violation; the notifier's watermark
reads the worktree and was right to say so. Quoting a draft is what made this line need a correction. L9 on S11 is deliberately NOT taken: D1_CATVIEWS is SEQUENCED-BEHIND (fourth in Andrew's
06:4xZ sequence) and its round is not open; S11 stays UNDER_INVESTIGATION until that round's CVO row.
The row's transferable half is worth carrying: a `disarm_owner` named on a row does not travel with a
session, and nothing in B.0 or the inbox surfaces it -- the `/canonical-flow --report-only` pass did.

---

## COMPILER TOOLS

| Tool | Runs | Result | Note |
|---|---|---|---|
| `python infra/system/system_parity.py` | 1 | DRIFTED 20/22 | LD-0319 PRIMARY; two FAILs named above |
| `comp-system --check` | 1 | STALE rc=2 | the FALLBACK, run before the primary by mistake (see self-corrections) |
| `comp-read --enumerate` | 3 | PASS | 0 hits with printed denominators (194 / 313 / 123 lines) on the three PRD-class docs; the zero is a measured absence |
| `comp-find --name` | 2 | PASS | 7 D12 proof instances located on --all (94 hits / 52,774 files scanned); page 1 of the proof census was NOT the answer |
| `comp-surprise` | 4 | PASS | 3 scoped (0 items each) + 1 bare (200 items / 66 open / 87 armed) |
| `.tools/to-check.py --all` | 4 | PASS | assignee 0; project scopes 0 / 0 / 1 active; scanned 2241 each |
| `.tools/to-liveness-join.py` | 1 | PASS | reports 8 zombies fabric-wide; DE~Z / AE~Z / OpalETL~Z ABSENT |
| `.tools/proof-of-spec-check.py` | 7 | 6 VALID / 1 INVALID | ANNOUNCE mode on flat TOs; SB instance rc=1 with 5 violations |
| `.tools/audit-archive-invoker.py` | 1 | 19 findings | 18 device-axis + 1 new UNCOVERED-AUDIT-LOG |

**What worked.** `comp-read --enumerate`'s printed denominator made three zeros claimable as absence.
`proof-of-spec-check.py`'s ANNOUNCE mode exposed the 32 unrowed surprises that no register field
mentions. `get_delivery_state` with a WIDE `since` surfaced the 28-row backlog the default page hides.

**What failed.** The comp-tool HUD refused one Bash call because a Python helper was named `find(`
(a token match, not a search) -- renamed and re-run; no rail bypass used. `proof-of-spec-check.py
--help` is not an option (it reads `--help` as a path, rc=2) -- invoked positionally.

**Gap found.** None new in the tools. The `ont-rulebank-version-current` defect (09-01) stands undispositioned.

---

## SELF-CORRECTIONS

1. Ran the LD-0319 FALLBACK (`comp-system --check`) before establishing the PRIMARY was unavailable.
   The primary was available and was then run. The banked rule was in memory and was not applied on
   the first pass; the verdict did not change, the instrument order was wrong.
2. Read the `--assignee` to-check census through `tail -40` on the first pass (a truncated census);
   re-captured to a file and read the RESULT line. The first read's conclusion (0 TOs) survived, by luck.

---

## BLOCKERS

```
NONE that block another seat.
```
Commit of this log was HELD by the merge window 0.0.0_AB_MSTR~Z opened at 06:5xZ (19448) and
released by the CLOSE frame 19458 (06:56Z; origin/SITEZ b80b692a1d, no MERGE_HEAD measured before
the commit). Law delivered in that window and read here: the XXX.md MSTR-row /govern arm (hourly
:17, scoped to the four-project sequence; these sessions end at the current project's L10 close)
and the comp-tool-hud CENSUS-FILTERED deny class (no piping comp-* into grep/head/tail/sed/awk/wc
without ENUMERATE/DENOMINATOR or a rail marker).

---

## CURRENT STATE (for a reader with zero prior context)

Site Z relaunched 06:30Z on Andrew's word with three Tier-1 seats. Andrew's sequence for this fabric
(19442, verbatim at 0.0.0_AB_MSTR~Z's record): NFRA_OPSEC202609 (renamed from NFRA_SECURITY202609 at
06:5xZ, 19445; 1.0.0_SA_CTO~Z is doing its L3/L4 now) -> OPAL_TICKET_VNEXT -> ASSETCLASS_TAXONOMY ->
D1_CATVIEWS research, every one through /canonical-flow; `/govern` granted to 0.0.0_AB_MSTR~Z, which
kills and re-instantiates the work group at each project's L10 close. This seat's engagement begins
at L8 when NFRA_OPSEC202609's L7 workers file investigation rows; nothing before that.

Monitors: inbox bx3jzj8dj; surprise notifier bhhfpxz1u. Zero crons. Push state of this log: LOCAL
(integrator pushes, LD-0367).

---

## NEXT STEPS

- [`3.0.0_SA_CVO~Z`] commit this log after the CLOSE frame; then L8 on NFRA_OPSEC202609's rows as
  they arrive on the notifier; L9 dispositions; the one L10 slug when every TO is terminal with a
  valid instance.
- [`1.0.0_SA_CTO~Z`] the L3 forks with Andrew for OPAL_TICKET_VNEXT (code regex + no D7 macro) before
  its turn in the sequence; the D12 codes when D12 re-enters.
- [`2.0.0_SA_COO~Z`] when D12 re-enters: the DE~Z dead seat on SF-SITEZ, the SB instance re-grounding,
  and a closing-pass TO for the 32 unrowed D12 surprises.
- [`0.0.0_AB_MSTR~Z`] LD-0319 relay to the laptop integrator (06 regen is a laptop act); the
  D12_PLATFORM_OPS ghost token in the D12 TOs; the uncovered LD-0500 audit log for the manifest owner.
- [`3.0.0_SA_CVO` base] D1_CATVIEWS-S5 (org/surprise_channel/D1_CATVIEWS/INVESTIGATION_v1.md:171)
  reads ARMED 10 d on; its own disarm_owner text records the DISARM as done and the schema cannot
  express DISARMED -- that inexpressibility IS the item. The open REMEDIATION (a Rule-24 record per
  axis) is the base seat's; D1_CATVIEWS is fourth in the 06:4xZ sequence. Read here, not acted on.

-- 3.0.0_SA_CVO
