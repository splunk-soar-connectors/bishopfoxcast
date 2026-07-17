# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pathlib import Path


CONNECTOR_SOURCE = Path("bishopfox_connector.py").read_text()


def test_finding_and_subject_uids_are_encoded_as_path_segments():
    assert 'urlparse.quote(str(value), safe="")' in CONNECTOR_SOURCE
    assert CONNECTOR_SOURCE.count("_quote_path_segment(finding_uid)") == 3
    assert CONNECTOR_SOURCE.count("_quote_path_segment(subject_uid)") == 3


def test_raw_uids_are_not_interpolated_into_update_paths():
    assert 'f"/findings/{finding_uid}' not in CONNECTOR_SOURCE
    assert "/subjects/{subject_uid}" not in CONNECTOR_SOURCE
