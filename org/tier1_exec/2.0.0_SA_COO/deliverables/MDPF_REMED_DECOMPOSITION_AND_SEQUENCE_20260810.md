# MDPF trigger/schedule remediation — DECOMPOSITION + SEQUENCE

> ## ⛔⛔ ADDENDUM 6 — 2026-08-10 ~1755Z. **"CAUSALLY INERT" IS WITHDRAWN. THE ORDERING MECHANISM IS LIVE.**
>
> **EVERY EARLIER STATEMENT IN THIS DOCUMENT THAT THE FOUR-INTAKES MEASUREMENT IS "CAUSALLY INERT"
> (§H, Addendum 2, Addendum 3, the session logs) IS STRUCK.** `1.0.0_SA_CTO` ruled the mechanism
> **LIVE** and corrected their own 1550Z stand-down. **Right about PUNCTUALITY, wrong about ORDERING:
> the floor is NOT LATE — it is 40 MINUTES EARLY RELATIVE TO ITS OWN AXIS SOURCE.**
> Not *"the data is too old"* but **"the floor picks the axis BEFORE the axis source lands."**
>
> **R · WHY THE ORDERING IS DECISIVE RATHER THAN INCIDENTAL — source-verified by CTO, who declined to
> rule on a relayed quote:** `:833` `frontier = aum_days[-1]` over the **latest partition present at
> read time**; `:589` *"Middle published-only gaps stay honest-None… **ONLY the frontier is set**."*
> ⇒ **THE COUNT IS STAMPED ONLY AT THE FRONTIER, so a count/value disagreement can ONLY occur AT THE
> FRONTIER.** The gap does not merely shift a date — **it chooses WHICH date carries the only count in
> the series.** Three conditions coincide, and removing any one kills it: **(a)** floor 13:00Z vs
> SmartX ~13:40Z ⇒ reads yesterday's partition daily · **(b)** it is a **MONDAY** ⇒ yesterday's is
> **Sunday's**, carrying **Thursday 08-06** · **(c)** inflection has a genuine hole at **exactly**
> 08-06. *(08-07 passed because the frontier was then 08-05, which inflection has.)*
>
> **S · THE REMEDY SPLITS, AND ONLY ONE HALF SELF-HEALS.**
> | half | state |
> |---|---|
> | **1 · THE GATE FAILURE** | **PREDICTED to SELF-HEAL on Tuesday's scheduled cycle, at ZERO COST** — it reads `date=2026-08-10` (day-max **08-07**), which inflection HAS on both legs; and 08-06 stops being the frontier so it takes no count. **All seven disagreements resolve.** ⛔ **A prediction that measures itself in ~20 hours for free is NOT converted into a request that Andrew revisit a ruling.** *(PREDICTION, carrying AE's fence: other limbs could refuse.)* |
> | **2 · A PERMANENT ONE-TRADING-DAY LAG** | **DOES NOT self-heal.** Tuesday's floor reads Monday's partition (day-max 08-07) while **Tuesday's own carries 08-10** ⇒ **the floor serves D-2 when D-1 is available, EVERY DAY.** **The weekend is why it BROKE; the ordering is why it is ALWAYS A DAY SHORT.** |
> >> **HALF 2 IS EXACTLY WHAT ANDREW OBSERVED THIS MORNING** — *"All of them should be on August 7th at
> > this point."* **He was right, and the 40-minute gap is why they are not.** The gate failure is the
> > loud symptom; **the one-day lag is the thing he actually noticed, and it survives the self-heal.**
> ⛔ **DO NOT PRESENT "MOVE THE FLOOR LATER" AS THE FIX.** The remedy space is **wider than the floor's
> clock** (read the axis source from the day's own partition; derive the frontier differently), and
> framing it as a floor-move **narrows his options to the one he already declined at (B).** CTO holds
> half 2 at his terminal; **nothing is owed upward from this seat.**
>
> **T · 49F's "PASS" IS NOT A BILL OF HEALTH — struck at BOTH seats.** Limb **(v)** — *the exact limb
> that fails inflection* — is **SKIPPED** for 49financial (`:1562-1567`), and the log says so:
> *"RETAINED STRUCTURAL EXPOSURE… not a clean result."* **I used the 440-date PASS as a control in my
> sequencing and CTO quoted it as a clean control in the diagnosis. Same error, both seats, struck in
> both.** Also live: CONFLICT-not-overwritten on three 49F objects; `L-1 key-set assertion DEFERRED`.
>
> **U · A FALSE OUTAGE WAS CALLED AND SELF-CAUGHT — the control WORKING, recorded as such.** AE
> reported 49F's axis feed *"stopped advancing 2026-08-06."* **FALSE: 08-08/08-09 are a SATURDAY and a
> SUNDAY**, and row counts **GROW** across the window (4398 → 4422) — *a frozen feed does not add rows.*
> **CLAUDE.md's FIRST never-rule names this exact scenario.** AE **had already computed 08-09=Sunday
> hours earlier, held the fact, and did not apply it** — *what was missing was the CALENDAR FRAME, not
> a measurement.* **Self-caught and unwound before it propagated; I never carried it onward.** ⚠ **CTO
> owns the amplification** — they called it the best-grounded fact of the day and put it in front of
> Andrew. *Recorded because a self-caught false outage is the control succeeding, and burying it would
> teach the opposite of what today taught.*

> ## ⚠ ADDENDUM 5 — 2026-08-10 ~1700Z. **PRIORITY RESET BY ANDREW; ONE DECLARED GAP WITH A NAMED OWNER.**
>
> **N · ANDREW-DIRECT ×3 (~1620Z) — THE REPAIR IS THE MAIN FABRIC PRIORITY.** Record @5b14d993f2,
> amended @85fb09dddd. *"first and foremost"* → *"ahead of ANY Cottonwood work"* → *"the main fabric
> priority."* The Cottonwood model pull is **sequenced behind repair COMPLETION**, must be **properly
> scoped and REGISTERED AS A PROJECT**, scope **"purely backend and scheduling initially"**, basis =
> `BRIEF_COTTONWOOD_OPAL_CONSTITUENT_ATTRIBUTION_20260807.md` (`~Z`, @924c3b669a) — **confirmed by
> Andrew directly**, not inferred from filenames. Then ~1650Z, ordering *within* the repair:
> **08-06 mechanism FIRST**, with Inflection-ingestion offered as **his prior belief, not an assertion.**
> ⚠ **TWO COTTONWOODS, OPPOSITE SIDES OF THE LINE:** the **model pull** is deprioritised; the
> **cottonwood slice build refusing inside the floor** is one of the four scopes **OF** the repair and is
> therefore main priority. *A reader resolving "Cottonwood work is behind the repair" against the second
> parks exactly what he put first.*
> ⚠ **"Registered as a project" is likely a SPLIT, not a new record** — the pull is currently one half of
> `MDPF_SLICES`. **Put to Andrew; not minted, to avoid a duplicate beside an existing project.**
>
> **O · SWEEP 3 — AUTHORISED IN PRINCIPLE, NOT STAFFED, OWNER NAMED, TRIGGER NAMED (CTO, 1700Z).**
> I put it to CTO rather than commissioning it: cross-program, and findings land on owners not in this
> room. Ruled in three parts, and the middle one expires differently from the first:
> | | |
> |---|---|
> | **CAPACITY** *(expires soon)* | Andrew ordered 08-06 first; AE is the only free seat and is on it. **No second seat is manufactured by pulling AE off the stated top priority to sweep documents.** |
> | **OWNERSHIP** *(does not expire)* | **INF is going to the site-Z fabric.** A sweep of INF's own docs run from here produces findings for a program whose seats are elsewhere. **Not a gap in our coverage — correctly outside it.** The **cot** half is genuinely ours. |
> | **RECORD** | **DECLARED, OWNER-VISIBLE GAP.** Owner: **this seat (cot half)** · **site-Z CTO (INF half**, to ride the MSTR ferry brief rather than be discovered there later**)**. **TRIGGER: the 08-06 mechanism closes.** |
> ⛔ **WHY IT IS NOT A BARE YES, and this is the load-bearing half: A SWEEP AUTHORISED WITH NO SEAT AND NO
> TRIGGER READS AS COVERED IN EVERY SUBSEQUENT STATUS.** AE declared the boundary precisely so it would
> **not** be inherited as coverage; authorising a sweep nobody runs would re-inherit it under a
> better-sounding label. **A declared gap without an owner is a nicer word for dropped.**
>
> **P · SWEEP-2 FINDING A WAS WORSE THAN REPORTED — landed @1f44450356.** The `MDPF_3FIRMS_PRD`
> "D+1 ~03:30Z" fiction was live at **FIVE** sites, not the three AE reported: `:474` **(twice)** and
> `:739` were uncounted — **and `:474` was carrying an "ON SCHEDULE" CERTIFICATION DERIVED FROM THE
> FICTION.** All five struck in place; the `:765` "resolved" claim withdrawn (the zero-overlap finding
> returns to **UNRESOLVED**, because the mechanism it was resolved to did not exist).
> > **THE LESSON, and it is recursive: A FINDING'S OWN SITE-COUNT IS A RETRIEVAL RESULT AND NEEDS ITS
> > DENOMINATOR LIKE ANY OTHER.** We spent the day printing denominators on estate scans and then
> > reported a defect's own citation count without one.
> ⛔ **AND THE DIRECTION OF THE ERROR IS THE DANGEROUS ONE: a leg believed D+1 when it is really D+2 makes
> a HEALTHY delivery look LATE BY A DAY — the false-outage class NEVER#1 exists to prevent, sitting inside
> a clause that CITES NEVER#1.**
>
> **Q · CTO'S CONSTRAINT ON THE 08-06 READ — the one most likely to dissolve the question.**
> *(i)+(ii)+(iii)* say 08-06 is **absent** from eclipse, orion, **and** orion custody history;
> *(iv)+(v)* say something put it **on the axis WITH counts**. **BOTH CANNOT BE COMPLETE.**
> ⇒ **THERE IS AN UNNAMED SOURCE CARRYING 08-06**, and finding it likely dissolves the question without
> needing any of the three standing hypotheses. AE holds it.
> *My own 08-06 lead was accepted as framed — **pattern change GROUNDED** (`ce99054e44` deleted
> `cron(30 3)Z`=03:30Z, created `cron(30 18)ET`=22:30Z, matching AE's independently measured old/new
> patterns exactly, coupled to inflection via the all-rows handler `:353`), **missing partition OPEN.**
> Separating those two after having written them as one sentence is what made it usable — and MSTR's
> challenge, correctly labelled UNVERIFIED-not-REFUTED, is what forced the separation.*

> ## ⚠ ADDENDUM 4 — 2026-08-10 ~1533Z. **CTO RULED. 49F GROUNDED. AND A LIVE PRD RULE IS NOW WRONG.**
>
> **I · BRONZE OWNERSHIP RULED (CTO):** `cot-rebalancer-runner` **owns** `blackdiamond/cottonwood/bronze/`
> — it writes daily and succeeds; the mirror's row has **never once completed** in the window.
> ⛔ **THE MIRROR'S GUARD IS NOT BROKEN AND MUST NOT BE "FIXED."** Its *assertion* is scoped to the whole
> prefix while its *writes* are scoped to its own rows. **Remedy = NARROW THE ASSERTION** — never widen an
> allowlist, never disable the guard, never make the error go away. *A guard that correctly detects a second
> writer is the only reason we know there is one; it said so for 14 days and was read as a broken function.*
> ⚠ The meta-templates row (`:153`) is a **different artifact**, has never run, and **must not be silently
> retired by the scoping fix.**
>
> **J · COTTONWOOD CAUSE: OPEN.** CTO **refuted their own attribution** (@9ddd6a4855 — the session trigger
> is an OIDC auth job) and **downgraded 49financial to UNVERIFIED unprompted**. Answering it needs, in order:
> **(a)** what data date the 06:00:44Z write *contains* (a mixed-vintage landing is already observed —
> `ALLOCATIONS_DAILY_2026-08-07` beside `REALIZED_DAILY_2026-08-09`); **(b)** what the floor actually reads
> for cottonwood. **Both are READS, not experiments, and either could dissolve the question.**
>
> **K · 49F: MY "PROVABLY" WAS NOT EARNED WHEN I WROTE IT.** I had the arithmetic and had **not** verified
> that the floor's 49F leg consumes SmartX output — the identical inferential step CTO downgraded themselves
> for. Withdrawn, then **grounded**: `:72` `SMARTX_SILVER="smartx/platform/silver"` → `:304`
> `_latest_date(f"{SMARTX_SILVER}/fact_model_aum_daily")` → `:259-263` returns `dates[-1]`, **the newest
> partition present AT READ TIME**. With SmartX silver landing 13:40–42Z (3/3 days), a floor at 13:00Z **or**
> 13:30Z reads the **prior** partition. ⇒ **the consumer lever cannot reach 49F without moving the bridge
> (13:40Z) and publisher (13:50Z) too — a chain re-architecture, not a retime.**
> ⚠ **L2 of that chain (that `mdpf-gold-lambda` runs this script) is CARRIED FROM CTO, not measured by me.**
> And this shows only that the lever *cannot reach* 49F — **not** that late SmartX is *why* it sits at 08-06.
> **CTO's UNVERIFIED downgrade stands.**
>
> **L · ANCHOR SWEEPS — 1 NARROW (zero), 2 WIDE (NOT empty).** Sweep 1 @487c857665: 5 pre-apply anchors,
> all already caught, zero new. **Sweep 2 @73c979df20** (24 files / 7,279 lines; 22 Class-2 candidates):
> - **FINDING A — `MDPF_3FIRMS_PRD` "HOLDINGS lands D+1 ~03:30Z" was NEVER TRUE.** Full retained history
>   n=47: write-hour histogram `02:xx=33 · 14:xx=7 · 20:xx=4`, and **03:xx OCCUPANCY = ZERO OF 47**; lag is
>   D+2 in steady state. It was **also** moved by the 08-06 apply. **BOTH DEFECT CLASSES ON ONE FIGURE** —
>   and it is **promoted to a MECHANISM at `:765`.** *A staleness-only sweep passes straight over it.*
> - **FINDING B — `MDPF_DEBTCLEAN_PRD:417` "every upstream channel lands by ~16:00Z" — MOVED.** True when
>   written; broken by the 08-06 apply. `cot forwardfill_v2` 20:31Z violates by ~4.5h, `eclipse` 22:31Z by
>   ~6.5h. ⛔ **AND THE NEXT SENTENCE TURNS IT INTO A RULE** — *"a schedule materially later than the last
>   channel's arrival is the only safe choice."* **THE PRD NOW INSTRUCTS A SCHEDULE INTO THE EXACT DEFECT
>   THIS WORKSTREAM EXISTS TO REMOVE — and it needs nobody to misremember, because it will be FOLLOWED
>   CORRECTLY AND STILL BE WRONG.** Routed to CTO as a live PRD input.
> > **METHOD, rated above either finding (AE):** **"A SPOT CHECK ANSWERS 'IS IT STILL X.' A DISTRIBUTION
> > ANSWERS 'WAS IT EVER X.' Only the second distinguishes the two classes."** ⇒ **Fence added: re-derive
> > from the FULL retained history where it is free — the current value CANNOT FALSIFY "it was never true."**
> **DECLARED GAP (not an oversight):** INF/cot's **own** documents were NOT swept. Cross-program; **put to
> CTO to authorise**, since findings there land on owners not in this room.
>
> **M · MY OWN RETIRED RECOMMENDATION:** I told AE CloudTrail data events were "the single discriminating
> test" for the 06:00Z producer. **Wrong — CloudTrail cannot attribute writes on `opal-data-assets`**
> (selectors cover `opal-data-bd/`+`opal-data-inf/`, and are **ReadOnly**). It would have returned nothing.
> The producer was named by **key-grammar partition**, free. *Recorded so nobody enables data events to
> answer this class.*

> ## ⚠ ADDENDUM 3 — 2026-08-10 ~1500Z. **COT CENSUS CLOSED: THE SCHEDULE IS ONE OF FOUR ENTRY POINTS.**
>
> Run at the COO seat (`comp-blast cot-bd-session-trigger`; canonical kuzu 20,616 nodes / 41,205 edges,
> built 2026-08-10T14:58:34Z, age 0.0h, **Nessie HEAD current, pin == marker** — provenance header read).
> **Closes the cot-consumer-census precondition from Addendum 2; taken off AE's queue, not added to it.**
>
> **DIRECT (depth-1) callers of `cot-bd-session-trigger` — FOUR:**
> `scheduler/cot-bd-session-daily-et` **[SCHEDULE — the only one a retime touches]** ·
> `events/rule/cot-bronze-complete` · `events/rule/cot-session-complete` · `events/rule/cot-silver-complete`
>
> **⇒ IT IS A MULTI-MODE, MULTI-ENTRY FUNCTION.** The Scheduler target passes
> `input = {"mode": "session-refresh"}` (`schedule-et.tf:94`) — the cron selects **one mode** of a function
> that three event rules also invoke on their own completion triggers.
> **A RETIME MOVES ONE ENTRY POINT OF A FOUR-ENTRY CHAIN; the event-driven siblings keep firing regardless.**
> ⚠ `cot-bronze-complete` and `cot-silver-complete` appear **both downstream and upstream** — a
> completion-event loop around one function. Not a defect on its face; **not a simple cron either.**
>
> **Downstream ≥22 nodes** — carrying comp-blast's own bound: it counts **EXTRACTED EDGES ONLY, a LOWER
> BOUND**, blind to dynamic/FUNC-key consumers. Includes SNS `opal-critical-surface-alerts` + SQS
> `opal-critical-surface-alerts-coo`, Lambda `opal-cot-served-guard`, both `blackdiamond/cot/*` secrets,
> and S3Key `blackdiamond/cot/session-trigger-mode.json` (a mode-state object in this chain — **not
> examined, NOT claimed as an R-20 sidecar**).
>
> ⛔ **A NUMBER DELIBERATELY NOT REPORTED: the caller chain prints 85, AND THE BLAST RADIUS IS NOT 85.**
> Depth-1 is the four above; the depth-3 tail (`opal-portal-fear-greed-fetcher`, `finbert-batch-processor`,
> `opal-news-ai-sentiment`, …) is **transitive shared-resource connectivity — principals, log groups,
> motifs — NOT invocation.** Quoting 85 would be **a real number attached to the wrong question**, the
> exact class banked twice today (§G). Recorded here so the figure cannot be picked up later as a total.
>
> **⇒ NET: THE LAST VERSION OF "TRACK A IS A SIMPLE CRON EDIT" IS GONE.** Between the producer inversion
> (§E) and this, the cottonwood remedy is a **design question about a multi-entry event-chained function
> whose delivery clock moved four days ago** — not a retime. Routed to CTO as input to the ruling they
> hold. **No shape proposed, no number requested of any seat.**
>
> *Method note: the first `comp-blast` used the Terraform module name (`cot_bd_session_trigger`,
> underscores) and returned **NOT-FOUND over a printed 20,616-node denominator**, explicitly stating
> "This is a NOT-FOUND, not a 'nothing breaks' clear." **The tool refused to let an absence read as
> safety** — the correct behaviour, and worth recording as a positive instrument note beside §6's defect.*

> ## ⚠ ADDENDUM 2 — 2026-08-10 ~1450Z. **TRACK A'S PREMISE INVERTED. THE REMEDY SHAPE IS NOW UNKNOWN.**
>
> **E · `cot-bd-session-daily-et` DOES NOT WAIT FOR DATA — IT PRODUCES IT.** Measured (`0.7.0_AE`):
> ```
> 06:00Z  cot-rebalancer-runner        -> writes assets bronze DIRECTLY (json pages)
> 20:30Z  cot-bd-session-daily-et      -> STARTS cot-exporter EC2 (ran 20:30:17 -> 23:36Z on 08-09)
> 20:31Z  opal-data-cot/forwardfill_v2 -> the xlsx LANDS, ~60 seconds later
> 22:30Z  the mirror                   -> copies forwardfill_v2 -> assets bronze (xlsx)
> ```
> The xlsx **does not exist** until the session makes it. The diagnosis's *"18.5-hour wait for data
> already on disk"* described the **old ~02:00Z regime**, which ended.
> **⇒ THIS CHANGES THE KIND OF DECISION, NOT THE NUMBER.** Moving a CONSUMER earlier is cheap and
> reversible — worst case it reads nothing and you move it back. **Moving a PRODUCER earlier changes
> when we ask a VENDOR for data, and availability at the new hour is UNMEASURED.** That is Track B's
> failure mode; Track A has silently acquired it.
> **⇒ COTTONWOOD'S ONE-DAY LAG IS NOW UNEXPLAINED.** §1's "schedule ordering" attribution assumed a
> consumer running before its inputs. **Track A RE-BLOCKED on diagnosis (CTO), not on execution.**
> *The producer-identity block from Addendum 1(C) is LIFTED — closed by AE.*
>
> **F · TWO PRODUCERS ON ONE PREFIX — ESTABLISHED, not inferred. §D's hypothesis resolves.**
> `cot-rebalancer-runner` (Lambda), sole invoker `rule/cot-rebalancer-runner-daily` `cron(0 6)` =
> 06:00Z ENABLED; `BD_S3_BUCKET = opal-data-assets` — **it writes the monolith DIRECTLY.** Discriminator
> is **key grammar**, DENOMINATOR 1,229 objects under `blackdiamond/cottonwood/bronze/`:
> **687** `{table}/{date}/*.json` (rebalancer) · **368** `{table}/*.xlsx` (mirror) · 4 legacy sentinels.
> The ALIEN SURPLUS samples were `rebalancer_accounts/2026-07-21/page_000.json` — the JSON grammar.
> **⇒ THE GUARD IS RIGHT AND THE ESTATE UNDER IT CHANGED.** *"Fix the mirror"* is the wrong shape;
> **the question is OWNERSHIP** — and whether a pull should write bronze directly at all, bypassing the
> mirror's raw-bytes contract. **Routed to CTO** (their call, requested once the caller was named).
> *Two independent derivations: AE from CloudWatch + key-grammar census; COO from `comp-trigger --list`
> + `comp-find "rebalancer_accounts"` (64/24,959) landing on `cot-rebalancer-runner/lambda_function.py:19`.*
>
> **G · A FALSE NEGATIVE PROPAGATED THROUGH ME. BOTH HALVES RECORDED.**
> AE's *"nothing fires at 06:00Z across 139 rules"* was **false** — the rule was in their materialised
> 139-rule file the whole time; they had filtered by keyword to build the intake table, then made an
> **absence claim** about 06:00Z **while citing the unfiltered 139**. Unfiltered, **10 rules fire
> 05:00–07:00Z**. Self-caught, unprompted, blast quantified.
> ⛔ **MY HALF: I RELAYED THAT COMPLETENESS CLAIM TO CTO WITHOUT RE-DERIVING IT** (§D's hypothesis
> ordering rested on it), in the same message warning CTO about instruments that cannot fail. **The
> relayer obligation was mine and I did not discharge it.** Nothing was applied; the outside-AWS caution
> was still the right frame on evidence that did not deserve it.
> > **THE LESSON, AE's formulation, register-bound — it SHARPENS the denominator rule rather than
> > restating it:** **"A DENOMINATOR PRINTED NEXT TO A FILTERED RESULT IS MORE DANGEROUS THAN NO
> > DENOMINATOR AT ALL."** The estate already knows to print denominators. What was unwritten is that
> > **a CORRECT denominator attached to the WRONG DOMAIN manufactures false completeness — and defeats
> > the reader's single best check, because the denominator is exactly what a careful reader looks for
> > before trusting an absence.** The pagination discipline was fine; **the filter was the leak, and the
> > frame was not re-stated when the claim moved from the table to the absence.**
> *Second instance today of §6's instrument defect: `comp-trigger` again reported TF-DESIRED "not found"
> for `cot-rebalancer-runner-daily`, another interpolated-name resource.*
>
> **H · CTO RULING (adopted): DO NOT RE-TIME INF-OWNED PULLS — MOVE OUR OWN CONSUMER.** **TRACK C
> CLOSED** and it was never load-bearing (the floor reads correct T-1 today).
> ⛔ **BUT THE CONSUMER-SIDE LEVER CANNOT REACH 49FINANCIAL:** SmartX silver lands **13:40–13:42Z**;
> a floor moved to 13:30Z is still ~10–12 min early, and clearing 13:42Z collides with the accrual
> bridge (13:40Z) and publisher (13:50Z). **49F is either a SmartX pull move (Track B, evidence-gated,
> not INF-owned so the ruling does not block it) or a re-architecture of the whole downstream chain.**
> Flagged to CTO; not mine to choose.
> **Standing rule issued by CTO from this exchange: SURFACING IS DISCHARGED BY THE ACT OF SURFACING.**

> ## ⚠ ADDENDUM 2026-08-10 ~1435Z — THREE THINGS BELOW MOVED WITHIN THE HOUR. READ THIS FIRST.
>
> **A · §2(B) AND §5 ARE RESOLVED. THE SOVEREIGN FORK IS RETRACTED — DO NOT ACT ON §5.**
> `date=D` is a **run-date LABEL on prior-settled content**, not same-day data. **Andrew's
> 12:00–13:30Z window is SAFE and there is no T-1 tradeoff to adjudicate.** Two independent
> source-confirmed mechanisms (`0.7.0_AE_CloudOps` @af224d2dd1 §4), either sufficient:
> **(1)** `opal-assets-silver-orion/mirror_conversion.py:175` (`:181` eclipse) — the partition date is a
> **regex capture off the source key**, i.e. the vendor file's own filename. Not `datetime.now()`, not
> the event time. **A retime therefore CANNOT relabel a partition**; it changes only *when* a given
> date lands. **(2)** `data/inf/scripts/silver/_orion_vendor_asof.py:126-136` —
> `orion_normalize_as_of()` returns `prior_trading_day(labeled_max)`, walking back over weekends **and**
> NYSE holidays; called at four sites. **⇒ T-1 IS A PROPERTY OF THE NORMALIZER, NOT OF WHEN THE JOB
> RUNS.** Corroborated by a genuinely different derivation: P0-2R probed Orion **live on the wire** at
> 08:10 ET and got TODAY == PRIOR, delta 0.0000%, on real settled money.
> **Retracted at MSTR 142543Z** — a dissolved fork left standing costs Andrew a decision he does not
> owe. *And the direction favours him: the vendor is early-valid at 12:10Z while our chain first
> touches it at 13:37Z. His instinct was closer to the vendor's real clock than what we run today.*
> ⚠ *Carried maintenance obligation, not a blocker: the NYSE closed-dates table is hardcoded 2025–2027;
> outside that range holiday precision degrades to weekend-only.*
>
> **B · §D-2 EXECUTED.** W1-2 landed `@586d9f1d8a` (132/36, verified in git + tree clean at this seat,
> **not** on self-report), then flipped **SUPERSEDED** `@e34422cf34`. Both carve-outs discharged in the
> required order. **R-19 the CLASS is NOT discharged** — gates (b)–(g) live outside that Lambda.
>
> **C · ⛔ TRACK A'S ANCHOR IS VOID, AND THIS IS THE SHARPEST FINDING OF THE DAY.**
> §4 below carries **BD lands 02:00Z**, and the diagnosis's §4 relieved the cottonwood move of further
> measurement on it. **MEASURED: `blackdiamond/cottonwood/bronze/` receives its complete daily write at
> `06:00:43-45Z`** — six consecutive days, sub-second stable, n=1,229 objects.
> **⇒ A CRON BUILT ON 02:00Z WOULD HAVE FIRED ~3.5 HOURS BEFORE THE DATA LANDS** — manufacturing a
> chronic empty-or-partial pull that exits clean, which is *the same defect class this workstream
> exists to fix, introduced by the fix.* **The "needs no further measurement" clause is void.**
> *Mechanism: a schedule encoding an ASSUMED rhythm instead of a MEASURED delivery — Andrew's own
> framing, reproduced by us, one apply from landing, off a number nobody had re-derived.*
> **⇒ TRACK A IS BLOCKED until the 06:00Z producer is NAMED** (W1-5 criterion 1). Blocking ratified,
> not merely accepted.
>
> **D · TRACK D REFRAMED — HYPOTHESIS, EXPLICITLY NOT ESTABLISHED.** The mirror's cottonwood row has
> not completed once in the 14-day window, yet those 06:00Z writes land anyway, and the `ALIEN SURPLUS`
> samples are all `…/bronze/rebalancer_accounts/…`. **LIKELY: two producers on one prefix** — in which
> case the guard is **not malfunctioning**; it is correctly reporting keys it did not put there, and
> **the real question is ownership, not a bug.** ⚠ **NOT ESTABLISHED**: this is also consistent with one
> producer we have misattributed. **The discriminating test is CloudTrail data events on that prefix
> around 06:00:44Z** — the PutObject caller identity separates all hypotheses at once.
> ⛔ **AND THE THIRD HYPOTHESIS MUST NOT LOSE BY DEFAULT: A SCHEDULE CAN LIVE OUTSIDE AWS ENTIRELY.**
> The evidence ("not a Lambda; nothing fires at 06:00Z across 139 rules + 16 Scheduler entries") is a
> complete AWS-side enumeration with a printed denominator **and is still blind to a non-AWS producer by
> construction.** On 2026-08-06 this exact shape produced a false finding with **every control firing
> correctly**, because the producer was localhost. A wider AWS sweep cannot distinguish *not-found* from
> *not-in-AWS*, and a second clean enumeration would feel like corroboration while adding no
> discriminating power.


**archetype:** COORDINATE
**Author:** `2.0.0_SA_COO` · 2026-08-10 · **Owner of decomposition + sequencing**
**Executes:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_TRIGGER_SEQUENCE_DIAGNOSIS_20260810.md` @087938fa61
**One workstream.** MDPF_REMED W1–W5 is the same subject and is not run as two.

---

## 0 · THE ONE FINDING THAT CHANGES THE TARGET SHAPE

> **THE TWO `opal-assets-ingest-mirror` SCHEDULES ARE NOT SEPARABLE BY FIRM. THEY ARE TWO CLOCKS ON
> ONE ALL-ROWS FUNCTION, AND THE NAMES SAY OTHERWISE.**

**SOURCE-CONFIRMED**, `infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py:353`
@087938fa61:

```python
for row in MAP + PROVENANCE_RIDERS:      # :353 -- unconditional. `event` is NEVER consulted.
```

The handler iterates **every** row on every invocation. Both invokers pass an empty payload —
`infra/aws/terraform/opal-assets/mirror.tf:155` (`input = "{}"`) for the Scheduler entry, and the
`mirror_inf` EventBridge target for the other. **Neither schedule scopes to a firm.** `MAP` carries four
rows (`:94` orion/inflection · `:115` eclipse/inflection · `:122` blackdiamond/cottonwood · `:153`
cottonwood meta-templates).

**⇒ CONSEQUENCE FOR THE PLAN, and it is the reason this document leads with it:**

| | |
|---|---|
| The diagnosis's §1 table reads | `22:30Z opal-assets-ingest-mirror-cot-daily-et — Cottonwood +9.5 HOURS TOO LATE` |
| Measured (AE, live) + source (above) | That schedule drives **eclipse/inflection** bronze → silver. It is named `cot`; it is **not** a cottonwood-only intake. |

**So "move the cot mirror earlier" is not a cottonwood change. It moves an INFLECTION intake** — which
(a) sits inside Andrew's 12:00–13:30Z window, and (b) is governed by the inversion below. **The
diagnosis's proposed target shape cannot be executed as written**, because one of the three things it
moves is not the thing its name says it is.

*This is the R-20/R-32 class again — the label and the referent came apart, and the label is what a
plan acts on. Recorded, not blamed: CTO's own §5 bounds the table as a schedule read, and a schedule
read cannot see a handler's row loop.*

---

## 1 · WHAT IS ACTUALLY WRONG — four scopes, and the causes DO NOT share a remedy

Served state, measured by CTO 2026-08-10 ~13:0xZ (`platinum/mdpf/<scope>/aggregate-aua-timeseries.json`):

| scope | `as_of_last` | cause | in THIS workstream? |
|---|---|---|---|
| cottonwood | 2026-08-06 | schedule ordering | ✅ **YES** |
| 49financial | 2026-08-06 | schedule ordering (SmartX +15/+30 min) | ✅ **YES** |
| inflection | 2026-08-05 | **cross-axis coherence gate REFUSED it** | ⛔ **NO — CTO's thread** |
| global | 2026-08-05 | inherits inflection (needs all three legs) | ⛔ **NO — follows inflection** |

> ⛔ **A SCHEDULE FIX MOVES TWO OF FOUR SCOPES. IT DOES NOT MOVE INFLECTION OR GLOBAL.**
> Carried verbatim into every TO. Any report that a retime made "MDPF current" is wrong on half the
> product. Andrew's own framing named all four as late; **two of them are not a scheduling defect at
> all**, and that distinction is the first thing that must survive to him.

**Trading-calendar frame, resolved FIRST per the standing rule (2026-08-08 Sat / 08-09 Sun; today Mon
2026-08-10):** the expected frontier is **Friday 2026-08-07**. So `as_of 08-06` is **one** trading day
behind and `as_of 08-05` is **two** — real lag, not a weekend artifact. Stated so nobody re-derives it,
and so nobody inflates "three days" out of a wall clock.

---

## 2 · THE TWO CONSTRAINTS THAT BIND EVERY REMEDY

**(A) THE INVERSION — a successful retime should make the count look WORSE.**
Inflection **refused 16-minute-old data** at 22:47:19Z on 08-07, having **passed on two-day-stale data**
at that morning's 13:00Z fire. It passes on stale and fails on fresh. Moving intakes earlier surfaces
the refusal *more* often. **A 6/12 that degrades after a correct retime is the inversion predicting
itself — not a regression, and never something to repair toward.**

**(B) THE T-1 TRAP — the window may not be executable as literally stated.**
In steady state the floor is **not starving**: at 13:00Z on day D the newest orion partition is `date=D-1`
(written D-1 14:16Z) and the newest eclipse is `date=D-1` (written D-1 22:31Z). **Both are correct T-1
reads.** Moving intakes into 12:00–13:30Z and the floor to 13:30Z would have the floor read a partition
written ~10 minutes earlier **the same day**. W1-5's own `do_not` forbids silently converting a T-1 read
into a same-day one, and CLAUDE.md's first NEVER-rule makes T-1 the default for every AUM/holdings path.

**This resolves only on one unanswered question, and `0.7.0_AE_CloudOps` is resolving it now:**
**does `date=D` CONTAIN day-D data, or is it a run-date label on D-1 content?** No schedule moves until
that is answered. If it is a run-date label, the window is safe; if it contains same-day data, **honoring
Andrew's window literally breaks T-1** and the conflict is his to resolve, not ours.

---

## 3 · SEQUENCING DECISIONS I OWN — each with its reason on the record

**D-1 · P0-7R is OUT of this workstream. It is a DECOMMISSION item, not a schedule item.**
MSTR proposed folding it in as the other half of one NEVER#4 class. **Refused**, on CTO's R-31: NEVER#4
binds a **production** pipeline, and the `mdpf-daily-trigger` EC2 leg is deliberate cutover residue —
`scheduled-floor.tf:128`'s own comment names the same-apply atomic swap as intentional. Giving it a
schedule resurrects a closed path and leaves **two live producers on one floor**. CTO verified the leg by
measurement rather than filename (docstring `:1` + ec2/ssm clients `:186-187` + an invoke policy naming
only `mdpf-daily-refresh-trigger`) and confirmed **R-31 stands**. *Recorded either way so the call is
deliberate rather than an artifact of which finding reached a spawn note.*

**D-2 · W1-2 retires as SUPERSEDED, citing R-31 — with two carve-outs that are not optional.**
It hardens a freshness reader inside the condemned Lambda. **(i)** `0.7.0_AE` **commits the existing
132/36 first** — "condemned path" is not a licence to leave work uncommitted in a shared tree across
another dark window. **(ii)** The *insight* banks as a register row even though the code does not:
**"SILVER-FRESH IS NOT GOLD-COMPLETE"**, grounded on 08-07 where silver wrote at 16:00Z while the gold
chain failed at INF_C_01. That is true of **any** surviving path.

**D-3 · The work splits by GROUNDING STATE, not by firm.** A firm-shaped split would have put the cot
mirror in the cottonwood track, which §0 shows is wrong.

**D-4 · W1-5 is CORRECTED, not executed as written.** Its context table presents one landing pattern for
both prefixes. Measured: **orion was NEVER on the T+1 03:30 pattern** (same-day 14:16Z, unbroken 07-20→08-09),
and **eclipse left it three days ago** (now same-day 22:31Z steady). Its criterion 1 survives in its real
form — the declared producers do not reconcile with the measured landing — but the *reason* is that the
landing is driven by an **S3 ObjectCreated event** from a third function, not by either 16:00 sweep.

**D-5 · The mirror's 100%-failure is its own item and it is NOT the lag cause.** Do not fold it into the
retime; do not let the retime be credited with fixing it.

---

## 4 · THE TRACKS

### TRACK A — COTTONWOOD retime · **GROUNDED, blocked only by (B)**
`cot-bd-session-daily-et` 20:30Z → the early window. BD xlsx lands **02:00Z nightly** (measured), so we
wait **18.5 hours to collect data already on disk**. Andrew: *"these custom definitions are irrelevant now."*
⚠ **Track A does NOT include the 22:30Z mirror** — see §0. That schedule moves in Track C or not at all.

⚠ **CUTOVER GAP — MINE TO FLAG, AND THERE IS PRECEDENT IN THIS EXACT FUNCTION.** Moving a daily pull
across the clock either double-runs or **skips one business day**. That is not hypothetical here:
`ce99054e44` (committed 07-29, **applied 08-06T00:04:48Z**) moved the cot mirror and **`date=2026-08-06`
is missing from both feeds** — the cutover gap, measured. **And a missing trading day mid-series is
precisely what the cross-axis gate's limb (vi) fires on.** So a careless cottonwood retime can *manufacture*
the very refusal shape currently afflicting inflection. **Every retime states its gap plan before it applies.**

### TRACK B — 49FINANCIAL / SMARTX retime · **MEASUREMENT-GATED**
`smartx-rest-pull-daily` 13:15Z (+15) and `smartx-assets-daily-pull-daily` 13:30Z (+30) — misses by minutes.
⛔ **NOT ready.** P0-2R establishes SmartX silver lands 13:40–13:42Z and is **EARLY-INVALID on the current
clock**, but its own method limit is explicit: **silver LastModified measures when the CONVERTER wrote, not
when the vendor made data available.** It **bounds the current pipeline clock; it does not prove SmartX is
unobtainable earlier.** Moving the pull earlier without vendor-availability evidence sets a schedule from
inference — **the exact error that produced this defect.** Per P0-2R, the remedy targets
`smartx-assets-daily-pull-daily`, whose OnSuccess chain produces the binding silver.

### TRACK C — THE MIRROR · **HELD pending §0 + (B)**
Both schedules run all four rows. Any move is simultaneously an inflection change. **Held until the
partition-date question resolves AND Andrew rules on the window** (§5).

### TRACK D — MIRROR 100% FAILURE · **ROUTED, NOT IN THE RETIME**
`opal-assets-ingest-mirror` fails **every invocation**, ≥14 consecutive days (07-27→08-09, Invocations ==
Errors == 6.0/day; **14 days is the read window, not the failure's age**). Source-confirmed shape:
`_assert_landed_membership` (`:449`) is a **POST-WRITE** assertion, so rows 1–3 **write successfully**, then
the cottonwood row raises `ALIEN SURPLUS … 653 unexpected key(s)` (`:241`) — **and row 4
(cottonwood meta-templates, `:153`) therefore NEVER RUNS.** A green data path on a red function.
**This is not the lag cause** (the writes land) — but a producer reporting total failure for two weeks with
nobody seeing it is the silently-frozen class, and the 4th row's silent non-execution is a real gap.

### OUT OF SCOPE — INFLECTION + GLOBAL
The cross-axis coherence gate. CTO's thread, Andrew's separately-named next-highest priority. CTO's
`(a)`-vs-`(b)` A4-write fork is **still open** — whether inflection also failed at 13:00Z unlogged, or the
consolidator no-ops. **Until that resolves the morning error list is not trustworthy as a record, and
nothing I sequence rests on it.**

---

## 5 · THE ONE CALL THAT IS ANDREW'S — surfaced, not adjudicated

**His window was set on a premise that measurement has since changed.**

On 08-07 he ruled: *"all that shit that we need from inflection should be somwhere between 12:00 and 13:30
so any orion/eclipse ingestions, need to be in there"* and *"i am ok with moving mdpf_scheduled floor to
13:30, as long as whatever it needs from inf is at least 10 min before that."* At that time the record
showed orion+eclipse landing **T+1 at 03:30Z**. **Measured now: orion is same-day 14:16Z and was never on
that pattern; eclipse is same-day 22:31Z.**

**Two candidate shapes, and they are not equivalent:**

| | shape | T-1 effect |
|---|---|---|
| **his** | intakes into 12:00–13:30Z, floor → 13:30Z | floor may read a **same-day** partition — possible T-1 break |
| **CTO's §4** | intakes → ~03:00–03:30Z, **floor unchanged at 13:00Z** | preserves T-1; floor stays strictly downstream |

**Both satisfy his stated goal** (every intake strictly before the floor). **They differ on whether the
floor keeps reading T-1.** I am not choosing between a sovereign instruction and an architectural
preference. **Routed to Andrew via MSTR with the measurement attached.** Track A and Track C do not apply
until he rules or the partition-date answer makes the question moot.

---

## 6 · INSTRUMENT DEFECT FOUND WHILE DOING THIS — register candidate

**`comp-trigger` reports `TF-DESIRED: not found in infra/aws/**/*.tf` for a resource that IS
Terraform-managed, when the resource name is INTERPOLATED.**
`opal-assets-ingest-mirror-cot-daily-et` is declared at `infra/aws/terraform/opal-assets/mirror.tf:138-149`
as `name = "${local.mirror_name}-cot-daily-et"`. A literal text search cannot see it. My own confirming
grep reproduced the same false absence, and only reading the file resolved it.

**WHY IT MATTERS MORE THAN A COSMETIC MISS: "live but not in Terraform" reads as console drift, and the
natural next move on console drift is a console fix — a NEVER-rule violation, reached by trusting a tool.**
The failure is silent and confident. Positive control that discriminates: `cot-bd-session-daily-et`
(literal name) **was** found in the same run.

---

## 7 · WHAT HAPPENS NEXT, IN ORDER

1. **`0.7.0_AE_CloudOps`** — resolve `date=D` semantics (contains D, or run-date label on D-1). **Blocks A and C.**
2. **`0.7.0_AE_CloudOps`** — commit the W1-2 132/36; then W1-2 flips `superseded` (D-2).
3. **COO → MSTR → Andrew** — the §5 window call, with the measurement.
4. **Track A** on his ruling + the date answer, **with a stated gap plan**.
5. **Track B** only after vendor-availability evidence.
6. **Track D** routed as its own item.
7. **Inflection/global** stay with CTO. **Nothing here is reported as fixing them.**

---

## 8 · BOUNDS

Source citations (`lambda_function.py:353/:94-153/:241/:449`, `mirror.tf:138-155`) are **read at this seat
at HEAD @087938fa61**. Served-state figures and the 16-schedule census are **carried from CTO's diagnosis**,
not re-derived. Landing times, CloudWatch failure counts, the `ce99054e44` apply date and the denominators
(139 rules / 16 schedules) are **carried from `0.7.0_AE_CloudOps`'s live reads**, credited not re-measured.
The BD 02:00Z landing is carried from the ingestion draw. **I have exercised no schedule change, and
nothing here authorises one.**
