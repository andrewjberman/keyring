#!/usr/bin/env python3
"""Round 23 CT-am-1: intake_receive.py classes a COLOURED import error as the missing dependency it names, and every other
failure stays failed. Standard library only; no network; no install; every child is a fake.

Arms run over the pure classification function (classify_import), the ANSI strip, and the child environments that
run_import and run_pip build (captured through a patched subprocess.run, restored afterwards).

LAST line: RECEIVE-COLOR arms=<k>/<n> ok=<True|False>"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
INTAKE = os.path.join(ROOT, "org", "devices", "intake")
sys.path.insert(0, INTAKE)
import intake_receive as ir  # noqa: E402

ESC = "\x1b"
DUCK = "adbc_driver_duckdb"
OWN = ["duckdb"]  # the pack's own top-level module for the duckdb wheel in this arm set

PLAIN_MISSING = ("Traceback (most recent call last):\n"
                 "  File \"<string>\", line 1, in <module>\n"
                 "ModuleNotFoundError: No module named '%s'\n" % DUCK)
# the shapes a Python 3.14 child prints with FORCE_COLOR=3 (colour around the class name and around the quoted name)
COLOUR_MISSING_1 = (ESC + "[1;35mModuleNotFoundError" + ESC + "[0m: No module named '" + ESC + "[35m" + DUCK + ESC
                    + "[0m'")
COLOUR_MISSING_2 = (ESC + "[1m" + ESC + "[35mModuleNotFoundError" + ESC + "[0m: No module named '" + ESC + "[35m" + DUCK
                    + ESC + "[0m'")
COLOUR_MISSING_3 = ("Traceback (most recent call last):\n"
                    + "  File " + ESC + "[35m\"<string>\"" + ESC + "[0m, line " + ESC + "[35m1" + ESC + "[0m, in "
                    + ESC + "[35m<module>" + ESC + "[0m\n" + COLOUR_MISSING_1 + "\n")
COLOUR_OTHER_IMPORT = (ESC + "[1;35mImportError" + ESC + "[0m: cannot import name '" + ESC + "[35mx" + ESC
                       + "[0m' from '" + ESC + "[35mduckdb" + ESC + "[0m'\n")
COLOUR_SYNTAX = ESC + "[1;35mSyntaxError" + ESC + "[0m: invalid syntax\n"
COLOUR_OWN_SUB = (ESC + "[1;35mModuleNotFoundError" + ESC + "[0m: No module named '" + ESC + "[35mduckdb.sub" + ESC
                  + "[0m'\n")
COLOUR_OWN = (ESC + "[1;35mModuleNotFoundError" + ESC + "[0m: No module named '" + ESC + "[35mduckdb" + ESC + "[0m'\n")

ARMS = []


def arm(label, fn):
    try:
        ok = bool(fn())
    except Exception as exc:  # noqa: BLE001 - a harness reports every arm, including an arm that raised
        print("ARM-ERROR: %s: %s: %s" % (label, type(exc).__name__, exc))
        ok = False
    ARMS.append((label, ok))
    print("ARM %s: %s" % (label, "PASS" if ok else "FAIL"))


def missing_class(stderr):
    cls, missing, _ = ir.classify_import(1, stderr, OWN)
    return cls == "import_missing_dep" and missing == DUCK


def is_failed(stderr):
    return ir.classify_import(1, stderr, OWN)[0] == "failed"


def run_with_fake_subprocess(stderr, fn):
    """Calls fn() with subprocess.run replaced by a fake that returns rc=1 and the given stderr. Returns (fn result, env seen)."""
    seen = {}
    real = subprocess.run

    def fake(cmd, **kw):
        seen["env"] = kw.get("env")
        seen["cmd"] = list(cmd)
        return subprocess.CompletedProcess(cmd, 1, "", stderr)

    subprocess.run = fake
    try:
        result = fn()
    finally:
        subprocess.run = real
    return result, seen.get("env") or {}


def pins_ok(env):
    return env.get("PYTHON_COLORS") == "0" and env.get("NO_COLOR") == "1" and "FORCE_COLOR" not in env


def env_with_force_colour(fn):
    old = os.environ.get("FORCE_COLOR")
    os.environ["FORCE_COLOR"] = "3"
    try:
        return fn()
    finally:
        if old is None:
            os.environ.pop("FORCE_COLOR", None)
        else:
            os.environ["FORCE_COLOR"] = old


# (a) plain text missing dependency
arm("a_plain_missing_dep", lambda: missing_class(PLAIN_MISSING)
    and ir.classify_import(1, PLAIN_MISSING, OWN)[1] == DUCK)
# (b) the same message wrapped in colour, three real shapes
arm("b1_colour_class_and_name", lambda: missing_class(COLOUR_MISSING_1))
arm("b2_colour_bold_then_class", lambda: missing_class(COLOUR_MISSING_2))
arm("b3_colour_traceback_lines", lambda: missing_class(COLOUR_MISSING_3))
# the strip itself: CSI and OSC forms are removed and the plain message is what is left
arm("b4_strip_leaves_plain_message",
    lambda: ir.strip_ansi(COLOUR_MISSING_1) == "ModuleNotFoundError: No module named '%s'" % DUCK)
arm("b5_strip_removes_osc_title",
    lambda: ir.strip_ansi(ESC + "]0;title" + "\x07" + "ModuleNotFoundError: x") == "ModuleNotFoundError: x")
# (c) a different failure, coloured, stays failed
arm("c1_colour_import_error_is_failed", lambda: is_failed(COLOUR_OTHER_IMPORT))
arm("c2_colour_syntax_error_is_failed", lambda: is_failed(COLOUR_SYNTAX))
# (d) the module named IS one of the pack's own modules: failed, coloured or plain
arm("d1_colour_own_module_is_failed", lambda: is_failed(COLOUR_OWN))
arm("d2_colour_own_submodule_is_failed", lambda: is_failed(COLOUR_OWN_SUB))
# (e) the child environments carry plain output and no FORCE_COLOR
arm("e1_import_env_pinned", lambda: env_with_force_colour(lambda: pins_ok(ir.build_import_env())))
arm("e2_pip_env_pinned", lambda: env_with_force_colour(lambda: pins_ok(ir.build_child_env())))
arm("e3_run_import_passes_pinned_env", lambda: env_with_force_colour(lambda: pins_ok(
    run_with_fake_subprocess(COLOUR_MISSING_1, lambda: ir.run_import("unused-target", DUCK, OWN))[1])))
arm("e4_run_import_still_classes_coloured_stderr", lambda: env_with_force_colour(lambda: (
    run_with_fake_subprocess(COLOUR_MISSING_1, lambda: ir.run_import("unused-target", DUCK, OWN))[0]
    .get("class") == "import_missing_dep")))
arm("e5_run_pip_passes_pinned_env", lambda: env_with_force_colour(lambda: pins_ok(
    run_with_fake_subprocess(PLAIN_MISSING, lambda: ir.run_pip(["python", "-m", "pip", "list"]))[1])))

passed = sum(1 for _, ok in ARMS if ok)
total = len(ARMS)
ok = passed == total and total > 0
print("RECEIVE-COLOR arms=%d/%d ok=%s" % (passed, total, ok))
sys.exit(0 if ok else 1)
