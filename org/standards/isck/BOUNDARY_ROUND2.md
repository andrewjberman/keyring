# ISCK ADVERSARIAL PASS — ROUND-2 BOUNDARY RECORD

**Cut by:** `1.0.0_SA_CTO~X` · **2026-08-28 00:2xZ** · **On the word of both attackers:** `3.0.0_SA_CVO~X`
DRY across the whole package (77074 → confirmed at @d144e7937c/@7c093caff5), `4.0.0_SA_CRO~X` DRY
across R2-2, ARM-4, DT-R2-6 and the carrier correction (77095). **What this record IS:** the close of
the second ATTACK ROUND on the contract chartered @14e6bcc50d. **What it is NOT:** the round-2 EXIT
to operational use — see §6; the charter's third condition (the vertical-slice battery) is a build
that has not been run, and this record says so rather than letting a green suite stand in for it.

---

## 1. VERSION IDENTITY PINS (R2-10 — published with the boundary, not on request)

```
  ATTACKED INPUT (round-1 output, frozen)      21d6fc7325
  ROUND-2 CHARTER                              14e6bcc50d
  BOUNDARY OUTPUT (package tip at cut)         9760630ae7      37 package commits since input (git rev-list --count 21d6fc7325..9760630ae7 -- org/standards/isck)
                                               [AMENDED: the record first printed 35, the count through 9fb81b743a, beside the 9760630ae7 pin --
                                                a typed number beside a derived one; CRO~X re-verify]
  LAST SCHEMA-CHANGING COMMIT                  2795145b63      (DT-R2-6; d144e7937c / 7c093caff5 / 9760630ae7 are prose + runner, diff on schema+validator EMPTY -- CVO~X 77074 read)
  SCHEMA  ISCK_CONTRACT.v0.schema.json         blob b2e3c3683e15   sha256 586bf52cf3171cdf361d6ed3fdb37e0c0cfa7f0b91d23bb3b4f1d48146360859
                                               (method: `git show <tip>:<path> | sha256sum` -- LF as stored; a CRLF working-tree read gives a DIFFERENT digest and is not this pin)
  CONTRACT ISCK_CONTRACT.md                    blob d1506ca0944e
  VALIDATOR validate_isck.py                   blob 418ad2b96d7c
  R2-2 DESIGN (attacked-dry, NOT LANDED)        blob 41cacec709b8   @7c093caff5
  ARM-4 RECORD                                 blob 5892013077d3   AT THE TIP 9760630ae7 (base @05086d045c = blob f85d4b24a6e6; class C rewritten MOOT @2795145b63)
                                               [AMENDED: first printed "5892... @05086d045c", false as an object-at-commit assertion; CRO~X re-verify]
  PUSH STATE AT CUT                            LOCAL -- origin/CLOUD @c29f17b5c9 (ls-remote read 00:18Z) carries 2795145b63 and earlier
  PUSH STATE, AMENDED 00:3xZ                   ON ORIGIN -- origin/CLOUD @3fbb493cdafd584209a10c6353794667e5507b98 (fresh fetch, this seat):
                                               merge-base --is-ancestor YES for 9760630ae7 (package tip), ece1ac0f41 (this record), 6245dc0a3d
                                               (first amendment); integrator 0.0.0_AB_MSTR 77126 read the same, independently
```

**Gates at the boundary tip, ATOMIC EXTRACT of 9760630ae7 (run_gates.sh, this seat, 00:25Z):**
validate 0 · ablation 0 · collisions 0 · isolation 0 · labels 0 · coverage-probes 0 → **overall
exit 0 | 11 open candidates (ARM1 9, ARM3 0, ARM4 2 of 20 undisposed)**. Self-test line: 4/4 axes +
14/14 positive + 67/67 reason+path-asserted mutants + 11/11 semantic + drift + gutted-schema
meta-controls. Second-seat reads at 7c093caff5 (schema-identical): CRO~X 77095 — ablation 45/45,
labels 15/15; COO~X 77035 at 05086d045c — the first all-green run of the pass, their labels gate
included. **15 → 29 → 11 is the runner remedy SUCCEEDING, not package movement** (CRO~X 77081's
framing, adopted verbatim): ARM4's 20 became visible when the summary learned to print a denominator,
ARM3 went 6 → 0 on DT~X's repairs, ARM4 went 20 → 2 when the consume gate disposed 18 by record.
**Ablation 47 → 45 is two WRONG arms retired (DT-R2-6), every remaining rule mutant-covered.**

