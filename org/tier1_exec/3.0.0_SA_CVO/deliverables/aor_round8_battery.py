"""CVO~B ROUND-8 gate-2 battery -- MY OWN fixtures against the LOCKED contract (CTO~B 023419Z)
+ the 3 fixture specifics (024233Z), pinned to commits 345c85daa + 5581c0de1.

Legs (each fires-on-defect + quiet-on-healthy where applicable):
  F1-S  frozen-as-of swap STORAGE: distinct {run-ts} keys, both retained, prior+new states as rows,
        rebuild == truth, count-blindness demonstrated (mover count identical).
  F1-D  frozen-as-of swap DETECTION: main() over the two keys -> 2 named ACCOUNT-ATTRIBUTION-DRIFT
        (from/to, raw_changed=False bug-shape). Asserted SEPARATELY from F1-S.
  F2    read-failure on an event file -> CANNOT-EVALUATE (my leg; DS covers list-fail + unparseable).
  F3    STRUCTURAL uncollapsibility: (a) key is a pure fn of run-ts ONLY (as_of not in the signature);
        (b) NEGATIVE write-path census of the committed source (every _write_parquet key expr known;
        the ONLY events/-prefix write routes through event_file_key); (c) cache-corruption never
        silently re-baselines (rebuild from events, first_run only when NO events); (d) rogue re-emit
        of an OLD frame cannot roll back rebuilt state (last-wins by event_ts).
  F4    quiet-on-no-change under a FROZEN as-of (healthy twin): compute_events EMPTY -> no file ->
        detector GREEN, _emit_alert NOT called. classify quiet on baseline/new.
  F5b   dual-state: OFF == servicing for EVERY account vs MY OWN servicing oracle (DELTA-0, own
        verdict line) + apply_resolution_fold(OFF) structural no-op; ON == fold-over-servicing;
        cross-view equality on two differently-shaped views; vintage non-mover rows UNTOUCHED.
  F5c   resolver-perturbation mutant: perturb ONE account in the resolution -> EVERY view reflects
        it mechanically (inherit-not-re-derive).
  R3    relabel value->value ONLY (EDGE-3 both blank directions excluded).
  R4    column-drop mutant: udf7 column gone -> fold collapses -> MASS change events surface it.
  R5    mover-expansion -> N named change findings (old MOVER-SET class, now per-account).
  R6    absent account: no event + state RETAINED.
  R7    legit re-designation: raw ALSO changed -> raw_changed=True.
  H     household_headline_map: inherit map + RAISES on a stale (col-less) account_team.
  NB    never-blocks: rc 0 on alert / cannot-evaluate / green paths (exercised in F1-D/F2/F4).

Exit: 0 all GUARDED / 2 defect-demonstrated / 3 placebo (a quiet leg fired).
Author: 3.0.0_SA_CVO~B, LD-0277 round-8. Stub law: stubs preserve the stubbed contract
(_emit_alert returns 0; _read_parquet returns a DataFrame).
"""
from __future__ import annotations

import inspect
import os
import re
import sys
from datetime import datetime, timezone

WS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace"
LIB = os.path.join(WS, "data", "inf", "scripts", "gold", "lib")
sys.path.insert(0, LIB)
import pandas as pd  # noqa: E402
import aor_resolution as ar  # noqa: E402
import aor_attribution_audit as au  # noqa: E402
from inflection_rep_scope import _servicing_advisor_key  # noqa: E402  (my independent OFF oracle)

FAILS, PLACEBO = [], []


def check(label, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + label + ((" [" + str(detail) + "]") if detail and not cond else ""))
    if not cond:
        FAILS.append(label)


def av2(rows):
    """rows: (account_id, rep_id, representative_name, advisor_of_record_raw)"""
    return pd.DataFrame(rows, columns=["account_id", "rep_id", "representative_name",
                                       "advisor_of_record_raw"])


NOW = datetime.now(timezone.utc)
AS_OF = "2026-07-11"  # FROZEN across both nights -- the round-7 killer axis
TODAY = NOW.strftime("%Y-%m-%d")


def ts_at(hh, mm, ss, ms):
    return NOW.strftime("%Y-%m-%d") + "T{:02d}:{:02d}:{:02d}.{:03d}Z".format(hh, mm, ss, ms)


TS1, TS2 = ts_at(2, 0, 0, 111), ts_at(2, 5, 0, 222)

