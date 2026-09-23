# AMGT_HARVST round 1: CVO adjudication (this project's first L9)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T01:4xZ at HEAD, LOCAL on SITEZ.
**Inputs:** `2.0.0_SA_COO~Y`'s L8 packet (msg 24503), the ten orders, the channel, the two judgment
deliverables, and this seat's own instruments: the acceptance sweep, a whole-bucket object census by publisher
and kind, and a full read of both judgment artifacts.

## Round state

**10 of 10 orders terminal**, every order reading `<status>complete</status>`. Criterion ids: 4+12+4+6+6+6+6+5+3+7
= **59**. The sweep reads **PASS 56 / FAIL 1 / UNVERIFIABLE 2 of 59**.

**Judgment census: 2 of 59, and both are graded below by this seat, neither self-graded.**

⚠ **DENOMINATOR CORRECTION:** the packet says "12 channel rows await your L9". **The channel holds 19 rows**, all
19 non-terminal before this adjudication. Every one is dispositioned here.

## The one FAIL: `HVST-h-10` AC3, `network_refused_hits 4`

The same-day replay bar required 0 refused hits and measured 4. **The issuer exempted it with its reason on the
record and explicitly did not ask me to treat the exemption as a pass.** Graded here:

**The FAIL stands on its literal terms, and it is ADMISSIBLE as a criterion defect under R4, not flipped.** The act
is shown correct on a different instrument: `http_events 0` in the delta — **no network call occurred.** The four
refused hits are the refuser doing its job on three publishers that had no replayable path (a live session check or
a fresh session build), which is a property of what the one authorised run returned, not of the replay. **The bar
was unmeetable by the cell's own design once three of five publishers ended in error or rejection**, and no further
act is authorised to move it. Row `Z-W10-S11` is not minted; the exemption is recorded here instead.

## JUDGMENT 1 -- `HVST-h-8` AC3, the timeline design spec: **FAIL**, on one clause of three

**The question:** would an engineer build the timeline from this spec alone, meeting FWD-5 and FWD-6 — every state
drawn, every relative figure named as serve-time, no working default fixed as a constant?

**Two clauses are met, and well:**
- **Relative figures named as serve-time.** §5 states `breakout_ratio` and `z_score` are computed at serve time and
  never stored, citing `C-HV-ABSOLUTE-ONLY`; the events arm says "No relative figure is computed on this arm". The
  default view plots stored absolute fields only.
- **No working default fixed as a constant.** §7 leaves the tier weights, the 0.3 share threshold, the event
  thresholds, the initial zoom, the tie-break direction and the synthetic event id open, each named as Andrew's or
  the build cell's.

⛔ **THE THIRD CLAUSE IS NOT MET: A READ-FAILURE STATE IS NOWHERE IN THE SPEC.** §6 enumerates five states —
Loading, a quiet security, the floor clamp, PARTIAL/DENIED days, and a never-collected security. **`PARTIAL` and
`DENIED` are DATA states read from `chatter_daily`; none of the five is "the timeline call itself failed".** §3
line 110 gestures at it ("not a blank list a reader cannot distinguish from a loading failure") without specifying
the state, and §5's API shape names no error envelope.

**This is not a theoretical gap. It is the defect I graduated on the sibling project SIX HOURS AGO, twice:**
`AMGT_RESAPP` Z-S227 (0 of 5 tabs carry an error branch, so a failed read renders as an empty panel) and C-S400
(the overlay asserts "No overlay data for this name yet" on any failed read, about a name whose overlay we wrote).
**A spec that omits the state is how a build reproduces it**, and this spec's own discipline — "say the state,
never hide it; mark, never degrade" — is the principle it fails to apply to its own read path.

