# `/self-drive 30m` every site-Z project -- ticks 4-6 (2026-10-09 ~09:3xZ to ~10:35Z), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_SELF_DRIVE_30M_EVERY_SITEZ_PROJECT.md` @4752d8dfcc.
Cron `fff05062`. Previous log: `ctoZ_self_drive_SITEZ_ALL_tick3.md` @e09a6fd867. **state: ARMED.**

## Scope

7 non-terminal SITEZ-placed projects; 2 of 9 closed. **Completion test: NOT DONE.** REACHABLE 6, UNREACHABLE 1 (NFRA_MCPMSP: G-MSPID).
Inbox at tick 6: 0 unread. Open calls: 1 (Barron's sign-in, an act).

## Acts and rulings

| item | ruling / act | carrier |
|---|---|---|
| open call b865, 08403355 gold wiring | NO gold build; CLOSED on laptop XA-20261009T093754Z-26ac (upheld) | @82c47946e7 |
| open call 9c9d, NFRA_MCPINDEX round 9 before round 8 drains | NO (rule 27: one open round per issuer); CLOSED on laptop XA-20261009T101408Z-e415 (upheld) | @ff362e8444 |
| COMM_ASSIST PRD header fabric laptop -> site-z (to-pipeline-gate refusal) | fixed, header-only, v0.3 | @c225bcc74e |
| COMM_ASSIST r12 CVO carried point: `firm_domains()` reads every registry firm | r12 proceeds (the gateway's Andrew-gated table holds); round 13 pins it to C-MAIL's five | msg to COO~ZZ |
| dell2 transcript pull: bearer name and route contract | `gateway/transcripts/bearer`; contract from source | @f67fbc2390 |
| dell2 ADVI_BILLING packet E2 (`copy_site_file_to_s3`) | TAKE, after r29 and MX-r-9, under its own pair | msg 32663 |
| dell2 `/hx/transcripts` METADATA GET | TAKE, one route, one Graph path, after r29/MX-r-9/E2 | @7f58eb8f77 |
| NFRA_OPALAI step 4 re-run (MSTR 32655) | Z-S63 FIXED live at opal_ai c9983bd: the fixed prompt ran, whoami = Opal Bloomberg, no sign-in; Analyst closed 10:06Z before Teams | (observation) |

## Never-widen halves signed

COMM_ASSIST r12 mail deploy @9e7932bc79 (binds the measured 12-file diff; the 7 registry files are additive when keyed by id);
NFRA_IAMROLES202609 IAM-v-4 @8e981e7cbc (DescribeSecret off smartx-assets-pull-role; live pre-state = tf:101); MDPF_DEMQUE DQ-t18 @3ccf1f560f
(the BBGTML meter wrapper; C1: merge only after today's 11:00Z pull is read).

## Acts only Andrew can do (cited)

- **Barron's sign-in** (AMGT_HARVST, call `sitez-20261008T231757Z-9f24`): his login.
- **G-MSPID** (NFRA_MCPMSP): the MSP calling identity and its MFA sign-in. "Not yet" / "doesnt matter right now". Not asked again.
- **Forced removal of two drained MCPORTAL worktrees** (call `sitez-20261009T083926Z-84ef`, HELD): a recursive delete.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `xadj.py open/show`, `open-calls.py close --xadj` | PASS | two CROSS-BOX calls closed on laptop rulings within ~10 minutes each |
| keyed JSON diff of `infra/logic/registry` | PASS | a positional diff misread index shifts as 234 changes; keyed by id, 0 |
| `iam get-role-policy`, `lambda get-function-configuration` | PASS | pre-state for IAM-v-4 |
| `git archive`-free source reads (`transcript_route.py`, `run_daily_pull.py`) | PASS | grounded the route contract and the DQ-t18 wrapper safety |

-- 1.0.0_SA_CTO~Z
