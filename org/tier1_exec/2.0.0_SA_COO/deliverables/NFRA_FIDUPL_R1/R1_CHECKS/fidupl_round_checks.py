#!/usr/bin/env python3
"""NFRA_FIDUPL round 1 -- the mechanical checks the task orders name (2.0.0_SA_COO~P1, 2026-10-19).

Usage (from the repo or worktree root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py <check>

Each check prints exactly one line: R1-<ID>-OK ... or R1-<ID>-FAIL <reason>. Only that line is the verdict.
Checks never write outside a temp dir, never print a secret and never print file contents. Python 3.9 syntax.
"""
import csv
import json
import os
import re
import subprocess
import sys
import tempfile

CF = "infra/aws/ec2/canonical-fidelity"
TF_ROOT = "infra/aws/terraform/canonical-fidelity-ec2"

TEST_FILES = {
    "fu1": ("%s/tests/test_quo_otp.py" % CF, [
        "test_reads_only_configured_line_and_sender", "test_ignores_messages_before_window_opens",
        "test_returns_code_for_fresh_message", "test_no_code_result_is_distinct_after_window",
        "test_code_never_logged_or_printed", "test_sends_browser_user_agent_and_raw_key_header",
        "test_other_line_never_read"]),
    "fu2a": ("%s/tests/test_signin.py" % CF, [
        "test_steps_in_order_password_factor_code_authorize", "test_selects_otpsms_factor",
        "test_code_requested_after_send_instant", "test_sign_in_refused_classified",
        "test_code_never_arrived_classified", "test_no_secret_in_logs_or_env",
        "test_persistent_profile_dir_used"]),
    "fu2b": ("%s/tests/test_signin_recon.py" % CF, [
        "test_finds_g_number_column_by_index_and_counts", "test_prints_no_values",
        "test_reports_column_count", "test_no_g_column_reports_none"]),
    "fu2c": ("%s/tests/test_gprobe.py" % CF, [
        "test_probe_switches_current_g_once_and_back", "test_probe_never_sets_default",
        "test_probe_restores_starting_g_even_on_error", "test_probe_compares_before_after_counts",
        "test_probe_prints_no_account_numbers_or_g_values", "test_probe_posts_form_without_isdefault",
        "test_probe_asserts_current_cell_equals_requested", "test_probe_uses_www2_jsp_endpoint"]),
    "fu2t": ("%s/tests/test_login_trace.py" % CF, [
        "test_trace_records_step_outline_without_values", "test_trace_stops_at_first_failing_step",
        "test_trace_never_records_secret_or_code", "test_locators_found_by_type_not_by_assumed_name",
        "test_trace_mode_stops_after_sms_request", "test_trace_records_network_calls_without_bodies",
        "test_trace_records_form_state_without_values", "test_trace_records_error_text_after_next",
        "test_trace_records_console_error_count", "test_trace_records_fingerprint_facts",
        "test_error_detection_requires_visible_text", "test_fingerprint_sets_window_chrome_and_languages",
        "test_user_agent_matches_installed_chromium_version", "test_trace_records_failed_request_shape_without_values",
        "test_trace_records_response_error_text", "test_trace_records_third_party_failures",
        "test_trace_notes_cookie_names_before_password_post", "test_preflow_runs_only_when_att_absent",
        "test_preflow_skipped_when_att_present",
        "test_launch_is_headed_under_a_started_xvfb", "test_launch_reuses_an_existing_display",
        "test_launch_fails_loud_when_xvfb_is_missing", "test_no_request_is_routed_or_blocked",
        "test_text_me_the_code_button_sends_the_sms", "test_call_me_button_is_never_clicked",
        "test_display_waits_for_the_x_socket", "test_launch_args_disable_extensions",
        "test_display_is_set_before_the_playwright_driver_starts"]),
    "fr1a": ("%s/tests/test_gswitch.py" % CF, [
        "test_parses_current_default_and_options", "test_switch_posts_form_without_isdefault",
        "test_switch_asserts_current_equals_requested", "test_switch_failure_raises_and_names_no_value"]),
    "fr1b": ("%s/tests/test_attribute.py" % CF, [
        "test_sweeps_every_option_and_restores_start", "test_restores_start_even_on_error",
        "test_never_sets_default", "test_summary_counts_only", "test_pages_account_list_until_short_page"]),
    "fr2": ("%s/tests/test_split.py" % CF, [
        "test_rows_split_by_account_to_firm_addresses", "test_account_under_two_g_of_one_firm_lands_once",
        "test_account_under_two_firms_listed_not_landed", "test_unplaced_accounts_listed",
        "test_unregistered_firm_scope_listed_not_landed", "test_raw_line_bytes_preserved",
        "test_dry_run_writes_nothing", "test_record_has_counts_and_lists",
        "test_unmapped_label_listed_not_landed", "test_record_lists_unplaced_and_conflict_accounts"]),
    "fr6": ("%s/tests/test_adapters.py" % CF, [
        "test_get_text_follows_redirect_and_returns_text", "test_post_form_sends_urlencoded_body_without_logging_values",
        "test_account_lister_pages_until_short_page", "test_extract_accounts_finds_list_by_key_not_by_container_name",
        "test_extract_failure_names_only_keys", "test_daily_real_deps_use_adapters",
        "test_extract_accounts_uses_measured_container_and_number_key", "test_lister_stops_at_available_total",
        "test_lister_sends_session_cache_id_on_later_pages", "test_lister_fails_loud_when_short_of_available"]),
    "fr3": ("%s/tests/test_backfill.py" % CF, [
        "test_windows_walk_backward_in_chunks", "test_stops_on_entitlement_refusal_and_names_it",
        "test_stops_on_retention_limit_and_names_it", "test_stops_at_account_open_date",
        "test_record_names_earliest_date_per_g_and_kind", "test_never_prints_g_numbers",
        "test_calls_injected_lander_per_window"]),
    "fr4": ("%s/tests/test_box_daily.py" % CF, [
        "test_daily_sequence_signin_fetch_land_attribute_split_record",
        "test_attribution_failure_still_records_and_exits_nonzero",
        "test_split_failure_exits_nonzero_after_land",
        "test_config_pointers_accept_firm_labels_and_account_columns",
        "test_main_chooses_daily_mode_from_config"]),
    "fu3": ("%s/tests/test_fetch.py" % CF, [
        "test_lists_then_downloads_six", "test_sends_xsrf_header",
        "test_only_completed_rows_of_the_six_names", "test_missing_file_reported_not_silent",
        "test_export_not_generated_yet_class", "test_download_refused_class",
        "test_bytes_written_exactly_as_served", "test_listing_has_sha256_and_contract_keys"]),
    "fu4": ("%s/tests/test_land.py" % CF, [
        "test_lands_six_to_builder_addresses", "test_scope_is_a_parameter",
        "test_address_called_at_landing_time", "test_content_date_from_first_field",
        "test_unreadable_date_is_failure_not_guess", "test_non_trading_day_is_failure",
        "test_same_sha_lands_once", "test_run_record_shape", "test_missing_file_exits_nonzero",
        "test_never_writes_outside_fidelity_prefix"]),
    "fu5": ("%s/tests/test_box_run.py" % CF, [
        "test_calls_signin_fetch_land_in_order", "test_stage_failure_exits_nonzero",
        "test_failure_still_writes_record_via_lander", "test_no_secret_in_environment",
        "test_reads_config_pointers_only"]),
}
SIX = ["account.txt", "position.txt", "balance.txt", "prices.txt", "security.txt", "transact.txt"]