## 2. TALLY — every LISTED finding UPHELD; refutations this round: ZERO — **denominator NOT YET AUDITABLE**

**AMENDED on CRO~X's re-verify:** the cells below mix findings with inputs, verified-accepts,
confirmations, censuses, fixes and owed work, and carry no unique finding ids — so "~40 findings" is
not reproducible from this table. The honest claim is **~40 LISTED CONTRIBUTIONS**; a deduplicated
FINDING REGISTER (one id per finding, source, disposition, commit) is OWED by `1.0.0_SA_CTO~X` before
the zero-refuted statistic may be attacked or quoted as a rate.

| seat | findings (all upheld) | the one that cost the most |
|---|---|---|
| `4.0.0_SA_CRO~X` | 6 charter gaps (pre-charter) · R2-2 inputs 1–4 + migration receipt · RA-1–5 · ARM-4 CUT-4 over-constraint · the DT-R2-6 CARRIER finding · 2 verified-accepts (R2-1 FINAL, R2-8 VERIFIED) | **RA-5**: my direction table said `canonicalized_as: NEITHER` against the semantic arm of the contract I wrote |
| `3.0.0_SA_CVO~X` | CVR2-2's four (the `superseded` laundering cell; contests-as-overlays; subject-grain `unknown`; `partial_legacy` fusion) · AT-1–6 · RE-1, RE-2 · CV-3 rubric on CUT-4 · branch-(a) input on DT-R2-6 · carrier confirmation · CV-1 CERTIFIED CLOSED @4f66d2edf2 | **RE-1**: my disposition said the AT-5 split "landed"; `git show 65ed5c07ad:… \| grep -c` = 0 |
| `0.4.0_DT_ClientPlatform~X` | DT-R2-1–6 (DT-R2-2 shared-enum propagation; DT-R2-3 atomic extracts; **DT-R2-6 candidate × contradicted UNINHABITABLE**, constructed three ways + positive control) · ARM-1 disjunctive parser fix · ARM-3 census 95/95 @db4062c3a7 · ARM-4 consume gate @9fb81b743a + its own key defect (found by generator count) + its own loader defect (found by attacking itself) | **DT-R2-6** overturned my ARM-4 class-C reasoning: the unsatisfiability I declined to "manufacture" already existed |
| `2.0.0_SA_COO~X` | COO-R2-1 (a green runner masks candidates — went LIVE the moment the suite first went all-green) · derive-from-schema gate remedy · labels gate 9/13 → 15/15 · DT-R2-6 exhaustive corroboration (6,144 instances, exactly 1 uninhabitable cell) · superseded-consumer census (OWED — the R2-2 landing gate) | **COO-R2-1**: the seam only mattered once nothing upstream was red to mask it |
| GPT review (Andrew-supplied) | the charter's source; R2-2's direction (events-are-truth) | — |
| `1.0.0_SA_CTO~X` (author) | 0 refutations issued. Named against myself, all caught by a second seat, none by me: RE-1 (silent-no-op patch reporting success), RA-5, CUT-4 (uncited premise: "unverified means the check did not run" — the citation EXISTED at §3.14's remedy column and I had not read it), the CARRIER (cited an event whose targets can never be an assertion, one commit after landing the design that makes it impossible), class C (DT-R2-6). Instrument slips: a `\1` eaten as an octal escape; a stray `cat` blocking stdin | the pattern: every one was a claim about an artifact I had not re-read at the cited vintage |

**Zero refutations is a statistic, not a compliment.** Round 1 refuted 3 of 24. Round 2 refuted 0
of a not-yet-registered denominator (~40 listed contributions). Either the attackers were more precise on a harder target (their findings were narrower and
came with constructed instances), or the author accepted too readily. Both readings are recorded;
the next round's attackers should try to refute an ACCEPTANCE.

## 3. CHARTER ITEMS R2-1 … R2-10 — resolved or carried WITH OWNER (exit condition 1)

| item | state | citation |
|---|---|---|
| R2-1 fabric semantics | LANDED, FINAL ACCEPT (CRO~X) | @9fa5a91af5 (execution vs referent families; `fabric_local` added) |
| R2-2 append-only + derived status | **DESIGN ATTACKED-DRY; LANDING CARRIED** — owner `1.0.0_SA_CTO~X`; gates: `2.0.0_SA_COO~X` superseded-consumer census + the 8-line landing checklist @bfcebc58c5; lands at the implementing boundary (WP-3 ledger) | draft @1061546c63 → @eeb0e6ab51 → @65ed5c07ad → @c733ac9819 → @5b15802d0f → @7c093caff5 |
| R2-3 warrant completion | LANDED | @1b08f0e37e + @5ffb98936c (forbid-mirror idiom, contested warrant) |
| R2-4 mixed temporal/epistemic axes | the `superseded` cell RESOLVED BY DESIGN in R2-2 (carried to its landing); limit-2 reclassification landed | @5ffb98936c; R2-2 §3a |
| R2-5 observation of absence | LANDED | @e07b9efec0 |
| R2-6 frontier coherence | LANDED | @1b08f0e37e |
| R2-7 mint receipt | LANDED (LAW 1's control defined; enforcement at WP-3, declared) | @7b6629d3b7 |
| R2-8 bridge_assertion | LANDED, VERIFIED ACCEPT (CRO~X); CV-1 CERTIFIED CLOSED | @547730fd8a + @7a1192b0c3; @4f66d2edf2 |
| R2-9 battery maturation | atomic runner @d2fc841873 · path-grained assertions + drift meta-control @3c37267b91 · seat modules (DT~X probes, COO~X gates) · denominator line @f18f4cf8d4 + @9760630ae7 · ARM-3 95/95 @db4062c3a7 · ARM-4 25/25 @8f8fe7db5f/@05086d045c · consume gate @9fb81b743a (**OUTSIDE the dry — §5**) · **ARM-1's 9 candidates CARRIED, owner `1.0.0_SA_CTO~X`, post-boundary** (4 of them already adjudicated in prose at ISCK_CONTRACT.md :81-83 — the record must say so per candidate) | — |
| R2-10 version identity | §1 of this record | — |

## 4. INDEPENDENCE LEDGER — who converged with whom, honestly

- **CRO inputs 3/4 ↔ CVO AT-3/AT-4 (contest ids; terminal shape): SHARED-CONTEXT, not
  corroboration.** CVO~X disclosed forming from the draft alone THEN diffing against CRO's inputs
  (sends 23:01:02Z vs 23:05:36Z) and tagged the convergence themselves.
- **RA-3 ↔ RE-2 (direction table): PARALLEL, shared-context.** 23:11:18Z vs 23:12:33Z; CVO~X stated
  the timestamps because parallel is not provable.
- **RA-5 (CRO) → CVO confirmation: SEQUENTIAL, and the ledger's honest entry is CVO~X's
  self-retraction** — their dry declaration had swept ONE row of a seven-row table and presented as a
  table pass; RA-5 found what the early stop missed; CVO then ran 7 of 7.
- **DT-R2-6 (DT~X, construction ×3 + positive control) ↔ COO~X (exhaustive enumeration, 6,144
  instances) ↔ CRO~X: THE ROUND'S ONE GENUINE INDEPENDENT CORROBORATION** — different instrument
  (enumeration vs construction), same single uninhabitable cell, and COO's method could have found a
  second cell and did not.
- **CUT-4: SEQUENTIAL CHAIN, every step disclosed** — CRO finding → author narrowed (@c1edaf9638)
  → CVO rubric (CV-3's author: FREE = free of REQUIRED warrants) → CRO's A/B → (B) @05086d045c. A
  chain, not a convergence; the flip is in the record.
- **CARRIER: CRO finding → CVO confirmation that OWNED the bad clause** (branch (a)'s
  `contest_resolved` carrier was CVO~X's suggested wording; they confirmed against it). A
  self-implicating confirmation is the strongest kind this ledger has.
- **RE-1: CVO~X ALONE, MEASURED** (a grep count of zero at the cited commit) — the round's
  cite-the-act-witnessed instance, mine.
- **COO-R2-1: COO~X alone; the module's OWNER (DT~X) concurred from the other side; CRO~X
  reproduced.** Three seats, three roles (finder / owner / reproducer).
- **Build-time anchor (round 1's named class): still unresolved and unresolvable** — every attacker
  read the same charter; which attacks they built is anchored on it. Disclosed, not cured.

## 5. WHAT WAS NOT ATTACKED (named, so silence is not coverage)

- **`source_frontier`, `surface_version`** — "NOT EXAMINED 2 of 12" at the tip (DT~X 77099); no
  finding all round from any instrument; ARM 1 is structurally blind to them (§6 prediction).
- **The ARM-4 CONSUME GATE @9fb81b743a** — explicitly OUTSIDE this boundary's dry (CRO~X 77095:
  "must not inherit this dry declaration"); DT~X's self-found loader defect (77101: `json.load` is
  last-wins on duplicate keys, a class-A entry could silently overwrite a class-D one) is DISCLOSED
  here, fix authorized under a sixth override, CRO~X attacks the fixed artifact with all three vectors.
- **ARM-1's 9 candidates** — carried, mine.
- **The vocab registries** (`vocab/*.json`, warn-only) — no attack.
- **The vertical-slice battery** — not built (§6).
- **The L0/L2 emission artifacts, DEC-02..05 thresholds, Nessie/Kuzu substrates** — separate arcs,
  not in this round's target.

## 6. THE REGISTERED PREDICTION — three-line state, `0.4.0_DT_ClientPlatform~X`, VERBATIM (77099)

Prediction (BOUNDARY_ROUND1.md): *"If the thinness was STRUCTURAL, round-2 findings cluster in the
record types STILL without field-relation conditionals after this commit: materializer,
source_frontier, surface_version, entity (4 of 10). If round 2 instead finds its next tranche inside
the newly-conditioned records, the characterization was wrong. ARM 1 re-differencing adjudicates."*

> **RETRACTED** My own verdict of REFUTED. I called it from ARM 1 reporting zero gaps in those four
> types -- three paragraphs after documenting, in the same commit message, that ARM 1 is
> structurally blind to a record with no discriminant. I read a blind instrument's zero as
> absence. That retraction stands unchanged and is the part of this I most want in the record.
>
> **SUPPORTED** The unconditioned types were NOT clean, which was the prediction's substantive half.
> 4.0.0_SA_CRO~X's gap 3 found current defects in entity AND materializer -- two of my four, by an
> instrument that can actually see discriminant-free records. DT-R2-1 was materializer; DT-R2-5
> included entity. AND THE STRONGEST EVIDENCE IS STRUCTURAL RATHER THAN ANECDOTAL: entity and
> materializer have both LEFT the unconditioned set -- the tip reads 2 of 12 NOT EXAMINED
> (source_frontier, surface_version), down from 4. They left it by acquiring conditionals, which is
> what happens when findings land in a record and get fixed. Their silence in every battery to round
> 1 was blindness, not health.
>
> **UNSETTLED** Whether findings CLUSTER there rather than merely OCCUR there -- and clustering was my
> actual word, so this is the half that decides the prediction. It is not settled and I do not think
> this round's evidence can settle it. Findings landed in BOTH populations and heavily in the
> newly-conditioned ones (R2-1 on entity_binding + state_observation, R2-3 warrants on
> identity_relation + entity_binding, DT-R2-6 on bridge_assertion). And of my four named types, TWO
> produced findings while source_frontier and surface_version produced NONE all round -- so even
> within the predicted set the distribution is split. ARM 1 CANNOT ADJUDICATE THIS AND I NAMED IT
> THE ADJUDICATOR. It is structurally blind in the unconditioned direction, which is the very
> direction the claim is about. I nominated an instrument incapable of testing my own prediction and
> did not notice until it ran.

**Carried beside it, DT~X's reusable line, verbatim:** *"A PREDICTION MUST NAME AN INSTRUMENT THAT
CAN RETURN BOTH ITS ANSWERS. Mine named one that could only ever return silence on half the domain,
and silence is what I then misread as refutation."*

## 7. EXIT-GATE STATE (ROUND2_CHARTER.md "THE EXIT GATE") — honestly, per condition

| condition | state |
|---|---|
| 1. R2-1..R2-10 resolved or carried with owners | **MET** — §3; two carries (R2-2 landing; ARM-1's 9), both owned by this seat |
| 2. every gate passes at a cited tip that is ON ORIGIN | **MET (amended 00:3xZ)** — six of six exit 0 at the ATOMIC EXTRACT of 9760630ae7 (§1), and 9760630ae7 is ON ORIGIN: `git merge-base --is-ancestor 9760630ae7 origin/CLOUD` = YES at origin/CLOUD @3fbb493cda after a fresh fetch (this seat's read; MSTR 77126 concurs). A git-archive extract at an on-origin hash is byte-identical to a true-clone extract by hash identity — and, so that this is EXERCISED rather than argued (DT~X 77140's caveat: "on origin now" ≠ "re-run since"), `run_gates.sh 9760630ae7` was RE-RUN at 00:39Z after the fetch that read it on origin: six of six exit 0 \| 11 open candidates, identical. Was HALF at cut (tip LOCAL) — the amendment is the record, not a rewrite |
| 3. the VERTICAL-SLICE END-TO-END BATTERY passes | **NOT RUN, NOT BUILT** — mint → bind → rename → observe → reconcile → materialize-from-frontier → Nessie advance → Kuzu dislocation → history preservation. It needs the WP-3 ledger and live substrates. **ROUND 2 DOES NOT EXIT TO OPERATIONAL USE ON THIS RECORD.** |

**What this boundary therefore certifies:** the attack round is closed dry at the cited tips; the
contract is `v0.2-candidate` — attacked, not frozen (GPT's freeze ≠ certification distinction,
adopted at the charter). **Post-boundary amendments expected and pinned when they land:** DT~X's
sixth-override loader guard @6245dc0a3d — **AMENDED: INSIDE the pinned package, not post-boundary**
(`git merge-base --is-ancestor 6245dc0a3d 9760630ae7` = YES; the shared worktree committed it at
00:23:31, before the runner commit; I had classified it by message-arrival time, not by the DAG —
CRO~X re-verify). It is post-DRY and outside the attacked set, which is a different claim. **The true
first post-boundary amendment is DT~X's entry guard @bb7444a08e** (is-ancestor NO; cures CRO~X's
superset-values FAIL: payload value set must EQUAL the key's, mismatch → suppress none + WARN, six
controls, five refusing one accepting) — CRO~X's three-vector regression at that citation COMPLETE and ACCEPTED (00:38Z, after @8bce3fa495): duplicate-key WARN/0 suppressed/NEW; renamed class-D NEW/non-suppressed; widened payload DISAGREES/WARN/NEW; exact key adjudicated exactly one; six atomic gates exit 0; 18 adjudicated / 2 deferred / 0 NEW; ARM-1's 9 adjudicated (mine); the R2-2 landing at WP-3 with its
checklist; the on-origin amendment to condition 2.

## 8. WHAT THE ROUND TAUGHT THAT THE CONTRACT NOW CARRIES (beyond the findings)

- **The message scrolls, the artifact persists — applied to the author.** Three of my five errors
  were dispositions that described a fix the artifact did not carry. Remedy in force since
  @c733ac9819: every patch is match-asserted (count == 1 before write; read-back after), and a
  disposition cites a grep count at the commit, never the script's own print.
- **A one-value enum is a discriminator with no discrimination** (AT-2): `status_basis: authored`
  alone is a VINTAGE bit, and vintage-by-absence is forgeable forward (RA-4) — so the post-boundary
  schema REQUIRES the map and vintage is a manifest lookup.
- **One field, two intents, one uninhabitable cell** (DT-R2-6): `adjudicated_by` served registry
  adjudication and evidential contradiction; the cross of their arms killed a real state. Rule
  24(iii) at the field grain.
- **A green runner masks candidates the moment nothing upstream is red** (COO-R2-1): the summary
  line now prints the denominator, and a missing consume line renders UNREAD, never zero.
- **FREE means free of REQUIRED warrants, not free of contradiction** (CUT-4): the doctrine sentence
  was under-specified and a forbid read as contradicting it; both surfaces fixed in one commit.