# 6 accounts: 1,2 movers (joe,noel); 3-5 peter blanks; 6 IWM (rep_id 3).
AV2 = av2([(1, 12, "Peter Lee", "Joe Brandenburg"),
           (2, 12, "Peter Lee", "Noel Soderblom"),
           (3, 12, "Peter Lee", None),
           (4, 12, "Peter Lee", None),
           (5, 12, "Peter Lee", None),
           (6, 3, "Inflection Wealth Management", None)])  # full firm name: bucket 'firm' is NAME-derived
FOLD1 = {1: "joe_brandenburg", 2: "noel_soderblom"}
EXPL1 = {1: "joe_brandenburg", 2: "noel_soderblom"}

# ---------------- F1-S: STORAGE ----------------
res1 = ar.resolve_accounts(AV2, FOLD1, EXPL1, AS_OF)
ev1 = ar.compute_events({}, res1, TODAY, TS1, first_run=True)
k1 = ar.event_file_key(TS1)
state1 = ar.merge_state({}, ar.state_from_resolution(res1, TS1))

FOLD2 = {1: "noel_soderblom", 2: "joe_brandenburg"}  # the SWAP; raw/explicit UNCHANGED (bug shape)
res2 = ar.resolve_accounts(AV2, FOLD2, EXPL1, AS_OF)  # as_of FROZEN
ev2 = ar.compute_events(state1, res2, TODAY, TS2)
k2 = ar.event_file_key(TS2)

store = {}
store[k1] = ev1.copy()
ev1_frozen = store[k1].copy()
store[k2] = ev2.copy()  # the second write -- must NOT touch k1

check("F1-S.1 distinct {run-ts} keys under FROZEN as-of", k1 != k2 and k1.startswith(ar.LEDGER_EVENTS_PREFIX))
check("F1-S.2 both keys RETAINED, night-1 content untouched by night-2 write",
      set(store) == {k1, k2} and store[k1].equals(ev1_frozen))
ch = ev2[ev2["event_type"] == "change"]
check("F1-S.3 night-2 swap = 2 distinct change ROWS carrying prior AND new state",
      len(ev2) == 2 and len(ch) == 2
      and sorted(int(a) for a in ch["account_id"]) == [1, 2]
      and set(zip(ch["prior_advisor_of_record"], ch["advisor_of_record"]))
      == {("joe_brandenburg", "noel_soderblom"), ("noel_soderblom", "joe_brandenburg")},
      ev2.to_dict("records"))
reb = ar.rebuild_state_from_events([store[k1], store[k2]])
check("F1-S.4 rebuild from the two files == night-2 truth",
      reb[1]["advisor_of_record"] == "noel_soderblom" and reb[2]["advisor_of_record"] == "joe_brandenburg")
check("F1-S.5 COUNT-BLINDNESS demonstrated: mover count IDENTICAL both nights (2==2)",
      int(res1["is_mover"].sum()) == int(res2["is_mover"].sum()) == 2)

# ---------------- driver for main() (contract-preserving stubs) ----------------
def run_main(keys, frames_by_key, read_raises_on=None, lookback="2"):
    names = ("_s3", "list_event_keys", "load_events", "_emit_alert", "_publish_sns_alert")
    saved = {n: getattr(au, n) for n in names}
    cap = {"findings": None, "emit_called": False}

    def _load(s3, bucket, key):
        if read_raises_on is not None and key == read_raises_on:
            raise RuntimeError("read boom")
        return frames_by_key[key]

    def _emit(findings, window):
        cap["findings"], cap["emit_called"] = findings, True
        return 0  # the real _emit_alert returns 0 -- preserve the contract

    au._s3 = lambda: object()
    au.list_event_keys = lambda *a, **k: list(keys)
    au.load_events = _load
    au._emit_alert = _emit
    au._publish_sns_alert = lambda *a, **k: None
    try:
        rc = au.main(["--bucket", "b", "--lookback-days", lookback])
    finally:
        for n, v in saved.items():
            setattr(au, n, v)
    return rc, cap

# ---------------- F1-D: DETECTION (separate from storage) ----------------
rc, cap = run_main([k1, k2], {k1: ev1, k2: ev2})
f = cap["findings"] or []
drift = [x for x in f if x["code"] == "ACCOUNT-ATTRIBUTION-DRIFT"]
check("F1-D.1 detector ALERTS on the frozen-as-of swap (2 named findings, not 'baseline day', not green)",
      len(drift) == 2 and sorted(x["account_id"] for x in drift) == [1, 2],
      [x.get("code") for x in f])