def out(line):
    print(line)
    return 0


def run(cmd, timeout=100, cwd=None, env=None):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, env=env)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "timeout"
    except OSError as e:
        return 127, str(e)


def tests(cid):
    rel, names = TEST_FILES[cid]
    tag = "R1-%s" % cid.upper()
    if not os.path.isfile(rel):
        return out("%s-FAIL absent %s" % (tag, rel))
    text = open(rel, encoding="utf-8", errors="replace").read()
    missing = [n for n in names if ("def %s(" % n) not in text]
    if missing:
        return out("%s-FAIL missing tests %s" % (tag, ",".join(missing)))
    rc, o = run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", rel])
    m = re.search(r"(\d+) passed", o)
    if rc != 0 or not m or "failed" in o or "error" in o.lower().split("passed")[-1]:
        return out("%s-FAIL pytest rc=%s %s" % (tag, rc, o.strip().splitlines()[-1] if o.strip() else ""))
    if int(m.group(1)) < len(names):
        return out("%s-FAIL only %s passed of %d required" % (tag, m.group(1), len(names)))
    return out("%s-OK passed=%s" % (tag, m.group(1)))


def synth_handoff(d, date="20261016", with_listing=True):
    """Six synthetic files: quoted CSV, no header, content date first, no client data."""
    for n in SIX:
        with open(os.path.join(d, n), "w", newline="", encoding="ascii") as f:
            w = csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([date, "SYNTH", n, "1"])
            w.writerow([date, "SYNTH", n, "2"])
    if with_listing:
        rows = []
        for n in SIX:
            b = open(os.path.join(d, n), "rb").read()
            import hashlib
            rows.append({"fileName": n, "fileType": "X", "profileId": None, "requestId": None,
                         "fileCreatedTimestamp": None, "fileDeliveredTimestamp": None,
                         "fileStatusDescription": "COMPLETED", "bytes": len(b),
                         "sha256": hashlib.sha256(b).hexdigest()})
        json.dump({"schema": "fidelity-handoff/1", "source": "person", "business_day_requested": "2026-10-19",
                   "fetched_at": "2026-10-19T20:00:00Z", "rows": rows, "missing": [], "failure": None},
                  open(os.path.join(d, "listing.json"), "w"))


class FakeSession(object):
    """The session interface FU-s-3 is built against (see the FU-s-3 face)."""

    def __init__(self, rows, files, status=200):
        self.rows, self.files, self.status = rows, files, status
        self.calls = []

    def xsrf_token(self):
        return "synthetic-xsrf"

    def post_json(self, path, body, headers=None):
        self.calls.append(("POST", path, body, headers or {}))
        return 200, {"statusElements": self.rows}

    def get_bytes(self, path, params, headers=None):
        self.calls.append(("GET", path, params, headers or {}))
        return self.status, self.files.get(params.get("fileName"), b"")


