# Cloud daily sprint: why it has not published since 09-11, and the fix

**Author:** 4.0.0_SA_CRO · **UTC:** 2026-09-15 ~21:3xZ
**Asked:** Andrew-direct ~20:4xZ, relayed by 0.0.0_AB_MSTR (msg 97239), VERBATIM: *"Cro will deal with the research ,
i just need that output"*.
**Handoff:** Andrew-direct at this terminal ~21:3xZ, VERBATIM: *"Hand off to MSTR to fix and deploy"*. So the fix and
the deploy are `0.0.0_AB_MSTR`'s; this document is the research and the spec.

## Answer first

- **The job runs, but it has failed every day since 09-12**: 4 of 4 scheduled fires (09-12, 13, 14 and 15), all the
  same way. The last served page is 09-11's fire 5.
- **Cause 1, the failure itself.** The model is never asked to put every directive in `process[]`.
  - The renderer started requiring that at `2f99f0d749`, committed 2026-09-11 18:07 ET.
  - The running image was deployed at 20:47Z (16:47 ET) the same day, before that rule existed. Its prompt asks for
    every directive in `projects` only (`infra/aws/lambda/daily_sprint_generator/lambda_function.py:345-347`).
  - The renderer arrives fresh with each clone of origin/CLOUD, so it enforces the new rule; the prompt is frozen in
    the image and never asks for it.
- **Cause 2, why nothing recovers.** The work directory is fixed at `/tmp/sprint` (`:74`; Dockerfile `:33`), and
  `clone_repo` clones into it without clearing it (`:155`). Lambda's two automatic retries reuse the warm container,
  whose `/tmp` persists, so each retry dies in under 100 ms on "destination path '/tmp/sprint' already exists".
- **The structural cause.** The prompt is baked into the image, while the rules it must satisfy are cloned live. They
  update on different paths, so any future renderer rule breaks the cloud job again until someone rebuilds the image.
  Fix F3 below closes that.

## Evidence

Every read below was taken 2026-09-15 between 20:49Z and 21:3xZ.

| What | Read |
|---|---|
| Schedule | `daily-sprint-generator-schedule`: `cron(10 20 * * ? *)` (16:10 ET), ENABLED, targeting the Lambda. The Lambda's timeout is 900 s, so "still running" at 20:49Z was impossible. |
| Today's fire (CloudWatch `/aws/lambda/daily-sprint-generator`, stream `2026/09/15/...68a3c745`) | 20:10:11 START; clone at `2033ff3ea6` (CLOUD); censuses agree at 205 commits / 29 workers. 20:12:37 `render_daily_report.py` rc=1, `VALIDATION FAILED (1)`: "process[] is missing 10 of 15 register directive(s): D5 ... D14". Retries at 20:13:38 and 20:15:45 failed the clone in 89 ms and 95 ms. |
| 09-12, 09-13, 09-14 | The same shape. `process[]` is missing 13 of 14, 11 of 15 and 10 of 15. Each day shows exactly one validation error, so **`projects[]`, which the prompt does ask for, passes 4 of 4 days**. The same pair of retry clone failures follows every day. |
| The rule's landing versus the image | Last handler commit `02f51f9fb2`, 2026-09-11 16:18 ET. Deployed image `get-function` ResolvedImageUri `daily-sprint-generator@sha256:e4a23058ac30...`, LastModified 2026-09-11T20:47:37Z. The rule commit `2f99f0d749` came at 18:07 ET, after the deploy. |
| What the image carries | Dockerfile `:29` copies only `lambda_function.py`. The renderer, the schema and the register all come from the clone at run time. |
| The rule | `daily_reports/scripts/render_daily_report.py:262-329`, `check_directive_coverage`. `projects` and `process` must each hold every register directive exactly once, and a quiet process row carries `state: "idle"` with a short no-work note. |
| Process row schema | `daily_reports/schema/DAILY_REPORT.schema.json`, `process.items`: requires `n`, `name` (at most 26 characters), `timeline` (at most 20), `state` in ok/act/hold/idle, and `note` (at most 120). All 15 register titles are 23 characters or fewer. |
| Census | `daily_reports/scripts/project_census.py:190-209`. `by_directive` lists only directives with at least one attributed commit, so an absent directive had zero attributed commits. |

The claims above are source reads plus CloudWatch reads. None of the fixes below has been exercised.

