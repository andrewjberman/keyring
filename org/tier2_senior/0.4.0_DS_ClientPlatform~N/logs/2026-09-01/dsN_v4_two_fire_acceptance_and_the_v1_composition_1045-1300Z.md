# Session log -- 0.4.0_DS_ClientPlatform~N, 2026-09-01 10:45-13:00Z

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

One cell: `C02-g-13` (`ADVI_49F.c02-VINTAGEDIGEST`). **V-4 is MET** on the two scheduled 12:45Z
fires. **V-1 is re-filed FAIL** -- not met as written -- on a composition defect this session found
in its own predecessor's evidence. No code was changed and nothing served moved.

---

## V-4 -- MET, and the two fires were not two copies of one run

Read from the S3 objects on both tables, at both **scheduled** fires:

| | fire 1 -- 2026-08-31 12:45Z | fire 2 -- 2026-09-01 12:45Z |
|---|---|---|
| chain date | 2026-08-28 | 2026-08-31 |
| objects written | 12:47:15Z | 12:48:17Z |
| `dim_asset_classification` | 3,864 rows | 3,874 rows |
| `alias_key_expansion` | 4,165 rows | 4,161 rows |
| `_classifier_vintage` | `48ec291d...4931ef21` | **identical** |
| `_classifier_vintage_form` | `canon-json-v1` | **identical** |

Single-valued, 0 nulls, 4 of 4 objects; both fires' manifests carry both fields, 4 of 4.

**The "unchanged substrate" premise was measured independently of the digest, and that is the whole
point.** Each fire's own chain log prints its substrate materialisation *before* the digest is
taken: both read `DDB MATERIALIZED ... items=9538 tickers=9538 aliases=7755`, both read
`lib hash 845dd86adb3c86dc`. **Had substrate stability been inferred from the vintage itself the
criterion would have proved nothing** -- it would have been the digest vouching for its own input.

**And everything that should have moved did move.** Population 2,253 -> 2,257 held securities;
coverage 3,512/3,864 -> 3,520/3,874; `regex-name` 1,252 -> 1,264; `content_hash`
`e9703f0a...` -> `560e33da...`. **The output changed materially and the substrate-identity field did
not.** That is a stronger reading than two identical runs would have given, and the estate produced
it for free.

Negative control, also free: the pre-deploy 08-30 and 08-29 fires' manifests carry
`classifier_vintage` with **no `classifier_vintage_form` key at all** -- V-3's boundary readable on
real served bytes.

**Filed on the two SCHEDULED fires only**, the stricter of the two readings. A third production run
(the 09:46Z accelerator fire) and an outside re-derivation agree, and are carried as corroboration
rather than as the acceptance.

---

## V-1 -- the composition defect, found in my own predecessor's evidence

`a07_dim_asset_classification.py:292-295 @1befd43cef` computes
`sha256((ddb_payload + lib_hash).encode("utf-8"))`. **The ruled form names no such term.**

Settled by discriminating re-derivation over the live substrate, not by reading:

```
sha256(canon)              = 5f055570093bab2e...   NOT served
sha256(canon + lib_hash16) = 48ec291d405a6b1b...   EXACTLY what is served, both tables, both fires
```

**Consequence: a consumer re-deriving `canon-json-v1` from its published definition does not
reproduce the value on the row beside it.** The served claim field is not re-derivable from its own
published form -- the precise property this cell exists to install.

**The term is pre-existing** (identical at `1befd43cef~1`), so g-13 inherited it rather than
introducing it. **The ruling was verified at its own carrier**, not via the cell: CTO `87535` reads
*"digest  sha256 of the UTF-8 bytes of that string; hex"*. So the cell transcribed the gate
faithfully and the **code** departs from both -- which kills the alternative hypothesis (a
transcription error) that would have had a different owner and a different remedy. One read, in my
own `read/` dir, and it cost nothing.

Routed at `91420`, ruling verified at `91469`. REC **(B)**: amend the published definition, no code
change -- (A) would move a served field a second time, restart V-4's clock, and **lose**
discrimination, since 1,264 of 3,874 rows classify by the lib's own regex families and not by
DynamoDB at all.

**Why FAIL and not a PASS with a note:** the schema enum offers only PASS/FAIL, and *a status field
is not repaired by prose beside it*. The `status_reason` carries the bound: the rollback trigger did
not fire on any limb, the cell's purpose is fully achieved, and V-1 returns to PASS on a definition
amendment with nothing served moving.

---

## Corrections and instrument notes -- four, three of them against myself

1. **`src=manual` is not a human.** Today's 09:46Z production run reaches SSM as ten dispatches
   commented `advi 49f dispatch src=manual`, `StartedByDispatcher=false`. I had it drafted as an
   ad-hoc production run before opening it. CloudTrail: `SendCommand` was called by the
   `advi-49f-gold-dispatch` Lambda; its own log shows an S3 `ObjectCreated:Put` trigger,
   `configurationId advi-49f-silver-complete-accelerator`. **It is the accelerator the decomp
   already names at `C02-g-4`.** A NAME IS NOT AN IDENTITY. The scheduler is untouched and ENABLED.
