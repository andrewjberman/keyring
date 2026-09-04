# /self-drive NFRA_OPSEC202609 -- ticks 4-6 (2026-09-03 ~10:43Z-12:0xZ), 1.0.0_SA_CTO~Z

state: ARMED | cron 30635e1e (:13/:43) | carrier org/XXX.md CTO row @f41a37322e | paired: solo | last log: tick 3 @9328b58827
scope: NFRA_OPSEC202609 (D12, site-z) -> 1 project (denominator: 1 of 1) | device SITEZ | completion test: NOT DONE (status active)

## Ticks covered

| tick | when | what |
|---|---|---|
| 4 | ~10:43Z | quiet on calls; the CVO's L8-L10 slug in the tree uncommitted (foreign rows) -- the Z-S10 disarm record HELD on the never-commit-over-a-foreign-row rule |
| 5 | ~11:13Z | the round-1 stamp @fdbe7360b9 read; dep_stage EXECUTING -> ROUND_CLOSE (row owner) @f726808ecb; Z-S21 (the DISARM RECORD for Z-S10) @e0df0ac956; ledger row 2 landed @f6e98d017e |
| 6 | ~11:43Z | the COO's card 19667 (OP-s-1, the REST API's carrier) pitched as 19668; verdict 19674 received and landed as ledger row 3 (this commit); round 2 opened at L6 (19678) -> dep_stage ROUND_CLOSE -> EXECUTING (this commit); the gate-model fork with the laptop CTO ruled (19685) |

## Calls pitched

- **tick 6, OP-s-1 (19668, on the COO's card 19667):** the REST API opal-portal-api f61h681z9g has no Terraform declaration; how does FWD-1's authorizer reach it -- (a) import first, (b) the script path, (c) a distinct adoption cell. REC (a) as OP-s-1's own first limb with the Z-S14 plan bar and a body-identity control. Classified ADJUDICABLE (no NEVER law names the class; C-10 is the PRD's own constraint). RESERVED claims pitched: 0. The all-reserved tell did not fire.

## Verdicts received

- **19674 (3.0.0_SA_CVO~Z, tick 6) -> ledger row 3.** Operative sentence, verbatim: "(a), the import as OP-s-1's own first limb, with the Z-S14 bar and the body-identity control -- as pitched, plus two amendments." AMEND C: the body-identity read is taken AFTER the first apply (an import writes state only); acceptance rows (1)-(7) in sequence; a non-empty semantic diff between export1 and export2 is a STOP and a row. AMEND D: the denominator is 39 printed as 20 non-OPTIONS + 19 OPTIONS (the REQUEST authorizer keyed on the origin header runs on preflights), with a refused OPTIONS at the raw address and a positive control (a preflight THROUGH CloudFront that succeeds); if the type cannot run on OPTIONS the denominator falls to 20 with the reason in the proof. Grounding validated by the driver at the pins: decomp @HEAD :64 (the cell, denominator 20); PRD @36786251af :420-426 (C-10 binds FWD-14..18 as written; the project-wide reading is ledger row 2's); DESIRED plane re-run with a different instrument (git ls-files: 0 of 398 tracked .tf under infra/aws/terraform declare aws_api_gateway_rest_api; the CVO's comp-find census read the same 0). LIVE counts (38 resources / 20 method-bearing / 39 methods / 0 authorizers) stand on the COO's aws read until the face's first acceptance row.

## Acts taken (driver's own lane)

| act | vintage |
|---|---|
| dep_stage EXECUTING -> ROUND_CLOSE on the stamp; REGISTRY cell; index regenerated | @f726808ecb |
| Z-S21, the DISARM RECORD for Z-S10 (belt stays; :6-10 narrative rides TO-OP-S-2 as the rider, three roles measured first) | @e0df0ac956 |
| ledger row 2 (Z-S14 verdict 19607) | @f6e98d017e |
| ledger row 3 (OP-s-1 verdict 19674); dep_stage ROUND_CLOSE -> EXECUTING on TO-OP-S-25-26-27 @435dcf9d85 + TO-OP-S-2 @339213aa54; REGISTRY cell; index regenerated; verdict recorded on the row's phase | this commit |
| deploy record d12-sms-origination-identity-activation reshaped to the HELD form | @f0a9691483 |
| gate fixes on this seat's surface, each with a falsifier: surprise-row-gate _blob utf-8; halt-gate race guard + 7/7 battery; proof-of-spec cell_refs separator + convention sentence; deploy_ledger table-row status | @c3ef3a2530, @1c4a867709, @50ff3d674a, @79c0e68071 |
| the surprise-row override plumbing: safe-commit exports the audited reason; the hook's block 10 honours it (installer template + this device's live hook) | @08497afdbe |

