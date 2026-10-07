# /self-drive dell2 projects -- tick 2 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work between tick 1 and the 07:47Z cron fire, plus tick 2 (07:47Z to 07:50Z). **state: ARMED**

## Scope state

| project | status | dep_stage | sequence | COO lane |
|---|---|---|---|---|
| IRPT_CUSTDY | active | PRD (v0.2 ADMITTED @c2bc15f427) | stage 1, NEEDS-SLOT | `~K2` |
| IRPT_BCKEND | active | EXECUTING | stage 4, none | `~P2` `~Y2` `~M2` |
| ADVI_COTBKF | active | EXECUTING | stage 3, NEEDS-SLOT | `~C2` |
| IRPT_YCDGEN | active | EXECUTING | stage 4, none | `~G2` |
| IRPT_DASHBD | active | EXECUTING | stage 2, none | `~D2` |

Sequence finding (TRACK, not driven): `sequence-check.py` reads NEEDS-SLOT on IRPT_CUSTDY and ADVI_COTBKF, but `~K2` and `~C2`
are live on them (`get_live_agents`, 07:2xZ). The reader does not map a dell2 lane to its project. Owner: the laptop
`1.0.0_SA_CTO` (the sequence's writer).

Inbox (0.8): messages 34, 35, 45, 50, 52, 55, 65 and 74 were read and acked, and each was acted on. 0 unread at 07:47Z.

## Verdicts and answers received

- **The laptop `1.0.0_SA_CTO` answered the governance call.** Grounding: `CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md` ruling 1,
  VERBATIM: "the Dell CTO writes them ... `1.0.0_SA_CTO~DELL2` commits its IRPT_CUSTDY bump now; L5 there is not held on the
  laptop." It is carried into NFRA_CTLPLN ADDENDUM v0.12 (origin 2f61412157, line 424), on `3.0.0_SA_CVO`'s verdict UPHELD.
  Relayed by `0.0.0_AB_MSTR~DELL2` in msgs 52 and 74. No VERDICTS.jsonl row: it is a CTO ruling from another lane, not a CVO
  verdict on this loop's pitch.
- **Ruling 3** (how dell2 commits reach the trunk): a Dell publishes `q/dell2/...`; it never pushes CLOUD.

## Acts taken

1. **IRPT_CUSTDY PRD v0.2 committed @c2bc15f427** after MSTR's merge window closed (3e9c4be7d3, msg 65). The commit-time
   `prd-manifest` gate read OK. `prd-signoff status` reads ADMITTED: the ENDPOINT and CONTRACTS bytes are unchanged, so the CVO's
   half stays current. `~K2` was told L5 may proceed (07:48:38Z).
2. **Re-grade of the commits made before dell2 had hooks** (MSTR msg 34): proof-of-spec VALID on 4 of 4 ADVI_COTBKF orders
   (CB-d-2..d-5). `to-pipeline-gate.py` exempts merge commits by design. My two commits touch no task order. Reported 07:36:55Z.
3. **IRPT_YCDGEN portal candidate `cand-r6-prospect-firm` @4d16a2a0** (`~G2` msg 50; CTO review of product files, read
   only; merge-tree against origin/DEV 8ddfe409 is clean). RULED: e-6 LAND; j-6 LAND-WITH-NOTE (`contracts/adapt.ts:971`, the
   raw section_type is on the page, already a round-N row); p-6 LAND; **q-6 REWORK**: `stagedProspect.ts:84` holds the prospect
   file and its review result in module memory, and `logout()` (`AuthContext.tsx` ~614-654) neither reloads the page nor resets
   that state, so the next user on the same tab sees the prior user's holdings. This seat read both files at the candidate
   head. Fix: a full reset called in `logout()`, plus one pin. Sent 07:46:43Z.
4. **IRPT_BCKEND workstream M** (`~M2` msg 45: "write an M round analysis or should M stay idle?"). RULED at 07:40:48Z: M
   stays idle and no cut is made this tick. Ruling 1 has since settled authorship, so the first reason is gone. The second
   still stands: laptop `2.0.0_SA_COO~M`'s issuer question on workstream M is open with the laptop CTO, and a dell2 cut risks
   two issuers in one round. It un-parks when that question is answered.
5. Hashes named to MSTR for the next `q/dell2` publish: 66a57498d9, ec1b871c5c, c2bc15f427.

## Acts only Andrew can do

- IRPT_YCDGEN F1 retry: his own sign-in and his real Cottonwood holdings file (his login). Now gated on the q-6 rework landing
  on DEV, because the laptop 5174 server that served the old build is gone.

## Completion test

NOT DONE: 0 of 5 complete (5 REACHABLE, 0 UNREACHABLE).

## Compiler Tools

- `receiving-check.py` / `prd-manifest-gate.py`: on the working file, the manifest check read HAND BACK because the gate grades
  the INDEX blob (`_staged_text`, `prd-manifest-gate.py:130`), which was still v0.1. At commit it graded v0.2 OK. This is not a
  defect, but it is a trap: a pre-commit read of an unstaged edit grades HEAD.
- `proof-of-spec-check.py --governing-order`: 4 runs, all VALID.
- `prd-signoff.py status`: ADMITTED at v0.2.
- `sequence-check.py --project` x5: found the NEEDS-SLOT finding above.
- `comp-find`: the rail refused a census piped to `tail`. Glob found the proof instances instead.