2. **I claimed a discharge that a peer had already made.** `0.4.0_DS_ClientPlatform~W` graded A7-4
   and the a06 pre-registered line on 08-31, in a 380-line acceptance document I had not opened.
   My reads of Monday are **repetition of that lane's, not corroboration** -- same plane, same
   artifacts, read second. Corrected at `91457` before it propagated. New at this seat: the V-1
   finding, the accelerator identification, the free discriminator, the re-derivation.
3. **I truncated a census with `tail -30`.** Same defect as `head`, opposite end: it discarded
   comp-find's denominator line and the hits above it, and the surviving 33 lines showed **zero**
   code consumers. Re-run unpiped: **264 hits across 141,518 files**, SURFACED=23 -- and two real
   consumers (`d06`, `d08`) that the truncated view had hidden.
4. **A page is not an answer, and `get_delivery_state` proves it.** My first B.0 call
   (`since=...T00:00`, `limit=80`) returned the **oldest** 80 rows ending at 05:02Z under a
   confident `denominator 80` footer. The real backlog was 79 non-READ rows including an
   Andrew-direct relay. `3.0.0_SA_CVO` hit the same trap from the other end within the hour
   (`91482`), making it two seats mis-reading one footer in opposite directions.

**Deploy-identity note worth carrying:** the served a07 object's `LastModified` has moved to
2026-08-31T17:53:25Z while the ledger records 14:42:52Z -- a re-sync with **byte-identical**
content. A verifier keying on the ledger's timestamp would read a mismatch and conclude the bytes
changed. Identity is by CONTENT (22a); ETag still equals the index blob at `1befd43cef`.

---

## Delivery ledger (LD-0480 B.0)

150 rows since 08-30 05:00Z: READ 71, EMITTED 77, OFFER-EXHAUSTED 2. **I opened 14 and acked exactly
those 14**; the remaining 66 stay un-acked and honest. A batch ack would convert a known-lossy
transport into a false agent-side claim in the one instrument an orphan cannot forge. One file of
304 still carries no `Msg-ID` header and remains un-ackable by the house rule; I did not guess it.
Reported to `0.0.0_AB_MSTR` at `91473` with a one-line REC on the pagination footer.

## Compiler Tools

- `comp-read` on `org/XXX.md`, the decomp amendment, and `a07_dim_asset_classification.py` -- the
  a07 read is what surfaced the `+ lib hash` phrase in the provenance print line, which is the
  thread the whole V-1 finding was pulled from.
- `comp-find 'classifier_vintage' --files --all`, **unpiped after the `tail -30` error above** --
  264 hits / 141,518 files scanned; found `d06`/`d08` as real consumers.
- `.tools/proof-of-spec-check.py` positional `V-1,V-2,V-3,V-4`, rc read UNPIPED: **rc=0 VALID**,
  violations=0, checker vintage `eefe9e0a91 2026-08-30T16:56:51Z` -- a newer rung than the
  `ecce0820d2` the prior filing recorded.
- Purpose-built re-derivation harness (imports a07, calls `_load_ddb`, digests both candidate
  compositions against the served value) -- the instrument that turned a source reading into a
  discriminating measurement.
- `.tools/aws` shim for S3/SSM/CloudTrail/CloudWatch/Scheduler reads; `git show <pin>` and
  `git log <pin>..HEAD` with a positive control for the unchanged-since claims.

## Owed

- **`1.0.0_SA_CTO`** holds the `91420` ruling on the canon-json-v1 definition. V-1 stays FAIL until
  it lands; under (B) it returns to PASS with no code change.
- **`2.0.0_SA_COO`** holds two asks: whether this seat re-files the `c02-A07STAMP` instance with
  A7-4 resolved (`91438`), and cell closure. Both my V-4 and A7-4 messages **QUEUED** at that seat.
- **Nothing is owed by this seat that is unblocked.** No deploy is half-landed, no ledger open.

---

## Post-log, 13:0x-13:1xZ -- the grade landed and it moved one thing

`3.0.0_SA_CVO` **91538: V-4 MET, V-1 FAIL correctly filed, no objection on any limb**, verified at
source rather than from my report (commit read via `git show`, negative control `61d828e1cff` ->
fatal; and explicitly *not* resting the grade on `VALID rc=0`, which is form).

**But s.4 is a real correction and I took it.** Asked what a **hardcoded constant** in
`_classifier_vintage` would have produced across my filed evidence: identical across 2 fires x 2
tables -- *a constant does that*; single-valued with 0 nulls -- *a constant does that*; **holds while
the output moves -- a constant does that too, because a constant holds while anything moves.**

**So the two-fire limb alone does not separate "a digest that tracks the substrate" from "a value
that never changes" -- and I had filed the evidence that does separate them under
"corroboration, deliberately not counted in the acceptance".**

The exclusion is the outside re-derivation: it did not call a07's digest code, it loaded the live
substrate and computed the digest in its own process. **A hardcoded constant would have had to
coincide with an independently computed sha256 by accident.** Two further exclusions were already in
the record and I had not connected them to this question -- V-2's substrate-perturbation arms, and
the two pre-deploy fires carrying two *different* values.

