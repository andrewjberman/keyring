# SERVE RULE — a positional path carries its identifying field, in the same call

**Status:** RULED (1.0.0_SA_CTO~Z, msg 2636, 2026-08-20). Binds this seat NOW.
**Placement:** here because `refs/REQUEST_CATALOG.md` is **G1-unwritable from this seat by
design** (Teams content can never become a prompt edit — the fence does not get an exception
for a rule I happen to agree with). **MSTR~Z folds the one line into the catalog at its next
integrator touch of these refs** — the §0b placement pattern. Until then, THIS is the
canonical home and the rule binds regardless of where it is written.
**No code changed anywhere.** S5 stands as landed `@598a96c3a8`; AE~Z's conditional
docstring line was withdrawn (msg 2640) so the record carries a single form.

---

## THE RULE

> **Whenever a served answer reads a POSITIONAL path, the SAME `--project` call carries the
> identifying field(s) beside the value.**

```
  WRONG (frameless)          portal_lookup get ... --project models.1.returns.YTD.model
                             -> 2.33          <- nothing here says "of ST"

  RIGHT (self-verifying)     portal_lookup get ... --project models.1.code \
                                                   --project models.1.name \
                                                   --project models.1.returns.YTD.model
                             -> "ST" / "Short Term" / 2.33
```

One subprocess, **0.797s measured**. The proof rides free.

## WHY — this is not hygiene, it is the afternoon's class one more time

`models.1` means **index 1**, not "the ST model". Today the array order is
UST/ST/INT/LT/ULT, so index 1 *is* ST — **by accident of order, not by contract.** Nothing
in the artifact guarantees that order and **nothing in the output `2.33` says which model it
came from.**

If a producer ever reorders that array, the path keeps returning a **well-formed, confident
number that is silently a different model's.** The concrete failure is quoting UST's
**+1.91** to Andrew as ST's — correct-looking, unfalsifiable from the output, in a
client-facing sentence.

**Same shape as every other defect found today:** the instrument answers *precisely* in a
domain the caller did not intend, and the output does not carry its own frame
(`latest-per-chat` when you meant every message; `count: 1` that never says "1 of 2";
`2.33` that never says "of ST"). No amount of care catches a frameless number — only
printing the frame beside it does.

**I found this by luck, not by rule** — I projected `code` and `name` alongside the figure
in a smoke test without thinking about why. That is exactly why it is written down: the next
serve, under time pressure, would not have been so lucky.

## HOW TO FIND THE IDENTIFIER WHEN YOU DO NOT KNOW THE INDEX

`--find <identifying-key>` returns the whole map in one call — **verified at this seat**,
1.008s, rc=0:

```
FIND 'code': 5 match(es) across 540 keys walked (COMPLETE walk of the retrieved object).
  models.0.code = "UST"    models.1.code = "ST"     models.2.code = "INT"
  models.3.code = "LT"     models.4.code = "ULT"
```

This is why AE~Z's proposed `--find` value-match was **declined at build-ladder rung 2** and
why the decline is right: the tool **already** answers "which index is ST?" — adding a flag
for it would be code written for a question already answered. *(AE~Z demonstrated this
rather than asserting it; I verified it here rather than taking the demonstration, because I
am the seat that will depend on it mid-serve.)*

## SCOPE — where this binds

Any served figure read from an **array-indexed** path, in any channel. It does NOT bind
name-keyed paths (`returns.YTD.model` under an already-identified model is fine — the
identity is in the path). The test: **could a producer reorder something and leave my path
pointing at a different entity while still returning a valid value?** If yes, project the
identifier.

## RELATED, same seat, same day

- `threads/2026-08-20-andrew-responsiveness-test/2026-08-20.md` — the message-loss defect
  (latest-per-chat), the parent instance of this class.
- `logs/2026-08-20/f8_relaunch_and_speed_addendum_1600-1840Z.md` — the measured latency
  budget that became OPAL_ANALYST §11's scope law, and both successor duties.
- S5 `@598a96c3a8` — repeatable `--project` is what makes this rule free rather than a
  second subprocess. The capability and its discipline arrived together.
