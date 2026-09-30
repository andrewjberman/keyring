# AMGT_RESAPP task order -- `AMGT-zz-2` -- `price_axis_pull.py` DERIVES ITS ROOT; NOTHING OUTSIDE ITS TREE ON `sys.path`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~181</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; the file's scheduled caller is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN by the issuer at the cut -- AC1 reads the literal (static) and the sys.path an import adds, from a linked worktree (dynamic).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-zz-2` (round 51, decomposition s.59)

`integrations/bloomberg/research/price_axis_pull.py` hardcodes a device path:
`:97` `REPO = os.environ.get("OPAL_WS_ROOT") or r"C:\Users\Opal Bloomberg\Desktop\ajb_workspace"`; `:98` puts
`REPO/integrations/bloomberg/mcp` on `sys.path` AT IMPORT; `:99-100` put `REPO` itself there; `:136` and `:143` build deliverable
paths from `REPO`. Run from a linked worktree, the import reads the MAIN workspace's files. `_REPO_SELF` (`:107-109`) already derives
the tree from `__file__`.

**Build:** the root is derived from the file's own tree (`Path(__file__).resolve().parents[3]`, the same as `_REPO_SELF`) with no
hardcoded device path and no environment override that can point it at another checkout; nothing outside this tree goes on
`sys.path` at import. `integrations/bloomberg/mcp` (for `blp_client`, imported lazily at `:252`) is added from THIS tree, and only
where it is needed (inside the function that imports `blp_client`), never at module import. `:136`/`:143` use the derived root.
Behaviour of every function is otherwise unchanged. Add or adjust a test in `test_price_axis_pull.py` that imports the module and
asserts no `sys.path` entry outside the module's tree was added.

## 2. BOUNDS

1. The one file and its one test file. Standing: no install, no push, no promote, no deploy, no vendor call, no Bloomberg call.
   REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`. Run the checks FROM YOUR WORKTREE (that is what the dynamic arm measures).

## 3. SURFACES

<paths>
integrations/bloomberg/research/price_axis_pull.py
integrations/bloomberg/research/tests/test_price_axis_pull.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~181/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_2_root.py; echo "exit=$?"</invocation><expect>(a) hardcoded root literals: 0; (b) import error: None, sys.path entries outside this checkout: 0; PRICE_AXIS_PULL DERIVES ITS ROOT: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest integrations/bloomberg/research/tests/test_price_axis_pull.py lib/research/metrics/tests/test_producer_axis_registry.py -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt;= 9 (9 at the cut, plus your new test) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~181/AMGT_RESAPP.TO-AMGT-zz-2.price-axis-pull-derives-its-root.proof_of_spec.json`. Report once: what you changed, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis ruling 2 (row Z-W1-S18). Base: AC1 FAIL (literal at line 97; from a worktree the import adds the
main workspace's paths); AC2 PASS 9. The ruling's "planted defect in the worktree reads RED" is measured directly by AC1's dynamic
arm: the cross-tree read happens only through the sys.path entries it counts (blp_client is imported lazily, so a two-file pytest
cannot reach a plant there).

<status>pending</status>
<round>51</round>
<slot>~181</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
