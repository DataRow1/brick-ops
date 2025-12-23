"""Module for job management operations."""

from db_ops.core.adapters.databricks import DatabricksJobsAdapter
from db_ops.core.models import Job
from db_ops.core.selectors import JobSelector


def find_jobs(adapter: DatabricksJobsAdapter, pattern: str) -> list[Job]:
    """Find jobs matching the given regex pattern."""
    return adapter.find_jobs_by_regex(pattern)


def select_jobs(
    adapter: DatabricksJobsAdapter,
    selector: JobSelector,
) -> list[Job]:
    """Select jobs matching the given selector."""
    return [job for job in adapter.find_all_jobs() if selector.matches(job)]
