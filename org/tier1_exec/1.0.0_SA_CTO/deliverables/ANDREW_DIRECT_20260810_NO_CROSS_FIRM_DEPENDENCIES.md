# ANDREW-DIRECT 2026-08-10 — NO CROSS-FIRM DEPENDENCIES ON PUBLISHING

**Recorded by:** `1.0.0_SA_CTO` at the CTO terminal · **broadcast same turn** (record+broadcast law).

---

## THE RULING, VERBATIM

> *"There is another issue that seems to be coming around quite a lot which I want to categorically
> rule against. I understand why the 'Global' scope is dependent upon the most recent date from all
> underlying firms, however that is the ONLY dependency that should exist. There should NEVER be
> cross-firm dependencies. I've heard comments here and there which seem to imply that there are
> dependencies from Inflection to 49, and similar concepts. If this does in fact exist, it needs to be
> remediated. There should never, ever be cross-firm dependencies on publishing."*

**SCOPE, read narrowly and stated so nobody widens it:**
- **PERMITTED — the one exception, named by him:** `global` depending on the **most recent date across
  all underlying firms**. Composition at Global is legitimate.
- **PROHIBITED:** any other cross-firm dependency. A firm's publish must not depend on a sibling firm.
- **DISPOSITION:** *"if this does in fact exist, it needs to be remediated"* — remediation is
  AUTHORIZED, conditional on the dependency being real. **It is real. Measured below.**

---

## ⛔ IT EXISTS. SOURCE-CONFIRMED, AND IT IS TODAY'S INFLECTION FAILURE.

`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:819-835` — verbatim:

```python
def derive_canonical_axis() -> list:
    """The canonical shared MDPF trading-day axis, derived ONCE per run from
    the DECLARED axis-source feed (fact_model_aum_daily -- route_bindings
    49financial model_leg; the participation meta's axis-source law).
    Criterion 2: sibling firms receive THIS axis from the orchestrator; ..."""
    aum = _cached("aum_daily", load_aum_daily)     # -> SMARTX_SILVER = "smartx/platform/silver"
    frontier = aum_days[-1] if aum_days else SERVED_AS_OF_FIRST
    dates = canonical_trading_axis(frontier)
```

`:72` `SMARTX_SILVER = "smartx/platform/silver"` · `:946-950` `FIRM_49F: {"model_leg": "smartx_aum_daily"}`

**⇒ EVERY FIRM'S AXIS IS DERIVED FROM 49FINANCIAL'S OWN FEED. `inflection` → `49financial` is exactly
the dependency he named, and he named it from hearing it in passing.**

**IT IS NOT THEORETICAL — IT IS TODAY'S OUTAGE.** The 49F-derived frontier landed on `2026-08-06`, a
date inflection's own feeds never carried, and inflection's cross-axis gate refused to emit. Global
inherited the failure. **Inflection HAS `2026-08-07` on both its own legs** (eclipse
`fact_portfolios_full`, orion `fact_assets`, both measured present). **On its OWN frontier, inflection
would have published.**

---

## ⛔ AND THE CODE ALREADY VIOLATES THE ESTATE'S OWN DECLARED CONFIG

`data/mdpf/config/route_bindings.yaml:28-33`:

```yaml
axis:
  note: "NYSE trading-day axis, each firm's OWN measured frontier
         (canonized SS2.1; no sibling-axis import)."
```

**THE DECLARED CONFIG SAYS *"each firm's OWN measured frontier"* AND *"NO SIBLING-AXIS IMPORT."*
THE CODE IMPORTS 49F'S AXIS TO EVERY SIBLING.**

>> **SO ANDREW'S RULING IS NOT A NEW CONSTRAINT — IT RESTATES A RULE THE ESTATE ALREADY CANONIZED
>> ("canonized SS2.1") AND THE CODE DOES NOT IMPLEMENT.** That changes the remediation's character
>> entirely: this is **not a design change requiring a decision. It is bringing code into compliance
>> with a binding it already claims to follow.**

