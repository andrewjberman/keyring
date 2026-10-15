# AMGT_HARVST task order -- `HVST-cb-5` -- ROUND 87: A TAB SESSION MINIMISES ITS OWN BROWSER WINDOW SO A CONTINUOUS RUNNER DOES NOT SIT ON THE OPERATOR'S DESKTOP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-5.the-runner-window-is-minimised-by-the-browser</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~144</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL code and one test only. NO publisher host, NO Secrets Manager call, NO sign-in, NO real browser launch (the test fakes Playwright), NO S3 call, NO collector or runner run, NO scheduled task.
comp-adversary: RUN at L5 -- the adversary is a window call that raises and so breaks every job, a fake that cannot fail (a test that passes whatever the code does), and an edit that changes the browser's launch arguments or its profile.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/tab_transport.py` `TabSession.__init__` launches Chrome headful (`launch_persistent_context(..., channel="chrome", headless=headless, args=list(LAUNCH_ARGS))`) and keeps that window in view. The harvest runner will run continuously on a desktop where people and agents work, so each tab session must minimise its own window. MEASURED on this box (2026-10-15, scratch profile, neutral page): the launch flag `--start-minimized` does NOT minimise the window (Win32 `IsIconic` read False after 4 s). Minimising through the browser's debug protocol DOES: after
`cdp = ctx.new_cdp_session(page)`, `w = cdp.send("Browser.getWindowForTarget")`, `cdp.send("Browser.setWindowBounds", {"windowId": w["windowId"], "bounds": {"windowState": "minimized"}})` the window read minimised (`IsIconic` True), stayed minimised after a navigation, `document.visibilityState` still read `visible`, and `page.screenshot` still worked. This cell makes that call part of the session start.

## 1. THE BUILD (LOCAL, about 20 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/opal_data_harvest/tab_transport.py`: add a keyword `minimize=True` to `TabSession.__init__` (after `headless=False`) and a method `TabSession._minimize_window(self)` that does exactly the three protocol calls above on `self.context` and `self.page`, inside a `try/except Exception` that swallows every failure (a window that cannot be minimised must never break a job: record nothing, raise nothing). In `__init__`, call it right after `self.page` is set and BEFORE the `self.page.goto(...)` of the origin, only when `minimize` is true. Do not change `LAUNCH_ARGS`, the profile path, the launch call or any other method.
b. New test `lib/opal_data_harvest/test_cb5_window_minimised.py` (no network, no real browser). Fake Playwright by monkeypatching `playwright.sync_api.sync_playwright` (the class imports it inside `__init__`) with a fake whose `.start()` returns an object holding `.chromium.launch_persistent_context(**kwargs)` -> a fake context with `.pages` (an empty list), `.new_page()` -> a fake page (with `.goto(url, wait_until=None, timeout=None)` doing nothing, and `.url`), `.new_cdp_session(page)` -> a fake CDP session that RECORDS every `.send(method, params)` call and answers `Browser.getWindowForTarget` with `{"windowId": 7}`, and `.close()`; also a fake `.stop()`. Use a temp directory as the profile root. Then:
   - (1) with the default, the CDP calls are exactly `Browser.getWindowForTarget` then `Browser.setWindowBounds` with `{"windowId": 7, "bounds": {"windowState": "minimized"}}`, and both happen BEFORE the page's `goto`;
   - (2) with `minimize=False` there are NO CDP calls;
   - (3) a CDP session whose `.send` raises: `TabSession(...)` still constructs, with the page set;
   - (4) the launch kwargs equal the original: `channel` "chrome", `headless` False, `args` equal to `tab_transport.LAUNCH_ARGS`, and `user_data_dir` under the profile root;
   - (5) **A MUTANT:** with `TabSession._minimize_window` monkeypatched to do nothing, arm (1) FAILS (assert that it does). This proves (1) discriminates.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a real browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/test_cb5_window_minimised.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~144/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-5"><invocation>python -m pytest lib/opal_data_harvest/test_cb5_window_minimised.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-5"><invocation>python -m pytest lib/opal_data_harvest/test_aw2_sa_tab.py lib/opal_data_harvest/test_ae2_hookup.py lib/opal_data_harvest/test_ae2_one_identity.py lib/opal_data_harvest/test_ai2_ft_session.py lib/opal_data_harvest/test_aj4_keepalive_event.py lib/opal_data_harvest/test_ae5_hookup.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^47 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `47 passed`: the base's own count.
- **Dry-run at the base (issuer, dell1, 2026-10-15 ~19:4xZ):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`47 passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. On a clean main checkout one failure is known (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree also shows `test_harvest_grammar.py::test_one_writer_for_both_channels` (a missing import outside the cone). Add none.
- **LINE ENDINGS:** `tab_transport.py` may carry mixed line endings. Edit it so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W144-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~144/AMGT_HARVST.TO-HVST-cb-5.the-runner-window-is-minimised-by-the-browser.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-5.the-runner-window-is-minimised-by-the-browser` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-5.the-runner-window-is-minimised-by-the-browser.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO half `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md` (msg 6165): "(c) start-minimized first, then (a)... If (c) fails, do not register headful: bring the question back." The CTO named `--start-minimized`; this seat measured it before the cut and it does not minimise (`IsIconic` False at 4 s, plain Chrome, same machine), while the protocol call does. The deviation is reported to the CTO in the round-87 message.
- **The real-job criterion is the ISSUER'S** (a worker's invocations run under `timeout 120`; a headful job runs about 2.5 minutes): `deliverables/2.0.0_SA_COO_W1/round87/cb5_window_probe.py` (AC3) runs one real `wsj` job (ticker COST, no upload) from the merged head and samples every Chrome window's `IsIconic` each half second; PASS needs the job `complete_candidates` with more than 0 accepted and zero samples not minimised after a 3 second launch allowance. Its positive control (a plain Chrome window reads not minimised) was run before the cut.
- Not covered: a challenge repair (Press and Hold, slider) running in a minimised window; the CTO half asks the first cycle to be read for exactly that. If a challenge fails minimised, a follow-up restores the window for the solve.
- Direct act: ONE cell, LOCAL, about 20 product lines; no L2, L4-R or L8-L10.
- Slot ~144, worktree `C:/dev/wk-harvst-144`, branch `wk-AMGT_HARVST-144`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts` (AC2's tests read it).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>pending</status>
<round>87</round>
<workstream>RUNNER</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
