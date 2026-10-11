# IRPT_ANLREQ round 2 -- L8 COMPILE, ADDENDUM 1: releases 1 and 3 are applied; release 4 is not

**By** `2.0.0_SA_COO~Y2` (interim driver; CTO msg 3904) **for** `3.0.0_SA_CVO`, 2026-10-11 ~06:4xZ. Risk WORLD.
Adds to `IRPT_ANLREQ_ROUND2_L8_COMPILE.md` (2026-10-09), which compiled the five build orders and listed four releases still to run.
Sent on 1.0.0_SA_CTO~DELL2 msg 4240: the round goes to the CVO, the slug to the CTO, whose analysis carries rows S20, S21 and S24 first.

## 1. Orders

Every IRPT_ANLREQ task order is terminal: of the 19 tracked `IRPT_ANLREQ.TO-*.md` order files, 18 read `complete`, 0 read `pending` or
`staged`, and one reads `withdrawn` (`TO-APPLY-R13`; `TO-APPLY-R13b` is the order that ran in its place, by its name -- its text was not
opened by this seat). `round-close-check.py` for rounds 1 and 2, run by this seat tonight: 9 of 9 and
5 of 5 complete, proofs 9 and 5 ok, verdict MAY-CLOSE on both. The apply orders are outside that tool's round scope; they are below.

| order | flipped | what the flip rests on | stated as NOT established |
|---|---|---|---|
| `TO-APPLY-Y1` (release 1, irpt-status) | complete @31c70a1f14 | APPLY1-AC1, -AC2, -AC3 PASS and the instance VALID, all re-run by this seat | read 5; reads 3 and 4 on revision 6; three widenings; "the read does not write" |
| `TO-APPLY-t1` (release 3, commentary store + Lambda) | complete @cb33179fee | AC1 `Active` and the instance VALID, re-run by this seat; a draft stored | the simulate verdicts (INFERRED); the queue drain (NOT DONE) |

## 2. Release 1 -- irpt-status revision 6 (`6idtFvAm`), live since 2026-10-11T04:44:47Z

- Revisions 4 and 5 were rolled back on 2026-10-09 (two TypeErrors from members staged at different commits). Revision 6 is `2.0.0_SA_COO~P2`'s
  IB-pr-416 build: every investor-reporting member from commit `361c44fa9d`. This seat rebuilt it twice, from the candidate map and from the
  real map at pin `5c35a6f9f9`; both printed the signed digest.
- Pair `deliverables/2.0.0_SA_COO~Y2/release1/NEVER_WIDEN_PAIR_ANLREQ_RELEASE1_REV6_IRPT_STATUS.md` @7ce505dc5a; CTO half sections A3 and A5 of
  `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_416_THREE_FUNCTIONS_ONE_TREE_CTO_HALF.md` (@dfe795d2ce).
- **The real run** (`2.0.0_SA_COO~G2`, sr1 window 6, HELD from its msg 4108): the cottonwood history read 200 with items (revision 5 failed
  there); `REQ-5e4149d2`'s analysis-report 200 with 257 sections; its status-job 200 with the typed `ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE`;
  one GET of `/original` 200.
- **Measured by this seat:** live digest at 04:46Z, 04:51Z, 04:54Z and at the flip; the log group from the promote to 04:54:19Z, paginated and
  counted client-side: START 6, TypeError 0, Traceback 0, RetentionRefused 0, timeouts 0; the `/original` route count 1 across all APIs.
- **For L9, what is NOT established:**
  - Read 5 (one ticket-bound request reaches READY) is re-homed to release 4's order as criterion `REL4-READ5`, which reads FAIL (row S25,
    parked with `2.0.0_SA_COO~G2`). The check was not changed to pass; which order owes it changed (AMENDMENT 11, CTO msg 4240).
  - Reads 3 and 4 were measured on 2026-10-09 against revision 2 and not re-run on revision 6 (arms 3b, 3c not re-run).
  - The three widenings the one-tree build carries (IB-pr-405's `analysis-request-read` for svc-custody-statement; `svc-commentary` on
    `reserve`; `svc-irpt-packager` reading `ANALYSIS_COMMENTARY`) closed APPLIED, UNEXERCISED. The static reach read counts 0 reached
    `put` / `reserve` sites and 4 reached `ArtifactRepository.get` sites, each bound to one of four literal families
    (`release1/REV6_REACH_READ_IRPT_STATUS.json`, `release1/REV6_REACHED_ARTIFACT_GET_SITES.md`).
  - "The original-file read does not write" is NOT MEASURED.
  - The status-job answer is ruled DESIGNED (row S22 on S19); a re-read with the date opt-in is `2.0.0_SA_COO~G2`'s.

