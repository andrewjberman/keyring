# Drive log -- 2.0.0_SA_COO~S2, IRPT_BCKEND (~PS), 2026-10-17 06Z to 12Z, dell2

Substantive ticks only. Push state: LOCAL (box-sync pushes).

## 06Z-09Z -- waiting on the switch-on chain
- `2.0.0_SA_COO~D2` issued `IRPT_DASHBD.TO-DB-b-328` (the switch-on and the first pass); IB2's watcher did not surface the 06:22Z GO, which I reported at 07:25Z (D2 nudged it). IB2 held at a STOP on the dry-run timeout (845 MB over the 819 MB line); D2 amended to 28 shards (CTO half @e73b48c481).
- Row S235 (@dispositioned S230): both function-map stamps equal the live shas; the read function moved once under TO-DB-b-323.

## 09Z-12Z -- the V leg
- 09:18Z canary id by broker from IB2. Step (1) PASS on my own reads (object exists, 52,718 bytes, one version, sha256 `2fb74e5d8087cf1e7b2891e144aaf0a3bbef97096512eb09a711776b3821d661`). Grade @85d57b9ed4.
- 11:13Z D2: full pass done, 4,012 documents. My listing of the reporting prefix: 22,269 objects = 4,012 filled + 18,257 others (unchanged count).
- CTO ruling msg 10508: no user-to-advisor edit; the V leg pair is a synthetic OPAL_GLOBAL covering viewer and a Cottonwood non-covering viewer (TO-DB-b-331, minted by IB2). Sessions arrived 11:38Z (900 s bearer tokens; no re-sign-in).
- Step (2) PASS at 11:4xZ: through `https://opalinvest.dev` with `Authorization: Bearer`, `X-Contract-Version: v1` and `selected_tenant=49financial`. COVERING 200, 52,718 bytes, sha256 equal to the object's. NON-COVERING refused `FIRM_BINDING`, no body, no leak. The first tries without the header and without the selector read `CONTRACT_VERSION` and `FIRM_BINDING` (public envelopes). Grade @44505f9642.
- Step (3) NOT RUN in the token window (the export POST needs a composed ExportBundle and `versions` / `render_options` values I could not read from a live source). Request prepared ahead, unsent: `deliverables/2.0.0_SA_COO~S2/VLEG_STEP3_EXPORT_REQUEST_PREP_20261017.md` (@commit after 44505f9642). CTO (via D2's 11:53Z tick): (2) accepted, (3) stays OWED, no re-mint.

## Open
- Step (3) OWED by ruling; a new pair and the prepared request would grade it. Not scheduled.
- `class_series` member of `reporting/entry.py` waits on `~D2`'s `class_object` v0.4.0 contract.
- Debt D2-S216 (`resolve.py` G7/G8) deferred: touching it moves two live functions' shas.
- D2's 5174 walk and the portal's reading of the route are held by the CTO; they are not mine.
