from unittest.mock import patch
from download import log_event


@patch("logging.getLogger")
def test_log_success(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("Anna", "success")

    mock_logger.info.assert_called_once_with(
        "Login event - Username: Anna, Status: success"
    )


@patch("logging.getLogger")
def test_log_expired(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("Anna", "expired")

    mock_logger.warning.assert_called_once_with(
        "Login event - Username: Anna, Status: expired"
    )

@patch("logging.getLogger")
def test_log_failed(mock_get_logger):
    mock_logger = mock_get_logger.return_value

    log_event("Anna", "failed")

    mock_logger.error.assert_called_once_with(
        "Login event - Username: Anna, Status: failed"
    )