# MDPF_TAXSMA - L5 seat priority and routing

Author: `1.0.0_SA_CTO~A`. Updated after **CTO97073 at2026-09-15T12:55:50Z**. PRD **v0.2 ADMITTED at60c722fe64**; both current signatures remain unchanged.

## Current disposition

**The exact lane `2.0.0_SA_COO~T` is LIVE and is now bound in `project.json`.** MSTR97081 confirms its launch after COO~F's exit. The checked-in canonical `org/mcp/server.py:get_agent_status("2.0.0_SA_COO~T")` returned **LIVE at2026-09-15T13:20:53Z**, last seen10s ago, PID26332, working on MDPF_TAXSMA startup and L5 decomposition. This was a direct invocation of the unchanged repository function because no callable MCP status tool was exposed in this Codex session; it did not register a seat or start a server/helper. The canonical L4 notifier sent the unchanged v0.2 release as **97083 at13:22:49Z**; broker readback at13:30:03Z is **READ**, acknowledged by that exact lane at13:26:22.594818Z. The final delivery receipt is below. L5 remains owned by COO~T and is not complete merely because the session is live.

Exact unread notice handled: `20260915T125550Z_1.0.0_SA_CTO_ANDREW_RULED_the_seat_order__MDPF_TAXSMA.md`, Msg-ID97073, sender `1.0.0_SA_CTO`. It relays Andrew's ~12:5xZ words verbatim:

> If push mdpf_taxsma as the next one followed by nfra_oplgtw

The CTO landed that order in **`org/missions/SEQUENCE.yaml` v4 at `8f0c4fa2bf1538031561ed60993976956e974efa`**. This author read the committed YAML: new stage0 contains MDPF_TAXSMA first and NFRA_OPLGTW second, both without waits_on gates. Stages1-3 remain as in the CTO's ruling. This resolves LD-0567's conflict with the earlier LGIC_CANON claim on COO~F's next free slot; it also confirms Andrew's earlier ~07:5xZ word at4524cc2466. The rejected tail-placement proposal8c70cabc48 remains **NOT ADOPTED**.

NFRA_OPLGTW keeps **`2.0.0_SA_COO~O`**. It needs no new slot while that lane remains active; it is next if the lane goes dark. IRPT_FNTEND round9 is not in Andrew's stated seat order and waits for a seat after these. The subsequent MSTR97076 reservation uses the slot freed by COO~F for fresh COO~T; COO~F is not repointed to TAXSMA.

## Named lane and launch condition (satisfied at13:20:53Z)

MSTR notice **97076 at 13:01:42 UTC**, exact file `20260915T130142Z_0.0.0_AB_MSTR_MDPF_TAXSMA_seat_named__2.0.0_SA_COO_T__.md`, names **`2.0.0_SA_COO~T`** under **LD-0569 at `f0f86cae9a8c4160458dc928e6cfeb40666bc7f0`**. It is a fresh context; COO~F remains the IRPT_FNTEND context and is not repointed. MSTR reports a clean 12:57 UTC preflight for ~T and asks COO~F to write its cold handoff and exit. MSTR will launch ~T once process truth shows that capacity free, then send this seat a confirmation line.

**Do not fire the notifier before that line.** The installed `.git/hooks/post-commit` invokes `.tools/git-hooks/prd-header-notify-post-commit.sh` after every commit; ordinary commits run `prd-header-notify.py reoffer`. That path reads the project's lane and can dispatch a held release. To honor MSTR's instruction without bypassing a hook, this seat records the reservation here but leaves `coo_lane` null until launch confirmation. No extra approval is requested.

MSTR's disk note (12 GB free on C:, about 1.4 GB per worker worktree) is an input for the new COO's later L6 fan-out. It does not authorize this seat to clean C:/tmp or launch workers, and it does not reinstate the resolved priority hold.

## Current sequence measurement

`python .tools/sequence-check.py --project MDPF_TAXSMA`, read after97073, reports:

- **PLACED, stage0**, PRD v0.2 ADMITTED with both current halves SIGNED; `dep_stage=PRD`, flag **NEEDS-SLOT**.
- **Next COO slot:** MDPF_TAXSMA -> LGIC_CANON -> ADVI_FIRMBKTS -> MDPF_CANON -> IRPT_BCKEND. NFRA_OPLGTW is already staffed, which is why it does not consume the next-slot queue entry.
- Laptop capacity **3/3**, lanes COO~F, COO~G and COO~O, from `org/mcp/liveness.json` registrations seen within120 seconds. This is the checker's broker-liveness observation, not an independent process or open-order audit.

The priority decision, lane selection and launch condition are now settled. The measurement above is historical; the exact canonical status at13:20:53Z supersedes the old F/G/O registration snapshot. Canonical delivery and intake by COO~T are now confirmed READ; the next work is its L5 decomposition.

## Next owners and exact handoff

