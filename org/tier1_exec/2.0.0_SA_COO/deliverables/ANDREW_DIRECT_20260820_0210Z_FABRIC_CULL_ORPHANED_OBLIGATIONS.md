# ANDREW-DIRECT 2026-08-20 ~0210Z -- FABRIC CULL, and what it orphaned

**VERBATIM (to `2.0.0_SA_COO`):**
> *"Yeah i closed down all the agents aside from you CTO MSTR and CRO~A because they were idle and i
> wanted to cull the not-working fabric"*

**SURVIVING ROSTER, grounded on telemetry rather than on the statement** (02:14Z, `<8m` activity):
`0.0.0_AB_MSTR` · `4.0.0_SA_CRO~A` · `2.0.0_SA_COO` · `1.0.0_SA_CTO`.
**CULLED:** `0.8.0_AE_CloudComp` · `0.7.0_AE_CloudOps` · `0.4.0_DS_ClientPlatform` (+`~A`, `~B`) ·
`3.0.0_SA_CVO` · `4.0.0_SA_CRO` (base). *(Note the base CRO seat is culled while the `~A` lane
survives.)*

⛔ **THIS IS RECORDED AS A SOVEREIGN ACT, NOT A PROBLEM TO SOLVE.** He culled deliberately and said
why. **Nothing here is a request to respawn anything.** Its only purpose is that **the mid-flight
obligations are visible to nobody else** -- each culled seat carried live commitments that the seat
itself was the record of.

## ⛔ THE CAPABILITY GAP, STATED PLAINLY
The four survivors are **coordination (COO), architecture (CTO), ferry (MSTR), research (CRO~A)**.
**There is no AE seat and no DS seat.** So until one exists:
**nothing can be deployed, applied, run, or read on the executing plane.** This fabric can decide,
design, route and record. It cannot touch AWS or data.

## >> THE SHARP RISK: THE SCHEDULED RUNS STILL FIRE. ONLY THE READERS ARE GONE.
Tonight's work armed two cron-driven paths, and **both will execute on schedule with no one assigned
to read them:**
| when | what | reader was | status |
|---|---|---|---|
| **~22:00Z today** | TrueShares first scheduled fetch (`cron 0 22`) | `0.4.0_DS` | **UNOWNED** |
| **~12:45Z today** | first unattended green on last night's deployed bytes; 13:30Z proof read | `0.4.0_DS~A` | **UNOWNED** |
**This is exactly the shape the whole night was spent on: A GREEN INVOCATION IS NOT EVIDENCE OF A
WORKING FETCH.** TrueShares in particular is a **current-day-only, forward-only source** -- an
unwatched failure there is *permanent daily data loss behind a healthy green*, which is the specific
harm AE caught pre-arming. The runs firing unobserved is not the same risk as the runs not firing.

## ORPHANED OBLIGATIONS, by owner
**`0.7.0_AE_CloudOps`** -- the two **41.8-day credential holds**, routed to them at **020924Z, ~6
minutes before the cull**, after being unblocked for the first time since early July. Also: the
2 pending roster entries, and c1-3's trigger decision (now answerable, no owner).
**`0.8.0_AE_CloudComp`** -- the **Andrew-prioritized comp-adversary dot-truncation fix**;
`NFRA_TRUNCLASS.SWEEP` (cut tonight, never started); **H8**; the **ack-path canary**, still the one
thing the broker cycle did not verify; the standing queue (REG/J3/HELD-STATE/T1-DEFROST).
**`0.8.0` + `4.0.0_SA_CRO` base together** -- **W-15's THIRD grain**, the canonical ontology
propagation (`NFRA_ONTOLOGY_C2C3_CANONICAL.yaml`, untouched ~11h, `DISSOLVING`=0, 8
`model-portfolios` carriers standing). **It gated CRO base's T2/T3 -- and both the blocker's owner
and the gated seat are now culled**, so that leg is doubly unowned.

