"""
Test the ingest function.
This test mocks the Redis and Elasticsearch connections,
the get_threads_to_process function, and the process_thread function.
It then calls the ingest function and asserts that the mocked functions
were called with the expected arguments and that the Redis database
was saved.
"""

import pytest
from unittest.mock import patch
import redis  # type: ignore
import elasticsearch  # type: ignore
import run_smat


@patch('run_smat.redis.Redis')
@patch('run_smat.elasticsearch.Elasticsearch')
@patch('run_smat.get_threads_to_process')
@patch('run_smat.process_thread')
def test_ingest(mock_process_thread, mock_get_threads, mock_elasticsearch, mock_redis):
    """Test the ingest function."""

    # Mock Redis and Elasticsearch instances
    mock_rdb = mock_redis.return_value
    mock_es = mock_elasticsearch.return_value

    # Mock the get_threads_to_process function to return a dictionary of threads
    mock_threads_to_process = {'thread1': 'last_mod1', 'thread2': 'last_mod2'}
    mock_get_threads.return_value = mock_threads_to_process

    # Call the ingest function
    run_smat.ingest()

    # Assert that Redis and Elasticsearch clients were instantiated
    mock_redis.assert_called_once_with(
        host=run_smat.REDIS_HOST, port=run_smat.REDIS_PORT, db=run_smat.REDIS_DB)
    mock_elasticsearch.assert_called_once_with(hosts=run_smat.ES_HOSTS)

    # Assert that get_threads_to_process was called with the Redis and Elasticsearch instances
    mock_get_threads.assert_called_once_with(rdb=mock_rdb, es=mock_es)

    # Assert that process_thread was called for each thread in the dictionary
    assert mock_process_thread.call_count == len(mock_threads_to_process)
    mock_process_thread.assert_any_call(
        thread_unique='thread1', last_mod='last_mod1', rdb=mock_rdb, es=mock_es)
    mock_process_thread.assert_any_call(
        thread_unique='thread2', last_mod='last_mod2', rdb=mock_rdb, es=mock_es)

    # Assert that rdb.bgsave() was called
    mock_rdb.bgsave.assert_called_once()