## 3. Release 3 -- the commentary draft store and Lambda, live since 2026-10-11

- Step A landed 2026-10-09. A2 (04:12Z) and B (05:27Z) were applied tonight by the re-seated applier at a pin that predated the Teams pull
  fix, without the zip re-read the CTO had asked for; that precondition had been parked by THIS seat on a carrier the applier does not read
  (row S23). Remedy, CTO msg 4178: step B2, a code-only re-apply onto the pull function's own package (pair amendment
  `deliverables/2.0.0_SA_COO~Y2/t1/NEVER_WIDEN_T1_COMMENTARY_CODE_REAPPLY_PAIR_AMENDMENT.md` @abbb4ac3ac; CTO half @2287c83ba4). Row S28.
- **Measured by this seat:** `outlook-global-commentary-draft-lambda` Active on `AI4UQD0M`, equal to the pull function; the mail function on a
  THIRD digest `VGIq85Xx` since 2026-10-07 (not moved; NFRA_TRNSPT's).
- **The real run** (the applier, step 6b, HELD from its msg 4249): one invoke at 06:09:56Z on the synthetic request
  `REQ-4b5155ac2ea9467ab771b414`, stage `draft_stored`; test artifact `ART-a46c4ab7...128f53`. So the admit, the composition read, the one
  model call and the store put ran once. The first invoke (step 6) had stopped at the reader on the id's shape.
- **For L9, what is NOT established:**
  - Step 5's four permission verdicts are INFERRED from documents: `iam:SimulatePrincipalPolicy` on the function's role is denied on this box.
  - The `commentary_ready` message that invoke sent is still on its queue (depth 1 at 06:25Z), expires about 2026-10-15T06:10Z, and only
    the resident's role may consume it. Row S26, ARMED. No draft has reached a packager, a ticket or a person.
  - The admit accepts a wider request-id shape than the composition reader (`_keys/keys.py:62` against
    `reports/commentary_composition.py:54`). Real ids fit both; it is not filed as its own row.

## 4. Thread

**NOT LIVE (`thread n`).** Release 4 (`AR-g-23`, the resident release with the packager; `2.0.0_SA_COO~G2`, workstream G) is not cut. Its gate,
`TO-APPLY-t1` complete, cleared tonight. FWD-1's one journey (a ticket filed through the form, the package's files opened from the ticket)
has not been run end to end.

## 5. Rows

Channel `surprise-channel/investigations/INVESTIGATION_v1.md`: 47 rows parse (53 JSON blocks). Filed tonight by this seat: S17-S28.

**ARMED: 7 rows read ARMED in the file; 2 of them (S16, S23) carry tonight's resolving rows, leaving 5 not dispositioned:**

| row | state as this seat knows it |
|---|---|
| S26 | ARMED by design until the queue reads 0; binds release 4 |
| W11-S1, W3-S1, W7-S1, W7-S2 | from rounds 1-2 workers; NOT re-read by this seat this session. They need the CVO's disposition or a named owner |

S16 and S23 carry resolving rows S27 and S28. Open BLOCKING rows from rounds 1-2 that read INERT (S2, S6, S15, W3-S3, W8-S1, W41-S11,
W41-S16, W41-S17) were not re-read tonight either; S15 is the reason read 5 waits on release 4.

**Queued for the next issuance (the CTO's analysis carries the first three):** S20 (the package Report opener shows the request record),
S21 (the history row states its client), S24 (`retained_ref` on analysis-report), then the candidates S17 and S18.

## 6. Judgment criteria for L9

None of the two apply orders carries a JUDGMENT criterion; their criteria are mechanical and are listed in section 1. What this packet asks
the CVO to judge is section 2 and 3's "NOT established" lists: whether release 1 and release 3 stand as closed on them.
