# /self-drive laptop directives -- tick 11 (2026-10-07 16:3xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`.
**Cadence:** 60m, cron `77f028d5`. **paired_with:** solo. **state: ARMED**. Covers the event-driven acts since the tick 10 log (author
time 2026-10-07T11:50:47-04:00 by `git log`) and the cron's eleventh fire.

## Measurements

- Trunk at 16:34Z (fetch): origin CLOUD `8798e5f484`; the shared laptop tree 11 ahead, 447 behind; no merge open.
- Sequence: 26 placed, stage enum OK, no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 2 of 3 COO lanes (`~C`, `~G`).
- Inbox: 0 unread files at the read; two more arrived and were read. Active commitments: 0 lines in 24 hours.
- Live on the laptop broker, 10. Stale summaries not read as state: `2.0.0_SA_COO~G` ("waiting on the round-2 analysis",
  delivered 16:3xZ), `4.0.0_SA_CRO`, `3.0.0_SA_CVO` ("open at the CTO: the 403", ruled 16:28Z).

## Andrew-direct since tick 10

- ~15:5xZ and ~16:1xZ at this terminal (record @39b37cf2bb): add Kenneth Cusick at Cottonwood; "We should have a skill for this".
- ~16:1xZ at `4.0.0_SA_CRO` (record @a3e5396e1e): six answers on the Ticket Center and NFRA_TRNSPT, among them "Yes Dell boxes can
  read all of that" (the transcripts store).

## Done by this seat directly

- **Kenneth Cusick provisioned** at Cottonwood by `users/scripts/create_user_v2.py --no-ses`: three rows written and read back
  (`opal-users-v2` PROFILE and MEMBER; `opal-partner-cottonwood`, 4 rows to 5); the temporary password checked against the stored
  hash with a wrong-string control; an Outlook draft created, not sent. The password is in no committed file.
- **The skill `/user-add`** (`.claude/skills/user-add/`).
- **The Python kit** (49 wheels, one tar, sha256 `60bb1a14...8799`) Taildropped to both Dells, rc 0 each.

## Calls ruled since tick 10 (the driver's own REC, each; event-driven)

| # | Call | Ruling | Carrier |
|---|---|---|---|
| 1 | pyarrow's version change (106373) | NO; Python 3.12 on the Dells instead | msg 106374 |
| 2 | The 3.12 installer: stub plus MSIs, or stop (106377) | stop; no stub goes to a Dell; ask the other boxes for the full installer | msgs 16:27Z, 16:28Z |
| 3 | Carry the 3.14 kit meanwhile (106388) | yes, carried | above |
| 4 | held-32 against dell1's CTO (106369) | dell1's ruling stands; landed on its terms | msg 15:51Z |
| 5 | Site Z's checked route (106370), and its batch (106399) | 5 pure packages offline; the 2 compiled ones read from the deployed Lambda first | msgs 15:51Z, 106403 |
| 6 | The transcripts store, on Andrew's word | this seat's ruling of 14:13Z reversed; a key-policy cell at `2.0.0_SA_COO~C`, with halves | msg 16:27Z |
| 7 | The 403 on dell1's render (106379) | the walker's access, by inference from a frontend-only diff; one control named | msg 106394 |
| 8 | LGIC_BLANKFIX round 2 (slug 106392) | FWD-1 NOT_REALIZED at 122 of 140; two calls ruled; six cells | @ef7133ec9a |
| 9 | The shared tree's lag | blocks no seat; a deploy seat's tree is a worktree at origin | msg 16:3xZ |
| 10 | Duplicate Taildrops on dell2 (106400) | one send per Dell here, one copy on dell1: the receive side on dell2 | msg 106404 |

## Reported to this seat, not measured by it

- The emergency release graded PASS under the issuer's amendment (`0.7.0_AE_CloudOps~I`); no principal minted.
- held-32 landed: two objects in the 49 Financial bucket, both read back equal to repo bytes by `0.0.0_AB_MSTR`.
- `0.7.0_AE_CloudOps~S` has read step 0 for TO-DEPLOY-e65 and waits on dell1's republished branch.

## Acts only Andrew can do

- NEW: the Outlook draft "RE: Opal Platform Access" is his to complete (the portal address) and send.
- NEW, conditional: if no Opal box holds the full Python 3.12.10 installer, 3.12 on the Dells needs his exception to his own
  red tier ("scripts and executables off the raw internet ... never"), or the Dells stay on 3.14.
- Standing: LGIC_BLANKFIX's DONE WHEN lines; the LGIC_LGCTFM card; a firm's people on their dashboard; the IRPT_YCDGEN sign-in;
  ADVI_BILLING and NFRA_OPSWKF inputs; the D2 hold; MDPF_HEALGAP HG-t-2.

## Completion test

NOT DONE, read from the register: 20 parked; 3 UNREACHABLE (LGIC_CANON, LGIC_LGCTFM, LGIC_ENFORCE); D10 UNMEASURABLE.

## Owed by this seat

- CTO halves: the transcripts key policy; dell1's read-only join; the break-glass role.
- The L10 read for NFRA_CTLPLN rounds 2 to 4 on `3.0.0_SA_CVO`'s slug.
- The correction of FWD-18's DONE WHEN and FWD-16's SOURCE at the next NFRA_CTLPLN addendum.

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `users/scripts/create_user_v2.py` | the canonical user writer | PASS | found by a file search; `comp-which` had no rule for it |
| `bcrypt.checkpw` | the temporary password against the stored hash | PASS | with a wrong-string control |
| `opalgateway create_draft` | the Outlook draft | PASS | a draft, never a send |
| `get_live_agents` | seat state | PARTIAL | three summaries older than the messages answering them |

- **What worked:** reading an existing row of the same firm before writing a new one.
- **Gap found:** the user script stamps a fixed creator and omits two name fields; both are in the skill.