def fu3_contract():
    tag = "R1-FU3C"
    if not os.path.isfile("%s/fetch.py" % CF):
        return out("%s-FAIL absent %s/fetch.py" % (tag, CF))
    sys.path.insert(0, CF)
    try:
        import importlib
        fetch = importlib.import_module("fetch")
        rows = [{"profileId": "p1", "requestId": "r%d" % i, "fileType": "T%d" % i, "fileName": n,
                 "fileStatusDescription": "COMPLETED", "fileCreatedTimestamp": "2026-10-19T17:32:07Z",
                 "fileDeliveredTimestamp": "2026-10-19T17:32:08Z"} for i, n in enumerate(SIX)]
        files = dict((n, b'"20261016","SYNTH","%s"\r\n' % n.encode("ascii")) for n in SIX)
        with tempfile.TemporaryDirectory() as d:
            sess = FakeSession(rows, files)
            listing = fetch.fetch_day(sess, "2026-10-19", d)
            lj = json.load(open(os.path.join(d, "listing.json"), encoding="utf-8"))
            need = ["schema", "source", "business_day_requested", "fetched_at", "rows", "missing", "failure"]
            bad = [k for k in need if k not in lj]
            ok_rows = len(lj.get("rows", [])) == 6 and all(
                set(["fileName", "fileType", "bytes", "sha256"]) <= set(r) for r in lj.get("rows", []))
            same = all(open(os.path.join(d, n), "rb").read() == files[n] for n in SIX)
            if bad or not ok_rows or not same or lj.get("source") != "automated" or lj.get("failure") is not None:
                return out("%s-FAIL listing keys missing=%s rows_ok=%s bytes_same=%s source=%s failure=%s"
                           % (tag, bad, ok_rows, same, lj.get("source"), lj.get("failure")))
            if not isinstance(listing, dict):
                return out("%s-FAIL fetch_day returned %s not a dict" % (tag, type(listing).__name__))
        return out("%s-OK rows=6 listing=fidelity-handoff/1" % tag)
    except Exception as e:  # noqa: BLE001 -- a check reports, it does not raise
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def fu4_dry():
    tag = "R1-FU4D"
    if not os.path.isfile("%s/land.py" % CF):
        return out("%s-FAIL absent %s/land.py" % (tag, CF))
    with tempfile.TemporaryDirectory() as d:
        synth_handoff(d)
        rc, o = run([sys.executable, "%s/land.py" % CF, "--handoff-dir", d, "--scope", "alongside", "--dry-run"])
        dests = re.findall(r"DRYRUN dest=(s3://opal-data-assets/fidelity/alongside/bronze/[a-z]+/20261016/[a-z]+\.txt)", o)
        if rc != 0 or len(set(dests)) != 6:
            return out("%s-FAIL rc=%s dests=%d last=%s" % (tag, rc, len(set(dests)),
                                                         o.strip().splitlines()[-1][:100] if o.strip() else ""))
    return out("%s-OK dests=6" % tag)


def fu5_boot():
    tag = "R1-FU5B"
    p = "%s/box/bootstrap.sh" % CF
    if not os.path.isfile(p):
        return out("%s-FAIL absent %s" % (tag, p))
    rc, o = run(["bash", "-n", p])
    if rc != 0:
        return out("%s-FAIL bash -n rc=%s" % (tag, rc))
    text = open(p, encoding="utf-8").read()
    if "playwright install" not in text:
        return out("%s-FAIL bootstrap never installs a browser" % tag)
    if re.search(r"(?im)^\s*export\s+\w*(PASSWORD|SECRET|API_?KEY|TOKEN)\w*=", text):
        return out("%s-FAIL bootstrap exports a secret-named variable" % tag)
    if re.search(r"[^\x00-\x7f]", text):
        return out("%s-FAIL non-ASCII in bootstrap" % tag)
    return out("%s-OK bash -n clean, browser install present, no secret export" % tag)


def tf_validate():
    tag = "R1-FU6V"
    if not os.path.isdir(TF_ROOT):
        return out("%s-FAIL absent %s" % (tag, TF_ROOT))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "init", "-backend=false", "-input=false", "-no-color"], 110)
    if rc != 0:
        return out("%s-FAIL init rc=%s %s" % (tag, rc, o.strip().splitlines()[-1][:100] if o.strip() else ""))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "validate", "-no-color"], 110)
    if rc != 0 or "Success! The configuration is valid." not in o:
        return out("%s-FAIL validate rc=%s" % (tag, rc))
    return out("%s-OK Success! The configuration is valid." % tag)