⚠ **AND THE DOCSTRING CITES `route_bindings` AS ITS AUTHORITY WHILE CONTRADICTING `route_bindings`'
OWN AXIS NOTE** — *"the DECLARED axis-source feed (… route_bindings 49financial model_leg)."* It reads
the *firm's model_leg* binding and presents it as an *axis-source law*, which the config's axis section
explicitly forbids. **This is the citation-does-not-support-its-claim class I ruled on the DEBTCLEAN
PRD earlier today: it borrows authority it was never given, and the borrowed authority is what made
the violation look canonical to every reader since.**

### THE DEFENCE IN THE DOCSTRING, AND WHY IT DOES NOT SURVIVE
It argues: *"no firm ever reads another firm's ARTIFACT frontier, so a sibling build failure
structurally cannot re-axis anyone."* **That is true and it is not the point.** The design moved the
coupling from **artifacts** to **FEEDS** and treated the artifact-level fix as sufficient.
**A shared axis is a cross-firm dependency at whichever layer it is read** — and the failure it was
built to prevent (a sibling's state re-axing another firm) **happened anyway today, via the feed.**

---

## ✅ THE CORRECT PATTERN ALREADY EXISTS IN-ESTATE — COTTONWOOD IS ON IT

`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`:

```python
def self_derived_axis(gold_by_date: dict, holdings_avail: "set[str]") -> "list[str]":
    """ROW-4 ON-PATTERN AXIS (T1.C @5b42aff274 under the T2.B ruling @440d16e018):
    canonical NYSE trading days, SERVED_AS_OF_FIRST .. Cottonwood's OWN measured
    frontier = max across BOTH measured legs ..."""
```

**Cottonwood derives its OWN frontier from its OWN two legs. It is labelled "ON-PATTERN" and rides a
prior ruling (`@440d16e018`).** So the pattern is ratified, implemented, and running.

**⇒ BUILD LADDER RUNG 2: THE ESTATE ALREADY HAS THIS. The remediation is to bring `inflection` and
`49financial` onto the pattern `cottonwood` already uses — not to design anything.**

---

## REMEDIATION SCOPE — MEASURED, NOT ESTIMATED

| scope | axis today | verdict |
|---|---|---|
| `cottonwood` | **its own two legs** (`self_derived_axis`) | ✅ **COMPLIANT** |
| `inflection` | **49financial's SmartX feed** | ⛔ **VIOLATION — remediate** |
| `49financial` | its own feed *(which is also everyone else's)* | ⚠ compliant **by coincidence**, not construction |
| `global` | composes across firms | ✅ **PERMITTED — his named exception** |

⚠ **A KNOWN, ALREADY-NAMED WORK ITEM POINTS AT THE SAME PLACE:** `:1562-1567` skips limb (v) for
49financial because *"count axis reads the legacy served import, not the value's feed"* —
**"49F decouple is a PREREQUISITE for cross-axis coverage here."** A **"49F decouple"** is already
named in the producer's own source. **This ruling is its authorization.**

## ⛔ WHAT THIS RULING DOES *NOT* DECIDE

- **It does not decide the floor's schedule.** The 40-minute ordering gap (floor 13:00Z vs SmartX
  ~13:40Z) is a **separate** defect and remains his open question. *Note the interaction, because it
  is the good kind:* **once each firm reads its own frontier, 49F's landing time stops being able to
  select inflection's frontier at all** — so this remediation shrinks the ordering problem to 49F
  alone rather than the whole estate.
- **It does not authorize a backfill.** Inflection's `2026-08-06` hole is real and stays. His
  *"fix forward, current-day execution"* qualifier from the point-in-time ruling still binds.
- **It does not re-open Andrew's `(B)` floor ruling.**
- **LANE:** the edits are `data/mdpf/scripts/gold/**` and `data/assets/scripts/gold/**` —
  **`0.4.0_DS_ClientPlatform` by Rule 13, not this seat.** Routed, not written here, not gated.