check("F1-D.2 findings carry from/to + raw_changed=False (bug shape -> 'likely servicing/derivation bug')",
      all(x.get("from") and x.get("to") and x.get("raw_changed") is False for x in drift)
      and all("servicing/derivation bug" in x["detail"] for x in drift))
check("F1-D.3 never-blocks: rc 0 WHILE alerting", rc == 0)

# ---------------- F2: read-failure -> CANNOT-EVALUATE ----------------
rc, cap = run_main([k1, k2], {k1: ev1, k2: ev2}, read_raises_on=k2)
codes = [x["code"] for x in (cap["findings"] or [])]
check("F2.1 event-file READ failure -> CANNOT-EVALUATE emitted (not green, not a swallowed WARN)",
      codes == ["CANNOT-EVALUATE"], codes)
check("F2.2 never-blocks: rc 0 on the cannot-evaluate path", rc == 0)

# ---------------- F3: STRUCTURAL uncollapsibility ----------------
sig = list(inspect.signature(ar.event_file_key).parameters)
check("F3.a key is a pure fn of run-ts ONLY (signature has no as_of/date axis)",
      sig == ["event_ts", "prefix"]
      and ar.event_file_key(TS2) == ar.event_file_key(TS2)      # idempotent naming
      and ar.event_file_key(TS1) != ar.event_file_key(TS2), sig)

src = open(os.path.join(LIB, "aor_resolution.py"), encoding="utf-8").read()
writes = [m.group(1) for line in src.splitlines() if "_write_parquet(" in line and "def _write_parquet" not in line
          for m in [re.search(r".*bucket,\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", line)] if m]
ekey_binding = re.search(r"ekey\s*=\s*event_file_key\(event_ts\)", src)
check("F3.b NEGATIVE write-path census: write keys == {RESOLUTION_KEY, ekey, LEDGER_STATE_KEY} and the"
      " ONLY events/-write is ekey = event_file_key(event_ts) -- no fixed/deterministic events path exists",
      sorted(set(writes)) == ["LEDGER_STATE_KEY", "RESOLUTION_KEY", "ekey"] and ekey_binding is not None,
      writes)

saved_rp, saved_lk = ar._read_parquet, ar.list_event_keys
try:
    def _rp_cache_corrupt(s3, bucket, key):
        if key == ar.LEDGER_STATE_KEY:
            raise RuntimeError("cache corrupt")
        return {k1: ev1, k2: ev2}[key]
    ar._read_parquet = _rp_cache_corrupt
    ar.list_event_keys = lambda s3, bucket, prefix=ar.LEDGER_EVENTS_PREFIX: [k1, k2]
    st, first, _bad = ar.load_prior_state(object(), "b")
    check("F3.c corrupt cache does NOT silently re-baseline: rebuilt from events, first_run=False,"
          " truth == night-2", first is False and st[1]["advisor_of_record"] == "noel_soderblom")
    ar.list_event_keys = lambda s3, bucket, prefix=ar.LEDGER_EVENTS_PREFIX: []
    st0, first0, _bad = ar.load_prior_state(object(), "b")
    check("F3.c2 first_run=True ONLY when NO events exist", first0 is True and st0 == {})
finally:
    ar._read_parquet, ar.list_event_keys = saved_rp, saved_lk

rogue = ar.rebuild_state_from_events([ev2, ev1, ev1.copy()])  # rogue re-emit of the OLD frame
check("F3.d rogue re-append of an OLD event frame cannot roll back state (last-wins by event_ts)",
      rogue[1]["advisor_of_record"] == "noel_soderblom")

# ---------------- F4: quiet-on-no-change (healthy twin) ----------------
ev_none = ar.compute_events(state1, res1, TODAY, TS2)  # SAME resolution again, FROZEN as-of
check("F4.1 no-change run under a frozen as-of emits ZERO event rows (quiet is correct)",
      len(ev_none) == 0)
rc, cap = run_main([k1], {k1: ev1})  # window holds only the baseline file
check("F4.2 detector GREEN on a baseline-only window; _emit_alert NOT called (non-placebo)",
      rc == 0 and cap["emit_called"] is False)
