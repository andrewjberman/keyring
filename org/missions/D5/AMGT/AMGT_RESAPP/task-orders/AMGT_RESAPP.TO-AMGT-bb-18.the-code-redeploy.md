# AMGT_RESAPP task order -- `AMGT-bb-18` -- THE ROUND-78 CODE REDEPLOY CARRYING THE ADAPTER'S SIX HOOKUPS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-18,AMGT-bb-23</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm, monitor or cadence; one redeploy by hand. The daily snapshot schedule is unchanged.
comp-iam: RUN by the issuer at the cut -- denominator: 14 build cells whose modules the artifact may carry (bb-1..bb-4, bb-7..bb-11, bb-13, bb-16, bb-17, bb-21, bb-22); they add no read path the function role lacks at the cut; a cell that needs a grant names it in the pair, and the plan STOPs on any IAM resource the pair does not list.
comp-iam coverage: BLIND to an IAM change outside the plan.
comp-adversary: RUN by the issuer at the cut -- deployed MkM9Kf37 (LastModified 2026-10-07T04:40:17Z) reads the round-77 served shape YES; `r78_bb17.py --crit AC1 --where local` at the base reads NO (H1 to H5 fail, H6 reads 2 wrong rows of 60), so the deployed line FAILS until this act.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-bb-18` (round 78, decomposition s.86)

Under ONE NEVER-2 entry and ONE never-widen pair:
1. **Code leg.** Build from a DETACHED worktree at EXACTLY the commit the GO names, never "at or after" it. `memory_size` stays 1769.
   - The CONTENT-DIFF the pair lists is measured at that commit against deployed `MkM9Kf37`. A file not on the list is a STOP.
   - ONE `safe-apply` on `infra/aws/terraform/harvest/`, the plan graded UNTARGETED: only the function's code (its
     artifact object and hash) may move. No route changes this round. Any other resource is a STOP, unless the pair names it.
   - The new CodeSha256 differs from `MkM9Kf37` AND equals the built artifact's. An unchanged hash is a 0-diff deploy: STOP.
   - Then run `round71/checks/leadpanel_cold_warm.py --label after` and read the cold invokes' `AMGT_PHASE` lines. Reported, not graded.
2. **After the code leg,** invoke the snapshot's scheduled event once (`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`), so
   the /freshness snapshot is written by the new code. Read the stamp.

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/`
(`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), and measure the
artifact before acting on any entry you find. `r78_deployed_cells.txt` (beside the round-78 checks) lists the round's deployed
checks; the GO states how many lines it holds.

A failing criterion is the ROLLBACK trigger: the prior artifact through the module, one code-only `safe-apply`. **Pins:** r76 c62
and c63, and r75 c59 with its 40-wide burst. A c59 that reads UNMEASURED (exit 2) is NOT a rollback trigger: report it and stop.

**Not served by this act, by ruling:** the segment table and its period labels, and the Seeking Alpha record reader. Their
modules may be in the artifact; no route reads them. If the CONTENT-DIFF shows a route reading one, STOP.

## 1a. AMENDMENT 1 (issuer, 2026-10-07 ~17:5xZ) -- LEG 0, cell `AMGT-bb-23`: THE BUILD TAKES PYARROW AND LINUX RPDS-PY FROM THE DEPLOYED ZIP

**Why:** no package may be fetched from the internet on this box (Andrew's word, 2026-10-07). The CTO ruled (msg 31206) that the
build takes these two packages from Opal's own deployed zip, under two terms: the zip's sha256 must equal the live function's
CodeSha256 read at build time or the build stops, with no download fallback; and the two packages in the new zip must equal the
deployed zip's byte for byte. **LEG 0 runs FIRST and may begin at once: it needs no pair, because it runs no build, applies
nothing and writes no store.** It is two files in `infra/aws/terraform/harvest/`. Commit it on its own, before legs 1 and 2.
Legs 1 and 2 (section 1) still wait for the GO.

**In this folder nothing else is fetched by you either:** before you run ANY build or deploy script on this box, find it in
`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/SITEZ_INSTALL_DOWNLOAD_LINE_CENSUS_20261007.md`; if a listed line can fetch, the
script does not run as it is, and you report the missing files (CTO msg 31234).

The build of the `opal-amgt-scoped-api` package downloads seven Python packages from the internet. That is no longer
allowed on this machine. Five of them will arrive as files and are not your concern. The other two, pyarrow 16.1.0 and
rpds-py 2026.6.3, must be taken from the package that is running now: the build copies their files out of a local copy
of that package, and only after proving the local copy IS the running package. You write a small helper that does the
proof and the copy, and you edit the build script to use it.

Words used below.
- "The build script" is `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`. Line numbers are the file's
  lines before your edit.
- "The helper" is a new file, `infra/aws/terraform/harvest/vendor_from_deployed.py`.
- "The deployed zip" is a local file holding the package the function runs now. On this machine it is
  `C:/tmp/ba20-r77-14a36147bd.zip`. You never type that path into the build script or the helper.
- "The four folders" are the zip entries whose names begin with `pyarrow/`, `pyarrow-16.1.0.dist-info/`, `rpds/` or
  `rpds_py-2026.6.3.dist-info/`. In the deployed zip they hold 132, 6, 4 and 5 files: 147 in all.
- "The live hash" is the text AWS returns as `CodeSha256` for the function `opal-amgt-scoped-api`: the sha256 of the
  running package, written in base64 (44 characters).

**File 1: the helper, `infra/aws/terraform/harvest/vendor_from_deployed.py` (new).** Standard library only. ASCII only.
Python 3.9 syntax. It imports none of: urllib, http, socket, ssl, ftplib, subprocess, boto3, botocore, requests, pip.

1. Command line: `--zip <path>`, `--expect-sha256 <base64 text>`, `--dest <folder>`, all three required. Use argparse,
   so `--expect-sha256=<text>` is accepted too.
2. Read the zip file in pieces and compute its sha256; write it in standard base64. If it is not exactly equal to the
   `--expect-sha256` text: print one line that begins `ERROR: sha256 mismatch` and states both values, write nothing,
   do not create the dest folder, and exit with a non-zero code. There is no other way past this step: no option skips
   it and nothing is fetched.
3. If the dest folder exists and holds anything, print a line beginning `ERROR:` and exit non-zero, writing nothing.
4. List the zip's file entries under the four folders. The four folder names are typed in the helper exactly as above,
   versions included. If any of the four has no entry, print a line beginning `ERROR:` that names the missing folder,
   write nothing and exit non-zero. (A zip holding `pyarrow-17.0.0.dist-info/` and no `pyarrow-16.1.0.dist-info/` is
   refused here. That is intended: this helper serves these two versions only.)
5. Refuse (a line beginning `ERROR:`, nothing written, non-zero exit) if any of those entry names begins with a slash,
   holds a backslash or a colon, or has `..` as a path part.
6. Only then write each entry under the dest folder at its own relative path, in binary mode, the bytes exactly as the
   zip gives them. Write nothing else there. Entries outside the four folders are never written.
7. Print one line per folder with its file count, then one last line beginning `OK:` with the total. Exit 0.

**File 2: the build script.** Eight edits. Do not change any line not named here.

- S1. After line 123 (`python "$SCRIPT_DIR/gen_harvest_prefixes.py" --check`) and before the comment line that begins
  `# ---- VENDOR:`, insert these lines, with a comment line above them naming AMGT-bb-23:

      FUNCTION_NAME="opal-amgt-scoped-api"
      DEPLOYED_ZIP="${AMGT_DEPLOYED_ZIP:?AMGT_DEPLOYED_ZIP must name the deployed package zip on this box}"
      FROM_DEPLOYED="$TMP/from-deployed"
      LIVE_SHA="$("$AWS" lambda get-function-configuration --function-name "$FUNCTION_NAME" --query CodeSha256 --output text | tr -d '\r\n')"
      if [ -z "$LIVE_SHA" ] || [ "$LIVE_SHA" = "None" ]; then echo "ERROR: no live CodeSha256 was read for $FUNCTION_NAME"; exit 1; fi
      echo "DEPLOYED: live CodeSha256 $LIVE_SHA; local zip $DEPLOYED_ZIP"
      MSYS2_ARG_CONV_EXCL='--expect-sha256=' python "$SCRIPT_DIR/vendor_from_deployed.py" \
        --zip "$DEPLOYED_ZIP" "--expect-sha256=$LIVE_SHA" --dest "$FROM_DEPLOYED"

  What they do: the build stops at once when the environment variable `AMGT_DEPLOYED_ZIP` is not set; it reads the live
  hash itself, every run; it calls the helper, and because the script runs under `set -e` a non-zero exit from the
  helper stops the build before any pip command. `MSYS2_ARG_CONV_EXCL` keeps Git Bash from rewriting a hash that begins
  with a slash into a Windows path; keep it and keep the `--expect-sha256=` form with the equals sign.
- S2. Line 126 (`RPDS_PIN="rpds-py==2026.6.3"`) stays. Add a comment line above it saying it is now used only by the
  local-interpreter download near line 560.
- S3. Delete line 132 (`PYARROW_PIN="pyarrow==16.1.0"`). Replace the comment at lines 127-131 with a comment saying
  pyarrow 16.1.0 and rpds-py 2026.6.3 are copied from the deployed package by `vendor_from_deployed.py` and are never
  downloaded. Change line 133 to exactly:

      VENDOR_PINS="jsonschema==4.26.0 attrs==26.1.0 jsonschema-specifications==2025.9.1 referencing==0.37.0 typing_extensions==4.16.0"

  Lines 134-147 (the pip download of `$VENDOR_PINS` and the wheel hash print) stay as they are.
- S4. Line 149: add a fourth argument, so it reads `python - "$ROOT" "$ZIP" "$WHEELS" "$FROM_DEPLOYED" <<'PYEOF'`.
  Line 155: read it, `root, out, wheels, from_deployed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]`.
- S5. Lines 240-244: replace the two constants `NATIVE_WHEEL_PREFIXES` and `NATIVE_WHEEL_TAGS` and their comment with
  one constant, `DEPLOYED_FOLDERS = ("pyarrow/", "pyarrow-16.1.0.dist-info/", "rpds/", "rpds_py-2026.6.3.dist-info/")`,
  and a comment saying these come from the deployed package. Leave lines 245-247 (`VENDOR_PRUNE`) exactly as they are.
- S6. Lines 430-437, inside the wheel loop: every wheel pip downloads must now be a pure one. Remove the `native` list
  and the admitted-native branch; a wheel whose name does not end `-none-any.whl` stops the build with a `FATAL:` line
  naming it. The rest of the loop (lines 438-448, the prune of each PURE wheel's members) stays.
- S7. Lines 449-455 (the block that demands exactly two native wheels and prints `VENDORED-NATIVE`): delete it. In its
  place, walk the folder `from_deployed`. For every file there: its zip name is its path relative to `from_deployed`
  with forward slashes; if that name does not begin with one of `DEPLOYED_FOLDERS`, or is already in `members`, `data`
  or `vendored`, stop with a `FATAL:` line; otherwise read the file in binary mode and store it, `vendored[name] =
  <its bytes>`. DO NOT pass these names through `VENDOR_PRUNE` or any other filter: every file the helper wrote goes
  into the zip unchanged. If the walk finds no file, stop with a `FATAL:` line. Then print one line beginning
  `VENDORED-FROM-DEPLOYED:` with the file count per folder. The text `expected exactly 2 admitted native wheels` must
  no longer appear anywhere in the script.
- S8. In the header comment, after the paragraph that ends "Any other non-pure wheel is refused." (line 71), add a
  short paragraph: since AMGT-bb-23 pyarrow and rpds-py are copied from the deployed package named by
  `AMGT_DEPLOYED_ZIP`, only when its sha256 equals the live CodeSha256 read at build time; there is no download for
  them; a version change of either goes back through intake.

**Rules.**
1. You do NOT run the build script, with or without `--build-only`. It cannot finish on this machine yet (the five
   other packages are not here) and it must not be tried.
2. You run no `pip download`, no `pip install`, and no command that fetches anything from the internet. You make no
   AWS write. The three check commands make one AWS read each at most; you make no other AWS call.
3. Neither file gains any way to obtain pyarrow or rpds-py other than the copy from the deployed zip: no fallback
   download, no second source, no option that skips the hash comparison.
4. You do not edit lines 544-741 of the build script (the isolated runtime check, the content diff, the upload). The
   pip download near line 560 stays: it is for the build machine's own interpreter and never reaches the zip.
5. You do not edit `content_diff.py`, `upload_verified.sh`, `gen_harvest_prefixes.py`, any `.tf` file, or anything
   under `lib/`.
6. No machine-specific path in either file: the zip's location reaches the script only through `AMGT_DEPLOYED_ZIP`.
7. ASCII only, LF line endings. The helper must pass `bash .tools/commit-gate.sh infra/aws/terraform/harvest/vendor_from_deployed.py`.

Report: the three verdict lines, the file counts the helper printed for the four folders, and the line numbers of the
script at which the zip is required, the live hash is read, the helper is called and the first pip download sits (the
AC3 output prints them).

For LEG 0 you do NOT run the build script, `pip`, `terraform` or any AWS write. `upload_verified.sh`, `content_diff.py` and every
`.tf` file are read, never edited. Prove LEG 0 with AC4, AC5 and AC6 below.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change the pair does not list, no S3 delete, no vendor or SEC call, no push
   of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-78 deployed check passes; R78 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c62 c63; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c59 --where deployed; echo "exit=$?"</invocation><expect>R76 C62 and C63 SERVED: YES (unless the pair states a round-78 cell changes what they read, and then as the pair says) and R75 C59 SERVED: YES with one or more cold invokes inside the bar, on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_served_shape.py" --where deployed; echo "exit=$?"</invocation><expect>R77 SERVED SHAPE: YES on the deployed function (no regression, unless the pair names one a round-78 ruling intends); and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bb-23"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb23.py" --crit AC1; echo "exit=$?"</invocation><expect>the helper, handed the deployed zip and the live CodeSha256, exits 0 and fills an empty folder with 147 of 147 files equal to the zip's entries byte for byte (132, 6, 4, 5; pyarrow 138 of 138, rpds 9 of 9) and nothing else; C1-C4 PASS; R78 BB23 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-bb-23"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb23.py" --crit AC2; echo "exit=$?"</invocation><expect>the helper stops with nothing copied on a wrong expected hash, on a copy of the zip with one byte changed inside a pyarrow member, and on a zip whose pyarrow dist-info is another version, while it exits 0 on the right hash, and the comparer reports the one flipped byte; P0 and N1-N4 PASS; R78 BB23 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-bb-23"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb23.py" --crit AC3; echo "exit=$?"</invocation><expect>read from the script text, the pip pin list is the five pure pins, no pip download for the Lambda platform names pyarrow or rpds, the script requires the zip, reads the live CodeSha256 and calls the helper before any pip download, there is no other fetch route, the prune list removes 0 of the 147 deployed files, the packaging step is handed the filled folder, and bash -n passes; C1-C7 PASS; R78 BB23 AC3 SERVED: YES; and exit=0 Which clauses are build and which are bound. AC1: C1 is bound (the zip on disk is the running package; PASS at the base), C2-C4 are build. AC2: N3 is bound (it tests the check's own comparer; PASS at the base), P0, N1, N2, N4 are build. AC3: C5 and C6 are bound (PASS at the base), C1-C4 and C7 are build. Every criterion as a whole is build: all three read NO at the base. **What this cell does NOT prove.** The full build with no network is not this cell's proof: the five pure wheels are not on this machine, so the script cannot run to a zip. Term 2 in the ruling's own words ("the two folders in the NEW ZIP equal the deployed zip's") is read at bb-18, on the zip that build makes, by python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb23.py" --compare-zip &lt;the built zip&gt; (expect R78 BB23 COMPARE-ZIP EQUAL: YES, 147 of 147). AC1 proves the same equality one step earlier, on the folder the packaging step reads; AC3 C7 reads from the text that the packaging step takes that folder</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256;
- the CONTENT-DIFF and size;
- every criterion's output lines;
- the leadpanel AFTER output and the cold `AMGT_PHASE` table;
- the snapshot stamp after the event.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.86; staged until the adapter cell (bb-17) drains and the pair is signed. At the GO the issuer fills
`round78/checks/r78_deployed_cells.txt` and states the line count. Checks dry-run at the base: bb-18 AC1 base NO CELLS LISTED exit 2
(FAIL as expected); AC2 pins as round 77's ba-20 proof read them on MkM9Kf37; AC3 base: `r77_served_shape.py --where local` reads YES
at the cut (the deployed read is the round-77 one real run, `round77/ONE_REAL_RUN_20261007.txt`). Peers V below three (bb-13) and
round 77's ba-13 ride this artifact.

<status>staged</status>
<round>78</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

**ISSUER GO FOR LEG 0 ONLY (2.0.0_SA_COO~Z, 2026-10-07 ~17:5xZ):** AMENDMENT 1 adds cell AMGT-bb-23 as LEG 0 and criteria AC4-AC6; it was drafted as its own order and `.tools/to-pipeline-gate.py` GATE (x) refused a second order file in round 78 ("a re-cut into the first issuance MODIFIES its orders and adds no file"), so it rides here. Draft and base dry-runs: `round78/GROUP_F_NOTES.md` @0ce9cfcfd1 (AC4, AC5, AC6 each read NO at the base). Legs 1 and 2 stay STAGED: they wait on the six files by Taildrop and on the pair, which also states `AMGT_DEPLOYED_ZIP`, `PIP_NO_INDEX=1`, `PIP_FIND_LINKS`, the `--compare-zip` read of the built zip, the dossier.py change (51 values in 35 names, CTO msg 31204) and that the then-deployed zip is KEPT on disk after the apply. Gate limb: GATE (viii) on a modify (`<placeholders>` NONE).

<status>pending</status>
