# ANDREW VOICE MEMO (2026-08-03 23:51 ET / 2026-08-04 03:51Z) -- THE CANONICAL Model Portfolios component->artifact map
**Source:** C:\Users\AndrewBerman\Downloads\New Recording 21_9678.m4a (411,885B, mtime 2026-08-03 23:51 ET)
**Transcription:** openai-whisper (model small, local), run 2026-08-04 ~03:52Z at the COO terminal on Andrew's direct instruction ("I have recorded a voice memo so there is no confusion on this subject henceforth").
**Supersedes-in-place:** the ~0447Z-quote application (already ruled a misreading @fa4bbc03b); CTO's 042528Z keep-legacy-quarterlies interim choice; any read of MP components from non-canonical locations.

## VERBATIM TRANSCRIPT (whisper output, unedited)

> "Okay. I want to make this very clear so there's no confusion. We need to be canonical here.
> AUMmetrics.json. That should cover the radial and the metrics under the container. Under the
> radial, those little metrics in that container, those need to be all covered. The whole section,
> that group, needs to be covered by AUM-metrics.json. To the right of that, in the portfolio
> analytics panel, the bell curve and the similar juxtaposed container that sits beneath the bell
> curve, those need to be covered by account-distribution.json. These two are symmetrical. The
> radial and underlying container, AUM-metrics.json, the bell curve and underlying container, that
> is account-distribution.json, that must be consistent, that is canonical for every single scope,
> global 49 financial inflection wealth management, and Coddenwood Capital Advisory. Following from
> that, in the AUM tab underneath the first tab of model portfolios, all of that data, monthly
> quarterly breakdown and daily area charts, all of that should be aggregate-AUA-TIME-SERIES.json
> for the respective scope. All of these assets need to be produced in the same ingestion fashion.
> Bronze coming in to Opal Data Assets, proceeding through silver, proceeding through gold,
> published through the Lambda to Opal-Portal Data-B2-Platinum-MDPF. That is the canonical
> location. All of those assets must only be read from that location. Confirm that you understand
> and realize it through DE now."

*(Phonetic normalizations, meaning unchanged: "Coddenwood Capital Advisory" = Cottonwood Capital
Advisors; "Opal-Portal Data-B2-Platinum-MDPF" = s3://opal-data-portal-v2/platinum/mdpf/;
"AUMmetrics" = aum-metrics.json.)*

## THE CANONICAL MAP (operative form, per scope in {global, 49financial, inflection, cottonwood})

| Component group | ONE canonical artifact |
|---|---|
| Radial (donut) + the metrics container beneath it (the whole group) | `platinum/mdpf/{scope}/aum-metrics.json` |
| Bell curve + the juxtaposed container beneath it (symmetrical to the above) | `platinum/mdpf/{scope}/account-distribution.json` |
| AUA tab: monthly/quarterly breakdown + daily area charts | `platinum/mdpf/{scope}/aggregate-aua-timeseries.json` |

**Production law:** every one of these assets is produced in the SAME ingestion fashion -- bronze
into `opal-data-assets` -> silver -> gold -> published through the Lambda (opal-assets-mdpf-portal-
publisher) to `s3://opal-data-portal-v2/platinum/mdpf/` -- THE canonical location.
**Read law:** these assets are read ONLY from that location. (Kills the frozen
`json/portfolios/aum-metrics.json` read; no legacy fallbacks.)

## Realization state at record time
- account-distribution + aggregate-aua-timeseries: ALREADY canonical-conformant (produced +
  published + read per the map) -- Andrew's bell/trend understanding confirmed correct.
- aum-metrics: producer exists for cottonwood only; global/49f/inflection artifacts DO NOT EXIST
  yet -> the elevated emitter (producer leg, DS/AE via CTO spec) + the DE read-repoint (honest-
  absent until the artifacts land, per the page's no-fallback law) realize the map.
