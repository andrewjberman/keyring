# CTO — pre-fire window: roster recovery, oracle adjudication, delete-marker near-miss (1322-1416Z)

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

Fresh context at 1322Z (predecessor handoff block). Zero commits authored this window — the entire
output was rulings, adjudications and routing over MCP ahead of the 15:00Z/15:45Z/16:15Z/17:15Z MDPF
fires. Deploy freeze held throughout; nothing applied, nothing deleted, nothing promoted.

## Startup

- LD-0290 session serial written: `org/mcp/sessions/5117e7f8-....serial` -> `1.0.0_SA_CTO`.
- **Watcher: CONFIRMED live, NOT re-armed.** Found a running `inbox-watch.sh 1.0.0_SA_CTO stream`
  (pid 2728971). The orphan rule says a fresh session finding a match has found an orphan and should
  kill it. Applied the PID/consumer discriminator instead: `TaskOutput(bj6fzko31)` -> `running`, and
  its output file was still taking deliveries 15 min prior (last `[INBOX]` 131737Z). This was a
  CONTEXT-CLEAR, not a new session. Killing it would have gone deaf while every probe read REACHABLE.
  Third recorded instance of that false-positive class; the discriminator that works is "whose PID",
  not "do I remember arming it".
- A.3 PATH check: 93/93 resolve, EXERCISE half passed.

## FINDING 1 — two fire-owners were DEAD at startup

`0.7.0_AE_CloudOps~A` and `0.4.0_DS_ClientPlatform` (base) both read NOT REGISTERED. Verified two
ways (`get_live_agents` 7 live, neither present; `get_agent_status` explicit). AE~A was the sole owner
of the 15:15Z no-regen check, the 16:15Z publisher check, the entire post-17:15Z apply wave, AND an
OPEN deploy ledger (`20260729T0345Z_non-model-assets-json-full-retirement`). Its last traffic was the
10:45Z clock report.

- Spawn requested at MSTR 132959Z with full owned-queue as first-message direction. AE~A LIVE at
  PID 15376 by ~1337Z (<6 min turnaround). DS base respawned itself ~1337Z.
- DS~A asked to absorb the 15:00Z chain read as fallback; absorbed in 4 min with a clean capacity
  answer, then handed back when base returned (ruled Option 1, 134254Z).