def tf_guard():
    tag = "R1-FU6G"
    if not os.path.isdir(TF_ROOT):
        return out("%s-FAIL absent %s" % (tag, TF_ROOT))
    text = ""
    for fn in sorted(os.listdir(TF_ROOT)):
        if fn.endswith(".tf"):
            text += open(os.path.join(TF_ROOT, fn), encoding="utf-8").read() + "\n"
    if not text.strip():
        return out("%s-FAIL no .tf files" % tag)
    bad = []
    if re.search(r"\bingress\s*\{", text) or "aws_vpc_security_group_ingress_rule" in text or re.search(r'type\s*=\s*"ingress"', text):
        bad.append("an ingress rule")
    if re.search(r"ingress\s*\{[^}]*0\.0\.0\.0/0", text):
        bad.append("0.0.0.0/0 inside an ingress block")
    if re.search(r":secret:[^\"\s]*\*", text):
        bad.append("a secret prefix wildcard")
    lines = text.splitlines()
    star = re.compile(r'"?[Rr]esources?"?\s*[:=]\s*(\[\s*)?"\*"')
    for i, ln in enumerate(lines):
        if star.search(ln) and not any("STAR-OK:" in x for x in lines[max(0, i - 3):i + 1]):
            bad.append("a Resource star without a STAR-OK comment (line %d)" % (i + 1))
    if "aws_secretsmanager_secret_version" in text:
        bad.append("a secret VERSION (a value in state)")
    if "prevent_destroy" not in text:
        bad.append("no prevent_destroy on the secret")
    if re.search(r"[^\x00-\x7f]", text):
        bad.append("non-ASCII")
    if bad:
        return out("%s-FAIL %s" % (tag, "; ".join(bad)))
    return out("%s-OK no ingress, no wildcard secret grant, no secret version, prevent_destroy present, every Resource star carries STAR-OK" % tag)


def tf_plan():
    tag = "R1-FU6P"
    if not os.path.isdir(TF_ROOT):
        return out("%s-FAIL absent %s" % (tag, TF_ROOT))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "init", "-input=false", "-no-color"], 110)
    if rc != 0:
        return out("%s-FAIL init rc=%s" % (tag, rc))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "plan", "-input=false", "-no-color"], 115)
    m = re.search(r"Plan: (\d+) to add, 0 to change, 0 to destroy\.", o)
    if rc != 0 or not m:
        return out("%s-FAIL plan rc=%s %s" % (tag, rc, o.strip().splitlines()[-1][:100] if o.strip() else ""))
    return out("%s-OK Plan: %s to add, 0 to change, 0 to destroy." % (tag, m.group(1)))


def tf_nochange():
    tag = "R1-FU7A"
    if not os.path.isdir(TF_ROOT):
        return out("%s-FAIL absent %s" % (tag, TF_ROOT))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "init", "-input=false", "-no-color"], 110)
    if rc != 0:
        return out("%s-FAIL init rc=%s" % (tag, rc))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "plan", "-input=false", "-no-color", "-detailed-exitcode"], 115)
    if rc != 0 or "No changes." not in o:
        return out("%s-FAIL plan rc=%s (0 = no changes, 2 = changes)" % (tag, rc))
    return out("%s-OK No changes." % tag)


def ledger():
    tag = "R1-FU7L"
    cm = "org/critical_paths/change_management"
    done = [f for f in (os.listdir(cm) if os.path.isdir(cm) else [])
            if "fidupl" in f.lower() and f.lower().endswith("deploy_completion.md")]
    sent = [f for f in (os.listdir("org/critical_paths/.open_deploys") if os.path.isdir("org/critical_paths/.open_deploys") else [])
            if "fidupl" in f.lower()]
    if not done:
        return out("%s-FAIL no NFRA_FIDUPL deploy_completion entry under %s" % (tag, cm))
    if sent:
        return out("%s-FAIL an open sentinel remains: %s" % (tag, ",".join(sent)))
    return out("%s-OK completion entries=%d, open sentinels=0" % (tag, len(done)))


def x1_run():
    tag = "R1-X1R"
    try:
        sys.path.insert(0, "lib")
        import boto3
        import opal_naming
        prefix = opal_naming.address("fidelity", "alongside", "bronze", "_runs", "00000000").rsplit("/00000000", 1)[0] + "/"
        m = re.match(r"s3://([^/]+)/(.+)$", prefix)
        s3 = boto3.client("s3", region_name="us-east-1")
        best = None
        for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=m.group(1), Prefix=m.group(2)):
            for o in pg.get("Contents", []):
                if o["Key"].endswith(".json") and "/run-" in o["Key"]:
                    if best is None or o["LastModified"] > best["LastModified"]:
                        best = o
        if best is None:
            return out("%s-FAIL no run record under %s" % (tag, prefix))
        rec = json.loads(s3.get_object(Bucket=m.group(1), Key=best["Key"])["Body"].read().decode("utf-8"))
        landed = [f for f in rec.get("files", []) if f.get("action") == "landed"]
        failed_files = [f for f in rec.get("files", []) if f.get("action") == "failed"]
        if (rec.get("source") != "automated" or rec.get("failure_class") or rec.get("failed_step")
                or rec.get("run_error") or failed_files or len(landed) != 6):
            return out("%s-FAIL source=%s failure_class=%s failed_step=%s failed_files=%d landed=%d" % (
                tag, rec.get("source"), rec.get("failure_class"), rec.get("failed_step"), len(failed_files), len(landed)))
        return out("%s-OK source=automated landed=6 content_date=%s" % (tag, rec.get("business_date_in_content")))
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def x1_recon():
    tag = "R1-X1G"
    root = "org/missions/D8/NFRA/NFRA_FIDUPL/deliverables"
    found = []
    for dp, _dn, fns in os.walk(root):
        for fn in fns:
            if fn == "FU-x-1_account_gnumber_read.md":
                found.append(os.path.join(dp, fn))
    if not found:
        return out("%s-FAIL no FU-x-1_account_gnumber_read.md under %s" % (tag, root))
    text = open(found[0], encoding="utf-8").read()
    m = re.search(r"columns=(\d+)", text)
    g = re.search(r"g_number_columns=(\[[^\]]*\])", text)
    if not m or not g:
        return out("%s-FAIL record lacks columns= or g_number_columns=" % tag)
    if re.search(r"G\d{8}", text):
        return out("%s-FAIL the record carries a G number value" % tag)
    return out("%s-OK columns=%s g_number_columns=%s" % (tag, m.group(1), g.group(1)))


