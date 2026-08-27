# ANDREW-DIRECT 2026-08-27 ~20:0xZ — THE PER-PARTNER SOURCE→TAXONOMY MAP

**Received by:** `0.4.0_DS_ClientPlatform~Z` (D1_CATVIEWS DS lane, Rule 27)
**Channel:** Andrew directly at this seat's terminal
**His framing:** *"I have gone through this countless times but I'm going to do it again just to
make sure it lands."* — the same complaint behind his 08-26 16:3xZ instruction to CTO
(*"look through logs and records and try to compile it all... we have gone over this many times"*).
**That repetition IS the finding: this content keeps failing to persist.** Hence a durable record.

> ⛔ **VERBATIM. THE PHRASING IS THE RULING — do not paraphrase this block.**

> *"We ingest all assets through opal-data-assets, i will now break down each partner by their data
> source as it rleates to the asset taxonomy here. For 49 Financial, they have the SMAs via smartx,
> those include PFOE DIVZ, a handful of tax accounts you should be able to find there somewhere
> (egress permitted) as well. Models are obvious, they all come from SmartX too. Client segment is
> always residual post-models and smas, in the case of 49, they are all opal-supervised in the
> context of the 0824 schwab account which is what feeds the portal. Moving to inflection, they have
> no SMAs, so its very easy, just the models from Eclipse already handled on logic, and any balance
> is Client Opal-Unsupervised. Regarding Cottonwood, its a little more complex. Models all come from
> rebalancer, we have already established what is primary and what is custom (opal fixed income).
> SMAs they actually don't have any (in the SMAs as a strategy bucket which is what we've built
> here). Regarding "Client" the contents of any portfolio that has opal models in it is considered
> supervised, so essentially any residual value in an account with an opal model falls into Client
> Opal Supervised, everything else is Opal Unsupervised as athe book-wide plug figure."*

---

## 1. THE MAP, AS HE STATED IT

| partner | Models source | SMAs | Client resolution |
|---|---|---|---|
| **49 Financial** | SmartX | **SmartX**: PFOE, DIVZ, + *"a handful of tax accounts"* (**egress permitted** to find them) | **ALL Opal-Supervised**, *"in the context of the 0824 schwab account which is what feeds the portal"* |
| **Inflection** | **Eclipse**, *"already handled on logic"* | **NONE** | **ALL Client Opal-Unsupervised** (*"any balance"*) |
| **Cottonwood** | **Rebalancer**; Primary vs Custom already established (Opal Fixed Income = Custom) | **NONE** — *"in the SMAs as a strategy bucket which is what we've built here"* | **DERIVED**: any portfolio containing an Opal model → its residual value is **Client Opal Supervised**; **everything else is Opal Unsupervised as the book-wide plug figure** |

**THE GENERAL RULE, stated once and binding on all three:**
> *"Client segment is always **residual post-models and smas**."*

Ingest substrate: **`opal-data-assets`**, for all partners. Measured layout — the bucket partitions
by **SOURCE SYSTEM**, not by firm: `blackdiamond/`, `eclipse/`, `orion/`, `smartx/`, `gold/`,
`config/`. (`cottonwood/` at top level returns nothing; positive control — the bucket lists.)

---

## 2. CORROBORATION — HE ASKED FOR IT AND IT HOLDS

Found via `comp-find -i 'opal.?unsupervised'` (**DENOMINATOR: 38 hits / 27,267 files scanned;
bands HEAD=5 SURFACED=8 CONFIG=5 DOC=20**), on his suggestion that a prior directive exists.

**`MP_TAXONOMY_COMPILED_REFERENCE_20260826.md` (`1.0.0_SA_CTO`) is the artifact he was thinking of**,
and today's word **CONFIRMS it on every overlapping point**:

| today's word | compiled reference | verdict |
|---|---|---|
| L1 Client = Opal Supervised / Opal Unsupervised | §1: same two values, fee-taking discriminator | ✅ agrees |
| Cottonwood: portfolio with Opal models → residual is supervised | §2: *"Opal-Supervised — DERIVED: the residual account value of any account with Opal Models contained within the portfolio"* (A3, 08-25) | ✅ **near-verbatim agreement** |
| Client = residual post-models-and-SMAs | §2's "residual account value" framing | ✅ agrees |
| 49F SMAs = PFOE, DIVZ, tax | §1: **L1 SMAs = Tax · Muni · DIVZ · PFOE**, an OPEN enumeration (A2/A6) | ✅ agrees |
| three cards (Models/SMAs/Client) | A6 08-26 16:36Z names the same three; reference reads it as elliptical of the four-value L0 | ✅ agrees |

⭐ **NEW TODAY, and absent from the compiled reference — this is the part worth persisting:**
1. **The per-partner DATA-SOURCE mapping** (SmartX / Eclipse / Rebalancer). The reference compiles
   the TAXONOMY; it does not map partner → source.
