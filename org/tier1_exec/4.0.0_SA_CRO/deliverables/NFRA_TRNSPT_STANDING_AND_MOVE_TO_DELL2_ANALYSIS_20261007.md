# NFRA_TRNSPT -- where it stands, where it fits, and what moving it to dell2 takes

**Author:** `4.0.0_SA_CRO` (Chief Research Officer), 2026-10-07 ~14:0xZ. **For:** `1.0.0_SA_CTO` (base).
**On:** Andrew-direct 2026-10-07 ~13:4xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_134xZ_NFRA_TRNSPT_TO_THE_BOX_HOLDING_IRPT_YCDGEN_DELL2.md`.
**Measured:** 2026-10-07 13:51Z to 14:0xZ at the laptop, working tree near `f701d5da50`. Nothing was changed.

NFRA_TRNSPT is the Opal communications database project (directive D9): Teams meeting transcripts, market updates and
investment feedback emails in one private store, plus a service that drafts commentary when a report is generated.

## 1. Conclusion

1. **Andrew's read is right for one half of the project.** NFRA_TRNSPT outcomes FWD-10 and FWD-11 are the commentary
   layer that follows report generation. That half is not built. It is the half that belongs beside IRPT_YCDGEN and
   IRPT_BCKEND on dell2.
2. **The project can move now.** It is between rounds: 17 of 17 task orders read complete and no seat has worked it
   since 2026-10-02. The rule is "between rounds, never mid-round".
3. **Its register says site Z, not dell2.** The four-box layout Andrew approved at ~01:0xZ today sent it to site Z. His
   ~13:4xZ word is later and names the box that holds IRPT_YCDGEN. One placement edit by the CTO base resolves it.
4. **One thing cannot be moved by a placement edit: who may read the data.** The store's encryption key names one
   principal, Andrew's. A dell2 seat can build and test on fixtures; it cannot read a real row. That is the project's
   own outcome FWD-8 working as designed, and it needs Andrew's word either way (section 5, call A).

## 2. Where it fits in the process

```
IRPT_YCDGEN (dell2)        IRPT_BCKEND (dell2)             NFRA_TRNSPT (register: SITEZ)
generates the report  -->  report reaches READY  -- hook -->  commentary Lambda:
in Opal's branding         (no hook exists yet;               slices past commentary for a similar report,
                           PRD contract C-TRIGGER             one model call, a draft lands as an internal
                           makes it an IRPT_BCKEND order)     ticket with the report attached (FWD-10, FWD-11)
                                                                       ^
                                                                       | past commentary = the gold examples
                           NFRA_TRNSPT's database half:                |
                           Manav's feedback emails, pulled daily ------+   (FWD-7)
                           Teams transcripts, market updates               (FWD-1 to FWD-6, FWD-9)
                           through the gateway at site Z (NFRA_OPLGTW)