def x1_probe():
    tag = "R1-X1P"
    root = "org/missions/D8/NFRA/NFRA_FIDUPL/deliverables"
    found = []
    for dp, _dn, fns in os.walk(root):
        for fn in fns:
            if fn == "FU-x-1_g_selector_probe.md":
                found.append(os.path.join(dp, fn))
    if not found:
        return out("%s-FAIL no FU-x-1_g_selector_probe.md under %s" % (tag, root))
    text = open(found[0], encoding="utf-8").read()
    m = re.search(r"list_narrows=(yes|no)", text)
    n = re.search(r"options=(\d+)", text)
    r = re.search(r"restored_starting_g=(yes|no)", text)
    if not m or not n or not r:
        return out("%s-FAIL record lacks list_narrows=, options= or restored_starting_g=" % tag)
    if r.group(1) != "yes":
        return out("%s-FAIL the starting G number was not restored" % tag)
    if re.search(r"G\d{8}", text):
        return out("%s-FAIL the record carries a G number value" % tag)
    return out("%s-OK list_narrows=%s options=%s restored_starting_g=yes" % (tag, m.group(1), n.group(1)))


def fu5_static():
    tag = "R1-FU5C"
    p = "%s/box/bootstrap.sh" % CF
    if not os.path.isfile(p):
        return out("%s-FAIL absent %s" % (tag, p))
    text = open(p, encoding="utf-8").read()
    m = re.search(r"amzn\)(.*?);;", text, re.S)
    if not m:
        return out("%s-FAIL no amzn branch" % tag)
    amzn = m.group(1)
    bad = []
    if "dnf install" not in amzn:
        bad.append("the amzn branch never runs dnf install")
    for lib in ("nss", "mesa-libgbm", "alsa-lib", "pango"):
        if lib not in amzn:
            bad.append("the amzn branch installs no %s" % lib)
    # --with-deps shells out to apt-get; it may appear only inside the ubuntu|debian branch of the case statement
    deb = re.search(r"ubuntu\|debian\)(.*?);;", text, re.S)
    deb_text = deb.group(1) if deb else ""

    def live_with_deps(blob):
        return [ln for ln in blob.splitlines() if "--with-deps" in ln and not ln.lstrip().startswith("#")]
    if len(live_with_deps(text)) > len(live_with_deps(deb_text)):
        bad.append("--with-deps is run outside the ubuntu|debian branch (apt-get is absent on amzn)")
    if "playwright install" not in text:
        bad.append("no playwright install")
    if bad:
        return out("%s-FAIL %s" % (tag, "; ".join(bad)))
    return out("%s-OK amzn branch installs browser libraries with dnf; --with-deps only in the ubuntu|debian branch" % tag)


def tf_venv():
    tag = "R1-FU6C"
    p = "%s/automation.tf" % TF_ROOT
    if not os.path.isfile(p):
        return out("%s-FAIL absent %s" % (tag, p))
    text = open(p, encoding="utf-8").read()
    if "/opt/fidelity-uploader/venv/bin/python" not in text:
        return out("%s-FAIL the automation never names the venv python" % tag)
    if re.search(r"(?<![/\w])python3\s+/opt/fidelity-uploader", text):
        return out("%s-FAIL the automation still runs system python3 on the wrapper" % tag)
    return out("%s-OK the automation runs the wrapper with /opt/fidelity-uploader/venv/bin/python" % tag)


def tf_plan_doc_only():
    tag = "R1-FU6P2"
    if not os.path.isdir(TF_ROOT):
        return out("%s-FAIL absent %s" % (tag, TF_ROOT))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "init", "-input=false", "-no-color"], 110)
    if rc != 0:
        return out("%s-FAIL init rc=%s" % (tag, rc))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "plan", "-input=false", "-no-color"], 115)
    if rc != 0 or "Plan: 0 to add, 1 to change, 0 to destroy." not in o:
        return out("%s-FAIL plan rc=%s %s" % (tag, rc, [x for x in o.splitlines() if x.startswith(("Plan:", "No changes"))][:1]))
    if "aws_ssm_document" not in o:
        return out("%s-FAIL the one change is not the automation document" % tag)
    return out("%s-OK Plan: 0 to add, 1 to change, 0 to destroy. (the automation document only)" % tag)


