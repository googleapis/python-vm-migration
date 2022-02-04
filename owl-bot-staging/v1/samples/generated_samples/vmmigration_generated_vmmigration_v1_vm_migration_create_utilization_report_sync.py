# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateUtilizationReport
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vm-migration


# [START vmmigration_generated_vmmigration_v1_VmMigration_CreateUtilizationReport_sync]
from google.cloud import vmmigration_v1


def sample_create_utilization_report():
    # Create a client
    client = vmmigration_v1.VmMigrationClient()

    # Initialize request argument(s)
    request = vmmigration_v1.CreateUtilizationReportRequest(
        parent="parent_value",
        utilization_report_id="utilization_report_id_value",
    )

    # Make the request
    operation = client.create_utilization_report(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END vmmigration_generated_vmmigration_v1_VmMigration_CreateUtilizationReport_sync]