```

So the project has two halves with different neighbours:

| Half | Outcomes | Neighbour it depends on | Neighbour's box |
|---|---|---|---|
| Commentary service | FWD-10, FWD-11 | IRPT_BCKEND (the READY hook), IRPT_YCDGEN (the report), the Ticket Center | dell2 |
| Database: feedback emails | FWD-7, FWD-8 | the gateway's mail route (NFRA_OPLGTW) | site Z |
| Database: transcripts and market updates | FWD-1 to FWD-6, FWD-9 | the gateway's Teams tools (NFRA_OPLGTW) | site Z |

The gateway was a cross-box dependency while the project ran on the laptop, and worked that way. On dell2 it stays one.
The READY hook is the dependency that gets shorter: its producer and its consumer would sit on one box.

## 3. Standing, measured

Register (`org/missions/D9/NFRA/NFRA_TRNSPT/project.json`): status active, stage EXECUTING, PRD v0.1 admitted with both
halves signed, `placement` SITEZ, `coo_lane` `2.0.0_SA_COO~T`, which is dark. Its `phase` and `blocking` fields describe
2026-09-30 and 2026-10-01 and are stale; the current record is the project's `STATUS.md`, written by `2.0.0_SA_COO~D`,
which held one FAST round and wound down 2026-10-02 ~04:0xZ. Last project commit by a working seat: `0af795349a`,
2026-10-02.

| Outcome | State | Evidence |
|---|---|---|
| FWD-7 feedback emails filed daily, unaided | Mechanism LIVE, outcome NOT yet shown | Lambda `outlook-global-transcripts-pull-lambda` is Active. Its schedule fired on its own five days running (2026-10-02 to 10-06, 23:30Z); each `run.json` reads `no_person: true`, `listed` 13 or 14, `landed` 0. No new admitted email has arrived, so the DONE WHEN (a real email filed by the ordinary run) has no evidence yet. One email was filed on 2026-10-02 by a run a seat started. |
| FWD-8 only the named people can read | Partly held | The key policy of the store's key names one user, `Andrew_Berman`. STATUS.md: the second named reader has no AWS principal; the refusal of a third person has not been shown to Andrew. |
| FWD-1 to FWD-5 transcripts | Built and tested, not live unaided | 30 transcripts in bronze and silver (census of 2026-10-01). The Teams pull's Terraform was left DESIRED, not applied. STATUS.md "Next 3": the thread trace re-run is owed. The fourth meeting type waits on one calendar invite, a person act. |
| FWD-6 market updates; FWD-9 one question across all three | Not read today | STATUS.md does not report them; not measured. |
| FWD-10, FWD-11 the commentary draft and its attached report | NOT BUILT | `data/transcripts/scripts/outlook/slicer.py` and `gold.py` exist with tests. No commentary Lambda exists under `infra/aws/lambda/` and none is declared in `infra/aws/terraform/transcripts/`. No stream or event-source mapping exists in `infra/aws/terraform/investor-reporting/` (the READY hook). |

Suite at the last pin: 165 tests passed (STATUS.md, 2026-10-01; not re-run today).

Parked items carried in STATUS.md, each with an owner: the 14 flagged words on the first real email row (Andrew, or
the CTO's word that a seat may list them); the full id of the 2026-08-11 message; the fourth meeting type.

## 4. What the move takes

**Register acts (the CTO base; minutes).**
1. `project.json`: `placement` SITEZ to DELL2, with a `placement_ruling` citing the Andrew-direct record above;
   refresh `phase` and `blocking` from STATUS.md in the same act; name the new `coo_lane`.
2. `org/missions/SEQUENCE.yaml`: the NFRA_TRNSPT row's `why` reads "TARGET BOX: sitez". It changes on Andrew's word,
   which this is.
3. `CTO_PLACEMENT_20261007_FOUR_BOX_LAYOUT_ANDREW_APPROVED.md` lists NFRA_TRNSPT under SITEZ: an amendment line.
4. One relay through `0.0.0_AB_MSTR` to `1.0.0_SA_CTO~DELL2` (take it) and to site Z (release it). Whether site Z has
   seated or started anything on it was NOT measured from here; ask before the award.

**Seat acts (dell2).**
5. One COO lane on dell2 for this project alone (one project per Tier-2 seat). It is its own seat, not a rider on the
   IRPT_YCDGEN lane.
6. That lane starts from `STATUS.md` and the PRD. No handoff note exists from `2.0.0_SA_COO~D` beyond STATUS.md.
7. The next round is a new round: the ROUND-N analysis for the FAST round of 2026-10-01/02 is owed by the CTO before
   anything is cut. Recommended first thread for it: the commentary service (FWD-10), with the READY hook as its
   first hop, since that is the work that is on dell2 for a reason.

**Cloud gaps on dell2 (read from the policy files in `infra/aws/terraform/nfra-ctlpln-identity/`; DESIRED, the live
attachment was not read).**

| # | Gap | Effect on this project | Who closes it |
|---|---|---|---|
| a | The transcripts key policy admits only `Andrew_Berman`; the Dell policies carry `kms:Describe/Get/List` and no `kms:Decrypt` | dell2 can list the bucket and cannot read or write one object in it. Every check against real data fails on dell2. | Andrew's word (call A), then the laptop writes the key policy |
| b | The Dell policies carry no `secretsmanager:GetSecretValue` | a dell2 seat cannot call the gateway's mail route by hand (the bearer was read under Andrew's user). The scheduled Lambda is unaffected: it runs under its own role. | a role request, or leave the manual route on the laptop |
| c | A Dell creates no IAM role | the commentary Lambda and the READY hook each need a role | the control-plane role request to the laptop (C-ROLE-REQUEST) |
| d | The Dell create grant read "built, not applied" at 07:1xZ, and a Terraform apply from a Dell failed at refresh (row NFRA_CTLPLN-W4-S4) | new resources for FWD-10 cannot be applied from dell2 until both land | NFRA_CTLPLN; re-read its state before the round is cut |
| e | The commentary draft is one vendor model call (Kimi K3) | a vendor call needs Andrew's per-use word; a standing word exists for this project (record `ANDREW_DIRECT_20260930_06xxZ_TRNSPT_DONE_WHEN_CONFIRMED_PAGEFILE_APPROVED_KIMI_STANDING_WORD.md`), given when the project was the laptop's | confirm it travels with the project (call B) |
| f | The Teams tools need an interactive Microsoft sign-in, per user | not available on dell2; the laptop's own sign-in had lapsed on 2026-10-02 | stays a site Z or person act |

Nothing in the deployed mail pull has to move. It is cloud-side and keeps running wherever the project is seated.

## 5. Calls for Andrew (each with a recommendation)

- **A. May the dell2 agent user read the transcripts store?** REC: no for the raw tier; yes for the silver tier only,
  if the key allows that split, and otherwise no. FWD-8's promise is "only the people he named". The commentary
  service does not need a seat to read raw mail: the Lambda reads it under its own role, and the build tests on
  fixtures. A laptop seat running as Andrew reads back the real evidence, as it did on 2026-10-02.
- **B. Does the Kimi standing word cover the project on dell2?** REC: yes, unchanged in scope.
- **C. Move the whole project, or only the commentary half?** REC: the whole project. One project has one placement and
  one COO lane; the database half's remaining work is small and its gateway dependency is cross-box from any seat.

## 6. Not measured

- Site Z's side: whether a lane was seated for NFRA_TRNSPT after the ~01:0xZ layout, and any work on a site Z branch.
- The live IAM attachment on `cloudops-dell2-agent-user`; the table in section 4 is the repository's policy files.
- Whether the pull Lambda's role reaches the key by a grant (the key policy shows no statement for it, yet the Lambda
  writes; a grant is the likely route and was not listed).
- FWD-6 and FWD-9, and the 165-test suite, today.
- Whether dell2's COO capacity is free: two lanes were seen committing there today (`2.0.0_SA_COO~G2`, `~K2`).