def box_live():
    tag = "R1-FU7B"
    try:
        import time

        import boto3
        rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "output", "-raw", "instance_id"], 60)
        iid = o.strip()
        if rc != 0 or not re.match(r"^i-[0-9a-f]+$", iid):
            return out("%s-FAIL no instance_id output (rc=%s)" % (tag, rc))
        py = ("import boto3, playwright; from playwright.sync_api import sync_playwright as sp; "
              "p = sp().start(); b = p.chromium.launch(); b.close(); p.stop(); print('FIDUPL-BOX-OK chromium=launched')")
        ssm = boto3.client("ssm", region_name="us-east-1")
        cid = ssm.send_command(InstanceIds=[iid], DocumentName="AWS-RunShellScript",
                               Parameters={"commands": ['/opt/fidelity-uploader/venv/bin/python -c "%s"' % py]})["Command"]["CommandId"]
        inv = {"Status": "Pending"}
        for _ in range(30):
            time.sleep(4)
            try:
                inv = ssm.get_command_invocation(CommandId=cid, InstanceId=iid)
            except Exception:  # noqa: BLE001 -- not registered yet
                continue
            if inv["Status"] in ("Success", "Failed", "TimedOut", "Cancelled"):
                break
        if inv["Status"] != "Success" or "FIDUPL-BOX-OK chromium=launched" not in inv.get("StandardOutputContent", ""):
            return out("%s-FAIL ssm status=%s" % (tag, inv["Status"]))
        return out("%s-OK chromium=launched" % tag)
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def box_headed():
    tag = "R1-FU10X"
    try:
        import time

        import boto3
        rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "output", "-raw", "instance_id"], 60)
        iid = o.strip()
        if rc != 0 or not re.match(r"^i-[0-9a-f]+$", iid):
            return out("%s-FAIL no instance_id output (rc=%s)" % (tag, rc))
        py = ("from playwright.sync_api import sync_playwright as sp; p = sp().start(); "
              "b = p.chromium.launch(channel='chrome', headless=False, args=['--no-sandbox']); b.close(); p.stop(); print('FIDUPL-BOX-OK headed=launched')")
        cmd = ("command -v Xvfb >/dev/null || { echo FIDUPL-BOX-NO-XVFB; exit 3; }; "
               "Xvfb :97 -screen 0 1440x900x24 >/dev/null 2>&1 & XP=$!; sleep 2; "
               "DISPLAY=:97 /opt/fidelity-uploader/venv/bin/python -c \"%s\"; RC=$?; kill $XP; exit $RC" % py)
        ssm = boto3.client("ssm", region_name="us-east-1")
        cid = ssm.send_command(InstanceIds=[iid], DocumentName="AWS-RunShellScript", Parameters={"commands": [cmd]})["Command"]["CommandId"]
        inv = {"Status": "Pending"}
        for _ in range(40):
            time.sleep(3)
            try:
                inv = ssm.get_command_invocation(CommandId=cid, InstanceId=iid)
            except Exception:  # noqa: BLE001 -- not registered yet
                continue
            if inv["Status"] in ("Success", "Failed", "TimedOut", "Cancelled"):
                break
        so = inv.get("StandardOutputContent", "")
        if inv["Status"] != "Success" or "FIDUPL-BOX-OK headed=launched" not in so:
            return out("%s-FAIL ssm status=%s%s" % (tag, inv["Status"], " (Xvfb not installed)" if "NO-XVFB" in so else ""))
        return out("%s-OK Xvfb present and a headed Google Chrome launches under it" % tag)
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def chrome_fallback_records():
    tag = "R1-FU11"
    d = "org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/"
    feas = d + "FU-s-11_feasibility.md"
    if not os.path.isfile(feas):
        return out("%s-FAIL absent %s" % (tag, feas))
    text = open(feas, encoding="utf-8").read()
    need = ["plugin_installable=", "claude_session_runs=", "display=", "needs="]
    miss = [k for k in need if k not in text]
    if miss:
        return out("%s-FAIL feasibility record lacks %s" % (tag, ",".join(miss)))
    return out("%s-OK feasibility record carries %d facts" % (tag, len(need)))


def chrome_fallback_signin():
    tag = "R1-FU11S"
    d = "org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/"
    rec = d + "FU-s-11_agent_signin_record.md"
    if not os.path.isfile(rec):
        return out("%s-FAIL absent %s" % (tag, rec))
    text = open(rec, encoding="utf-8").read()
    if "outcome=SIGNED_IN" not in text or "driver=cdp-remote" not in text or "headful=true" not in text:
        return out("%s-FAIL record does not show an agent-driven headful sign-in (outcome=SIGNED_IN, driver=cdp-remote, headful=true)" % tag)
    if re.search(r"G\d{8}", text):
        return out("%s-FAIL the record carries a G number" % tag)
    return out("%s-OK agent-driven headful sign-in recorded values-free" % tag)