if cap["emit_called"]:
    PLACEBO.append("F4.2")
check("F4.3 classify quiet on baseline/new state-loads", au.classify_events(ev1) == [])

# ---------------- F5b: DUAL-STATE ----------------
res_off = ar.resolve_accounts(AV2, {}, {}, AS_OF)
my_servicing = {}
for r in AV2.itertuples():
    key, _ = _servicing_advisor_key(r.rep_id, r.representative_name)
    my_servicing[int(r.account_id)] = key
off_by = {int(r.account_id): str(r.advisor_key) for r in res_off.itertuples()}
check("F5b-OFF DELTA-0: under OFF every account's advisor_key == MY OWN servicing oracle"
      " (6/6, incl rep_id-3 IWM), zero movers",
      off_by == my_servicing and int(res_off["is_mover"].sum()) == 0,
      {a: (off_by.get(a), my_servicing.get(a)) for a in my_servicing if off_by.get(a) != my_servicing.get(a)})

view = pd.DataFrame({"account_id": [1, 2, 3, 6], "advisor_key": ["vintage_x", "peter_lee", "peter_lee",
                                                                 "inflection_wealth_management"],
                     "rep_bucket": ["individual", "individual", "individual", "firm"]})
view_before = view.copy()
_, n_off = ar.apply_resolution_fold(view, res_off)
check("F5b-OFF apply_resolution_fold(OFF) is a STRUCTURAL no-op (0 rows touched, frame byte-identical"
      " -- incl the vintage row)", n_off == 0 and view.equals(view_before))

res_on = ar.resolve_accounts(AV2, FOLD1, EXPL1, AS_OF)
on_by = {int(r.account_id): str(r.advisor_key) for r in res_on.itertuples()}
check("F5b-ON fold-over-servicing: movers 1->joe 2->noel (rep_bucket individual), non-movers == servicing",
      on_by[1] == "joe_brandenburg" and on_by[2] == "noel_soderblom"
      and all(on_by[a] == my_servicing[a] for a in (3, 4, 5, 6))
      and set(res_on[res_on["is_mover"] == True]["rep_bucket"]) == {"individual"})  # noqa: E712

# cross-view equality: two differently-shaped views inherit IDENTICAL per-account keys
view_c01 = pd.DataFrame({"account_id": [1, 1, 2, 3, 6], "amount": [10, 20, 30, 40, 50],
                         "advisor_key": ["peter_lee"] * 5, "rep_bucket": ["individual"] * 5})  # txn-shaped
view_d00c = pd.DataFrame({"account_id": [1, 2, 3, 5], "aua": [1.0, 2.0, 3.0, 4.0],
                          "advisor_key": ["peter_lee"] * 4, "rep_bucket": ["individual"] * 4})  # acct-shaped
ar.apply_resolution_fold(view_c01, res_on)
ar.apply_resolution_fold(view_d00c, res_on)
eq = all(set(view_c01[view_c01["account_id"] == a]["advisor_key"]) ==
         set(view_d00c[view_d00c["account_id"] == a]["advisor_key"]) == {on_by[a]}
         for a in (1, 2, 3))
check("F5b-XV cross-view equality (ON): txn-shaped and account-shaped views carry IDENTICAL per-account"
      " advisor_key == the resolution's", eq)
check("F5b-VN vintage preservation: NON-mover rows untouched on every basis (acct 3 stays peter on both)",
      set(view_c01[view_c01["account_id"] == 3]["advisor_key"]) == {"peter_lee"}
      and set(view_d00c[view_d00c["account_id"] == 5]["advisor_key"]) == {"peter_lee"})

# ---- F5b FULL-attach mode (A_00/A_01 current-snapshot; CTO~B fact 2: BOTH modes DELTA-0) ----
full_off = pd.DataFrame({"account_id": [1, 2, 3, 6],
                         "advisor_key": [my_servicing[a] for a in (1, 2, 3, 6)],
                         "rep_bucket": ["individual", "individual", "individual", "firm"]})
full_before = full_off.copy()
ar.attach_advisor_key(full_off, res_off)
check("F5b-FULL-OFF: FULL attach under OFF re-stamps servicing onto a servicing-correct current"
      " snapshot -> values UNCHANGED (DELTA-0 for the A_00/A_01 mode)",
      full_off.equals(full_before))
