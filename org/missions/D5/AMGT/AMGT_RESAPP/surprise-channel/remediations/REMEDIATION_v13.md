# AMGT_RESAPP round 13: remediation slug

**To:** `1.0.0_SA_CTO~Z` only. **From:** `3.0.0_SA_CVO~Z`. One L10 handoff, every artifact LOCAL on SITEZ. The
adjudication is `adjudications/ADJUDICATION_v13.md`. Written 2026-09-18T17:45Z.

**Result.**
- **Orders.** All 97 orders are terminal. Round 13's fifteen read 26 PASS and 3 FAIL, and all three FAILs are
  criterion defects.
- **Thesis chart.** BA_US_Equity's chart serves three verified filing points with spans (FWD-18).
- **Lead Panel.** Price serves 2026-09-15.
- **Print.** Print serves all 33 names on the page's request shape.
- **Model tab.** It carries three scores, each classed ABSENT with its own cause.
- **Blocked.** Nothing in round 13 could be captured through the real edge, because MFA gates the automation logins.

## Next cut: obligations, most consequential first

1. **Peers V (S162, `1.0.0_SA_CTO~Z`).**
   - The measure is Andrew's to define, and he reserved it by name.
   - Peer identity is the binding constraint: 224 of 1,658 peer rows are numeric SEDOL stems the resolver skips.
   - peers_v's empty absent_reason needs no new data.
   - No round-14 scores cell before his answer.
2. **One issuer per round (S154, `1.0.0_SA_CTO~Z`).** Round 13 was issued twice by two continuations of one seat.
   A gate keyed to the round, not the serial, is the only check that sees it.
3. **Acceptance at L10 (S169, ARMED).** The census counts an order terminal on a VALID instance whatever its
   verdicts. Every close needs a per-criterion sweep over every order until a gate reads acceptance.
