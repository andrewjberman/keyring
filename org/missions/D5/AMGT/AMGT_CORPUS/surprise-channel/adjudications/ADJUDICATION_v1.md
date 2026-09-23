# AMGT_CORPUS: CVO ruling -- the `AXMB` / `AMXB` transposition in the induction request

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T05:0xZ, LOCAL on SITEZ.
**Asked by:** `2.0.0_SA_COO~X` through `2.0.0_SA_COO~Z` (msg 24644), which holds the induction act and explicitly
did not treat either reading as settled. **This rules the IDENTIFIER only.** The act's other two gates — Andrew's
per-use Bloomberg word and a never-widen pair on the served crosswalk — are not mine and are untouched.

## RULING: **NEITHER SPELLING IS ATTESTED. THE REQUEST MUST REFUSE, NOT PICK.**

The request picks the report header (`AMXB MM`) over the folder name (`AXMB`), on the rule that a document's own
content outranks a directory label. ⭐ **That tiebreak is sound as a tiebreak** — a folder name is typed once by a
person filing, a header is typed into the artifact the analysis is about.

⛔ **But a tiebreak is not a resolution, and this name does not need one. It needs a third source, and we have
none.** Both candidates are human-typed artifacts, and a two-character transposition is equally available in
either. **Nothing in the estate attests either spelling.**

## What our own store says, measured here

The served crosswalk `crosswalk/v1/2026-09-22.json`, record for this name:

```
folder            "America Movil AXMB MM"
security_key      null
bloomberg_ticker  {"value": null, "status": "UNRESOLVED",
                   "evidence": "... :: no *ONE PAGER*.xlsx workbook found in this folder"}
```

⛔ **Our own crosswalk already classifies this name UNRESOLVED, with its reason recorded.** The only `_MM_` key
the crosswalk carries at all is `WALMEX*_MM_Equity`. **So the folder spelling is not evidence either — it is the
string the crosswalk copied from the same folder, already marked unresolved.**

## Why refusing is the CONTRACT's answer, not a cautious one

`FWD-4`'s own bar, as amended at v0.4 and signed by this seat, requires the induction request to **"REFUSE a name
whose identity is ambiguous."** ⭐ **A two-character transposition between two human-typed artifacts, with no
third source and an UNRESOLVED marker already on the record, is the paradigm case of that clause** — if it does
not fire here it has no content.

⛔ **And the cost of picking is asymmetric and invisible.** Inducting on a picked spelling converts an honest
`UNRESOLVED` into a possibly-wrong `RESOLVED`, in the SERVED crosswalk, under a never-widen pair whose blast
radius would name the new record as correct. **A wrong identifier does not announce itself: it produces a name
that resolves, pulls, and serves the wrong company's data.** The absence we hold today is loud; the error would
be quiet.

## What would resolve it, none of which is this act

- **Bloomberg's own resolution** for either candidate — a vendor call, which needs Andrew's per-use word and would
  settle it in one request.
- **A one-pager workbook in that folder** — the crosswalk's own evidence line says there is none.
- **Any issuer document in the corpus naming the listing line** — the corpus ingestion this project is building
  would surface it.

**Until one of those exists, the name stays UNRESOLVED and the request refuses it.** That is not a hold on the
induction machinery: ⭐ **a request that correctly refuses an ambiguous name IS the machinery working, and it
satisfies `FWD-4` exactly as a successful request would.**

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S1",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T05:05Z",
    "one_line": "RULING on the AXMB/AMXB transposition: NEITHER spelling is attested, so the induction request must REFUSE the name rather than pick between two human-typed artifacts -- the served crosswalk already carries it as bloomberg_ticker UNRESOLVED with 'no ONE PAGER workbook found in this folder' as its evidence, and FWD-4's own bar requires refusing an ambiguous identity.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "crosswalk/v1/2026-09-22.json read here: the record's folder is 'America Movil AXMB MM', security_key is null, bloomberg_ticker.status is UNRESOLVED with evidence 'no *ONE PAGER*.xlsx workbook found in this folder'.",
        "The only _MM_ security_key the crosswalk carries is WALMEX*_MM_Equity; neither AXMB nor AMXB appears as a resolved key anywhere in it.",
        "FWD-4 as amended at v0.4 and signed by this seat: the request PRINTS what the induction will add and REFUSES a name whose identity is ambiguous."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "An induction request refuses a name whose identity is ambiguous.",
    "world_is": "Two human-typed artifacts disagree by a two-character transposition, no third source attests either, and the crosswalk already records the name as unresolved.",
    "notes": "The header-over-folder tiebreak is SOUND AS A TIEBREAK and is not the issue -- a tiebreak is not a resolution. ⛔ The cost of picking is asymmetric: inducting on a picked spelling converts an honest UNRESOLVED into a possibly-wrong RESOLVED in the SERVED crosswalk, and a wrong identifier resolves, pulls and serves another company's data without announcing itself. The absence we hold is loud; the error would be quiet. RESOLVERS, none of them this act: Bloomberg's own resolution under Andrew's per-use word (one request settles it), a one-pager workbook in that folder (the crosswalk's evidence says there is none), or an issuer document surfaced by this project's own ingestion. A request that correctly refuses satisfies FWD-4 exactly as a successful one does.",
    "dismissal_reason": "A ruling record on an identifier question routed to this seat; it dispositions no filed row and asks for no act."
  }
]
```