1. **[0.0.0_AB_MSTR, complete]** Notice97081, exact file `20260915T131240Z_0.0.0_AB_MSTR_2.0.0_SA_COO_T_LAUNCHED_13_10Z_for_MDPF_.md`, reports COO~F's cold handoff at6d8030b6ee and exit, then COO~T's launch around13:10Z. It instructs this seat to bind the lane and fire the notifier once canonical get_agent_status reads LIVE.
2. **[1.0.0_SA_CTO~A, complete]** The exact lane measured LIVE at13:20:53Z; `project.json` now records `coo_lane: "2.0.0_SA_COO~T"`. No sequence edit or PRD_NOTIFY_TO bypass is used.
3. **[1.0.0_SA_CTO~A, complete; READ confirmed]** Binding commit `a245ccd226` triggered the installed canonical post-commit notifier, which sent **97083** to the exact lane at13:22:49Z, attempt1/6. The broker initially returned SENT at13:25:23Z. Final readback at13:30:03Z confirms READ, acked_by exact COO~T at13:26:22.594818Z. The canonical notifier retired the outstanding row after that acknowledgement.
4. **[2.0.0_SA_COO~T]** Own L5 decomposition and the downstream canonical flow for admitted v0.2 at60c722fe64. This routing note issues no task order or implementation GO.

The named-person workbook-content authorization remains a capability-activation input under the signed PRD; it is not a new whole-project precondition on L5 priority. All eight approved endpoint bars still require deliberate walkthrough or controlled-test EXERCISED proof at delivery. This update changes no PRD, contract, signature, workbook or production resource.

## Superseded routing history

COO~G notice96997 declined the project under its assigned scope and capacity; that refusal did not select another lane. The earlier checker read TAXSMA as UNPLACED. CTO97006 then rejected the proposed placement after IRPT_BCKEND and kept movement held until Andrew resolved the competing LGIC_CANON next-slot claim. That decision hold is now superseded by97073 and SEQUENCE v4; the historical checker output is not the current queue.

Prior authority: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_075xZ_LAPTOP_CAPACITY_ORDER_TAXSMA_THEN_OPLGTW_THEN_IRPT_BCKEND.md@4524cc2466a861f38565eac09e5f88c9e10a9013`, LD-0567. No new sequence edit is made by this seat.

## Canonical delivery receipt, 2026-09-15T13:25:23Z

- Binding commit: `a245ccd226`; exact `coo_lane`: `2.0.0_SA_COO~T`.
- Installed `.tools/git-hooks/prd-header-notify-post-commit.sh` / `.tools/prd-header-notify.py reoffer` released the held v0.2 row, **Msg-ID97083**, from `1.0.0_SA_CTO~A` to `2.0.0_SA_COO~T`, sent at `2026-09-15T13:22:49.679428+00:00`, attempt1/6, held=null.
- Subject: `[PRD LANDED] MDPF_TAXSMA v0.2 @905d2df375 -- step 4 done; step 5 is yours`. The release pin is the second-signature commit; finalized ADMITTED metadata remains at `60c722fe64`.
- Canonical `delivery_state(97083)` / broker ledger read at13:25:23Z: **SENT**, last polled13:24:24Z; emitted_at=null, acked_at=null, acked_by=null. READ is pending and must not be claimed from this receipt.
- COO~T was sent the finalized admitted pin, contract and next-limb ownership at13:23:59Z and asked to ACK97083. MSTR and base CTO received the measured status and handoff at13:24:00/02Z.
- Fresh `sequence-check.py --project MDPF_TAXSMA`: PLACED stage0; PRD v0.2 ADMITTED, brief and ratified-text SIGNED; no flags; capacity3/3 COO~G/~O/~T. TAXSMA no longer consumes a NEEDS-SLOT queue entry.
- Unchanged file hashes verified after binding: PRD SHA256 `35c38dc71f71739116f04d8a647cf66025a041279ec2a79175daaed22583ec34`; contract SHA256 `5adfb0c5c001f42fc3591d08d5819a7d990f7b9baaf58af232bd2fe892bf7d9a`.

This completes the named-lane binding and canonical send requested by97081. The next output is COO~T's L5 decomposition; neither delivery nor liveness certifies that output or endpoint exercise.

## Final agent-intake receipt, 2026-09-15T13:30:03Z

Canonical `delivery_state(97083)` now returns **READ**. The broker names `to_serial` and `acked_by` as exact **`2.0.0_SA_COO~T`**, with `emitted_at` and `acked_at` both **`2026-09-15T13:26:22.594818+00:00`**. The notifier's outstanding v0.2 row is retired. This supersedes the earlier SENT-only observation; the named-lane binding, canonical send and agent intake are complete. COO~T owns L5 decomposition, which this receipt does not certify.

## S02 source registry dependency, CTO97095

The14:17:53Z CTO notice identifies a fact for the unchanged v0.2 cut: the workbook source has no systems.json row, so the canonical address builder refuses sharepoint and ms. Independent14:22Z probes reproduce both failures with four registered positive controls. `S02_SOURCE_REGISTRY_DEPENDENCY.md` records the exact evidence and the bounded-payload/raw-source classification question sent to LGIC_NAMING owner COO~G at14:23:19Z. COO~T received the dependency for S02 at14:23:21Z; other surfaces continue. Per-run status is separate firm State, and no retention beyond the admitted minimized Gateway response is authorized. No key/class is invented and no signed PRD, contract, endpoint, seat assignment or project stage changes.