4. **MFA and the capture (W31-S3, Andrew's decision via `1.0.0_SA_CTO~Z`).** A headed session where a person
   enters the code, or an exemption only he can grant. Until then, W27-S10 and the page judgments stay unmeasured.
5. **The slash in security keys.**
   - Routing (W27-S10, ARMED): make `handler()` indifferent to encoded versus literal.
   - The producers (W32-S3): the posture key depth and `batch.py:81-84`.
6. **The drafting/v1 population.** The other 11 objects still carry the pre-verification shape; rebuilding them is a
   population act under its own pair (W27-S3's remedy text).
7. **Management content (W32-S2, `2.0.0_SA_COO~Z`).** 7 of 33 keyed names carry officers. Five rosters are served
   SERVED while empty. The CARD 5 enrichment reached none of the added names.
8. **Tooling and process (all OPEN).**
   - W31-S1: the empty portal gitlink.
   - W31-S2: the npx/bun decoy.
   - W32-S4: the cache defaulting into a worker folder.
   - W34-S1: the Terraform plan blocked by a gitignored artifact.
   - W34-S2: the lane gate versus co-signed direct acts.
   - S153: orders issued without a `<status>` element.

## Remediated in-round (closed)

S155, S159, W27-S3 (for BA), S149, S168, W27-S11 and W33-S1 -- plus W23-S5, S137, S141 and S139 from round 12,
advanced in REMEDIATION_v12.

## Two process findings with no item id

- **Per-act verification ran on timing luck.** Acts landing 15-20 minutes apart outran a 30-minute signer tick, so
  rk-25's own build was never measured.
- **Uncommitted artifacts failed four ways in one evening.** A completion marker suppressed terminality; a row was
  discarded by a peer's commit; two rows deadlocked each other's commits; and a filtered view made a refusal look like
  success. The one remedy: commit within seconds, and verify by HEAD moving.

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-S154",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED: round 13 was issued TWICE by two continuations of ONE seat identity -- f0cbb2d813 then the re-cut 7acf65b08b -- and each spawned its own workers, so four cells were written in two generations. ONE ISSUER PER ROUND held by no mechanism when both issuers carry the same serial.",
    "evidence": [
      "Z-S154 (2.0.0_SA_COO~Z, first-hand): the first continuation adopted an uncommitted, unattributed draft of the 15 orders, cut f0cbb2d813 and spawned five workers from da2c3c479a before learning a second continuation had re-cut the round (62e9cfbf60 / 7acf65b08b) and spawned seven more.",
      "Z-S152 @2f3840fc21 (this seat): at 14:45Z, 14:54Z and 15:08Z the live edits sat in worktrees based at da2c3c479a, which does not carry the re-cut; chain CK was written in both generations.",
      "Measured cost: rk-19 producer, rk-21 and rk-28 each drained ONE generation and left the other on an unmerged branch (0f297b6ba6 second parent 7aef98df54; 339473fab4; e56b59fa22 second parent c9816ba669). chain SP wrote two key shapes (Z-S155). BA_US_Equity analysis object written four times 14:57Z-16:02Z with thesis_driver points 3,1,1,3 (msg 23547)."
    ],
    "remedy": "Make a second L6 issuance into a round that already has one REFUSE at the gate, keyed to the round and not to the issuing serial -- two continuations of one seat carry the same serial, so a serial-keyed check cannot see this collision. Name the resolution for the case where it happens anyway: the later cut is canonical only by an explicit ruling row, as S156 did here after the fact.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S153",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED: all fifteen round-13 orders were issued with NO <status> element, while every worker face tells the worker to flip it at close -- so each worker had to invent the line, and one uncommitted invented line hid a finished order from the record for twelve hours.",
    "evidence": [
      "Z-S153 (4.0.0_SA_CRO~Z): to-check.py listed all 15 with status ??; round-12 orders carried a tag from their adding commit (rk-9 @2726497094).",
      "rk-24 batch-unresolved-objects: the working tree carried <status>complete</status> while HEAD carried no tag; _proof_terminal refused with \"in the worktree differs from HEAD -- the checker would grade the worktree\"; committed @bee2b0a0dd after this seat census (msg 23626)."
    ],
    "remedy": "Issue every order with a record-face <status> element in its adding commit, and add the check to the limb that already grades newly added orders.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S155",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, REMEDIATED and DISARMED: chain SP wrote scores/v1/ in two key shapes from two generations. Ruled -- the date-partitioned shape is canonical -- and the served read now resolves that shape and only that shape.",
    "evidence": [
      "S156 adopted S155 own recommendation: scores/v1/<security_key>/<as_of_date>.json is canonical, the flat set a superseded artifact left in place.",
      "Measured at this seat 18:0xZ: 66 objects under scores/, all written 2026-09-17 14:43:27Z-16:10:08Z, ZERO before that day; 31 flat and 33 date-partitioned counting the two slash keys; a sampled date-partitioned key has one version (msg 23559).",
      "Z-S172: the served read returns scores_status SERVED, read_completed true, object_key scores/v1/BA_US_Equity/2026-09-17.json -- the date-partitioned key."
    ],
    "remedy": "Executed in-round: the date-partitioned shape ruled canonical (S156) and read on the served plane (Z-S172).",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-18T00:35Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S159",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED and REMEDIATED: the rk-19 adapter deploy moved served output with the COO half of its never-widen pair carried only as a session dispatch; the half is now a committed file, and the rollback it names was reconstructed after the act.",
    "evidence": [
      "Z-S159 @8597de9671 (this seat): at filing the ledger held 11 never-widen files -- five complete pairs for rounds 10-12 and, for round 13, the CTO half alone (@e3fc4495cf).",
      "NEVER_WIDEN_ROUND13_RK19_ADAPTER_SECOND_JOIN_COO_HALF.md committed @0fdf4feb87, verified an ancestor of HEAD here; the ledger then held 12 files, six complete pairs.",
      "The file states the rollback VersionId (Ocz1IJKMxPe.KAEGqllNw7feYn9FTg.k) was NOT named in the original dispatch and was fixed afterwards by matching CodeSize against the pre-act read."
    ],
    "remedy": "Executed in-round @0fdf4feb87. Standing rule for the next cut: a half is a committed file before the act, and it names the rollback artifact version, not only a code hash.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W27-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED and REMEDIATED for BA_US_Equity: the producer fix corrected the analysis object but the adapter reads a SEPARATE drafting/v1 cache written once; that cache was rebuilt under its own pair and the chart now serves three verified points.",
    "evidence": [
      "STOP 6 pair: CTO half @a9c6cc924c, COO half @75d97c813e; drained cfd72b4122. Exactly one key moved (12 keys under drafting/v1/, only BA_US_Equity.json after 22:00Z).",
      "Served read at this seat, direct invoke built from the adapter own route table, 22:38:17Z: thesis_driver_chart SERVED, source filing, points_count 3, held_uncited 0, 2023=528 P0278, 2024=348 P0277, 2025=600 P0276, adapter zuWM8IZziIL4 unchanged."
    ],
    "remedy": "Executed in-round for BA_US_Equity (STOP 6, cfd72b4122). Next cut: rebuild the other 11 drafting/v1 objects as a population act under its own pair.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S149",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED and REMEDIATED: rk-5 tab scores reached no served surface. Round 13 wired them -- the producer writes them, the adapter carries a scores key on 33 of 33 names, the page renders it, and the read completes after the grant.",
    "evidence": [
      "rk-30 producer, adapter and page halves: every criterion PASS except adapter AC1 (C-S307).",
      "Z-S172: scores_status SERVED, read_completed true on the date-partitioned key, CodeSha256 0l7f4YGikexr unchanged by the grant."
    ],
    "remedy": "Executed in-round by the rk-30 chain and the scores/v1/ grant.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S162",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, DISARMED: Peers V serves ABSENT on 33 of 33. The first reading (vocabulary mismatch, S162) was ruled, then corrected: with vendor egress authorized the measure computes for 30 of 34 names as written, and the binding constraint is PEER IDENTITY -- 224 of 1,658 landed peer rows carry a numeric SEDOL stem the resolver skips.",
    "evidence": [
      "S164 (1.0.0_SA_CTO~Z) ruled round 13 ships the honest-ABSENT state; S174 withdrew its operative reading after 4.0.0_SA_CRO~Z egress brief @e12ed54a9f measured 30 of 34 with the measure as written.",
      "Andrew-direct ~12:5xZ, recorded @c6c49ede58: \"we will always be able to find peers, I will answer that once ive better seen the shape of the data.\" The measure definition is his, reserved by name.",
      "Served read at this seat after the grant: robustness absent_reason \"n=1 of 6 measured (constraints [2, 5]), below the n>=5 eligibility floor\"; divergence absent_reason \"FWD-20 house FCF forecast has not been built yet\"; peers_v absent_reason None."
    ],
    "remedy": "Three parts, in order of what they wait on: (1) peers_v emits a real absent_reason like its siblings -- no new data, owner at the next cut; (2) resolve peer identity for the 224 numeric SEDOL-stem rows so the measure reaches the population; (3) Andrew answers what Peers V means where a peer set is short (reserved to him, @c6c49ede58). No round-14 scores cell before (3).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-18T00:12Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S168",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, REMEDIATED and DISARMED: the adapter role had no grant on scores/v1/ on either limb, so every scores read failed with AccessDenied. The grant was added under its own pair and verified per limb.",
    "evidence": [
      "S168: 33 of 33 read scores_status READ_FAILED with the full AccessDenied text -- the half disclosure clause is what made it visible.",
      "Z-S172: thirteen entries in each limb, the added values exactly arn:aws:s3:::opal-data-harvest/scores/v1/* and scores/v1/*, the other twelve byte-identical with an empty lost set; iam:SimulatePrincipalPolicy allows the two added reads, denies four negative reads and denies PutObject and DeleteObject on scores/v1/. Pair CTO @a9fb5caa70, COO @8db1cd0a76; drained cefd5e6ae5."
    ],
    "remedy": "Executed in-round: the scores/v1/ read grant, both limbs, trailing-slash form, cefd5e6ae5.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-18T02:59Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W27-S11",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, REMEDIATED and DISARMED: the adapter role had no grant on scores/v1/ on either limb, so every scores read failed with AccessDenied. The grant was added under its own pair and verified per limb.",
    "evidence": [
      "S168: 33 of 33 read scores_status READ_FAILED with the full AccessDenied text -- the half disclosure clause is what made it visible.",
      "Z-S172: thirteen entries in each limb, the added values exactly arn:aws:s3:::opal-data-harvest/scores/v1/* and scores/v1/*, the other twelve byte-identical with an empty lost set; iam:SimulatePrincipalPolicy allows the two added reads, denies four negative reads and denies PutObject and DeleteObject on scores/v1/. Pair CTO @a9fb5caa70, COO @8db1cd0a76; drained cefd5e6ae5."
    ],
    "remedy": "Executed in-round: the scores/v1/ read grant, both limbs, trailing-slash form, cefd5e6ae5.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-18T02:59Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-S169",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, ARMED: the open-order census counts an order TERMINAL on a VALID proof instance whatever its criteria say, and the L10 precondition is read off that census. VALID names well-formedness, not passing.",
    "evidence": [
      "S169 (1.0.0_SA_CTO~Z): rk-30 page half recorded AC2 FAIL, proof-of-spec-check returned VALID rc=0, and the census removed it from the open set.",
      "Z-S170 @f8af42864c (this seat): at 02:3xZ SEVEN of seven orders in the terminal-by-instance bucket carried a FAIL (9 PASS, 7 FAIL of 16 criteria).",
      "ROUND 13 AT CLOSE, every one of its 15 orders read per criterion in THREE classes: 26 PASS, 3 FAIL, 0 UNVERIFIABLE-BY-INSTRUMENT; rk-26 withdrawn with no instance. Census 0 open of 97."
    ],
    "remedy": "Make the L10 precondition read acceptance, not only terminality: a per-criterion sweep over every order of the round, in the three classes, with its denominator printed. Until a gate does, every close carries that sweep by hand.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T02:57Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W27-S10",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, ARMED -- dispositioned WITHOUT its discriminating instrument: whether the gateway forwards %2F encoded (the page works) or normalises it to a literal slash (two names 404 at the router) is still unmeasured, and every instrument that could see it is closed.",
    "evidence": [
      "Direct invoke: encoded 200 for both names, literal 404 -- it builds rawPath itself, so it certifies its own assumption.",
      "Direct HTTPS to the gateway: 401 on all four calls, the no-slash positive control and the no-header negative control included -- never reached the adapter (msg 23610).",
      "Authorizer logs: zero events 00:00Z-00:30Z against 51 in a control window, IdentitySource Authorization, and it logs \"path: undefined\" when it does run (msg 23616). Adapter logs: zero path events in 36 hours with a live positive control. Gateway access logging is not configured.",
      "The one surviving instrument, a browser-network capture through the real edge (rk-26), was withdrawn by its issuer on Andrew word @5dc9089ca7 after MFA blocked the automation login (W31-S3)."
    ],
    "remedy": "Remove the dependency: make handler() route a security_key the same way whether its slash arrives encoded or literal, so gateway normalisation stops mattering. Failing that, an authenticated capture through the real edge settles it -- that path runs through Andrew MFA decision (W31-S3).",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-19T09:20Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W32-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED, OPEN: the same slash in two producers -- the posture store writes the two names one level deeper than every other name, and the management batch census splits security keys on \"/\" so those two names can never be built.",
    "evidence": [
      "W32-S3: posture/v1/BP/_LN_Equity/... instead of posture/v1/BP_LN_Equity/...; a consumer splitting on the first \"/\" reads BP and NG and undercounts by two.",
      "1.0.0_SA_CTO~Z @0cdd86b29d, verified at source: batch.py:81-84 splits on \"/\", and the same census counts placeholder filings as real, so one enable would write about 176 zero-officer rosters served as SERVED."
    ],
    "remedy": "Census every site that splits or nests on \"/\" inside a security key (posture writer, management batch census at batch.py:81-84, served_names) and fix them in one pass; stop the census counting placeholder filings as real before any enable.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W31-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, DISARMED: a linked worktree carries an EMPTY portal/ gitlink -- no .gitmodules URL and no supported mechanism populates it -- so no portal-touching worker can run in its own worktree.",
    "evidence": [
      "W31-S1: 0 files under portal/ in the assigned worktree; the worker stopped rather than reconstruct the tree.",
      "Disarmed by its owner (S166): the page halves were completed and re-run against the main tree portal (5b767811e7, 9074091db1)."
    ],
    "remedy": "Either create portal-cell worktrees with portal/ checked out at the gitlink commit, or rule that portal cells run in the main tree -- and say which in the issuance.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-18T00:35Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W31-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, ARMED: on this device `npx tsc -b` in the bun-managed portal fetches and runs a registry package named tsc that compiles nothing and exits clean, so any criterion written that way cannot see a type error.",
    "evidence": [
      "W31-S2: the literal invocation printed the decoy banner, rc 0; ./node_modules/.bin/tsc.exe -b ran the real compiler, rc 0, no output.",
      "The remedy is already banked estate memory (msg 23636): bun install writes no npm shims, so invoke the local binary by path. Both round-13 criteria were re-cut that way (5b767811e7, 9074091db1) and now PASS."
    ],
    "remedy": "Invoke the local compiler by path in every portal typecheck criterion, and make the portal refuse npx for its own binaries (packageManager pin or a committed lockfile npm trusts).",
    "owner": "0.4.0_DT_ClientPlatform",
    "round": "v13",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "0.4.0_DT_ClientPlatform",
      "round": "v13",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~348/DISPOSITION_LEDGER.json@4c3f3fcb2e: the ARMED hazard has no live instance: no open order's criterion uses npx for a portal binary, portal/package.json pins packageManager bun and a typecheck script, and the ARMED owner 0.4.0_DT_ClientPlatform holds no order in this project; a new instance would be a new row"
      }
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "0.4.0_DT_ClientPlatform",
      "at": "2026-10-09T20:19:00Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W31-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, ARMED: mandatory MFA, which Andrew required for all users on 2026-09-02, now gates the documented automation logins, so no headless capture can authenticate. rk-26 was withdrawn on his word, and with it round 13 only judgment criteria and W27-S10 only oracle.",
    "evidence": [
      "W31-S3: the D12_PHONE_OTP_ALL_AWS challenge intercepts both documented logins before any token is issued; the worker did NOT read the MFA store or any signing secret to recover a code.",
      "rk-26 withdrawn @5dc9089ca7 (Andrew-direct \"write off the frontend TO\"); census 0 open of 97.",
      "Judgment grades: rk-26 AC2 and AC3 are NOT graded -- the order has no proof instance, and the grade carrier requires one. Round 12 rk-2 AC6 and rk-8 AC4 stay NOT_EVALUATED as graded in ADJUDICATION_v12, with the missing instrument now named: an authenticated browser-network capture through the real edge."
    ],
    "remedy": "Andrew decides how, if at all, an authenticated capture is made: a human completes the one-time code in a HEADED session and the harness drives after it (MFA stays on for everyone), or an MFA-exempt automation identity (an exemption only he can grant). Separately, update the frontend-dev auth README and every constitution that still names these logins as working.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-18T17:58Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W32-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED, OPEN: the vendor call Andrew authorized at CARD 5 enriched NONE of the seven names rk-22 added, because domains.json lists only the original five QA names -- and the management figure \"12 of 12\" is a STATUS count: 7 of the 12 rosters carry officers.",
    "evidence": [
      "W32-S2: every added name lusha_enrichment.status SKIPPED; ceo_public_profile never queried.",
      "rk-22 criteria read at HEAD: AC1 expects the counts to rise toward the ceiling with every non-measured name carrying a reason; AC2 a two-value classification. Neither tests enrichment, and the order never names the vendor service or domains.json -- so AC1 and AC2 PASS stand on their text (working record @c8c3ec7f37).",
      "Exec Management first read, 4.0.0_SA_CRO~Z msg 23697 re-measured by 1.0.0_SA_CTO~Z @0cdd86b29d: 12 rosters SERVED by status, 7 with officers (62), 5 with zero officers under UNRESOLVED-SOURCE -- 7 of 33 keyed names carry officers."
    ],
    "remedy": "Make the enrichment domain list follow the management population (or say in the order that it does not); and serve a roster with zero officers as ABSENT with its class, not SERVED. State content counts beside status counts in every report.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W32-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GRADUATED, OPEN: a shared library cache defaults into a NUMBERED WORKER deliverables folder, so running the posture producer rewrites a tracked file in another worker record.",
    "evidence": [
      "W32-S4: lib/research/peers/universe.py load_candidate_universe() rebuilt deliverables/0.9.0_WK_AMGT_RESAPP~21/candidate_universe.json; the worker left the diff uncommitted rather than write outside its grant.",
      "Read here: that path is clean against HEAD in the shared tree -- the diff stayed in the worker worktree and did not come across at the drain."
    ],
    "remedy": "Move CACHE_DIR_DEFAULT out of any worker-numbered deliverables folder to a durable, non-tracked cache home.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W33-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, REMEDIATED and DISARMED: 59 of 237 unresolved names carry security_key null, and the new writer would have collapsed them onto one colliding key. The issuer ruled skip-and-count; a real run wrote 178 of 178 distinct objects with 0 collisions.",
    "evidence": [
      "W33-S1: filings/v1/None/UNRESOLVED-SOURCE.source.json would have been written 59 times.",
      "ISSUER AMENDMENT 1 @837e7b1007 skips a falsy security_key and counts it; drained db6c40083f; rk-24 producer AC1-AC3 PASS (237 = 59 + 178; 178 of 178 found, objects_missing empty)."
    ],
    "remedy": "Executed in-round by ISSUER AMENDMENT 1 (837e7b1007). The 59 unkeyed names ride S117.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-17T18:50Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W34-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, ARMED: no Terraform plan can run in a fresh worktree of infra/aws/terraform/harvest, targeted or not, because an unrelated resource reads a gitignored, never-committed build artifact at plan time.",
    "evidence": [
      "W34-S1: chatter-axis-schedule.tf:124 filebase64sha256() reads .build/chatter-axis-producer.zip; -target does not prune the evaluation; the worker used a disposable, never-committed placeholder."
    ],
    "remedy": "Either commit the build step that produces the artifact into the plan path, or make the expression tolerate its absence so an unrelated resource cannot block a targeted plan.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-19T02:28Z"
    }
  },
  {
    "id": "AMGT_RESAPP-Z-W34-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GRADUATED, OPEN, ARMED: a co-signed direct act on an infra path cannot satisfy the owned-paths lane gate, which reads grants only from task-order files -- so every such act needs the audited author override.",
    "evidence": [
      "W34-S2: owned-paths-validate refused the worker commit of scoped-amgt-api.tf, the one file the act existed to change.",
      "The Terraform source landed under GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL @3c2a6e47ca; 1.0.0_SA_CTO~Z endorsed the escape as correct for this case (msg 23649)."
    ],
    "remedy": "Either mint a task order for every co-signed direct act, or teach the lane gate to read a signed pair as a grant for the paths it names.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v13",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v13"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Z",
      "at": "2026-09-19T02:15Z"
    }
  }
]
```

-- 3.0.0_SA_CVO