**REMEDY, bounded:** one state in §6 ("the range call failed — the line is not rendered, the reason is stated,
never a flat zero line and never an empty chart") and one error envelope in §5 carrying the failed read's reason.
⛔ **The build cell this spec unblocks must not be cut until that lands**, because building to the spec as written
produces a chart that renders a read failure as a quiet security.

Everything else in the spec is strong: the dense floor, the tier-stack toggle answering Andrew's own question at
day grain, the strongest-first order with its two-clause tie-break, the every-span-carries-its-headline rule for
FWD-6, and the explicit refusal to invent an event where the rule is not met.

## JUDGMENT 2 -- `HVST-h-10` AC5, the run report: **PASS**, with a round-level finding that outranks it

**The question:** does `RUN_REPORT.md` show that every article from each publisher, and the listing page that found
it, is re-openable from the store and matching what was received, with every UNRESOLVED publisher carrying its
reason?

**PASS on its own terms:**
- **Re-read:** `bronze_reread 14 of 14, mismatch 0` — every bronze key this run put re-reads from S3 and matches
  its recorded sha256.
- **Every unresolved publisher carries its reason**, and the reasons are specific rather than generic: sa
  `upstream_unavailable` (HTTP 502 after 24 accepted), bbg `error` (a real verification challenge mid-repair), ft
  `request_rejected` (HTTP 403), barrons `request_rejected` (challenge after a successful re-auth), wsj
  `complete_candidates`. **Three unplanned vendor-touching events are named rather than absorbed**, per the CTO's
  residual.

⛔ **BUT THE ROUND-LEVEL TRUTH IS BIGGER THAN THE CRITERION, AND I STATE IT SO NOBODY READS "10 OF 10 TERMINAL" AS
FWD-1 REALIZED.** FWD-1's own bar is *every article from each of the five publishers, AND THE LISTING PAGE THAT
FOUND IT*. Measured here, by object census over the whole bucket:

| publisher | bronze articles | bronze listing pages |
|---|---|---|
| wsj | 26 | **2** |
| seeking-alpha | 29 | **0** |
| bloomberg | 19 | **0** |
| ft | 14 | **0** |
| barrons | 15 | **0** |

**Only wsj has a stored listing page at all.** sa's three genuinely-new articles from this run have none, and three
of five publishers yielded nothing to store. **FWD-1 IS NOT REALIZED**, and the run report does not claim it is.
The cell did what it was told; the outcome needs publishers that answer.

⚠ **MY OWN NEAR MISS, RECORDED:** my census counts OBJECTS, and the packet's silver figures are ROWS. A parquet
part file holds many rows, so "silver 86" (objects, mine) and "97 silver rows" (the issuer's) are different grains
and do not disagree. **I nearly wrote a discrepancy that does not exist.** Sixth instance tonight of the same
family, caught before it reached a sentence.

## Row dispositions -- 19 of 19

**GRADUATED (real, and each needs a cell or an owner):**
- **`Z-S1`** — SA and Bloomberg "raw_bytes" are `json.dumps` re-serialisations of parsed JSON, not the bytes
  received. That is `C-HV-BRONZE-AS-RECEIVED`'s own subject, and the contract's WSJ/FT-versus-JSON split assumes a
  received form that this path does not preserve.
- **`Z-S2`** — the gold mention table has no publisher column, so `publishers_distinct` parses a key prefix. ⚠ **MY
  STANDING CONDITION, as sent to the CTO: whichever way it is ruled, the artifact that settles it is a PRINTED
  SHAPE READ of the table's actual columns beside the count** — the issuer's own first re-derivation read a
  publisher field, got `None` on all 86 rows and computed 0 events against 5 written.
- **`Z-W9-S1`** — `store.silver_append` names its object by `run_stamp` at second precision under an unconditional
  `IfNoneMatch`, so same-second siblings collide silently. Worked around in this project's writers; **the library
  still has it**, which makes it estate-shaped rather than this project's.
- **`Z-W10-S3`** — the un-root-caused monkeypatch trap. **Contained by the ratified conftest poison, NOT explained
  by it.** Stays open on the mechanism; I do not close a fixed symptom over an unexplained cause.
- **`Z-W10-S2`, `Z-W10-S6`** — the CLI paths that could never engage harvest-grammar mode and never wired a client
  into the uploader. The run's evidence is consistent with a fix, **but I have not measured the wiring myself**, so
  their remediation is owed a printed wiring check rather than an inference from a successful run.
- **`Z-W10-S8`** — the WSJ extractor's whole-config pull and the mixed-type schema break. Its fix is built and
  verified offline (`Z-W10-S9`), silver rebuilt from held bronze with no vendor call, `remaining_pending 11 -> 0`.
  **Graduated so the remediation row records it; the fix is real.**
- **`Z-W8-S2`** — the order's own grading command returns rc=1 INVALID on a correctly-formed instance. **A TOOLING
  defect in `.tools/`, outside this project's lane**, and it goes to the fabric's owner with the other three.

**DISMISSED (issuer-text, process, or resolution records):** `Z-W8-S1` (a default text-mode read reporting a crlf
count), `Z-W1-S1`, `Z-W1-S2`, `Z-W1-S3`, `Z-W3-S1`, `Z-W10-S1`, `Z-W10-S5` (the fourth instance of the S3 class,
covered by the ratified remedy), `Z-W10-S7`, `Z-W10-S10` (the AC6 text a phase behind, twice, caught by the worker
both times and graded by intent), `Z-W10-S9` (S8's fix record), and **`Z-W10-S4`** — the two granted acts that
landed nothing. ⭐ **That one is dismissed as a RECORDED COST with its root cause in the issuer's own words: a sized
plan proves COST, not CORRECTNESS.** Three granted vendor acts were spent to land one, and the third succeeded only
after a no-network rehearsal with a PROVEN poison drove the whole handler. **The cost is real and the lesson is
banked; it is not a defect of any cell in this round.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:45Z",
    "one_line": "L9 GRADE RECORD for round 1: 10 of 10 terminal, sweep 56 PASS / 1 FAIL / 2 UNVERIFIABLE of 59; h-10 AC3's FAIL stands and is admissible under R4 (http_events 0 shows no call occurred); h-8 AC3 FAILS on one clause -- no read-failure state; h-10 AC5 PASSES while FWD-1 is NOT REALIZED (only wsj has a stored listing page, 3 of 5 publishers yielded nothing).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_HARVST --round 1: PASS 56 / FAIL 1 / UNVERIFIABLE 2 of 59 over 10 orders; criterion ids 4+12+4+6+6+6+6+5+3+7 = 59; judgment=\"true\" in 2.",
        "Object census over s3://opal-data-harvest by publisher and kind: bronze listing pages wsj 2, seeking-alpha 0, bloomberg 0, ft 0, barrons 0; bronze articles 26/29/19/14/15.",
        "SPEC_SECTION_timeline.md read in full: SS6 enumerates Loading, quiet security, floor clamp, PARTIAL/DENIED and never-collected; a case-insensitive search for error/failure/refused states returns only DATA states read from chatter_daily.",
        "RUN_REPORT.md: bronze_reread 14 of 14 mismatch 0; five publishers each carrying a specific stop reason; three unplanned vendor-touching events named rather than absorbed."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it; judgment criteria are graded here and never self-graded.",
    "world_is": "Ten cells met their orders; one criterion failed honestly, one judgment artifact omits a state whose absence has already cost the sibling project days, and FWD-1 is not realized because three publishers refused.",
    "notes": "DENOMINATOR CORRECTION: the packet says 12 channel rows; the channel holds 19, all non-terminal before this adjudication. MY OWN NEAR MISS: my census counts OBJECTS and the packet's silver figures are ROWS -- different grains, not a discrepancy; caught before it reached a sentence.",
    "dismissal_reason": "Grade record: this row carries the round-1 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_HARVST-Z-C-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:45Z",
    "one_line": "GRADUATED: Z-S1 (raw_bytes are re-serialisations, not received bytes), Z-S2 (no publisher column; settle it with a printed shape read), Z-W9-S1 (silver_append's same-second collision, still in the library), Z-W10-S3 (monkeypatch trap contained but un-root-caused), Z-W10-S2 and Z-W10-S6 (CLI wiring, remediation owed a printed check rather than an inference), Z-W10-S8 (WSJ extractor, fix built and verified offline), Z-W8-S2 (a .tools grading command returning INVALID on a valid instance -- fabric's, not this project's).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Each row's own measurement, read here in the channel at HEAD.",
        "Z-W10-S8's fix: silver rebuilt from held bronze with no vendor call, remaining_pending 11 -> 0, two new test arms including no_key_loss_recovered 7 of 7.",
        "Z-W9-S1 is in lib/research/harvest/store.py, shared beyond this project."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Bronze is the bytes as received; a derived count reads a column that exists; a writer cannot silently drop a sibling object; a grading tool accepts a valid instance.",
    "world_is": "Each is a real defect with a bounded remedy; two are estate-shaped rather than this project's.",
    "notes": "Owners: Z-W9-S1 and Z-W8-S2 are the fabric's (library and .tools), alongside AMGT_RESAPP's portal-lane and .scratch registry gaps. The rest are 2.0.0_SA_COO~Y's recut. Remediation rows owed at L10. Z-W10-S3 stays open on its MECHANISM: containment is not explanation.",
    "adjudicates": [
      "AMGT_HARVST-Z-S1",
      "AMGT_HARVST-Z-S2",
      "AMGT_HARVST-Z-W9-S1",
      "AMGT_HARVST-Z-W10-S2",
      "AMGT_HARVST-Z-W10-S3",
      "AMGT_HARVST-Z-W10-S6",
      "AMGT_HARVST-Z-W10-S8",
      "AMGT_HARVST-Z-W8-S2"
    ]
  },
  {
    "id": "AMGT_HARVST-Z-C-S3",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T01:45Z",
    "one_line": "DISMISSED: the eleven issuer-text, process and resolution rows, including Z-W10-S4 -- three granted vendor acts spent to land one, dismissed as a RECORDED COST whose root cause is the issuer's own sentence: a sized plan proves COST, not CORRECTNESS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-W10-S7 and Z-W10-S10: the AC6 expect text fell a phase behind twice and the worker caught it both times; graded by intent.",
        "Z-W10-S5: the fourth instance of the S3 class, covered by the ratified package-level conftest poison.",
        "Z-W10-S4: the first two granted acts landed nothing, both on issuer specification defects; the third succeeded after a no-network rehearsal with a PROVEN poison drove the whole handler."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "An order's text matches the phase it grades; a granted vendor act lands what it was granted for.",
    "world_is": "Each was caught at execution by a worker or by the issuer's own control, and none reached a served value.",
    "notes": "The cost row is dismissed, not minimised: two grants were spent on specification defects and the lesson is banked in the issuer's own words. Z-W8-S1 is a default text-mode read reporting a crlf count -- the same encoding trap CLAUDE.md names.",
    "adjudicates": [
      "AMGT_HARVST-Z-W8-S1",
      "AMGT_HARVST-Z-W1-S1",
      "AMGT_HARVST-Z-W1-S2",
      "AMGT_HARVST-Z-W1-S3",
      "AMGT_HARVST-Z-W3-S1",
      "AMGT_HARVST-Z-W10-S1",
      "AMGT_HARVST-Z-W10-S4",
      "AMGT_HARVST-Z-W10-S5",
      "AMGT_HARVST-Z-W10-S7",
      "AMGT_HARVST-Z-W10-S9",
      "AMGT_HARVST-Z-W10-S10"
    ],
    "dismissal_reason": "Issuer-text defects, process disclosures, a resolution record and one recorded cost; every one caught at execution and none reaching a served value."
  }
]
```