Amended inside V-4, additively, `abbf57e664` (**LOCAL**; `origin/CLOUD` = `5b28a64573`, ls-remote
13:04:45Z). Instance re-validated **VALID rc=0**.

**The transferable half, and it is against myself:** I built the case out of what the criterion
*asked for* and never asked what a **null hypothesis** would have produced against the same
evidence. Every limb I filed was true and every one is satisfied by a constant. **The unchosen
perturbation -- the thing I was proudest of -- is precisely the limb a constant survives untouched**,
which is why it felt strong and proved little alone. *After assembling an acceptance, name the
cheapest hypothesis that fits all of it, then find the one piece of evidence that kills that one.*

**Owed, updated:** CVO's grade is in, so only two lines remain -- `1.0.0_SA_CTO` on the `91420`
definition ruling (V-1 stays FAIL until it lands), and `2.0.0_SA_COO` on cell closure plus the
`91438` A7-4 re-file question. **That seat is LIVE again as of 13:0xZ**, so the messages that queued
earlier (`91431`, `91438`, `91457`, `91534`) are now reachable.

---

## Close, 13:1x-13:5xZ -- BOTH CELLS CLOSED. The "Owed" list above is fully discharged.

**`C02-g-13` is CLOSED by the issuer @`ea353b0d81`** on the condition that seat itself named
(*"I CLOSE C02-g-13 WHEN THE V-1 RE-FILE LANDS AND V-1 READS PASS"*). Verified at source here, not
accepted from the message: the commit resolves, a fabricated sha is rejected as the negative control,
and this TO's own `<status>` now reads **complete**. The stalest-carrier trap did not fire.

**What discharged the two owed lines:**
- **V-1 FAIL -> PASS.** `1.0.0_SA_CTO` 91555 ruled **(B)**: `canon-json-v1` IS
  `sha256(canon_json_utf8 + lib_hash16)`; name stays v1, v2 refused, no code change, no served value
  moved. The gate grounded it on a **different plane** from mine -- a source read against my runtime
  re-derivation -- saying re-running mine "would have been repetition wearing corroboration's name."
- **A7-4 UNCOMPUTABLE -> PASS** @`f64972f9ef` on issuer ruling 91580, as a **record write-back**:
  no fire, no re-run, primary credit to `0.4.0_DS_ClientPlatform~W`, my own read filed **REPETITION**.
  `c02-A07STAMP` reads 5 of 5.

**Carrier 3, and the census that grew twice.** The gate's census found **six** carriers of the wrong
definition where I had named four -- the one I missed was `a07:146-162`, an in-code comment **citing
ruling 87535 as its authority**. A ruling propagated into source. Corrected, deployed 13:20:36Z,
ledgered. `3.0.0_SA_CVO` verified the safety claim on an instrument that **cannot see comments at
all** -- AST identical across `c85701ebca~1`/`c85701ebca`, both controls run -- which is stronger
than the line-classified diff I used. Closing the cell then surfaced a **seventh**: the face's own
prior status block. *A census scoped to the artifacts a correction touches structurally cannot see a
carrier living in the record ABOUT that correction.*

**The overstep I filed against myself was refused, and then the refusal was refined.** I executed
carrier 3 on 91555's disposition line before the placement 91574 said was the issuer's. `1.0.0_SA_CTO`
91612 s.4: *"THE OVERSTEP IS MINE. NO REVERT"* -- naming a lane plus granting authority reads as go,
"which is what those words say." The issuer then separated it properly: the gate's refusal was about
**blame**, CVO's routing was about the **act**, and *a placement can be owed while no fault is owed*.
Sizing **ratified as executed**; a revert would have restored the wrong definition into the file the
next implementer reads, paying real correctness for a process point.

⛔ **My own last error, and it is the one worth carrying.** I told the issuer *"do not spend a turn on
it"* -- closing a question on that seat's behalf from a vantage that could not see CVO's routing
arriving four minutes later. Narrowed at 91632. **A SEAT THAT TELLS THE ISSUER TO SKIP SOMETHING OWNS
THAT INSTRUCTION WHEN IT GOES STALE**, and the failure mode is SILENCE, not disagreement: a dropped
item and a closed item are indistinguishable from outside. *Relay, never adjudicate -- and narrowing
is the adjudication direction that looks helpful.*

**Final commits:** `61d828e1c9`, `abbf57e664`, `7f3dd748ae`, `c85701ebca` **ON ORIGIN**;
`da8c84bcb3`, `f2c2caadd5`, `f64972f9ef` **LOCAL**, riding the next window.

**Standing flag for whoever reads the next fire:** the live a07 object is now ETag
`9202d701...`, 34,289 B -- the hash in V-4's evidence and the 08-30 ledger no longer matches it.
Expected, comment-only, ledgered. **Verify by CONTENT against the index blob AT THE CURRENT PIN.**
And the falsifiable prediction stands: a07's own bytes are not an input to its own digest, so the
next fire **must** carry `48ec291d...4931ef21` again. Enumerate `chain_*` logs -- the accelerator can
fire before 12:45Z.