def box_cdp():
    tag = "R1-FU11C"
    try:
        import time

        import boto3
        rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "output", "-raw", "instance_id"], 60)
        iid = o.strip()
        if rc != 0 or not re.match(r"^i-[0-9a-f]+$", iid):
            return out("%s-FAIL no instance_id output (rc=%s)" % (tag, rc))
        cmd = ("echo listeners=$(ss -ltnH | awk '{print $4}' | grep ':9222$' | tr '\\n' ' '); "
               "curl -s -m 5 http://127.0.0.1:9222/json/version | python3 -c \"import sys,json; d=json.load(sys.stdin); print('browser=' + d.get('Browser','?').split('/')[0])\"")
        ssm = boto3.client("ssm", region_name="us-east-1")
        cid = ssm.send_command(InstanceIds=[iid], DocumentName="AWS-RunShellScript", Parameters={"commands": [cmd]})["Command"]["CommandId"]
        inv = {"Status": "Pending"}
        for _ in range(30):
            time.sleep(3)
            try:
                inv = ssm.get_command_invocation(CommandId=cid, InstanceId=iid)
            except Exception:  # noqa: BLE001 -- not registered yet
                continue
            if inv["Status"] in ("Success", "Failed", "TimedOut", "Cancelled"):
                break
        so = inv.get("StandardOutputContent", "")
        listeners = [x for x in so.split("listeners=")[-1].split("\n")[0].split() if x]
        if inv["Status"] != "Success" or "browser=Chrome" not in so and "browser=HeadlessChrome" not in so:
            return out("%s-FAIL ssm status=%s; the CDP endpoint did not answer on 127.0.0.1:9222" % (tag, inv["Status"]))
        if not listeners or any(not x.startswith("127.0.0.1:") for x in listeners):
            return out("%s-FAIL the CDP port is not bound to 127.0.0.1 only: %s" % (tag, ",".join(listeners)))
        return out("%s-OK the box Chrome answers CDP on 127.0.0.1:9222 only" % tag)
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def _tf_out(name):
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "output", "-raw", name], 60)
    return rc, o.strip()


def autoshutdown_tag():
    tag = "R1-FU8T"
    try:
        import boto3
        rc, iid = _tf_out("instance_id")
        if rc != 0 or not re.match(r"^i-[0-9a-f]+$", iid):
            return out("%s-FAIL no instance_id output (rc=%s)" % (tag, rc))
        ec2 = boto3.client("ec2", region_name="us-east-1")
        tags = ec2.describe_instances(InstanceIds=[iid])["Reservations"][0]["Instances"][0].get("Tags", [])
        val = dict((t["Key"], t["Value"]) for t in tags).get("AutoShutdown")
        if val != "disabled":
            return out("%s-FAIL tag AutoShutdown=%s on %s" % (tag, val, iid))
        return out("%s-OK AutoShutdown=disabled on the instance" % tag)
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def automation_no_stop():
    tag = "R1-FU8D"
    try:
        import boto3
        rc, name = _tf_out("document_name")
        if rc != 0 or not name:
            return out("%s-FAIL no document_name output (rc=%s)" % (tag, rc))
        ssm = boto3.client("ssm", region_name="us-east-1")
        doc = ssm.get_document(Name=name)
        content = doc.get("Content", "")
        if "stopInstance" in content or '"stopped"' in content or "'stopped'" in content or re.search(r"DesiredState\W+stopped", content):
            return out("%s-FAIL the live document version %s still has a stop step" % (tag, doc.get("DocumentVersion")))
        if "changeInstanceState" not in content or "running" not in content:
            return out("%s-FAIL the live document lost its start step" % tag)
        return out("%s-OK no stop step in live document version %s" % (tag, doc.get("DocumentVersion")))
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def automation_role_describe_status():
    tag = "R1-FU8P"
    try:
        import boto3
        rc, arn = _tf_out("automation_role_arn")
        if rc != 0 or not arn.startswith("arn:aws:iam::"):
            return out("%s-FAIL no automation_role_arn output (rc=%s)" % (tag, rc))
        iam = boto3.client("iam", region_name="us-east-1")
        res = iam.simulate_principal_policy(PolicySourceArn=arn, ActionNames=["ec2:DescribeInstanceStatus"], ResourceArns=["*"])
        dec = [r["EvalDecision"] for r in res["EvaluationResults"]]
        if dec != ["allowed"]:
            return out("%s-FAIL ec2:DescribeInstanceStatus decision=%s" % (tag, dec))
        return out("%s-OK the automation role is allowed ec2:DescribeInstanceStatus" % tag)
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def box_md5():
    tag = "R1-FU9M"
    try:
        import hashlib
        import time

        import boto3
        names = ["signin.py", "signin_recon.py"]
        local = dict((n, hashlib.md5(open("%s/%s" % (CF, n), "rb").read()).hexdigest()) for n in names)
        rc, iid = _tf_out("instance_id")
        if rc != 0 or not re.match(r"^i-[0-9a-f]+$", iid):
            return out("%s-FAIL no instance_id output (rc=%s)" % (tag, rc))
        ssm = boto3.client("ssm", region_name="us-east-1")
        cmd = "md5sum " + " ".join("/opt/fidelity-uploader/%s" % n for n in names)
        cid = ssm.send_command(InstanceIds=[iid], DocumentName="AWS-RunShellScript", Parameters={"commands": [cmd]})["Command"]["CommandId"]
        inv = {"Status": "Pending"}
        for _ in range(30):
            time.sleep(3)
            try:
                inv = ssm.get_command_invocation(CommandId=cid, InstanceId=iid)
            except Exception:  # noqa: BLE001
                continue
            if inv["Status"] in ("Success", "Failed", "TimedOut", "Cancelled"):
                break
        if inv["Status"] != "Success":
            return out("%s-FAIL ssm status=%s (the box must be running)" % (tag, inv["Status"]))
        box = {}
        for ln in inv.get("StandardOutputContent", "").splitlines():
            parts = ln.split()
            if len(parts) == 2:
                box[parts[1].rsplit("/", 1)[-1]] = parts[0]
        bad = [n for n in names if box.get(n) != local[n]]
        if bad:
            return out("%s-FAIL box differs from the repo for %s" % (tag, ",".join(bad)))
        return out("%s-OK signin.py,signin_recon.py match the repo on the box" % tag)
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def box_md5_all():
    tag = "R1-FU10M"
    try:
        import hashlib
        import time

        import boto3
        names = sorted([f for f in os.listdir(CF) if f.endswith(".py")]
                       + ["box/" + f for f in os.listdir(CF + "/box") if f.endswith((".py", ".sh"))])
        local = dict((n, hashlib.md5(open("%s/%s" % (CF, n), "rb").read()).hexdigest()) for n in names)
        rc, iid = _tf_out("instance_id")
        if rc != 0 or not re.match(r"^i-[0-9a-f]+$", iid):
            return out("%s-FAIL no instance_id output (rc=%s)" % (tag, rc))
        ssm = boto3.client("ssm", region_name="us-east-1")
        cmd = "md5sum " + " ".join("/opt/fidelity-uploader/%s" % n for n in names)
        cid = ssm.send_command(InstanceIds=[iid], DocumentName="AWS-RunShellScript", Parameters={"commands": [cmd]})["Command"]["CommandId"]
        inv = {"Status": "Pending"}
        for _ in range(30):
            time.sleep(3)
            try:
                inv = ssm.get_command_invocation(CommandId=cid, InstanceId=iid)
            except Exception:  # noqa: BLE001
                continue
            if inv["Status"] in ("Success", "Failed", "TimedOut", "Cancelled"):
                break
        box = {}
        for ln in inv.get("StandardOutputContent", "").splitlines():
            parts = ln.split()
            if len(parts) == 2:
                box[parts[1].replace("/opt/fidelity-uploader/", "")] = parts[0]
        bad = [n for n in names if box.get(n) != local[n]]
        if inv["Status"] not in ("Success", "Failed") or bad:
            return out("%s-FAIL ssm status=%s; box differs from the repo for %s" % (tag, inv["Status"], ",".join(bad) or "none listed"))
        return out("%s-OK all %d shipped files match the repo on the box" % (tag, len(names)))
    except Exception as e:  # noqa: BLE001
        return out("%s-FAIL %s: %s" % (tag, type(e).__name__, str(e)[:120]))


