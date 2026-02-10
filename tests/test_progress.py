from dbops.cli.common.progress import _display_job_label, _run_display_sort_key
from dbops.core.jobs import JobRun


def test_display_job_label_name_before_id_and_aligned():
    labels = {
        1: _display_job_label(1, {1: "alpha_job", 2: "beta"}, name_width=12),
        2: _display_job_label(2, {1: "alpha_job", 2: "beta"}, name_width=12),
    }

    assert labels[1].startswith("alpha_job")
    assert labels[2].startswith("beta")
    assert labels[1].index("(id: ") == labels[2].index("(id: ")


def test_display_job_label_falls_back_to_id_when_name_missing():
    assert _display_job_label(42, {1: "alpha"}, name_width=10) == "42"


def test_run_display_sort_key_uses_job_name_then_run_id():
    runs = [
        JobRun(run_id=30, job_id=3),
        JobRun(run_id=10, job_id=1),
        JobRun(run_id=20, job_id=2),
    ]
    names = {1: "beta", 2: "alpha", 3: "alpha"}

    sorted_runs = sorted(runs, key=lambda run: _run_display_sort_key(run, names))
    assert [(r.job_id, r.run_id) for r in sorted_runs] == [(2, 20), (3, 30), (1, 10)]