## The fix: a spec for 0.0.0_AB_MSTR

**F1. The prompt asks for `process`, like `projects`.** After `lambda_function.py:347`, add:
> `process` MUST ALSO carry ALL {n_directives} directives, exactly once each, worked or not. A directive with no
> commits gets `"state": "idle"` and a short no-work note. `n` is the DIRECTIVE NUMBER and `name` its exact title.

The evidence this is enough on a normal day: the identical instruction for `projects` has held 4 of 4.

**F2. Clear the work directory before cloning.** In `clone_repo`, before the `git clone` at `:155`, add
`if os.path.exists(WORKDIR): shutil.rmtree(WORKDIR)` and `import shutil`. Do not pass `ignore_errors`: a delete that
fails should fail loudly. This is what lets the two automatic retries recover a transient failure, such as an OpenAI
error.

**F3. One repair pass on a validation failure.** This is generic, so a future renderer rule cannot silently break the
job.
- Before rendering, run the cloned renderer's own validation on the model's JSON: `validate(d)` at
  `render_daily_report.py:370`, or the render itself with its `VALIDATION FAILED` lines.
- If it reports errors, send the model ONE follow-up carrying its previous JSON and the exact error lines, asking for
  the corrected full object.
- Validate again. If it still fails, raise, and nothing is published.
- This reuses the repo's gates; it is not a second validator, so it is not a shadow implementation.
- NOT READ HERE: `validate`'s return shape. Confirm it returns the error list before wiring it.

**F4. Optional backstop: fill quiet rows mechanically, and only when the census proves quiet.**
- For a register directive missing from `process[]` or `projects[]` whose number is ABSENT from
  `pc["by_directive"]` (zero attributed commits), append the quiet row:
  - `process`: `{n, name: title, timeline: "no work today", state: "idle", note: "No work on this today."}`
  - `projects`: `{n, name: title, text: "No movement today.", quiet: true}`
- **Never fill a directive the census shows worked.** An idle row would print "no work" over real work, which is the
  exact misreading the rule exists to prevent. That case goes to F3.
- Not measured here: which of today's omitted directives had commits in the cloud population. The cloud census logs
  totals only. So F4 alone may not have saved 09-15, and F1 plus F3 is the fix.

## Deploy and verify notes (0.0.0_AB_MSTR's call; carried from the 09-11 record)

Source: `org/critical_paths/change_management/20260911T2002Z_daily-sprint-generator-first-apply_deploy_completion.md`.

- **This is an image act (NEVER-2).** The `:latest` tag has exactly one consumer, this function, as measured on 09-11
  (0 of 3 image Lambdas and 0 of 9 ECS families). Open a deploy-ledger entry.
- **Build flags.** Build with `--provenance=false --sbom=false --platform linux/amd64`. The 09-11 L3 trap: buildx's
  default manifest list is refused by Lambda, with an error that reads as a broken image.
- **A pushed `:latest` does not move the function by itself.** `main.tf` ignores `image_uri` changes, and Lambda runs
  a resolved digest. Today's digest `e4a23058...` differs from the first-apply digest `f0f2d435...`, so it was already
  moved once on 09-11. Use the sanctioned route that moved it then, and prove that ResolvedImageUri equals the pushed
  digest.
- **The fix lives only in the image.** The scripts it runs come from origin/CLOUD, so the fix does not need the CLOUD
  push hold lifted. Unpushed laptop work still stays outside the cloud report; the page discloses that, and it is
  Andrew's hold.
- **QA.**
  - Offline: put a report missing `process` rows through the cloned renderer. It should read VALIDATION FAILED before
    the fix and clean after it. Add a positive control that a worked directive is not idle-filled.
  - Warm retry: two invocations in one container, where the second clone must succeed.
  - A live invoke publishes a served day:
    - today's date would overwrite 0.0.0_AB_MSTR's local edition;
    - a missing past day (09-12, 09-13 or 09-15) is a backfill, which `main.tf`'s event-target comment calls "a
      deliberate act with the never-widen sign-off";
    - otherwise the 09-16 20:10Z fire is the acceptance.

## Not done by this seat

- No code change, build, deploy or invoke.
- `validate()`'s signature was not read.
- The cloud population's per-directive counts for the failed days were not measured.
- The route that moved the image on 09-11 was not traced.
