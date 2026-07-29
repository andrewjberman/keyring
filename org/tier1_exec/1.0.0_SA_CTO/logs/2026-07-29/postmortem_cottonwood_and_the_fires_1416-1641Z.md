# CTO POSTMORTEM — the fires, the cottonwood arc, and five errors of mine (1416-1641Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE

Written at Andrew's instruction ("/log this postmortem"). Postmortem shape: what happened, what I got
wrong, what caught it, and what the estate should keep. My own errors lead because they are the most
useful content in the window.

Window: 1416Z (prior log @741d336281) -> 1641Z. Commits authored by me: ONE (`d73b6bc4cd`, a chore).
Everything else was rulings and dispatch. Deploy freeze held throughout; nothing applied.

---

## 1. THE FIRES — all three produced real evidence, none of it the expected kind

| clock | outcome |
|---|---|
| chain (event-driven) | FIRED 15:02:30Z. Stage 6 **REFUSED TO WRITE** — correctly. Cottonwood leg un-composed; folding it would have silently dropped 31 dates of sanctioned history. No-output = the guard succeeding. |
| 15:45Z accrual | FIRED unattended, then **CRASHED** on a missing IAM grant (runner lacks PutObject on `opal-data-assets/portal/gold/mdpf/*`). Dispatcher printed OK — that is the DISPATCH rc, not the RUN rc. |
| 16:15Z publisher | FIRED 16:15:31-32Z, wrote **all four firms** incl. cottonwood, canonical hyphenated names. Republished unchanged vintages because the bridge above is blocked. D2 16:15Z leg CLOSED. |
| 17:15Z emitter | **HAS NOT FIRED** as of this writing (16:41Z). See error 5. |

D2 verdict stands as pinned pre-evidence: **PARTIAL** — 3/4 legs scheduled, chain leg fails
D2-as-scheduled per PIN-4(i). A scheduled leg that fires and crashes is MORE informative than no
schedule: it proved trigger, dispatch and runner path, and isolated the failure to one grant.

## 2. MY ERRORS — five, all caught before cost, none caught by me

**(a) I asked a lane to fabricate a balance.** Compared coverage counts (interpolated artifact
non_model 47 dates vs compose output 6) and ordered the compose extended. `non_model_aua` is a DERIVED
BALANCE (`custody - model`), underivable where custody is absent. A W-2b identity gate already fails
the build on exactly the shape I ordered. Following it would have tripped that gate or laundered a
~$334mm interpolated quantity a set-equality proof measured as never having participated.
*Caught by 0.4.0_DS_ClientPlatform~A, with source citations, refusing the instruction.*

**(b) I asked for an artifact Andrew had retired nine hours earlier.** Directed DS~A toward producing
`cottonwood/non-model-assets.json` because global had one and cottonwood did not.
`non_model_assets.json` was retired ESTATE-WIDE by Andrew-direct ~0340Z; the page has no legacy fetch
left for it. Global's 81,931 B copy is a corpse of the retired plane.
*Caught by 0.4.0_DE_ClientPlatform, which read the prior art before designing, as instructed.*

**(c) I built a structural claim on `aws s3 ls` LOCAL time.** Asserted "every cottonwood object is
stale at 2026-07-28T20:35:22Z; nothing wrote cottonwood today; the working writer skips cottonwood."
Host is UTC-4. `2026-07-28 20:35:22` local IS `2026-07-29T00:35:22Z`; `head-object` shows the real
write at `Wed, 29 Jul 2026 16:15:32 GMT`. Four hours, crossing midnight into a whole-day error, turned
into a false structural claim that sent two lanes hunting an exclusion that does not exist.
**Our own memory names this instrument as banned:**
`feedback_aws_s3_ls_lastmodified_is_local_time_never_a_liveness_oracle`.
*Caught by DS~A, because its "stale" stamp and its own `date -u` disagreed by exactly 4h and it chased
the discrepancy instead of accepting the number.*

**(d) Routing churn: three ownership changes on one ad-hoc run in 25 minutes.** Named DS~A, switched
to AE base on a CAPABILITY read ("who holds the runner"), then Andrew named DS. The error was
reassigning a lane on capability when the lane is a matter of DOCTRINE (Rule 13: DS owns gold producer
scripts) and ultimately sovereign preference. Capability is a tiebreak between agents who both own a
thing; it is not grounds to move a lane. Cost: two context-switches for AE base, which had held
correctly throughout. Also briefly created a genuine double-fire risk — two agents each holding a
"you fire" from me.

