"""Offline COO review of the immutable R9 Price handback; never writes AWS."""
import argparse
import contextlib
import copy
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

PIN = '1b6cd9d4e026570ad3fccb7f7fa89719a0f8164e'
PATCH_HASH = 'c823c390ba2896fe4c472b3d4a03b0a32fb439f475fa9c4f498f97d03dab65ce'
HOME = Path(__file__).resolve().parent


class MemoryTable:
    def __init__(self):
        self.items = {}
        self.fail_pointer = False

    def Table(self, name):  # noqa: N802 -- boto3 interface
        return self

    def batch_writer(self):
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def put_item(self, Item):  # noqa: N803 -- boto3 interface
        if self.fail_pointer and Item['ticker'] == '_CURRENT':
            raise RuntimeError('injected pointer write failure')
        self.items[(Item['axis_date'], Item['ticker'])] = copy.deepcopy(Item)


def identity(tickers, **kwargs):
    return ({ticker: {'security_key': ticker + '_Equity', 'identity_status': 'MEASURED'}
             for ticker in tickers},
            {'tickers_resolved': len(tickers), 'tickers_considered': len(tickers),
             'source': 'in-memory review fixture', 'fallback_reason': None})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate-root', required=True)
    root = Path(parser.parse_args().candidate_root).resolve()
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=root)
    assert git('rev-parse', 'HEAD').decode().strip() == PIN
    delta = git('diff', PIN + '^', PIN, '--', 'lib/research/price')
    assert hashlib.sha256(delta).hexdigest() == PATCH_HASH
    assert delta == git('cat-file', 'blob', '5969b4bc5e12feb660c946399cf1436c77132321')
    sys.path.insert(0, str(root))
    from lib.research.price import backfill_legacy_generation as cli
    from lib.research.metrics import generation_writer as writer
    assert Path(cli.__file__).resolve().is_relative_to(root)
    date = '2026-09-23'
    axes = cli.axes_for_subject('PRICE')
    checks = []

    def retained(axis, *args, **kwargs):
        return [{'ticker': 'NEW', 'rank_sort': '00001', 'rank': 1, 'score': 3.0,
                 'axis': axis, 'as_of_date': date}]

    def seeded():
        table = MemoryTable()
        for axis in axes:
            prior = writer.build_generation(axis, date, [{'ticker': 'OLD', 'score': 1.0}],
                                            'prior', 'original-vintage', state=writer.STATE_COMPLETE)
            writer.default_write_generation(prior, resource=table)
        return table

    def publish(table):
        def write(generation, table_name):
            return writer.default_write_generation(generation, table_name, resource=table)
        return write

    # An unexpected external call fails this review rather than reaching AWS.
    with patch('boto3.client', side_effect=AssertionError('external client forbidden')), \
         patch('boto3.resource', side_effect=AssertionError('external resource forbidden')), \
         patch.object(cli, 'build_identity_index', side_effect=identity):
        with patch.object(cli, 'read_crossed_partition', side_effect=retained):
            table = seeded()
            result = cli.republish_crossed_generation(date, write_fn=publish(table), run_id='positive')
            assert all(p['state'] == 'COMPLETE' and p['pointer_written'] for p in result['products'])
            assert all(table.items[(axis + '#' + date, '_CURRENT')]['row_count'] == 1 for axis in axes)
            checks.append('retained scored members publish explicit COMPLETE')

        with patch.object(cli, 'read_crossed_partition', return_value=[]):
            table = seeded()
            prior = copy.deepcopy(table.items)
            result = cli.republish_crossed_generation(date, write_fn=publish(table), run_id='absent')
            assert all(p['state'] == 'FAILED' and p['pointer'] is None
                       and p['reason_code'] == 'NO_RETAINED_MEMBERS' for p in result['products'])
            assert all(table.items[key] == value for key, value in prior.items())
            added = [v for k, v in table.items.items() if k not in prior]
            assert len(added) == len(axes)
            assert all(v['record_type'] == 'generation_failed_marker' for v in added)
            checks.append('absent retained members preserve all prior bytes and add only failure markers')
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = cli.main(['--as-of', date, '--republish-crossed', '--dry-run'])
            assert code == 1 and 'NO_RETAINED_MEMBERS' in output.getvalue()
            assert 'NO LIVE WRITE' in output.getvalue()
            checks.append('crossed dry-run reports failure with nonzero exit')

        with patch.object(cli, 'read_crossed_partition', side_effect=retained):
            table = seeded()
            prior = copy.deepcopy(table.items)
            table.fail_pointer = True
            result = cli.republish_crossed_generation(date, write_fn=publish(table), run_id='writefail')
            assert all(p['state'] == 'FAILED' and p['pointer'] is None
                       and not p['pointer_written'] and p['failure_reason'] for p in result['products'])
            assert all(table.items[key] == value for key, value in prior.items())
            checks.append('crossed pointer failure clears draft pointers and preserves prior bytes')

        legacy = [{'ticker': 'NEW', 'px_start_date': '2026-09-01', 'px_start': 10,
                   'px_end_date': date, 'px_end': 20}]
        table = seeded()
        prior = copy.deepcopy(table.items)
        table.fail_pointer = True
        with patch.object(cli, 'read_legacy_partition', return_value=legacy), \
             patch.object(cli, 'default_write_generation', side_effect=publish(table)):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = cli.main(['--as-of', date])
        assert code == 1 and 'POINTER ABSENT' in output.getvalue() and 'RECEIPT' in output.getvalue()
        assert all(table.items[key] == value for key, value in prior.items())
        checks.append('legacy CLI handles nullable failed pointers without replacing prior data')

    result = {'candidate_pin': PIN, 'price_patch_sha256': PATCH_HASH,
              'matches_frozen_blob': True, 'external_clients_forbidden': True,
              'controls_passed': checks, 'live_acceptance': 'NOT_EVALUATED', 'deployment': 'NOT_PERFORMED'}
    (HOME / 'PRICE_HANDBACK_REVIEW.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