full_on = full_before.copy()
ar.attach_advisor_key(full_on, res_on)
check("F5b-FULL-ON: FULL attach under ON moves ONLY the movers (1->joe, 2->noel; 3,6 stay servicing)",
      list(full_on["advisor_key"]) == ["joe_brandenburg", "noel_soderblom", "peter_lee",
                                       "inflection_wealth_management"]
      and list(full_on["rep_bucket"]) == ["individual", "individual", "individual", "firm"])
vint = pd.DataFrame({"account_id": [1], "advisor_key": ["vintage_x"], "rep_bucket": ["individual"]})
ar.attach_advisor_key(vint, res_off)
check("F5b-MODE-DISCRIMINATION: a FULL attach on a VINTAGE frame DOES overwrite history (vintage_x ->"
      " servicing) -- demonstrating WHY the 7 vintage consumers ride movers-only; the census below"
      " asserts the mode assignment", list(vint["advisor_key"]) == ["peter_lee"])

# ---------------- F5c: resolver-perturbation MUTANT ----------------
res_mut = res_on.copy()
m = res_mut["account_id"] == 3
res_mut.loc[m, "advisor_key"] = "noel_soderblom"
res_mut.loc[m, "is_mover"] = True
res_mut.loc[m, "rep_bucket"] = "individual"
va = pd.DataFrame({"account_id": [3], "advisor_key": ["peter_lee"], "rep_bucket": ["individual"]})
vb = pd.DataFrame({"account_id": [3, 3], "x": [1, 2], "advisor_key": ["peter_lee"] * 2,
                   "rep_bucket": ["individual"] * 2})
ar.apply_resolution_fold(va, res_mut)
ar.apply_resolution_fold(vb, res_mut)
vc = pd.DataFrame({"account_id": [3], "advisor_key": [pd.NA]})
ar.attach_advisor_key(vc, res_mut, rep_bucket_col=None)
check("F5c perturbation PROPAGATES: one flipped resolution row -> EVERY view reflects it mechanically"
      " (inherit, not re-derive)",
      set(va["advisor_key"]) == set(vb["advisor_key"]) == set(vc["advisor_key"]) == {"noel_soderblom"})

# ---------------- R3: relabel EDGE-3 (value->value only, both blank directions excluded) ----------------
state_r = {1: {"advisor_of_record": "joe_brandenburg", "advisor_of_record_raw": "Joe Brandenburg"},
           3: {"advisor_of_record": "peter_lee", "advisor_of_record_raw": None},
           4: {"advisor_of_record": "peter_lee", "advisor_of_record_raw": "Peter Lee"}}
av2_r = av2([(1, 12, "Peter Lee", "J. Brandenburg"),   # value->value, advisor unchanged -> relabel
             (3, 12, "Peter Lee", "Peter Lee"),          # blank->populated -> NOT an event
             (4, 12, "Peter Lee", None)])                # populated->blank -> NOT an event
ev_r = ar.compute_events(state_r, ar.resolve_accounts(av2_r, {1: "joe_brandenburg"}, {}, AS_OF), TODAY, TS2)
check("R3 relabel fires value->value ONLY (1 relabel; blank<->populated excluded both directions)",
      len(ev_r) == 1 and ev_r.iloc[0]["event_type"] == "relabel" and int(ev_r.iloc[0]["account_id"]) == 1,
      ev_r.to_dict("records"))
fr = au.classify_events(ev_r)
check("R3.b classify -> ACCOUNT-RAW-RELABEL-NO-SHIFT named",
      len(fr) == 1 and fr[0]["code"] == "ACCOUNT-RAW-RELABEL-NO-SHIFT" and fr[0]["account_id"] == 1)

# ---------------- R4: column-drop mutant -> fold collapses -> MASS change events surface it ----------------
av2_nocol = AV2.drop(columns=["advisor_of_record_raw"])
res_nocol = ar.resolve_accounts(av2_nocol, {}, {}, AS_OF)  # raws gone => fold would build EMPTY
ev_col = ar.compute_events(state1, res_nocol, TODAY, TS2)
ch_col = ev_col[ev_col["event_type"] == "change"]
check("R4 udf7 COLUMN DROP surfaces as MASS change events (both movers revert -> 2 changes fire; "
      "the retired SOURCE-DRIFT-COLUMN class is covered by the ledger diff where it matters)",
      len(ch_col) == 2 and sorted(int(a) for a in ch_col["account_id"]) == [1, 2])