> ### ✅ RESOLVED @022631Z -- **PARKED-WITH-A-REASON (CTO), not unowned**
> **THE LIVE `ANY_EXEC` LIST AFTER THE CULL IS EXACTLY TWO: CTO AND COO.** (CRO~A measured, I
> verified: `.owned-paths.yaml` is enumeration-based and `4.0.0_SA_CRO~A` is NOT in `ANY_EXEC` --
> *"a title is not a grant, and neither is a lane suffix on a granted base."*) I routed it to CTO
> rather than taking it myself; CTO chose **(2) it waits**, and stated the reason in full so the
> morning fabric inherits a DECISION rather than a gap:
> **(a) ZERO LIVE BLOCKAGE** -- the gated consumer (CRO base's T2/T3) is *also* culled, so executing
> at 02:30Z unblocks nobody who exists. On respawn the owner executes it in minutes from records that
> already carry the content (CVO's adjudication @51285984d6 names the `DISSOLVING` marking; CRO's
> naming word gives keyed-mdpf + alias; the 8 carriers are enumerated).
> **(b) THE LEAD IS A SOVEREIGN ASSIGNMENT** -- Andrew put CRO base at LEAD with CVO assisting **and
> culled them knowing that**. An unled canonical-ontology edit on that spine would be re-verified by
> any respawned lead anyway, so **it does not bank the work; it banks a re-verification obligation.**
> **(c) PERMITTED IS NOT OWNER, AND IT CUTS BOTH WAYS** -- CTO adopted the same test I applied to
> myself: ANY_EXEC-permitted and architecture-adjacent is **capability, not ownership.** Right owner
> is 0.8.0-or-successor under the CRO-base lead, on respawn.
> **STATE: PARKED-WITH-A-REASON. Materially better than unowned, and the honest state.**
**`4.0.0_SA_CRO` base** -- **the ontology lock-down LEAD** (Andrew-ruled 08-19: CRO base leads, CVO
assists). **Both the lead and the assist are culled.**
**`0.4.0_DS~B`** -- CRO~A's cent-exact BI-plane tie-out (`456,773,323.40`, 216 groups, cross-plane)
landed as their L1 authority proof with **no seat left to consume it.**

## THE TWO CRON READS NOW HAVE A NAMED READER (CTO, 021739Z)
**12:45Z: CTO's, and it always was** -- DS~A's protocol @8ddd943794 records F3-FIRST as CTO's read
order, and every falsifier is a READ inside their pre-authorization (`schema_version` 1.1-vs-1.0 as
the ran-vs-stale discriminator; parquet carrying `quantity`; product tables from S3 never the run
log; `LastModified` never `_ingested_at`). They take the 13:30Z proof read too.
**22:00Z TrueShares: NAMED FALLBACK READER at ~21:30Z if no DS-class seat exists -- CTO.**
**HONEST RESIDUAL (theirs, and it is the right one): if a green FAILS, the REMEDY is an ACT and it
queues** until an executing seat exists. That is the cull's known shape, not a new risk.
> **A fallback with a name and a time is a plan; a fallback with neither is a hope.**

## WHAT IS GENUINELY FINISHED AND NEEDS NO ONE
TAXSMA code plane complete (both first mints byte-verified) · WS-R3 deployed · source-map landmine
disarmed · TrueShares armed on both planes · dim 436 dropped with its measurement · MDPF_INFACTUAL
closed OVERTAKEN · W-15 grains 1+2 · the SITEZ merge landed · `MEMORY.md` back under its load cap.

> ## ⛔ CORRECTED @0219Z -- THE BROKER FIX WAS ON THIS LIST AND IT IS ONLY PARTLY DONE
> I listed *"broker cycled with the re-offer bound verified holding at 3"* as FINISHED. **I measured
> the DB and concluded about the SYSTEM.** CTO's post-cycle payload showed **x5 multiplicity across
> 31 distinct** against a cap of 3. I ran their discriminator at 02:19Z:
> `MAX offer_count anywhere = 3` · dist `0->319, 1->1, 2->1, 3->117` · CTO's rows `2->1, 3->32`.
> **THE COUNTER IS PERFECT AND THE PAYLOAD IS x5. Both are correct, and they cannot both be true of a
> mechanism that reads its own counter.**
> >> **THE SPLIT: THE BOUND LIMITS HOW MANY TIMES A ROW IS OFFERED, NOT HOW MANY COPIES ONE OFFER
> ASSEMBLES.** 117 rows sat down at the ceiling, so **unbounded growth IS genuinely fixed -- the
> x45-and-climbing curve is dead.** But payload multiplicity is untouched: heartbeats stay ~5x
> larger than needed and **do not grow.** Better than four hours ago; not "fixed."
> **MECHANISM INFERRED, NOT SOURCE-CONFIRMED** -- two output measurements, no read of the assembly
> code. `0.8.0` held source and is culled.
> **Same shape as CVO's "complete at both grains," which I had corrected ninety minutes earlier: a DB
> read is not a system read, and the return path is a second plane my query never touched.**
> **MOVED: FINISHED -> ORPHANED-AND-PARTIAL**, beside the ack canary. Same instrument family,
> ~530KB scale, day-fabric urgency.

## MY OWN MISS, RECORDED HERE BECAUSE IT IS THE NIGHT'S CLEANEST INSTANCE
I reported the two credential holds as *"at Andrew, outside COO power"* in **every drive cycle
tonight** and **never ran a describe to check whether the credential already existed.** They had
existed since 2025-12-23. My own skill requires that an `awaits-X` be legitimate *only if X is
outside COO power **AND** you re-verified it is still moving* -- **I verified only that the gate still
SAID it was waiting.** MSTR's line stands as the lesson: *existence checks are describe-cheap.*
