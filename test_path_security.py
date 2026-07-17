from pathlib import Path


CONNECTOR_SOURCE = Path("bishopfox_connector.py").read_text()


def test_finding_and_subject_uids_are_encoded_as_path_segments():
    assert 'urlparse.quote(str(value), safe="")' in CONNECTOR_SOURCE
    assert CONNECTOR_SOURCE.count("_quote_path_segment(finding_uid)") == 3
    assert CONNECTOR_SOURCE.count("_quote_path_segment(subject_uid)") == 3


def test_raw_uids_are_not_interpolated_into_update_paths():
    assert 'f"/findings/{finding_uid}' not in CONNECTOR_SOURCE
    assert "/subjects/{subject_uid}" not in CONNECTOR_SOURCE