2. **Per-firm Client resolution as a closed set** across all three partners in one statement.
3. **49F scope qualifier:** *"the 0824 schwab account which is what feeds the portal."*
4. **Cottonwood Unsupervised = "the book-wide plug figure"** — i.e. computed by SUBTRACTION.
   ⚠ Consequence: an error in Supervised propagates directly into Unsupervised. That is the same
   reasoning the standing Cottonwood hold uses (*"the error is UNBOUNDED"*), so his framing
   **corroborates the hold's logic** rather than relaxing it.
5. **Egress permitted** for the 49F tax accounts in SmartX.

---

## 3. MEASURED — HIS THREE FIRM RULES ARE **ALREADY ENCODED AND CORRECT**

`data/mdpf/scripts/gold/mdpf_category_registry.py`:

```python
CLIENT_L1_RULE = {
    "49financial": CLIENT_L1_ALL_SUPERVISED,     # <- "they are all opal-supervised"
    "inflection":  CLIENT_L1_ALL_UNSUPERVISED,   # <- "any balance is Client Opal-Unsupervised"
    "cottonwood":  CLIENT_L1_DERIVED,            # <- the Opal-model-portfolio predicate
}
```

**All three match his word exactly. No registry edit is implied by this directive.**
(`global` deliberately has no entry — CTO 69348: it is a roll-up, not a client base.)

⛔ **THE AVAILABLE ERROR HERE IS TO READ A SOVEREIGN CONFIRMATION AS A CHANGE ORDER** and go re-do
encoded work. Second instance in two turns — his Client L1 statement was likewise already true in
the emitted data.

---

## 4. ⭐ WHAT THIS DIRECTIVE SURFACED — THE COTTONWOOD HOLD'S BLOCKER IS DISCHARGED AT BRONZE

His Cottonwood rule sent me to re-read `CLIENT_L1_HELD["cottonwood"]`, whose stated blocker is an
**ingest coverage gap**, remedy named as *"MODEL_DETAIL_SCOPE=all with the descent guard OFF"*.

**MEASURED NOW, live, with controls:**

```
LIVE LAMBDA ENV (get-function-configuration, cot-rebalancer-runner)
    MODEL_DETAIL_SCOPE = "all"          <- APPLIED. Code DEFAULT at :71 is still
                                           "opal_closure", so this is an env fact,
                                           not a code fact. DESIRED != APPLIED.

BRONZE rebalancer_model_detail, file counts (client-side count; KeyCount NOT trusted)
    2026-08-24 :  30      <- the hold's own measurement
    2026-08-25 :  30
    2026-08-26 :  81      <- the jump
    2026-08-27 :  83

THE HOLD'S TWO NAMED SPECIMENS (its largest uncovered accounts, $46,436,739.80):
    Anna *9237  1ae61190-70fb-4d6c-a259-cee9019ed125  -> PRESENT
    Anna *9238  6ae9e540-9b27-474c-8ad9-3dfc5131c530  -> PRESENT
    NEGATIVE CONTROL, fabricated uuid                 -> ABSENT (the probe can say no)
```

>> **THE HOLD'S STATED BLOCKER NO LONGER HOLDS AT THE BRONZE RUNG, ON THE HOLD'S OWN CHOSEN
   SPECIMENS.** The hold text itself warns about exactly this: *"A LIVE HOLD CITING A DEAD REASON IS
   THE MIRROR OF A DEAD RULING CITED AS LIVE AUTHORITY."* <<

⛔ **WHAT I DO NOT CLAIM, AND THE GAP IS REAL:**
- **83 files ≠ 64/64 roster coverage.** `all` = roster UNION closure, so the count includes closure
  children. I did **not** compute per-roster-model coverage.
- I did **not** verify `silver/fact_model_definition` reflects the new bronze, and **bronze presence
  is not silver correctness**.
- **This is NOT a lift.** A disarm condition being met is not a ship decision, and the hold is
  `2.0.0_SA_COO~Z`'s with a named STOP. **Surfaced for re-measurement by its owner, not lifted here.**

---

## 5. EGRESS — AUTHORIZED, AND PROBABLY NOT NEEDED

*"(egress permitted)"* is his explicit per-use word for finding the 49F tax accounts in SmartX,
which CLAUDE.md otherwise forbids (*availability is not authorization*).

⚠ **But SmartX data is already landed in our own S3** — `smartx/platform/silver/
fact_allocation_account_map/` is read by `data/assets/scripts/gold/runners_49f/a00_runner.py:55`.
**The tax accounts are likely findable from our own silver without any vendor call.** Prefer the
landed artifact; keep the egress grant unspent unless the internal read comes up short.

---

## 6. STATUS

**Recorded and broadcast the same turn** per `org/XXX.md`. **NOT self-assigned** — no registry edit
is implied, the Cottonwood item is COO's hold, and the 49F tax-account lookup is unseated work.
`D1_CATVIEWS` remains **NO-SHIP** (`@0d08954d4c`); nothing here touches that ruling's basis.