**(e) I asserted a fire that had not occurred.** Told DS~A at 163338Z "the 17:15Z emitter has fired."
It had not; it was 16:33Z. I conflated the fire that had just landed (16:15Z publisher) with the next
on the list. Same shape as the falsifier premise DS base caught this morning. Had it stood, an agent
could reasonably conclude 4c's once-only "before" half was spent and stop protecting it — the exact
hazard the freeze exists for. *Caught by me, 8 minutes later, on a clock read.*

**THE COMMON SHAPE IN (a), (b), (c):** I reasoned from an ABSENCE or a COVERAGE GAP without
establishing what the thing IS, whether it should exist, or whether my instrument could see it.
**An absence is not evidence of a defect until you know the thing was supposed to be there.**
Three instances, one page, ninety minutes.

## 3. THE DEFECT IN MY OWN ORACLE — all six falsifiers presumed a write

F1-F6 (my 135339Z, the settled model-leg oracle) share one unstated premise: **that a write occurred.**
On the no-write the chain actually produced, the scorer returns F1+F3 tripped, 2/450 covered — reading
as a CATASTROPHIC backfill failure and naming the wrong culprit (the dim backfill, which landed
correctly). DS base ran it, recognised it was measuring the pre-fire artifact it had itself baselined
an hour earlier, and refused to report the verdict.

**ADOPTED: no failure signature is assertable unless the artifact's ETag/LM has MOVED. The write is the
precondition of the entire falsifier set. No write = UNGRADED, not FAILED.**

Second instance of the same class in one day — F4's premise was "a fire occurred", F1/F2/F3/F5/F6's is
"a write occurred". Both premises were mine and unstated.

## 4. THE COTTONWOOD ARC — root-caused, and smaller than it looked

**Root cause, byte-proven:** the interpolated backfill was built AND SERVED on 07-23 to the LEGACY
plane. `json/mdpf/cottonwood/aggregate-aua-timeseries.json` md5 `194e5bb05c4523abb2cc05988f53005f`
87,262 B == the gold interpolated artifact, byte-identical. The portal then re-pointed legacy ->
platinum, and platinum's cottonwood slice is a different object (md5 `0ec286f2...`, 37,518 B, model
2/450). **Nothing was clobbered — a plane migration left the payload behind.** The producer's own
docstring anticipated it: *"WRITES (staged ONLY; served publish is a separate co-signed step)"*. That
step ran once, to the old plane, and was never re-established.

**Andrew's zombie-writer hypothesis: REFUTED for cottonwood** (`comp-clobber --live`: 4 versions, 4
distinct etags, ACTIVE_CLOBBER=False, no interleaving — one faithful writer copying a thin source).
**CONFIRMED elsewhere:** 3 live interleaved clobbers on the legacy plane (49f + inflection
aggregate-aua-timeseries, json/portfolios/aum-timeseries) + 11 repo multi-writer sinks. Routed to COO.

**Non-model: closed, both sides correct.** Cottonwood's artifact declares
`non_model_aua_status: "NOT_MEASURED (Rebalancer carries model assignment only)"` — an honest
declaration about its source. The other three scopes carry `non_model_aua` fully populated (426-432
dates) in the SAME artifact; no separate non-model file exists anywhere in the working path. DE
confirmed the render already field-reads it and treats zero-pre-backfill as correct. **Andrew ruled
~1724Z: server-side.** Producer computes and states; nothing derives in the browser.

**The finding with the longest reach — run ordering, not a bug:**
```
producer read at        2026-07-29T00:33:22Z
source partition landed 2026-07-29T03:30:38Z    (2h57m LATER)
```
38-object census: cottonwood silver lands daily ~03:30Z; the chain runs ~00:33Z. **~3 hours early,
every day, by construction.** The producer was never wrong — at generation time 07-24 genuinely was
the latest partition. Cottonwood is systematically one trading day staler than data we already hold.
DS base corrected its own earlier fix-shape-2 call off this: **the mixed-basis objection largely
dissolves via RUN ORDERING, not a basis rule.** The cheap fix is scheduling; the expensive design
question may not need answering.

**Net remaining work: one IAM grant + one label fix + conformance. NO modified publisher, and
therefore NO interim deviation to record** — Andrew offered to accept a cottonwood-special interim
script; we do not need one. Unbuilt is the best outcome.

## 5. THE THING ANDREW FORCED, AND IT IS THE MOST VALUABLE RESULT OF THE DAY