## The gate-model fork, ruled

The laptop 1.0.0_SA_CTO (93561 via 19675) asked this seat to stop its safe-commit.sh case-pattern edit (the laptop closed that defect @0fb0d15f19) and disputed the REMEDIATED-needs-no-route exemption. This seat stopped the case-pattern edit uncommitted, stated its reading (19682: the route axis has no value for "nothing"; s.5 closes on the remediation row; the schema makes route optional), and held the gate edit one reply cycle. 3.0.0_SA_CVO~Z (19680) added the discriminating fact: under the laptop model the schema's REMEDIATED state is unreachable on any remediation row, so exactly one carrier must change either way. **RULING (laptop CTO 93571 via 19685): "Both positions were half right"** -- a NEW remediation row MAY omit route and loop_target IFF remediation.state is REMEDIATED and, when ARMED, disarm.state is DISARMED; every other route-less row stays refused; the base lands it in surprise-row-gate.py with a four-cell battery, reaching site Z on the next CLOUD -> SITEZ leg. This seat's (a) discarded from the working tree (git checkout) as asked; (b) was never committed. The (c) installer diff and the (b2) export travel to the base as a patch by message; both are already in @08497afdbe here (committed before the ruling was read) -- identical bytes at the base merge clean; a different spelling is the integrator's pick. The CVO's four REMEDIATED rows (S2, S11, S13, S17) wait for the ruled gate at HEAD on SITEZ. The CVO's correction to the ruling's record (19689: the round-1 slug landed NO done item as a re-entry row; the five done or out-of-project items simply carry no remediation row) rides the same carrier back.

## Scope state (denominators printed)

| project | status | dep_stage | task orders | rows |
|---|---|---|---|---|
| NFRA_OPSEC202609 | active | EXECUTING (round 2, since 11:47Z) | 2 open (TO-OP-S-25-26-27 ~S GO 11:41Z; TO-OP-S-2 ~Z GO 11:47Z) / 4 terminal (round 1); TO-OP-S-16-17-8R2 drafted, dispatches on the key's APPLIED ledger; OP-s-1's task order next on ledger row 3 | 21 investigation rows (Z-S1..Z-S21), 5 remediation rows (all SPEC_ERROR -> 6) |

Completion test: **NOT DONE** -- org/projects/NFRA_OPSEC202609.json status `active` (1 of 1 members REACHABLE; 0 UNREACHABLE). Round 2 runs at L7 on two seats; the decomposition is not spent (the in-place key flips, the demo import, S13, OP-s-1, OP-s-4, OP-s-24's Lambda limb remain).

RESERVED cards at Andrew: none open on this scope (OP-x-2 and OP-x-6 approved ~08:4xZ; OP-x-1 and OP-s-1 adjudicated by the loop; Z-S14 adjudicated tick 2). Carried for the successor, outside this scope: the D7 forks (no ratified D7 macro; OPAL_TICKET_VNEXT fails R1).

## Compiler Tools

- ledger: org/tier1_exec/1.0.0_SA_CTO/drive_pairs/NFRA_OPSEC202609/VERDICTS.jsonl (3 rows; `consumed` is the consumer's)
- grounding re-runs: `git show <pin>:<file>` line reads; `git ls-files infra/aws/terraform` + a per-file substring read (the DESIRED plane, a different instrument from the CVO's comp-find)
- flip: scratchpad flip_executing.py (project.json) + an in-line REGISTRY substitution (assert 1 of 1 per token); `.tools/missions-tree-index.py derive --write` then `check`
- falsifiers: scratchpad rowgate_falsify_v2.py (the gate, BEFORE/AFTER); the hook block exercised on an in-repo bad row (rc 1 / rc 1 / rc 0 + WARN)
- inbox: org/mcp/inbox/1.0.0_SA_CTO/~Z/ (the lane SUBDIR; the suffixed dir is a decoy)
- push state: LOCAL (0.0.0_AB_MSTR~Z integrates SITEZ; LD-0367)
