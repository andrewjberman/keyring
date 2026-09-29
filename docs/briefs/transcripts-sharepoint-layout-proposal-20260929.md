# Proposal: the SharePoint "Transcripts" folder, organized by the LGIC naming grammar

- Author: `4.0.0_SA_CRO~T`, 2026-09-29. Status: PROPOSED, shown to Andrew. Nothing is created in SharePoint.
- Order: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260929_18xxZ_TRANSCRIPTS_SCOPE_FOUR_ARCHETYPES_SHAREPOINT_HOME.md`
- Canon read: `infra/logic/02_DOCTRINE.md` R1, R2, R9, R17, R20; generated naming section N1;
  `lib/opal_naming.py` `key()` and `address()`.

## 1. What the canon gives and where SharePoint departs

The key grammar is `{source}/{scope}/{tier}/{table}/{partition}` with the object as the leaf. It is ruled for S3
keys. SharePoint is not a plane the canon rules, so this proposal BORROWS the grammar's vocabulary and states its
one departure.

| Grammar slot | Value here | Basis |
|---|---|---|
| container | the `Transcripts` folder | Andrew's word |
| source | `teams` | the system that produced the transcript |
| scope | `global` | Opal-internal, not one client firm's data |
| table | the archetype, snake_case | Andrew's four archetypes |
| tier | `bronze`, `silver` | closed list N1 |
| partition | `date=YYYY-MM-DD` | N1, the meeting's Eastern date |
| object | `{PREFIX}-{YYYYMMDD}-{HHMM}.{ext}` | the transcript store's existing id |

DEPARTURE (declared, R20 shape): Andrew asked for the four archetype folders directly inside `Transcripts`. The
grammar puts source, scope and tier ABOVE the table. Here source and scope are constant, so they are carried in a
manifest at the root instead of as two folder levels, and the archetype sits above the tier.

## 2. The layout

```
Transcripts/
  README.md                         what this folder is, the grammar, the owner
  MANIFEST.tsv                      one row per transcript: archetype, date, id, sha256, Graph ids, organizer
  series.json                       archetype registry: every Teams subject and chat that maps to each archetype
  monday_meeting/
    bronze/
      date=2026-09-28/
        MM-20260928-0857.vtt        raw WebVTT, byte-exact as Microsoft served it
        MM-20260928-0857.graph.json Graph ids, sha256, organizer, claim classes
    silver/
      date=2026-09-28/
        MM-20260928-0857.json       parsed utterances, speakers, coverage
        MM-20260928-0857.md         the same transcript, readable by a person
  ocio_ic/
    bronze/date=YYYY-MM-DD/ICO-...
    silver/date=YYYY-MM-DD/ICO-...
  asset_management_ic/
    bronze/date=YYYY-MM-DD/ICA-...
    silver/date=YYYY-MM-DD/ICA-...
  research_meeting/
    bronze/date=YYYY-MM-DD/RT-...
    silver/date=YYYY-MM-DD/RT-...
  other_meeting/
    bronze/date=YYYY-MM-DD/OM-..._{subject_snake_case}
    silver/date=YYYY-MM-DD/OM-...
```

## 3. Rules

1. BRONZE IS RAW (R9). The `.vtt` is never edited, renamed or re-saved. Everything in `silver/` is re-derivable
   from `bronze/` alone.
2. NOTHING BUT TIER DATA INSIDE A TIER (R17). The manifest, registry and README sit at the root.
3. NO ENTITY ID AS A FOLDER (R2). A Graph meeting id or chat id is never a folder name. It lives in the sidecar
   and the manifest.
4. AN ARCHETYPE IS A REGISTRY ROW, NOT A NAME MATCH. Meetings "may be called various different things", so
   `series.json` maps each Teams chat to an archetype. A new name for an old meeting is one registry row.
5. ONE DATE BASIS. The partition is the meeting's Eastern calendar date. The id clock is Eastern start.
6. NEVER OVERWRITE. A second, different body for the same transcript id is refused and flagged.
7. ASCII, snake_case folders, no spaces.

## 4. What the builder says

`lib/opal_naming.py` refuses `teams` as a source: it is not a row in `infra/logic/registry/systems.json`.

```
key('teams','global','bronze','monday_meeting','date=2026-09-28')
  REFUSED: source 'teams' is not a systems.json key
key('gateway','global','bronze','monday_meeting','date=2026-09-28')
  gateway/global/bronze/monday_meeting/date=2026-09-28
```

Per rule 30 a refusal is a missing registry row to add, not a name to hand-type. Two choices:

| Choice | Effect |
|---|---|
| Add a `teams` row to `systems.json` (recommended) | the source names where the data comes from |
| Use the existing `gateway` row | no registry change; the source names the carrier, not the origin |

If the transcripts are ever mirrored to S3, the builder's address for the same content is
`s3://opal-data-assets/{source}/global/bronze/monday_meeting/date=2026-09-28/`, so the SharePoint tree and the
S3 key read the same from the archetype down.

## 5. Open for Andrew

1. Archetype folder names as shown, or different words.
2. `teams` as a new registry row, or `gateway`.
3. Which SharePoint site holds `Transcripts`, and who may read it. Committee transcripts are sensitive.
4. Which archetype "Opal Investment Committee" belongs to. It is a separate Teams chat from both committees.
5. Whether `other_meeting` is wanted now, or only the four.
6. Whether the 29 Research Meeting transcripts already in the repository store are copied into
   `research_meeting/`.

## 6. Effect on work already done

`research_transcripts/schema/series.json` uses `equity_research_call`, `ic_ocio`, `ic_asset_management`. On
approval those keys are renamed to the archetype names above. The lander writes to the repository store today; its
target becomes this folder through the gateway's existing `upload_text_to_site` tool.
