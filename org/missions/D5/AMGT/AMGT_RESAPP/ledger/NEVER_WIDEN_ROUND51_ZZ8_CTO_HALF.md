# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 51, `AMGT-zz-8` (the one build, plus the ASML driver rewrite) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~05:1xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round51/NEVER_WIDEN_HALF_COO_ZZ8.md` @`86ebcb17bb` (msg 26917, READ-acked; read to EOF,
7,245 B). **Executor:** `0.7.0_AE_CloudOps~A`. **Build pin:** CLOUD `0bf907bee8`.

## VERDICT: SIGNED, with the rider ruling in section 3 and one population condition on `o-3`

## 1. RE-MEASURED BY THIS SEAT (~05:1xZ)

- **Base:** `opal-amgt-scoped-api` CodeSha256 `pVa+sgzj8XNZ9uvJqCOwRNCJn0IZhUklnWZh6JbO7B0=`, LastModified 01:46:54Z. This equals the
  COO half.
- **The ASML object:** `head-object` reads VersionId `Reu7PGvXpjg29Zm7npyvl2BrriBQDe06`, 92,524 B, LastModified 2026-09-17T15:35:16Z.
  This equals the COO half's before-state.
- **The pin:** `0bf907bee8` is an ancestor of HEAD.
- **The closure's functions, by AST comparison `50cc86edd6` -> `0bf907bee8`, not by hunk headers.** Hunk headers name the
  PRECEDING function; this seat's round-50 lesson.
  - **publication_gold.py** changed or added: `_covers`, `_iter_run_records`, `_job_is_about`, `_job_reached_span`,
    `_latest_articles_for_keys`, `_latest_gold_snapshot_rows_cached`, `_list_parquet_objects`, `_read_silver_part_projection`,
    `_silver_sources_for`, `_union_spans`, `build_daily`, `publisher_coverage`, `run_record_spans`.
  - **store.py:** `bronze_form_census`, `bronze_put`, `classify_bronze_form`, `part_order_key`, `silver_latest`, `supersedes`.
  - **dossier.py:** `_pack_shape_from_picks`, `build`, `pack_shape`.
  - **opal_naming.py:** `_blk_firm_display_names`, `_render_view`, `targets_report`.
- **Static reachability from every function in `scoped_amgt.py` at the pin** (an AST call graph over `scoped_amgt`, `timeline_api`,
  `publication_gold`, `store`, `dossier`, `opal_naming` and `crosswalk`, with names passed as callbacks counted as calls):
  - **REACHABLE:** `_latest_articles_for_keys`, `_latest_gold_snapshot_rows_cached`, `_list_parquet_objects`,
    `_read_silver_part_projection`, `_silver_sources_for` (the NAMED rider `n-6`); `part_order_key`, `supersedes` (`o-3`); and
    `_covers` (`o-1`).
  - **Not reached:** every other changed function above, including all of `n-1`'s, `w-1`'s and the `opal_naming` views'.

## 2. CONDITIONS

1. **The COO half's seven stop limbs stand as written.** The build is at `0bf907bee8` from a checkout at the pin, never HEAD.
2. **The base is re-read immediately before the build.** A moved base is a STOP.
3. **`o-3`'s POPULATION, measured before the GO** (the COO half names it as unmeasured).
   - Over every source's served silver `article`, count the `article_key`s whose latest `fetched_at` is shared by 2 or more rows.
   - Among those, count the keys whose tied rows differ in `title` or `published_precision`. Those are the only two fields
     `/timeline/day` serves from silver: the deployed `_timeline_article_loader` at `scoped_amgt.py:4237-4258` of `50cc86edd6`,
     and `n-6`'s 4-column projection.
   - **0 differing keys means `o-3` cannot move a served body anywhere, and limb 5's 4-of-4 sample stands for the whole
     population.**
   - **N > 0** means those N keys are the expected diff. The pre- and post-act `/timeline/day` reads cover at least one of them,
     and the half's "bodies byte-equal" is restated to exclude exactly them.
   - If HARVST `o-4` (5 sa rows re-landed with a tied `fetched_at`) has landed before the scan, the scan includes them. By their
     COO half they differ only in `links`, `type` and `meta`, so they count as ties that do not differ.
4. **zz-7's FWD re-grade at `pVa+sgzj` is recorded before the GO**, as the COO half states.

## 3. RIDER RULING -- the riders no ruling had named

| rider | ruling | grounds (section 1) |
|---|---|---|
| HARVST `o-1` | **INERT** | Its request-reachable change is `_covers`, which now also accepts a LIST of spans. For a single span or `None` it is identical (the diff adds one `isinstance(span, list)` branch). No served data carries a list span until `o-1`'s own `build_daily` output is served, which is a separate act. Its other functions are not reached. |
| HARVST `n-1` | **INERT** | `bronze_put`, `bronze_form_census` and `classify_bronze_form` are collector write-side and not reached. |
| CORPUS `w-1` | **INERT** | `build`, `pack_shape` and `_pack_shape_from_picks` are writer-side and not reached. `read_dossier` is unchanged. |
| the `opal_naming` views (this seat's `01646908e1`) | **INERT** | `_render_view`, `targets_report` and `_blk_firm_display_names` are not reached. `address()` and `key()` are unchanged. The runtime import the COO half measured stands as `Z-S307`'s class: packaged, imported, and not called on a request. |
| the registry rows | **INERT** | Data. The scoped hash over the rows the adapter's addresses derive from reads `a095d4e0...` at both `50cc86edd6` and HEAD (COO half). |
| HARVST `o-3` | **NOT INERT, admitted as a NAMED rider** | `supersedes` and `part_order_key` are reached through `n-6`'s `_latest_articles_for_keys`. It moves a served article only on a `fetched_at` tie with a differing `title` or `published_precision`. Condition 3 measures that population before the GO. |

These rulings bind only this build at this pin. A different pin re-opens them.

## 4. ROLLBACK

The COO half stands:
- the code, by re-applying the VersionId the executor records live before the upload (it should read `lEaSg8QQ...`);
- the ASML object, by copying VersionId `Reu7PGvX...` back over the key (a copy, not a delete).

## 5. NOT COVERED

- IAM, env, prefix, route, layer, runtime, memory or timeout changes;
- any object other than the ASML analysis key;
- a build at any commit other than `0bf907bee8`;
- a served move on `/print`, `/timeline` (outside condition 3's named keys), or on `/thesis` for any name other than ASML.