# ---------------- R5: mover EXPANSION -> N named findings ----------------
FOLD5 = {**FOLD1, 3: "joe_brandenburg", 4: "joe_brandenburg", 5: "joe_brandenburg"}
ev_x = ar.compute_events(state1, ar.resolve_accounts(AV2, FOLD5, EXPL1, AS_OF), TODAY, TS2)
fx = au.classify_events(ev_x)
check("R5 gross mover expansion -> 3 NAMED per-account change findings (the retired MOVER-SET class,"
      " now account-grain)", sorted(x["account_id"] for x in fx) == [3, 4, 5]
      and all(x["code"] == "ACCOUNT-ATTRIBUTION-DRIFT" for x in fx))

# ---------------- R6: absent account -> no event + state RETAINED ----------------
ev_abs = ar.compute_events(state1, ar.resolve_accounts(AV2[AV2["account_id"] != 2], FOLD1, EXPL1, AS_OF),
                           TODAY, TS2)
st_abs = ar.merge_state(state1, ar.state_from_resolution(
    ar.resolve_accounts(AV2[AV2["account_id"] != 2], FOLD1, EXPL1, AS_OF), TS2))
# R6 INVERTED (round-8.2 F7). The old arm asserted "emits NOTHING -- coverage axis owned elsewhere".
# THAT ASSERTION ENCODED THE DEFECT. I measured the hand-off: NOTHING owned the coverage axis
# (INF_D_10 = 0 refs, INF_D_11 = docstring prose only, no coverage detector anywhere in inf gold), and
# it composed with F2 into a silent served-number defect with no alarm. CTO ruled: rebuild the detector.
# A HAND-OFF TO AN OWNER YOU HAVE NOT VERIFIED IS A DELETION. My own battery carried that unverified
# premise for two rounds -- the fixture, not the code, was the thing that was wrong.
_drops = int((ev_abs["event_type"] == "coverage_drop").sum()) if len(ev_abs) else 0
check("R6 vanished account EMITS coverage_drop (F7) and its state is RETAINED",
      _drops == 1 and st_abs[2]["advisor_of_record"] == "noel_soderblom")

# ---------------- R7: legit re-designation discriminated ----------------
av2_l = AV2.copy()
av2_l.loc[av2_l["account_id"] == 1, "advisor_of_record_raw"] = "Patrick Scanlan"
ev_l = ar.compute_events(state1, ar.resolve_accounts(av2_l, {1: "patrick_scanlan", 2: "noel_soderblom"},
                                                     EXPL1, AS_OF), TODAY, TS2)
fl = [x for x in au.classify_events(ev_l) if x["code"] == "ACCOUNT-ATTRIBUTION-DRIFT"]
check("R7 legit re-designation: raw ALSO changed -> raw_changed=True + 'likely legitimate' in detail",
      len(fl) == 1 and fl[0]["raw_changed"] is True and "legitimate re-designation" in fl[0]["detail"])

# ---------------- H: household headline inherit ----------------
at = pd.DataFrame({"household_id": ["hh286", "hh300"],
                   "household_headline_advisor_key": ["noel_soderblom", "peter_lee"]})
hm = ar.household_headline_map(at)
check("H.1 household_headline_map inherits C_07's stamped headline (hh286 -> noel)",
      hm.get("hh286") == "noel_soderblom" and hm.get("hh300") == "peter_lee", hm)
try:
    ar.household_headline_map(pd.DataFrame({"household_id": ["hh286"]}))
    stale_raised = False
except RuntimeError:
    stale_raised = True
check("H.2 STALE pre-round-8 account_team (no stamped col) -> RAISES (refuse to serve an empty headline"
      " set), never a silent empty map", stale_raised)

print()
if PLACEBO:
    print("ROUND-8 BATTERY: PLACEBO-FIRING on %s" % PLACEBO)
    sys.exit(3)
if FAILS:
    print("ROUND-8 BATTERY: %d DEFECT(S)/GAP(S): %s" % (len(FAILS), FAILS))
    sys.exit(2)
print("ROUND-8 BATTERY: ALL LEGS GUARDED (F1-S/F1-D split, F2, F3 structural, F4 quiet, F5b dual-state,"
      " F5c mutant, R3-R7 remapped, H household) on 345c85daa+5581c0de1.")
sys.exit(0)