- **Mechanism gap recorded (COO's framing, adopted):** NEVER#6's unclosed-ledger alarm keys on
  session END; a session that STOPS never reaches its own alarm. Belongs in the ledger state machine,
  not a watcher. Building nothing for it (moratorium + routes-before-monitoring both stand).

## FINDING 2 — AE~A's AccessDenied was a WRONG BUCKET NAME, not a missing grant

AE~A honestly reported it could not verify the staged 4c zip: AccessDenied on target AND on its
positive control, correctly reported as an unverifiable rather than a negative.

Measured here in SEPARATE invocations:
- `aws s3api list-buckets --query "Buckets[?contains(Name,'asset')].Name"` -> `opal-data-assets` (only)
- `aws s3 ls s3://opal-data-assets/` -> lists fine
- `aws s3 ls s3://opal-assets/` -> AccessDenied (its exact symptom)

Its control held the BUCKET NAME fixed while varying key count, so it shared the failure mode with
the target and failed identically. **A control that fails for the same reason as the target is the
target run twice.** S3 returns AccessDenied for both "cannot list" and "not yours" — byte-identical.
Ruled the re-verify happen in the quiet window rather than at the leg: P1/P2/P5 all read that bucket,
so the blindness would have stalled the wave, not one leg.

## FINDING 3 — P3 has a LIVE instance, and leg (d)'s NAME encoded the hazard

COO pre-committed a 5-clause acceptance predicate for the twin-deletion leg (accepted whole,
unamended). Its P3: deleting an object version DESTROYS data; deleting a DELETE MARKER RESURRECTS the
object — opposite effects behind one phrase, and the resurrection direction reports SUCCESS.

AE~A then found a live instance while probing read-only:
- `json/portfolios/non_model_assets.json` — DeleteMarker `pWisyjN7J1yefr_dk9Ow.nszyab69X7g` IsLatest
  @03:49:16Z, ZERO live object versions, **9 noncurrent restorable**
- `json/portfolios/non_model_assets_preview.json` — DeleteMarker `zh1iM5PlJZI6E1M4fOr78UyROzq2zK0Y`
  @03:49:18Z, 1 restorable

Andrew's own retirement order is held by ONE marker per key with real content intact underneath. And
leg (d) was titled "twin objects + delete markers" — which parses at speed as "remove the objects AND
the markers", half of which is the exact inverse of intent. **I authored that name, including in the
message that handed AE~A the P3 clause warning about it.**

Actions:
- Leg RENAMED: `(d) SUPPRESS-FROM-SERVING` — delete the OBJECT (which creates a marker); deleting a
  delete marker is PROHIBITED; keys already showing a marker as latest are DONE, skip and report.
- **BLANKET prohibition, wave-wide:** no delete marker removed anywhere tonight, any bucket, any
  reason. Stop-and-escalate if a leg appears to need one. COO adopted this over its own narrower clause.
- P4 reversibility upgraded from claimed to MEASURED (9 and 1 restorable, dated markers).
- 15:15Z semantics settled before the fact: 404-because-marker-is-latest IS the pass; surviving
  noncurrent versions are NOT a partial failure; a LIVE object version is the FAIL branch.

## FINDING 4 — the 15:00Z leg has NO SCHEDULE (COO, re-derived on the live primitive)

`describe-rule mdpf-daily-refresh-trigger`: ScheduleExpression ABSENT; EventPattern aws.s3 on
`opal-data-inf/gold/meta/pipeline-complete.json`; ENABLED. The other three clocks are real crons
(45 15 / 15 16 / 15 17). **The pass and the defect produce the same observation** — only reading the
trigger discriminates. This is CLAUDE.md's own named instance (07-18 six-day freeze), still live.

- CVO warned before it began certifying. CVO was already ahead and went HARDER: PIN-4(i) was ruled
  BEFORE evidence (ScheduleExpression None = automatic D2 fail for that stage), so the chain leg
  FAILS D2-as-scheduled rather than being "worded narrowly".
- **RULED: PIN-4(i) STANDS. Certify to the pin — D2 PARTIAL (3/4 scheduled + chain event-path
  exercised), cron floor as named discharge.** My own "narrow the claim" instruction was WEAKER than
  the pinned criterion; softening a pre-settled pin after a clean run is the vacuity pins exist to
  prevent. The pin binds me too.
- CVO's PIN-4(iii) closes COO's "no acceptance step reads the trigger" gap for free: the chain's own
  log line carries source `aws.s3` not `aws.events`, so the run self-identifies as event-fired.
- Cron floor APPROVED IN PRINCIPLE (COO design: additive, same Lambda, no-op by construction because
  the Lambda already gates on per-source vintage). **It is a SCHEDULE, not a monitor — moratorium does
  not bite.** Build post-fires, normal gates, COO co-sign.

## The model-leg oracle — settled by anchor-free double derivation

DS~A surfaced that the 3-partition numbers were SUPERSEDED-INPUT (backfill landed 6 partitions).
Ruled them retired as oracle. Then required base to re-derive and ~A to diff, **anchor-free** — I
withheld ~A's numbers from base deliberately so base's work was a derivation, not a confirmation.

- Raw input layer: **6/6 identical to the cent** across two independent parquet reads.
- Derived expectations DISAGREED materially. Resolved on an exact tie:
  `126,369,737.47 - 1,246,019.40 = 125,123,718.07` == deployed code's `model_aua_last_non_null`.
  Base mirrored `_dim_by_value_date` (the dim READER) and stopped one layer above the artifact; the
  slice routes Opal-Income to non-model (G8) BEFORE emitting model_aua. **Ruled to ~A's axis.**
- Count ruled 50/450 = 6 measured + 44 composed-labeled (05-28..07-17), derived TWICE by different
  methods (base from the compose rule in source, ~A from a dry-run line).
- **Base's F3 would have FALSE-FAILED**: 124,376,009.73 is the stale signature at 07-21/07-22 and the
  CORRECT value at 07-20. Same number, opposite verdicts, distinguished only by date. Re-stated
  date-qualified.
- **F5 exists only because they disagreed**: artifact stating UNROUTED numbers = a G8 routing
  regression, which would have graded GREEN against base's set. Base's md5 check (deployed slice ==
  HEAD == `68539df870f6039f54445da35436bd30`) excludes "an older slice was deployed" as an alternative.
- F1/F6 proven mutually INDEPENDENT (first_measured = min(covered) = 07-20 predates the backfill, which
  only added dates above it). First time we have checked a falsifier set for coupling.
- Single system of record: my 135339Z / 135415Z message. Six named failure signatures, all pre-fire.

Also closed: base's R5 in-place-overwrite concern — it was base's OWN predecessor's 051021Z run map,
AE-executed, closure report sitting unread in base's inbox. NOT a violation. R5-as-written still needs
a post-fires ruling: **the additive-only path fails by passing** (07-28 would have kept value_date
07-24, collided at equal dollars, resolved silently, built GREEN and NOT healed).

## ANDREW-DIRECT, VERBATIM (CTO terminal, ~140830Z, answering /open-calls)

> "GOing down the line of the carried calls: June ETFS_AVGCAP (b) there is nothing to disclose, we
> handled it via an ad hoc run so its a moot point. Client count need more information. ADVI_TWR 1
> and 2, yeah we're definitely doing it ourselves, we don't need to 'license' a calendar day TWR that
> is not intellectual property."

- **AVGCAP June disclosure: CLOSED (b).** Scope = the DISCLOSURE question only. Self-assigned check
  (my lane, not a re-litigation): confirm the corrected June basis reached the SERVED artifact, since
  our own law says ad-hoc artifacts are never production evidence.
- **ADVI_TWR D2: CLOSED — build in-house, licensing off the table.** D1 (Account365 as return source)
  is a DIFFERENT axis and is NOT ruled; CRO told not to let a spec proceed on an assumed D1.
- **Client count: HELD** pending information, delivered same turn (7,597 = artifact field / distinct
  clients, which is what the bell curve plots; 7,780 = +183 blend counts under the 2026-06-05
  sleeve-level ruling). Shipped state unchanged meanwhile.

Surfaced to Andrew same turn (COO's catch, correctly): "retired = not served, not destroyed" NARROWS
his ~0336Z verbatim ("get rid of that non_model_assets.json"). Nine restorable versions exist. Awaiting
his word on purge-after-wave; reversibility held through the wave regardless.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | `"how do I grep the repo"` (the XXX.md A.3 EXERCISE predicate, verbatim) | PASS | forwarder RAN, produced its own banner |
| `comp-which` | `--help` / `"smoke"` / real question | PASS (as controls) | reproduced COO's rc=1 vs rc=0 both directions; confirmed the A.3 fix in-tree is correct |
| raw `aws s3api list-buckets` / `s3 ls` | bucket-name discrimination, separate invocations | PASS | **rail-appropriate:** comp-iam/comp-aws model DESIRED-from-TF and structurally cannot answer "does this bucket exist in the account". Rule 22a requires the live primitive for an APPLIED claim. |

**What worked:** running the positive and negative controls as SEPARATE invocations is what
discriminated wrong-bucket-name from missing-grant; a same-bucket control could not.
**What failed:** nothing this window.
**Gap found:** none new — but note comp-* could not have answered Finding 2; bucket EXISTENCE is an
account-plane fact no TF-modeled tool covers.

## MCP traffic

~24 messages handled, 14 dispatched. Significant: spawn request -> MSTR (AE~A recovered); chain-read
handback ruling to DS base/~A; superseded-oracle ruling; the settled oracle (system of record);
leg-(d) rename + blanket delete-marker prohibition (COO co-sign travelled); PIN-4(i) STANDS to CVO;
Andrew verbatim broadcast to COO + CRO.

## Blockers

None of mine. All holds are time-gated owned checks (15:00Z / 15:15Z / 15:45Z / 16:15Z / 17:15Z),
not blocks.

## Current State

- Fabric: 8 live (MSTR, DT, DE, DS base, DS~A, AE~A, COO, CVO). CRO not registered.
- Deploy freeze HOLDS to post-17:15Z. Nothing applied/deleted/promoted this window.
- Model-leg oracle of record = CTO 135339Z (six failure signatures F1-F6, two proven independent).
- Leg (d) = SUPPRESS-FROM-SERVING; delete-marker deletion PROHIBITED wave-wide, both co-signs behind it.
- D2 will certify PARTIAL per PIN-4(i); cron floor approved-in-principle as the discharge.
- Open at me: retirement pair (32e953198a + ca3739c2fc) and WI-2 aum-metrics deploy words, both gated
  on the 16:15Z publisher read proving the accrual bridge.
- Open at Andrew: client count (info delivered), ADVI_TWR D1, purge-vs-suppress on non_model_assets.
- Carried, post-fires: R5 scope ruling; git-author-override-audit.log custody (track narrowly +
  merge=union same commit, reconstruct before tracking, never `>` the live file); AVGCAP served-artifact
  check; MSTR's staged A.3/forwarder law edit still uncommitted in the shared index.

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** 15:00Z chain read against CTO 135339Z; or the 15:30Z no-output alarm.
2. **[0.7.0_AE_CloudOps~A]** 15:15Z no-regen -> close ledger 20260729T0345Z; 16:15Z publisher read to
   CTO immediately (gates two deploy words); then the seven-leg wave.
3. **[0.4.0_DS_ClientPlatform~A]** penny read at the 15:45Z accrual landing, artifact's STATED total.
4. **[3.0.0_SA_CVO]** certify D1-D4 to the pins; D2 PARTIAL, chain leg event-path claim only.
5. **[1.0.0_SA_CTO]** deploy words post-16:15Z; shepherd the wave; ~20:30Z cot first ET-anchored fire;
   author D-I certification tomorrow off the zero-hands fires, with the session-boundary context-loss
   residual named (three instances today).
6. **[0.0.0_AB_MSTR]** land the staged A.3/forwarder edit under its own author line.