His challenge: *why are we making all these failure classes without testing whether the producer gets
the right data.* Fair, and the answer was that every check we had tested INTERNAL CONSISTENCY — the
oracle was derived from the same dim partitions the producer reads, so wrong inputs would pass all six
falsifiers identically. Cottonwood's absence proved it: an entire firm missing from a client-facing
total, and NOT ONE falsifier could have caught it. He found it on his own screen.

Ordered a source-to-served reconciliation. Result:
- **AUM RECONCILES EXACTLY.** 16,825 raw custodial parquet rows -> `463,015,162.92` == served
  `partner_custody_total`, DELTA 0.00, read with pandas, no gold logic in the path. **The first
  independently established number of the day.** Decomposes exactly: model 125,132,212.03 +
  non_model 337,882,950.89.
- **COUNT LEG UNRECONCILED** — and DS base refused to force it. Its predicate returned 296 vs 292
  served; it identified its OWN predicate as the problem (45 strategy values, a whole Core|Satellite
  family its substring missed) and called landing within 4 a **coincidental near-miss, not a
  reproduction**. Marked UNRECONCILED rather than claim a tie it had not earned.
- **Cottonwood absent on FOUR series, not two** — count 292, aum 125,894,245.45, active 294,
  excl_unfunded 2 — each delta exactly cottonwood's own figure. A filter artifact cannot produce four
  series each tying to the cent on exactly two of three firms.
- A $762,033.42 gap between two client-facing "model" numbers is **NOT a defect** — declared in-band
  in the artifact's own meta (`sleeves_dropped`, 3 leaf hits, non-Opal sleeves excluded), to the cent.

## 6. INSTRUMENT FAILURES — three false absences in one afternoon, three different layers

| instrument | how it lied |
|---|---|
| `aws events list-rules` | structurally BLIND to EventBridge Scheduler — 11 live schedules invisible, incl. the 15:45Z accrual clock. Returns a clean confident list of half the estate. |
| `comp-trigger mdpf` | saw all 143 rules; the PREDICATE could only match names containing "mdpf". Then printed the 143-wide scan denominator beside a 1-wide search. |
| `aws s3 ls` (mine) | LOCAL time presented as UTC — 4h shift crossing midnight into a whole-day error. |

**RULE SHARPENED: print the PREDICATE, not just the denominator.** A denominator can be true, precise,
and about the wrong thing — 143 was what the tool WALKED, not what the predicate SELECTED. DS base's
line, about its own error, and it is better than the version we had.

**AND: what caught it was changing the AXIS of the search** (every rule with a 17:xx cron, regardless
of name), not running the same search harder.

Related, routed: COO escalated a P0 control whose failure text **recommends its own removal**
(`WARN: ... (runner json/mdpf/* grant?)` — the grant the deny exists to withhold). Different and worse
than a wrong signpost: it hands a 3am responder a correct-sounding instruction whose execution IS the
breach, and nothing errors when they comply. **A control whose failure text recommends its own removal
is not a control with a documentation gap; it is a control with a countdown.**

Andrew-direct ~1645Z: `pipescript` -> `comp-opalbizsem`, built-in refresh, source-timestamp head.
Motivating incident: a 44-day frozen resolver serving a stale artifact as "primary served rollup LIVE
fresh." **I generalised the header to a comp-tool-wide contract** — a vintage header does not prevent
staleness, it makes staleness unmissable at the point of reading, and unlike a refresh function it
cannot itself go stale.

## 7. WHAT WORKED — worth recording, because it is why nothing landed wrong

- **Guards refused, correctly, three times:** Stage 6 refused rather than drop 31 dates; the IAM deny
  held the retirement every run; the W-2b identity gate would have caught my fabricated balance.
- **Lanes refused CTO instructions with source and were right** — twice (DS~A on the balance, DE on
  the retired artifact). Neither cost time because both were caught before building.
- **AE~A found a LIVE instance of COO's P3 hazard nobody asked for** — Andrew's retired
  `non_model_assets.json` held by ONE delete marker with 9 restorable versions underneath; removing
  the marker republishes a client-facing artifact and reports success. Leg (d) renamed
  SUPPRESS-FROM-SERVING; wave-wide no-delete-marker prohibition.
- **Anchor-free double derivation** produced F5 (the G8 routing regression tripwire), which exists
  ONLY because two agents derived separately and disagreed.
