# AMGT_RESAPP: CVO disposition of the field-map rows (Z-S219, Z-S220, Z-S221)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T13:4xZ at HEAD after `e5e8cbeaa1`, LOCAL on SITEZ.
**Context:** `1.0.0_SA_CTO~Z` filed these three rows with the field-level channel map (msg 24242, map @`3a0b3cadaa`).
No round is open. They are dispositioned now so the channel stays at 0 open for the next L10.
**Instruments:** this seat's own, all local, with no network. Each is a different instrument from the row's evidence.

## Z-S219: the SA identity check reads the ticker. CONFIRMED on source.

`integrations/bloomberg/research/sa_forecast_fallback.py:239` reads
`sa_name = sa_attrs.get("name") or sa_attrs.get("companyName") or ""`. SA's `attributes.name` is present and is the
ticker (the row's live BABA read), so the `or` never reaches `companyName`. `entity_test(block_name, sa_name)` then
compares our company name against a ticker. The fix is to read `companyName` first. The offline tests that put a
company name in `name` must change with it. INERT, because 0 values have been filled through this path. GRADUATED.

## Z-S220: SERP freshness and the SERP writer use different partitions. CONFIRMED on source.

- Writer: `lib/research/harvest/bright_data_serp.py:6-8` documents `{request}/date=YYYY-MM-DD/{hash}`,
  partitioned by fetch date.
- Reader: `lib/research/freshness/build_view.py:177` is `latest_bright_data_serp_stamp(client, security_key)`.

A SERP key carries no security key, so this reader can never find a SERP object. INERT, because the writer has no
production caller and 0 objects. The remedy depends on the key design (the working key in the partition, or a
key-to-query index). GRADUATED to the key-design cut.

## Z-S221: Latin-alphabet languages are read as English. CONFIRMED by invocation.

`lib/research/filings/document.py` `detect_language`, called in-process:
- a German sentence (umlauts included) returns `language: en`, with an ASCII letter share of 0.97;
- a French sentence returns `en` at 0.98;
- an English control returns `en` at 1.00.

So no Latin-alphabet language would ever reach translation. The dropped `text_translated` at
`scoped_amgt.py:1660-1672` is taken from the row as filed (source-cited) and not re-read here. INERT, because every
served analysis today comes from an English EDGAR filing. **But it is live against Andrew's IEFA direction** (global,
non-US from the start): the first European annual report would be analysed as English, untranslated, with no warning.
GRADUATED to the IEFA structure design. **It must land before any non-US filing is analysed**, not merely soon after.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S388",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T13:45Z",
    "one_line": "GRADUATED: Z-S219 (SA identity check reads attributes.name, the ticker, before companyName), Z-S220 (SERP freshness reads security_key= while the writer partitions date=), Z-S221 (detect_language returns 'en' for German and French) -- each confirmed on a different instrument; all INERT today; Z-S221 must land before any non-US filing is analysed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "sa_forecast_fallback.py:239: sa_name = sa_attrs.get('name') or sa_attrs.get('companyName') or '' -- name (the ticker) wins whenever present.",
        "bright_data_serp.py:6-8 documents date=YYYY-MM-DD partitioning; build_view.py:177 latest_bright_data_serp_stamp(client, security_key).",
        "In-process detect_language: German sentence -> en (ascii share 0.973), French -> en (0.981), English control -> en (1.0)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The SA identity check confirms the same company; freshness reports the latest SERP pull per security; foreign filings are detected and translated.",
    "world_is": "Each check reads the wrong field or misclassifies; none has served a wrong value yet.",
    "notes": "Owners: Z-S219 rides 2.0.0_SA_COO~Z's first code cell after Andrew's list; Z-S220 resolves with the key design; Z-S221 with the IEFA structure design and before any non-US filing is analysed. Remediation rows owed at L10.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S219",
      "AMGT_RESAPP-Z-S220",
      "AMGT_RESAPP-Z-S221"
    ]
  }
]
```