def tf_plan_perg():
    tag = "R1-FR5P"
    if not os.path.isdir(TF_ROOT):
        return out("%s-FAIL absent %s" % (tag, TF_ROOT))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "init", "-input=false", "-no-color"], 110)
    if rc != 0:
        return out("%s-FAIL init rc=%s" % (tag, rc))
    rc, o = run(["terraform", "-chdir=%s" % TF_ROOT, "plan", "-input=false", "-no-color"], 115)
    m = re.search(r"Plan: (\d+) to add, (\d+) to change, 0 to destroy\.", o)
    if rc != 0 or not m or int(m.group(1)) != 1:
        return out("%s-FAIL plan rc=%s %s" % (tag, rc, [x for x in o.splitlines() if x.startswith(("Plan:", "No changes"))][:1]))
    added = re.findall(r"# (aws_[a-z_]+\.[\w\[\]\"-]+) will be created", o)
    if len(added) != 1 or not added[0].startswith("aws_secretsmanager_secret."):
        return out("%s-FAIL the one added resource is not a Secrets Manager secret: %s" % (tag, added))
    if "aws_secretsmanager_secret_version" in open("%s/perg.tf" % TF_ROOT, encoding="utf-8").read():
        return out("%s-FAIL perg.tf carries a secret VERSION (a value in state)" % tag)
    return out("%s-OK Plan: 1 to add, %s to change, 0 to destroy. (the per-G secret and the box role policy)" % (tag, m.group(2)))


CHECKS = {
    "fu1": lambda: tests("fu1"), "fu2a": lambda: tests("fu2a"), "fu2b": lambda: tests("fu2b"), "fu2c": lambda: tests("fu2c"), "fu2t": lambda: tests("fu2t"),
    "fu3": lambda: tests("fu3"), "fu3c": fu3_contract, "fu4": lambda: tests("fu4"), "fu4d": fu4_dry,
    "fu5": lambda: tests("fu5"), "fu5b": fu5_boot, "fu10x": box_headed, "fu11f": chrome_fallback_records, "fu11c": box_cdp, "fu11s": chrome_fallback_signin, "fu6v": tf_validate, "fu6g": tf_guard, "fu6p": tf_plan,
    "fu7a": tf_nochange, "fr1a": lambda: tests("fr1a"), "fr1b": lambda: tests("fr1b"), "fr2": lambda: tests("fr2"), "fr3": lambda: tests("fr3"), "fr4": lambda: tests("fr4"), "fr6": lambda: tests("fr6"), "fr5p": tf_plan_perg, "fu5c": fu5_static, "fu6c": tf_venv, "fu6p2": tf_plan_doc_only, "fu7b": box_live, "fu8t": autoshutdown_tag, "fu8d": automation_no_stop, "fu8p": automation_role_describe_status, "fu9m": box_md5, "fu10m": box_md5_all, "fu7l": ledger, "x1r": x1_run, "x1g": x1_recon, "x1p": x1_probe,
}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: fidupl_round_checks.py <%s>" % "|".join(sorted(CHECKS)))
        sys.exit(2)
    CHECKS[sys.argv[1]]()