- **Cross-device SQS round trip closed both directions** by agent-side ACK, not queue depth.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-clobber --sweep` | opal-data-portal-v2 platinum/mdpf/cottonwood; json/mdpf; json/portfolios | PASS | 0 / 2 / 1 actively clobbered — refuted the cottonwood hypothesis, confirmed 3 legacy-plane zombies |
| `comp-clobber --live` | cottonwood + global aggregate-aua-timeseries | PASS | 4 versions, 4 etags, no interleaving — one faithful writer; also caught the 16:15:32Z publisher fire |
| `comp-clobber scan` | `--min-writers 2`, then `--include-partitioned` | PARTIAL | 11 multi-writer sinks of 111; MDPF writers NOT surfaced (dynamically constructed) — the live oracle was required |
| raw `aws s3api head-object` / `s3 cp` | artifact-by-artifact comparison, 4 scopes | PASS | **rail-appropriate**: byte/md5 identity and per-series coverage are not questions any comp tool answers |

**What worked:** `comp-clobber --live` is the discriminating instrument — the static scan could not see
the MDPF writers at all, and the tool says so in its own output ("STATIC = a code CANDIDATE. The ORACLE
is runtime").
**What failed:** my own use of `aws s3 ls` as a liveness oracle (error c).
**Gap found:** `comp-clobber scan` does not surface dynamically-constructed write sinks even with
`--include-partitioned`; the MDPF publisher/bridge writers are invisible to it. Routed as an
observation, not a TO.

## MCP traffic

~55 messages handled this window. Significant: ad-hoc run GO + 2 ownership corrections; 4c ownership
ruled to AE~A; IAM fix-forward ruled (do NOT race the publisher); leg (d) gated on (c)
applied-plane-dead; audit-archive unwedge adjudicated; zombie-path census routed to COO;
`comp-opalbizsem` ratified + header generalised; cottonwood design brief + 3 retractions of it;
Andrew verbatims recorded x4 (server-side non-model, run-the-producer-properly, zombie paths,
comp-opalbizsem).

## Blockers

None of mine. All holds are time-gated or owned checks. The retirement-pair and WI-2 deploy words
remain HELD pending the frozen-file consumer census (aum-timeseries.json) — an owned open question,
not a block.

## Current State

- Freeze HOLDS to post-17:15Z. **17:15Z emitter has NOT fired** (16:41Z at writing). Nothing applied,
  deleted, or promoted this window.
- Fabric: 8 live. DS~A respawned 152355Z (4th session-edge loss today); DE live since 154626Z.
- Cottonwood: root-caused; remaining = 1 IAM grant (AE~A, ruled 155914Z) + label fix (44 dates
  asserting `interpolated_estimate` over None) + conformance. Design @bf8cb273f9 (DS~A lane),
  DE design @d6587e2951.
- Oracle of record: CTO 135339Z + the write-precondition amendment (§3).
- Leg (d) = SUPPRESS-FROM-SERVING, gated on (c) verified dead on the APPLIED plane; wave-wide
  delete-marker prohibition, both co-signs behind it.
- D2 certifies PARTIAL per PIN-4(i); cron floor approved in principle — note `scheduled-floor.tf`
  ALREADY EXISTS ("BUILT AND VERIFIED, NOT LANDED"), so it is a landing decision, not a build.
- Andrew rulings this window: AVGCAP disclosure closed (b); ADVI_TWR build in-house (D1 still open);
  client count HELD; non-model server-side; run the producer properly (DS); kill zombie paths;
  `comp-opalbizsem` + refresh + vintage header.

## Next Steps

1. **[0.7.0_AE_CloudOps~A]** IAM grant (full `portal/gold/mdpf/*` write set, not the traceback key),
   plan-before-apply, do NOT race the publisher; then re-fire the bridge; then the 7-leg wave
   post-17:15Z.
2. **[0.4.0_DS_ClientPlatform]** finish the source-to-served reconciliation — close the COUNT leg with
   the canonical crosswalk applied, or report it unreconciled with the predicate stated.
3. **[0.4.0_DS_ClientPlatform~A]** label fix; server-side non-model leg with the FIRM-SEPARATION STOP
   CONDITION intact; explain 6-vs-38.
4. **[0.4.0_DE_ClientPlatform]** provenance rendering against corrected labels; axis recommendation;
   re-push 72f132c5 with the anchored SURFACE_ACK.
5. **[2.0.0_SA_COO]** zombie-path retirement scoped into the teardown wave (legacy-plane clobbers
   first; VERIFY FIRM SEPARATION before touching any `platinum/firm/*`).
6. **[1.0.0_SA_CTO]** D-I certification tomorrow off the zero-hands fires, carrying: the write-
   precondition amendment, the session-boundary context-loss residual (4 instances today), and the
   methodological residual that today's schedule conclusion was re-grounded on a wider instrument
   after the fact.
